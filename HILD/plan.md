# HILD plan

The living plan records goals, current state and next steps. History is in Git and the [journal](journal/); the latest entry is [2026-11-23](journal/2026-11-23.md).

## Goals

1. Develop HILD using its own human-supervised development process.
2. Provide a reusable first-time installation with clear authority, agent selection and mechanical verification.
3. Validate the installed process through genuine human-agent onboarding in a fresh repository.
4. Later, preserve and reconcile existing installations and project knowledge, beginning with MotorAdpatationSBI.

## Current state — 2026-11-23

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
- **Scope [#33](https://github.com/Motor-Learning-Lab/HILD/issues/33) (process spine) is complete.** The researcher merged [PR #40](https://github.com/Motor-Learning-Lab/HILD/pull/40) as [`f44681b`](https://github.com/Motor-Learning-Lab/HILD/commit/f44681b). `HILD/process.md` is now an eight-section spine that every session reads, with eight topic files in `HILD/process/`, under decisions 0012 and 0013 (both `Accepted`). New installations import the spine in Claude Code. Wiki concept pages that describe the old text are marked `needs-review` (`Concept-hild-in-brief`, formerly `understood`) or `needs-revision` (three drafts).
- **Scope [#20](https://github.com/Motor-Learning-Lab/HILD/issues/20) (understanding map):** the concept pages and guide are written; code and skill pages are next.
- **Not yet approved:** proposals [#15](https://github.com/Motor-Learning-Lab/HILD/issues/15) and [#17](https://github.com/Motor-Learning-Lab/HILD/issues/17), and proposed scope [#16](https://github.com/Motor-Learning-Lab/HILD/issues/16) on branch agreements. Decision [0004](decisions/0004-selectable-agent-integrations.md) still says `Proposed`.

## Next steps

1. **Scope [#18](https://github.com/Motor-Learning-Lab/HILD/issues/18) rewrites against the split:** `hild-integrate`, `hild-explain`, then the four short skills. They also remove rules that skills and templates restate, tighten the moved topic text, and resolve `hild-journal`'s contradiction about where milestone commits go.
2. **Scope [#20](https://github.com/Motor-Learning-Lab/HILD/issues/20):** revise the concept pages that cite the old `process.md` (`Concept-hild-in-brief`, `-review-and-acceptance`, `-scope-agreements`, `-session-orientation`, `-durable-state`, `-understanding-map`) against the spine and topic files; code pages; skill pages after each skill's rewrite merges.
3. **Issue [#38](https://github.com/Motor-Learning-Lab/HILD/issues/38)** (install guidance inactive until restart; `hild-explain` trigger misses draft PRs): not yet scoped.
4. **Later:** review the stale `Proposed` status of decision 0004, and settle CI for integration branches under scope #16.

## Deliberately deferred

- Integrating with an existing wiki or relocating existing authoritative research documents.
- Upgrades and three-way reconciliation of locally modified HILD installations.
- Migrating MotorAdpatationSBI or retrospectively changing its history.
- Claiming native Claude/Codex/Copilot hook behavior without an actual supported agent test.
