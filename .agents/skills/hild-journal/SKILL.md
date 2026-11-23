---
name: hild-journal
description: Records a milestone in the journal and updates the plan, so that the work survives the end of a chat. Use at each milestone the process lists (work finished and pushed; a PR opened, marked ready or merged; a result, finding or decision; provisional work under independent work; context compaction), at session start when the journal is behind Git, or when asked to log progress.
---

# Journal: record a milestone

What the plan, journal and decision records are, and which events are
milestones, is in the [HILD process, §5](../../../HILD/process.md#5-state-in-files).
How to write each is in [the plan-and-journal topic](../../../HILD/process/plan-and-journal.md)
and [the decision-records topic](../../../HILD/process/decision-records.md).
The format is the [journal-entry template](../../../HILD/templates/journal-entry.md).
Use the host's recorded locations if they are not HILD's defaults.

## Steps

1. **Find what is missing.** Compare the latest journal entry with Git
   history, open PRs and the work done since. Include work from an earlier
   session that was never recorded.
2. **Write the journal entry** in today's file, adding to the current
   session's section. Record facts and link each to its evidence: the
   commit, PR, issue, command or notebook. Under independent work, list
   each deferred approval in *Permission points*, as the process's
   [*Independent work*](../../../HILD/process.md#independent-work) requires.
3. **Point to decisions.** A consequential choice gets a decision record
   through a reviewed PR; link it, or say it is still a draft. Note smaller
   choices in the journal itself.
4. **Update the plan** so its goals, state and next steps are current.
5. **Commit and push** the milestone, on the branch you are working on or
   on `main` where the process allows it
   ([§2](../../../HILD/process.md#2-the-life-of-a-piece-of-work)).

Do not invent outcomes, backdate events you have not verified, or write
separate report files that duplicate the plan and journal.
