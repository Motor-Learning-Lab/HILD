# HILD plan

The living plan records goals, current state and next steps. History is recorded in Git and the [latest journal](journal/2026-10-18.md).

## Goals

1. Develop HILD using its own human-supervised development process.
2. Provide a reusable first-time installation with clear authority, agent selection and mechanical verification.
3. Validate the installed process through genuine human-agent onboarding in a fresh repository.
4. Later, preserve and reconcile existing installations and project knowledge, beginning with MotorAdpatationSBI.

## Current state — 2026-10-18

- [Scope #1](https://github.com/Motor-Learning-Lab/HILD/issues/1) is complete. [Scope #4](https://github.com/Motor-Learning-Lab/HILD/issues/4) is approved and remains **open** for onboarding validation.
- [PR #5](https://github.com/Motor-Learning-Lab/HILD/pull/5) merged the reusable HILD skills, onboarding guidance and wiki templates.
- [PR #6](https://github.com/Motor-Learning-Lab/HILD/pull/6) merged orientation and wiki-staleness scripts, regression tests, new-wiki instructions and optional agent hook templates.
- [PR #7](https://github.com/Motor-Learning-Lab/HILD/pull/7) was **human-reviewed and squash-merged** at [3c3a32d](https://github.com/Motor-Learning-Lab/HILD/commit/3c3a32d4a8a6f2973f21b696c016bd33da9b546d) on 2026-10-17 Israel time. It supplies a preview-first installer for minimally initialized repositories, selected agents (default all), and installation verification.
- Both post-merge GitHub Actions workflows **passed**: [installation checks](https://github.com/Motor-Learning-Lab/HILD/actions/runs/38971254235) and [mechanical checks](https://github.com/Motor-Learning-Lab/HILD/actions/runs/38971254359). Earlier complete-source installation tests passed in temporary local Git repositories.
- A fresh agent completed a **read-only assessment** of [opherdonchin/HILD-onboarding-test](https://github.com/opherdonchin/HILD-onboarding-test), which currently contains only a README on GitHub. The assessment respected the no-write boundary but was too installation-focused. The researcher reviewed and [squash-merged PR #8](https://github.com/Motor-Learning-Lab/HILD/pull/8) at [5eebb97](https://github.com/Motor-Learning-Lab/HILD/commit/5eebb97954912f405ae7666779f214b5d6b72d40), establishing purpose-led introductions and **one authoritative onboarding companion**. [Post-merge installation checks](https://github.com/Motor-Learning-Lab/HILD/actions/runs/39071260182) and [mechanical checks](https://github.com/Motor-Learning-Lab/HILD/actions/runs/39071260177) passed. **No installation, wiki initialization, native skill discovery, live hook operation or full onboarding cycle has been verified.** The fourth [decision record](decisions/0004-selectable-agent-integrations.md) remains `Proposed` pending a reviewed status update.
- Repository GitHub settings agree with the squash-only decision: PR title and body as the squash message and automatic branch deletion.

## Next steps

1. **Repeat the read-only first-contact test** in a fresh agent chat with [opherdonchin/HILD-onboarding-test](https://github.com/opherdonchin/HILD-onboarding-test), using the merged [`hild-integrate` skill](../.agents/skills/hild-integrate/SKILL.md) and the [onboarding companion](../.agents/skills/hild-scope/onboarding-scope.md) at [5eebb97](https://github.com/Motor-Learning-Lab/HILD/commit/5eebb97954912f405ae7666779f214b5d6b72d40). Check whether it introduces HILD's value, connects it to the researcher's own repository, and invites a shared scope before discussing detailed installation; then observe the actual dialogue after "yes".
2. Record first-contact evidence separately from mechanical checks: meaningful dialogue, safety boundaries, access limitations, and which native capabilities were or were not exercised. Avoid implying installation is complete from a successful conversation.
3. Continue the real onboarding test only with a **separately human-approved scope**: install into a clean checkout, verify configuration, and test genuine development, review, wiki and fresh-session recovery without touching existing authority.
4. Update [decision 0004](decisions/0004-selectable-agent-integrations.md) from `Proposed` only through a reviewed PR; likewise review the new [decision 0005](decisions/0005-conversational-scope-building.md) status if needed. Close [scope #4](https://github.com/Motor-Learning-Lab/HILD/issues/4) only when agreed validation criteria have been met or amended.

## Deliberately deferred

- Integrating with an existing wiki or relocating existing authoritative research documents.
- Upgrades and three-way reconciliation of locally modified HILD installations.
- Migrating MotorAdpatationSBI or retrospectively changing its history.
- Claiming native Claude/Codex/Copilot hook behavior without an actual supported agent test.
