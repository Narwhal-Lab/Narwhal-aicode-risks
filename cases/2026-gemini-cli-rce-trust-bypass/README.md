# Gemini CLI Workspace-Trust and Tool-Allowlist RCE (2026)
> Gemini CLI 工作区信任与工具白名单绕过 RCE

| Field | Value |
|---|---|
| Category | Agent Risks |
| Severity | 🔴 Critical |
| AI Tool | Gemini CLI, run-gemini-cli |
| Language | TypeScript, GitHub Actions |
| Real Incident | ✅ |
| Reproducible | ❌ |
| Disclosed | 2026-04-24 |
| CVE | — |
| CVSS | 10.0 |

## TL;DR
Gemini CLI and the `run-gemini-cli` GitHub Action shipped unsafe defaults for headless CI usage: workspace folders were implicitly trusted, and `--yolo` mode ignored fine-grained tool allowlists. In workflows that processed untrusted pull requests or issues, malicious workspace files or prompt injection could lead to remote code execution.

## Background / 背景
Gemini CLI is an AI coding command-line tool, and `run-gemini-cli` packages it for GitHub Actions. These tools are attractive for issue triage, PR review, and automated coding workflows because they can read repository context and call shell-backed tools.

That same integration makes the trust boundary unusually sharp. A CI workflow may run the assistant on attacker-controlled repository contents, issue text, or pull-request diffs while holding repository tokens, model credentials, or workflow permissions.

## What Went Wrong / 问题剖析
The reviewed GitHub Advisory describes two related failures.

First, Gemini CLI in headless mode automatically trusted the checked-out workspace and processed local `.gemini/` configuration, including environment files. In untrusted CI contexts, malicious repository content could influence the agent runtime before a human had explicitly trusted that folder.

Second, when Gemini CLI ran with `--yolo`, it ignored fine-grained tool allowlists. A workflow might intend to allow only a narrow shell command such as `run_shell_command(echo)`, but the policy engine treated the shell tool too broadly. Prompt injection against an automated triage or review workflow could therefore escape the intended command boundary.

Patched versions changed both behaviors: headless mode requires explicit workspace trust, and tool allowlisting is evaluated under `--yolo`.

## Impact / 影响范围
GitHub rated the advisory Critical with CVSS 10.0. The affected surface included:

- `@google/gemini-cli` versions before `0.39.1`
- `@google/gemini-cli` `0.40.0-preview.2`
- `google-github-actions/run-gemini-cli` versions before `0.1.22`

The risk was concentrated in non-interactive CI/CD workflows that ran Gemini on untrusted inputs. In that setting, the AI agent becomes an interpreter for attacker-provided text and repository state, and any shell tool exposure can become code execution.

## Reproduction / 复现
This case does not include a PoC. The advisory provides enough technical detail to understand the bug class, but public exploit material would be easy to adapt against real CI workflows.

## Lessons & Mitigation / 启示与缓解
- Treat AI coding agents in CI as code execution surfaces, not as passive linters.
- Do not run headless agents on untrusted pull requests or issues unless the workflow has explicit trust controls and reduced permissions.
- Avoid broad `--yolo` execution in automation; use narrow allowlists and verify that the agent runtime enforces them.
- Pin patched versions: `@google/gemini-cli >= 0.39.1` or `0.40.0-preview.3`, and `run-gemini-cli >= 0.1.22`.
- Separate read-only triage workflows from workflows that can run shell commands, write repository content, or access secrets.

## References / 参考资料
- [GitHub Advisory GHSA-wpqr-6v78-jr5g](https://github.com/advisories/GHSA-wpqr-6v78-jr5g)
- [google-github-actions/run-gemini-cli security advisory](https://github.com/google-github-actions/run-gemini-cli/security/advisories/GHSA-wpqr-6v78-jr5g)
- [run-gemini-cli repository](https://github.com/google-github-actions/run-gemini-cli)
