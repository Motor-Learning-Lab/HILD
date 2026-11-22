# Decision records — HILD process topic

Part of the [HILD process](../process.md), which every session reads first.
Read this file before creating, changing or superseding a decision record.
What a decision record is, that it arrives only by a reviewed PR, and that
titles are read before deciding in an area, are in the process,
[§5](../process.md#5-state-in-files).

## How one decision changes another

A *new decision* may **modify**, **overrule** specific provisions of, or
**replace** an earlier decision. It must link the predecessor, state the
precise effect and what still applies, and explain its reasoning in full.
An earlier accepted decision remains historical evidence even when its
current applicability changes.

## Reference implementation

- **Files:** Decisions use numbered files
  `HILD/decisions/NNNN-short-title.md` and
  [the decision-record template](../templates/decision-record.md). The agent
  drafts them and the researcher accepts them by reviewing and merging a
  PR on the *read* track.
- **Forward notice:** In the same PR that introduces the successor, edit
  the **beginning** of every affected older record to show a prominent
  link to the proposed successor and summarize its intended effect. Keep
  the historical content intact. Distinguish *proposed* supersession
  (not yet operative) from *accepted* supersession. Upon acceptance, the
  older record's opening notice identifies any partial or full supersession
  and links to the accepted successor. Do not bury this notice at the end.
- **Current authority:** Update the operative rule in the [HILD process](../process.md)
  or its topic files (or the relevant project's rules) when the successor is
  accepted. A proposed PR's changes are not accepted authority until
  human review/merge.
- **When:** Draft a record for decisions constraining future work—tools,
  models, conventions and rejected alternatives worth remembering.
  Minor choices go in the journal.
