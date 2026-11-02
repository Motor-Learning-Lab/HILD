# Live onboarding test for the combined HILD candidate

> **Test plan, not a test result.** This document describes the supervised onboarding experiment proposed under [scope #12](https://github.com/Motor-Learning-Lab/HILD/issues/12). The corrected candidate has **not** passed this experiment. The earlier [Windows/Claude pilot](https://github.com/opherdonchin/HILD-onboarding-ipad-2026-10/pull/2) was informative but exposed a broken checkout; see [PR #11](https://github.com/Motor-Learning-Lab/HILD/pull/11). This protocol records a particular validation exercise, not permanent instructions for installing future HILD releases.

## What we want to find out

Can a researcher who is new to HILD use a coding agent to adopt it in a fresh repository and complete one small, supervised development task **without losing control or getting stuck with a broken installation**?

We need to observe both sides:

- **Human supervision:** Does the agent explain decisions, show the actual scope issue, request separate permission before installing, open a reviewable PR, respect the human merge decision, and preserve enough history to resume later?
- **Working installation:** Are the skills and configuration installed from the intended HILD revision, discoverable by the selected agent, durable after a new checkout, and verifiable? Does the new wiki and its status board work when authorized?

This is deliberately more than a test of scripts. Automated checks can show that files and links are created correctly; they cannot establish that a real agent asks for permission at the right time or that a researcher can understand the workflow. That distinction was established in [decision 0003](https://github.com/Motor-Learning-Lab/HILD/blob/main/HILD/decisions/0003-onboarding-scope-and-validation.md). The original first-install goal and wiki exercise are in [scope #4](https://github.com/Motor-Learning-Lab/HILD/issues/4).

## Three decisions that must stay separate

1. **Accept this procedure.** Reviewing [PR #14](https://github.com/Motor-Learning-Lab/HILD/pull/14) means reviewing the plan for the test. It does not mean the test happened.
2. **Authorize a particular live test.** Before creating a new GitHub repository or wiki, changing Git settings, or writing to the target, the researcher must separately agree to the actual environment and the relevant actions. Record that agreement on [scope #12](https://github.com/Motor-Learning-Lab/HILD/issues/12) or an agreed validation issue.
3. **Judge the results and subsequent merges.** After observing the exercise, the researcher decides whether the evidence is sufficient. A successful test alone does not merge HILD PRs #11, #13 or #14; only the researcher can separately approve and perform those merges.

## The proposed exercise

| Stage | What happens | What we need to see |
|---|---|---|
| 1. Prepare | Confirm the combined HILD commit, the selected agent/OS, a new repository, and the permissions for the experiment. | A recorded source commit, environment and explicit approval for any new remote resources. |
| 2. First contact | Start a new agent conversation as a newcomer to HILD. Ask the agent to guide adoption. | A useful explanation, a proposed *actual* scope issue, and a stop for the researcher's approval of that issue. |
| 3. Install | Inspect the installation preview, separately authorize installation, install and verify. On Windows, check that Claude skills remain linked after a fresh Git checkout. | Consent at the right point; the manifest points to the candidate commit; structural verification and checkout durability, or an accurately reported failure. |
| 4. Small development | Agree on a bounded task, have the agent work on a branch and PR, then review it. If satisfactory, the **researcher** merges the test-host PR. | An understandable PR, actual human review, milestone updates in the plan/journal, and no agent-initiated merge. |
| 5. Understanding and recovery | If authorized, use a fresh wiki and its status board. Start another agent session without relying on the first conversation. | Working wiki navigation; only the researcher marks pages `understood`; the new session finds the task's outcome, decisions and next step. |

These stages are the **required end-to-end evidence** for the combined candidate unless the researcher explicitly changes the acceptance criteria. Do not ask the participant to repeat expected answers from the earlier pilot. An independent-work mandate under [proposed decision 0008](https://github.com/Motor-Learning-Lab/HILD/blob/a2116cdb8f75d70dfdc42840d7d7994bcd445600/HILD/decisions/0008-independent-work-and-human-acceptance.md) is **not** part of this supervised test; it needs its own later exercise.

## Prepare the exact candidate

The three PRs are stacked, not merged into `main`:

| PR | Contribution to the candidate | Base |
|---|---|---|
| [#11](https://github.com/Motor-Learning-Lab/HILD/pull/11) | Fixes observed installation, startup, consent and state problems | `main` |
| [#13](https://github.com/Motor-Learning-Lab/HILD/pull/13) | Clarifies HILD's process and its GitHub/skills workflow | PR #11's branch |
| [#14](https://github.com/Motor-Learning-Lab/HILD/pull/14) | Provides this test plan and its supporting plan/journal updates | PR #13's branch |

**Test the head commit of PR #14**, which includes the parents' changes. Its SHA is not fixed in this file because editing a PR or carrying later parent changes forward will change it. Immediately before the test, record the current 40-character SHA and verify CI for *that exact commit*:

```sh
gh pr view 14 --repo Motor-Learning-Lab/HILD --json headRefOid --jq .headRefOid
```

If a parent PR changes, it is **not** automatically incorporated into existing descendants. Forward-merge the updated parent into each descendant without rewriting pushed history; check the PR #14 ancestry, record the new SHA, and rerun relevant automated checks. A past CI run or pilot tests only the revision it actually used.

The initial [October 2026 Windows pilot](https://github.com/opherdonchin/HILD-onboarding-ipad-2026-10/pull/2) found that `core.symlinks=false` can turn `.claude/skills` into a plain file on checkout, even though the initial install looked successful. PR #11 now refuses unsafe Windows settings before writing. Its [Windows/Ubuntu installation checks](https://github.com/Motor-Learning-Lab/HILD/actions/runs/40746166251) and [mechanical checks](https://github.com/Motor-Learning-Lab/HILD/actions/runs/40746166212) passed. These are regression evidence, **not** a completed retest of the combined candidate.

## Agree on the test host before touching it

Record the new target repository, local workspace, OS/shell, coding agent and version (when available), selected HILD integrations (default: all), PR #14 candidate SHA and known prerequisites. Confirm the target is genuinely new and contains no work to preserve. Do not provision a repository or wiki, change credentials or Git settings, or delete anything without the researcher's specific agreement. If an essential test component cannot be authorized or run, mark it **BLOCKED**, not passed.

### First-contact prompt

Start a **new conversation** with the chosen coding agent working in the approved test repository. Replace `<CANDIDATE_SHA>` with the checked PR #14 head SHA:

> I'd like to start using HILD (Human-in-the-Loop Development) in the repository currently open in my coding environment.
>
> I'm new to HILD. For this test, use HILD at commit `<CANDIDATE_SHA>`, **not** the `main` branch. Read its README at `https://github.com/Motor-Learning-Lab/HILD/blob/<CANDIDATE_SHA>/README.md` and its `hild-integrate` skill at `https://github.com/Motor-Learning-Lab/HILD/blob/<CANDIDATE_SHA>/.agents/skills/hild-integrate/SKILL.md`. Follow the process and companion instructions **from the same commit**.
>
> Please help me decide whether and how to adopt HILD here. Explain why each decision matters. Don't change local files or GitHub resources without the appropriate agreement.

The agent must establish a local HILD source checkout at the pinned commit before installing. Merely reading the correct URL while installing files from an arbitrary `main` clone does not count.

## Installation and platform-specific checks

The researcher should see the read-only preview **before** explicitly authorizing `--apply`. The chosen integration list must match the agreement. From the confirmed source checkout:

```sh
python HILD/scripts/install_hild.py --target /path/to/test-repo --agents all
# Only after explicit permission for the proposed file changes:
python HILD/scripts/install_hild.py --target /path/to/test-repo --agents all --apply
python HILD/scripts/install_hild.py --target /path/to/test-repo --verify
```

Use the selected integrations instead of `all` if different. Verify that `HILD/installation.json` records the pinned `source_commit`. `--verify` checks files and links, **not** whether an agent uses the skills correctly. Distinguish skills that were installed, discovered, executed and actually used.

For native **Windows + Claude Code**, inspect `git config --get core.symlinks` in the target before applying. The candidate should refuse `false` or unset configuration and explain why. If the researcher separately authorizes a local Git change, enable symlinks and verify Windows can create directory symlinks. Confirm `.claude/skills` has Git mode `120000` and is a working directory link **after a fresh checkout with symlinks enabled**; its existence immediately after installation is insufficient. Do not silently fix an unsafe configuration.

If the installer fails during file creation, report what it rolled back. If later verification fails, newly created files may remain; report that state and **do not blindly rerun `--apply`**. Confirm session orientation reads local status without fetching or pulling the wiki. Read the plan and journal themselves to see whether important milestones were actually recorded.

Other agent platforms, runtime hooks and wiki access are separate capabilities. Report which were genuinely exercised; mark the others **NOT TESTED** rather than extrapolating from Windows/Claude evidence.

## Record evidence and decide what follows

For each stage in the exercise table, record **PASSED**, **FAILED**, **BLOCKED** or **NOT TESTED** with links to the issue, PR, commits, CI runs, wiki pages or a retained conversation transcript. Distinguish the agent's claim from an observed action. The result belongs on [scope #12](https://github.com/Motor-Learning-Lab/HILD/issues/12) or the agreed validation issue, not only in chat.

Any missed human stopping point means the relevant stage **FAILED**, even if file verification passed. If the exercise fails, repair the owning still-open HILD PR (#11 for installer/tooling, #13 for process guidance, #14 for the procedure), carry the corrected parent forward, rerun CI and plan another **fresh** attempt. Do not substitute a repaired old test host for validating the new candidate.

Only after the full required exercise succeeds (or the researcher explicitly revises its criteria) may the researcher consider approving and squash-merging HILD PRs **#11, #13, #14 in order**. After each parent merges, check the next PR's base and resulting diff against `main`. Then verify the ordinary published `main` onboarding path separately. Close [scope #4](https://github.com/Motor-Learning-Lab/HILD/issues/4) and [scope #12](https://github.com/Motor-Learning-Lab/HILD/issues/12) only when their remaining agreed goals are actually met.

The test results and any changes to the criteria remain durable in the linked issues and PRs. This file remains the **historical procedure for the scope #12 candidate test**, not a claim that later releases have passed it.
