# 0010 — One skill-writing checklist in the process; no skill-authoring skill

**Date:** 2026-11-22 · **Status:** Accepted on the researcher's merge of [PR #31](https://github.com/Motor-Learning-Lab/HILD/pull/31)

**Relationship to earlier decisions:** None. It makes concrete the existing rule that skills hold procedure and point to rules ([process, *Where each thing lives*](../process.md#where-each-thing-lives-and-how-to-change-it)).

**Context:** [Scope #18](https://github.com/Motor-Learning-Lab/HILD/issues/18) step 1 compared HILD's 11 skill files with published skill-authoring guidance ([research](https://github.com/Motor-Learning-Lab/HILD/wiki/Resource-skill-authoring-guidance), [audit](https://github.com/Motor-Learning-Lab/HILD/issues/18#issuecomment-7066427222)). The skills met every formal limit, but they restated about 67 rules from `process.md`. Three rules existed only in a skill or a template comment, and descriptions overlapped. The external sources also disagree on description voice: Anthropic asks for the third person, while agentskills.io prefers imperative "Use this skill when…".

**Decision:**
- **One checklist**, the section [*Writing skills*](../process.md#writing-skills) in `process.md`. Authors use it when writing or changing a skill, and `hild-digest` checks skills against it.
- **No skill-authoring skill.**
- **Descriptions are in the third person and include a "Use when…" clause.**
- **Rules a skill needs get a home outside the skill:** in `process.md`, or in a template if the rule is a format. The skill links to that home. The three skill-only rules moved accordingly:
  - credentials go to *Autonomy*;
  - `Closes` / `Part of` goes to *Git and GitHub*;
  - what an installation scope states goes to the scope template.

**Why:**
- **The checklist as a template** was considered. It was rejected because the list is mostly rules about skills, and the researcher asked for the most consistent arrangement: rules in `process.md`, formats in templates ([choice B](https://github.com/Motor-Learning-Lab/HILD/issues/18#issuecomment-7068649158)).
- **A skill-authoring skill** was rejected. Anthropic's guide says Claude needs no "writing skills" skill, and vendor `skill-creator` tools already exist. HILD's one addition, linking rather than restating, is something to check in review, not a way to create skills.
- **On description voice,** the researcher chose the third person plus "Use when…" ([choice A](https://github.com/Motor-Learning-Lab/HILD/issues/18#issuecomment-7068262993)). It follows Anthropic's explicit rule and keeps the trigger wording agentskills.io recommends. Neither voice has been tested against the other.

**Consequences:**
- The skill rewrites under scope #18 follow the checklist.
- Most current descriptions do not yet meet item 2. Changing a description also changes the generated skills index, and this repository's hand-written index in `AGENTS.md`.
- Host repositories receive the checklist with `process.md`, so it applies to skills they write.

**Validation:** scope #18 requires a live session after the rewrites, showing that Claude Code still finds `hild-scope` and follows it to a proposed scope issue. Until then, the checklist's effect on skill selection is **untested**.
