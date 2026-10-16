# Onboarding: suggested first scope

Read this file only when the researcher asks to **scope onboarding**. It helps
`hild-scope` prepare an ordinary scope issue; it is **not another set of
development rules**. Follow the [HILD process](../../../HILD/process.md) for
issues, branches, PRs, explanations, approval and journals.

## What onboarding is for

Help someone try HILD on their own project, through one **small, useful
change**. At the same time, gather evidence of which installed capabilities
actually work. Do not create throwaway code or invent a decision just to
complete a checklist.

## Choices to bring up while preparing the scope

Ask about these as appropriate. Explain the default first; the researcher may
keep it without creating a formal decision record.

- **Where project knowledge lives:** Does the default `HILD/` location work
  for the plan, journal and decisions? Is any existing file authoritative?
  Avoid a second copy of the same information.
- **How explanations are written:** Does the proposed PR explanation format
  fit this project's work? For example, mathematical details are useful for
  some scientific changes but irrelevant to documentation-only changes.
- **How work is recorded:** Is the default journal format practical? What
  information is important for understanding or reproducing this project?
- **Agent setup and understanding map:** Which agents are selected for this
  installation? Is a new wiki available, and who will review its pages?

These are **topics to surface, not required customization**. Record a
meaningful choice in a decision record when it constrains future work.
Anything needing deeper discussion can become a **future scope or issue**;
onboarding need not settle every convention.

## What to propose in the onboarding scope

1. **A real first deliverable.** Prefer a small improvement to the project's
   README or initial plan: explain what the project is trying to do, where
   HILD's rules live, and the first meaningful next step. Agree on the actual
   change with the researcher.
2. **Evidence of the HILD workflow.** The proposed scope should say which
   capabilities the human and agent intend to exercise: new-session
   orientation, scope agreement, an early draft PR, explanations and approval,
   journal/plan updates, and a squash merge. Follow the ordinary process for
   **how** to perform them; don't restate it in the issue.
3. **A proposed understanding page.** Ask whether the PR should propose a
   new wiki page called `Process-HILD` (a **process page**, not a code page).
   It would explain in plain language how this particular repository uses
   HILD, with links to its authoritative files and any limitations. If the
   reviewer agrees, the agent drafts it **after the PR merges**. The reviewer
   then reads it and alone may mark it `understood`.
4. **Evidence and limits.** Record which capabilities passed, failed, were
   blocked, or were not tested, with links or observations. A fresh agent
   session after the merge should recover the project's state from its files.

## Boundaries

Onboarding is recommended, not mandatory. **Installation integrity** (files,
settings and references) is a separate check; it does not establish that the
agent behaves correctly. If a wiki or hook is unavailable, report the
limitation; do not claim a pass. Do not integrate an existing wiki as part of
the first-install onboarding scope.

The result of reading this file is a **proposal for human agreement**.
The normal HILD process governs everything after that agreement.
