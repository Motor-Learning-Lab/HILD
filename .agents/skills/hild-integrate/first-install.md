# Installing HILD after the researcher approves the scope

Read this companion **only after** completing the strict read-only
`hild-integrate` assessment and receiving explicit human agreement to install
into a **new, clean repository**. An approved assessment alone is not
authorization to install. Reconciliation of an existing HILD installation or
pre-existing wiki is outside this procedure.

## Before execution

1. Confirm the approved target Git root, source HILD checkout and upstream
   revision. Explain that installing changes the target repository, but does
   not commit, push, create GitHub issues, change settings or create a wiki.
2. Confirm the supported agent selection: `all` (default) or a subset of
   `claude`, `codex` and `copilot`. This selection controls intentional
   hooks/configuration, not permission for another agent to read shared files.
3. Identify any existing files or uncommitted work that would be affected.
   Never overwrite an existing AGENTS file, gitignore, agent settings, wiki
   files or local HILD state without a separate, explicit reconciliation plan.
4. Make sure the source checkout contains the **whole** HILD package:
   README, process, scripts, templates, shared skills and selected hook
   templates. Using an incomplete upstream checkout is not a valid install.

## Preview (read-only) then install (approved write)

1. After the researcher agrees to the installation scope, record that agreement
   in a GitHub scope issue for the **target** repository. Create a working
   branch there. The install will create files on that branch, **not** silently
   change the default branch.
2. From the **HILD source checkout**, run the preview command below. Discuss
   the exact proposed file changes before applying them.
3. Run the approved install, commit and push its first small change, and open
   a **draft PR promptly**, following the normal HILD review procedure.
   Neither the script nor this companion automatically commits, pushes or
   merges. The human remains responsible for merge approval.

From the **HILD source checkout**, run:

```bash
python3 HILD/scripts/install_hild.py --target /path/to/new-repo --agents all
```

The command must print a read-only installation proposal, including all
target paths and the selected agents. Discuss any unexpected additions.
Do not treat the preview as approval.

Only once the researcher agrees to that exact proposal:

```bash
python3 HILD/scripts/install_hild.py --target /path/to/new-repo --agents all --apply
```

The script refuses dirty repositories and collisions. It records a source
commit and per-file hashes in `HILD/installation.json`, creates a starter
plan/journal and only the selected agent adapters. The first implementation
does **not** modify existing files; installation into a partially configured
repository needs a new assessment.

## Verification and next step

```bash
python3 HILD/scripts/install_hild.py --target /path/to/new-repo --verify
```

This checks the recorded baseline for the installed files. Separately verify
the repository's GitHub squash settings, the selected agent's **actual**
skill discovery and startup behavior, and the **new** wiki when created.
Mechanically correct files are **not** proof of runtime agent behavior.

The installed `HILD/README.md` contains a copyable starter prompt. Ask the
agent to invoke `hild-scope`; onboarding is the suggested first scope but
not mandatory. The researcher must approve onboarding's own scope and PR.

**Do not run `--apply` to upgrade an installed or locally modified HILD.
Do not silently modify a pre-existing wiki.** Report unsupported situations
and propose a new scope instead.
