# Understanding map — HILD process topic

Part of the [HILD process](../process.md), which every session reads first.
Read this file before creating or changing an understanding-map page or its
status. Who judges understanding, and why the map is never authoritative, are
in the process, [§6](../process.md#6-understanding).

## Where the map lives

The reference implementation uses the repository's separate GitHub wiki,
cloned into a gitignored `wiki/` directory. An installation must identify its
authoritative understanding-map location; support for alternatives is an
unresolved design choice.

## Page kinds

A page's name starts with its kind (`Code-environment`,
`Concept-kalman-filter`), and `Home` and the sidebar group pages by kind.

| Kind | What it holds |
|---|---|
| `code` | One load-bearing module or finalized notebook: *What it does*, *How and why*, *How it fits the larger project*, *Invariants and pitfalls* (what must stay true if the code changes, and the mistakes that are easy to make). Records the files it covers and the `main` commit it describes. |
| `concept` | An idea the code relies on, linking code pages to the math. |
| `process` | How we work and how the tooling works: explanation of the process, as opposed to the project's content. |
| `guide` | A reading path: which pages to read, in what order, to understand an area. |
| `resource` | A background source: what it is, a link, and why it matters here. |

New kinds are added here when a real page needs one. The [code-page template](../templates/wiki-code-page.md) and [general-page template](../templates/wiki-page.md) give each page's format.

## Statuses

| Status | Set by | Meaning |
|---|---|---|
| `not-written` | nobody | No page exists yet. Another page links to it, or a pull request proposes it. |
| `stub` | agent | A page that exists only as a placeholder, still to be written. |
| `draft` | agent | Written by the agent; the researcher has not confirmed it. |
| `understood` | researcher only | The researcher currently confirms it; this may be withdrawn later. |
| `needs-revision` | either | The researcher has read it and it did not do its job, or the agent knows it falls short. The agent owes a rewrite. |
| `needs-review` | either | Merged on the fast track, or the researcher is no longer sure. |
| `stale` | script | The code changed materially since the commit the page describes. |

`not-written` is the one status that is not recorded on a page, since there is no page:
it is what an explanation's *Wiki pages* section says of a page that is linked or
proposed and does not exist.

`needs-revision` and `needs-review` point in opposite directions: the first says the
page must change, the second that the researcher must read it again.

**Changed pages need review again.** When a merged change alters what a page
describes, or the page itself is materially edited after the researcher confirmed
it, the page becomes `needs-review`, even if it was `understood`.

In the reference implementation, a generated *Status board* page lists the pages that exist by status, and the
`not-written` pages that some page links to.

## Who writes

The agent drafts pages; the researcher edits them, in the browser or
through the agent. When the researcher retracts an earlier `understood`
judgment, update the page status (normally to `needs-review` or
`needs-revision`, as appropriate) rather than treating the prior status
as authoritative.

## Staleness

A script compares the commit each code page describes with `main`;
pages whose code has changed materially become `stale`. Nothing yet surfaces
stale pages automatically ([#23](https://github.com/Motor-Learning-Lab/HILD/issues/23)):
for now the `stale` status is the signal, which agents and the researcher search
for and the *Status board* lists. Code pages record `main` commits (code as it stands); journals and
explanations may link to branch commits.

## When the wiki is committed and pushed

The wiki has no pull requests; its history is
its record. When a git-backed understanding map is configured, the agent pulls it before touching it (to pick up the researcher's browser edits) and commits and pushes it straight after every change it makes. Nothing is left
uncommitted in the local clone. When orientation tooling is installed, session-start data reports anything unpushed.
