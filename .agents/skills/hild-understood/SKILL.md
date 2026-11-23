---
name: hild-understood
description: Drafts and updates the researcher's understanding-map pages and their statuses, and records the researcher's own judgment of what they understand. Use after a merge that calls for wiki pages, when a page no longer matches the repository, when the researcher confirms or withdraws their understanding of a page, or when creating a new wiki has been approved.
---

# Understood: maintain the understanding map

Who judges understanding is in the [HILD process, §6](../../../HILD/process.md#6-understanding).
Page kinds, statuses, who sets them and when the map is pushed are in
[the understanding-map topic](../../../HILD/process/understanding-map.md).
The formats are the [code-page](../../../HILD/templates/wiki-code-page.md)
and [general-page](../../../HILD/templates/wiki-page.md) templates.

**Read [new-wiki.md](new-wiki.md) when** the project has no wiki and the
researcher has approved creating one. If you find an existing wiki you were
not told about, stop and propose a separate scope for integrating it; do
not create or overwrite a wiki implicitly.

## Steps

1. **Get the latest pages.** Find the map's recorded location. If there is
   no local clone, ask before making one
   ([§7](../../../HILD/process.md#7-rules-at-every-step)). Pull with
   `--ff-only`; if that fails, stop and explain rather than overwrite
   anyone's edits.
2. **Write from the repository as it is.** A code page describes code
   already on `main` and records that commit. When a page may be out of
   date, compare what it describes with the current source. Link every
   claim to the lines it relies on.
3. **Set statuses as the topic says.** Never mark a page `understood`
   yourself. When the researcher confirms or withdraws their understanding,
   record it, quoting them.
4. **Keep navigation current.** Update `Home` and the sidebar. If
   `HILD/scripts/wiki_status.py` is installed, run it with `--write` on the
   wiki and read what it changed; it does not commit or push.
5. **Publish straight away.** Commit and push the wiki after each change,
   then give the researcher the page links and say which pages await their
   reading.

In onboarding, the first PR may propose a `Process-HILD` page; write it
only after that PR merges.
