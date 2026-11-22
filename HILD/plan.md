# HILD plan

The living plan records goals, current state and next steps. History is in Git and the [journal](journal/); the latest entry is [2026-11-22](journal/2026-11-22.md).

## Goals

1. Develop HILD using its own human-supervised development process.
2. Provide a reusable first-time installation with clear authority, agent selection and mechanical verification.
3. Validate the installed process through genuine human-agent onboarding in a fresh repository.
4. Later, preserve and reconcile existing installations and project knowledge, beginning with MotorAdpatationSBI.

## Current state — 2026-11-22

- **[Scope #12](https://github.com/Motor-Learning-Lab/HILD/issues/12) is being finalized.** The integration branch `integration/scope-12` comes to `main` in the finalization PR. It carries:
  - portable installation and startup repairs ([PR #11](https://github.com/Motor-Learning-Lab/HILD/pull/11));
  - the process/reference-implementation distinction ([PR #13](https://github.com/Motor-Learning-Lab/HILD/pull/13));
  - the [onboarding test protocol](onboarding-test-protocol.md) ([PR #14](https://github.com/Motor-Learning-Lab/HILD/pull/14));
  - the [scope #22](https://github.com/Motor-Learning-Lab/HILD/issues/22) corrections ([PRs #24–#26](https://github.com/Motor-Learning-Lab/HILD/pull/26)), in which Claude Code finds the skills through `@AGENTS.md` and a skills index;
  - the rule that test evidence is kept in HILD ([PR #27](https://github.com/Motor-Learning-Lab/HILD/pull/27)).
- **Decisions [0007](decisions/0007-process-vs-reference-implementation.md), [0008](decisions/0008-independent-work-and-human-acceptance.md) and [0009](decisions/0009-claude-skills-via-agents-md.md) are `Accepted`** and take effect on `main` with that PR.
- **The onboarding test ran on 2026-11-22** against candidate `768bae1`, using Claude Code on Windows.
  - Every human stopping point held: scope issues, the installer preview, review and merge. Installation, a small development task, merge settings and a fresh wiki worked.
  - The researcher accepted the candidate as working and waived the final recovery session. See the [results and evidence](https://github.com/Motor-Learning-Lab/HILD/issues/12#issuecomment-7071278845).
  - Codex and Copilot remain **untested**. So does a full explain-back, which the researcher waived.
- **Follow-ups from the test:** [#28](https://github.com/Motor-Learning-Lab/HILD/issues/28) (installation does not raise GitHub's merge settings) and [#29](https://github.com/Motor-Learning-Lab/HILD/issues/29) (the generated `AGENTS.md` does not say the index is Claude Code's intended route).
- **Scope [#18](https://github.com/Motor-Learning-Lab/HILD/issues/18) (tighten the skills):** step 1 is reviewed and its three choices are decided; PR A and the rewrites wait for `main`. **Scope [#20](https://github.com/Motor-Learning-Lab/HILD/issues/20) (understanding map):** the concept pages and guide are written; code and skill pages wait for `main` and #18.
- **Not yet approved:** proposals [#15](https://github.com/Motor-Learning-Lab/HILD/issues/15) and [#17](https://github.com/Motor-Learning-Lab/HILD/issues/17), and proposed scope [#16](https://github.com/Motor-Learning-Lab/HILD/issues/16) on branch agreements. Decisions [0004](decisions/0004-selectable-agent-integrations.md) and [0005](decisions/0005-conversational-scope-building.md) still say `Proposed`.

## Next steps

1. **The researcher reviews and merges the finalization PR.** Afterwards: close scopes #4, #12 and #22 and issue #21; delete `integration/scope-12`; and, when the researcher agrees, delete the test repository `opherdonchin/HILD-onboarding-2026-11`, whose evidence is on [scope #12](https://github.com/Motor-Learning-Lab/HILD/issues/12#issuecomment-7071270525).
2. **On `main`:** scope #18 PR A and the skill rewrites, folding in #28 and #29 where they fit; then scope #20's code and skill pages.
3. **Later:** review the stale `Proposed` status of decisions 0004 and 0005, and settle CI for integration branches under scope #16.

## Deliberately deferred

- Integrating with an existing wiki or relocating existing authoritative research documents.
- Upgrades and three-way reconciliation of locally modified HILD installations.
- Migrating MotorAdpatationSBI or retrospectively changing its history.
- Claiming native Claude/Codex/Copilot hook behavior without an actual supported agent test.
