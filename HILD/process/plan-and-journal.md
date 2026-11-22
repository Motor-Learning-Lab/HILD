# Plan and journal — HILD process topic

Part of the [HILD process](../process.md), which every session reads first.
Read this file before writing or updating the plan or a journal entry. What
each record is, and the milestones at which both are updated, are in the
process, [§5](../process.md#5-state-in-files).

## Plan — `HILD/plan.md` (default)

- **When to update:** at milestones, whenever a goal, the state, or the next steps
  change.
- **How:** rewrite in place; the old versions are in `main`'s history.
- **Where between milestones:** not yet specified. The process does not yet say
  on which branch a plan update made during open work is committed.

## Journal — `HILD/journal/YYYY-MM-DD.md` (default)

- One file per day; a second session on the same day adds a new
  `## Session N` section.
- **When to update:** at milestones. Each update adds to the current session's
  section, so the entry is always complete up to the last milestone.
- **Format:** [the journal-entry template](../templates/journal-entry.md).
- **When to read:** earlier entries when resuming a thread
  of work (search by topic).
- Entries are history: do not rewrite past entries except to fix errors, and say so.

## Compaction

When context is compacted, hooks ask the summary to keep unrecorded milestones and remind
the agent to record them straight afterwards.
