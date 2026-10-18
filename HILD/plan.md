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
- **Live Copilot pilot completed and repository retired.** A researcher tested first contact, scope negotiation, and Copilot-only installation in a GitHub Codespace. HILD's installer was applied on a branch and its resulting [PR #2](https://github.com/Motor-Learning-Lab/HILD/issues/4#issuecomment-6243195811) was merged by the human in the temporary host before the researcher deleted the test repository. The transcript exposed repeated unnecessary forms, missing review/recorded approval of the **actual scope issue**, and GitHub CLI/Codespaces credential mismatches. The durable observations are in [scope #4](https://github.com/Motor-Learning-Lab/HILD/issues/4#issuecomment-6243195811). The original host and its `chat.json` are no longer accessible. Mechanical tests were reported as passing in the pilot; the full onboarding, live Copilot hook/skill behavior, wiki initialization and new-session recovery remain **unverified**.
- [PR #8](https://github.com/Motor-Learning-Lab/HILD/pull/8) was reviewed and merged at [5eebb97](https://github.com/Motor-Learning-Lab/HILD/commit/5eebb97954912f405ae7666779f214b5d6b72d40), establishing one novice onboarding companion and conversational first contact. The 2026-10-18 pilot indicates more work on review gates and access repair is necessary. The [fourth decision record](decisions/0004-selectable-agent-integrations.md) and [decision 0005](decisions/0005-conversational-scope-building.md) still say `Proposed`, pending human review of their status.

- Repository GitHub settings agree with the squash-only decision: PR title and body as the squash message and automatic branch deletion.

## Next steps

1. **Review [PR #9](https://github.com/Motor-Learning-Lab/HILD/pull/9)** — requires the agent to link the **actual scope issue**, seek explicit review, record approval on the issue, and only then begin implementation. Its [decision 0006](decisions/0006-scope-issue-approval-gate.md) is proposed and awaits read-track approval.
2. **Review [PR #10](https://github.com/Motor-Learning-Lab/HILD/pull/10)** — adds an on-demand GitHub/Codespaces access companion, linked by integration and onboarding skills, based on observed authentication and Git-push failures. These PRs are independent and **must not be merged by the agent**.
3. After review and merge, rerun a genuine scoped exercise in a new, **separately authorized** host repository. Look for approval recorded in the scope issue, a documented PR review track, effective access recovery, and actual skill/hook use; distinguish behavioral observations from mechanically passing installation tests.
4. Review the status of earlier [decisions 0004](decisions/0004-selectable-agent-integrations.md) and [0005](decisions/0005-conversational-scope-building.md), using a PR for any status changes. Keep [scope #4](https://github.com/Motor-Learning-Lab/HILD/issues/4) open until its outstanding live validation is performed or its goals are amended by the researcher.

## Deliberately deferred

- Integrating with an existing wiki or relocating existing authoritative research documents.
- Upgrades and three-way reconciliation of locally modified HILD installations.
- Migrating MotorAdpatationSBI or retrospectively changing its history.
- Claiming native Claude/Codex/Copilot hook behavior without an actual supported agent test.
