---
name: hild-integrate
description: Assess a repository read-only and help the researcher decide how to adopt, upgrade, reconcile or audit HILD. For newcomers, load the onboarding companion before presenting findings.
---

# HILD integration — assess first, then guide agreement

Authoritative rules: [HILD process](../../../HILD/process.md). If reading
this skill from an upstream URL before installing HILD, also read the upstream
process; links relative to this skill may not resolve in the target repository.

## Non-negotiable read-only first pass

**Assess first; do not install.** During the initial assessment, do **not**
change files, branches, issues, pull requests, settings, hooks or remote refs;
do not commit, fetch, pull, execute scripts or generate files. Read-only
operations such as `git status`, `git log`, `git ls-files`, `git show`
and GitHub GET requests are allowed. Avoid suspected secrets and untrusted
executables. Report access limitations rather than treating unseen work as
absent.

## Gather enough evidence to guide the conversation

1. **Identify the two repositories.** Check the target repository, branch,
   visible files and existing work; identify the upstream HILD commit and
   available access. Never confuse GitHub's committed state with an unexamined
   local working tree.
2. **Check what needs preserving.** Look for project instructions, process
   rules, skills/hooks, decisions, plan, journal, tests, wiki, repository
   settings and development conventions. Identify each authoritative home;
   don't assume HILD should replace an existing one.
3. **Recognize the installation state.** Distinguish no HILD, an installation
   with known upstream provenance, one with uncertain provenance, and partial
   adoption. For an existing installation, compare the recorded old upstream
   baseline (B), current local files (L) and proposed upstream (N), where
   possible. If the baseline is missing, say so; don't overwrite local changes.
4. **Identify the consequential choices and blockers.** Think through safe
   additions, collisions, prerequisites and feasible ways forward without
   changing anything.

These are **assessment tasks**, not a mandatory order of headings in the
conversation. Keep supporting paths, revisions, conflicts and evidence
available for questions and the eventual scope issue.

## When the researcher is new or wants guidance

If the researcher is unfamiliar with HILD, wants to learn it by installing
it, or asks for guidance getting started, **read and follow the
[onboarding companion](../hild-scope/onboarding-scope.md) before responding**.
It is the authoritative procedure for explaining HILD to newcomers,
connecting its value to the researcher's project, inviting the first
scope, and responding to a "yes" to developing that scope.

This applies **before installation**, too. If this skill was loaded from
an upstream URL, fetch the onboarding companion from that **same upstream
repository and revision**; do not assume the target already contains it.
Use [hild-scope](../hild-scope/SKILL.md) for the general scope agreement
once that conversation begins.

For an experienced researcher who does not need onboarding, proceed with
the normal integration discussion. Do not load newcomer instructions
unnecessarily.

## How to present findings and handle limitations

- Investigate thoroughly; **present progressively**, emphasizing relevant
  findings, uncertainty, and what needs agreement next. Supply the full
  technical inventory on request or when a consequential choice requires it.
- Recommend a sensible default when one is clearly appropriate; mention
  that alternatives can be discussed. Compare a small set of options when
  their tradeoffs materially affect the researcher. Avoid a mandatory
  questionnaire or a menu of every possible configuration.
- If access, permissions, a local checkout or another prerequisite blocks an
  **agreed next action**, investigate feasible alternatives, explain the
  simplest path and work with the researcher to resolve it. Don't turn
  a blocker into a premature demand for configuration or abort the discussion.
- Keep provenance and uncertainty explicit even when not displaying a full
  report. Never claim the wiki, hooks or agent skill loading work merely
  because files exist.

## Before agreement is complete

The eventual scope must capture the target and upstream revision, what
existing authority will be preserved, intended changes, conflicts and
deferrals, stopping points, and checks for success. It must also distinguish
what has been observed from what remains to be tested. Record the result in
the [scope-issue format](../../../HILD/templates/scope-issue.md) **after
developing the agreement**, not as an upfront form for the researcher.

**Stop before creating an issue or making changes until the researcher agrees
to the proposed scope.** The initial read-only assessment is not permission
to create an issue. A conversation agreeing to *discuss* scoping is not
permission to install. After the researcher explicitly agrees to install,
read [first-install.md](first-install.md) for a fresh repository only; it
describes a separately approved preview-first procedure. It does not
implement existing-wiki integration or upgrade reconciliation.
