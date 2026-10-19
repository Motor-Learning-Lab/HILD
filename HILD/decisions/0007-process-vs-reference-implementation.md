# 0007 — Distinguish HILD process requirements from reference mechanisms

**Date:** 2026-10-18 · **Status:** Proposed; awaiting human review under [scope #12](https://github.com/Motor-Learning-Lab/HILD/issues/12).

## Context

The early HILD implementation grew around GitHub issues, draft pull requests, a separate wiki, Git-based state and agent-discovered skills. These tools serve HILD well, but describing them as **HILD itself** can cause agents to treat an unavailable mechanism as a failed process—or improvise by dropping an essential human safeguard. The Windows/VS Code pilot showed why agents and researchers need to collaborate on platform-dependent solutions.

## Proposed decision

**HILD is a human-supervised development process.** Its essential requirements concern:

- Inspectable authority for bounded work, with explicitly authorized independent work remaining provisional wherever ordinary approvals are deferred
- Proposed changes kept reviewable before acceptance
- Evidence and interconnected explanations that enable meaningful human review and acceptance at an appropriate depth
- Durable goals, progress, decisions and tests beyond one chat session
- Researcher-confirmed *current* understanding, including the right to retract confirmation

**GitHub issues, PRs, Git history, plan/journal Markdown files, understanding wikis and agent skills/hooks are the currently supported reference implementation** of these requirements. They remain our recommended, documented default rather than being removed or vaguely generalized.

The researcher may change process conventions as well as implementation
conventions through the reviewed decision procedure. For example, the
approximately fifteen-minute explanation limit is a process convention;
GitHub's exact code permalink syntax implements the process requirement for
interconnected knowledge and evidence. All PRs require human acceptance
regardless of review depth or whether the human used a PR comment.

When a reference mechanism is unsuitable, the agent explains **the function it serves**, proposes a feasible equivalent with the researcher, records the agreed departure and tests the alternative where practicable. The substitute must preserve authorization, durability, inspectability, human review and understanding. For example, a persistent non-GitHub scope record can substitute for a scope issue **only if** the researcher actually reviews and approves it and future sessions can recover that approval; a chat summary by itself cannot.

## Rationale and alternatives

A fully implementation-agnostic toolkit or general adapter framework is premature. Conversely, identifying HILD with one platform makes it brittle and understates the agent's responsibility to understand the process. We keep actual, specific procedures alongside the requirements they
implement: first state a rule independently of tools where possible, then
give its concrete convention. Entire sections may be process-only or
implementation-only. A binding implementation convention is not automatically
optional merely because it is not fundamental to the process.

## Consequences and validation

The [authoritative process](../process.md) defines this distinction and a
forward-linked decision-supersession convention: a later decision may modify,
overrule or replace an earlier one, explaining what remains effective, while
the older record retains its historical reasoning with a visible notice at
the beginning. [Proposed decision 0008](0008-independent-work-and-human-acceptance.md)
would qualify [decision 0006](0006-scope-issue-approval-gate.md) regarding
explicitly authorized independent work, without treating delegation as
human acceptance.

 Public and installed READMEs introduce HILD in those terms; agent skills identify their purpose and reference workflow; templates distinguish objectives from mechanisms. The [digest skill](../../.agents/skills/hild-digest/SKILL.md) checks whether later documentation blurs the boundary.

This decision **does not** implement or validate non-GitHub backends, waive scope review or authorize agents to merge on the researcher's behalf. An upcoming guided onboarding exercise should demonstrate that agents understand the essential requirements while using the reference GitHub implementation. Further alternatives require their own agreed scope and evidence.
