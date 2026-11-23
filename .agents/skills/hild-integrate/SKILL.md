---
name: hild-integrate
description: Assesses a repository read-only and helps the researcher decide how to adopt, upgrade or reconcile HILD there, then installs HILD in a new repository once an installation scope is approved. Use when someone wants to add HILD to a repository, install or upgrade it, or compare an existing installation with upstream HILD.
---

# Integrate HILD: assess, agree, then install

The rules are in the [installation topic](../../../HILD/process/installation.md)
and the [scope topic](../../../HILD/process/scope.md). If you are reading this
skill from upstream before HILD is installed, read the upstream process and
topic files too: links relative to this skill may not resolve in the target
repository.

**Read the [onboarding companion](../hild-scope/onboarding-scope.md) when**
the researcher is new to HILD or asks for guidance. It then governs the
conversation in step 5; keep your findings to inform it. If HILD is not
installed, read it from the same upstream revision as this skill.

**Read the [GitHub-access companion](github-access.md) when** a missing
checkout, authentication, permission or Git remote blocks the agreed next
action.

**Read [first-install.md](first-install.md) only** at step 7.

## Steps

1. **Assess read-only.** Until a scope is approved, do not change files,
   branches, issues, pull requests, settings, hooks or remote refs, and do not
   commit, fetch, pull, run scripts or generate files. Reading is fine:
   `git status`, `git log`, `git ls-files`, `git show` and GitHub GET
   requests. Avoid suspected secrets and untrusted executables. Report what
   you could not see rather than treating it as absent.
2. **Identify the two repositories:** the target's repository, branch,
   visible files and existing work; the upstream HILD commit; and the access
   available. Don't confuse GitHub's committed state with an unexamined local
   working tree.
3. **Find what must be preserved:** project instructions, process rules,
   skills and hooks, decisions, plan, journal, tests, wiki, repository
   settings and conventions. Identify each one's authoritative home.
4. **Recognize the installation state:** no HILD, an installation of known
   upstream provenance, one of uncertain provenance, or partial adoption. For
   an existing installation, compare the recorded upstream baseline (B), the
   current local files (L) and the proposed upstream (N) where possible; if
   the baseline is missing, say so. The installer accepts only a **new**
   repository: clean, with no tracked files beyond `README.md`, `LICENSE`,
   `LICENSE.md` and `.gitignore`. Any other repository needs a separate
   integration scope. Then work out safe additions, collisions,
   prerequisites and feasible ways forward, without changing anything.

   Steps 2–4 are tasks, not an order for the conversation. Keep paths,
   revisions, conflicts and evidence at hand for questions and for the scope
   issue.
5. **Report and ask.** Give a researcher who knows HILD a short,
   evidence-based account: what HILD appears to have installed, what must be
   preserved, and what is uncertain. Connect a recommendation to their goal
   and explain the main tradeoff, if there is one. End with the next
   consequential question or proposed agreement, not the full inventory. Then:
   - if they correct a fact or name an existing authority, revise the
     assessment before proposing to change that material;
   - if they give a new goal or constraint, shape the scope around it;
   - if they want an alternative, compare only the relevant paths, grounded
     in the repository and the available tooling.
6. **Agree the scope with [`hild-scope`](../hild-scope/SKILL.md),** using the
   [scope-issue template](../../../HILD/templates/scope-issue.md)'s note on
   what an installation scope states. Have the technical inventory, authority
   map and source revision ready when a decision or the scope needs them.
   **Stop** until the researcher has approved the actual issue, as
   `hild-scope` says.
7. **Install** in a new repository by following
   [first-install.md](first-install.md). It does not upgrade an existing
   installation, reconcile local changes or integrate an existing wiki: for
   those, report the situation and propose a separate scope.
