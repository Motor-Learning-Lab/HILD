# Onboarding: a first scope that helps the researcher learn by doing

Read this file **only** when the researcher wants to scope HILD
onboarding. It supplements [hild-scope](SKILL.md); it is not a separate
skill or a second set of process rules.

## Help the person see the point

The researcher is learning **how to work with HILD on their own
project**, not studying HILD's implementation. Ask what they want the
project to become and what would make the first HILD experience useful.
Use what they have already told you.

A repository that is nearly empty offers an opportunity to do two
useful things together: establish how the project will develop and
experience HILD's normal method for agreeing on, reviewing and recording
work. Installing HILD may itself be the first scope if the researcher
has not installed it; otherwise choose a small, **real project task**.
Do not invent demonstration code or decisions to tick off capabilities.

## Surface the decisions that matter, when they matter

HILD offers defaults. Explain the reason for a default first and ask
whether it serves the researcher's needs. Bring up only consequential
choices, as they become relevant:

- Where should authoritative plans, process rules, decisions and
  journal entries live? Will the standard `HILD/` directory work, or
  would that duplicate an existing source?
- What kind of explanations and progress records will help this
  researcher understand the scientific code? Do the default PR and
  journal formats suffice for now?
- Which AI agents will actually be used? HILD supports a shared set of
  skills with selected platform-specific configuration.
- How will the researcher record understanding? Is there a **new** wiki
  to create later? Do not overwrite or reconcile an existing wiki.

Don't require a formal choice about every item. If the default works,
keep it. If deeper customization is worth doing, propose a **later
scope** rather than letting setup consume the entire conversation.
Record an important decision only when a genuine choice constrains
future work.

## Make the first scope useful and verifiable

Help the researcher pick one attainable outcome and describe what
would count as evidence of success. The normal HILD process supplies
the issue, early draft PR, explanations, review, approval and durable
journal; **don't teach all those steps in advance**. Introduce them
as the researcher encounters them.

An onboarding PR may propose a `Process-HILD` **wiki page**: an
accessible guide to how HILD works *in this repository*, linking to
the actual authoritative files rather than copying their rules.
With the reviewer's agreement, draft it **after that PR merges**.
Only the researcher can mark it `understood`.

Keep two separate judgments:
- **Installation integrity:** files, references and configurations
  checked mechanically.
- **Onboarding behavior:** whether the agent actually followed the
  agreement and review process and the human understood it.

Record concrete evidence for capabilities actually exercised, and
label others blocked, untested or not applicable. A fresh session
should try recovering project state from recorded work, rather than
this chat. Onboarding is recommended for newcomers; it is not a
mandatory repeat after every HILD update.

## If something blocks the next step

Investigate what tools and access exist and what is missing. Explain
the simplest feasible route, offer alternatives only when meaningful,
and help the researcher continue. A limitation such as a missing
local checkout matters when work requiring it is about to begin;
it should not displace the conversation about the project's goals.

Don't create a wiki without agreement, integrate a pre-existing wiki,
or report agent skill discovery as verified merely because files exist.
