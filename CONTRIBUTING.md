# Contributing a Case

> 中文版见下方

We welcome new case submissions documenting security risks of AI-generated code. There are **two ways to contribute**:

## Path A — Submit an Issue (no git/markdown experience needed)

Open the [**📝 Submit a case**](../../issues/new?template=submit-case.yml) Issue Form. Fill out the structured fields; a maintainer will fact-check, convert to a draft PR, and credit you. **SLA: a maintainer responds within 14 days.**

## Path B — Open a Pull Request (for confident contributors)

1. **Pick the right bucket**:
   - `cases/` — confirmed real incidents with primary sources (vendor advisory / CVE / official postmortem / court filing)
   - `inferred/` — partial public evidence; event appears real but key facts not pinned down
   - `scenarios/` — illustrative patterns, **not** confirmed events
2. **Copy the template**: `cp -r {bucket}/_template {bucket}/<year>-<short-slug>`
3. **Fill `meta.yaml`** with structured metadata (see field reference below).
4. **Write the bilingual `README.md`** following the template sections.
5. **Add evidence to `assets/`**: screenshots, archived web pages, advisory PDFs, etc.
6. **(Optional) Add `code/`** for minimal reproducible PoCs. Mark `reproducible: true` in `meta.yaml`.
7. **Validate locally**:
   ```bash
   pip install pyyaml
   python3 scripts/validate_cases.py          # schema check
   python3 scripts/validate_cases.py --check-links   # also HEAD all references (slower)
   python3 scripts/render_index.py            # regenerate index + SVGs
   ```
8. **Open a PR** with the regenerated `cases/README.md` included. The PR template has a verification checklist.
9. **CI** runs `validate_cases.py` and checks that `render_index.py` artifacts are up-to-date.

## `meta.yaml` field reference

| Field | Required | Type | Notes |
|---|---|---|---|
| `slug` | ✅ | string | Must match directory name (`<year>-<short-slug>`) |
| `title_en` | ✅ | string | English title (used as card heading) |
| `title_cn` | ✅ | string | Chinese title |
| `year` | ✅ | int | Year the incident was disclosed or research was published |
| `disclosed` | ⚪ | date | Disclosure date (YYYY-MM-DD) if known |
| `category` | ✅ | enum | One of: `supply-chain`, `code-vulns`, `cloud-iac`, `agent-risk`, `domain-specific`, `ip-compliance`, `human-factor` |
| `severity` | ✅ | enum | `critical` / `high` / `medium` / `low` / `info` |
| `severity_basis` | ✅ | enum | `cvss` (anchored to a public CVE) / `quantifiable-impact` (anchored to a published loss / scope figure) / `editorial` (judgment without a CVSS scale) |
| `severity_evidence` | ✅ | string | One line citing the specific evidence the severity rests on |
| `cvss` | ⚪ | float | CVSS v3.x score for cases with a CVE |
| `cve` | ⚪ | string | CVE id (e.g. `CVE-2025-55526`) |
| `real_incident` | ✅ | bool | `true` for real-world events; `false` for `scenarios/` |
| `evidence_strength` | ⚪ | enum | `full` (cases/) / `partial` (inferred/) — required for inferred cases |
| `missing_evidence` | ⚪ | string | For `inferred/` cases: what evidence would promote this to `cases/` |
| `ai_tool` | ✅ | list | AI tools involved (e.g. `[Claude Code, Cursor, ChatGPT]`) |
| `language` | ⚪ | list | Programming languages involved |
| `attack_surface` | ⚪ | list | Free-form tags for the affected surface |
| `reproducible` | ✅ | bool | `true` if `code/` contains a runnable PoC |
| `tldr` | ✅ | string | One-sentence summary (≤120 chars) used on the homepage card |
| `references` | ✅ | list | List of `{title, url}` |
| `verification_notes` | ⚪ | string | What was checked during verification, what could not be confirmed |
| `tags` | ⚪ | list | Free-form keyword tags |

## Severity basis — how to choose

This is the single field that most submissions get wrong. Pick:

- **`cvss`** when the case has a CVE in NVD or a vendor advisory with a published CVSS score. Put the score in `cvss:` and cite NVD/MSRC/etc. in `severity_evidence:`.
- **`quantifiable-impact`** when there's no CVSS but a *primary source* publishes a loss/scope figure ($X stolen, Y records leaked, Z repos pulled the bad package). Cite the specific source.
- **`editorial`** when neither applies (legal cases, IP/compliance, behavioural patterns). Acknowledge in `severity_evidence:` that this is a judgment call.

If you can't pin down at least `editorial` with a one-line justification, the case is too thin to merge. Try `inferred/` instead.

## Style guide

- **Bilingual READMEs**: English heading, Chinese subtitle in a blockquote, then bilingual section headers (`## Background / 背景`).
- **No emoji in raw evidence**: keep screenshots and quoted log output literal.
- **Don't speculate on attribution**: if AI involvement is inferred (e.g. from commit co-authorship), say so explicitly. Do not assert beyond what public evidence supports.
- **Mind the licenses**: only include third-party PDFs/HTML archives that you have the right to redistribute under CC BY 4.0 or compatible terms.

## Verification policy

Every case is fact-checked before merge. Specifically:

- Each URL in `references:` is opened and confirmed to load and to corroborate the specific claim attributed to it.
- If a CVE is cited, the entry in NVD is checked for CVSS, disclosure date, and any "disputed" flag.
- Loss / scope figures are traced to a primary source.
- AI-attribution evidence is independently confirmed (commit signatures inspected, advisory pages opened).

Cases that survive verification go in `cases/`. Cases with partial evidence go in `inferred/` with a banner. Cases that turn out to be unsupported go in `scenarios/` (or are removed).

## Maintainer SLA

| Submission path | First response |
|---|---|
| Issue Form | 14 days |
| PR — minor edit | 7 days |
| PR — new case | 14 days |
| PR — new bucket / structural change | 30 days |

If a maintainer hasn't responded by then, ping the thread.

## Recognition

Once your contribution is merged, a maintainer will run:

```
@all-contributors please add @your-handle for content
```

…which adds you to the [Contributors](README.md#contributors) wall on the homepage. You can also list specific contribution types (`research`, `review`, `doc`, `infra`, etc.) — the bot will figure it out.

## Code of Conduct

By participating, you agree to abide by the [Contributor Covenant](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). Be respectful; assume good faith; report misconduct to thebinking66@gmail.com.

---

# 贡献案例（中文）

欢迎提交新的 AI 生成代码安全风险案例 —— 可以是真实事件、复现实验或研究发现。

## 如何添加案例

1. 拷贝模板：`cp -r cases/_template cases/<年份>-<短 slug>`
2. 填写 `meta.yaml`（字段参考见上）
3. 按模板撰写双语 `README.md`
4. 把证据材料放到 `assets/`：截图、网页归档、披露 PDF 等
5. （可选）`code/` 放最小可复现 PoC，并把 `meta.yaml` 中 `reproducible` 设为 `true`
6. 向 `main` 分支提 PR；CI 会跑 `scripts/render_index.py` 自动重渲染案例索引

提交前请阅读上方 Style guide。
