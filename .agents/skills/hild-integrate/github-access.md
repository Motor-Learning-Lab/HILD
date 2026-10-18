# GitHub access: diagnose the next blocked action together

**Load this companion only when the researcher needs to establish or repair
GitHub access** during HILD adoption or onboarding. It supports
[hild-integrate](SKILL.md) and
[the onboarding companion](../hild-scope/onboarding-scope.md);
the [HILD process](../../../HILD/process.md) still governs approval and
autonomy. This is a troubleshooting guide, not permission to perform
unapproved GitHub writes.

## Begin with the actual obstacle

Briefly tell the researcher **what action is blocked and why it matters**
(e.g., "We have agreed on an installation scope, but I can't create its
GitHub issue yet"). Ask one useful question only when needed: which
environment or command is failing? Prefer checking accessible evidence
over asking the researcher to perform unnecessary steps.

Different capabilities need different checks:

- **Read the repository:** Can the agent see the target's committed files?
- **Access its working tree:** Is there a local Git checkout that the agent's
  terminal can actually reach? A GitHub-connected chat is not a checkout.
- **Create issues/PRs:** Can the chosen GitHub tool act on the target repo?
- **Push code:** Can local Git authenticate and write to the target remote?
- **Run the installer:** Can the agent access **both** a clean source HILD
  checkout and a clean target checkout on the appropriate branch?

An authenticated web browser, a valid GitHub CLI login, an agent's own
terminal environment and an authorized Git credential helper are **not
necessarily the same identity or capability**. Verify the specific action
rather than declaring the entire GitHub connection broken.

## First diagnostics (read-only)

Run these from the agent's **own terminal environment**, ideally in the
workspace associated with the target repository:

```sh
pwd
git rev-parse --show-toplevel
git status --short
gh auth status
```

If `git rev-parse` fails, inspect the actual workspace directories or
working-directory setting **before** concluding that no checkout exists.
In a Codespace, the project commonly lives under `/workspaces/REPO`, but
use the actual path. Confirm that the resolved Git root is the **target**,
not an unrelated checkout or a temporary download directory.

If `gh` is available and the target is `OWNER/REPO`, the following
GitHub **read** checks can help:

```sh
gh api repos/OWNER/REPO --jq '{full_name, permissions}'
gh api repos/OWNER/REPO/issues --jq 'length'
```

`OWNER/REPO` is a placeholder; substitute the confirmed target.
A GET request proves some read access; it does **not** prove that creating
issues, PRs or pushes is authorized. Only perform the **actual intended
write** after HILD's relevant approval gate, not a dummy issue or test
commit created to probe permissions.

To understand why `gh` behaves differently across environments, inspect
**presence, not values**, of its environment credentials:

```sh
for n in GH_TOKEN GITHUB_TOKEN; do
  if test -n "$(printenv "$n")"; then
    printf '%s is set\n' "$n"
  else
    printf '%s is unset\n' "$n"
  fi
done
```

Compare results from the **agent's tool terminal** with the researcher's
interactive terminal if they disagree. In particular, the environment
variables `GH_TOKEN` and `GITHUB_TOKEN` take precedence over credentials
stored by GitHub CLI (in that order). A command working in the user's
terminal may fail when run by an agent whose subprocess inherits a
different environment.

## Choose the least disruptive remedy

**Existing Codespace for the target repository.** GitHub normally supplies
credentials scoped to the Codespace's source repository; they may not
authorize access to another repository. First locate the real checkout
and check `gh auth status` **in the agent's environment**. If GitHub CLI
access is blocked but a connected GitHub integration can perform the
approved operation, use that integration instead of changing the user's
credentials. Report which method is verified.

**A token environment variable prevents interactive `gh auth login`.**
Explain that the CLI already sees an environment token but this need not
be the credential the agent's own terminal sees. If an interactive login
is genuinely needed and the researcher agrees to change authentication
setup, temporarily omit the token **for that one command**, leaving
the original environment intact:

```sh
env -u GH_TOKEN -u GITHUB_TOKEN gh auth login --hostname github.com --git-protocol https --web
```

The browser/device authorization is the researcher's action. Confirm it
worked using `gh auth status` in the environment that will run `gh`.
Authentication can store credentials or modify user-level configuration:
explain that side effect before asking the researcher to approve it.
Avoid broad, permanent changes to environment variables just to make
one command work.

**GitHub API works but `git push` fails.** This may be a **separate Git
credential or remote-protocol issue**, not a failed login. Check the
target remote and whether it uses HTTPS or SSH, without printing embedded
credentials. If GitHub CLI is authenticated and the researcher agrees to
configure Git's credential helper, `gh auth setup-git` is a documented
option for HTTPS. It changes Git configuration, so first explain the
scope of that change; in a Codespace, changing the default helper can
affect other repositories. Diagnose SSH errors separately rather than
blindly switching protocols.

**Permission still denied.** Check that the authenticated account is
authorized for the **correct** repo and the requested operation (issues,
pull requests, branch writes). Repository permissions, token permissions
and org policy may differ. Offer a relevant manual GitHub UI route or
a different already-authorized tool if available. Do not bypass branch
protections or broaden token permissions without a clear need and the
researcher's approval.

## Keep the researcher in control

- Explain **one next diagnostic or repair** and its expected outcome; offer
  alternatives when a meaningful tradeoff exists.
- Never ask the researcher to paste access tokens, private SSH keys,
  device codes or other credentials into chat, issues, PRs or logs.
- Avoid commands that print tokens (such as `gh auth token`), embed
  credentials in a remote URL, or publish credentials in Git history.
- Installing credentials, editing Git configuration and creating GitHub
  resources are distinct side effects; obtain agreement for each.
- When a problem is resolved, verify the **specific blocked capability**,
  record what was tested and what remains unknown, and return to the
  original HILD stopping point. Access repair does **not** waive review
  of the proposed scope issue or approval of installation.

## Current sources

Prefer the provider's maintained documentation over assuming an older
authentication recipe always applies:

- [GitHub: Troubleshooting repository authentication in Codespaces](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-authentication-to-a-repository)
- [GitHub CLI: environment variables and token precedence](https://cli.github.com/manual/gh_help_environment)
- [GitHub CLI: login](https://cli.github.com/manual/gh_auth_login)
- [GitHub CLI: configure Git credential helper](https://cli.github.com/manual/gh_auth_setup-git)

The exact availability of Copilot/Codex/Claude terminals and permissions
must be verified in the running environment; a documented fix is not proof
it worked in this session.
