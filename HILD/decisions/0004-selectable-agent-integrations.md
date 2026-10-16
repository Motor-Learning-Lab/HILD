# 0004 — One HILD core with selectable agent integrations

**Date:** 2026-10-16 · **Status:** Proposed (substance approved in [scope #4](https://github.com/Motor-Learning-Lab/HILD/issues/4); awaiting review of [PR #7](https://github.com/Motor-Learning-Lab/HILD/pull/7))

**Context:** Researchers may use Claude Code, Codex, GitHub Copilot or several of them. Copying process skills separately for each agent creates conflicting sources of truth. Conversely, installing every platform's hooks and settings into a single-agent project introduces unnecessary files and potentially unexpected startup behavior.

**Decision:** Every HILD installation has **one shared canonical process and set of skills**. At first installation, the researcher chooses supported agent integrations, defaulting to **all supported agents**. Install only the selected platform-specific configuration/hook files; where possible they refer to the shared skill directory rather than copying it. Record the selection and exact upstream source revision in the local installation metadata. Later updates should preserve that selection unless the researcher explicitly changes it.

**Why:** A shared implementation prevents drift, while selection keeps a particular project's repository comprehensible. HILD's process stays usable even if a platform lacks working lifecycle hooks; the agent can invoke the appropriate skill explicitly.

**Limits:** Selection is **not** a permissions boundary: another agent may still read common files. Configuration and discovery are separate from demonstrated agent behavior. Native skill loading, hook execution and delivery of orientation must be verified separately on each supported platform. The first installer addresses **new, minimally initialized** repositories; integration with an existing wiki or upgrades of locally modified installations remain separate scopes.

**Consequences:** The installer requires a persistent, small selection record and must avoid overwriting existing agent configuration. Source copies of the skills must have one authoritative home. Support documentation should distinguish installed, configured, tested and unsupported behavior without inventing cross-agent parity.

**Origin:** [Scope #4](https://github.com/Motor-Learning-Lab/HILD/issues/4) and the [agent-selection review comment](https://github.com/Motor-Learning-Lab/HILD/issues/4#issuecomment-6188541675).
