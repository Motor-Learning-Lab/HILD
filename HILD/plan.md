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
- A fresh agent completed a **read-only assessment** of [opherdonchin/HILD-onboarding-test](https://github.com/opherdonchin/HILD-onboarding-test), a new repository containing a README. The assessment respected the no-write boundary, but the human found its response over-detailed and prematurely technical; [PR #8](https://github.com/Motor-Learning-Lab/HILD/pull/8) proposes conversational guidance before continuing this validation. **No installation, wiki initialization, native skill discovery, live hook operation or full onboarding cycle has been verified.** The [fourth decision record](decisions/0004-selectable-agent-integrations.md) still says `Proposed` and requires a reviewed PR to update its accepted status.
- Repository GitHub settings agree with the squash-only decision: PR title and body as the squash message and automatic branch deletion.

## Next steps

1. Review [PR #8](https://github.com/Motor-Learning-Lab/HILD/pull/8). Subsequent review comments prompted a positive, concrete explanation of where HILD works, better first-task suggestions for current versus outdated installations, and a cleaner division between newcomer onboarding (one companion) and experienced integration dialogue. Verify those changes and obtain human read-track approval before merging.
2. **Repeat the first-contact experiment** with a fresh agent after that change merges. Check whether it introduces HILD's purpose, connects it to the researcher's project, invites scope-building rather than presenting a finished agreement, and respects read-only and approval boundaries.
3. Continue the test in the existing [opherdonchin/HILD-onboarding-test](https://github.com/opherdonchin/HILD-onboarding-test) repository only through a human-approved scope: install into the clean checkout, check files/configuration, and validate a real HILD onboarding cycle, wiki and fresh-session recovery.
4. Update the still-`Proposed` status of [decision 0004](decisions/0004-selectable-agent-integrations.md) via a reviewed PR, and close [scope #4](https://github.com/Motor-Learning-Lab/HILD/issues/4) only when its validation goals are met or amended.

## Deliberately deferred

- Integrating with an existing wiki or relocating existing authoritative research documents.
- Upgrades and three-way reconciliation of locally modified HILD installations.
- Migrating MotorAdpatationSBI or retrospectively changing its history.
- Claiming native Claude/Codex/Copilot hook behavior without an actual supported agent test.
