---
name: hild-digest
description: Audit repo understandability, stale material, duplicated rules, neglected decisions and understanding-map freshness, and propose a bounded cleanup. Use for periodic repo reviews and requests to inspect hygiene.
---

# Digest

The aim is a project the human reviewer can hold in their head. Authoritative criteria come from the host's established `AGENTS.md` and [HILD process](../../../HILD/process.md). **Do not duplicate a separate hygiene rulebook in this skill.**

1. **Understanding map:** when configured, pull fast-forward and check code pages for staleness using `HILD/scripts/wiki_status.py` if installed; record missing pages and open understanding-debt issues. Create/update issues and wiki status only as authorized by the project's agreed scope. Report missing tooling rather than pretending this check ran.
2. **Repository inventory:** inspect tracked files (`git ls-files`), current plan, decisions, code, relevant wiki pages, PRs and tests. Look for stale or unreferenced material, duplicative authority, unclear names, missing evidence, inconsistent claims and unreviewed changes, using actual project rules.
3. **Report first:** briefly assess whether the repo has become easier or harder to understand. Give a prioritized table of finding, location, governing rule and proposed action; identify what could be deleted or simplified.
4. **Follow up by agreement:** do not repair nontrivial issues merely because they were identified. Each approved fix gets a scope issue or joins an existing agreed scope. Record the audit milestone using `hild-journal`.

The original [digest procedure](https://github.com/opherdonchin/MotorAdpatationSBI/blob/main/.github/skills/digest/SKILL.md) and this HILD adaptation describe the same review process; the process file, not this skill, remains the rule authority.
