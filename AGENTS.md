# Agent instructions — HILD

## Purpose and authority

This repository develops HILD, a reusable **human-supervised development process** for AI-assisted scientific software. Its essential requirements concern researcher authority, inspectable agreements and changes, evidence-based review and durable understanding; GitHub/skills/hooks provide the current reference implementation.

This root `AGENTS.md` governs work **on HILD itself**. It is not a file that `hild-integrate` copies into host repositories: an existing project's agent instructions remain authoritative, with a proposed pointer to its locally installed HILD process.

**Read [the HILD process](HILD/process.md) first.** It defines scope agreements, approval tracks, explanation format, durable state, decision records, autonomy, git workflow and the understanding map. Do not copy or reinterpret those rules here.

The original working process is in [MotorAdpatationSBI](https://github.com/opherdonchin/MotorAdpatationSBI/blob/main/docs/process.md); relevant history is [issue #5](https://github.com/opherdonchin/MotorAdpatationSBI/issues/5), [PR #6](https://github.com/opherdonchin/MotorAdpatationSBI/pull/6), [PR #7](https://github.com/opherdonchin/MotorAdpatationSBI/pull/7). Preserve its actual decisions and documented subsequent changes. Do not turn HILD into a generic checklist.

## Current project

- [Plan](HILD/plan.md): current state and next steps.
- [Decision records](HILD/decisions/): choices, alternatives, consequences.
- [Journal](HILD/journal/): milestone history.
- [Scope #1](https://github.com/Motor-Learning-Lab/HILD/issues/1): first approved scope, divided into foundation and bootstrap PRs.

Develop HILD **using HILD**. Keep changes small, reviewable, reversible, and on branches with draft PRs. No unapproved scope expansion and no merge without the human reviewer.

## Project-specific guidance

- Favor minimal, explicit procedures over abstractions or complex automation.
- Do not modify or reorganize MotorAdpatationSBI as part of building HILD.
- An initial integration assessment is read-only, including GitHub state; do not run unknown scripts or hooks while assessing.
- Distinguish agreed design, proposals, implemented behavior, tests and outstanding questions.
- No claims that unported skills, integrations or hooks work; verify them when they exist.
- Skills and agent configurations live where agents discover them; keep authoritative policy and project knowledge at their recorded homes.
