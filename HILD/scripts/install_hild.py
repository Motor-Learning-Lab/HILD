#!/usr/bin/env python3
"""Plan, install, or verify HILD in a clean, newly initialized Git repository.

The default is read-only. Use --apply only after a researcher has explicitly
approved the installation scope. Existing files are never overwritten.
"""

import argparse
import hashlib
import json
import re
import subprocess
from urllib.parse import unquote
import sys
from datetime import date
from pathlib import Path

AGENTS = ("claude", "codex", "copilot")
ADAPTERS = {
    "claude": ("HILD/templates/claude-settings.json", ".claude/settings.json"),
    "codex": ("HILD/templates/codex-hooks.json", ".codex/hooks.json"),
    "copilot": ("HILD/templates/copilot-hooks.json", ".github/hooks/hild.json"),
}
REQUIRED = (
    "HILD/README.md",
    "HILD/process.md",
    "HILD/agent-setup.md",
    "HILD/scripts/session_context.sh",
    "HILD/scripts/wiki_status.py",
    ".agents/skills/hild-scope/SKILL.md",
    ".agents/skills/hild-understood/new-wiki.md",
)
MANIFEST = "HILD/installation.json"


class InstallationError(Exception):
    """An installation cannot proceed without changing existing material."""


def git(repo, *args):
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True, text=True, check=False,
    )
    if result.returncode:
        raise InstallationError(result.stderr.strip() or "git command failed")
    return result.stdout.strip()



def upstream_url(source):
    """Read actual checkout provenance; don't invent a canonical remote."""
    result = subprocess.run(
        ["git", "-C", str(source), "remote", "get-url", "origin"],
        capture_output=True, text=True, check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else None


def digest(content):
    return hashlib.sha256(content).hexdigest()


def selected_agents(value):
    if value == "all":
        return AGENTS
    names = tuple(dict.fromkeys(part.strip().lower() for part in value.split(",")))
    if not names or any(name not in AGENTS for name in names):
        raise InstallationError("Choose all or a comma-separated subset of claude,codex,copilot")
    return names


def ensure_new_repo(target):
    if not target.is_dir():
        raise InstallationError(f"Repository does not exist: {target}")
    root = Path(git(target, "rev-parse", "--show-toplevel")).resolve()
    if target != root:
        raise InstallationError("Target must be the root of its Git repository")
    if git(target, "status", "--porcelain"):
        raise InstallationError("Target has uncommitted or untracked changes; preserve them before installing")
    allowed = {"README.md", "LICENSE", "LICENSE.md", ".gitignore"}
    tracked = set(git(target, "ls-files").splitlines())
    if tracked - allowed:
        raise InstallationError(
            "Target already contains project files: " + ", ".join(sorted(tracked - allowed))
            + ". Use a separate existing-repository integration scope."
        )



def ensure_source_checkout(source):
    if not source.is_dir():
        raise InstallationError(f"HILD source checkout is missing: {source}")
    root = Path(git(source, "rev-parse", "--show-toplevel")).resolve()
    if root != source:
        raise InstallationError("Source must be the root of a HILD Git checkout")
    if git(source, "status", "--porcelain"):
        raise InstallationError("HILD source has uncommitted changes; cannot record a reproducible source commit")


SKILL_PATH = re.compile(r"\.agents/skills/[A-Za-z0-9_-]+/SKILL\.md")


def skills_index(source):
    """One line per skill, built from each skill's frontmatter description."""
    lines = []
    for skill in sorted((source / ".agents/skills").glob("*/SKILL.md")):
        text = skill.read_text(encoding="utf-8")
        match = re.search(r"^description:\s*(.+?)\s*$", text, re.MULTILINE)
        if not text.startswith("---") or not match:
            raise InstallationError(f"{skill.relative_to(source).as_posix()} has no frontmatter description")
        lines.append(f"- `{skill.parent.name}` "
                     f"([{skill.relative_to(source).as_posix()}]({skill.relative_to(source).as_posix()})): "
                     f"{match.group(1)}")
    return lines


def build_files(source, target, agents):
    """Prepare every output as bytes."""
    for rel in REQUIRED:
        if not (source / rel).is_file():
            raise InstallationError(f"HILD source is incomplete: missing {rel}")
    plan = {}
    shared = ["HILD/README.md", "HILD/process.md", "HILD/agent-setup.md"]
    shared += [
        p.relative_to(source).as_posix() for folder, pattern in (
            ("HILD/templates", "*.md"), ("HILD/templates", "*.json"),
            ("HILD/scripts", "*.py"),
            ("HILD/scripts", "*.sh"), (".agents/skills", "**/*"),
        )
        for p in sorted((source / folder).glob(pattern)) if p.is_file()
    ]
    for rel in sorted(set(shared)):
        plan[rel] = (source / rel).read_bytes()

    index = skills_index(source)
    if not index:
        raise InstallationError("HILD source has no skills with a frontmatter description")
    plan["AGENTS.md"] = (
        "# Project agent instructions\n\n"
        "This project uses [HILD](HILD/process.md) to develop scientific software.\n"
        "Read [HILD's plan](HILD/plan.md) and [getting-started guide](HILD/README.md)\n"
        "before proposing substantive work. Project-specific scientific and coding\n"
        "rules belong here; don't duplicate the HILD process.\n\n"
        "## HILD skills\n\n"
        "HILD's procedures are skills. Read the listed file when its description\n"
        "fits the request. Agents that discover skills natively may use them directly.\n"
        "Claude Code finds the skills only through this index. That is intended\n"
        "([decision 0009](https://github.com/Motor-Learning-Lab/HILD/blob/main/HILD/decisions/0009-claude-skills-via-agents-md.md)):\n"
        "they are not native Claude Code skills, so there are no `/hild-*` commands;\n"
        "ask for a skill by name.\n\n"
        + "\n".join(index) + "\n"
    ).encode()

    if "claude" in agents:
        # Claude Code loads other files only through @path imports.
        plan["CLAUDE.md"] = (
            "# Claude Code entry point\n\n"
            "Project instructions, which link to the [HILD process](HILD/process.md):\n\n"
            "@AGENTS.md\n"
        ).encode()

    for agent in agents:
        template, destination = ADAPTERS[agent]
        source_file = source / template
        if not source_file.is_file():
            raise InstallationError(f"Missing {agent} hook template: {template}")
        plan[destination] = source_file.read_bytes()

    # Preserve an existing ignore file; never overwrite or append to it silently.
    if (target / ".gitignore").is_file():
        check = subprocess.run(
            ["git", "-C", str(target), "check-ignore", "-q", "--no-index",
             "wiki/HILD-wiki-test.md"],
            capture_output=True, check=False,
        )
        if check.returncode:
            raise InstallationError(
                "Existing .gitignore does not ignore wiki/. Add /wiki/ and commit "
                "that change before installing; no existing file will be changed."
            )
    else:
        plan[".gitignore"] = b"# HILD's separate GitHub wiki checkout\n/wiki/\n"
    plan["HILD/plan.md"] = (
        f"# {target.name} plan\n\n"
        "## Goals\n\n- Agree on the project's scientific and software goals.\n\n"
        "## Current state\n\n- HILD's first-time files have been installed; "
        "live agent behavior has not been validated.\n\n"
        "## Next steps\n\n"
        "1. Open an agent chat with repository access and invoke `hild-scope`.\n"
        "2. New to HILD? Propose an onboarding scope and review it before changes.\n"
        "3. After specific approval, create and verify a fresh understanding wiki.\n"
    ).encode()
    plan[f"HILD/journal/{date.today().isoformat()}.md"] = (
        f"# {date.today().isoformat()}\n\n"
        "## Session 1 — First HILD installation\n\n"
        "**Goal:** Prepare this repository to use HILD.\n\n"
        "**Done:** Installed HILD files and selected agent configurations.\n\n"
        "**Results:** Mechanical checks must be run; actual skill loading, "
        "wiki creation, and onboarding remain unverified.\n\n"
        "**Next:** Scope a real first task; onboarding is recommended.\n"
    ).encode()
    plan["HILD/decisions/.gitkeep"] = b""

    source_sha = git(source, "rev-parse", "HEAD")
    metadata = {
        "schema": 1,
        "source_repository": upstream_url(source),
        "source_commit": source_sha,
        "agents": list(agents),
        "authority": {
            "process": "HILD/process.md",
            "plan": "HILD/plan.md",
            "journal": "HILD/journal/",
            "decisions": "HILD/decisions/",
            "understanding_map": "wiki/",
        },
        "files": {
            name: {"sha256": digest(data)}
            for name, data in sorted(plan.items())
        },
    }
    plan[MANIFEST] = (json.dumps(metadata, indent=2, sort_keys=True) + "\n").encode()
    return plan


def check_collisions(target, plan):
    for rel in plan:
        path = target / rel
        if path.exists() or path.is_symlink():
            raise InstallationError(f"Existing path would be overwritten: {rel}")
        for parent in path.parents:
            if parent == target:
                break
            if parent.is_symlink():
                raise InstallationError(f"Existing directory symlink could redirect installation: {parent}")
            if parent.exists() and not parent.is_dir():
                raise InstallationError(f"Path component is not a directory: {parent}")


def apply_plan(target, plan):
    created_files, created_dirs = [], []
    try:
        for rel, data in sorted(plan.items()):
            path = target / rel
            missing = []
            parent = path.parent
            while parent != target and not parent.exists():
                missing.append(parent)
                parent = parent.parent
            for folder in reversed(missing):
                folder.mkdir()
                created_dirs.append(folder)
            path.write_bytes(data)
            created_files.append(path)
    except (OSError, ValueError) as error:
        for path in reversed(created_files):
            path.unlink()
        for folder in reversed(created_dirs):
            folder.rmdir()
        raise InstallationError(f"Installation stopped; new files rolled back: {error}") from error


_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def local_link_problems(root, rel, content):
    """Check local Markdown links in the installed process and skills."""
    problems = []
    for raw in _LINK.findall(content):
        destination = raw.split("#", 1)[0].strip()
        if (
            not destination
            or "://" in destination
            or destination.startswith(("mailto:", "data:", "<", "#"))
        ):
            continue
        destination = unquote(destination).split(" ", 1)[0]
        # Skip illustrative URL placeholders; documentation templates are not
        # checked here, only the actual user instructions and skill files.
        path = (root / rel).parent.joinpath(destination).resolve()
        if not path.is_relative_to(root.resolve()) or not path.exists():
            problems.append(f"{rel}: broken local link {raw!r}")
    return problems


def verify(target):
    """Check structure without treating legitimate local edits as failures."""
    metadata_path = target / MANIFEST
    if not metadata_path.is_file():
        raise InstallationError(f"No {MANIFEST} to verify")
    info = json.loads(metadata_path.read_text(encoding="utf-8"))
    missing, local_edits = [], []
    for rel, expected in info["files"].items():
        path = target / rel
        if not path.is_file():
            missing.append(f"{rel}: missing expected file")
        elif digest(path.read_bytes()) != expected["sha256"]:
            local_edits.append(rel)
        elif rel.endswith(".md") and "/templates/" not in rel:
            missing.extend(local_link_problems(
                target, rel, path.read_text(encoding="utf-8")
            ))

    if "claude" in info["agents"]:
        claude = target / "CLAUDE.md"
        if not claude.is_file() or not re.search(
                r"^@AGENTS\.md\s*$", claude.read_text(encoding="utf-8"), re.MULTILINE):
            missing.append("CLAUDE.md: does not import @AGENTS.md, so Claude Code won't load it")
    agents_md = target / "AGENTS.md"
    listed = (set(SKILL_PATH.findall(agents_md.read_text(encoding="utf-8")))
              if agents_md.is_file() else set())
    if not listed:
        missing.append("AGENTS.md: no HILD skills index")
    missing.extend(f"AGENTS.md: indexed skill missing: {rel}"
                   for rel in sorted(listed) if not (target / rel).is_file())

    for item in missing:
        print("FAIL", item)
    for item in local_edits:
        print("LOCAL CHANGE (preserved):", item)

    for name in info["agents"]:
        _, config_path = ADAPTERS[name]
        path = target / config_path
        if path.is_file():
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except (ValueError, UnicodeDecodeError):
                missing.append(f"{config_path}: invalid JSON")
                print("FAIL", missing[-1])

    if not missing:
        print(f"PASS: all {len(info['files'])} recorded paths are present; "
              f"{len(local_edits)} have legitimate local changes")
    print("NOT TESTED: live agent discovery/hooks, onboarding, GitHub settings or wiki publication")
    return 1 if missing else 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--source", type=Path, default=Path(__file__).resolve().parents[2],
                        help="source HILD checkout (default: checkout containing this script)")
    parser.add_argument("--target", type=Path, default=Path.cwd(), help="target Git repository root")
    parser.add_argument("--agents", default="all", help="all (default) or claude,codex,copilot subset")
    parser.add_argument("--apply", action="store_true", help="write files only after human approval")
    parser.add_argument("--verify", action="store_true", help="check an existing installation, no writes")
    args = parser.parse_args(argv)
    source, target = args.source.resolve(), args.target.resolve()
    try:
        if args.apply and args.verify:
            raise InstallationError("--apply and --verify cannot be combined")
        if args.verify:
            return verify(target)
        agents = selected_agents(args.agents)
        ensure_source_checkout(source)
        ensure_new_repo(target)
        plan = build_files(source, target, agents)
        check_collisions(target, plan)
        if not args.apply:
            print("READ-ONLY INSTALLATION PROPOSAL: no files were changed.")
            print("Selected agents:", ", ".join(agents))
            for name in sorted(plan):
                print(" ADD", name)
            print("Approval required before rerunning with --apply.")
            return 0
        apply_plan(target, plan)
        print(f"Installed HILD for {', '.join(agents)} into {target}")
        result = verify(target)
        if result:
            print(
                "INSTALLATION NEEDS ATTENTION: verification failed after file creation. "
                "New files remain in place for inspection; no automatic rollback "
                "or second --apply was performed.",
                file=sys.stderr,
            )
        return result
    except (InstallationError, json.JSONDecodeError) as error:
        print("HILD:", error, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
