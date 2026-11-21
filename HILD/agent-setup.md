# Agent startup integrations

**This page describes the agent-specific mechanics of HILD's reference
implementation, not the requirements that define HILD.** Agent instructions
and hooks help agents follow the human-supervised process; they are not
required to define or understand it. The installer keeps one copy of HILD's
rules and skills and offers platform-specific adapters according to the
researcher's agent selection (default: all supported agents).

This page explains **what the adapter templates can do**. The
[preview-first installer](scripts/install_hild.py) supports new, minimally
initialized Git repositories and selects agent-specific adapters; reconciling
an existing HILD installation or established repository is not yet supported.
Neither installed files nor a valid configuration proves that a real agent
has discovered or used the skills.

| Agent | Shared skills | Optional startup file | Current evidence |
|---|---|---|---|
| Codex | `.agents/skills/hild-*/SKILL.md` | `.codex/hooks.json` from [template](templates/codex-hooks.json) | Supported locations documented; not tested in a live Codex session |
| GitHub Copilot CLI/cloud | `.agents/skills/hild-*/SKILL.md` | `.github/hooks/hild.json` from [template](templates/copilot-hooks.json) | Supported locations documented; not tested in a live Copilot session |
| Claude Code | `.agents/skills/hild-*/SKILL.md`, found through the skills index in `AGENTS.md`, which `CLAUDE.md` imports with `@AGENTS.md` | `.claude/settings.json` from [template](templates/claude-settings.json) | Tested in [scope #19](https://github.com/Motor-Learning-Lab/HILD/issues/19#issuecomment-6748912826): with the import and index, Claude chose and followed the right skill and stopped before acting; headless runs, not yet a full onboarding |

Claude Code does not read `.agents/skills/`, and `CLAUDE.md` loads other files
only through `@path` imports, so the installer writes `CLAUDE.md` containing
`@AGENTS.md` and puts a skills index in `AGENTS.md`: each skill's name, path
and description, built from the skill's frontmatter. The installer creates no
`.claude/skills` link, so nothing depends on the user's OS or Git symlink
settings. The consequence is that Claude Code treats the skills as
instructions it is pointed to rather than as native slash-command skills; see
[decision 0009](decisions/0009-claude-skills-via-agents-md.md), which is
proposed and not yet accepted.

## What the startup scripts do

[The startup collector](scripts/session_context.sh) prints Git status, the
current plan, recent journal entries, issues and PRs, and information about a
local wiki clone when present. The [orientation skill](../.agents/skills/hild-orient/SKILL.md)
tells the agent how to present this information to the researcher.

- **Codex:** Project hooks use `.codex/hooks.json` in a *trusted* project.
  Codex may require the human to explicitly trust hooks. Copying a valid JSON
  file is not sufficient evidence that it ran. The hook invokes the shell
  collector from the Git root.
- **Claude Code:** Project hooks live in `.claude/settings.json` and can
  supply startup context and reminders during conversation compaction.
  The provided template must be **merged carefully** with existing settings,
  never overwrite them.
- **Copilot:** Repository hooks use `.github/hooks/*.json`; a
  `sessionStart` command can run the collector. GitHub's documentation says
  that hook stdout may be ignored by the Copilot CLI, so running this hook
  **does not guarantee** that the agent receives an orientation. Use the
  `hild-orient` skill or startup prompt as the reliable fallback.
  The template is for Unix shells; native Windows operation is untested.

If an agent has no working hook, open a chat with repository access and
explicitly request `hild-orient`. **No HILD procedure requires a hook to
function**; the hook only reduces the work of gathering facts.

## How to verify an installation

1. Check the selected platform configuration exists, parses, and points to
   the intended shared skills/scripts; unselected configurations should not
   be installed by HILD.
2. In a fresh session with the selected agent, ask it to identify HILD,
   load `hild-scope` and `hild-orient`, and report what actually ran.
3. Observe whether an actual startup hook fired and whether the agent used
   its information. Record separately: **installed**, **discovered**,
   **executed**, and **used by the agent**.
4. Report skipped or unsupported behavior honestly. Do not count source
   documentation or mechanically valid JSON as a successful agent session.

## References

- [Claude Code skills](https://code.claude.com/docs/en/skills) and
  [hooks](https://code.claude.com/docs/en/hooks)
- [GitHub Copilot skills](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills)
  and [hooks](https://docs.github.com/en/copilot/concepts/agents/hooks)
- [Codex repository-local skills](https://developers.openai.com/blog/skills-agents-sdk)
  and [project hooks](https://developers.openai.com/docs/hooks)

Later installation work must preserve existing settings and explicitly report
which compatibility tests were actually performed.
