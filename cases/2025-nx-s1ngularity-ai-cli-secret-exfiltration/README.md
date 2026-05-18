# Nx s1ngularity Supply-Chain Attack Weaponized AI CLIs (2025)
> Nx s1ngularity 供应链攻击武器化 AI CLI

| Field | Value |
|---|---|
| Category | Hallucination & Supply Chain |
| Severity | 🔴 Critical |
| AI Tool | AI CLI agents |
| Language | JavaScript, GitHub Actions, npm |
| Real Incident | ✅ |
| Reproducible | ❌ |
| Disclosed | 2025-08-27 |
| CVE | CVE-2025-10894 |
| CVSS | — |

## TL;DR
The Nx s1ngularity incident compromised npm releases for `nx` and related packages. The malicious postinstall code scanned local files, collected credentials, published encoded data to GitHub repositories, and included an AI-agent prompt in `telemetry.js` to inventory sensitive text files.

## Background / 背景
Nx is a widely used build system for JavaScript and monorepo projects. A malicious release of Nx is high impact because it can run during package installation across developer machines, CI jobs, and editor-driven tooling.

This case belongs in an AI-code-risk library because the malware did not merely target source repositories. The advisory appendix documented a prompt that instructed an AI file-search agent to enumerate text configuration and environment files and write an inventory to `/tmp/inventory.txt`. The attack shows AI coding CLIs becoming ambient tools that malware can try to commandeer.

## What Went Wrong / 问题剖析
Nx's postmortem traces the root cause to a GitHub Actions workflow vulnerability: an unsafe pull-request title validation step combined with `pull_request_target` privileges. The attacker used that path to reach workflows with higher permissions and ultimately obtain an npm publish token.

Malicious versions of `nx` and several `@nx/*` packages were then published to npm. The malicious `postinstall` behavior scanned user files, looked for credentials, and posted encoded content to GitHub repositories under affected users' accounts with names containing `s1ngularity-repository`.

The case also highlights a newer attacker pattern: use local AI tooling as a helper. The advisory appendix shows an instruction prompt for a file-search agent to inventory likely plaintext secrets and configuration files. In other words, developer AI tools can become part of the malware execution environment even when they are not the original vulnerability.

## Impact / 影响范围
GitHub Advisory GHSA-cxm3-wv7p-598c is reviewed, marked Critical, and associated with CVE-2025-10894. It lists multiple malicious versions of `nx` and related packages, including `nx` 21.5.0, 20.9.0, 20.10.0, 21.6.0, 20.11.0, 21.7.0, 21.8.0, and 20.12.0, plus affected `@nx/*` packages.

The malicious code attempted credential theft and GitHub publication of exfiltrated data. Nx also reported that the Nx Console VS Code extension could trigger installation of the latest `nx` package during the affected window, broadening exposure beyond users who explicitly installed Nx.

## Reproduction / 复现
No PoC is included. The malicious packages have been removed or deprecated, and defensive analysis should rely on the official advisory, postmortem, and incident indicators.

## Lessons & Mitigation / 启示与缓解
- Avoid `pull_request_target` for workflows that execute untrusted content unless every interpolated field is treated as hostile.
- Replace long-lived npm tokens with trusted publishing/OIDC where possible.
- Scan package lifecycle scripts, especially `postinstall`, before allowing packages into CI or developer base images.
- Treat local AI CLIs as high-value executable tooling: malware may use them for file search, summarization, credential discovery, or command planning.
- Rotate GitHub, npm, cloud, and environment credentials if a machine installed a malicious Nx version during the affected window.

## References / 参考资料
- [Nx postmortem: s1ngularity](https://nx.dev/blog/s1ngularity-postmortem)
- [GitHub Advisory GHSA-cxm3-wv7p-598c](https://github.com/advisories/GHSA-cxm3-wv7p-598c)
- [Nx repository security advisory GHSA-cxm3-wv7p-598c](https://github.com/nrwl/nx/security/advisories/GHSA-cxm3-wv7p-598c)
- [NVD: CVE-2025-10894](https://nvd.nist.gov/vuln/detail/CVE-2025-10894)
