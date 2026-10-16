---
name: hild-scope
description: Prepare a human-agreed scope issue before substantive development in a HILD project. Use when the researcher wants to plan work, scope a change, or begin HILD onboarding.
---

# Scope

Rules: [HILD process](../../../HILD/process.md), *Scope agreements*; format:
[scope-issue template](../../../HILD/templates/scope-issue.md).
First locate the project's real plan, decisions, and process files. By default they live under `HILD/`, but a project may keep them elsewhere.

1. **Understand the goal.** Read the current plan and relevant past decisions. Explain how this work helps the project; if it does not fit an existing goal, ask about that.
2. **Agree what the work includes.** Discuss open choices before turning them into a scope issue. Identify what will and will not be done, which normal permission requirements are relaxed, and how success will be checked. Propose separate PRs if the work is too large to explain in one sitting.
3. **Onboarding only:** if the request is to scope HILD onboarding, read [onboarding-scope.md](onboarding-scope.md) now and adapt its example to this installation. Do not load that companion file for ordinary scopes.
4. **Propose the issue.** Use the [scope template](../../../HILD/templates/scope-issue.md). If GitHub is accessible, create a proposed issue labelled `scope`, then show the researcher its contents and link. If GitHub is unavailable, present the proposed text without claiming it was created.
5. **Wait for agreement.** Do not begin implementation before the researcher approves the scope. Record approval in the issue before work; if its boundaries change later, propose the amendment and wait instead of silently drifting.

The scope issue is an agreement about *future* work, not evidence that the work is already done. Do not merge a PR or certify human understanding on the researcher's behalf.
