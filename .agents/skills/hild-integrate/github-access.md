# GitHub access: diagnose the next blocked action

**Read this when** a GitHub step or the local checkout fails for lack of
access during integration or onboarding, or when the researcher asks for a
readiness check. It is shared by [`hild-integrate`](SKILL.md),
[`hild-scope`](../hild-scope/SKILL.md) and the
[onboarding companion](../hild-scope/onboarding-scope.md). Credentials and
consequential actions such as logging in follow the
[process, §7](../../../HILD/process.md#7-rules-at-every-step).

Aim for the smallest remedy that unblocks the researcher's next approved
step, not a full audit of the environment.

## Steps

1. **Name the blocked capability:** reading or editing files in the working
   repository; creating or commenting on issues or pull requests; branching,
   committing or pushing; or reading or updating the wiki, if that is agreed
   work.
2. **Identify how this agent reaches GitHub,** from the evidence or one
   targeted question. For example: a local editor or terminal, possibly over
   SSH; a hosted agent or Codespace with its own shell; a connected GitHub
   tool with no local checkout; or the researcher doing some steps on the
   GitHub website. These are examples, not a ranking. A signed-in browser, a
   connector, the researcher's terminal, the agent's own environment and
   Git's push credentials can all differ: test the capability the next step
   needs, and don't conclude from one result that all access works or fails.
3. **Diagnose through that route.**
   - **A connected tool without a shell:** check what it can read and, if
     shown, its permissions, and use its GitHub actions. Don't demand a
     clone or `gh auth login` if the tool is enough. API access does not
     mean a local script can run; if the step needs one, discuss a suitable
     environment or a step the researcher does on GitHub.
   - **A terminal and a checkout:** find the real working directory rather
     than assuming there is no checkout:

     ```sh
     pwd
     git rev-parse --show-toplevel
     git status --short
     git remote
     ```

     Confirm that the Git root and remote are the intended target, not
     upstream HILD or another project. If `git rev-parse` fails, find the
     workspace or ask where it is. Show a remote URL only when needed, with
     any embedded credentials redacted.
   - **If GitHub CLI (`gh`) is relevant,** check it before suggesting a
     login:

     ```sh
     gh auth status
     gh api repos/OWNER/REPO --jq '{full_name, permissions}'
     ```

     A successful read shows read access only, not permission to create
     issues, open PRs or push. Don't create dummy issues or commits to test
     write access; use the real operation after its approval gate.
   - **If results disagree** between tools, terminals and the agent's own
     processes, compare the environments before changing authentication.
     `gh` uses `GH_TOKEN` and `GITHUB_TOKEN` ahead of stored credentials,
     and they can differ between terminals, containers, SSH hosts and agent
     processes. Check whether they are set, never their values:

     ```sh
     for n in GH_TOKEN GITHUB_TOKEN; do
       if test -n "$(printenv "$n")"; then printf '%s is set\n' "$n"
       else printf '%s is unset\n' "$n"; fi
     done
     ```
4. **Recommend one recovery,** with alternatives only when their tradeoffs
   matter:
   - **Wrong directory or no checkout:** find the existing workspace, or make
     a clone after agreement, preserving uncommitted work.
   - **Missing issue or PR permission:** check the signed-in identity, the
     target, the credential's scopes and any organization policy. Use a
     connected tool that already has the rights, or offer a step the
     researcher does on GitHub. Explain any permission change before asking
     for it.
   - **No usable `gh` login:** explain the login options for this
     environment. The researcher can start a browser login with
     `gh auth login --hostname github.com --git-protocol https --web`. If an
     inherited token blocks it, then with consent omit the variables for
     that one command:
     `env -u GH_TOKEN -u GITHUB_TOKEN gh auth login --hostname github.com --git-protocol https --web`.
     Afterwards confirm `gh auth status` in the agent's own environment.
   - **`gh` works but `git push` fails:** check whether the remote uses SSH or
     HTTPS and which credentials apply. With agreement, `gh auth setup-git`
     makes `gh` Git's HTTPS credential helper; it changes Git configuration.
     Diagnose SSH separately rather than switching protocols blindly.
   - **No wiki access:** find out whether the wiki is initialized and whether
     the tool can write to it. A wiki is a separately authorized step, not a
     prerequisite for assessment or installation. If it can't be edited, hand
     over a manual step or propose a later scope; never claim it was updated.
5. **Verify the capability that was blocked,** say what is still unverified,
   and return to the HILD step that was blocked, at its approval gate.
   Repairing access approves nothing: not a scope, an installation or a
   merge.

## Environment notes, when relevant

- **Codespaces:** the checkout is usually under `/workspaces/REPO`. A
  repository-scoped token in the researcher's shell may not reach the
  agent's environment; check both when they disagree.
- **Hosted agents and connectors:** look for their GitHub actions and
  permissions before proposing CLI configuration. They may manage issues and
  PRs with no shell.

These are starting points, not claims of support for every product version.
Use the documentation of the agent, editor or host that actually applies:

- [GitHub CLI environment variables](https://cli.github.com/manual/gh_help_environment)
- [GitHub CLI login](https://cli.github.com/manual/gh_auth_login)
- [GitHub CLI Git credential helper](https://cli.github.com/manual/gh_auth_setup-git)
- [GitHub: Codespaces repository authentication](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-authentication-to-a-repository)
