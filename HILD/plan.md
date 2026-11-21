# HILD plan

The living plan records goals, current state and next steps. History is recorded in Git and the [latest journal](journal/2026-11-09.md); later journals are on [`main`](https://github.com/Motor-Learning-Lab/HILD/tree/main/HILD/journal).

## Goals

1. Develop HILD using its own human-supervised development process.
2. Provide a reusable first-time installation with clear authority, agent selection and mechanical verification.
3. Validate the installed process through genuine human-agent onboarding in a fresh repository.
4. Later, preserve and reconcile existing installations and project knowledge, beginning with MotorAdpatationSBI.

## Current state — 2026-11-21 (evening)

- **On `main`:** [scope #1](https://github.com/Motor-Learning-Lab/HILD/issues/1) is complete. PRs [#5](https://github.com/Motor-Learning-Lab/HILD/pull/5)–[#10](https://github.com/Motor-Learning-Lab/HILD/pull/10) supply the skills, orientation and wiki-status scripts, the preview-first installer with agent selection and `--verify`, the onboarding companion, the scope-issue approval gate and the GitHub-access companion. GitHub settings enforce squash-only merges with the PR title and body as the message.
- **Pilots:** a Copilot pilot in a Codespace and Claude Code trials on Windows (2026-10-18 and 2026-10-28) exposed defects in forms, approval gates, credentials, Windows symlinks and wiki tooling. They are recorded in [scope #4](https://github.com/Motor-Learning-Lab/HILD/issues/4#issuecomment-6253200260) and the [2026-10-28 journal](journal/2026-10-28.md). A full onboarding, live Copilot and Codex behavior, and fresh-session recovery remain **unverified**.
- **[Scope #12](https://github.com/Motor-Learning-Lab/HILD/issues/12) uses the integration branch `integration/scope-12`** ([amendment](https://github.com/Motor-Learning-Lab/HILD/issues/12#issuecomment-6739027054)). It now holds all three component PRs, squash-merged by the researcher on 2026-11-09:
  - [PR #11](https://github.com/Motor-Learning-Lab/HILD/pull/11), carrying [PR #13](https://github.com/Motor-Learning-Lab/HILD/pull/13), as [`5e9d051`](https://github.com/Motor-Learning-Lab/HILD/commit/5e9d051b343839e9ee8abde75649a553969eb4a9): portable installation and startup repairs, and the distinction between HILD's process and its GitHub-and-skills reference implementation.
  - [PR #14](https://github.com/Motor-Learning-Lab/HILD/pull/14) as [`0688ae8`](https://github.com/Motor-Learning-Lab/HILD/commit/0688ae84a0efb3060bfcd2d6ca31d6718f0e0b36): the [onboarding test protocol](onboarding-test-protocol.md).
  - `0688ae8` has the same tree as PR #14's last head `6b7a596`, on which [installation](https://github.com/Motor-Learning-Lab/HILD/actions/runs/42618550494) and [wiki-checker](https://github.com/Motor-Learning-Lab/HILD/actions/runs/42618550351) CI passed. The workflows run on pull requests and on pushes to `main` only, so **pushes to the integration branch are not checked by CI**.
  - The researcher [approved decisions 0007 and 0008](https://github.com/Motor-Learning-Lab/HILD/pull/13#issuecomment-6422857797); their accepted status takes effect when the branch reaches `main`.
  - **The single supervised onboarding test has not run.** It needs a disposable test repository that the researcher approves separately.
- **Pre-test corrections done ([scope #22](https://github.com/Motor-Learning-Lab/HILD/issues/22)).** The researcher merged three PRs into this branch on 2026-11-21:
  - [PR #24](https://github.com/Motor-Learning-Lab/HILD/pull/24), as `7b993d3`: `wiki_status.py` ignores code spans and writes LF, and the templates are tested against it;
  - [PR #25](https://github.com/Motor-Learning-Lab/HILD/pull/25), as `81d43ad`: process clarifications on automatic orientation, stale pages, changed pages needing review, and where plan updates go;
  - [PR #26](https://github.com/Motor-Learning-Lab/HILD/pull/26), as `1ba9e05`: Claude Code finds the skills through `@AGENTS.md` and a skills index, with no `.claude/skills` link (decision 0009), and the startup hook no longer replaces the first request.
  - CI passed on each PR. Decision 0009 is accepted with the PR; its file status changes when the branch reaches `main`.
- **Scope [#18](https://github.com/Motor-Learning-Lab/HILD/issues/18) (tighten the skills):** step 1 is reviewed, and the researcher decided all three choices. PR A and the rewrites wait for `main`. **Scope [#20](https://github.com/Motor-Learning-Lab/HILD/issues/20) (understanding map):** the step 2 concept pages and guide are written. Code and skill pages wait for `main` and for #18.
- **[HILD wiki](https://github.com/Motor-Learning-Lab/HILD/wiki):** three `draft` concept pages on installation, symlinks and platform independence, and a generated Status board.
- **Not yet approved:** proposals [#15](https://github.com/Motor-Learning-Lab/HILD/issues/15) and [#17](https://github.com/Motor-Learning-Lab/HILD/issues/17), and proposed scope [#16](https://github.com/Motor-Learning-Lab/HILD/issues/16) on branch agreements. Decisions [0004](decisions/0004-selectable-agent-integrations.md) and [0005](decisions/0005-conversational-scope-building.md) still say `Proposed`.

## Next steps

1. **The researcher approves a disposable test repository.** The agent then runs the supervised onboarding test on this branch's head, following [the protocol](onboarding-test-protocol.md). Defects are fixed by small PRs into this branch, and the test is repeated.
2. **After the test passes: a finalization PR from `integration/scope-12` to `main`.** The researcher merges it. Decisions 0007, 0008 and 0009 then take effect, and scopes [#4](https://github.com/Motor-Learning-Lab/HILD/issues/4), [#12](https://github.com/Motor-Learning-Lab/HILD/issues/12) and [#22](https://github.com/Motor-Learning-Lab/HILD/issues/22) and issue [#21](https://github.com/Motor-Learning-Lab/HILD/issues/21) can close.
3. **Then, on `main`:** scope #18 PR A and the skill rewrites, followed by scope #20's code and skill pages.
4. Later: review the stale `Proposed` status of decisions 0004 and 0005; settle CI for integration branches under [scope #16](https://github.com/Motor-Learning-Lab/HILD/issues/16).

## Deliberately deferred

- Integrating with an existing wiki or relocating existing authoritative research documents.
- Upgrades and three-way reconciliation of locally modified HILD installations.
- Migrating MotorAdpatationSBI or retrospectively changing its history.
- Claiming native Claude/Codex/Copilot hook behavior without an actual supported agent test.
