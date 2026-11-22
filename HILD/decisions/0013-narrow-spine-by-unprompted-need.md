# 0013 — The spine holds what an agent needs without being prompted

**Date:** 2026-11-22 · **Status:** Accepted (human-reviewed and squash-merged in [PR #39](https://github.com/Motor-Learning-Lab/HILD/pull/39) on 2026-11-22; status updated in the PR that carries it out)

**Relationship to earlier decisions:** **Modifies** [decision 0012](0012-process-spine-and-topic-files.md). Still in force from 0012:
- `HILD/process.md` is a spine read at the start of every session, with topic files under `HILD/process/` read on demand;
- every agent loads the spine (*Decision* 5);
- no rule changes meaning (*Decision* 6);
- the checklist move that modified [decision 0010](0010-skill-authoring-checklist.md).

This record replaces 0012's rule for what goes in the spine, its contents (*Decision* 1, 2 and 4), and its two-step plan of a move followed by a rewrite (*Decision* 7).

**Context:** [Scope #33](https://github.com/Motor-Learning-Lab/HILD/issues/33). The first split under 0012 ([PR #37](https://github.com/Motor-Learning-Lab/HILD/pull/37)) left a 447-line spine, because 0012 kept every passage that might help an agent reason. The researcher judged the spine too broad.

A first attempt to narrow it moved whole passages. The researcher judged that badly divided: many passages mix an **essence** every agent needs with **mechanics** needed only during one activity. Examples:
- what a scope issue is, versus its label and template;
- what orientation means, versus the hook that triggers it;
- the principle for an unavailable mechanism, versus worked substitutes;
- the shape of the lifecycle, versus branch names and `archive/`.

A separate analysis divided the content within passages. The researcher approved its target list for the spine and chose to fold the independent-work mechanics into the spine.

PR #37 also departed from 0012: it moved all of presentation rules 4 and 5, where 0012 named only rule 4's GitHub detail.

**Decision:**

1. **The test for the spine.** A piece of content belongs in the spine if an agent could go wrong by not knowing it **at a moment when nothing it is doing would send it to look it up**. Otherwise it goes to a topic file, skill, template or the wiki, and the spine carries only the trigger that sends the agent there. This replaces 0012's rule that unclear passages stay in the spine.
2. **The spine has eight sections**, stated as essence: what is true and why, not how to carry out an activity. Estimated at about 185 lines.

   | § | Section | Contents |
   |---|---|---|
   | 1 | What HILD is for | The five outcomes; process versus reference implementation, which stays binding until the researcher agrees to change it. A described procedure is not evidence it is installed or tested; follow a rule by hand until its tool is verified. Paths are defaults; use the host's recorded locations. The principle for an unavailable mechanism |
   | 2 | The life of a piece of work | The diagram; one descriptive line per stage, with no mechanics; approving a scope authorizes work but does not accept its result; when direct commits to `main` are allowed |
   | 3 | The researcher's authority | Routine actions; the stopping points; staying inside the approved scope and proposing amendments; the agent never accepts or merges; **independent work, both principle and mechanics**; decision style |
   | 4 | Talking with the researcher | Each presentation is a real check of understanding; write for an unfamiliar reader; recommend a default rather than a questionnaire; one sitting, one method; "I don't get it" is a good answer; every reference is a real link, and claims about code link to exact lines |
   | 5 | State in files | State lives in files; milestones; what the plan, journal and decision records are, including that decisions arrive only by reviewed PR and are never rewritten to change the original judgment; read the relevant decision titles before deciding or changing anything in an area; what to read at session start; what orientation means |
   | 6 | Understanding | Only the researcher judges their understanding; the map is never authoritative; accepting a PR does not make a page understood |
   | 7 | Rules at every step | Credentials; branch first; merge only through a reviewed PR, as a squash merge; push at milestones; commit messages say why; the 🤖 prefix; never rewrite a pushed PR branch; never stop while waiting for a merge |
   | 8 | The map | Where each thing lives; the three kinds of tool; how to change a rule; the topic files and when to read each |

3. **Eight topic files**, each read before the activity it names:

   | Topic file | Read before | Gains, compared with PR #37 |
   |---|---|---|
   | `scope.md` | proposing, creating, recording approval of, or amending a scope issue | the four scope questions as a description rather than a form; the template and label; amendments link to the original issue; the onboarding pointer |
   | `review.md` | writing a proposal or PR explanation, asking for review, or responding to it | loses rule 4's general half to §4 and the "not understood by acceptance" line to §6 |
   | `git.md` | creating a branch, opening or finishing a PR, committing to `main`, preparing a merge, or changing merge settings | branch naming; opening a draft PR at the first push |
   | `plan-and-journal.md` (new) | writing or updating the plan or a journal entry | how each is written: rewrite in place, file naming, sessions, template, history, the compaction note |
   | `decision-records.md` | creating, changing or superseding a decision record | how one decision modifies, overrules or replaces another; loses "read titles first" to §5 |
   | `understanding-map.md` | creating or changing an understanding-map page or its status | the wiki's location and setup |
   | `installation.md` (new) | assessing, installing, upgrading or reconciling HILD in a repository, or agreeing a substitute for an unavailable mechanism | host-configured locations; installed HILD is local; worked substitutes; the read-only assessment rule |
   | `writing-skills.md` | writing or changing a skill | unchanged |

4. **Removed from the process:**
   - the origin paragraph, which `AGENTS.md` and the wiki already carry;
   - the presentation table and the *Process:* and *Implementation:* labels, whose content the sections now state directly;
   - copies of a rule stated elsewhere. Each rule keeps one statement; the independent-work rule, for example, is stated once, in §3.
5. **Rules that lived only in a skill get a home:**
   - "a short OK or a technical choice is not an independent-work mandate" (§3);
   - "do not begin unapproved nontrivial work before the researcher responds" (§3);
   - where milestone commits go during open work (`plan-and-journal.md`). This is recorded as currently unspecified, as the process says, and the skill's contradictory wording is noted for the skill rewrites.
6. **Stale text is corrected:**
   - the wiki is "not yet configured";
   - "(placement to be verified)" and "(when ported)" in the homes table;
   - scope #4 described as still planned.

   "Researcher" replaces "reviewer" throughout.
7. **One PR, replacing PR #37.**
   - The spine is newly written as essence sentences.
   - Text moving to topic files keeps its wording, apart from what the move requires.
   - The PR lists every passage of the old `process.md` with its destination, and every rule's single home, so nothing dropped can go unnoticed.
   - Tightening the moved topic text, and removing restated rules from skills and templates, are deferred: the skill and template trimming to the [scope #18](https://github.com/Motor-Learning-Lab/HILD/issues/18) rewrites.

**Why:**

- **Unprompted need is the right test** because the spine's job is the moments when no skill or task points anywhere. Anything an activity reliably triggers can wait for that trigger. 0012's rule, "unclear stays in", guaranteed coherence but not a usable size.
- **Dividing within passages** keeps each idea's meaning in the spine while removing how-to detail. Moving whole passages either lost the meaning or kept the detail.
- **Independent work stays whole in the spine,** at the researcher's choice. Its mechanics are short, a miss is costly, and an agent may slide into independent work without a clear moment that would send it to a topic file.
- **The two added rules** (never rewrite a pushed branch; never stop while waiting for a merge) pass the test: nothing prompts a lookup when an agent rebases or idles.
- **"Read the relevant decision titles first" moves to the spine** because [PR #32](https://github.com/Motor-Learning-Lab/HILD/pull/32) showed the cost of missing it.
- **One PR instead of a move then a rewrite:** the spine's essence sentences are new writing by nature, so a verbatim first step would only be reworked again. The per-passage listing gives the same assurance that nothing was lost.

**Consequences:**

- [Decision 0012](0012-process-spine-and-topic-files.md) gets a notice at its beginning, and its status becomes `Accepted` (it was merged in [PR #36](https://github.com/Motor-Learning-Lab/HILD/pull/36)).
- PR #37 is closed unmerged. Its verbatim-check approach is reused for the text that moves to topic files.
- The installer change from PR #37 is carried into the new PR: the topic files, the spine import in `CLAUDE.md`, the read-first line in `AGENTS.md`, and the `--verify` check.
- Links into renamed sections are updated: in skills, `onboarding-scope.md`, `github-access.md`, templates, scripts and decision records (links only). `--verify` does not check anchors, so the PR lists them.
- The scope #18 skill rewrites remove restated rules from skills and templates, pointing to the spine section or topic file.

**Validation:**

- **Before the new PR merges:**
  - the researcher reads the spine on its own and judges that it describes HILD as one coherent whole;
  - the per-passage listing shows every rule's single home.
- **Mechanical:** all tests pass. A fresh installation passes `--verify`, imports the spine, and reaches every topic file from the map.
- **Behavioral:** one fresh session in a throwaway installation handles an ordinary request and one situation no skill covers. The decision-record case from PR #37 is repeated. The researcher judges the transcripts. Codex and Copilot are **not tested**.
