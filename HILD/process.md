# How we work — HILD

This is a faithful adaptation of the [MotorAdpatationSBI process](https://github.com/opherdonchin/MotorAdpatationSBI/blob/main/HILD/process.md), developed under [scope #5](https://github.com/opherdonchin/MotorAdpatationSBI/issues/5) and [PRs #6](https://github.com/opherdonchin/MotorAdpatationSBI/pull/6) and [#7](https://github.com/opherdonchin/MotorAdpatationSBI/pull/7). This document is the **authoritative HILD process**, not an independently invented replacement.

The aim is that the human **reviewer** stays fully on top of a scientific software project: what is being built, why, how it works, what has been checked, and what they understand less well. Agent-produced documentation supports that understanding.

## Local authority and implementation status

- **Default:** process, plan, journal, decisions and templates live under `HILD/`.
  An established host may configure **each** authoritative location independently,
  preserving existing files; do not move or duplicate them merely to install HILD.
- **Project rules:** scientific aims, source layout, coding conventions and other
  project-specific rules live in the host's `AGENTS.md` or established equivalent.
  That document **points to** this process rather than copying it.
- **Installed HILD is local:** local modifications are legitimate. New upstream
  versions must be compared and reconciled, not installed over the local version.
- **Current bootstrap status:** this first governance PR ports the rules, durable
  state and templates. The original skills, scripts, Claude hooks and wiki are
  **not yet installed in this repo**. Sections below define the intended
  behavior and identify the reference tooling; they do not claim it operates.
  `hild-integrate` will begin with read-only assessment in PR B of
  [scope #1](https://github.com/Motor-Learning-Lab/HILD/issues/1).
- **Path interpretation:** paths in this document are defaults for HILD, not
  installation-time mandates. Every procedure must resolve the host's recorded
  authoritative paths before acting. Choice of configuration format is deferred.

## The life of a piece of work

```
scope issue ─► branch + draft PR ─► work in small commits ─► explanation
     ─► explain-back (or fast track) ─► final cleanup ─► squash merge
     ─► journal, plan, wiki updated
```

1. **Scope.** Every nontrivial development starts as an issue labelled `scope`: the
   contract for the work (see *Scope agreements*). The agent drafts it; the reviewer
   agrees or edits it. No work starts before agreement.
2. **Branch and draft PR.** The agent works on a branch named `<area>/<short-description>`
   and opens a draft PR that closes the scope issue as soon as the branch is first pushed,
   so every commit is retained by GitHub from the start.
3. **Work.** Small commits, each explaining why. Commits are cheap; the PR is where
   organization happens. PR branches are never rewritten (no force-push, no rebase), so
   any link to a branch commit stays valid. Superseded material on a branch moves to
   `archive/` instead of being deleted, so it stays at hand while the work continues.
4. **Explanation.** The agent writes the PR description as an explanation (see
   *Presentations*), which lists the wiki pages the change relies on and proposes the
   pages it calls for.
5. **Approval.** The reviewer approves on one of the tracks in *Approval*, in a PR
   comment.
6. **Final cleanup.** The last commit before merge deletes `archive/` and anything else
   temporary (see *Superseded material* under *Git and GitHub*).
7. **Squash merge.** The reviewer merges. `main` gets one commit per development, whose
   message is the PR's title and description: the explanation lives in `main`'s history.
8. **Record.** The agent brings the journal and plan up to date and drafts the wiki
   pages proposed in the explanation and agreed by the reviewer (see *Understanding
   map*).

Work done directly on `main` (small fixes, plan and journal updates, anything the
reviewer asks for there) may be committed and pushed to `main`. Decision records are the
exception among the durable state files: they always arrive by pull request (see
*Decision records*).

## Scope agreements

A scope issue follows [the scope template](templates/scope-issue.md): the goal, what is in
and out of scope, which standing stopping points are lifted, and how we will know the
work is done.

Work inside an agreed scope is pre-approved. Anything outside it, the agent stops and
asks. If the scope turns out to be wrong, the agent proposes a change to the issue rather
than quietly drifting.

## Presentations

Proposals, explanations and orientations follow the same rules, so that each one is a
real check of the reviewer's understanding rather than a request for an OK.

1. **Purpose first.** Which goal this serves and why now. If it cannot be connected to a
   goal, say so: that is a warning sign.
2. **What you should understand.** Two or three things the reviewer should be able to
   explain by the end.
3. **Layers,** in the order of [the PR explanation template](templates/pr-explanation.md): a plain
   summary, the math, a code walkthrough, the evidence, the consequences, surprises, and
   the wiki pages.
4. **Links everywhere.** Every claim about code links to the exact lines with a GitHub
   permalink (`https://github.com/<owner>/<repo>/blob/<commit>/<path>#L10-L20`). Every
   other reference, to an issue, pull request, commit, file, decision record, wiki page
   or notebook cell, is a link too, in anything posted on GitHub and in every file in the
   repo. Do not rely on GitHub to make the link: a bare `#12` or commit hash links only
   in issue and PR text and never inside backticks, and nothing links by itself in a
   repository file or the wiki.
5. **Load-bearing vs boilerplate.** The walkthrough labels code as *load-bearing — read
   this* or *boilerplate — skim*.
6. **One sitting, one method.** If a change cannot be explained in about fifteen
   minutes, it is too big and gets split. A change introduces one method at a time. A
   method the reviewer has not been shown before comes with its background (a concept
   page in the wiki) and with a check against a result the reviewer already trusts,
   such as a published result or existing code, before anything is built on it.
7. **"I don't get it" is always a good answer.** It means the explanation or the code
   needs work, never that the reviewer failed.
8. **Math that survives GitHub's markdown.** Display math goes in fenced ` ```math `
   blocks, whose content markdown leaves alone. In `$...$` and `$$...$$`, markdown eats
   a backslash before punctuation (`\,` `\;` `\!` `\{` become `,` `;` `!` `{`) and
   mangles `<`; avoid them there (write `y_{1:t-1}`, not `y_{<t}`, and `\lbrace`,
   `\rbrace` for braces). Check that with `gh api markdown` when in doubt. GitHub also
   refuses some macros, `\operatorname` among them (write `\mathrm{...}`); that error
   appears only in the browser, so `gh api markdown` cannot show it.
9. **An explanation always describes the change as it now stands.** After review, the
   explanation is rewritten in place, not patched: a reader should never have to combine
   an old description with a list of amendments. What changed in response to review is
   recorded at the very end, in a dated *Changes after review* section; each later round
   appends another.

10. **Wiki pages are part of an explanation.** Every explanation has a *Wiki pages*
    section with two lists. *Relevant pages:* each existing wiki page the change relies on
    or affects, with how it is relevant and its status, so the reviewer can see which
    background they have confirmed and which they have not. *Proposed pages:* each page
    the change calls for, new or to be updated, with what it would cover. A concept page
    the reviewer needs in order to follow the change is written before review (rule 6)
    and listed as relevant. The other proposed pages are written once the reviewer
    agrees to them; code pages after the merge, because they record a `main` commit.

| Presentation | When | Where |
|---|---|---|
| Proposal | Before nontrivial work | The scope issue |
| Explanation | Before merge | The PR description |
| Orientation | Start of every session (automatic) | Chat |
| Journal | At milestones | `HILD/journal/` |

## Approval

Approval happens **in a PR comment**, so it is part of the PR's permanent record. (If it
happens in chat, the agent posts a short summary of it as a PR comment.) The agent cannot
merge, so approval is not enforced by the agent: it is the reviewer's own gate before
pressing merge. The PR description ends by proposing a track; the reviewer may choose
another.

| Track | For | The reviewer's comment | After merge |
|---|---|---|---|
| **Trivial** | Typo and wording fixes, dependency bumps within existing pins, `explore_` notebooks | Nothing needed | — |
| **Read** | Changes whose text *is* the content: documentation, process, decision records | "Read all changes", plus any questions | — |
| **Full** | Code, and anything whose behaviour is not visible by reading it | Explains back in a sentence or two what the change does and why | Wiki pages drafted or updated |
| **Fast** | Code, when moving quickly | Confirms the minimum: what it is for, what goes in and comes out, what it affects | `understanding-debt` label; an issue to work through it; related wiki pages `needs-review` |

On the full track the agent replies to the explanation, comparing it with what the code
does. A mismatch is a found gap: the agent explains again or the code changes. The
reviewer chooses the fast track whenever a full explain-back would cost more than the
change is worth right now; the debt it leaves is visible and gets scheduled. The trivial
list starts conservative and is calibrated over time.

## Understanding map

The **understanding map** records what the reviewer understands. The original implementation uses a separate GitHub wiki cloned into a gitignored `wiki/` directory. That is the initial reference arrangement, **not yet configured here**. An installation must identify its authoritative understanding-map location; support for alternatives is an unresolved design choice.

The understanding map is never authoritative. It may restate and summarize what the repo says, in
the reviewer's terms, to make the repo easier to approach; the repo is the source. When
the two drift apart, that is a signal to slow down and check that the reviewer is still
on top of the work, and that it is making real progress rather than only producing code.

**Page kinds.** A page's name starts with its kind (`Code-environment`,
`Concept-kalman-filter`), and `Home` and the sidebar group pages by kind.

| Kind | What it holds |
|---|---|
| `code` | One load-bearing module or finalized notebook: *What it does*, *How and why*, *How it fits the larger project*, *Invariants and pitfalls* (what must stay true if the code changes, and the mistakes that are easy to make). Records the files it covers and the `main` commit it describes. |
| `concept` | An idea the code relies on, linking code pages to the math. |
| `process` | How we work and how the tooling works: explanation of the process, as opposed to the project's content. |
| `guide` | A reading path: which pages to read, in what order, to understand an area. |
| `resource` | A background source: what it is, a link, and why it matters here. |

New kinds are added here, when a real page needs one. Formats: [code-page template](templates/wiki-code-page.md) and [general-page template](templates/wiki-page.md).

**Statuses.**

| Status | Set by | Meaning |
|---|---|---|
| `not-written` | nobody | No page exists yet. Another page links to it, or a pull request proposes it. |
| `stub` | agent | A page that exists only as a placeholder, still to be written. |
| `draft` | agent | Written by the agent; the reviewer has not confirmed it. |
| `understood` | reviewer only | The reviewer has read, edited and confirmed it. |
| `needs-revision` | either | The reviewer has read it and it did not do its job, or the agent knows it falls short. The agent owes a rewrite. |
| `needs-review` | either | Merged on the fast track, or the reviewer is no longer sure. |
| `stale` | script | The code changed materially since the commit the page describes. |

`not-written` is the one status that is not recorded on a page, since there is no page:
it is what an explanation's *Wiki pages* section says of a page that is linked or
proposed and does not exist.

`needs-revision` and `needs-review` point in opposite directions: the first says the
page must change, the second that the reviewer must read it again.

In the reference implementation, a generated *Status board* page lists the pages that exist by status, and the
`not-written` pages that some page links to.

**Who writes.** The agent drafts pages; the reviewer edits them, in the browser or
through the agent.

**Staleness.** A script compares the commit each code page describes with `main`;
pages whose code has changed materially become `stale`, and an issue is opened to
review them, once the corresponding tooling is installed. Code pages record `main` commits (code as it stands); journals and
explanations may link to branch commits.

**When the wiki is committed and pushed.** The wiki has no pull requests; its history is
its record. When a git-backed understanding map is configured, the agent pulls it before touching it (to pick up the reviewer's browser edits) and commits and pushes it straight after every change it makes. Nothing is left
uncommitted in the local clone. When orientation tooling is installed, session-start data reports anything unpushed.

## Where each thing lives, and how to change it

Every rule, format and procedure has exactly one authoritative home. Other places
point to it; they never restate it. The table gives **defaults**, not locations to
impose on established host repositories.

| What | Default authoritative home |
|---|---|
| Why the project exists; layout; coding, notebook and hygiene rules | host `AGENTS.md` |
| How reviewer and agent work together | `HILD/process.md` (this file) |
| Step-by-step agent procedures | agent-discoverable `hild-*` skills (placement to be verified) |
| Formats for scope issues, PRs, journal, decisions, understanding pages | `HILD/templates/` |
| Machinery, including scripts | `HILD/scripts/` (when ported) |
| Agent-specific hooks | agent-native configuration (when ported) |
| Current goals, state and next steps | `HILD/plan.md` |
| What happened | `HILD/journal/` |
| Why we chose what we chose | `HILD/decisions/` |
| Project terms | host glossary, if one exists |
| What the reviewer understands | understanding map (reference implementation: GitHub wiki) |
| What remains unvalidated or insufficiently understood | issue tracker, with explicit debt labels when adopted |

To change something:

1. Find its authority in this table (or the host's configured mapping) and edit it there.
2. A new coding or hygiene habit goes in the host's project rules; a change to how
   human and agent work together goes here. Skills point to rules and templates
   rather than restating them; a skill changes when the **procedure** changes.
3. If something seems to need saying in two places, make one a pointer.
4. Rule and decision changes arrive through a reviewed PR on the **read** track.
   Audits must look for rules that have crept into secondary locations.

## How the tooling works

The **reference implementation** uses brief skills that link here for rules and
to templates for formats. An agent loads a skill when its task matches.
These are procedures, not duplicate process specifications.

| Skill | When |
|---|---|
| `orient` (planned `hild-orient`) | Start of a session; "where are we?" |
| `scope` (planned `hild-scope`) | Before nontrivial development |
| `explain` | When a PR is ready for review |
| `journal` | At milestones |
| `understood` | To maintain the understanding map |
| `digest` | Periodic repository audit |
| `hild-integrate` | Assess adoption, later installation and upgrade; first pass read-only |

The names of the first six procedures follow the [original skills](https://github.com/opherdonchin/MotorAdpatationSBI/tree/main/.github/skills). Their final HILD names and cross-agent discovery locations are not fully decided.

Two mechanical tools in the original repository have **not yet been ported**:

- [`session_context.sh`](https://github.com/opherdonchin/MotorAdpatationSBI/blob/main/.github/skills/scripts/session_context.sh) gathers branch, plan, journal, recent changes, issues, PRs and wiki status for orientation.
- [`wiki_status.py`](https://github.com/opherdonchin/MotorAdpatationSBI/blob/main/.github/skills/scripts/wiki_status.py) detects potentially stale code pages and generates a status board.

Three [Claude Code hooks](https://github.com/opherdonchin/MotorAdpatationSBI/blob/main/.claude/settings.json) start orientation, prompt for retention of unrecorded milestones before compaction, and prompt for their recording after compaction. The original PR verified startup partially and tested compaction commands only. [Issue #10](https://github.com/opherdonchin/MotorAdpatationSBI/issues/10) tracks live compaction testing; [issue #11](https://github.com/opherdonchin/MotorAdpatationSBI/issues/11) tracks Copilot/Codex equivalents.

**None of these scripts or hooks runs automatically in HILD yet.**
Until the corresponding skills exist, an agent follows the process manually.
The bootstrap integration assessment must never run a write-capable hook or
script before human approval.

## Durable state files

State lives in files, not in chat.

The agent cannot tell when a session will end, so the plan and journal are updated at
**milestones**, not at the end:

- a sub-step of agreed work is finished and pushed;
- a PR is opened, marked ready, or merged;
- a significant result, finding or dead end;
- a decision is made;
- context is compacted: hooks ask the summary to keep unrecorded milestones and remind
  the agent to record them straight afterwards;
- at the start of a session, if orientation finds the last session's work missing from
  the journal, the agent fills it in from git history before anything else.

### Plan — `HILD/plan.md` (default)

- **What:** current goals, current state, and the ordered next steps. Nothing else.
- **When to update:** at milestones (above), whenever a goal, the state, or the next steps
  change.
- **How:** rewrite in place; the old versions are in `main`'s history (see *Git and
  GitHub*).
- **When to read:** at the start of every session.

### Journal — `HILD/journal/YYYY-MM-DD.md` (default)

- **What:** a factual log of the work. One file per day; a second session on the same day
  adds a new `## Session N` section.
- **When to update:** at milestones (above). Each update adds to the current session's
  section, so the entry is always complete up to the last milestone.
- **Format:** [the journal-entry template](templates/journal-entry.md).
- **When to read:** the latest entry at startup; earlier entries when resuming a thread
  of work (search by topic).
- Entries are history: do not rewrite past entries except to fix errors, and say so.

### Decision records — `HILD/decisions/NNNN-short-title.md` (default)

- **What:** choices that constrain future work and are not obvious from the code: tools,
  model formulations, conventions, rejected alternatives worth remembering.
- **When to write:** when the decision is made (drafted by the agent, accepted by the
  reviewer). Small choices go in the journal's *Decisions* line instead.
- **How it is accepted:** a new record, and any change to an existing one, arrives as a
  pull request on the *read* track, so the reviewer can comment on its lines. The agent
  never commits a decision record directly to `main`, and only the reviewer's approval of
  that pull request makes its status `Accepted`.
- **Format:** [the decision-record template](templates/decision-record.md).
- **Superseding:** write a new record and set the old one's status to `Superseded by
  NNNN`. Decision records are kept, not deleted: the history of why is the point.
- **When to read:** before changing anything in an area a record covers (check titles
  with `ls docs/decisions`).

## Autonomy

- **Routine, no need to ask:** reads, searches, local edits, running notebooks and tests,
  normal git, and creating, commenting on and closing issues.
- **Standing stopping points** — ask first, unless lifted by a scope agreement or by the
  reviewer: new classes or helper functions, new directories or new kinds of auxiliary
  files, dependency changes, anything destructive or hard to undo, anything with external
  side effects beyond issues and this repo's own branches and PRs.
- **Independent work.** When asked to work independently, the agent keeps going without
  asking for any permission, including destructive changes within the repo, and records
  every point where permission would normally have been asked, and what was decided, in
  the journal's *Permission points*.
- For non-obvious tradeoffs, explain briefly and choose the simpler, less stateful option.

## Git and GitHub

- Before starting, decide whether the work needs a branch, say what was decided, and
  commit any pending work.
- Branches merge into `main` only with the reviewer's approval, through a pull request,
  as a squash merge.
- Never stop work while waiting for a merge: continue on the branch or start the next
  piece of work.
- All work must be recoverable on another machine: push at every milestone.
- **Superseded material** — the one rule, referred to elsewhere:
  - on a branch, move it to `archive/` so it stays at hand while the work continues;
  - the final commit before merge deletes `archive/`; the material stays reachable
    through the PR's commits;
  - on `main`, delete superseded files rather than keeping `old` copies; git history is
    the archive. Update or remove references in the same change.
  - Exception: decision records are kept and marked superseded.
- Commit messages explain why, not just what.
- When the agent acts through the reviewer's GitHub account, its comments start with
  **🤖 Claude:** (or the agent's name) so it is clear who wrote what.
- Replies to review comments go in the comment's own thread, with permalinks to the fix.
