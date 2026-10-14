# HILD plan

The living plan records current goals, state and next steps; history lives in Git and in the [journal](journal/2026-10-14.md).

## Goals

1. Establish HILD's own governance from the proven [MotorAdpatationSBI process](https://github.com/opherdonchin/MotorAdpatationSBI/blob/main/docs/process.md).
2. Provide a read-only `hild-integrate` assessment that works before installation.
3. Subsequently add explicit installation, authority mapping and safe three-way reconciliation.
4. Port the remaining process skills and mechanisms, verifying cross-agent behavior.
5. Adopt HILD in MotorAdpatationSBI as the first substantial integration test without reorganizing it beforehand.

## Current state — 2026-10-14

- [Scope #1](https://github.com/Motor-Learning-Lab/HILD/issues/1) approved in chat; scope approval recorded on GitHub.
- [PR #2](https://github.com/Motor-Learning-Lab/HILD/pull/2): governance foundation. The reviewer commented on unclear tooling status and the roles of `AGENTS.md` and the README. Those passages were clarified on the branch; the PR awaits human review of these revisions and is **not merged**.
- Initial public repository exists; `main` has an MIT license and a short README.
- The full original rules are carried into [the process](process.md), with implementation status explicitly distinguished: **no local HILD skills, automation, scripts or wiki are operational yet**.
- HILD currently permits merge commits and rebase merges in GitHub settings; agreed policy is squash only and requires manual settings adjustment.
- Skill discovery paths, config file format and understanding-map alternatives remain open. No integration has been performed on MotorAdpatationSBI.

## Next steps

1. Update PR #2 explanation for review feedback and obtain the human's explicit read-track approval. An initial static audit of internal Markdown links and source provenance is complete.
2. Human reviewer reads PR #2 and records approval or requested changes. Do not merge on the agent's initiative.
3. Within approved [scope #1](https://github.com/Motor-Learning-Lab/HILD/issues/1), prepare PR B with the `hild-integrate` **read-only assessment** procedure; verify agent loading/location and rehearse on MotorAdpatationSBI, with no writes.
4. Design and scope installation, version tracking and reconciliation separately after seeing the assessment results.

## Deliberately deferred

- Cross-agent hooks and automatic session orientation; original [issues #10](https://github.com/opherdonchin/MotorAdpatationSBI/issues/10) and [#11](https://github.com/opherdonchin/MotorAdpatationSBI/issues/11) document unresolved verification.
- Wiki creation, status script, auditing and additional skills.
- Retrospective compliance of a host project's existing history.
- A full configuration schema and upgrade engine.
