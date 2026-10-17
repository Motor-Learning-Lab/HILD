# Onboarding: introduce HILD and develop a useful first scope

**Read this companion when a researcher is unfamiliar with HILD, asks for
guidance getting started, or wants an onboarding scope.** It is the single
procedural home for newcomer-facing introductions and first-scope examples,
whether HILD is already installed or the researcher is still considering
installation. It is **not a separate skill**.

The [HILD process](../../../HILD/process.md) remains authoritative for
scope agreements, issues, pull requests, review, and approval. The general
[hild-scope skill](SKILL.md) defines ordinary scope development; the
[hild-integrate skill](../hild-integrate/SKILL.md) defines read-only assessment
and installation boundaries. This companion adds the *onboarding-specific
interaction*, not another copy of those rules.

## First contact: explain the value before discussing installation

Assume the researcher may know little about HILD. Introduce it as an approach
to AI-assisted scientific software development that keeps the researcher in
control of decisions and helps them deeply understand the resulting code
and algorithms.

Explain in accessible terms how small agreed scopes, reviewable changes,
further explanation when something is unclear, durable plans and decisions,
and a separate understanding-map wiki work together. **HILD does not run
inside the wiki:** issues and pull requests coordinate development; the wiki
documents important concepts, code and the researcher's understanding.

Then connect these ideas to **the researcher's own repository and goals**.
Show interest in what they want to build. For a nearly empty repository,
installing HILD can itself be a useful first development exercise, helping
the researcher clarify how the project should proceed. For an established
project, explain how HILD might support existing work without displacing it.

Invite the researcher to **develop a first scope together**. Do not open with
a full authority map, installation inventory, verification checklist or
request to approve implementation. Make clear that a scope issue is an
agreement about manageable work, and that creating it is a later step.

This example illustrates the *purpose* of an introduction, not prescribed
text:

> HILD helps you develop scientific software with an AI agent while
> keeping you in control of what gets built and understanding how it works.
> We'll agree on small pieces of work, review the changes, and preserve
> important decisions and explanations so the project remains understandable.
>
> Your repository is currently almost empty, so we could learn HILD
> while preparing it for the project you want to build. One of HILD's first
> practices is to agree on a scope for a manageable piece of work.
> Would you like us to develop that first scope together?

Adapt this to the researcher and repository. Don't recite it unchanged or
repeat goals the researcher already supplied.

## After the researcher says yes to *developing* a scope

Start **collaboratively defining the goal**, not configuring tools or
requesting implementation permission. For a researcher who has already said
they want to learn HILD by installing it, this is an example of the next
response the human reviewer found useful:

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

It is an **example, not a fixed script or a required four-question
interview**. Follow the researcher's answer. They have agreed to
*discuss* a scope, not approved one or authorized installation.

## During onboarding: surface decisions when useful

Bring up consequential choices only as they become relevant, recommending
the normal default and explaining why it might help the researcher:

- Where will project rules, plan, journal and important decisions live?
  Does the default `HILD/` location avoid competing copies?
- What kind of explanations and progress records will help this researcher
  understand the scientific work? Are the default PR and journal formats
  enough for now?
- Which coding agents will the researcher actually use? HILD can configure
  several agents while keeping one shared core.
- How will the researcher maintain their understanding map? Is there a
  **new** wiki to initialize, or must an existing wiki be left untouched?

Don't require a formal answer to every item. When a default fits, keep it.
Defer extensive customization to another scope if necessary. Create a
decision record only for a genuine consequential choice.

**When a blocker becomes relevant to the next agreed action**, investigate
what access and tools are available, explain the most practical route, and
help the researcher resolve it. A missing local checkout matters before
running an installer, not as the opening topic before developing the goal.

## Onboarding work and evidence

If HILD is not installed, a **reviewed installation** can be the first
useful scope. If it is installed, choose a small, real task that advances the
researcher's project; do not create throwaway exercises.

Let the [normal HILD process](../../../HILD/process.md) introduce each issue,
draft PR, explanation, review, merge, journal and decision as it becomes
relevant. Do not teach the full workflow upfront or create a special
parallel onboarding workflow.

An onboarding PR may propose a `Process-HILD` wiki page explaining HILD
**in this repository**, with links to authoritative files. If approved,
draft it **after the PR merges**. Only the researcher may confirm that a
page is `understood`.

Keep **installation integrity** (files and configuration) distinct from
**onboarding validation** (observed human-agent behavior and understanding).
Record what passed, failed, was blocked, or was not tested; a new session
should recover state from durable project records. A beginner may choose
onboarding, but it is not required for every installation or update.

Do not initialize or reconcile a pre-existing wiki, claim agent hooks work
without observing them, or weaken any review/approval requirement.
