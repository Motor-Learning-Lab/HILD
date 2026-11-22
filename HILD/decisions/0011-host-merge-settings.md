# 0011 — Installation proposes squash-only merge settings before the first merge

**Date:** 2026-11-22 · **Status:** Accepted on the researcher's merge of [PR #31](https://github.com/Motor-Learning-Lab/HILD/pull/31)

**Relationship to earlier decisions:** Extends [decision 0002](0002-squash-only-merges.md) from HILD's own repository to every repository HILD is installed in. 0002's rule (squash merges only, with the PR title and description as the commit message) is unchanged.

**Context:** GitHub's defaults allow merge commits and fill a squash commit's message with the branch's commit messages. The first merge went wrong twice:
- **HILD's own first merge** on 2026-10-14 was a merge commit ([journal](../journal/2026-10-14.md)).
- **In the [scope #12 onboarding test](https://github.com/Motor-Learning-Lab/HILD/issues/12#issuecomment-7071278845) on 2026-11-22,** the installation PR's squash commit carried the commit messages instead of the PR explanation ([#28](https://github.com/Motor-Learning-Lab/HILD/issues/28)).

The installation procedure said only "separately verify the repository's GitHub squash settings". The installation scope did not cover them, so the test agent could not change them without a second scope.

**Decision:**
- **The rule:** `process.md` (*Git and GitHub*) says the repository's settings enforce 0002. Only squash merges are allowed, the PR title and description are the squash defaults, and merged branches are deleted.
- **Installation:** before the installation PR is merged, the agent reads the settings. If they differ, it proposes the change as an external change. It applies the change only with the researcher's agreement, given in the installation scope or separately, then reads the values back and records them on the scope issue.
- **The installer itself does not touch GitHub.**

**Why:**
- **Having the installer set the values** was rejected. The installer writes only local files after a preview. Changing GitHub settings is an external change that needs its own agreement and admin rights.
- **Leaving it to the researcher's choice on the merge screen** was rejected because it failed in both first merges.
- **A check in `--verify`** was not adopted for now, because `--verify` checks local files and works offline.

**Consequences:**
- [`first-install.md`](../../.agents/skills/hild-integrate/first-install.md) gains a step before the first merge, and the scope template's installation note mentions merge settings.
- Without admin access, the agent explains the manual choice on the merge screen.

**Validation:** the next fresh installation should show the proposal before the first merge. That is **not yet observed**.
