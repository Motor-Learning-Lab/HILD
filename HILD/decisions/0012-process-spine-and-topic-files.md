# 0012 — The process is a spine read every session, with topic files read on demand

**Date:** 2026-11-22 · **Status:** Proposed

**Relationship to earlier decisions:** **Modifies** [decision 0010](0010-skill-authoring-checklist.md) in one provision: the *Writing skills* checklist moves from a section of `process.md` to the topic file `HILD/process/writing-skills.md`. The rest of 0010 still applies. No other decision changes; decisions that link to sections of `process.md` keep their meaning, and only their links are updated.

**Context:** [Scope #33](https://github.com/Motor-Learning-Lab/HILD/issues/33). `HILD/process.md` is 669 lines. HILD's own `CLAUDE.md` imports all of it into every session. Installed hosts import none of it: their generated `CLAUDE.md` imports only `AGENTS.md`, which links to the process. So an agent in a host reasons about HILD only if a skill sends it to the file, and then it reads the whole file to find one section. Working from part of the process causes real errors: in [PR #32](https://github.com/Motor-Learning-Lab/HILD/pull/32) an agent with an outdated copy rewrote a decision record against the decision-record rule.

The researcher set the principle: **"a conservative design: we should build a spine that we think has all the information an agent needs to reason coherently and contextually. We should remove those parts that are more strongly related to specific processes and rules that an agent only needs in order to ensure that its actions are properly aligned."**

**Decision:**

1. **`HILD/process.md` becomes the spine.** It keeps every passage an agent needs to reason about HILD as a whole:
   - what HILD is for;
   - the life of a piece of work;
   - each section's *Process:* statement;
   - the rules that apply at any moment;
   - the map of where each thing lives.

   When it is unclear which side a passage belongs on, it stays in the spine.
2. **Rules that only align one kind of action move to topic files** under `HILD/process/`. The spine's map gives one line per topic file saying when to read it:

   | Topic file | Read before | Contents ([`process.md` at `5b599eb`](https://github.com/Motor-Learning-Lab/HILD/blob/5b599eb00df03451fcb01c9f160b051666e72a8d/HILD/process.md)) |
   |---|---|---|
   | `scope.md` | creating a scope issue, recording its approval, or amending it | the two agreements; recording approval ([L150-L166](https://github.com/Motor-Learning-Lab/HILD/blob/5b599eb00df03451fcb01c9f160b051666e72a8d/HILD/process.md#L150-L166)) |
   | `review.md` | writing a proposal or PR explanation, or asking for review | presentation rules 1–3, 4's GitHub detail, 8–10 ([L216-L237](https://github.com/Motor-Learning-Lab/HILD/blob/5b599eb00df03451fcb01c9f160b051666e72a8d/HILD/process.md#L216-L237), [L246-L267](https://github.com/Motor-Learning-Lab/HILD/blob/5b599eb00df03451fcb01c9f160b051666e72a8d/HILD/process.md#L246-L267)); approval's GitHub implementation and tracks ([L292-L315](https://github.com/Motor-Learning-Lab/HILD/blob/5b599eb00df03451fcb01c9f160b051666e72a8d/HILD/process.md#L292-L315)) |
   | `understanding-map.md` | creating or changing a wiki page or its status | page kinds, statuses, who writes, staleness, when the wiki is committed ([L331-L386](https://github.com/Motor-Learning-Lab/HILD/blob/5b599eb00df03451fcb01c9f160b051666e72a8d/HILD/process.md#L331-L386)) |
   | `decision-records.md` | creating, changing or superseding a decision record | numbering, successor notices, current authority, when to write one ([L567-L589](https://github.com/Motor-Learning-Lab/HILD/blob/5b599eb00df03451fcb01c9f160b051666e72a8d/HILD/process.md#L567-L589)) |
   | `git.md` | opening, finishing or preparing a PR for merge, or changing merge settings | merge settings; superseded material; `Closes` versus `Part of`; replies in thread ([L646-L652](https://github.com/Motor-Learning-Lab/HILD/blob/5b599eb00df03451fcb01c9f160b051666e72a8d/HILD/process.md#L646-L652), [L656-L662](https://github.com/Motor-Learning-Lab/HILD/blob/5b599eb00df03451fcb01c9f160b051666e72a8d/HILD/process.md#L656-L662), [L664-L666](https://github.com/Motor-Learning-Lab/HILD/blob/5b599eb00df03451fcb01c9f160b051666e72a8d/HILD/process.md#L664-L666), [L669](https://github.com/Motor-Learning-Lab/HILD/blob/5b599eb00df03451fcb01c9f160b051666e72a8d/HILD/process.md#L669)) |
   | `writing-skills.md` | writing or changing a skill | the checklist ([L478-L510](https://github.com/Motor-Learning-Lab/HILD/blob/5b599eb00df03451fcb01c9f160b051666e72a8d/HILD/process.md#L478-L510)) |

3. **Moved to the understanding map:** the tooling examples, the table of original procedure names, and the origin notes ([L438-L472](https://github.com/Motor-Learning-Lab/HILD/blob/5b599eb00df03451fcb01c9f160b051666e72a8d/HILD/process.md#L438-L472)). They explain history; no rule is lost. The skills index in `AGENTS.md` already lists the procedures.
4. **Everything else stays in the spine** (about 416 lines before item 7). This includes the life of a piece of work ([L80-L134](https://github.com/Motor-Learning-Lab/HILD/blob/5b599eb00df03451fcb01c9f160b051666e72a8d/HILD/process.md#L80-L134)), *Develop scopes through dialogue*, the presentation principles that apply to all writing (plain language, one sitting, "I don't get it"), the plan and journal, all of *Autonomy*, and the Git rules that apply at every step: merge only through a reviewed PR, push at milestones, commit messages say why, and the 🤖 prefix.
5. **Every agent reads the spine at the start of a session.**
   - **Claude Code:** `CLAUDE.md` imports it (`@HILD/process.md`), in HILD itself and in the `CLAUDE.md` the installer generates.
   - **Codex and Copilot:** the generated `AGENTS.md`, which both read natively, tells them to read `HILD/process.md` before anything else.
6. **No rule changes meaning.** Removing duplication and tightening wording (item 7) may change how a rule is said, never what it requires.
7. **Each rule is stated once, and the wording is tightened.** This happens in two steps, so that each can be reviewed on its own:
   - **The move:** text moves verbatim to the spine, topic files and wiki. Wording changes only where a move requires it, such as a cross-reference to a section now in another file, and each change is listed.
   - **The rewrite:** each rule is stated once, in the section that owns it, and other sections link there instead of restating it. For example, the independent-work rule is stated in *What HILD requires*, *Life of a piece of work*, *Scope agreements*, *Approval* and *Autonomy*; it keeps its full statement in *Autonomy* only. Wording is then made shorter and clearer. For each section, the rewrite lists the requirements it contained before and shows where each one is stated after, so you can check that nothing was dropped or changed.

**Why:**

- **Alternatives considered:**
  - *One file, as now.* Coherent, but every skill link loads the whole file, and hosts still load nothing.
  - *One file with a summary at the top.* The summary would restate rules in a second place, against the one-home rule.
  - *Spine plus topic files* (chosen). It keeps one home per rule, and it gives every session the reasoning while loading alignment detail only for the task at hand.
- **The spine is larger than first estimated.** The scope estimated 180–220 lines. Applying the conservative rule to every passage gives about 416, because most of `process.md` is reasoning rather than action-specific detail. The researcher then added removing duplication and tightening wording to the scope ([amendment](https://github.com/Motor-Learning-Lab/HILD/issues/33#issuecomment-7078144999)). Size stays a result, not a target: the conservative rule decides what is in the spine, and the rewrite only decides how it is said.
- **Why the move and the rewrite are separate:** a verbatim move can be checked mechanically. A rewrite needs a careful reading for any change in meaning, and that reading is easier when nothing else changes at the same time.
- **What hosts gain:** at present they load no process at all. After this change they load the spine at every session start, in place of whatever an agent happens to read. HILD's own sessions load the spine instead of all 669 lines.

**Consequences:**

- [Decision 0010](0010-skill-authoring-checklist.md) gets a notice at its beginning: the checklist now lives in `HILD/process/writing-skills.md`.
- Every link to a moved section is updated: in skills, templates, `README`s, `AGENTS.md`, the installer's file list and tests, and decision records (links only). Links pinned to a commit still resolve and are left alone.
- The installer installs `HILD/process/` and generates the spine import (Claude) and the read-first line (`AGENTS.md`). `--verify` checks the new files and their links.
- A skill links to its topic file rather than to `process.md#section`.
- The work arrives as two PRs: the move, with the installer change and link updates; then the rewrite.
- Wiki pages that link to moved sections are updated after the merge, and a wiki page receives the tooling history.

**Validation:**

- **Before the rewrite merges:** the researcher reads the spine on its own and judges that it describes HILD as one coherent whole.
- **The rewrite drops nothing:** every requirement listed for a section before the rewrite is shown stated after it.
- **Mechanical:** all tests pass. In a fresh installation, `--verify` passes, `CLAUDE.md` imports the spine, and every topic file is reachable from the spine's map.
- **Behavioral:** one fresh Claude Code session in a throwaway installation handles an ordinary request and one situation no skill covers, and the researcher judges the transcripts. Codex and Copilot reading the spine through `AGENTS.md` is **not tested**.
