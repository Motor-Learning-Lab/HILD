# 0002 — Squash merges only

**Date:** 2026-10-14 · **Status:** Accepted (human-reviewed in [PR #2](https://github.com/Motor-Learning-Lab/HILD/pull/2), merged 2026-10-14)

**Context:** We need rapid, small commits during development, permanent links to reviewed intermediate work, and a `main` history where each feature has one meaningful explanation.

**Decision:** Merge branches by squash only, after explicit human approval. The squash commit uses the pull request title and description, updated to reflect the final change. Delete merged branches. Open a draft PR as soon as the branch is pushed; never rewrite pushed PR history. Superseded material can be retained in a branch `archive/` during work, but is removed by the final pre-merge commit; it stays accessible through earlier PR commits. Keep superseded **decision records** as history.

**Why:** The human reviewer can inspect every intermediate commit in the PR, while the integration branch receives one explanatory commit. Rebase/squash history rewriting would break permalinks; merge commits clutter `main`. The rationale and alternatives were established in the original project's [decision 0004](https://github.com/opherdonchin/MotorAdpatationSBI/blob/main/docs/decisions/0004-squash-merge-branch-archives.md).

**Consequences:** HILD repository settings should disable rebase and merge commits, enable squash using the PR title and description, and delete branches automatically. **These settings are not yet configured** (GitHub currently allows all three methods); they require an administrative setting change. Until then, only squash merges are permitted by policy.

**Origin:** [HILD scope #1](https://github.com/Motor-Learning-Lab/HILD/issues/1).
