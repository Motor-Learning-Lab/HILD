# HILD plan

The living plan records goals, current state and next steps. History is recorded in Git and the [journal](journal/2026-10-17.md).

## Goals

1. Develop HILD using its own human-supervised development process.
2. Provide a reusable first-time installation with clear authority, agent selection and mechanical verification.
3. Validate the installed process through genuine human-agent onboarding in a fresh repository.
4. Later, preserve and reconcile existing installations and project knowledge, beginning with MotorAdpatationSBI.

## Current state — 2026-10-17

- [Scope #1](https://github.com/Motor-Learning-Lab/HILD/issues/1) is complete. [Scope #4](https://github.com/Motor-Learning-Lab/HILD/issues/4) is approved and remains **open** for onboarding validation.
- [PR #5](https://github.com/Motor-Learning-Lab/HILD/pull/5) merged the reusable HILD skills, onboarding guidance and wiki templates.
- [PR #6](https://github.com/Motor-Learning-Lab/HILD/pull/6) merged orientation and wiki-staleness scripts, regression tests, new-wiki instructions and optional agent hook templates.
- [PR #7](https://github.com/Motor-Learning-Lab/HILD/pull/7) was **human-reviewed and squash-merged** at [3c3a32d](https://github.com/Motor-Learning-Lab/HILD/commit/3c3a32d4a8a6f2973f21b696c016bd33da9b546d) on 2026-10-17 Israel time. It supplies a preview-first installer for minimally initialized repositories, selected agents (default all), and installation verification.
- Both post-merge GitHub Actions workflows **passed**: [installation checks](https://github.com/Motor-Learning-Lab/HILD/actions/runs/38971254235) and [mechanical checks](https://github.com/Motor-Learning-Lab/HILD/actions/runs/38971254359). Earlier complete-source installation tests passed in temporary local Git repositories.
- HILD has **not** yet been installed into a live GitHub host project. No real wiki initialization, agent-native skill discovery, live hook operation or complete onboarding cycle has been verified. The [fourth decision record](decisions/0004-selectable-agent-integrations.md) still says `Proposed` and requires a reviewed PR to update its accepted status following PR #7's merge.
- Repository GitHub settings agree with the squash-only decision: PR title and body as the squash message and automatic branch deletion.

## Next steps

1. Obtain explicit agreement on a **disposable test repository**, proposed as a public `Motor-Learning-Lab/HILD-onboarding-test` initialized with a README, and on enabling/creating its **new** GitHub wiki. Do not create or mutate either before agreement; never touch an existing wiki.
2. Conduct the [onboarding scope exercise](../.agents/skills/hild-scope/onboarding-scope.md): read-only assessment, approved installation plan, target scope issue, branch/draft PR, useful initialization, real reviewer decisions and approval, verified squash merge, post-merge `Process-HILD` wiki draft and fresh-session orientation.
3. Record observed capability evidence separately from file/configuration checks, including missing or unavailable agent integrations; treat partial support as partial rather than complete success. The test should begin with one agent that can actually be exercised; additional platforms need their own observations.
4. Complete the outstanding reviewed decision-record status update and document the results in a small HILD PR. Close [scope #4](https://github.com/Motor-Learning-Lab/HILD/issues/4) only when the agreed validation criteria are met or amended by the researcher.

## Deliberately deferred

- Integrating with an existing wiki or relocating existing authoritative research documents.
- Upgrades and three-way reconciliation of locally modified HILD installations.
- Migrating MotorAdpatationSBI or retrospectively changing its history.
- Claiming native Claude/Codex/Copilot hook behavior without an actual supported agent test.
