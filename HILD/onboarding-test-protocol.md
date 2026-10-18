# Fresh HILD onboarding validation — combined candidate

**Status:** Proposed under [approved scope #12](https://github.com/Motor-Learning-Lab/HILD/issues/12). This protocol is not evidence that a live test has run. It is kept upstream in HILD, not installed into the host repository by default.

## Purpose

Verify both HILD's **process** and its **GitHub/skills reference implementation** in a genuinely new repository. The preceding Windows/VS Code pilot produced useful behavioral evidence and found defects; do **not** repair or reopen that disposable installation for this test.

Use a **stacked, unmerged candidate** until the researcher has observed a successful onboarding run:

| PR | Contains | Base branch |
|---|---|---|
| [#11](https://github.com/Motor-Learning-Lab/HILD/pull/11) | Concrete installation, startup, approval and state corrections | `main` |
| [#13](https://github.com/Motor-Learning-Lab/HILD/pull/13) | Process requirements separated from reference mechanisms, plus proposed decision 0007 | `fix/portable-first-install-validation` |
| [#14](https://github.com/Motor-Learning-Lab/HILD/pull/14) | This validation protocol and review evidence | `docs/process-versus-reference-implementation` |

The **HEAD commit of PR #14** is the combined candidate: its ancestry includes the commits in PRs #11 and #13. This is a *test source revision*, not the stable HILD `main`. Record its exact 40-character SHA **immediately before the test** using:

```sh
gh pr view 14 --repo Motor-Learning-Lab/HILD --json headRefOid --jq .headRefOid
```

If PR #11 or #13 acquires further commits, those changes **do not automatically appear** in already-created descendant branches. Incorporate the updated parent into each descendant by ordinary forward Git merges, with no history rewrite, and reconfirm the ancestry and PR #14 SHA. Re-run relevant CI on the combined candidate. **Never report a test as validating a changed SHA that it did not execute.**

## Before starting — researcher approval

**No new test repository, GitHub wiki, permission change or deletion is authorized by this protocol.** The researcher agrees separately on the new GitHub repository, local workspace and agent/platform combination. Confirm a clean, newly initialized target with no work to preserve or silently overwrite.

Record in [scope #12](https://github.com/Motor-Learning-Lab/HILD/issues/12) or the agreed validation issue: target repository, local OS/shell, coding agent and version where known, selected HILD agents (default: all), candidate SHA, and any relevant platform-specific prerequisites (e.g. Windows symlink support). Record any *capabilities not tested*, rather than promising universal support.

This is an agent-guided onboarding experiment; the person doing it should not be required to recite the expected answers or the previous failures.

## A fresh first-contact prompt

Open a **new conversation** with a coding agent that can work on the newly approved test repository. Replace `<CANDIDATE_SHA>` with the verified PR #14 head commit:

> I'd like to start using HILD (Human-in-the-Loop Development) in the repository currently open in my coding environment.
>
> HILD develops a human-supervised scientific software process, and currently provides a GitHub-and-agent-skills reference implementation.
>
> For this test, use HILD **at commit `<CANDIDATE_SHA>`**, not the `main` branch. Read its README at `https://github.com/Motor-Learning-Lab/HILD/blob/<CANDIDATE_SHA>/README.md` and its `hild-integrate` skill at
> `https://github.com/Motor-Learning-Lab/HILD/blob/<CANDIDATE_SHA>/.agents/skills/hild-integrate/SKILL.md`. Read the process and any companions it directs you to **from the same commit**.
>
> I'm new to HILD. Guide me through deciding whether and how to adopt it in this repository. Explain the purpose behind our choices, not just the GitHub or shell commands. Don't change local files or GitHub resources without our appropriate agreement.

The agent must establish the upstream source revision and source checkout before installation. If the agent can only read GitHub URLs, work with the researcher to establish a reproducible local source checkout at the pinned commit when installation becomes authorized; don't mistake an arbitrary `main` clone for that source.

## What to observe — process first, mechanisms second

Observe the actual human–agent conversation, not just the presence of files. A concise score sheet should mark each item **PASSED, FAILED, BLOCKED or NOT TESTED**, link to evidence (GitHub issue, PR, commit, test run, or locally retained transcript), and distinguish the agent's claims from what was observed.

| Process requirement | Reference implementation / observation |
|---|---|
| Purpose-led onboarding | The agent connects HILD's objectives to the repository; it introduces GitHub and skills as means rather than HILD's definition |
| Bounded authorization | Goal, limits, evidence and autonomy developed naturally; the agent creates a **proposed issue**, links it, explains what it permits and excludes, then stops for human inspection and approval |
| Durable human approval | The researcher reviews the **actual issue**; approval is recorded on that issue *before* implementation |
| Implementation-specific consent | A read-only installer preview shows proposed paths. The researcher explicitly authorizes `--apply`; choosing between implementation options alone is **not inferred as execution consent** |
| Inspectable change | Agent works on a branch, opens a draft PR early, records what changed, and does not merge for the human |
| Reproducible install | Manifest `source_commit` equals the candidate SHA; source and target remain distinguishable; verifier passes or failures are accurately identified and recoverable |
| Platform adaptation | Agent explains the function of skills/symlinks/hooks and collaborates on any needed workaround without quietly dropping an approval or review safeguard |
| Recoverable work in progress | Scope, PR, decisions, results and next step appear in the plan/journal **before** merge; a new session can find current state |
| Meaningful review | Agent provides the actual PR link, layered explanation and evidence, proposes a review track and waits; reviewer records the chosen track and **only the researcher merges** |
| Understanding map | If approved, a *fresh* wiki has working Home/sidebar/status-board navigation; the board is generated correctly on first pass; only the human can confirm `understood` |
| Human acceptance and recovery | After human merge, final state updates and an agreed wiki draft (if proposed) are recorded; an independent fresh session uses the plan/journal and GitHub state to orient without silently modifying wiki content |

Check **installed, discovered, executed and used** separately for agent skills and hooks. Windows Claude symlinks, Unix path serialization, Codex/Copilot runtime hooks and wiki remote access are not interchangeable evidence; report what was tested on the selected platform. It is acceptable to mark optional agent platforms **NOT TESTED** rather than manufacture results.

## Mechanical checks and stopping points

Before the human approves installation, inspect and discuss the preview. After approval, run:

```sh
# From the confirmed candidate HILD source checkout:
python HILD/scripts/install_hild.py --target /path/to/test-repo --agents all
# Only with the researcher's separate approval of that exact preview:
python HILD/scripts/install_hild.py --target /path/to/test-repo --agents all --apply
python HILD/scripts/install_hild.py --target /path/to/test-repo --verify
```

Use the exact chosen agent selection instead of `all` when agreed. `--verify` checks structural integrity, not live agent behavior. If file creation fails, report the rollback; if verification fails *after* file creation, report that newly created files remain in place and **do not re-run `--apply` blindly**.

For Windows, verify that the linked Claude skills folder actually resolves, that Git records the link as mode `120000` and that a fresh checkout with appropriate symlink support preserves the link. A shell, Git configuration or permission problem invites collaborative diagnosis, not false success.

The session orientation script must report local state without fetching/pulling the wiki clone. Confirm current plan and journal *contain* the recent milestones rather than merely checking that the collector read a file.

If any human stopping point is violated, the test is **FAILED** even when the installation files are mechanically correct. Stop, document the observed failure and decide on an upstream correction within the **still-open** relevant PR.

## How to finish

Keep all three HILD PRs open and unmerged until the researcher has completed this fresh installation and human review/merge and a fresh-session recovery check, or has explicitly amended the success criteria.

If candidate onboarding fails, fix the defect in PR #11 when concrete tooling is at fault, PR #13 when the process/mechanism guidance is at fault, or PR #14 when the test procedure is at fault. Propagate parent commits through stacked branches without force-pushing, then start another **fresh** test from the new candidate SHA. Do not declare the old host fixed as a substitute.

Once successful, the researcher reviews and squash-merges the **HILD PRs in order** (#11, #13, #14), adjusting each PR base to `main` after its parent is merged and checking the resulting diff. Human approval and merge are separate from the test pass. Afterwards, retest the ordinary public `main` getting-started path to establish published behavior, and only close [scope #4](https://github.com/Motor-Learning-Lab/HILD/issues/4) and [#12](https://github.com/Motor-Learning-Lab/HILD/issues/12) when their agreed remaining conditions are met.
