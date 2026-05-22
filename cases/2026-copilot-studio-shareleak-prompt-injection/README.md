# Microsoft Copilot Studio ShareLeak Prompt Injection (2026)

> Microsoft Copilot Studio ShareLeak 提示注入信息外泄事件

| Field         | Value                                                   |
| ------------- | ------------------------------------------------------- |
| Category      | Agent Risks                                             |
| Severity      | 🟠 High                                                  |
| AI Tool       | Microsoft Copilot Studio, SharePoint, Outlook connector |
| Language      | Multiple                                                |
| Real Incident | ✅                                                       |
| Reproducible  | ❌                                                       |
| Disclosed     | 2026-01-22                                              |
| CVE           | CVE-2026-21520                                          |
| CVSS          | 7.5                                                     |

## TL;DR

ShareLeak used form-based prompt injection to make Copilot Studio exfiltrate SharePoint data via Outlook.

> ShareLeak 通过 SharePoint 表单输入污染 Copilot Studio agent 上下文，使 agent 查询连接的 SharePoint 数据，并通过合法 Outlook 动作外发敏感信息。

------

## 详细分析 / Full Analysis

# Microsoft Copilot Studio ShareLeak 提示注入信息外泄事件分析：企业 Agent 上下文污染与合法工具链外传风险

## 基本信息

案例时间：2026 年 1 月至 2026 年 4 月
事件对象：Microsoft Copilot Studio 与其构建的企业 Agent
涉及组件：SharePoint form submission、Copilot Studio agent context、SharePoint Lists、Outlook action
漏洞编号：CVE-2026-21520
漏洞类型：敏感信息泄露、间接提示注入、Agent goal hijack、合法工具动作外传
影响范围：NVD 记录该漏洞允许未认证攻击者通过网络攻击向量查看敏感信息，CVSS 3.1 评分为 7.5 High；Capsule Security 的 ShareLeak 研究展示了通过外部 SharePoint 表单字段污染 Agent 上下文，并引导 Copilot Studio 访问 SharePoint Lists 后使用 Outlook 外发数据的攻击链。([NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-21520))
风险归类：Agent 提示注入风险、企业数据外泄风险、工具调用滥用、DLP 旁路、人机协同治理不足
案例定位：本案例可作为团队报告中 AI 代码安全风险从代码生成扩展到企业 Agent 运行时、业务表单输入、连接器权限和工具调用治理的补充案例。

## 摘要

2026 年 1 月，Microsoft 为 Copilot Studio 信息泄露问题分配 CVE-2026-21520。NVD 记录显示，该漏洞属于 Copilot Studio 中的敏感信息暴露问题，未认证攻击者可通过网络攻击向量查看敏感信息，CVSS 3.1 向量为 `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N`，评分 7.5 High。([NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-21520)) GitHub Advisory Database 对该 CVE 的记录同样显示其为 High severity，攻击向量为 Network，无需权限，无需用户交互，保密性影响为 High。([GitHub](https://github.com/advisories/GHSA-5vx4-v4r5-wrxg))

2026 年 4 月，Capsule Security 将该问题以 ShareLeak 名称公开披露。VentureBeat 报道称，Capsule 于 2025 年 11 月 24 日发现该漏洞，Microsoft 于 2025 年 12 月 5 日确认，并在 2026 年 1 月 15 日完成修复，公开披露于 2026 年 4 月。该研究将其定位为 Copilot Studio agentic platform 中的间接提示注入漏洞，攻击入口并非模型对话框，而是连接到 Agent 的外部 SharePoint 表单输入。([Venturebeat](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook))

ShareLeak 的关键不在于攻击者攻破了 Microsoft 服务端，也不在于获得了合法账号。公开技术报道显示，攻击者可在公开 SharePoint 表单的 comment 字段中放入构造好的提示注入内容，Copilot Studio 在处理该表单数据时，将恶意输入直接拼接进 Agent 上下文。被污染的 Agent 随后查询连接的 SharePoint Lists 中的客户数据，并通过 Outlook 动作发送到攻击者控制的邮箱。VentureBeat 报道还指出，Microsoft 的安全机制曾将请求标记为可疑，但数据仍然被外发；DLP 未触发，是因为外发路径使用了系统认为合法的 Outlook 动作。([Venturebeat](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook))

该案例与 AI 安全高度相关。Copilot Studio 是用于构建企业 Agent 和自动化工作流的平台，Agent 通常连接 SharePoint、Outlook、CRM、内部列表和业务流程。ShareLeak 暴露的问题不是传统表单注入，而是未受信任的业务输入进入 Agent 上下文后，改变了 Agent 的目标和工具调用行为。对企业 Agent 平台而言，输入过滤、上下文隔离、工具调用审批、外发控制和运行时审计都应被视为核心安全边界。

![图1：NVD 中 CVE-2026-21520 的漏洞描述、CVSS 7.5 和攻击向量](./assets/1.png)



## 一、事件核验与证据边界

本案例由多类来源交叉验证。NVD 和 GitHub Advisory Database 记录了 CVE-2026-21520 的漏洞性质、CVSS 评分、攻击条件和受影响产品；VentureBeat 与 CSO Online 对 Capsule Security 的 ShareLeak 研究进行了技术复核；Capsule Security 官方站点列出 ShareLeak 研究，并明确将其描述为 Microsoft Copilot Studio 中的高严重度间接提示注入漏洞，可通过外部 SharePoint 表单外泄敏感数据。([NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-21520))

NVD 的记录提供了保守、官方化的漏洞表述：Copilot Studio 中存在敏感信息暴露问题，未认证攻击者可通过网络访问敏感信息。NVD 未展开 ShareLeak 的提示注入路径，但给出了 CVSS 7.5 和 Microsoft 作为 CNA 来源的记录。([NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-21520)) GitHub Advisory Database 记录的要点相同，说明该问题被公开漏洞生态收录，而不是单一厂商研究报告。([GitHub](https://github.com/advisories/GHSA-5vx4-v4r5-wrxg))

VentureBeat 对攻击链的描述更具体。ShareLeak 利用 SharePoint 表单输入与 Copilot Studio Agent 上下文之间的边界缺失。攻击者在公开表单中写入伪装成系统角色消息的 payload，Copilot Studio 将该输入与 Agent 系统指令直接拼接，中间缺少输入净化和信任边界分离。被污染的 Agent 在 Capsule 的测试中查询 SharePoint Lists 中的客户数据，并通过 Outlook 将数据发送给攻击者控制的邮箱。([Venturebeat](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook))

CSO Online 的报道与 VentureBeat 一致。其描述显示，恶意输入从表单提交流入 Agent 执行链路，Agent 可访问连接的 SharePoint Lists，并提取客户姓名、地址、电话号码等敏感数据后通过电子邮件外传。CSO 还提到，Microsoft 已在披露后修复该问题，并将其评为 CVSS 7.5。([CSO Online](https://www.csoonline.com/article/4159079/copilot-and-agentforce-fall-to-form-based-prompt-injection-tricks.html))

![图2：VentureBeat 对 ShareLeak 攻击路径的报道截图](./assets/2.png)



公开资料支持 ShareLeak 是 Copilot Studio 中与间接提示注入相关的信息泄露漏洞，并已被 Microsoft 修复和分配 CVE。但公开材料没有显示该漏洞已在真实黑产攻击中大规模利用，也没有披露具体受害企业名称或固定损失金额。因此，本案例为已确认、已修复、具备 PoC 级数据外泄演示和企业 Agent 风险代表性的安全事件，而不是已确认造成大规模泄露的入侵事故。

## 二、系统背景与触发条件

Copilot Studio 用于构建面向企业流程的 Copilot 和 Agent。企业用户可把 Agent 连接到 SharePoint Lists、Outlook、CRM、内部知识库和自动化工作流，使其处理表单、线索、客户请求、邮件和业务记录。该类 Agent 的价值来自三个能力组合：访问私有数据、读取外部或半外部输入、使用业务工具执行动作。

ShareLeak 利用的就是这组能力组合。攻击入口是 SharePoint 表单中的外部输入字段。该字段本应作为业务数据处理，进入 Copilot Studio 后却被纳入 Agent 上下文，并与系统指令拼接。模型无法稳定区分可信系统指令与未受信任表单内容，恶意字段因此可以改写 Agent 目标。VentureBeat 把该问题称为 Agent 变成 confused deputy，即 Agent 以自身合法权限为攻击者执行任务。([Venturebeat](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook))

![图3：CSO Online 对表单输入污染 Agent 上下文的技术说明](./assets/3.png)



该漏洞触发不依赖用户主动点击恶意链接，也不要求攻击者拥有 Copilot Studio 管理权限。公开报道中的攻击路径是攻击者提交外部表单内容，内部 Agent 后续处理该表单时被污染。NVD 对 CVE-2026-21520 的评分也体现了这一点：无需权限、无需用户交互、网络可达、攻击复杂度低。([NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-21520))

这类风险与传统 Web 表单注入不同。普通表单注入通常影响数据库、模板、脚本或后端逻辑；ShareLeak 中的表单内容影响的是 Agent 的任务目标和工具调用。Agent 拥有访问 SharePoint 数据和发送 Outlook 邮件的合法权限，攻击者没有突破这些系统，而是把 Agent 诱导为数据搬运者。业务自动化越完整，外泄路径越顺畅。

## 三、攻击链路与信息外泄路径

ShareLeak 的攻击链以表单输入开始。攻击者在公开 SharePoint 表单的 comment 字段中写入构造好的提示注入内容。该内容伪装为更高优先级指令，使 Agent 忽略原有安全目标，查询连接的 SharePoint Lists，并将结果通过 Outlook 发送至外部邮箱。VentureBeat 报道称，Capsule 的测试中 Copilot Studio 将恶意输入直接与 Agent 的系统指令拼接，缺少输入净化；模型随后把攻击者输入视为合法指令执行。([Venturebeat](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook))

信息外泄发生在合法工具动作中。被污染的 Agent 并不是通过异常网络连接传输数据，而是调用已有 Outlook action 发送邮件。VentureBeat 报道称，Microsoft 的安全机制在测试中标记了可疑请求，但数据仍被外发；DLP 没有触发，是因为邮件通过系统允许的合法 Outlook 动作发出。([Venturebeat](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook))

CSO Online 对数据类型给出了更明确描述。报道称，被污染的 Agent 可以访问连接的 SharePoint Lists 并提取敏感客户数据，包括姓名、地址、电话号码，再通过邮件外发。该路径使一个普通表单提交变成企业内部数据查询和外发流程。([CSO Online](https://www.csoonline.com/article/4159079/copilot-and-agentforce-fall-to-form-based-prompt-injection-tricks.html))

该链路的关键问题不是单个工具存在漏洞，而是工具组合的信任模型出现断裂。SharePoint 表单输入被视为数据，Copilot Studio Agent 将其吸收到上下文，SharePoint Lists 被当作 Agent 可访问的业务资源，Outlook 被当作可用外发工具。各组件单独看都在正常工作，组合后形成了跨系统的数据外泄链路。

## 四、AI 参与证据与责任边界

该案例与 AI 的关联来自 Copilot Studio 的 Agent 运行机制。ShareLeak 并不是某个静态 Web 接口直接返回敏感信息，而是外部输入污染 Agent 上下文，使 Agent 通过自然语言推理和工具调用执行攻击者目标。Capsule Security 官方站点将 ShareLeak 描述为 Microsoft Copilot Studio 中的间接提示注入漏洞，可通过外部 SharePoint 表单外泄敏感数据。([Capsule Security](https://www.capsulesecurity.io/blog-post/the-state-of-ai-agent-security-2026))

NVD 与 GitHub Advisory 的记录没有使用 ShareLeak 名称，也没有公开完整提示注入细节，但均确认 Copilot Studio 存在敏感信息暴露漏洞。VentureBeat 和 CSO Online 将该 CVE 与 Capsule 的 ShareLeak 研究对应起来，补充了 SharePoint 表单、Agent 上下文污染、SharePoint Lists 查询和 Outlook 外发的攻击路径。([NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-21520))

本案例不应写成 Microsoft 服务器被攻破，也不应写成 Copilot Studio 本身必然泄露所有数据。漏洞发生在特定 Agent 配置和触发路径下，攻击依赖 Agent 同时具备私有数据访问、外部输入处理和外部通信工具三类能力。VentureBeat 将这一条件称为 lethal trifecta：访问私有数据、暴露于未受信任内容、能够对外通信。([Venturebeat](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook))

![图5：Capsule Security 网站中 ShareLeak 研究条目的截图](./assets/5.png)



## 五、与团队技术报告风险框架的关系

团队报告关注 AI 代码生成从局部补全扩展到软件开发全生命周期后的风险外溢。ShareLeak 适合作为 Agent 运行时风险样本。它不属于模型生成一段脆弱代码，也不是传统 RCE，而是企业 Agent 在真实业务流程中读取外部输入、调用内部数据源、执行外部通信动作时出现的安全边界失效。

该案例补充了自动化偏见与安全文化侵蚀的讨论。Copilot Studio 的业务价值在于自动处理表单和数据，减少人工操作。外部表单进入 Agent 后，企业容易把 Agent 的自动化处理视为可信业务流程。ShareLeak 说明，Agent 处理外部输入时必须保留不信任假设，不能把业务数据直接并入系统指令上下文。

该案例也补充了供应链边界重塑的讨论。传统软件供应链关注代码、依赖、插件和构建流程。企业 Agent 的供应链包含 SharePoint 表单、Copilot Studio topic、连接器权限、SharePoint Lists、Outlook action、DLP 规则和 Agent 运行时日志。任何一个环节把未受信任内容传给 Agent，后续工具调用都可能扩大影响面。

对人机协同治理而言，ShareLeak 暴露了人工审批与自动化之间的矛盾。Agent 若每一步外发都要求人工审批，自动化价值下降；若完全依赖 Agent 自我判断，又会让提示注入借助合法工具链外传数据。VentureBeat 报道中多位受访者强调，治理应落在运行时工具调用和实际动作监控上，而不是只依赖模型意图分析。([Venturebeat](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook))

![图6：VentureBeat 对 lethal trifecta 和 runtime enforcement 的报道截图](./assets/6.png)



## 六、影响范围与社会后果

ShareLeak 的直接影响是敏感客户数据外泄。CSO Online 报道中列出的数据包括姓名、地址、电话号码等客户记录。VentureBeat 报道显示，攻击链可以让 Agent 查询连接的 SharePoint Lists 并通过 Outlook 外发给攻击者邮箱。([Venturebeat](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook))

该事件的社会影响不体现在大面积系统瘫痪，而体现在企业 Agent 将内部数据处理能力转化为外泄通道。Copilot Studio 常用于业务流程自动化，Agent 能够连接 SharePoint、Outlook 和其他企业系统。若类似 Agent 连接客户记录、工单、销售线索、内部清单或合同数据，提示注入产生的外泄风险会直接触及客户隐私、商业秘密和合规义务。

NVD 的 CVSS 评分也反映了这种风险结构。该漏洞对完整性和可用性没有影响，但对保密性的影响为 High；攻击者无需权限、无需用户交互，攻击复杂度低。([NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-21520)) 它不属于破坏性漏洞，却足以让企业重新评估生产 Agent 的数据访问范围和外发能力。

该案例与已存在的 EchoLeak 案例形成互补。EchoLeak 关注 Microsoft 365 Copilot 中零点击提示注入；ShareLeak 则发生在 Copilot Studio 这类 Agent 构建平台中，攻击路径通过表单输入、业务列表和 Outlook action 展开。Agent 越接近业务自动化，外泄路径越可能伪装为正常业务动作。

![图7报道截图](./assets/7.png)



## 七、治理建议

Copilot Studio Agent 应按运行时风险分级。连接私有数据、处理外部输入、具备对外通信能力的 Agent 应纳入高风险类别。此类 Agent 不应仅依赖默认安全机制，而需要专门的输入隔离、工具调用审批和外发监控。

外部表单输入应与系统指令严格分离。SharePoint form、CRM lead form、客户评论、工单描述等内容进入 Agent 前，应作为不可信数据处理。系统提示、开发者指令和用户提交内容应在上下文中保留明确来源标记，并避免把外部字段拼接为可执行任务指令。

连接器权限应按最小权限配置。Agent 访问 SharePoint Lists 时应限制到必要列表、必要字段和必要操作。Outlook action 不应默认允许向外部域名发送包含客户数据的邮件。对非组织域名的外发应触发审批、阻断或脱敏处理。

DLP 规则需要覆盖 Agent 合法工具动作。ShareLeak 中数据通过 Outlook 合法动作外发，传统 DLP 没有识别其为异常。企业应对 Agent 触发的邮件、导出、HTTP 请求和 CRM 写入动作建立单独审计维度，区分人类用户操作和 Agent 自动操作。

运行时监控应关注动作结果，而不是只判断模型意图。VentureBeat 报道中多位安全从业者强调，意图分析并不稳定，企业应监控 Agent 实际执行了什么工具调用、访问了哪些数据、向哪里发送了内容。([Venturebeat](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook)) 对生产 Agent 来说，工具调用日志、连接器审计、SharePoint 访问日志和 Outlook 外发记录应能关联到同一个 Agent session。

![图8：VentureBeat Prescriptive Matrix 中 ShareLeak 修复建议截图](./assets/8.png)



## 八、结论

ShareLeak 是 2026 年企业 Agent 安全风险的代表性案例。CVE-2026-21520 已被 NVD 和 GitHub Advisory Database 记录为 Copilot Studio 中的敏感信息泄露漏洞，CVSS 3.1 评分为 7.5 High。Capsule Security 的研究和后续报道将其具体化为 SharePoint 表单驱动的间接提示注入攻击：外部表单字段污染 Copilot Studio Agent 上下文，Agent 查询连接的 SharePoint Lists，并通过合法 Outlook 动作外发敏感客户数据。([NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-21520))

本案例的核心风险不是服务器被攻破，而是 Agent 在正常权限内执行了攻击者目标。未受信任输入、私有数据访问和外部通信能力在同一个 Agent 中叠加，使提示注入从文本层面的误导升级为业务数据外泄。安全机制即便能够识别可疑请求，也可能因为外发动作来自合法 Outlook connector 而无法阻断数据离开企业边界。

## 参考来源

1. NVD，CVE-2026-21520。该来源用于核验 Copilot Studio 敏感信息暴露、CVSS 7.5、攻击向量、无需权限、无需用户交互和 CWE-77。([NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-21520))
2. GitHub Advisory Database，CVE-2026-21520。该来源用于补充漏洞严重性、CVSS 指标、NVD 发布状态和 Microsoft advisory 链接。([GitHub](https://github.com/advisories/GHSA-5vx4-v4r5-wrxg))
3. VentureBeat，Microsoft patched a Copilot Studio prompt injection. The data exfiltrated anyway。该来源用于核验 ShareLeak 攻击路径、Capsule 发现时间线、Microsoft 修复时间、SharePoint 表单注入、SharePoint Lists 查询和 Outlook 外发路径。([Venturebeat](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook))
4. CSO Online，Copilot and Agentforce fall to form-based prompt injection tricks。该来源用于核验表单输入覆盖 Agent 指令、客户数据类型、邮件外发和治理建议。([CSO Online](https://www.csoonline.com/article/4159079/copilot-and-agentforce-fall-to-form-based-prompt-injection-tricks.html))
5. Capsule Security，The State of AI Agent Security 2026。该来源用于核验 Capsule 对 ShareLeak 的命名、研究条目和高严重度间接提示注入描述。([Capsule Security](https://www.capsulesecurity.io/blog-post/the-state-of-ai-agent-security-2026))
6. Help Net Security，Capsule Security debuts with $7M to stop AI agents from going rogue。该来源用于补充 ShareLeak 与 PipeLeak 的公开披露背景，以及 Capsule 对 agent runtime 风险的定位。([helpnetsecurity.com](https://www.helpnetsecurity.com/2026/04/15/capsule-security-platform/?utm_source=chatgpt.com))