# HILD — Human-in-the-Loop Development

HILD is a **human-supervised development process** for scientific software created with AI agents. The goal isn't merely working code: the researcher remains in control of development decisions and develops an understanding of the code and algorithms. HILD requires explicit, reviewable work agreements, inspectable changes, evidence-based review, durable project knowledge and researcher-confirmed understanding.

**GitHub, Git branches and pull requests, agent skills and hooks, journals and an understanding wiki are our recommended reference implementation** of that process, not its definition. An agent and researcher may adapt those mechanisms to their actual environment if the essential human-control and understanding functions remain intact and the alternatives are agreed and documented.

## Status

**The first-time installer is available; guided onboarding is being validated.** [Scope #4](https://github.com/Motor-Learning-Lab/HILD/issues/4) is testing HILD with an actual new repository.

- [PR #5](https://github.com/Motor-Learning-Lab/HILD/pull/5) added the reusable skills, onboarding guidance and wiki templates.
- [PR #6](https://github.com/Motor-Learning-Lab/HILD/pull/6) added tested orientation and wiki-staleness scripts and optional agent setup templates.
- [PR #7](https://github.com/Motor-Learning-Lab/HILD/pull/7) merged the preview-first installer, agent selection and mechanical verification. **Live agent startup, wiki creation and an end-to-end onboarding cycle are still unverified.**

The [current plan](HILD/plan.md) distinguishes implemented, mechanically tested and unverified capabilities.

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

HILD preserves the *process requirements* of bounded authorization, independently inspectable work, meaningful explanation/review, durable decisions and progress, and researcher-confirmed understanding. The initial *GitHub reference implementation* uses scope issues, early draft PRs, small commits, plans, journals and an understanding wiki. Project-specific scientific conventions remain in the host project.

## Developing HILD with HILD

**HILD's own development follows HILD.** Proposed changes begin with a human-agreed scope, proceed through small commits and a reviewable PR, and are documented through explanations, decisions, and durable project state. This is an ongoing real-world test of whether the process is understandable and useful—not a claim that every supporting skill or hook is already implemented.

The [project instructions](AGENTS.md) direct coding agents to follow the [HILD process](HILD/process.md), and the [plan](HILD/plan.md) tracks what is currently implemented and still missing.

## Read-only adoption assessment

The [`hild-integrate` skill](.agents/skills/hild-integrate/SKILL.md) starts with a **read-only assessment**. It also introduces HILD to the researcher and helps develop an installation scope through conversation, so the first work is useful to the researcher's own project.

To begin, open a chat with an agent that can access your repository. Give it the [upstream integration skill](https://github.com/Motor-Learning-Lab/HILD/blob/main/.agents/skills/hild-integrate/SKILL.md) and your target repository, then ask:

> I want to learn HILD and use it in this repository. Please read the HILD README, integration skill and process, and assess my repository without making changes. Explain what HILD can help me achieve here, then work with me to **develop our first installation scope**. Don't create an issue or modify the repository until we agree on the scope.

The first conversation is meant to **build shared understanding**, not make the researcher approve a lengthy installation specification immediately. A scope issue records the finished agreement; it does not replace the conversation that leads to it. For a reproducible assessment, pin an exact upstream commit.

The default installation location is `HILD/`. The [preview-first installer](HILD/scripts/install_hild.py) currently supports **new, minimally initialized Git repositories** after explicit approval. Existing-repository integration, upgrading locally modified installations, and three-way reconciliation remain **unimplemented**; established knowledge must never be overwritten silently.

## Starting work with HILD

After HILD is installed, open an agent chat **with access to your repository** and ask it to read the project instructions and invoke `hild-scope`. The [installed HILD README](HILD/README.md) supplies a ready-to-copy prompt:

> We are developing this repository using HILD. Please read its agent instructions and HILD process, then use `hild-scope` to **develop** our next scope with me. I'm new to HILD, so please also read its onboarding companion and help me learn through the conversation. I want to begin with onboarding, but don't create an issue or make changes until we've agreed on the scope.

**Onboarding is recommended for new users, not required.** Experienced researchers can replace it with their actual first development task. The scope skill reads its [onboarding companion](.agents/skills/hild-scope/onboarding-scope.md) only when onboarding is requested. A completed onboarding exercise may propose a fresh `Process-HILD` wiki draft for creation after the PR merges.

The skills, scripts and installer are on `main`, with mechanical checks, but **installed files are not evidence of agent behavior**. The real onboarding cycle, GitHub wiki publishing and agent runtime compatibility are being tested under [scope #4](https://github.com/Motor-Learning-Lab/HILD/issues/4).

## Contributions

Read [AGENTS.md](AGENTS.md), [the process](HILD/process.md), and [the current plan](HILD/plan.md) before substantive work. Scope agreements precede implementation. Branches are squash-merged only after the researcher's explicit approval.
