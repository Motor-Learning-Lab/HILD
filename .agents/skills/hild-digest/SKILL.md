---
name: hild-digest
description: Audits how easy the repository is to understand and proposes a bounded cleanup, covering obsolete files, rules stated in more than one place, skills that break the skill-writing checklist, conflicting claims, untested or unreviewed work, and stale understanding-map pages. Use for a periodic repository review, or when the researcher asks for a hygiene check or audit.
---

# Digest: audit the repository

The criteria are the host's `AGENTS.md` and the [HILD process](../../../HILD/process.md)
with its topic files. This skill says how to look, not what is right: judge
each finding against the rule it links to.

## Steps

1. **Check the understanding map.** If one is configured, pull it with
   `--ff-only` and run `HILD/scripts/wiki_status.py` if it is installed.
   Note stale pages, pages linked but not written, and open
   understanding-debt issues. If the tooling is missing, say the check did
   not run.
2. **Review the repository.** Read the tracked files (`git ls-files`), the
   plan, decisions, code, tests, relevant wiki pages and open PRs. Look for:
   - obsolete, unused or confusingly named files, and missing test evidence;
   - a rule stated in more than one place, or outside its home
     ([§8](../../../HILD/process.md#8-the-map));
   - text that treats a GitHub, skill or hook mechanism as the process
     itself, or an untested alternative as working
     ([§1](../../../HILD/process.md#1-what-hild-is-for));
   - provisional work from independent work reported as accepted
     ([*Independent work*](../../../HILD/process.md#independent-work));
   - an older decision changed by a later one without a notice at its top
     ([decision-records topic](../../../HILD/process/decision-records.md));
   - claims that conflict, and changes still awaiting review.

   Keep concrete conventions; do not propose replacing them with vague goals.
3. **Check the skills** against [the writing-skills topic](../../../HILD/process/writing-skills.md):
   each skill's size, any rule it restates or holds without another home,
   and descriptions that claim the same requests.
4. **Report, before changing anything.** Say whether the repository is
   getting easier or harder to understand. For each important problem give
   its location, the rule it breaks and a specific fix, and name what could
   be simplified or removed.
5. **Fix only by agreement.** Each fix the researcher approves gets a scope
   issue or joins an agreed scope. Record the audit as a milestone with
   [`hild-journal`](../hild-journal/SKILL.md).
