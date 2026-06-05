# `inferred/` — Cases with partial public evidence

> 介于 `cases/`(已完整确证)与 `scenarios/`(纯示例)之间的中间档。

## When to use this directory / 何时把案例放在这里

Use `inferred/` when **all of the following** are true:

- The incident appears to be real (not a research experiment, not a hypothetical scenario)
- There is **at least one** independent public source attesting to it (e.g. a journalist, a security researcher, a tweet from a credible account)
- But you **cannot** point to a vendor advisory, a CVE, an official postmortem, or a court filing that pins down the specific facts you're asserting
- AI involvement is plausible but the attribution evidence is partial (e.g. circumstantial, screenshot-based, or only stated by a secondary source)

把案例放进 `inferred/` 当且仅当满足以上**全部**条件:事件看起来是真实发生的(不是实验也不是假设),至少有一份独立公开来源,但缺少厂商 advisory / CVE / 官方复盘 / 法庭文书等"硬"一手材料,且 AI 参与的归因证据是部分性的(传闻、截图、二手转述)。

If you have a vendor advisory or a CVE, use `cases/` instead.
If you're making up a teaching example, use `scenarios/` instead.

## Required disclaimers in the README

Every README under `inferred/` must:

1. Open with an `> ⚠️ Inferred case` banner (see `inferred/_template/README.md`).
2. List in `meta.yaml` the specific *missing* evidence that would promote it to `cases/`.
3. Set `evidence_strength: partial` in `meta.yaml`.
4. Use hedged language in the body: "appears to", "according to", "if the report is accurate" — not "the company lost X."

## Promotion / 升级路径

If a vendor advisory, CVE, or official postmortem subsequently appears, anyone can open a PR to:

- Move the directory: `git mv inferred/<slug> cases/<slug>`
- Update `meta.yaml`: set `evidence_strength: full`, fill in `cve` / `cvss` / etc.
- Remove the inferred-case banner from the README

## Demotion / 降级路径

If verification later reveals the incident was a misunderstanding or a misattribution, the case should be moved to `scenarios/` (with notes), or removed entirely.
