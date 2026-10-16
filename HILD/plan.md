# HILD plan

The living plan records current goals, state and next steps; history lives in Git and in the [journal](journal/2026-10-14.md).

## Goals

1. Establish HILD's own governance from the proven [MotorAdpatationSBI process](https://github.com/opherdonchin/MotorAdpatationSBI/blob/main/docs/process.md).
2. Provide a read-only `hild-integrate` assessment that works before installation.
3. Subsequently add explicit installation, authority mapping and safe three-way reconciliation.
4. Port the remaining process skills and mechanisms, verifying cross-agent behavior.
5. Adopt HILD in MotorAdpatationSBI as the first substantial integration test without reorganizing it beforehand.

## Current state — 2026-10-16

- [Scope #1](https://github.com/Motor-Learning-Lab/HILD/issues/1) is **complete and closed**. Both [governance PR #2](https://github.com/Motor-Learning-Lab/HILD/pull/2) and [bootstrap PR #3](https://github.com/Motor-Learning-Lab/HILD/pull/3) have merged.
- [PR #3](https://github.com/Motor-Learning-Lab/HILD/pull/3) merged by **squash** on 2026-10-15 (Israel time), commit [d85dfd0](https://github.com/Motor-Learning-Lab/HILD/commit/d85dfd04275ffc040c2897871d6b23d6fd5187e9). [PR #2](https://github.com/Motor-Learning-Lab/HILD/pull/2) had merged by **merge commit**, contrary to policy; do not rewrite published history.
- The [read-only `hild-integrate` skill](../.agents/skills/hild-integrate/SKILL.md) is now available in the repository. A manual, GitHub-only, no-write assessment of MotorAdpatationSBI was recorded in [the journal](journal/2026-10-14.md). **Native agent discovery and a live local working-tree assessment have not been tested.**
- [Decisions 0001 and 0002](decisions/) are marked `Accepted` following human review and a PR-based status update.
- GitHub settings now disable merge and rebase merges, leaving squash as the only permitted merge method. **Remaining differences from accepted policy:** `delete_branch_on_merge=false` and squash commit defaults are `COMMIT_OR_PR_TITLE` / `COMMIT_MESSAGES`, not PR title / PR description. Correct those in repository settings; do not rewrite existing commits.
- Reusable agent procedure files now exist in HILD. **Session hooks, supporting scripts, active understanding wiki and installation/upgrade machinery do not yet exist**; no installation into MotorAdpatationSBI has occurred.

- [Scope #4](https://github.com/Motor-Learning-Lab/HILD/issues/4) was approved on 2026-10-15. [PR #5](https://github.com/Motor-Learning-Lab/HILD/pull/5) has now been **reviewed and squash-merged** on 2026-10-16 ([commit d40f9e8](https://github.com/Motor-Learning-Lab/HILD/commit/d40f9e810750597b1441b42d2374eee00480a75a)). Six reusable HILD skills, the optional onboarding scope companion, wiki templates and getting-started instructions are on `main`. No active wiki, hook, installer or live agent-loading verification exists yet.

## Next steps

1. Begin PR B under [approved scope #4](https://github.com/Motor-Learning-Lab/HILD/issues/4): port and test orientation and wiki-staleness scripts, define **new-wiki-only** setup, and prepare selected-agent startup integration. Keep the implementation split into reviewable parts if needed. Live agent discovery remains **untested**.
2. Subsequent PRs in [approved scope #4](https://github.com/Motor-Learning-Lab/HILD/issues/4) port the working scripts, initialize a **fresh** understanding wiki and selected-agent hooks, implement approved first-time installation with mechanical verification, and demonstrate an actual onboarding cycle.
3. Update GitHub settings for PR title + PR description as squash message and automatic branch deletion. Squash-only merge method is already enabled.
4. Keep integration with **existing** wikis and three-way upgrades of locally modified HILD installations outside this scope.

## Deliberately deferred

- Cross-agent hooks and automatic session orientation; original [issues #10](https://github.com/opherdonchin/MotorAdpatationSBI/issues/10) and [#11](https://github.com/opherdonchin/MotorAdpatationSBI/issues/11) document unresolved verification.
- Wiki creation, status script, auditing and additional skills.
- Retrospective compliance of a host project's existing history.
- A full configuration schema and upgrade engine.
