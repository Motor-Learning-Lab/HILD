# HILD plan

The living plan records goals, current state and next steps. History is in Git and the [journal](journal/); the latest entry is [2026-11-22](journal/2026-11-22.md).

## Goals

1. Develop HILD using its own human-supervised development process.
2. Provide a reusable first-time installation with clear authority, agent selection and mechanical verification.
3. Validate the installed process through genuine human-agent onboarding in a fresh repository.
4. Later, preserve and reconcile existing installations and project knowledge, beginning with MotorAdpatationSBI.

## Current state — 2026-11-22

- **[Scope #12](https://github.com/Motor-Learning-Lab/HILD/issues/12) is complete.** The researcher merged the finalization [PR #30](https://github.com/Motor-Learning-Lab/HILD/pull/30) as [`9f48e17`](https://github.com/Motor-Learning-Lab/HILD/commit/9f48e17fe7b7e4209b22461d869e61518d4e4c5e), which closed scopes #4, #12 and #22 and issue #21. `main` now carries:
  - portable installation and startup repairs ([PR #11](https://github.com/Motor-Learning-Lab/HILD/pull/11));
  - the process/reference-implementation distinction ([PR #13](https://github.com/Motor-Learning-Lab/HILD/pull/13));
  - the [onboarding test protocol](onboarding-test-protocol.md) ([PR #14](https://github.com/Motor-Learning-Lab/HILD/pull/14));
  - the [scope #22](https://github.com/Motor-Learning-Lab/HILD/issues/22) corrections ([PRs #24–#26](https://github.com/Motor-Learning-Lab/HILD/pull/26)), in which Claude Code finds the skills through `@AGENTS.md` and a skills index;
  - the rule that test evidence is kept in HILD ([PR #27](https://github.com/Motor-Learning-Lab/HILD/pull/27)).
- **Decisions [0007](decisions/0007-process-vs-reference-implementation.md), [0008](decisions/0008-independent-work-and-human-acceptance.md) and [0009](decisions/0009-claude-skills-via-agents-md.md) are `Accepted`** and in effect.
- **The onboarding test ran on 2026-11-22** against candidate `768bae1`, using Claude Code on Windows.
  - Every human stopping point held: scope issues, the installer preview, review and merge. Installation, a small development task, merge settings and a fresh wiki worked.
  - The researcher accepted the candidate as working and waived the final recovery session. See the [results and evidence](https://github.com/Motor-Learning-Lab/HILD/issues/12#issuecomment-7071278845).
  - Codex and Copilot remain **untested**. So does a full explain-back, which the researcher waived.
- **Scope [#18](https://github.com/Motor-Learning-Lab/HILD/issues/18) (tighten the skills):** PR A ([#31](https://github.com/Motor-Learning-Lab/HILD/pull/31)) and PR B, the `hild-scope` rewrite ([#32](https://github.com/Motor-Learning-Lab/HILD/pull/32), merged as [`5b599eb`](https://github.com/Motor-Learning-Lab/HILD/commit/5b599eb00df03451fcb01c9f160b051666e72a8d)), are on `main`. Decisions 0005, 0010 and 0011 are `Accepted`; 0003 carries a successor notice. The merge-settings step and the index wording are **not yet tested live**. The remaining rewrites wait for #33.
- **Scope [#33](https://github.com/Motor-Learning-Lab/HILD/issues/33) (process spine), approved.** Decision 0012 was merged by mistake in [PR #34](https://github.com/Motor-Learning-Lab/HILD/pull/34); [PR #35](https://github.com/Motor-Learning-Lab/HILD/pull/35) reverts it, and [PR #36](https://github.com/Motor-Learning-Lab/HILD/pull/36) re-proposes it. The scope now includes removing duplication and tightening wording. Classification puts the spine at about 416 lines before that rewrite.
- **Scope [#20](https://github.com/Motor-Learning-Lab/HILD/issues/20) (understanding map):** the concept pages and guide are written; code and skill pages are next.
- **Not yet approved:** proposals [#15](https://github.com/Motor-Learning-Lab/HILD/issues/15) and [#17](https://github.com/Motor-Learning-Lab/HILD/issues/17), and proposed scope [#16](https://github.com/Motor-Learning-Lab/HILD/issues/16) on branch agreements. Decision [0004](decisions/0004-selectable-agent-integrations.md) still says `Proposed`.

## Next steps

1. **The researcher merges [PR #35](https://github.com/Motor-Learning-Lab/HILD/pull/35)** (revert), **then reviews [PR #36](https://github.com/Motor-Learning-Lab/HILD/pull/36)** (decision 0012, read track). Then under #33: the verbatim move with the installer change, then the rewrite; then the scope #18 rewrites against the split: `hild-integrate`, `hild-explain`, then the four short skills.
2. **Scope [#20](https://github.com/Motor-Learning-Lab/HILD/issues/20)'s code pages** now, in parallel; skill pages after each skill's rewrite merges.
3. **Later:** review the stale `Proposed` status of decision 0004, and settle CI for integration branches under scope #16.

## Deliberately deferred

- Integrating with an existing wiki or relocating existing authoritative research documents.
- Upgrades and three-way reconciliation of locally modified HILD installations.
- Migrating MotorAdpatationSBI or retrospectively changing its history.
- Claiming native Claude/Codex/Copilot hook behavior without an actual supported agent test.
