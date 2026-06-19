# Nx "s1ngularity" NPM Supply Chain Attack Abuses LLM Prompt to Steal Credentials(2025)
> Nx “s1ngularity” 供应链攻击：滥用大模型提示批量窃取密钥（2025）

| Field | Value |
|---|---|
| Category | supply-chain |
| Severity | critical |
| AI Tool | Claude、Q、Gemini等 |
| Language | — |
| Real Incident | ✅ |
| Reproducible | ❌ |
| Disclosed | 2025-09 |
| CVE | — |
| CVSS | — |

## TL;DR
In 2025, Nx suffered supply-chain poisoning. Malware abused LLMs via optimized prompts to steal credentials in three-stage attacks, exposing thousands of repos. The project fixed CI rules and release policies afterward.
> 2025 年 Nx 遭供应链投毒，恶意脚本借助 Claude、Gemini 等 AI 工具，通过迭代提示词盗取海量密钥，攻击分三阶段泄露数千仓库源码，事后项目优化 CI 审批与发布机制完成整改。


## 基本信息

* 发生时间：2025-08
* 公开时间：2025-09
* 风险类型：供应链安全、提示词注入
* 影响范围：Claude、Q、Gemini等


## 一、事件概述与技术细节

Nx “s1ngularity” 供应链入侵事件经 Wiz 安全调研证实，恶意投毒造成海量账号凭据外泄，事件危害持续扩散。Nx 作为 JS 生态热门开源构建工具，每周 NPM 下载量超 550 万次。2025 年 8 月 26 日，攻击者借助项目存在漏洞的 GitHub Actions 流水线，发布植入恶意脚本 telemetry.js 的 NPM 恶意版本。该跨平台后门针对 Linux、macOS 环境，除常规搜刮 SSH 密钥、npm/GitHub 令牌、环境配置与钱包私钥外，还会调用本地 Claude、Amazon Q、Gemini 等 AI 客户端，依托大模型提示检索敏感信息，最终将窃取数据上传至 s1ngularity 公共仓库。本次攻击已波及 2180 个账户、7200 个代码仓库，大量被盗密钥仍处于可用状态，后续风险仍在蔓延。

<img width="800" height="400" alt="image" src="assets/1.jpg" />

Wiz安全报告披露，攻击者在Nx供应链攻击期间迭代优化恶意提示词以提升窃取效率。攻击者不断补充角色设定与技术细节调整指令，迭代轨迹清晰体现提示工程实战化特征；譬如在指令中添加渗透测试相关描述后，大模型拒绝执行敏感操作的频次显著上升。


## 二、影响范围

本次Nx s1ngularity供应链入侵被Wiz划分为三段递进式攻击周期，攻击者分步骤落地窃取、泄密、定向爆破等恶意操作，危害逐层放大。

* 第一阶段（8.26–8.27）：恶意包落地，大批量窃取本地凭据
恶意NPM版本大范围分发，超1700名开发者安装受污染Nx程序，恶意脚本完成本地遍历，累计盗取2000余个唯一身份密钥，扫描并外泄近20000份系统配置文件。虽然GitHub在恶意仓库上线仅8小时就完成下架处置，但攻击者早已提前完成全部敏感数据的备份与离线留存，阻断措施未能挽回已发生的数据泄露损失。
* 第二阶段（8.28–8.29）：盗用凭据批量扒开私有代码资产
黑客依托首轮盗取的有效GitHub访问令牌，批量篡改受害仓库配置，把大量私有代码库强制转为公开可见状态，并统一在仓库命名中嵌入标识`s1ngularity`。本轮攻击新增480个受害账号，其中多数为企业组织账号，合计6700座私有仓库彻底裸漏在公网环境，源码、业务配置全部外泄。
* 第三阶段（8.31及以后）：精准定向，对头部企业实施深度渗透
攻击者收拢前期窃取的高权限账号，锁定特定企业主体开展针对性打击，借助两个攻陷的账户继续批量解锁，额外强制公开500个私有仓库，持续扩大泄密范围，后续衍生的源码滥用、密钥盗用风险仍在持续扩散。

<img width="800" height="473" alt="image" src="assets/2.jpg" />


## 三、响应措施

Nx 官方在 GitHub 发布事故根因复盘报告，明确本次供应链入侵的核心诱因是PR标题注入漏洞，叠加项目不当启用`pull_request_target`事件触发机制。该配置缺陷允许外部攻击者借助恶意PR绕过权限管控，在CI流水线内以项目高权限上下文执行任意系统代码，非法劫持版本发布流程，最终窃取项目用于NPM上架的发布密钥，促成恶意安装包对外分发。

事件处置阶段，项目团队完成多项应急整改：平台侧全量下架所有被投毒的恶意Nx安装包，对已外泄的各类发布令牌集中吊销、批量轮换密钥，同时为全部具备发包权限的开发者账号强制开启双因素认证，封堵账号盗用隐患。在长效安全加固层面，Nx改用NPM可信发布者机制，从架构上废除传统令牌发包模式；除此之外，项目针对PR驱动的CI工作流新增人工审核卡点，所有外部PR无法自动触发流水线构建，从源头杜绝同类漏洞再次被利用。

## 四、关联报告风险点

该案例对应报告3.2节软件供应链风险：知识截断和供应链投毒：报告指出知识截断会造成模型推荐含已知漏洞的第三方依赖，催生供应链污染；本事故根源为 GitHub Actions 配置缺陷，攻击者投毒 NPM 发布恶意包，属于典型的开源供应链入侵。恶意脚本利用本地 Claude、Q、Gemini 等 AI 工具，借助提示词搜刮密钥，属于AI 交互带来敏感凭据泄露风险，匹配原文：开发者本地 AI 客户端在交互中因提示滥用造成密钥、私有代码外泄。
同时对应3.3节安全文化侵蚀（自动化偏见）：项目 CI 流水线缺少 PR 人工审批、过度自动化放行 PR，开发团队盲目信赖原有 CI 配置安全，疏于代码准入校验，是自动化偏见引发安全管控缺位；同时开发者普遍在本地环境混用 AI 编码工具并存放密钥，放大泄露风险，契合报告所述过度依赖自动化、人工审查弱化，团队安全能力退化。

## 五、参考来源

* AI-powered malware hit 2,180 GitHub accounts in “s1ngularity” attack                                                                  (https://www.bleepingcomputer.com/news/security/ai-powered-malware-hit-2-180-github-accounts-in-s1ngularity-attack/)
* AI驱动恶意软件在“s1ngularity”攻击中入侵2180个GitHub账户
(https://www.anquanke.com/post/id/311988)
