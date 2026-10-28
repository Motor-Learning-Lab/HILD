"""Behavioral tests for the preview-first fresh-HILD installer."""

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

INSTALLER = Path(__file__).parents[1] / "HILD/scripts/install_hild.py"
REQUIRED = (
    "HILD/README.md",
    "HILD/process.md",
    "HILD/agent-setup.md",
    "HILD/scripts/session_context.sh",
    "HILD/scripts/wiki_status.py",
    ".agents/skills/hild-scope/SKILL.md",
    ".agents/skills/hild-understood/new-wiki.md",
)


def git(repo, *args):
    subprocess.run(
        ["git", "-C", str(repo), "-c", "user.name=Test User",
         "-c", "user.email=test@example.org", *args],
        check=True, capture_output=True, text=True,
    )


def init_repo(path):
    path.mkdir()
    git(path, "init", "-q")
    (path / "README.md").write_text("# New project\n", encoding="utf-8")
    git(path, "add", "README.md")
    git(path, "commit", "-qm", "Initial project")


@pytest.fixture
def repositories(tmp_path):
    source, target = tmp_path / "source", tmp_path / "target"
    init_repo(source)
    init_repo(target)
    for rel in REQUIRED:
        path = source / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"Source content for {rel}\n", encoding="utf-8")
    for agent, template in (
        ("claude", "claude-settings.json"),
        ("codex", "codex-hooks.json"),
        ("copilot", "copilot-hooks.json"),
    ):
        path = source / "HILD/templates" / template
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({"agent": agent}), encoding="utf-8")
    path = source / "HILD/scripts/install_hild.py"
    shutil.copyfile(INSTALLER, path)
    (source / "HILD/templates/scope-issue.md").write_text("# Scope\n")
    git(source, "add", "-A")
    git(source, "commit", "-qm", "Source package")
    return source, target


def install(source, target, *options):
    return subprocess.run(
        [sys.executable, str(INSTALLER),
         "--source", str(source), "--target", str(target), *options],
        capture_output=True, text=True,
    )


def test_preview_does_not_write_anything(repositories):
    source, target = repositories

    def working_tree_paths():
        # Git may create/remove internal maintenance locks during read-only
        # commands. The install preview promises no project file changes.
        return sorted(
            path.relative_to(target)
            for path in target.rglob("*")
            if ".git" not in path.relative_to(target).parts
        )

    before = working_tree_paths()
    result = install(source, target, "--agents", "codex")
    assert result.returncode == 0, result.stderr
    assert "READ-ONLY" in result.stdout
    assert ".codex/hooks.json" in result.stdout
    assert ".claude/settings.json" not in result.stdout
    assert working_tree_paths() == before


def test_single_agent_apply_verify_and_changed_file_detection(repositories):
    source, target = repositories
    result = install(source, target, "--agents", "codex", "--apply")
    assert result.returncode == 0, result.stderr
    assert (target / ".codex/hooks.json").is_file()
    assert not (target / ".claude").exists()
    info = json.loads((target / "HILD/installation.json").read_text())
    assert info["agents"] == ["codex"]
    # Paths in a durable installation record must work on Linux and Windows.
    assert all(chr(92) not in name for name in info["files"])
    assert "HILD/scripts/install_hild.py" in info["files"]
    assert ".agents/skills/hild-scope/SKILL.md" in info["files"]
    assert info["source_repository"] is None  # synthetic source has no remote
    assert info["source_commit"]
    assert install(source, target, "--verify").returncode == 0

    (target / "HILD/process.md").write_text("Changed locally\n")
    verify = install(source, target, "--verify")
    assert verify.returncode == 0
    assert "LOCAL CHANGE (preserved): HILD/process.md" in verify.stdout


def test_claude_preview_and_apply_refuse_disabled_git_symlinks(repositories):
    """The first created link may work, while a subsequent Git checkout destroys it."""
    source, target = repositories
    git(target, "config", "core.symlinks", "false")
    for options in ((), ("--apply",)):
        result = install(source, target, "--agents", "claude", *options)
        assert result.returncode == 2
        assert "core.symlinks=true" in result.stderr
        assert not (target / "HILD").exists()
    # Other agents do not require the Claude discovery link.
    assert install(source, target, "--agents", "codex").returncode == 0


def test_claude_verify_detects_checkout_risk_after_successful_install(repositories):
    source, target = repositories
    git(target, "config", "core.symlinks", "true")
    result = install(source, target, "--agents", "claude", "--apply")
    assert result.returncode == 0, result.stderr + result.stdout
    assert (target / ".claude/skills").is_symlink()

    # Reproduces the live pilot: the link still works until Git checks out
    # a commit, but the repository configuration cannot preserve it.
    git(target, "config", "core.symlinks", "false")
    result = install(source, target, "--verify")
    assert result.returncode == 1
    assert "core.symlinks=true" in result.stdout


def test_default_installs_all_adapters_without_duplicate_skills(repositories):
    source, target = repositories
    git(target, "config", "core.symlinks", "true")
    result = install(source, target, "--apply")
    assert result.returncode == 0, result.stderr
    assert (target / ".claude/skills").is_symlink()
    assert (target / ".claude/skills").readlink() == Path("../.agents/skills")
    assert (target / ".claude/settings.json").exists()
    assert (target / ".codex/hooks.json").exists()
    assert (target / ".github/hooks/hild.json").exists()
    # Inert documentation templates may be available for any agent;
    # only selected hooks and discovery files are activated.
    for sample in ("claude-settings.json", "codex-hooks.json", "copilot-hooks.json"):
        assert (target / "HILD/templates" / sample).is_file()
    assert not (target / ".claude/skills/hild-scope").is_symlink()
    assert install(source, target, "--verify").returncode == 0


def test_existing_path_blocks_installation_without_partial_writes(repositories):
    source, target = repositories
    (target / "AGENTS.md").write_text("# Existing researcher rules\n")
    git(target, "add", "AGENTS.md")
    git(target, "commit", "-qm", "Existing agent instructions")
    result = install(source, target, "--apply")
    assert result.returncode == 2
    assert "AGENTS.md" in result.stderr
    assert not (target / "HILD").exists()
    assert (target / "AGENTS.md").read_text() == "# Existing researcher rules\n"


def test_uncommitted_target_refused_even_for_preview(repositories):
    source, target = repositories
    (target / "untracked.txt").write_text("Do not touch")
    result = install(source, target)
    assert result.returncode == 2
    assert "uncommitted" in result.stderr
    assert not (target / "HILD").exists()


def test_missing_source_file_refuses_installation(repositories):
    source, target = repositories
    (source / "HILD/scripts/wiki_status.py").unlink()
    git(source, "add", "-A")
    git(source, "commit", "-qm", "Source version missing wiki checker")
    result = install(source, target, "--apply")
    assert result.returncode == 2
    assert "incomplete" in result.stderr
    assert not (target / "HILD").exists()


def test_reapplying_never_overwrites_local_changes(repositories):
    source, target = repositories
    assert install(source, target, "--agents", "copilot", "--apply").returncode == 0
    (target / "HILD/plan.md").write_text("Research plan edited by a human\n")
    second = install(source, target, "--agents", "copilot", "--apply")
    assert second.returncode == 2
    assert (target / "HILD/plan.md").read_text() == "Research plan edited by a human\n"


def test_existing_gitignore_that_excludes_wiki_is_preserved(repositories):
    source, target = repositories
    ignore = target / ".gitignore"
    ignore.write_text("*.tmp\n/wiki/\n", encoding="utf-8")
    git(target, "add", ".gitignore")
    git(target, "commit", "-qm", "Existing ignored wiki checkout")
    before = ignore.read_bytes()
    result = install(source, target, "--agents", "codex", "--apply")
    assert result.returncode == 0, result.stderr
    assert ignore.read_bytes() == before
    info = json.loads((target / "HILD/installation.json").read_text())
    assert ".gitignore" not in info["files"]


def test_existing_gitignore_without_wiki_rule_blocks_installation(repositories):
    source, target = repositories
    ignore = target / ".gitignore"
    ignore.write_text("*.tmp\n", encoding="utf-8")
    git(target, "add", ".gitignore")
    git(target, "commit", "-qm", "Existing project ignores")
    result = install(source, target, "--apply")
    assert result.returncode == 2
    assert "wiki/" in result.stderr
    assert ignore.read_text() == "*.tmp\n"
    assert not (target / "HILD").exists()


def test_uncommitted_source_is_refused(repositories):
    source, target = repositories
    (source / "untracked-source-file.txt").write_text("Pending upstream edit")
    result = install(source, target, "--apply")
    assert result.returncode == 2
    assert "source has uncommitted changes" in result.stderr
    assert not (target / "HILD").exists()


def test_existing_parent_symlink_cannot_redirect_installer(repositories):
    source, target = repositories
    outside = target.parent / "outside"
    outside.mkdir()
    (target / ".gitignore").write_text("/wiki/\n/.agents\n")
    git(target, "add", ".gitignore")
    git(target, "commit", "-qm", "Ignore wiki and external-directory link")
    (target / ".agents").symlink_to(outside, target_is_directory=True)
    result = install(source, target, "--apply")
    assert result.returncode == 2
    assert "redirect" in result.stderr
    assert not (outside / "skills").exists()
    assert not (target / "HILD").exists()


def test_existing_scientific_files_require_a_different_scope(repositories):
    source, target = repositories
    (target / "model.py").write_text("print('science')\n")
    git(target, "add", "model.py")
    git(target, "commit", "-qm", "Existing scientific work")
    result = install(source, target, "--apply")
    assert result.returncode == 2
    assert "existing-repository integration scope" in result.stderr
    assert not (target / "HILD").exists()



def test_missing_installed_file_is_an_integrity_failure(repositories):
    source, target = repositories
    assert install(source, target, "--agents", "codex", "--apply").returncode == 0
    (target / "HILD/process.md").unlink()
    result = install(source, target, "--verify")
    assert result.returncode == 1
    assert "missing expected file" in result.stdout


def test_corrupt_selected_hook_is_an_integrity_failure(repositories):
    source, target = repositories
    assert install(source, target, "--agents", "codex", "--apply").returncode == 0
    (target / ".codex/hooks.json").write_text("{invalid")
    result = install(source, target, "--verify")
    assert result.returncode == 1
    assert "invalid JSON" in result.stdout


def test_full_hild_checkout_when_tooling_pr_is_merged(tmp_path):
    """Exercise the complete, real HILD source now that PR #6 is on main."""
    checkout = Path(__file__).parents[1]
    missing = [rel for rel in REQUIRED if not (checkout / rel).is_file()]
    for template in ("claude-settings.json", "codex-hooks.json", "copilot-hooks.json"):
        rel = "HILD/templates/" + template
        if not (checkout / rel).is_file():
            missing.append(rel)
    assert not missing, "Full HILD source is incomplete: " + ", ".join(missing)

    source = tmp_path / "full-hild-source"
    shutil.copytree(
        checkout, source,
        ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache", "*.pyc"),
    )
    target = tmp_path / "fresh-repo"
    init_repo(target)
    git(target, "config", "core.symlinks", "true")
    installed = install(source, target, "--apply")
    assert installed.returncode == 0, installed.stderr
    assert (target / "HILD/scripts/wiki_status.py").exists()
    assert (target / "HILD/agent-setup.md").exists()
    assert (target / ".agents/skills/hild-understood/new-wiki.md").exists()
    # Optional companions must travel with the shared skills; a file in
    # upstream HILD is not enough if the host installer omits it.
    access_companion = ".agents/skills/hild-integrate/github-access.md"
    assert (target / access_companion).is_file()
    manifest = json.loads((target / "HILD/installation.json").read_text())
    assert access_companion in manifest["files"]
    assert install(source, target, "--verify").returncode == 0



def test_broken_local_link_in_installed_process_fails_verification(repositories):
    source, target = repositories
    process = source / "HILD/process.md"
    process.write_text("# HILD\n\n[Missing local page](unknown-document.md)\n")
    git(source, "add", "-A")
    git(source, "commit", "-qm", "Broken source link to test integrity")
    applied = install(source, target, "--agents", "codex", "--apply")
    assert applied.returncode == 1
    assert "broken local link" in applied.stdout
    assert "New files remain in place for inspection" in applied.stderr
    assert (target / "HILD/process.md").exists()


@pytest.mark.skipif(sys.platform != "win32", reason="Windows-specific symlink test")
def test_windows_claude_skill_link_is_working_and_portable(repositories):
    """A native Windows link must work locally and in a Git checkout on POSIX."""
    source, target = repositories
    git(target, "config", "core.symlinks", "true")
    applied = install(source, target, "--agents", "claude", "--apply")
    assert applied.returncode == 0, applied.stderr + applied.stdout
    link = target / ".claude/skills"
    assert link.is_symlink()
    assert (link / "hild-scope/SKILL.md").is_file()
    assert install(source, target, "--verify").returncode == 0

    # The blob committed to Git must also be a cross-platform POSIX link.
    git(target, "add", "-A")
    blob = subprocess.run(
        ["git", "-C", str(target), "show", ":.claude/skills"],
        check=True, capture_output=True, text=True,
    ).stdout
    assert blob == "../.agents/skills"

    # Recreate the user's actual next step: a fresh Windows Git checkout.
    git(target, "commit", "-qm", "Install HILD")
    cloned = target.parent / "roundtrip"
    subprocess.run(
        ["git", "-c", "core.symlinks=true", "clone", "-q",
         str(target), str(cloned)],
        check=True, capture_output=True, text=True,
    )
    assert (cloned / ".claude/skills").is_symlink()
    assert (cloned / ".claude/skills/hild-scope/SKILL.md").is_file()

    # Reproduce the actual failure: Git with symlinks disabled materializes
    # the same committed link as a plain text file in a new Windows clone.
    disabled = target.parent / "roundtrip-disabled"
    subprocess.run(
        ["git", "clone", "-q", "-c", "core.symlinks=false",
         str(target), str(disabled)],
        check=True, capture_output=True, text=True,
    )
    assert not (disabled / ".claude/skills").is_symlink()
    assert (disabled / ".claude/skills").is_file()
    failure = install(source, disabled, "--verify")
    assert failure.returncode == 1
    assert "core.symlinks=true" in failure.stdout
