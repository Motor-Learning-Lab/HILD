# Writing skills — HILD process topic

Part of the [HILD process](../process.md), which every session reads first. Read this file before writing or changing a skill.


A skill holds a **procedure**: what the agent does, in order, and where it
stops. Rules live in the [HILD process](../process.md) and its topic files,
and formats in the templates (*Where each thing lives*). When writing or changing a skill, check it against this list;
`hild-digest` checks the same list. The research behind it is summarized in
the understanding map's skill-authoring resource page, where one is kept.

1. **Front matter:** only `name` and `description`, so one file works for
   every agent; `name` equals the skill's directory name.
2. **Description:** third person, saying what the skill does, then
   "Use when…" with the requests that should select it. Key words first;
   under 1,024 characters. It does not claim a request that another
   skill's description also claims.
3. **Procedure, not rules:** numbered steps and exact stopping points. Where a
   step depends on a rule, link to the rule's section in the process or its
   topic file instead of restating it.
4. **No rule lives only in a skill.** If a skill needs a rule that has no
   home, add the rule to its home (on the read track) and link to it.
5. **Only what the agent would otherwise get wrong.** Leave out background
   the agent already knows. Explanation of why HILD works this way belongs
   in the understanding map; keep a short reason only where a step would
   otherwise look arbitrary.
6. **Size:** keep `SKILL.md` well under 500 lines. Put longer material in
   companion files linked directly from `SKILL.md` (one hop, not chains),
   each with a stated "read this when". A companion over 100 lines starts
   with a table of contents.
7. **Links resolve** in an installed repository. `install_hild.py --verify`
   checks that local links reach existing files; it does not check section
   anchors.
8. **Tested when the procedure changes:** a fresh agent session shows the
   skill is found and followed. Say what was not tested.
