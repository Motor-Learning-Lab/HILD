---
name: hild-orient
description: Presents a short start-of-session orientation: what needs the researcher, where the project stands, what changed and what comes next. Use at the start of a session, or when the researcher asks where the project stands or what to do next.
---

# Orient: where the project stands

What orientation is, and when it happens, is in the
[HILD process, §5](../../../HILD/process.md#5-state-in-files); how to talk to
the researcher is in [§4](../../../HILD/process.md#4-talking-with-the-researcher).
Use the host's recorded locations if its plan, journal or wiki are not at
HILD's defaults.

## Steps

1. **Gather the facts.** If a session-start hook supplied them, use them.
   Otherwise read the plan, the latest journal entry, recent Git history,
   open issues and PRs, and the understanding map's status yourself. Do not
   assume a hook or `HILD/scripts/session_context.sh` ran or exists.
2. **Check what is missing.** Note finished work the journal does not
   mention and wiki edits that are not pushed. Repair a journal gap with
   [`hild-journal`](../hild-journal/SKILL.md) before anything else, as §5
   says; report wiki gaps.
3. **Present, in about fifteen lines,** leading with what needs the
   researcher:
   - **Needs you:** PRs awaiting review, with their proposed tracks; scope
     issues awaiting approval; deferred approvals and the provisional work
     that depends on them; questions; wiki pages to read.
   - **Where we are:** the current goal and state.
   - **Since last time:** material changes, with links.
   - **Understanding debt:** work the researcher has not fully reviewed, and
     wiki pages that may no longer match the code.
   - **Next:** the plan's next step and what you propose now.

   If the researcher's first message asks for something else, keep this
   brief and then handle the request.
4. **Stop.** Wait for the researcher before starting unapproved nontrivial
   work ([§3](../../../HILD/process.md#3-the-researchers-authority)).

If a source of facts is unavailable, say so rather than filling it in from
memory.
