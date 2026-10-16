# HILD plan

The living plan records current goals, state and next steps; history lives in Git and in the [journal](journal/2026-10-14.md).

## Goals

1. Establish HILD's own governance from the proven [MotorAdpatationSBI process](https://github.com/opherdonchin/MotorAdpatationSBI/blob/main/docs/process.md).
2. Provide a read-only `hild-integrate` assessment that works before installation.
3. Subsequently add explicit installation, authority mapping and safe three-way reconciliation.
4. Port the remaining process skills and mechanisms, verifying cross-agent behavior.
5. Adopt HILD in MotorAdpatationSBI as the first substantial integration test without reorganizing it beforehand.

## Current state — 2026-10-16

- [Scope #1](https://github.com/Motor-Learning-Lab/HILD/issues/1) is complete. The original governance and read-only integration assessment are on `main`.
- [Scope #4](https://github.com/Motor-Learning-Lab/HILD/issues/4) is approved and ongoing. [PR #5](https://github.com/Motor-Learning-Lab/HILD/pull/5) merged reusable skills, onboarding guidance and templates as [d40f9e8](https://github.com/Motor-Learning-Lab/HILD/commit/d40f9e810750597b1441b42d2374eee00480a75a).
- [PR #6](https://github.com/Motor-Learning-Lab/HILD/pull/6) merged the wiki checker, orientation script, tests, optional agent-hook templates and fresh-wiki instructions as [ac63a3a](https://github.com/Motor-Learning-Lab/HILD/commit/ac63a3a34bf366d5c195d4676c7374053371b014). Mechanical GitHub Actions tests passed. **No active wiki or live agent discovery test has occurred.**
- [Draft PR #7](https://github.com/Motor-Learning-Lab/HILD/pull/7) adds preview-first fresh-repository installation, selectable agent adapters, provenance and safety tests. Automated tests now pass against the complete HILD source, including structural installation verification. Live agent discovery and wiki publication remain unverified.
- Squash-only merge settings, PR-title/description commit text and automatic branch deletion are **verified**. No HILD installation into MotorAdpatationSBI has occurred.

## Next steps

1. **Review PR #7:** a non-rewriting merge commit brought PR #6's toolkit onto the installer branch. [GitHub Actions run 38962742449](https://github.com/Motor-Learning-Lab/HILD/actions/runs/38962742449) passed **16 installer tests**, including the real full-package smoke test; [mechanical checks](https://github.com/Motor-Learning-Lab/HILD/actions/runs/38962742525) also passed. Its installer is ready for human review, not yet merged.
2. With a separately agreed disposable target repository and new-wiki creation, complete the onboarding validation phase (PR D), including scope/PR, human approval, draft `Process-HILD` wiki page after merge, and fresh-session agent behavior checks.
3. **Deferred:** upgrading locally customized HILD, integration with existing wikis, and retroactive migration of MotorAdpatationSBI.

## Deliberately deferred

- Cross-agent hooks and automatic session orientation; original [issues #10](https://github.com/opherdonchin/MotorAdpatationSBI/issues/10) and [#11](https://github.com/opherdonchin/MotorAdpatationSBI/issues/11) document unresolved verification.
- Wiki creation, status script, auditing and additional skills.
- Retrospective compliance of a host project's existing history.
- A full configuration schema and upgrade engine.
