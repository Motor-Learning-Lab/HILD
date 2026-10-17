---
name: hild-scope
description: Work with the researcher to agree on a manageable scope before nontrivial development. Use when someone wants to plan work, scope a change, or begin HILD onboarding.
---

# Scope — develop an agreement together

Authority: [HILD process](../../../HILD/process.md), *Scope agreements*.
The completed agreement uses the
[scope issue template](../../../HILD/templates/scope-issue.md).
Locate the host project's real plan, decisions and process; `HILD/` is
the default, not a reason to duplicate files kept elsewhere.

## Begin a conversation, not a form

Start with what the researcher is trying to achieve and why that work
matters. Read the current plan and relevant decisions; draw on goals
already stated instead of asking the researcher to repeat them.

If the researcher has just agreed to **develop** a first scope, explain
briefly that HILD uses scopes to agree on manageable work, and that the
agreement will eventually be recorded as a GitHub issue. Then **discuss
the goal**, not the installer, working directory, settings or every step
of implementation.

For example, *when the person has already said they want to install
HILD and learn by doing*:

> Great. Let's develop our first scope together.
>
> In HILD, a scope is an agreement about a manageable piece of work. We
> start by agreeing on what we want to achieve, then decide what belongs
> in that work, what should wait, and how we'll know we've succeeded.
> Once we're satisfied, we'll record the agreement as a GitHub issue.
>
> You've said you want to learn HILD while installing it in your
> repository. I suggest our first scope have two outcomes: a repository
> ready to use HILD, and a first experience making and reviewing
> decisions together about how the work should proceed.
>
> Does that capture what you'd like to accomplish, or is there
> something else you want to get out of this first scope?

**Adapt to the person's actual project and situation.** This example
illustrates the *interaction*, not a mandatory script.

## Build shared understanding of the work

The agreement needs four things:

- **Goal:** what the researcher wants to accomplish, and why.
- **Boundaries:** what belongs in this work and what waits.
- **Evidence:** how the researcher and agent will recognize success.
- **Autonomy:** what the agent can decide or change within the scope,
  and what still needs explicit human agreement.

These describe **the finished scope**, not four questions to ask
in a fixed order. Develop them naturally, following the researcher's
responses. Summarize decisions periodically so the agreement becomes
visible. Don't rush to file an issue or proceed with development simply
because the researcher said "yes" to discussing a scope.

Contribute expertise: suggest a reasonable default and explain **why
it will serve the researcher**. Mention available alternatives briefly;
compare a few choices if the tradeoffs matter. Avoid a broad menu or
configuration questionnaire unless options materially affect the outcome.
When a blocker becomes relevant to the agreed work, help diagnose it
and propose a feasible next step instead of merely stopping.

## Onboarding only

If the researcher wants an **onboarding scope**, read
[onboarding-scope.md](onboarding-scope.md) and adapt its suggestions to
the current repository. Do not read that companion for ordinary scopes.
Onboarding is still a normal, reviewed development scope; avoid
duplicating process rules in a special onboarding procedure.

## Record the agreement and stop

Once the researcher understands and agrees on the work, prepare an issue
using the [canonical template](../../../HILD/templates/scope-issue.md).
Explain in plain language what it authorizes and what it does not.
If GitHub is accessible and the researcher has explicitly agreed to
**create the scope issue**, create it labelled `scope` and link it.
Otherwise present the draft without claiming it exists.

**An invitation to start scoping is not approval of the final scope.**
Do not implement the work until the human explicitly approves that
scope; record approval in the issue. If an agreed boundary changes later,
propose an amendment and wait rather than drifting.

Never merge a pull request or mark the researcher's understanding
confirmed on their behalf.
