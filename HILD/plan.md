# HILD plan

The living plan records current goals, state and next steps; history lives in Git and in the [journal](journal/2026-10-14.md).

## Goals

1. Establish HILD's own governance from the proven [MotorAdpatationSBI process](https://github.com/opherdonchin/MotorAdpatationSBI/blob/main/docs/process.md).
2. Provide a read-only `hild-integrate` assessment that works before installation.
3. Subsequently add explicit installation, authority mapping and safe three-way reconciliation.
4. Port the remaining process skills and mechanisms, verifying cross-agent behavior.
5. Adopt HILD in MotorAdpatationSBI as the first substantial integration test without reorganizing it beforehand.

## Current state — 2026-10-15

- [Scope #1](https://github.com/Motor-Learning-Lab/HILD/issues/1) is **complete and closed**. Both [governance PR #2](https://github.com/Motor-Learning-Lab/HILD/pull/2) and [bootstrap PR #3](https://github.com/Motor-Learning-Lab/HILD/pull/3) have merged.
- [PR #3](https://github.com/Motor-Learning-Lab/HILD/pull/3) merged by **squash** on 2026-10-15 (Israel time), commit [d85dfd0](https://github.com/Motor-Learning-Lab/HILD/commit/d85dfd04275ffc040c2897871d6b23d6fd5187e9). [PR #2](https://github.com/Motor-Learning-Lab/HILD/pull/2) had merged by **merge commit**, contrary to policy; do not rewrite published history.
- The [read-only `hild-integrate` skill](../.agents/skills/hild-integrate/SKILL.md) is now available in the repository. A manual, GitHub-only, no-write assessment of MotorAdpatationSBI was recorded in [the journal](journal/2026-10-14.md). **Native agent discovery and a live local working-tree assessment have not been tested.**
- [Decisions 0001 and 0002](decisions/) are marked `Accepted` following human review and a PR-based status update.
- GitHub settings now disable merge and rebase merges, leaving squash as the only permitted merge method. **Remaining differences from accepted policy:** `delete_branch_on_merge=false` and squash commit defaults are `COMMIT_OR_PR_TITLE` / `COMMIT_MESSAGES`, not PR title / PR description. Correct those in repository settings; do not rewrite existing commits.
- The other original process skills, session hooks, scripts and understanding map are not installed in HILD. No installer, automated upgrade/reconciliation engine, or integration into MotorAdpatationSBI exists.

- [Scope #4](https://github.com/Motor-Learning-Lab/HILD/issues/4) was approved in chat on 2026-10-15. [Draft PR #5](https://github.com/Motor-Learning-Lab/HILD/pull/5) is porting general HILD skills, onboarding guidance and canonical wiki formats; these changes are **not merged**. Next PRs in the scope handle scripts, fresh wiki, selected-agent adapters, installer verification and real onboarding validation.

## Next steps

1. Address the researcher's [PR #5](https://github.com/Motor-Learning-Lab/HILD/pull/5) feedback on onboarding clarity, initial project choices, and readable writing. The revised scope companion now avoids repeating normal PR rules; PR and journal formats omit irrelevant sections. Update the explanation and obtain the human's read-track approval. Live agent loading remains **untested**; do not merge on the agent's initiative.
2. Subsequent PRs in [approved scope #4](https://github.com/Motor-Learning-Lab/HILD/issues/4) port the working scripts, initialize a **fresh** understanding wiki and selected-agent hooks, implement approved first-time installation with mechanical verification, and demonstrate an actual onboarding cycle.
3. Update GitHub settings for PR title + PR description as squash message and automatic branch deletion. Squash-only merge method is already enabled.
4. Keep integration with **existing** wikis and three-way upgrades of locally modified HILD installations outside this scope.

## Deliberately deferred

- Cross-agent hooks and automatic session orientation; original [issues #10](https://github.com/opherdonchin/MotorAdpatationSBI/issues/10) and [#11](https://github.com/opherdonchin/MotorAdpatationSBI/issues/11) document unresolved verification.
- Wiki creation, status script, auditing and additional skills.
- Retrospective compliance of a host project's existing history.
- A full configuration schema and upgrade engine.
