---
name: hild-journal
description: Record a development milestone in the durable journal and update the living plan. Use after pushes, PR state changes, results, decisions, or compaction, or on a request to log progress.
---

# Journal

Rules: [HILD process](../../../HILD/process.md), *Durable state files*.
Formats: [journal entry](../../../HILD/templates/journal-entry.md) and
[decision record](../../../HILD/templates/decision-record.md).

1. **Find unrecorded work.** Compare the latest journal entry, Git history, open PRs and the current work. Resolve the host's authoritative plan, journal and decision locations; the defaults are `HILD/plan.md`, `HILD/journal/`, `HILD/decisions/`.
2. **Record facts** in `YYYY-MM-DD.md` at the configured journal location. Append within the current session; a second session on the same date gets another session heading. Link material results to the command, source, notebook or commit that produced them.
3. **Decisions:** record important, non-obvious decisions through reviewed PRs in the configured decision directory; never declare them accepted merely because the agent drafted them. Small choices go in the journal.
4. **Update the plan** in place with current goals, actual state and ordered next steps; git history preserves older versions.
5. **Commit and push** the milestone within the agreed branch/scope, or on `main` after merge where allowed by the process.

Do not invent outcomes, backdate unverified events, or create separate report files that duplicate the plan and journal.
