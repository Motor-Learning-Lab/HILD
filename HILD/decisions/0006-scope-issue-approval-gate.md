# 0006 — Review the actual scope issue before implementation

> **Proposed partial supersession (not yet accepted):**
> [Decision 0008 — Independent work, provisionality and human acceptance](0008-independent-work-and-human-acceptance.md)
> would permit *explicitly authorized independent execution* to continue past
> ordinary scope checkpoints, while keeping unapproved choices and dependent
> work provisional pending human review. This record's normal supervised
> scope-approval gate remains the default. The original decision below is
> retained as historical evidence; decision 0008 is not operative unless
> accepted by human review and merge of its PR.


**Date:** 2026-10-18 · **Status:** Proposed; pending review in [PR #9](https://github.com/Motor-Learning-Lab/HILD/pull/9).

## Context

The first real [HILD-onboarding-test](https://github.com/Motor-Learning-Lab/HILD/issues/4#issuecomment-6243195811) showed that a coding agent could agree conversationally on a scope, create its GitHub issue, then proceed toward installation without stopping for the researcher to review and approve the **actual issue**. The issue received no approval comment. The agent separately obtained permission for the installer preview, which did not remedy the scope-approval omission.

## Decision proposed

A scope has **two distinct agreements**: permission to *record a proposed issue* and approval of that **specific issue's contents** as the contract for implementation.

After creating the issue, the agent provides its GitHub link, summarizes what it permits and excludes, and stops. The researcher reviews that issue and explicitly approves or requests revision. Before any implementation starts, approval must be recorded on the issue itself: either the researcher's own GitHub comment or an accurately attributed agent comment recording an approval given in chat. Material changes to the scope require renewed approval.

The installer preview, project changes and PR review have their **own** approval decisions. A short conversational "OK" about plans or a link given in a status report is not a substitute for explicit approval of the issue.

## Why and consequences

The durable issue is the boundary on the agent's authority. The researcher needs an accessible artifact to review and a clear opportunity to correct it **before** changes begin. This adds one meaningful stopping point rather than an extensive extra questionnaire. Agents must be able to proceed even if approval occurs in chat, provided the approval is correctly represented on GitHub.

The [process](../process.md) defines this gate; [hild-scope](../../.agents/skills/hild-scope/SKILL.md) gives the ordinary procedure; the [fresh-install companion](../../.agents/skills/hild-integrate/first-install.md) checks that approval exists. No automated GitHub enforcement is claimed.

## Validation

Test in a fresh agent session: after informal scoping, the agent creates a **proposed** issue, links it, pauses for human approval of its exact content and records that approval; without approval, it makes no implementation changes. Also test a revision request. This remains **untested** until observed in a live session.
