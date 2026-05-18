# Cursor Sandbox Escape via Git Hooks (2026)
> Cursor 通过 Git Hooks 逃逸沙箱

| Field | Value |
|---|---|
| Category | Agent Risks |
| Severity | 🔴 Critical |
| AI Tool | Cursor |
| Language | Git |
| Real Incident | ✅ |
| Reproducible | ❌ |
| Disclosed | 2026-02-13 |
| CVE | CVE-2026-26268 |
| CVSS | 9.9 |

## TL;DR
Cursor versions before 2.5 allowed sandbox escape through improperly protected `.git` settings. A malicious agent path, including prompt injection, could write Git hooks that Git later executed automatically, producing out-of-sandbox RCE.

## Background / 背景
Cursor is an AI-native code editor. Like other agentic coding tools, it needs file-system access to edit code, inspect repository state, and run development workflows. Cursor's security boundary therefore depends on which files the agent can write and which downstream tools will execute those files.

Git hooks are a dangerous target in that model. They are stored under `.git/hooks` or configured through Git settings, and they are executed automatically by normal Git operations such as commit, merge, checkout, or other repository actions.

## What Went Wrong / 问题剖析
CVE-2026-26268 describes a sandbox escape in Cursor prior to version 2.5. The core issue was missing authorization around writes to `.git` configuration. A malicious agent, for example one controlled through prompt injection, could write or alter Git hook configuration.

The hook itself might not execute immediately. The vulnerability becomes dangerous because Git later runs hooks automatically, outside the original agent sandbox context. That turns a file-write primitive into delayed command execution.

This case is important because the exploit path is not a traditional parser bug. It is a cross-tool trust failure: the AI agent can modify repository control files, and another trusted developer tool later executes them.

## Impact / 影响范围
NVD scores the issue as CVSS 9.9 Critical. The affected product is Cursor before 2.5. The CVEProject record also lists a vendor/GitHub score of 8.1 High, while NVD's primary score is 9.9.

The realistic impact is highest when an agent processes untrusted content, such as copied instructions, generated tasks, or repository text that can steer the model. If the agent is allowed to write Git metadata, the repository can become a persistence and execution boundary bypass.

## Reproduction / 复现
No PoC is included. The case is documented from the CVE, NVD, and vendor advisory records.

## Lessons & Mitigation / 启示与缓解
- Upgrade Cursor to 2.5 or later.
- Treat `.git/`, Git hooks, editor startup files, shell profiles, package-manager scripts, and CI files as privileged write targets.
- Agent sandboxes should deny writes to execution-triggering control files unless explicitly approved.
- Security review for coding agents should include delayed execution paths, not only immediate shell commands.
- Prompt-injection defense should include file-system policy, because model instructions can be transformed into writes that another tool later executes.

## References / 参考资料
- [NVD: CVE-2026-26268](https://nvd.nist.gov/vuln/detail/CVE-2026-26268)
- [CVEProject cvelistV5: CVE-2026-26268](https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/26xxx/CVE-2026-26268.json)
- [Cursor security advisory GHSA-8pcm-8jpx-hv8r](https://github.com/cursor/cursor/security/advisories/GHSA-8pcm-8jpx-hv8r)
