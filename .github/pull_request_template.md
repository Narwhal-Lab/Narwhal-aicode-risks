<!-- 感谢您的贡献!提 PR 之前请勾选以下清单。Thanks for your contribution! Please tick the items below. -->

## What does this PR do? / 这个 PR 做了什么?

<!-- One paragraph. Link to a related Issue if any. / 一段话即可;有关联 issue 请引用。 -->

## Type / 类型

- [ ] New case (`cases/`) — confirmed real incident with primary sources
- [ ] New inferred case (`inferred/`) — partial public evidence
- [ ] New scenario (`scenarios/`) — illustrative, not a confirmed event
- [ ] Edit to an existing case
- [ ] Repo infrastructure (scripts, CI, docs)

## Pre-flight checklist / 投稿前自查

### Content / 内容

- [ ] Used `cases/_template/` (or `inferred/_template/` / `scenarios/_template/`) as the starting structure
- [ ] `meta.yaml` filled with all required fields including `severity_basis` and `verification_notes` (if applicable)
- [ ] README has the unified header (English title + Chinese subtitle + info table + TL;DR)
- [ ] Bilingual content: English headings paired with Chinese where the rest of the repo does so

### Verification / 核实

- [ ] **Every URL in `references` and the body has been opened and confirmed to load.** / 所有 references 与正文中的 URL 我都点开过并确认加载正常
- [ ] If a CVE is cited, it has been confirmed in NVD with the listed CVSS score
- [ ] Loss / scale numbers (`$X`, `Y records`, `Z users`) are sourced from a primary disclosure
- [ ] AI-attribution evidence is concrete (commit signatures, advisory text, etc.) — not speculation

### Local checks / 本地检查

- [ ] `python3 scripts/validate_cases.py` passes
- [ ] `python3 scripts/render_index.py` runs and the regenerated `cases/README.md` is included in this PR

### Compliance / 合规

- [ ] I have rights to redistribute any third-party assets I'm adding (screenshots, archived web pages, etc.) under CC BY 4.0
- [ ] No secrets, internal data, or personal identifiers in the PoC code

## How would you like to be credited? / 您希望如何署名?

<!-- GitHub username, real name, or 'anonymous'. After merge, a maintainer will run `@all-contributors please add @you for content` to add you to the contributor wall. -->
