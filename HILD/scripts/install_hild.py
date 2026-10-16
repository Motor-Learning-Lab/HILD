#!/usr/bin/env python3
"""Plan, install, or verify HILD in a clean, newly initialized Git repository.

The default is read-only. Use --apply only after a researcher has explicitly
approved the installation scope. Existing files are never overwritten.
"""

import argparse
import hashlib
import json
import subprocess
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



def ensure_source_checkout(source):
    if not source.is_dir():
        raise InstallationError(f"HILD source checkout is missing: {source}")
    root = Path(git(source, "rev-parse", "--show-toplevel")).resolve()
    if root != source:
        raise InstallationError("Source must be the root of a HILD Git checkout")
    if git(source, "status", "--porcelain"):
        raise InstallationError("HILD source has uncommitted changes; cannot record a reproducible source commit")


def build_files(source, target, agents):
    """Prepare every output as bytes; a None value represents the Claude symlink."""
    for rel in REQUIRED:
        if not (source / rel).is_file():
            raise InstallationError(f"HILD source is incomplete: missing {rel}")
    plan = {}
    shared = ["HILD/README.md", "HILD/process.md", "HILD/agent-setup.md"]
    shared += [
        str(p.relative_to(source)) for folder, pattern in (
            ("HILD/templates", "*.md"), ("HILD/scripts", "*.py"),
            ("HILD/scripts", "*.sh"), (".agents/skills", "**/*"),
        )
        for p in sorted((source / folder).glob(pattern)) if p.is_file()
    ]
    for rel in sorted(set(shared)):
        plan[rel] = (source / rel).read_bytes()

    plan["AGENTS.md"] = (
        "# Project agent instructions\n\n"
        "This project uses [HILD](HILD/process.md) to develop scientific software.\n"
        "Read [HILD's plan](HILD/plan.md) and [getting-started guide](HILD/README.md)\n"
        "before proposing substantive work. Project-specific scientific and coding\n"
        "rules belong here; don't duplicate the HILD process.\n"
    ).encode()

    if "claude" in agents:
        plan["CLAUDE.md"] = (
            "# Claude Code entry point\n\n"
            "Follow [project instructions](AGENTS.md), which link to the\n"
            "[authoritative HILD process](HILD/process.md).\n"
        ).encode()
        plan[".claude/skills"] = None

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
        "source_repository": "https://github.com/Motor-Learning-Lab/HILD",
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
            name: {"sha256": digest(data)} if data is not None
            else {"symlink": "../.agents/skills"}
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
            if data is None:
                path.symlink_to("../.agents/skills", target_is_directory=True)
            else:
                path.write_bytes(data)
            created_files.append(path)
    except (OSError, ValueError) as error:
        for path in reversed(created_files):
            path.unlink()
        for folder in reversed(created_dirs):
            folder.rmdir()
        raise InstallationError(f"Installation stopped; new files rolled back: {error}") from error


def verify(target):
    metadata_path = target / MANIFEST
    if not metadata_path.is_file():
        raise InstallationError(f"No {MANIFEST} to verify")
    info = json.loads(metadata_path.read_text(encoding="utf-8"))
    problems = []
    for rel, expected in info["files"].items():
        path = target / rel
        if "symlink" in expected:
            if not path.is_symlink() or str(path.readlink()) != expected["symlink"]:
                problems.append(f"{rel}: expected symlink to {expected['symlink']}")
        elif not path.is_file() or digest(path.read_bytes()) != expected["sha256"]:
            problems.append(f"{rel}: missing or changed from installed baseline")
    for item in problems:
        print("FAIL", item)
    if not problems:
        print(f"PASS: {len(info['files'])} recorded paths match the installation baseline")
    print("NOT TESTED: native agent skill discovery, hooks, onboarding, GitHub settings and wiki publication")
    return 1 if problems else 0


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
        return verify(target)
    except (InstallationError, json.JSONDecodeError) as error:
        print("HILD:", error, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
