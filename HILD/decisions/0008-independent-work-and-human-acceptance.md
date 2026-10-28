# 0008 — Independent work, provisionality and human acceptance

**Date:** 2026-10-19 · **Status:** Proposed in [PR #13](https://github.com/Motor-Learning-Lab/HILD/pull/13); effective only upon human acceptance/merge.

**Relationship:** **Modifies** the general advance-implementation restriction of [decision 0006 — Review the actual scope issue before implementation](0006-scope-issue-approval-gate.md) *only* for expressly authorized independent work. Does not replace its ordinary scope-review procedure or remove human merge authority. Also clarifies review-track conventions in [the HILD process](../process.md).

## Context

The normal HILD workflow requires the researcher to inspect and approve the
actual scope issue before the agent implements it. The initial onboarding
pilot showed why this is important when the researcher is supervising work
step by step. However, HILD also permits the researcher to authorize an
agent to work independently, potentially advancing far beyond checkpoints
that would ordinarily require separate approval. Treating the authority to
**continue** as approval of every interim decision would destroy the
researcher's ability to review and reject that work later.

The original four PR review tracks also distinguished trivial changes by
whether a review comment was required. Practical work in
[MotorAdpatationSBI](https://github.com/opherdonchin/MotorAdpatationSBI)
has required researcher approval even for trivial PRs without consistently
using formal approval comments for larger ones. This distinction did not
function as intended.

## Decision

1. **Independent execution is not human acceptance.** When expressly
   authorized to work independently, an agent may pass ordinary stopping
   points and keep developing, including on the basis of choices not yet
   approved by the researcher. The agent must preserve an inspectable
   chronological trail of these choices, where authority was deferred, and
   which later changes depend on them.
2. **Provisional dependencies remain provisional.** Every action and result
   relying on an unapproved choice remains provisional until the researcher
   works through the relevant decisions and accepts, changes or rejects them.
   Later implementation or testing cannot retroactively authorize an
   upstream choice. A standing independent-work instruction is permission
   to proceed, not a blanket approval of decisions or results.
3. **Ordinary supervised work is unchanged.** Without a clear independent
   mandate, the issue-based pre-implementation approval gate of decision 0006
   still applies. The agent must not infer such a mandate from ambiguous
   agreement to discuss scope or choose an installation strategy.
4. **Human acceptance is required for every PR.** Review *depth* (trivial,
   read, full or fast) is separate from the acceptance decision. The human
   alone decides whether to accept and merge. A specific approval-as-comment
   formula is not required; comments can provide a useful durable review
   trail without becoming a substitute for the human decision.
5. **External consequences require care.** Git-tracked local edits can
   remain inspectable and provisional; an irreversible action on an
   external system cannot be undone by calling it provisional. The agent
   needs appropriate specific authorization for such consequences.

## Reference implementation

In the GitHub workflow, the agent preserves deferred permission points and
dependencies in the [journal](../templates/journal-entry.md), presents them
in the PR explanation and next-session orientation, keeps the affected
changes on an unmerged branch and draft PR, and links any proposed scope
revision to the original issue. The researcher reviews the deferred
decisions and downstream effects before acceptance. For ordinary work,
the agent still shows the actual `scope` issue and records approval there
before implementation.

Review tracks control explanation depth. PR comments may record the chosen
track and explain-back but are not mandatory acceptance tokens. The human
squash-merges the PR. Agent tools never merge on the human's behalf.

## Why and consequences

This permits useful long-running independent investigation without
mistaking delegated execution for delegated judgment. It preserves the
researcher's power to revisit provisional technical choices, and it keeps
the established carefully supervised onboarding workflow for projects
that have not elected independent operation.

The independent-work exception calls for targeted changes to the process,
scope, explanation, orientation and journal guidance, plus an explicit
**proposed successor notice at the beginning of decision 0006**. The
historical decision text is not rewritten. Once this decision is accepted,
the successor notice must be marked effective, and the operative process
and companion documents must agree.

## Validation

Use the next live onboarding test to check the **ordinary supervised**
path, including the scope-approval gate. Evaluate the independent-work
exception separately using a real, specifically authorized independent
task and a later human review of its provisional decision trail; no such
behavior is claimed tested merely because these instructions exist.
