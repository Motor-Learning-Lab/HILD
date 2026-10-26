# HILD plan

The living plan records goals, current state and next steps. History is recorded in Git and the [latest journal](journal/2026-10-26.md).

## Goals

1. Develop HILD using its own human-supervised development process.
2. Provide a reusable first-time installation with clear authority, agent selection and mechanical verification.
3. Validate the installed process through genuine human-agent onboarding in a fresh repository.
4. Later, preserve and reconcile existing installations and project knowledge, beginning with MotorAdpatationSBI.

## Current state — 2026-10-26

- [Scope #1](https://github.com/Motor-Learning-Lab/HILD/issues/1) is complete. [Scope #4](https://github.com/Motor-Learning-Lab/HILD/issues/4) is approved and remains **open** for onboarding validation.
- [PR #5](https://github.com/Motor-Learning-Lab/HILD/pull/5) merged the reusable HILD skills, onboarding guidance and wiki templates.
- [PR #6](https://github.com/Motor-Learning-Lab/HILD/pull/6) merged orientation and wiki-staleness scripts, regression tests, new-wiki instructions and optional agent hook templates.
- [PR #7](https://github.com/Motor-Learning-Lab/HILD/pull/7) was **human-reviewed and squash-merged** at [3c3a32d](https://github.com/Motor-Learning-Lab/HILD/commit/3c3a32d4a8a6f2973f21b696c016bd33da9b546d) on 2026-10-17 Israel time. It supplies a preview-first installer for minimally initialized repositories, selected agents (default all), and installation verification.
- Both post-merge GitHub Actions workflows **passed**: [installation checks](https://github.com/Motor-Learning-Lab/HILD/actions/runs/38971254235) and [mechanical checks](https://github.com/Motor-Learning-Lab/HILD/actions/runs/38971254359). Earlier complete-source installation tests passed in temporary local Git repositories.
- **Live Copilot pilot completed and repository retired.** A researcher tested first contact, scope negotiation, and Copilot-only installation in a GitHub Codespace. HILD's installer was applied on a branch and its [installation PR (recorded in the pilot evidence)](https://github.com/Motor-Learning-Lab/HILD/issues/4#issuecomment-6243195811) was merged by the human in the temporary host before the researcher deleted the test repository. The transcript exposed repeated unnecessary forms, missing review/recorded approval of the **actual scope issue**, and GitHub CLI/Codespaces credential mismatches. The durable observations are in [scope #4](https://github.com/Motor-Learning-Lab/HILD/issues/4#issuecomment-6243195811). The original host and its `chat.json` are no longer accessible. Mechanical tests were reported as passing in the pilot; the full onboarding, live Copilot hook/skill behavior, wiki initialization and new-session recovery remain **unverified**.
- [PR #8](https://github.com/Motor-Learning-Lab/HILD/pull/8) was reviewed and merged at [5eebb97](https://github.com/Motor-Learning-Lab/HILD/commit/5eebb97954912f405ae7666779f214b5d6b72d40), establishing one novice onboarding companion and conversational first contact. The 2026-10-18 pilot indicates more work on review gates and access repair is necessary. The [fourth decision record](decisions/0004-selectable-agent-integrations.md) and [decision 0005](decisions/0005-conversational-scope-building.md) still say `Proposed`, pending human review of their status.

- **Pilot-derived improvements merged:** [PR #9](https://github.com/Motor-Learning-Lab/HILD/pull/9) at [2fb36a4](https://github.com/Motor-Learning-Lab/HILD/commit/2fb36a406aa817fe52f03e751699c2e78ce8c6d9) clarifies that the researcher must see and approve the actual scope issue before work starts. [PR #10](https://github.com/Motor-Learning-Lab/HILD/pull/10) at [a2b9705](https://github.com/Motor-Learning-Lab/HILD/commit/a2b9705f679fbfcd11891b0728ea0014f30fa880) supplies an environment-neutral, on-demand GitHub-access companion and nonblocking onboarding guidance about access. Post-merge [installation checks](https://github.com/Motor-Learning-Lab/HILD/actions/runs/39110721076) and [mechanical checks](https://github.com/Motor-Learning-Lab/HILD/actions/runs/39110721098) passed. **These are instructional and mechanical results, not demonstrated agent behavior.**
- Repository GitHub settings agree with the squash-only decision: PR title and body as the squash message and automatic branch deletion.
- **Scope #12 / PRs #11, #13 and #14 (2026-10-26):** The three stacked PRs remain **draft/open/unmerged**. [PR #11](https://github.com/Motor-Learning-Lab/HILD/pull/11) corrects concrete installation/startup findings. The researcher explicitly [approved PR #13 and decisions 0007/0008 and partial supersession of 0006](https://github.com/Motor-Learning-Lab/HILD/pull/13#issuecomment-6422857797) on 2026-10-26, with merger and activation of accepted decision status still gated by live onboarding. [PR #13](https://github.com/Motor-Learning-Lab/HILD/pull/13) is unchanged at `92de97e`; its revised process distinguishes requirements and GitHub/skills mechanisms passage by passage. [PR #14](https://github.com/Motor-Learning-Lab/HILD/pull/14) now incorporates PR #13 through the [forward merge `172290a`](https://github.com/Motor-Learning-Lab/HILD/commit/172290abb33e90f3c8607a1a70ab1e58824a9768), preserving both histories. The [installation](https://github.com/Motor-Learning-Lab/HILD/actions/runs/40370174344) and [mechanical](https://github.com/Motor-Learning-Lab/HILD/actions/runs/40370174342) CI suites **passed on that merge commit**. Check the [PR #14 description](https://github.com/Motor-Learning-Lab/HILD/pull/14) and workflow runs for the latest head before a live test; an earlier run never validates a later commit. The [protocol](onboarding-test-protocol.md) has been unblocked as a *candidate preparation*; **no new live onboarding exercise, remote host, or wiki has been created**.

## Next steps

1. Confirm the **latest** [PR #14](https://github.com/Motor-Learning-Lab/HILD/pull/14) head includes [PR #13](https://github.com/Motor-Learning-Lab/HILD/pull/13) and verify both CI suites on that exact head. Record the candidate SHA and any untested behavior; green CI is only structural/mechanical evidence.
2. Review [PR #14's protocol](onboarding-test-protocol.md) and separately obtain the researcher's authorization for a **new disposable test repository**, agent/platform and any wiki setup. Do not provision or alter these before approval.
3. Run an ordinary **human-supervised end-to-end onboarding** from the pinned candidate: approved scope issue, separate installer-apply consent, early draft PR, plan/journal milestones, agent discovery and orientation, meaningful review and human-only merge, fresh understanding wiki, and new-session recovery. Record PASSED / FAILED / BLOCKED / NOT TESTED with actual evidence.
4. If a test fails, correct the owning unmerged HILD PR, carry the change forward without rewriting history, rerun CI and retry in a genuinely fresh host.
5. Only after the acceptance exercise succeeds and the researcher separately authorizes each merge, squash-merge #11, #13 and #14 in order. Mark decisions 0007 and 0008 accepted and decision 0006 partially superseded when effective on `main`; then check published onboarding before closing [scopes #4](https://github.com/Motor-Learning-Lab/HILD/issues/4) and [#12](https://github.com/Motor-Learning-Lab/HILD/issues/12).
6. Later review stale proposed metadata for [decision 0004](decisions/0004-selectable-agent-integrations.md) and [decision 0005](decisions/0005-conversational-scope-building.md) in a focused state-correction PR.

## Deliberately deferred

- Integrating with an existing wiki or relocating existing authoritative research documents.
- Upgrades and three-way reconciliation of locally modified HILD installations.
- Migrating MotorAdpatationSBI or retrospectively changing its history.
- Claiming native Claude/Codex/Copilot hook behavior without an actual supported agent test.
