# HILD — Human-in-the-Loop Development

HILD is a reusable, human-supervised process for developing scientific software with AI coding agents. The goal is not just working code: the researcher should understand what is built, why it works, what has been checked, and what remains uncertain.

## Status

**Governance foundation merged; read-only bootstrap under review.** This repository does not yet offer an installer, automated upgrade, or tested cross-agent hooks. Do not assume HILD has been installed in another repository.

- [Agreed scope #1](https://github.com/Motor-Learning-Lab/HILD/issues/1) separates the [merged foundation PR #2](https://github.com/Motor-Learning-Lab/HILD/pull/2) from [read-only bootstrap PR #3](https://github.com/Motor-Learning-Lab/HILD/pull/3).
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


## Read-only adoption assessment (available for review)

The first [`hild-integrate` skill](.agents/skills/hild-integrate/SKILL.md) is a **procedure for assessing**, not installing, HILD. Its initial implementation is in [PR #3](https://github.com/Motor-Learning-Lab/HILD/pull/3) and is not yet merged.

To ask an agent to assess a scientific repository **before** HILD is installed, give it the upstream [skill URL on main](https://github.com/Motor-Learning-Lab/HILD/blob/main/.agents/skills/hild-integrate/SKILL.md) **after PR #3 merges** (until then, use the relative review link above) and the repository to assess, and tell it: *read that procedure, assess this repository read-only, propose a scope, and stop without making changes*. Once the PR is merged, use the URL on `main`; for reproducible assessments pin a commit.

The default installation location will be `HILD/`, with per-role overrides for existing authoritative files. **Installing, upgrading and three-way reconciliation are not yet implemented.** Each will require a separately approved scope.

## Contributions

Read [AGENTS.md](AGENTS.md), [the process](HILD/process.md), and [the current plan](HILD/plan.md) before substantive work. Scope agreements precede implementation. Branches are squash-merged only after the researcher's explicit approval.
