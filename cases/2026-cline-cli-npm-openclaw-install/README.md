# Unauthorized Cline CLI npm Publish Installed OpenClaw (2026)
> Cline CLI npm 未授权发布导致 OpenClaw 被安装

| Field | Value |
|---|---|
| Category | Hallucination & Supply Chain |
| Severity | 🟡 Medium |
| AI Tool | Cline CLI, OpenClaw |
| Language | JavaScript, npm |
| Real Incident | ✅ |
| Reproducible | ❌ |
| Disclosed | 2026-02-17 |
| CVE | — |
| CVSS | — |

## TL;DR
An unauthorized party used a compromised npm publish token to publish `cline@2.3.0`. The package added a `postinstall` script that globally installed `openclaw@latest`; Cline's advisory says OpenClaw itself was legitimate and non-malicious, but the event exposed a real AI-coding-tool distribution-chain failure.

## Background / 背景
Cline is an open-source AI coding assistant with a CLI and editor integrations. Its CLI is distributed through npm, so a compromised npm publishing path can directly affect developer machines and CI environments.

The official post-mortem is especially relevant to AI-assisted development security because the incident involved automation around AI-powered triage and publication workflows. Cline later removed AI-powered triage workflows and moved npm publishing to OIDC provenance through GitHub Actions.

## What Went Wrong / 问题剖析
According to Cline's advisory, an unauthorized party published `cline@2.3.0` on February 17, 2026 using a compromised npm publish token. The package differed from the legitimate CLI release by a modified `package.json` containing a postinstall script:

```json
"postinstall": "npm install -g openclaw@latest"
```

The official advisory states that the CLI binary and other package contents matched the legitimate release, and that OpenClaw was an unrelated non-malicious open-source package. The security failure was nevertheless real: the package channel for an AI coding CLI accepted an unauthorized release.

The post-mortem also describes the broader lessons: AI automation with broad tool access in CI/CD can become a security boundary, and publication credentials must not be exposed to workflows that process untrusted input.

## Impact / 影响范围
The affected version was `cline@2.3.0`, available for roughly eight hours on February 17, 2026. Users who installed that version had OpenClaw globally installed without authorization.

Cline states that the VS Code extension and JetBrains plugin were not affected, and that corrected version `2.4.0` fixed the package. The compromised token was revoked, old publishing flow was replaced, and npm publishing now uses OIDC provenance.

The impact is medium in this case library because the payload was reportedly non-malicious, but the attack path reached a real package release channel for a developer AI tool.

## Reproduction / 复现
No reproduction is included. The compromised version was deprecated, and reinstalling it would not be useful for defensive research.

## Lessons & Mitigation / 启示与缓解
- Do not let AI triage workflows run with shell access and publication-adjacent credentials.
- Use OIDC trusted publishing instead of long-lived npm tokens.
- Treat `postinstall` as executable code and scan package diffs before allowing new CLI versions into developer images.
- Monitor package registries for unexpected versions and unexpected lifecycle scripts.
- When an AI development tool is affected, check both direct developer installs and CI images, because CLI packages often live in both places.

## References / 参考资料
- [Cline post-mortem: Unauthorized Cline CLI npm publish](https://cline.bot/blog/post-mortem-unauthorized-cline-cli-npm)
- [Cline security advisory GHSA-9ppg-jx86-fqw7](https://github.com/cline/cline/security/advisories/GHSA-9ppg-jx86-fqw7)
- [GitHub Advisory GHSA-9ppg-jx86-fqw7](https://github.com/advisories/GHSA-9ppg-jx86-fqw7)
