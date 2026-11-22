# Installing and adapting HILD — HILD process topic

Part of the [HILD process](../process.md), which every session reads first.
Read this file before assessing, installing, upgrading or reconciling HILD in
a repository, or agreeing a substitute for an unavailable mechanism. The
principle for an unavailable mechanism, and that paths are defaults, are in
the process, [§1](../process.md#1-what-hild-is-for).

## Substitutes for an unavailable mechanism

For example, another durable issue tracker could record a scope if the
researcher can inspect and approve the actual record and future sessions can
recover that approval. When compatibility issues arise, report specific
problems and demonstrated workarounds upstream for later review.

## Authority and local configuration

- **Default implementation:** process, plan, journal, decisions and templates live under `HILD/`.
  An established host may configure **each** authoritative location independently,
  preserving existing files; do not move or duplicate them merely to install HILD.
  Adopting HILD preserves a host's existing authority.
- **Project rules:** scientific aims, source layout, coding conventions and other
  project-specific rules live in the host's `AGENTS.md` or established equivalent.
  That document **points to** this process rather than copying it.
- **Installed HILD is local:** local modifications are legitimate. New upstream
  versions must be compared and reconciled, not installed over the local version.
- **Configuration format:** choice of configuration format is deferred.

## Assessment

An initial `hild-integrate` **assessment** never runs hooks or
write-capable scripts, and never changes local or GitHub state before human
approval.

## Automatic orientation

Orientation happens by default when a session opens (process,
[§5](../process.md#5-state-in-files)). A session-start hook achieves this
where the agent supports one; otherwise a standing instruction in the
host's agent instructions does. The hook is a convenience, not a
precondition.
