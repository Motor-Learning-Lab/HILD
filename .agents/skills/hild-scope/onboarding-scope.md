# Suggested first scope — HILD onboarding

This is a **companion to [hild-scope](SKILL.md)**, read **only** when the researcher asks to scope onboarding. It is not a separate skill and is not an automatic installation step.

## Goal

Guide a new researcher through a **real HILD development cycle** while collecting evidence about the installed capabilities. The exercise should initialize useful project history, not add disposable demonstration code. Adapt it to the project's actual needs and installed features; propose a GitHub scope issue for human agreement.

## Suggested activities and evidence

1. **Orient.** In a fresh agent session, identify the HILD process, plan, skills and current project state. Record whether the agent discovered instructions automatically or was given explicit links.
2. **Agree on a scope.** Draft and discuss a normal scope issue for onboarding, including permitted GitHub/wiki side effects, stopping points and acceptance checks. Wait for human agreement before implementation.
3. **Demonstrate the Git workflow.** Create a branch, push a small legitimate initialization improvement, and open a draft PR early. Use small, linked commits; do not rewrite the branch.
4. **Record knowledge honestly.** Update the plan and journal at milestones. If a genuine, consequential choice arises (e.g. an authoritative location), draft a decision record in the PR; **do not invent a decision merely to exercise a template**.
5. **Propose the understanding page.** In the PR's *Wiki pages* section, propose `Process-HILD`: what HILD means for *this* repository, where authoritative rules/state live, which agent integrations are configured, and which capabilities remain unverified. Do not pre-create a code page that needs the eventual `main` commit.
6. **Explain and review.** Use `hild-explain` for a layered PR description with actual evidence, missing tests and an approval track. Respond to the researcher's questions and changes. **The researcher approves and merges**; the agent does not certify understanding or approval.
7. **After merge.** Check that squash was used and the expected commit/history exists. Draft the *agreed* `Process-HILD` wiki page **after merge**, and invite researcher review. Start a new agent session to test whether orientation and state recovery work from durable records.
8. **Report coverage.** For each capability (skill discovery, scope, PR, decision if used, journal/plan, approval, merge, wiki, fresh orientation), report `pass`, `fail`, `pending`, `not applicable` or `not tested`, with an evidence link and reason. Report both positive behavior and explicit stopping at boundaries.

## Limits

- **Onboarding validation differs from mechanical installation verification.** Both outcomes should be recorded, but a file's existence alone is never proof that an agent followed the process.
- Onboarding is **recommended**, not mandatory for every installation or update. HILD's own first installer should undergo this complete exercise. Repeat it selectively after major changes, not after every update.
- A pre-existing wiki must not be integrated or reconciled as part of first-install onboarding. If a fresh wiki cannot be created, record the blocker and do not claim wiki validation passed.
- Do not expand the human's agreed scope, provision external resources, or take destructive action without explicit permission.

The actual scope issue must use the [canonical scope-issue template](../../../HILD/templates/scope-issue.md), not copy the instructions above as a separate competing process policy.
