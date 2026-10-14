# 0001 — Contained HILD layout, with authority-preserving overrides

**Date:** 2026-10-14 · **Status:** Proposed (substance agreed in chat; PR review pending)

**Context:** New projects benefit from a clear default home for HILD's own process and state. Existing scientific repositories already have authoritative instructions, plans, decisions and documentation; moving them into a new folder would create disruption or competing copies.

**Decision:** HILD defaults to a contained `HILD/` directory for its process, configuration, plan, journal, decision records and supporting machinery. An adopting repository may override individual locations, especially for existing authoritative files. Integration must discover which home is authoritative for each role and must not copy, move or overwrite established knowledge merely to fit the default. Agent-discoverable skills live where the agent expects them, pointing to the canonical process.

**Why:** A default reduces the cost of starting a new project. Per-role overrides let existing projects preserve their working practices and history without creating duplicate sources of truth. Alternatives rejected: forcing all projects to reorganize into `HILD/`; scattering all HILD machinery at the root by default.

**Consequences:** The integration procedure needs an explicit authority map, and future skills must resolve configured locations rather than hard-code `HILD/`. The syntax of configuration, agent-specific skill locations and optional root-level layout remain undecided; this record does **not** settle them.

**Origin:** [HILD scope #1](https://github.com/Motor-Learning-Lab/HILD/issues/1); the original [source-of-truth discussion in PR #7](https://github.com/opherdonchin/MotorAdpatationSBI/pull/7).
