# Presentations and approval — HILD process topic

Part of the [HILD process](../process.md), which every session reads first. Read this file before writing a proposal or PR explanation, or asking for review.

## Presentations

1. **Purpose first.** Which goal this serves and why now. If it cannot be connected to a
   goal, say so: that is a warning sign.
2. **What you should understand.** Two or three things the reviewer should be able to
   explain by the end.
3. **Explain in layers,** using the [PR explanation template](../templates/pr-explanation.md).
   Start with a plain-language summary, then discuss the important parts, evidence
   and consequences. Include mathematical background when relevant, and describe
   surprises when there were any. **Omit sections that have nothing to say.**
   The template is a default: the researcher may agree to adjust the format for
   the project's work without losing the purpose of each review.
4. **Interconnected explanations and evidence.** Link important claims,
   decisions, results, code and explanations to the material they rely on,
   so a future researcher or agent can follow and evaluate the reasoning.
   **GitHub implementation:** Every claim about code links to the exact
   lines with a GitHub permalink (`https://github.com/<owner>/<repo>/blob/<commit>/<path>#L10-L20`). Every
   other reference, to an issue, pull request, commit, file, decision record, wiki page
   or notebook cell, is a link too, in anything posted on GitHub and in every file in the
   repo. Do not rely on GitHub to make the link: a bare `#12` or commit hash links only
   in issue and PR text and never inside backticks, and nothing links by itself in a
   repository file or the wiki.
5. **Load-bearing vs boilerplate.** The walkthrough labels code as *load-bearing — read
   this* or *boilerplate — skim*.
8. **Math that survives GitHub's markdown.** Display math goes in fenced ` ```math `
   blocks, whose content markdown leaves alone. In `$...$` and `$$...$$`, markdown eats
   a backslash before punctuation (`\,` `\;` `\!` `\{` become `,` `;` `!` `{`) and
   mangles `<`; avoid them there (write `y_{1:t-1}`, not `y_{<t}`, and `\lbrace`,
   `\rbrace` for braces). Check that with `gh api markdown` when in doubt. GitHub also
   refuses some macros, `\operatorname` among them (write `\mathrm{...}`); that error
   appears only in the browser, so `gh api markdown` cannot show it.
9. **An explanation always describes the change as it now stands.** After review, the
   explanation is rewritten in place, not patched: a reader should never have to combine
   an old description with a list of amendments. What changed in response to review is
   recorded at the very end, in a dated *Changes after review* section; each later round
   appends another.

10. **Wiki pages are part of an explanation.** Every explanation has a *Wiki pages*
    section with two lists. *Relevant pages:* each existing wiki page the change relies on
    or affects, with how it is relevant and its status, so the reviewer can see which
    background they have confirmed and which they have not. *Proposed pages:* each page
    the change calls for, new or to be updated, with what it would cover. A concept page
    the reviewer needs in order to follow the change is written before review (rule 6)
    and listed as relevant. The other proposed pages are written once the reviewer
    agrees to them; code pages after the merge, because they record a `main` commit.

## Approval

**GitHub implementation:** The agent provides the actual PR link and current
explanation and requests review. The researcher chooses a track; the PR
description proposes one. PR comments can document the track and discussion,
and the agent may faithfully attribute an approval received in chat, but a
specific comment phrase is **not** mandatory for PR acceptance. The researcher
alone approves the final merge and performs it. A draft PR or merely sending
a status link does not constitute human review.

| Track | Appropriate for | Review expected | Acceptance |
|---|---|---|---|
| **Trivial** | Typos, straightforward wording changes, pinned dependency bumps | Brief inspection; no formal explain-back | Researcher accepts and merges |
| **Read** | Documentation, process text, decision records | Read the change and raise questions | Researcher accepts and merges |
| **Full** | Code and changes whose behavior is not evident from text | Explain back what changed and why; agent checks against actual behavior | Researcher accepts and merges |
| **Fast** | Code when immediate detailed review is not worthwhile | Confirm purpose, inputs/outputs and affected areas | Researcher accepts and merges, with visible understanding debt |

On the full track, compare the researcher's explain-back with the
implementation. A mismatch means the explanation or change needs work.
On the fast track, label the PR `understanding-debt`, create a follow-up
issue and mark related wiki pages `needs-review`. On every track, accepting
a PR does not by itself mean that any related page is understood (see
*Understanding map*). The conservative trivial
category may be recalibrated by the researcher. Review depth, explicit
execution permission, PR acceptance and merging are separate decisions.
