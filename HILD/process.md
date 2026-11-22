# How we work — HILD

This is a faithful adaptation of the [MotorAdpatationSBI process](https://github.com/opherdonchin/MotorAdpatationSBI/blob/main/docs/process.md), developed under [scope #5](https://github.com/opherdonchin/MotorAdpatationSBI/issues/5) and [PRs #6](https://github.com/opherdonchin/MotorAdpatationSBI/pull/6) and [#7](https://github.com/opherdonchin/MotorAdpatationSBI/pull/7). This document is the **authoritative HILD process**, not an independently invented replacement.

The aim is that the human **reviewer** stays fully on top of a scientific software project: what is being built, why, how it works, what has been checked, and what they understand less well. Agent-produced documentation supports that understanding.

## What HILD requires, and how we implement it

**HILD is a human-supervised development process, not a particular software
package or GitHub workflow.** It is meant to preserve the researcher's
authority, understanding and ability to resume work as agents help develop
scientific software. Five outcomes make the process recognizable:

1. **Agreed authority:** work has an inspectable account of its goal,
   boundaries, success evidence and delegated autonomy. Ordinary supervised
   work begins after researcher approval; explicitly authorized independent
   work may pass ordinary permission checkpoints, but the unapproved work and
   decisions remain provisional pending later human review.
2. **Inspectable change:** proposed changes stay separate from accepted work
   until the researcher can examine their purpose, effects and evidence.
3. **Meaningful review:** the researcher decides whether to accept work, with
   explanation and evidence appropriate to the change. Review intensity does
   not remove the need for human acceptance; the agent never accepts or merges
   on the researcher's behalf.
4. **Recoverable development state:** the goals, progress, decisions, tests
   and unresolved questions remain accessible beyond any one chat session.
5. **Researcher-confirmed understanding:** the agent proposes explanations
   and flags uncertainty, but only the researcher determines their current
   understanding, including withdrawing an earlier confirmation.

**GitHub issues, Git branches, draft PRs, squash merges, agent skills, hooks,
a plan, a journal and an understanding wiki are HILD's reference
implementation.** They are concrete, recommended ways to achieve those
outcomes—not the definition of the outcomes. The procedures below describe
that implementation precisely because it is the one currently developed and
tested; describing another possible implementation does **not** claim it
already works.

**How to read the rest of this document:** Process statements specify what
the human and agent aim to achieve, without depending on a particular tool.
Nearby implementation instructions say how this installation achieves it;
these remain binding conventions until the researcher agrees to change them.
Some passages are wholly process or wholly implementation, where that is
clearer. Do not mechanically duplicate a process statement for every command.
Process rules themselves can also be revised through reviewed decisions.
Interlinked explanations and evidence are part of the process; GitHub
permalinks and wiki links are our concrete way of making those connections.

When the normal mechanism is unavailable or a project has established
alternatives, the agent should explain **what function the mechanism serves**,
work with the researcher on an equivalent way to provide that function, and
record the agreed choice and remaining limitations. For example, another
durable issue tracker could record a scope if the researcher can inspect and
approve the actual record and future sessions can recover that approval.
A casual conversation without a reviewable record is **not** an equivalent
replacement. Do not silently substitute tools, weaken stopping points or
claim equivalence without evidence. When compatibility issues arise, report
specific problems and demonstrated workarounds upstream for later review.

## Authority and local configuration

- **Requirement:** each type of authoritative guidance and development state has
  one discoverable home, and adopting HILD preserves a host's existing authority.
  **Default implementation:** process, plan, journal, decisions and templates live under `HILD/`.
  An established host may configure **each** authoritative location independently,
  preserving existing files; do not move or duplicate them merely to install HILD.
- **Project rules:** scientific aims, source layout, coding conventions and other
  project-specific rules live in the host's `AGENTS.md` or established equivalent.
  That document **points to** this process rather than copying it.
- **Installed HILD is local:** local modifications are legitimate. New upstream
  versions must be compared and reconciled, not installed over the local version.
- **Capability status:** a procedure described here is not evidence it has
  been installed or tested. See this project's `HILD/plan.md`, installation
  metadata (when present), and actual test evidence to determine what works.
- **Path interpretation:** paths in this document are defaults for HILD, not
  installation-time mandates. Every procedure must resolve the host's recorded
  authoritative paths before acting. Choice of configuration format is deferred.

## The life of a piece of work — GitHub reference workflow

**Process:** An ordinary piece of work proceeds from a bounded agreement,
through inspectable provisional changes and evidence-based human review, to
human acceptance and a recoverable account of what was learned. Approval of
the work and approval of its eventual result are distinct. Explicitly
authorized independent work can progress ahead of ordinary permission
checkpoints, but cannot make its unapproved choices accepted by doing so
(see *Autonomy*).

**Implementation:** Our default GitHub lifecycle is:

```
scope issue ─► branch + draft PR ─► work in small commits ─► explanation
     ─► human review (appropriate track) ─► final cleanup ─► human squash merge
     ─► final plan/journal update + agreed wiki pages
          (plan and journal also updated during work)
```

1. **Scope and authorization.** Establish the work agreement and its review
   status. Normally create an issue labelled `scope`, present its actual link
   and obtain the researcher's explicit approval, recorded on the issue, before
   implementation (see *Scope agreements*). Under separately authorized
   independent work, mark any missing approval and dependent work provisional.
2. **Inspectable work.** Keep changes separate from accepted code. Use a
   branch named `<area>/<short-description>` and open a draft PR as soon as
   the branch is first pushed. The PR is the durable work-in-progress record.
3. **Small increments and recovery.** Commit small, explainable changes with
   messages saying why. Update the plan and journal at meaningful milestones
   while the PR is open; include unresolved permission points. Push each
   milestone. Do not rewrite pushed PR branch history (no force-push or rebase).
   Move superseded temporary material to `archive/` while the branch is open.
4. **Explain the current change.** Make the PR description a layered explanation
   with evidence, linked sources, consequences, and relevant/proposed wiki pages
   (see *Presentations*). Describe the current diff, not merely the original
   intent. Disclose provisional work and missing human decisions.
5. **Human review and acceptance.** Present the actual PR and ask the
   researcher to choose an appropriate depth of review. All tracks ultimately
   require human acceptance, including trivial changes; a PR comment is a
   useful durable record but not a universal prerequisite for acceptance.
   No agent may merge on the researcher's behalf (see *Approval*).
6. **Finalize reviewable contents.** Remove `archive/` and temporary material
   in the last commit before merge, preserving earlier branch commits.
7. **Human merge.** The researcher squash-merges after acceptance. On `main`,
   the resulting commit uses the PR title and final description, preserving
   the explanation in the Git history.
8. **Record and reconnect knowledge.** Finalize plan/journal after merge
   (without deferring earlier milestone records) and draft agreed wiki pages.
   Link the accepted result back to its scope, evidence and related knowledge.

**Reference-workflow exception:** Small fixes and state updates may be
committed directly to `main` when the researcher explicitly requests or
authorizes that route. Decision records always follow reviewed PRs, not direct
`main` changes (see *Decision records*).

## Scope agreements

**Process:** Scope makes the agent's authority and the expected result
inspectable. In ordinary supervised work, the human reviews and approves the
actual agreement before implementation. A standing authorization to proceed
independently is not approval of later choices beyond that agreement: such
choices and their dependent work must remain visibly provisional until the
human reviews them. Scope changes cannot become approved merely because an
agent recorded them.

**Implementation:** In the GitHub reference workflow, a scope issue follows
[the scope template](templates/scope-issue.md): the goal, what is in
and out of scope, which standing stopping points are lifted, and how we will know the
work is done.

The mechanics of proposing a scope issue, recording its approval and amending it are in [the scope topic](process/scope.md).

Work inside an approved scope is authorized for execution, not thereby
accepted as a result. In ordinary supervised work, the agent stops and asks
before exceeding it. **Only when the researcher has explicitly authorized
independent work** may the agent pass ordinary stopping points: it records
each deferred permission and the resulting provisional work, presents the
expanded or changed scope for later approval, and does not merge or otherwise
represent provisional work as accepted. If scope changes materially, the
proposed change is linked to the original issue; the earlier approval does
not automatically extend to it. External actions that cannot be recovered
are not made safe merely by a provisional label.

### Develop scopes through dialogue

A scope agreement covers four questions: **goal** (what and why),
**boundaries** (what's in and out), **evidence** (how success will be
recognized), and **autonomy** (what the agent may do without further
permission). These describe a completed agreement, **not four questions to
ask in order**. Develop them in natural conversation, drawing on what the
researcher already said, offering relevant expertise, and reflecting back
emerging agreement. A "yes" to *working on a scope* is not approval of the
finished scope or permission to implement it.

When there is a good, reversible default, recommend it and explain its value;
mention that alternatives exist. Present a small set of alternatives when
important tradeoffs genuinely require a choice. Do not present every possible
option as a questionnaire. Keep technical investigations rigorous, but disclose
details as they become relevant to the researcher's next decision. If an
access or tooling limitation blocks an agreed action, work with the researcher
to diagnose it and choose a way forward. The completed issue may be detailed
even when the conversation that produced it was short and focused.

For a researcher **new to HILD or requesting guidance**, the
[onboarding companion](../.agents/skills/hild-scope/onboarding-scope.md)
is the single procedural home for introductory explanations and the
guided first-scope conversation. Both `hild-integrate` and `hild-scope`
point there rather than restating those instructions
([decision 0005](https://github.com/Motor-Learning-Lab/HILD/blob/main/HILD/decisions/0005-conversational-scope-building.md)).

## Presentations

Proposals, explanations and orientations follow the same rules, so that each one is a
real check of the reviewer's understanding rather than a request for an OK.

Write so that **a researcher unfamiliar with HILD's internal terminology can follow**.
Name the actor and action rather than relying on vague references ("it", "this").
Explain unfamiliar terms when first used, give concrete examples when a procedure is
abstract, and distinguish working capabilities from proposals and untested behavior.
A procedure that is clear only to the agent still needs improvement.

Rules 1–5 and 8–10 are in [the review topic](process/review.md).

6. **One sitting, one method.** As our current *process* limit, if a change
   cannot be explained in about fifteen minutes, it is too big and gets split.
   The researcher may explicitly adjust this limit as the process evolves. A change introduces one method at a time. A
   method the reviewer has not been shown before comes with its background (a concept
   page in the wiki) and with a check against a result the reviewer already trusts,
   such as a published result or existing code, before anything is built on it.
7. **"I don't get it" is always a good answer.** It means the explanation or the code
   needs work, never that the reviewer failed.

| Presentation | When | Where |
|---|---|---|
| Proposal | Before nontrivial work | The scope issue |
| Explanation | Before merge | The PR description |
| Orientation | Start of every session (automatic) | Chat |
| Journal | At milestones | `HILD/journal/` |

**Automatic** orientation means it happens by default when a session opens,
without the researcher having to ask for it. If the researcher's first message
asks for something else, the orientation is brief and the request is then
handled. A session-start hook achieves this where the agent supports one;
otherwise a standing instruction in the host's agent instructions does. The
hook is a convenience, not a precondition (see *How the tooling works*).

## Approval

**Process:** Producing work is not accepting it. The researcher decides
whether to accept every change, including a trivial one. Explanation and
review depth are proportional to the change; they do not substitute for
acceptance. Independent work beyond approved authority is provisional until
the researcher reviews the deferred choices and the consequences built on
them. Acceptance of a downstream result cannot silently erase that debt.

How review is requested, and the review tracks, are in [the review topic](process/review.md).

## Understanding map

**Process:** Maintain a linked, recoverable map of the researcher's current
understanding and uncertainties. The researcher alone judges what they
understand; they may withdraw an earlier confirmation at any time, and that
current judgment overrides a stale page status. An agent's draft, status
checker, or past confirmation cannot certify present understanding.

**Implementation:** The **understanding map** records what the reviewer understands. The original implementation uses a separate GitHub wiki cloned into a gitignored `wiki/` directory. That is the initial reference arrangement, **not yet configured here**. An installation must identify its authoritative understanding-map location; support for alternatives is an unresolved design choice.

The understanding map is never authoritative. It may restate and summarize what the repo says, in
the reviewer's terms, to make the repo easier to approach; the repo is the source. When
the two drift apart, that is a signal to slow down and check that the reviewer is still
on top of the work, and that it is making real progress rather than only producing code.

Page kinds, statuses, who writes pages, staleness, and when the wiki is committed are in [the understanding-map topic](process/understanding-map.md).

## Where each thing lives, and how to change it

**Process:** Preserve one authoritative source for each rule, decision,
procedure and current-state record, with links between related knowledge
instead of duplicated prose.

**Implementation:** Every rule, format and procedure has exactly one authoritative home. Other places
point to it; they never restate it. The table gives **defaults**, not locations to
impose on established host repositories.

| What | Default authoritative home |
|---|---|
| Why the project exists; layout; coding, notebook and hygiene rules | host `AGENTS.md` |
| How reviewer and agent work together | `HILD/process.md` (this file) and its topic files in `HILD/process/` |
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

## Topic files

Rules that only align one kind of action live in topic files under
[`HILD/process/`](process/), so a session reads them when a task calls for
them ([decision 0012](https://github.com/Motor-Learning-Lab/HILD/blob/main/HILD/decisions/0012-process-spine-and-topic-files.md)).
Read the topic file **before** the action it names:

| Topic file | Read before |
|---|---|
| [`scope.md`](process/scope.md) | creating a scope issue, recording its approval, or amending it |
| [`review.md`](process/review.md) | writing a proposal or PR explanation, or asking for review |
| [`understanding-map.md`](process/understanding-map.md) | creating or changing an understanding-map page or its status |
| [`decision-records.md`](process/decision-records.md) | creating, changing or superseding a decision record |
| [`git.md`](process/git.md) | opening or finishing a PR, preparing one for merge, or changing merge settings |
| [`writing-skills.md`](process/writing-skills.md) | writing or changing a skill |

## How the tooling works

The process above defines **what** the human and agent must do. Tooling makes
those steps easier to remember and carry out; it does not create new rules.
There are three different kinds of supporting tool:

- **Skills are instructions for the agent.** For example, the orientation skill
  says how to turn repository facts into a short report for the reviewer.
  The skill points to the rules here and to a template where appropriate.
- **Scripts do mechanical work.** They collect or compare information that
  would be tedious or error-prone for an agent to assemble by hand. They are
  not the source of process rules.
- **Hooks connect a supported agent event to an action.** For example, a
  Claude Code session-start hook runs a script automatically. An agent without
  that hook can still perform the same work by following the skill manually.

Worked examples, the table of procedure names and the origin of HILD's tooling are in the understanding map ([Process-tooling-history](https://github.com/Motor-Learning-Lab/HILD/wiki/Process-tooling-history)).

Until a supporting tool is installed and verified, the agent follows the
rules manually rather than pretending automation exists. An initial
`hild-integrate` **assessment** never runs hooks or write-capable scripts,
and never changes local or GitHub state before human approval.
When writing or changing a skill, follow [the writing-skills topic](process/writing-skills.md).

## Durable state files

**Process:** Goals, decisions, significant results, open questions, progress
and any deferred human decisions must survive a chat and remain connected to
the evidence that produced them. Keep the current plan distinct from the
factual history of how work developed.

**Implementation:** State lives in files, not in chat.

The agent cannot tell when a session will end, so the plan and journal are updated at
**milestones**, not at the end:

- a sub-step of agreed work is finished and pushed;
- a PR is opened, marked ready, or merged;
- a significant result, finding or dead end;
- a decision is made or a deferred authorization creates provisional work;
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
- **Where between milestones:** not yet specified. The process does not yet say
  on which branch a plan update made during open work is committed.
- **When to read:** at the start of every session.

### Journal — `HILD/journal/YYYY-MM-DD.md` (default)

- **What:** a factual log of the work, including decisions, links to evidence,
  provisional actions and deferred permission points where relevant.
  One file per day; a second session on the same day adds a new
  `## Session N` section.
- **When to update:** at milestones (above). Each update adds to the current session's
  section, so the entry is always complete up to the last milestone.
- **Format:** [the journal-entry template](templates/journal-entry.md).
- **When to read:** the latest entry at startup; earlier entries when resuming a thread
  of work (search by topic).
- Entries are history: do not rewrite past entries except to fix errors, and say so.

### Decision records — `HILD/decisions/NNNN-short-title.md` (default)

- **Process:** Record consequential choices and their reasoning so future
  work can recover what is currently decided and why. A decision is not
  retroactively rewritten to present a changed judgment as the original one.
  A *new decision* may **modify**, **overrule** specific provisions of, or
  **replace** an earlier decision. It must link the predecessor, state the
  precise effect and what still applies, and explain its reasoning in full.
  An earlier accepted decision remains historical evidence even when its
  current applicability changes.
- **Mechanics:** numbering, successor notices, current authority and when to write a record are in [the decision-records topic](process/decision-records.md).

## Autonomy

**Process:** Delegation of execution and human approval are different.
Ordinary supervised work proceeds inside an approved scope and stops at
unapproved boundaries. When the researcher **explicitly authorizes
independent work**, the agent may keep developing beyond ordinary permission
checkpoints. Such permission authorizes *continuation*, not the unreviewed
choices, scope expansions or dependent results as accepted HILD work. The
agent records what was done, which ordinary approvals were bypassed and
what later work depends on those choices. All of that remains **provisional**
until the researcher works through it and decides what to accept, revise or
reject. Later work cannot bootstrap approval for its own prerequisites.

**Reference GitHub conventions:**

- **Routine, without additional permission:** reads, searches, local edits,
  running notebooks/tests, normal Git operations and creating/commenting on
  issues and PRs within the existing scope.
- **Ordinary stopping points:** ask before introducing new classes or helper
  functions, new directories or auxiliary-file kinds, dependencies,
  destructive/hard-to-reverse changes and external side effects beyond
  this repository's issues, branches and PRs, unless the approved scope
  explicitly delegates them.
- **Independent work:** record every deferred checkpoint, agent choice,
  affected commit and dependent work in the journal's `Permission points`
  and surface them in the PR explanation and next session orientation.
  Keep the relevant PR draft/provisional; do not merge, publish as accepted,
  or erase deferred approvals. Project-local destructive edits may be made
  provisionally under a specifically authorized independent-work mandate,
  with recoverable Git history. Irreversible effects on external systems
  are not made reversible by labeling them provisional; seek explicit
  authority for these separately.
- **Credentials:** never ask for or publish credentials, private keys,
  device codes or raw `gh auth token` output in chat, terminal logs,
  issues or PRs, and never put credentials in Git remote URLs or commits.
  Logging in, storing credentials, changing Git configuration or
  permissions, and making new clones are consequential actions: explain
  them and get agreement first.
- **Decision style:** when a tradeoff is not obvious, explain briefly and
  prefer the simpler, less stateful option, while recording provisional
  choices where approval is deferred.

## Git and GitHub — reference implementation details

**Process:** Proposed work must remain inspectable, recoverable and linked
to its scope and explanation, and only human-accepted changes may become
accepted project state.

**Implementation:** These are the currently supported, binding Git-based
conventions, not an assertion that a GitHub feature is intrinsically
required for human-supervised development.

- Before starting, decide whether the work needs a branch, say what was decided, and
  commit any pending work.
- Branches merge into `main` only with the reviewer's approval, through a pull request,
  as a squash merge.
- Never stop work while waiting for a merge: continue on the branch or start the next
  piece of work.
- All work must be recoverable on another machine: push at every milestone.
- Commit messages explain why, not just what.
- When the agent acts through the reviewer's GitHub account, its comments start with
  **🤖 Claude:** (or the agent's name) so it is clear who wrote what.
- Merge settings, superseded material, `Closes` versus `Part of`, and replies to review comments: see [the Git topic](process/git.md).
