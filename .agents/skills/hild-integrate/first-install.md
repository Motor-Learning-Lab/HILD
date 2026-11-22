# Installing HILD after the researcher approves the scope

Read this companion after the read-only `hild-integrate` assessment
and the researcher's approval of the installation scope. First make sure
the researcher has **seen the actual GitHub scope issue**, has had a chance
to correct it, and has approved it. Record that approval in the issue.
If you cannot establish this, return to the
[hild-scope conversation](../hild-scope/SKILL.md) before starting work;
an earlier "OK" to discussing a proposal is not enough.

This procedure installs **the current GitHub-and-skills reference
implementation** into a new, clean repository. HILD itself is a development
process, not the installer; reconciling an existing installation or wiki
requires a separate scope and unsupported workarounds must not be presented
as already tested.

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
   For a blocked GitHub operation or unavailable local checkout, use
   [github-access.md](github-access.md) to diagnose access without overriding
   the researcher's approval gates.
4. Make sure the source checkout contains the **whole** HILD package:
   README, process, scripts, templates, shared skills and selected hook
   templates. Using an incomplete upstream checkout is not a valid install.

## Claude Code: no symlink or Git setting is needed

Claude Code finds the skills through the generated `CLAUDE.md`, which imports
`@AGENTS.md`, and the skills index in `AGENTS.md`. The installer creates no
`.claude/skills` link, so it checks no Git symlink setting
([decision 0009](https://github.com/Motor-Learning-Lab/HILD/blob/main/HILD/decisions/0009-claude-skills-via-agents-md.md)).
`--verify` checks the import and that every indexed skill exists.

## Preview (read-only) then install (approved write)

1. Confirm the **target repository's approved scope issue link and recorded
   approval**. If either is missing, return to [hild-scope](../hild-scope/SKILL.md):
   present the issue for human review and pause. Once approval is documented,
   create a working branch in the target repository. Installation changes
   belong on that branch, not silently on the default branch.
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

Only once the researcher agrees to that exact proposal **and authorizes applying it**:

If you asked about an implementation choice *and* separately requested permission to
run `--apply`, an answer naming only the choice is not authorization to execute.
Briefly confirm the action before proceeding; do not reconfirm approval that was
already unambiguous.

```bash
python3 HILD/scripts/install_hild.py --target /path/to/new-repo --agents all --apply
```

The script refuses dirty repositories and collisions. If file creation fails,
new files are rolled back; **verification failure after creation leaves the
new files in place** for inspection. Explain this distinction rather than
claiming every failure is automatically reversed. The script records a source
commit and per-file hashes in `HILD/installation.json`, creates a starter
plan/journal and only the selected agent adapters. The first implementation
does **not** modify existing files; installation into a partially configured
repository needs a new assessment.

## Verification and next step

```bash
python3 HILD/scripts/install_hild.py --target /path/to/new-repo --verify
```

This checks the recorded baseline for the installed files. Separately verify
the selected agent's **actual**
skill discovery and startup behavior, and the **new** wiki when created.
Mechanically correct files are **not** proof of runtime agent behavior.

## Merge settings, before the first merge

GitHub's defaults allow merge commits and fill a squash commit's message with
the branch's commit messages, so the PR explanation never reaches `main`.
Before the researcher merges the installation PR:

1. Read the settings:
   `gh api repos/OWNER/REPO --jq '{allow_merge_commit, allow_rebase_merge, allow_squash_merge, squash_merge_commit_title, squash_merge_commit_message, delete_branch_on_merge}'`.
2. If they differ from
   [process, *Git and GitHub*](../../../HILD/process.md#git-and-github--reference-implementation-details),
   propose the change, unless the approved scope already includes it. It is an
   external change and needs the researcher's agreement.
3. With agreement, set `allow_merge_commit=false`, `allow_rebase_merge=false`,
   `allow_squash_merge=true`, `squash_merge_commit_title=PR_TITLE`,
   `squash_merge_commit_message=PR_BODY` and `delete_branch_on_merge=true` with
   `gh api -X PATCH repos/OWNER/REPO -F <name>=<value> ...`. Read them back and
   record the before and after values on the scope issue.
4. Without admin access, say so, and tell the researcher to choose
   **Squash and merge** and paste the PR description as the commit message.

## Starting work

The installed `HILD/README.md` contains a copyable starter prompt. Ask the
agent to invoke `hild-scope`; onboarding is the suggested first scope but
not mandatory. The researcher must approve onboarding's own scope and PR.

**Do not run `--apply` to upgrade an installed or locally modified HILD.
Do not silently modify a pre-existing wiki.** Report unsupported situations
and propose a new scope instead.
