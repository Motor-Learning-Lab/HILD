# Git and GitHub details — HILD process topic

Part of the [HILD process](../process.md), which every session reads first. Read this file before opening or finishing a PR, preparing one for merge, or changing merge settings.

## Git and GitHub

- The repository's GitHub settings enforce this: only squash merges are allowed, the
  squash commit's default title and message are the PR's title and description, and
  merged branches are deleted
  ([decision 0011](https://github.com/Motor-Learning-Lab/HILD/blob/main/HILD/decisions/0011-host-merge-settings.md)).
  Changing these settings is an external change: the agent proposes it, applies it only
  with agreement, reads the values back and records them. A new installation does this
  before its first merge.
- **Superseded material** — the one rule, referred to elsewhere:
  - on a branch, move it to `archive/` so it stays at hand while the work continues;
  - the final commit before merge deletes `archive/`; the material stays reachable
    through the PR's commits;
  - on `main`, delete superseded files rather than keeping `old` copies; git history is
    the archive. Update or remove references in the same change.
  - Exception: decision records are kept and marked superseded.
- A PR description links its scope issue with `Closes #N` only when the PR
  finishes issue N; otherwise it writes `Part of #N`. GitHub closes an
  issue automatically when a PR containing `Closes #N` merges.
- Replies to review comments go in the comment's own thread, with permalinks to the fix.
