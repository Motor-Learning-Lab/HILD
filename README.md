# HILD — Human-in-the-Loop Development

HILD is a reusable, human-supervised process for developing scientific software with AI coding agents. The goal is not just working code: the researcher should understand what is built, why it works, what has been checked, and what remains uncertain.

## Status

**Foundation under development.** This repository does not yet offer a complete installer or an operational `hild-integrate` skill. Do not assume HILD has been installed in another repository.

- [Agreed scope #1](https://github.com/Motor-Learning-Lab/HILD/issues/1) separates the foundation from the first read-only integration procedure.
- [HILD's process](HILD/process.md) governs development in this repository. Some supporting skills, hooks, and the understanding map described there are **not yet ported**; their status is recorded in [the plan](HILD/plan.md).

## Where to start

This repository has different entry points for **people** and **coding agents**.
They are not competing sources of process rules.

| File | Audience and purpose |
|---|---|
| **[README.md](README.md)** (this page) | Public introduction: why HILD exists, whether it is ready to use, and how adoption will work |
| **[AGENTS.md](AGENTS.md)** | Starting point for an agent **working on HILD itself**: project-specific instructions and links to the authoritative process, plan and decisions |
| **[HILD/process.md](HILD/process.md)** | Authoritative description of how the human reviewer and the agent collaborate |
| **[HILD/plan.md](HILD/plan.md)** | Current development state, open questions and next steps |

When HILD is adopted into an **existing** repository, its current root
`AGENTS.md` (or equivalent) remains the project's own instruction file.
Integration should propose a short link to the HILD process, **not overwrite
that file with this repository's AGENTS.md**.

## Origins and design constraints

HILD is extracted from the working process developed in [MotorAdpatationSBI](https://github.com/opherdonchin/MotorAdpatationSBI). Its starting points are [scope #5](https://github.com/opherdonchin/MotorAdpatationSBI/issues/5), [PR #6](https://github.com/opherdonchin/MotorAdpatationSBI/pull/6), [PR #7](https://github.com/opherdonchin/MotorAdpatationSBI/pull/7), and its current [process specification](https://github.com/opherdonchin/MotorAdpatationSBI/blob/main/docs/process.md).

HILD preserves scope agreements, early draft PRs, small commits, layered explanations, human review tracks, durable plans and journals, decisions, and a researcher-confirmed understanding map. Project-specific scientific conventions remain in the host project.

## Developing HILD with HILD

**HILD's own development follows HILD.** Proposed changes begin with a human-agreed scope, proceed through small commits and a reviewable PR, and are documented through explanations, decisions, and durable project state. This is an ongoing real-world test of whether the process is understandable and useful—not a claim that every supporting skill or hook is already implemented.

The [project instructions](AGENTS.md) direct coding agents to follow the [HILD process](HILD/process.md), and the [plan](HILD/plan.md) tracks what is currently implemented and still missing.


## Adoption (planned)

An agent should first read the upstream `hild-integrate` procedure **without requiring HILD to be installed**. Its first action is a read-only assessment of existing rules, project knowledge, working tree and history. It proposes an adoption or reconciliation plan and stops for human agreement before any changes.

The default is a contained `HILD/` directory; existing repositories can keep their own authoritative files elsewhere through configured paths. Local installations are reconciled with upstream, never blindly replaced.

## Contributions

Read [AGENTS.md](AGENTS.md), [the process](HILD/process.md), and [the current plan](HILD/plan.md) before substantive work. Scope agreements precede implementation. Branches are squash-merged only after the researcher's explicit approval.
