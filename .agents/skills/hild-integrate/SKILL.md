---
name: hild-integrate
description: Assess whether and how to adopt or update HILD in a scientific software repository. The first pass is read-only; inventory existing authority, identify conflicts and propose a reviewed scope. Use when asked to install, integrate, upgrade, reconcile or audit HILD.
---

# HILD integration — assessment first

Authoritative rules: [HILD process](../../../HILD/process.md) in this repository. If this file is read **via an upstream URL before installation**, the agent must also read that upstream process; relative links may not resolve in the target repository.

## Contract

**Your first action is assessment, never installation.** State that you are assessing only. Do **not** change files, branches, issues, PRs, settings, hooks or remote refs; do not commit, fetch, pull, run scripts, or generate files. Reads such as `git status`, `git log`, `git ls-files`, `git show` and GitHub GET operations are allowed. Do not open suspected secrets or execute untrusted tools. If access is incomplete, report the limitation; never treat missing evidence as proof of absence.

## Assessment steps

1. **Identify and protect the target.** Confirm target repository and intended upstream HILD source, current branch, working-tree state and access level. Preserve any uncommitted or unpushed work. Read the upstream process and the target's entry-point instructions before interpreting its files.
2. **Inventory existing authority.** Locate process rules, `AGENTS.md`/agent instructions, skills and hooks, decisions, plans, journals, wiki/understanding map, tests, repository conventions and relevant development history. Identify the canonical home of each; distinguish established conventions from copies or stale descriptions. Use only read operations.
3. **Classify the HILD state.** (a) no identifiable HILD installation; (b) existing installation with reliable upstream provenance; (c) installation with missing/uncertain provenance; or (d) partial/mixed adoption. A folder name alone is not enough to establish origin. Record source commit/version if verifiable.
4. **For an existing installation, compare without changing.** If possible, identify **B** = recorded upstream baseline, **L** = current local files and **N** = proposed upstream. Explain local modifications (`B→L`) and upstream changes (`B→N`) and any conflicts. If B is unavailable, say so; do not infer or replace locally evolved content.
5. **Propose, then stop.** Report authoritative paths to retain, optional HILD additions, collisions/risks, incremental compliance work and a small proposed scope. Label observations versus recommendations. Ask the researcher to approve or change the proposal; **do not create the scope issue or implement it yet**.

## Required assessment report

- **Target, source and read-only status:** repository, branch, changes present, upstream HILD URL/version; what could not be inspected.
- **Existing working process:** concise description with paths or links, including project-specific rules and understanding records.
- **Classification and authority map:** which file or system controls each responsibility; flag duplication and unknowns.
- **Proposed changes, conflicts and deferrals:** distinguish safe additions from locally edited or established material. Never silently relocate or overwrite documentation.
- **Next agreement:** smallest bounded scope, risks, checks and explicit decisions for the human; **stop without mutation**.

## Not implemented here

This skill contains **no installer**, no automated migration, no upgrade merge engine, no compliance enforcement and no cross-agent hooks. After the human accepts an integration scope, a separately implemented and approved procedure will perform changes through the HILD branch/PR review cycle. Do not treat an approved *assessment* as authority to install or update.
