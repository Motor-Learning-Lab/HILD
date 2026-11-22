# How we work — HILD

This is the HILD process. Every session reads it first. It says what is true
and why. How to carry out particular activities is in the topic files under
[`HILD/process/`](process/); [the map](#8-the-map) says when to read each one.

## 1. What HILD is for

HILD is a **human-supervised development process** for AI-assisted scientific
software, not a particular software package or GitHub workflow. Its aim is
that the researcher stays fully on top of the project: what is being built,
why, how it works, what has been checked, and what they understand less
well. Five outcomes make the process recognizable:

1. **Agreed authority:** work has an inspectable account of its goal,
   boundaries, success evidence and delegated autonomy.
2. **Inspectable change:** proposed changes stay separate from accepted work
   until the researcher can examine their purpose, effects and evidence.
3. **Meaningful review:** the researcher decides whether to accept work, with
   explanation and evidence appropriate to the change.
4. **Recoverable development state:** the goals, progress, decisions, tests
   and unresolved questions remain accessible beyond any one chat session.
5. **Researcher-confirmed understanding:** the agent proposes explanations
   and flags uncertainty, but only the researcher determines their current
   understanding.

GitHub issues, Git branches, draft PRs, squash merges, agent skills, hooks, a
plan, a journal and an understanding wiki are HILD's **reference
implementation**: concrete, recommended ways to achieve those outcomes, not
their definition. Its conventions remain binding until the researcher agrees
to change them. The process itself changes only through reviewed decisions.

- **Described is not working.** A procedure described here is not evidence
  that it has been installed or tested, and a skill's presence does not show
  that an agent found or followed it. The plan, installation metadata and
  actual test evidence say what works. Until a supporting tool is installed
  and verified, follow the rule by hand rather than pretending automation
  exists.
- **Paths are defaults.** Paths in this process are HILD's defaults. A host
  may have recorded other authoritative locations; resolve them before
  acting.
- **When a mechanism is unavailable,** or a project has established
  alternatives, explain **what function the mechanism serves**, work with the
  researcher on an equivalent way to provide that function, and record the
  agreed choice and its remaining limitations. A casual conversation without
  a reviewable record is **not** an equivalent. Do not silently substitute
  tools, weaken stopping points or claim equivalence without evidence.

## 2. The life of a piece of work

An ordinary piece of work goes from a bounded agreement, through inspectable
provisional changes and evidence-based review, to the researcher's acceptance
and a recoverable account of what was learned.

```
scope issue ─► branch + draft PR ─► work in small commits ─► explanation
     ─► researcher's review (appropriate track) ─► final cleanup
     ─► researcher's squash merge ─► final plan/journal update + agreed wiki pages
          (plan and journal also updated during work)
```

1. **Scope:** the researcher and agent agree the goal, boundaries, evidence
   and autonomy, and the researcher approves the written agreement itself.
2. **Inspectable work:** changes stay on a branch, apart from accepted work;
   a draft PR is the durable record of work in progress.
3. **Small commits:** the work proceeds in small, explainable steps, with
   the plan and journal kept current at milestones.
4. **Explanation:** the PR explains the change as it now stands, with its
   evidence, so the researcher can judge it.
5. **Review:** the researcher chooses how deeply to review and whether to
   accept.
6. **Cleanup:** temporary material is removed before the merge.
7. **Merge:** the researcher squash-merges the accepted change.
8. **Reconnect:** the plan and journal record the result, agreed wiki pages
   are written, and the result is linked to its scope, evidence and related
   knowledge.

**Approving a scope authorizes the work; it does not accept its result.**
Accepting the result is a separate decision, made at review.

Small fixes and state updates may be committed directly to `main` only when
the researcher explicitly requests or authorizes that route. Decision records
never are.

## 3. The researcher's authority

Producing work is not accepting it. The researcher decides whether to accept
every change, including a trivial one. Review depth is proportional to the
change and never substitutes for acceptance. **The agent never accepts or
merges on the researcher's behalf.** Review depth, permission to proceed,
acceptance of a PR and merging are separate decisions.

- **Routine, without further permission:** reads, searches, local edits,
  running notebooks and tests, normal Git operations, and creating and
  commenting on issues and PRs within the existing scope.
- **Ordinary stopping points:** ask before introducing new classes or helper
  functions, new directories or auxiliary-file kinds, dependencies,
  destructive or hard-to-reverse changes, and external side effects beyond
  this repository's issues, branches and PRs, unless the approved scope
  explicitly delegates them. Having asked, do not begin unapproved
  nontrivial work before the researcher responds.
- **Inside the scope:** work inside an approved scope is authorized for
  execution, not thereby accepted as a result. In ordinary supervised work,
  the agent stops and asks before exceeding it. If the scope must change
  materially, the agent proposes the change; the earlier approval does not
  extend to it, and a change is not approved because the agent recorded it.

### Independent work

Delegating execution is different from approval. **Only when the researcher
explicitly authorizes independent work** may the agent keep developing
beyond ordinary stopping points. A short "OK" or a technical choice is not
such a mandate. The mandate authorizes *continuation*, not the unreviewed
choices, scope expansions or dependent results as accepted work. All of that
stays **provisional** until the researcher works through it and decides what
to accept, revise or reject. Accepting a downstream result cannot silently
erase that debt, and later work cannot bootstrap approval for its own
prerequisites.

Under such a mandate the agent:

- records every deferred checkpoint, agent choice, affected commit and
  dependent work in the journal's `Permission points`, and surfaces them in
  the PR explanation and the next session's orientation;
- presents the expanded or changed scope for later approval;
- keeps the relevant PR draft and provisional: it does not merge, publish as
  accepted, or erase deferred approvals;
- may make project-local destructive edits provisionally only under a
  specifically authorized mandate, with recoverable Git history.

Irreversible effects on external systems are not made reversible by
labeling them provisional; seek explicit authority for these separately.

**Decision style:** when a tradeoff is not obvious, explain briefly and
prefer the simpler, less stateful option, recording provisional choices where
approval is deferred.

## 4. Talking with the researcher

Proposals, explanations and orientations are each a real check of the
researcher's understanding, not a request for an OK.

- **Write for a researcher unfamiliar with HILD's terms.** Name the actor and
  action rather than relying on vague references ("it", "this"). Explain
  unfamiliar terms when first used, give concrete examples when a procedure
  is abstract, and distinguish working capabilities from proposals and
  untested behavior. A procedure that is clear only to the agent still needs
  improvement.
- **Recommend; don't run a questionnaire.** When there is a good, reversible
  default, recommend it, say why it serves the researcher, and mention that
  alternatives exist. Present a small set of alternatives only when an
  important tradeoff genuinely requires a choice. Keep technical
  investigations rigorous, but disclose details as they become relevant to
  the researcher's next decision.
- **One sitting, one method.** If a change cannot be explained in about
  fifteen minutes, it is too big and gets split; the researcher may
  explicitly adjust this limit. A change introduces one method at a time. A
  method the researcher has not been shown before comes with its background
  (a concept page in the wiki) and with a check against a result they
  already trust, such as a published result or existing code, before
  anything is built on it.
- **"I don't get it" is always a good answer.** It means the explanation or
  the code needs work, never that the researcher failed.
- **Every reference is a real link.** Link important claims, decisions,
  results, code and explanations to the material they rely on, so a future
  researcher or agent can follow and evaluate the reasoning. Every claim
  about code links to the exact lines.

## 5. State in files

State lives in files, not in chat. Goals, decisions, significant results,
open questions, progress and any deferred human decisions must survive a
chat and stay connected to the evidence that produced them. The agent cannot
tell when a session will end, so the plan and journal are updated at
**milestones**, not at the end:

- a sub-step of agreed work is finished and pushed;
- a PR is opened, marked ready, or merged;
- a significant result, finding or dead end;
- a decision is made, or a deferred authorization creates provisional work;
- context is compacted: record any unrecorded milestones straight afterwards;
- at the start of a session, if the last session's work is missing from the
  journal, fill it in from git history before anything else.

What each record is:

- **The plan** holds the current goals, the current state and the ordered
  next steps. Nothing else.
- **The journal** is the factual history of the work: decisions, links to
  evidence, provisional actions and deferred permission points. Past entries
  are not rewritten.
- **Decision records** keep consequential choices and their reasoning, so
  future work can recover what is currently decided and why. They arrive only
  through a reviewed PR, never by a direct commit to `main`. A decision is
  never rewritten to present a changed judgment as the original one: a later
  decision modifies, overrules or replaces it, and the earlier one remains
  historical evidence. The current rule is always stated in this process, so
  no one has to reconcile old decisions to know it.

**Before deciding or changing anything in an area, read the titles of its
decision records** and the successor notices at their tops.

**At the start of a session,** read this file, the plan and the latest
journal entry. **Orientation** follows by default, without the researcher
having to ask: a short account of where the project stands, what changed,
what needs the researcher's attention and what to do next. If the
researcher's first message asks for something else, the orientation is brief
and the request is then handled.

## 6. Understanding

Only the researcher judges what they understand. They may withdraw an earlier
confirmation at any time, and that current judgment overrides any page
status. An agent's draft, a status checker or a past confirmation cannot
certify present understanding. **Accepting a PR does not by itself mean that
any related page is understood.**

The **understanding map** records what the researcher understands and where
they are uncertain; in the reference implementation it is the GitHub wiki. It
is never authoritative. It may restate and summarize what the repository
says, in the researcher's terms, to make the repository easier to approach;
the repository is the source. When the two drift apart, that is a signal to
slow down and check that the researcher is still on top of the work, and that
it is making real progress rather than only producing code.

## 7. Rules at every step

- **Credentials:** never ask for or publish credentials, private keys, device
  codes or raw `gh auth token` output in chat, terminal logs, issues or PRs,
  and never put credentials in Git remote URLs or commits. Logging in,
  storing credentials, changing Git configuration or permissions, and making
  new clones are consequential actions: explain them and get agreement first.
- **Branch first:** before starting, decide whether the work needs a branch,
  say what was decided, and commit any pending work.
- **Merge only through a reviewed PR:** branches merge into `main` only with
  the researcher's approval, through a pull request, as a squash merge.
- **Never rewrite a pushed PR branch:** no force-push or rebase.
- **Push at every milestone,** so all work is recoverable on another machine.
- **Commit messages explain why,** not just what.
- **Never stop work while waiting for a merge:** continue on the branch or
  start the next piece of work.
- **Say who wrote it:** when the agent acts through the researcher's GitHub
  account, its comments start with **🤖 Claude:** (or the agent's name).

## 8. The map

Every rule, format and procedure has exactly one authoritative home. Other
places point to it and never restate it. These homes are defaults; an
established host may have recorded others.

| What | Default authoritative home |
|---|---|
| Why the project exists; layout; coding, notebook and hygiene rules | host `AGENTS.md` |
| How the researcher and agent work together | `HILD/process.md` (this file) and its topic files in `HILD/process/` |
| Step-by-step agent procedures | `hild-*` skills in `.agents/skills/`, listed in `AGENTS.md` |
| Formats for scope issues, PRs, journal, decisions, understanding pages | `HILD/templates/` |
| Machinery, including scripts | `HILD/scripts/` |
| Agent-specific hooks | agent-native configuration |
| Current goals, state and next steps | `HILD/plan.md` |
| What happened | `HILD/journal/` |
| Why we chose what we chose | `HILD/decisions/` |
| Project terms | host glossary, if one exists |
| What the researcher understands | understanding map (reference implementation: GitHub wiki) |
| What remains unvalidated or insufficiently understood | issue tracker, with explicit debt labels when adopted |

**Tools help carry out the process; none creates rules.** Skills are
step-by-step instructions for the agent. Scripts do mechanical work. Hooks
connect an agent event to an action; an agent without a hook can do the same
work by following the skill by hand.

**To change something:**

1. Find its home in the table (or the host's recorded mapping) and change it
   there.
2. A new coding or hygiene habit goes in the host's project rules; a change
   to how the researcher and agent work together goes in this process. A
   skill points to rules and templates rather than restating them, and
   changes when the **procedure** changes.
3. If something seems to need saying in two places, make one a pointer.
4. Rule and decision changes arrive through a reviewed PR on the **read**
   track. Audits look for rules that have crept into secondary locations.

### Topic files

Read a topic file **before** the activity it names. Each one holds the
details that align that activity with this process.

| Topic file | Read before |
|---|---|
| [`scope.md`](process/scope.md) | proposing, creating, recording approval of, or amending a scope issue |
| [`review.md`](process/review.md) | writing a proposal or PR explanation, asking for review, or responding to it |
| [`git.md`](process/git.md) | creating a branch, opening or finishing a PR, committing to `main`, preparing a merge, or changing merge settings |
| [`plan-and-journal.md`](process/plan-and-journal.md) | writing or updating the plan or a journal entry |
| [`decision-records.md`](process/decision-records.md) | creating, changing or superseding a decision record |
| [`understanding-map.md`](process/understanding-map.md) | creating or changing an understanding-map page or its status |
| [`installation.md`](process/installation.md) | assessing, installing, upgrading or reconciling HILD in a repository, or agreeing a substitute for an unavailable mechanism |
| [`writing-skills.md`](process/writing-skills.md) | writing or changing a skill |
