# First installation in a new repository

**Read this when** the researcher has approved an installation scope issue for
a new, clean repository, after the read-only `hild-integrate` assessment. If
the approval is not recorded on the issue, return to
[`hild-scope`](../hild-scope/SKILL.md) and stop. The rules are in the
[installation topic](../../../HILD/process/installation.md) and the
[Git topic](../../../HILD/process/git.md). If a GitHub step or the local
checkout fails for lack of access, use the
[GitHub-access companion](github-access.md).

This installs the current GitHub-and-skills reference implementation. It does
not reconcile an existing installation or wiki.

## Steps

1. **Confirm the inputs:**
   - the approved target Git root;
   - the HILD source checkout and its revision. It must hold the whole
     package: README, process and topic files, scripts, templates, skills and
     the selected hook templates. An incomplete checkout is not a valid
     source;
   - the agent selection: `all` (the default) or some of `claude`, `codex`
     and `copilot`. It controls hooks and configuration, not which agents may
     read the shared files. Claude Code needs no `.claude/skills` link or Git
     symlink setting
     ([decision 0009](https://github.com/Motor-Learning-Lab/HILD/blob/main/HILD/decisions/0009-claude-skills-via-agents-md.md)).

   Tell the researcher that installing changes the target repository but does
   not commit, push, create issues, change settings or create a wiki.
2. **Check what would be affected:** existing files and uncommitted work.
   Never overwrite an existing `AGENTS.md`, `.gitignore`, agent settings, wiki
   files or local HILD state without a separate reconciliation plan.
3. **Create a working branch** in the target repository. The installation
   goes there, not onto the default branch.
4. **Preview.** From the HILD source checkout, run:

   ```bash
   python3 HILD/scripts/install_hild.py --target /path/to/new-repo --agents all
   ```

   It prints a read-only proposal with every target path and the selected
   agents. Discuss it with the researcher, including anything unexpected.
   **Stop:** the preview is not approval. Wait until the researcher agrees to
   this exact proposal **and** authorizes applying it. If you asked about a
   choice and, separately, for permission to apply, an answer naming only the
   choice is not that permission: confirm briefly. Don't reconfirm an
   approval that was already unambiguous.
5. **Apply:**

   ```bash
   python3 HILD/scripts/install_hild.py --target /path/to/new-repo --agents all --apply
   ```

   The script refuses a dirty repository and any collision, and modifies no
   existing file. If creating files fails, it removes the new files; if
   verification fails after creation, the new files stay for inspection. Tell
   the researcher which happened. It records the source commit and per-file
   hashes in `HILD/installation.json`, and creates a starter plan and journal
   and the selected agents' adapters.
6. **Commit, push and open a draft PR,** following the normal review route.
   The script commits, pushes and merges nothing; the researcher merges.
7. **Verify:**

   ```bash
   python3 HILD/scripts/install_hild.py --target /path/to/new-repo --verify
   ```

   It checks the installed files against the recorded baseline, that
   `CLAUDE.md` imports `@AGENTS.md` and `@HILD/process.md`, and that every
   indexed skill exists. Correct files do not show that an agent uses them:
   separately check the selected agent's actual skill discovery and startup
   behavior, and the new wiki if one is created. Say what you could not
   check.
8. **Merge settings, before the first merge.** GitHub's defaults allow merge
   commits and fill a squash commit's message from the branch's commits, so
   the PR explanation never reaches `main`.
   1. Read the settings:
      `gh api repos/OWNER/REPO --jq '{allow_merge_commit, allow_rebase_merge, allow_squash_merge, squash_merge_commit_title, squash_merge_commit_message, delete_branch_on_merge}'`.
   2. If they differ from the [Git topic](../../../HILD/process/git.md),
      propose the change, unless the approved scope already includes it. It
      is an external change and needs the researcher's agreement.
   3. With agreement, set `allow_merge_commit=false`,
      `allow_rebase_merge=false`, `allow_squash_merge=true`,
      `squash_merge_commit_title=PR_TITLE`,
      `squash_merge_commit_message=PR_BODY` and `delete_branch_on_merge=true`
      with `gh api -X PATCH repos/OWNER/REPO -F <name>=<value> ...`. Read
      them back, and record the before and after values on the scope issue.
   4. Without admin access, say so, and tell the researcher to choose
      **Squash and merge** and paste the PR description as the commit
      message.
9. **Point to the next step.** The installed `HILD/README.md` has a starter
   prompt that asks the agent to use `hild-scope`. Onboarding is the
   suggested first scope but not mandatory, and it needs its own approved
   scope and PR.

**Never run `--apply` to upgrade an installed or locally modified HILD, and
never silently modify a pre-existing wiki.** A partially configured
repository needs a new assessment. Report the situation and propose a new
scope instead.
