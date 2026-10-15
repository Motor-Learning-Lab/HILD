---
name: hild-orient
description: Present a concise start-of-session orientation about project progress, pending human reviews, understanding debt, and next work. Use on session start or when asked where the project stands.
---

# Orient

Rules: [HILD process](../../../HILD/process.md), *Presentations* and *Durable state files*. Resolve any configured authoritative paths before acting.

1. **Gather facts.** Use orientation data from a configured startup hook if available. Otherwise read the project's plan, latest journal, recent commits, working tree, open issues/PRs and understanding-map status. The reference `HILD/scripts/session_context.sh` (once installed) can supply these facts; do not assume it has run or exists.
2. **Catch up the record.** Identify unrecorded milestones or unpushed wiki changes. Report them; follow the `hild-journal` or `hild-understood` procedures within an agreed scope, not by silently inventing history.
3. **Present** in about fifteen lines, leading with what needs the human:
   - **Needs you:** PRs awaiting review and proposed approval tracks, scope issues awaiting agreement, questions, wiki pages to read.
   - **Where we are:** current goal and state.
   - **Since last time:** material changes, with links.
   - **Understanding debt:** open issues and stale/needs-review pages, if tracked.
   - **Next:** the next plan step and what is proposed now.
4. **Wait.** Do not start nontrivial development before the reviewer responds unless an agreed scope explicitly covers continuing work.

A hook firing is not evidence that orientation was delivered or understood. If an information source is unavailable, say so rather than filling it in from memory.
