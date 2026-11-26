---
name: hild-explain
description: Writes a pull request's explanation, keeps it describing the change as it stands, asks the researcher for review and responds to review. Use when opening a pull request (a draft included), after pushing to an open pull request, when work is ready for review, and when review comments arrive.
---

# Explain: the pull request's explanation, from draft to merge

The rules are in [the review topic](../../../HILD/process/review.md) and the
[HILD process, §3 and §4](../../../HILD/process.md#3-the-researchers-authority).
The format is the [PR explanation template](../../../HILD/templates/pr-explanation.md).
Branches, scope links and review threads follow [the Git topic](../../../HILD/process/git.md).

## Steps

1. **When the draft PR opens,** write its description straight away: link
   the scope issue (`Closes` or `Part of`, as the Git topic says) and state
   the purpose. A draft PR is a record of work in progress, not a request
   for review.
2. **After every push to an open PR,** check that the description still
   describes the change as it now stands, and fix anything the push made
   wrong, such as a link to a deleted file or moved lines.
3. **When the work is ready, write the full explanation from the actual
   change.** Record the head commit and read the whole diff against the
   PR's real base (`git diff <base>...HEAD`; a stacked PR may not target
   `main`). Explain what exists now, not what was first intended. Follow
   the template in the order a reader needs, not file order, and leave out
   sections with nothing to say. If the change cannot be explained in one
   sitting, propose a split and stop.
4. **Show provisional work.** If independent work deferred any approvals,
   list each one and the work that depends on it, as the process's
   [*Independent work*](../../../HILD/process.md#independent-work) requires.
   Passing tests do not accept those choices.
5. **List the wiki pages.** Read the understanding map's current state and
   fill the template's *Wiki pages* section. Write a concept page the
   researcher needs before asking for review, using
   [`hild-understood`](../hild-understood/SKILL.md). If no map is
   configured, say so.
6. **Check before asking.** Follow every link and line reference at the
   head commit. Check math rendering as the review topic says, or say it
   was not checked.
7. **Ask for review, then stop.** Mark the PR ready. Give the researcher
   its link, two or three sentences on what it changes, and the proposed
   review track, and ask them to review it. Wait for their answer.
8. **Respond to review.** Reply in each comment's own thread, with
   permalinks to the fix. After new commits, rewrite the explanation in
   place and add a dated *Changes after review* section at the end. On the
   full track, compare the researcher's explain-back with the code; on the
   fast track, record the understanding debt. Both are in the review topic.
9. **After the researcher merges,** record the milestone with
   [`hild-journal`](../hild-journal/SKILL.md), then write the agreed wiki
   pages with [`hild-understood`](../hild-understood/SKILL.md).

Never say a PR was approved, tests passed or a merge happened before the
evidence exists.
