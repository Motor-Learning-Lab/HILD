# 0003 — Onboarding is an optional first HILD scope, not a separate skill

**Date:** 2026-10-15 · **Status:** Proposed (substance agreed in [scope #4](https://github.com/Motor-Learning-Lab/HILD/issues/4); pending PR review)

**Context:** A copied HILD directory is not evidence that agents discover or follow its rules. New adopters also need a useful first experience. A separate onboarding skill or mandatory onboarding on every update would introduce unnecessary machinery and repetition.

**Decision:** The root and installed HILD READMEs invite the user to open a chat with repository access and invoke `hild-scope`. Their suggested first request is **onboarding**, but experienced users may substitute any other development goal. `hild-scope/SKILL.md` refers to a companion `onboarding-scope.md`, loaded **only** for an onboarding request. Onboarding is a normal, reviewed development scope using an issue, early draft PR, real plan/journal updates, and any *genuine* decisions that arise. It may propose a `Process-HILD` understanding-map wiki page that is drafted after merge and confirmed by the human.

**Verification distinction:** Every installation/update receives mechanical installation-integrity checks; those checks do not demonstrate behavioral compliance. The interactive onboarding cycle is **recommended but optional** for users. It is part of HILD's *first* complete installer acceptance test and is repeated selectively for major changes to the process or agent machinery, **not for every HILD update**. Evidence must distinguish passed, failed, pending, inapplicable and untested capabilities.

**Why:** The learner experiences the real process while creating useful, durable project artifacts. There is a single scoping entry point, not competing procedures; validation investment follows changes that actually warrant it.

**Consequences:** The scoping skill needs only one optional companion file. Onboarding validation cannot be claimed before the real human-agent cycle and post-merge orientation finish. A wiki page cannot be recorded as complete just because it was proposed in the PR.

**Origin:** Design and acceptance discussion captured in [HILD issue #4](https://github.com/Motor-Learning-Lab/HILD/issues/4).
