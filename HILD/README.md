# HILD in this repository

HILD helps a human researcher understand, direct and approve AI-assisted scientific software development. The [local process](process.md) governs this installation; the repository's [agent instructions](../AGENTS.md) define project-specific conventions.

This README is an **entry point**, not a second copy of the process. The [plan](plan.md) records current goals and next steps. The authoritative locations of any overridden files should be documented in this installation's configuration when available.

## Getting started

Open a new chat with an AI coding agent that has **access to this repository**, and give it the prompt below. A beginner should leave **onboarding** in the prompt. A researcher who already knows HILD can replace that request with the scientific or software task they actually want to scope.

> We are developing this repository using HILD. Please read the repository's agent instructions and HILD process, then use the [hild-scope skill](../.agents/skills/hild-scope/SKILL.md) to prepare our next scope.
>
> To get started, please prepare a scope addressing **onboarding**: demonstrate HILD's actual capabilities through a small, useful development cycle, and verify which ones work. Explain the proposed scope and wait for my agreement before implementing anything.

The `hild-scope` skill loads its [onboarding companion](../.agents/skills/hild-scope/onboarding-scope.md) **only** for an onboarding scope. No separate onboarding skill or mandatory onboarding run is required.

## What to expect

The scope is a proposal for human agreement. Once agreed, HILD development uses a branch and draft PR, small commits, reviewable explanations, and human approval before a squash merge. Plans, journals and decisions are persistent records. An onboarding PR may propose a `Process-HILD` understanding-map wiki page, created as a draft **after merge**, then reviewed by the human.

**Installation verification** checks files and configuration; it does **not** establish that agent behavior works. **Onboarding validation** exercises agent behavior and is optional for adopters but valuable when HILD changes substantially.

If the expected skill, wiki or hook is not installed or does not work, the agent should say so and record the gap, never silently claim success.

See the [upstream HILD project](https://github.com/Motor-Learning-Lab/HILD) for releases and documentation. An installed copy can evolve locally; updates require reconciliation rather than blind replacement.
