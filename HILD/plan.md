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
- **Live Copilot pilot completed and repository retired.** A researcher tested first contact, scope negotiation, and Copilot-only installation in a GitHub Codespace. HILD's installer was applied on a branch and its [installation PR (recorded in the pilot evidence)](https://github.com/Motor-Learning-Lab/HILD/issues/4#issuecomment-6243195811) was merged by the human in the temporary host before the researcher deleted the test repository. The transcript exposed repeated unnecessary forms, missing review/recorded approval of the **actual scope issue**, and GitHub CLI/Codespaces credential mismatches. The durable observations are in [scope #4](https://github.com/Motor-Learning-Lab/HILD/issues/4#issuecomment-6243195811). The original host and its `chat.json` are no longer accessible. Mechanical tests were reported as passing in the pilot; the full onboarding, live Copilot hook/skill behavior, wiki initialization and new-session recovery remain **unverified**.
- [PR #8](https://github.com/Motor-Learning-Lab/HILD/pull/8) was reviewed and merged at [5eebb97](https://github.com/Motor-Learning-Lab/HILD/commit/5eebb97954912f405ae7666779f214b5d6b72d40), establishing one novice onboarding companion and conversational first contact. The 2026-10-18 pilot indicates more work on review gates and access repair is necessary. The [fourth decision record](decisions/0004-selectable-agent-integrations.md) and [decision 0005](decisions/0005-conversational-scope-building.md) still say `Proposed`, pending human review of their status.

- **Pilot-derived improvements merged:** [PR #9](https://github.com/Motor-Learning-Lab/HILD/pull/9) at [2fb36a4](https://github.com/Motor-Learning-Lab/HILD/commit/2fb36a406aa817fe52f03e751699c2e78ce8c6d9) clarifies that the researcher must see and approve the actual scope issue before work starts. [PR #10](https://github.com/Motor-Learning-Lab/HILD/pull/10) at [a2b9705](https://github.com/Motor-Learning-Lab/HILD/commit/a2b9705f679fbfcd11891b0728ea0014f30fa880) supplies an environment-neutral, on-demand GitHub-access companion and nonblocking onboarding guidance about access. Post-merge [installation checks](https://github.com/Motor-Learning-Lab/HILD/actions/runs/39110721076) and [mechanical checks](https://github.com/Motor-Learning-Lab/HILD/actions/runs/39110721098) passed. **These are instructional and mechanical results, not demonstrated agent behavior.**
- **Second external onboarding pilot — Windows/VS Code Claude Code:** The human-guided [scope issue and PR](https://github.com/opherdonchin/HILD_onboarding_test/pull/2) demonstrated the revised issue-approval checkpoint, live Claude skill discovery and a first understanding wiki, while exposing Windows manifest and symlink defects, a stale journal-history lookup, a mismatched wiki status name, first-pass status-board output and an obsolete agent setup claim. The test installation is **not** a repair target; its defects are input to HILD itself. Findings were documented in [scope #4](https://github.com/Motor-Learning-Lab/HILD/issues/4#issuecomment-6253200260).
- **Corrective [draft PR #11](https://github.com/Motor-Learning-Lab/HILD/pull/11) remains OPEN / UNMERGED by agreement.** The focused fixes are now accompanied by [Windows and Linux installation CI](https://github.com/Motor-Learning-Lab/HILD/actions/runs/39152812601) and [mechanical CI](https://github.com/Motor-Learning-Lab/HILD/actions/runs/39152812593), all passed, including a native Windows symlink-and-fresh-checkout regression. **Do not merge or close this stabilization PR until a fresh separately authorized onboarding installation from that PR's unmerged commit works.**
- Repository GitHub settings agree with the squash-only decision: PR title and body as the squash message and automatic branch deletion.

## Next steps

1. **Keep [PR #11](https://github.com/Motor-Learning-Lab/HILD/pull/11) open as the candidate HILD revision.** Its Linux/Windows installer and mechanical checks are now passing; avoid using the abandoned host installation as a repair exercise.
2. **Human-controlled fresh integration test:** Agree on and create a completely new disposable repository, then guide installation and first onboarding **from the exact current PR #11 head SHA** instead of `main`. The human reviews its scope issue, proposed installer files and PR, and alone merges the test PR. Report observed vs untested abilities, especially Windows symlinks, installer verification, new wiki and agent-session orientation.
3. If the trial exposes defects, commit the minimal reproducible fix and regression test to **the still-open PR #11**, rerun CI and retest with a **new** installation. Only after it succeeds should the researcher approve and merge PR #11. Keep [scope #4](https://github.com/Motor-Learning-Lab/HILD/issues/4) open until overall acceptance criteria are met.
4. Later: separately review the status of [decision 0004](decisions/0004-selectable-agent-integrations.md), [decision 0005](decisions/0005-conversational-scope-building.md), and [decision 0006](decisions/0006-scope-issue-approval-gate.md).

## Deliberately deferred

- Integrating with an existing wiki or relocating existing authoritative research documents.
- Upgrades and three-way reconciliation of locally modified HILD installations.
- Migrating MotorAdpatationSBI or retrospectively changing its history.
- Claiming native Claude/Codex/Copilot hook behavior without an actual supported agent test.
