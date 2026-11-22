# Onboarding: introduce HILD and develop a first scope

**Read this when** a researcher is new to HILD, asks for guidance getting
started, or wants an onboarding scope, whether or not HILD is installed. The
[scope steps](SKILL.md) and [HILD process](../../../HILD/process.md) still apply.

## 1. First contact

Explain HILD in terms of the researcher's project, purpose before setup:

- HILD helps them develop scientific software with an AI agent while
  keeping control of what gets built and understanding how it works.
- In practice, in their Git repository: a **scope issue** agrees each piece
  of work, a **pull request** shows each change for their review, a plan
  and journal keep the state between sessions, and an optional wiki records
  what they understand. HILD is not a service that runs on its own. Describe
  these as the way HILD currently works, not as what defines it
  ([process, *What HILD requires*](../../../HILD/process.md#what-hild-requires-and-how-we-implement-it)).

Ask what they want to build only if you don't already know. For a nearly
empty repository, installing HILD can be the first piece of work; for an
established one, say how HILD works with what is already there. Invite them
to develop a first scope together; offer detail later, when it helps.

An example to adapt, not to recite:

> HILD helps you develop scientific software with an AI agent while
> keeping control of what gets built and understanding how it works.
> We'll agree on small pieces of work, review changes, and preserve
> important decisions and explanations so the project stays understandable.
>
> Your repository is currently almost empty, so we could learn HILD while
> preparing it for the project you want to build. Would you like us to
> develop our first scope together?

**Access.** Say once, early, that HILD works best when the agent can change
the repository and create GitHub issues and pull requests (a wiki may need
more later). Offer to check now or when a step needs it; it is not a
prerequisite, and the researcher can do some steps in GitHub themselves. If
a check is wanted or a step fails, use the [GitHub-access companion](../hild-integrate/github-access.md).

## 2. After the researcher agrees to develop a scope

Start from the goal ([scope steps](SKILL.md), step 2). An example to adapt,
for a researcher who wants to learn HILD by installing it:

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

## 3. Choices to raise when they become relevant

Recommend the default and say why it suits this project. Defaults may simply
be accepted; record a choice only when its reason will matter later.

- **Where knowledge lives:** the default `HILD/` files, or the host's
  existing authoritative files where they already exist.
- **What supports understanding:** whether the default PR explanation and
  journal formats suit this work.
- **Which agents to support:** the AI coding agents the researcher uses;
  HILD keeps one set of skills for all of them.
- **Understanding map:** whether to start a fresh wiki. An existing wiki is
  preserved; integrating with it needs its own scope.

## 4. Choosing the first task

Check whether HILD is installed first:

- **Not installed:** suggest installing HILD as the first scope, if that
  serves the researcher's goal.
- **Installed and verified current:** ask what they want to do next, unless
  they have said. Offer one or two suggestions grounded in the repository
  and develop a small real task together.
- **Installed but older, locally changed, or of unknown origin:** help the
  researcher understand that state and decide whether to deal with it now,
  using [`hild-integrate`](../hild-integrate/SKILL.md)'s read-only
  comparison. Never assume an automatic upgrade.

Choose the task with the researcher, and introduce issues, PRs, review and
the journal as the work reaches them, not all up front.

## 5. Closing an onboarding scope

- Propose a `Process-HILD` wiki page explaining HILD in this repository,
  with links to its authoritative files, in the PR's *Wiki pages* section.
- Record which capabilities worked, were blocked or were not tested; files
  being present does not show an agent uses them. Suggest a later fresh
  session recover the state from the plan and journal.
