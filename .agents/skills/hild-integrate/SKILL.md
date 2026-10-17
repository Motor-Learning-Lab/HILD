---
name: hild-integrate
description: Introduce HILD, assess a repository read-only, and help the researcher decide how to adopt or update it. Use when asked to install, integrate, upgrade, reconcile or audit HILD.
---

# HILD integration — understand the goal before installing

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

## First conversation with a researcher

Someone asking to adopt HILD may know very little about it. **Begin by
explaining what it is for**, in plain language: small agreed pieces of work,
human review and understanding of code and algorithms, explanations when
something is unclear, and durable decisions and an independent understanding
map (often a GitHub wiki). HILD coordinates development through repository
issues and pull requests; it does **not** run inside the wiki.

Then connect those benefits to the **researcher's repository and already
stated goal**. For an almost-empty repository, installing HILD can itself
teach the collaboration method while starting a real project. For an
established repository, explain the value of preserving its existing process.
Don't imply that the researcher should accept unknown files or agent hooks
before learning what they do.

**Invite the researcher to build the first installation scope together.**
For example: "One of the first things to learn is how HILD uses a scope issue
to agree on a manageable piece of work. Would you like to work together on
the scope for installing HILD here?" This is an illustration, **not** text
to recite in every repository.

Do not lead with a large authority table, a complete installation plan, a
verification matrix, or a request to approve implementation. A "yes" to
*developing a scope* starts the dialogue; it does **not** approve the final
scope or authorize installation. Use the [hild-scope skill](../hild-scope/SKILL.md)
to work toward that agreement, including its conversational guidance.

A newcomer should understand why HILD may help their project and why
scoping is the natural next step before being asked to configure software.

## How to present findings and handle limitations

- Investigate thoroughly; **present progressively**. Start with what is
  relevant to the researcher's project, the useful next decision and any
  material uncertainty. Supply the technical inventory on request or when
  a consequential choice depends on it.
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
