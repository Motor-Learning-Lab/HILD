# HILD plan

The living plan records current goals, state and next steps; history lives in Git and in the [journal](journal/2026-10-14.md).

## Goals

1. Establish HILD's own governance from the proven [MotorAdpatationSBI process](https://github.com/opherdonchin/MotorAdpatationSBI/blob/main/docs/process.md).
2. Provide a read-only `hild-integrate` assessment that works before installation.
3. Subsequently add explicit installation, authority mapping and safe three-way reconciliation.
4. Port the remaining process skills and mechanisms, verifying cross-agent behavior.
5. Adopt HILD in MotorAdpatationSBI as the first substantial integration test without reorganizing it beforehand.

## Current state — 2026-10-14

- [Scope #1](https://github.com/Motor-Learning-Lab/HILD/issues/1) was approved by the human reviewer.
- [PR #2](https://github.com/Motor-Learning-Lab/HILD/pull/2), the governance foundation, was reviewed and merged on 2026-10-14; its process, root instructions, templates and initial decisions are on `main`. **GitHub used a merge commit rather than the agreed squash strategy.** Preserve history, correct repository settings before future merges.
- The original [process](process.md) is now documented here; a working HILD integration skill, hooks, scripts and understanding map are not yet installed.
- Two [decision records](decisions/) still say `Proposed` despite their substance being accepted in PR #2; their status should be updated **through a PR**, not directly on `main`.
- HILD's GitHub settings still permit merge commits and rebase merges; human administrator needs to enable squash-only, PR title/body squash messages and branch deletion.
- [PR #3](https://github.com/Motor-Learning-Lab/HILD/pull/3) implements a **reviewable first-pass read-only `hild-integrate` procedure** under `.agents/skills/hild-integrate/` (documented for Codex and Copilot; live discovery not tested). A manual GitHub-only assessment of MotorAdpatationSBI found its existing process and authoritative paths without modifying the host. No installer or three-way reconciliation exists.

## Next steps

1. [PR #3](https://github.com/Motor-Learning-Lab/HILD/pull/3) is ready for the human's **read-track review**. Its description includes the completed read-only rehearsal and testing limits.
2. Complete the decision records' `Accepted` status updates through PR #3, following the rule against directly committing decisions to `main`.
3. Human reviewer reviews and explicitly approves PR B. **Do not merge until repository settings have been corrected to squash-only.**
4. Scope a separate installation/reconciliation implementation after evaluating the assessment.

## Deliberately deferred

- Cross-agent hooks and automatic session orientation; original [issues #10](https://github.com/opherdonchin/MotorAdpatationSBI/issues/10) and [#11](https://github.com/opherdonchin/MotorAdpatationSBI/issues/11) document unresolved verification.
- Wiki creation, status script, auditing and additional skills.
- Retrospective compliance of a host project's existing history.
- A full configuration schema and upgrade engine.
