---
name: hild-understood
description: Draft and maintain the reviewer's understanding-map pages, including post-merge code pages, explanations of concepts, guides, resources, and HILD process pages. Use after a merge, when understanding changes, or when a page is stale.
---

# Understood

Rules: [HILD process](../../../HILD/process.md), *Understanding map*.
Templates: [wiki code page](../../../HILD/templates/wiki-code-page.md) and
[general wiki page](../../../HILD/templates/wiki-page.md).

The original arrangement is a separate GitHub wiki repository cloned into a gitignored `wiki/` directory; the target installation records its own actual location. **Do not create or overwrite a wiki implicitly.** In particular, existing-wiki integration is outside the first-install scope.

1. **Locate and pull first.** Determine the configured understanding map and its Git remote. For a Git-backed wiki, pull fast-forward only before editing to preserve browser changes. If unavailable or divergent, report and stop; don't overwrite.
2. **Draft or revise from source.** A code page describes actual merged code and records its `main` commit, never an unmerged branch head. For a stale page inspect the diff since its recorded commit. General pages use the kind appropriate to the subject.
3. **Preserve reviewer authority.** The agent may set `draft`, `stub`, `needs-revision`, or `needs-review` when justified; **only the researcher** may confirm `understood`. Link related pages and create stubs for missing links only within the agreed change.
4. **Keep navigation and status current.** Update Home and sidebar. If installed, run `HILD/scripts/wiki_status.py --write` against the configured wiki and check its changes. The script does not commit or push.
5. **Publish promptly.** Commit and push the wiki after each approved update; report page links and those awaiting human review.

For onboarding, the scope/PR may propose a `Process-HILD` wiki page, but write the agreed draft **after** the onboarding PR has merged.
