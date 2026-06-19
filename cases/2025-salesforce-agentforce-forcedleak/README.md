# Salesforce Agentforce ForcedLeak Prompt Injection (2025)

> Salesforce Agentforce ForcedLeak 间接提示注入数据外泄事件

| Field         | Value                                           |
| ------------- | ----------------------------------------------- |
| Category      | Agent Risks                                     |
| Severity      | 🔴 Critical                                      |
| AI Tool       | Salesforce Agentforce, Einstein AI, Web-to-Lead |
| Language      | Multiple                                        |
| Real Incident | ✅                                               |
| Reproducible  | ❌                                               |
| Disclosed     | 2025-09-25                                      |
| CVE           | —                                               |
| CVSS          | 9.4, Noma Security assessment                   |

## TL;DR

ForcedLeak used Web-to-Lead prompt injection to make Agentforce leak CRM data.

> ForcedLeak 通过 Salesforce Web-to-Lead 表单植入间接提示注入，使 Agentforce 在处理线索数据时查询 CRM 并通过受信任域名外传敏感信息。

------

## 详细分析 / Full Analysis

# Salesforce Agentforce ForcedLeak 间接提示注入数据外泄事件分析：当 CRM 线索数据变成 Agent 指令

## 基本信息

案例时间：2025 年 7 月发现，2025 年 9 月公开披露
事件对象：Salesforce Agentforce，Web-to-Lead，Einstein AI 相关 Agent 执行链路
漏洞别名：ForcedLeak
漏洞类型：间接提示注入，Agent 上下文污染，CRM 数据外泄，受信任 URL 绕过
影响范围：Noma Security 认为启用 Agentforce 与 Web-to-Lead 的组织可能受到影响，尤其是销售、营销和客户获取流程中会让 AI Agent 处理外部线索数据的组织。Salesforce 在收到报告后实施 Trusted URLs Enforcement，用于限制 Agentforce 与 Einstein AI 生成或调用不受信任外链。([Noma Security](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/))
风险归类：Agent 提示注入风险，CRM 数据外泄风险，业务输入污染，工具调用与外发通道治理不足
案例定位：本案例可作为团队报告中 AI 风险从代码生成扩展到企业 Agent 运行时、业务数据入口和 SaaS 平台自动化工作流的补充案例。

## 摘要

ForcedLeak 是 Noma Labs 在 Salesforce Agentforce 中发现的一条高危漏洞链。Noma 将其评为 CVSS 9.4，核心风险是外部攻击者可通过 Salesforce Web-to-Lead 表单提交恶意线索内容，使 Agentforce 在后续处理该线索时执行隐藏指令，从 CRM 中查询敏感数据，并借助受信任域名完成外传。Noma 在 2025 年 7 月 28 日向 Salesforce 报告该问题，Salesforce 于 9 月 8 日实施 Trusted URLs Enforcement，9 月 25 日公开披露。([Noma Security](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/))

这不是传统的 Web 表单漏洞。攻击者并不需要登录 Salesforce，也不需要突破 CRM 权限模型。攻击入口是一条看起来正常的 Web-to-Lead 线索。恶意指令被写进线索 Description 字段，进入 CRM 数据库后等待员工或业务流程调用 Agentforce 处理。当 Agentforce 读取该线索时，外部输入和系统任务混在同一个上下文里，模型无法稳定区分业务数据和攻击指令，最终把隐藏指令当作当前任务的一部分执行。([Noma Security](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/))

Noma 的 PoC 还利用了一个已经过期但仍在 Salesforce CSP 允许列表中的域名 `my-salesforce-cms.com`。研究者注册该域名后，使用图片预览请求承载外泄数据，使外传流量看起来来自受信任域名。Salesforce 后续重新控制该过期域名，并推出 Trusted URLs Enforcement，防止 Agentforce 和 Einstein AI 将输出发送到未受信任 URL。([Noma Security](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/))

![图1：Noma Security 对 ForcedLeak 的原始披露截图](./assets/1.png)

## 一、事件核验与证据边界

ForcedLeak 的主证据来自 Noma Security 原始研究。Noma 明确写到，该漏洞链可使外部攻击者通过间接提示注入从 Salesforce CRM 工具中外泄敏感数据，并指出问题涉及上下文校验不足、模型过度服从注入指令和 CSP 绕过。该研究还给出公开时间线：2025 年 7 月 28 日发现并报告给 Salesforce，7 月 31 日 Salesforce 确认收到，9 月 8 日实施 Trusted URLs Enforcement，9 月 25 日公开披露。([Noma Security](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/))

The Hacker News 对事件做了独立报道，确认 ForcedLeak 由 Noma Security 发现，CVSS 评分为 9.4，影响启用 Agentforce 与 Web-to-Lead 的组织。报道概括了五步攻击链：攻击者提交带恶意 Description 的 Web-to-Lead 表单，内部员工用 AI 查询线索，Agentforce 执行正常指令和隐藏指令，系统查询 CRM 中敏感线索信息，数据通过攻击者控制的受信任域名以图片请求形式发送出去。([The Hacker News](https://thehackernews.com/2025/09/salesforce-patches-critical-forcedleak.html))

Dark Reading、Salesforce Ben、Simon Willison 等来源从不同角度复核了该事件。Dark Reading 将其描述为 Salesforce Web forms 被 Agentforce autonomous agent 用于外泄 CRM 数据；Salesforce Ben 说明，Noma 称任何启用 Agentforce 与 Web-to-Lead 的组织都可能受到影响，Salesforce 后续发布补丁防止 Agentforce 输出发送到不受信任 URL；Simon Willison 则重点解释了攻击者如何借助 Web-to-Lead 注入内容和过期受信任域名完成图像外传。([Dark Reading](https://www.darkreading.com/vulnerabilities-threats/salesforce-ai-agents-leak-sensitive-data))

![图2：The Hacker News 对 ForcedLeak 攻击链的报道截图](./assets/2.png)



公开资料可以证明 ForcedLeak 是一次已披露、已报告、已修复的 Salesforce Agentforce 漏洞链，也能证明 PoC 级数据外泄路径成立。ForcedLeak 是一条经研究验证并由 Salesforce 修复的企业 Agent 数据外泄漏洞链，社会影响体现在高价值 CRM 数据面临可外泄风险，而不是已经公开确认的大规模客户数据泄露事故。([Noma Security](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/))

## 二、系统背景与触发条件

Salesforce Agentforce 是面向企业业务流程的 Agent 平台。它不是单纯问答机器人，而是在 CRM 环境中读取线索、客户数据、业务记录，并执行多步工作流的自动化组件。Noma 在报告中强调，Agentforce 与传统 prompt-response 系统不同，它具备更强的自主决策能力，会分析上下文、决定动作并执行复杂业务任务。([Noma Security](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/))

Web-to-Lead 是 Salesforce 常见的线索收集入口。外部用户可以通过网站、会议活动页面或营销表单提交潜在线索，这些数据会直接进入 CRM。Noma 的攻击利用了这个业务入口。攻击者不需要进入企业内部，只要向公开 Web-to-Lead 表单提交带有隐藏指令的线索记录，后续当员工使用 Agentforce 处理该线索时，恶意内容就会被 Agent 读入上下文。([Noma Security](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/))

最合适的注入位置是 Description 字段。Noma 对 Web-to-Lead 字段进行分析后认为，First Name、Last Name、Company、Email 等字段长度太短，而 Description 字段可容纳约 42,000 个字符，足以放入复杂的多步指令。这个字段原本用于描述线索需求，却在 Agent 工作流里变成了可影响模型行为的长文本指令容器。([Noma Security](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/))

![图3：Noma Security 对 Web-to-Lead 字段和 Description 注入点的分析截图](./assets/3.png)

这条链路的危险在于输入的身份发生了变化。提交线索时，它是外部用户控制的数据。被 Agentforce 读取时，它变成了 AI 上下文的一部分。被模型处理后，它又可能变成执行指令。传统系统通常把表单输入当数据处理，而 Agent 系统会把数据读成语义。ForcedLeak 的根因就在这条边界上。

## 三、攻击链路与处置过程

攻击从一条 Web-to-Lead 表单开始。攻击者在 Description 字段中写入隐藏指令，伪装成线索备注。线索进入 CRM 后，内部员工以正常方式要求 Agentforce 处理该线索，例如查看某个 lead 并回答其问题。Agentforce 在同一上下文中读取员工任务和攻击者提交的隐藏指令，随后查询 CRM 中的敏感线索数据。([Noma Security](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/))

PoC 中的数据外传通过图片请求完成。恶意指令要求 Agentforce 在回答末尾包含一段 HTML 图片标签，将查询到的邮箱或线索数据拼接进图片 URL 参数。由于目标域名 `my-salesforce-cms.com` 曾在 Salesforce 的 CSP 允许列表中，且已经过期可被购买，研究者注册该域名后便能接收这些请求并记录 URL 参数。([Noma Security](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/))

Noma 将执行流程概括为五步：攻击者提交带恶意 Description 的 Web-to-Lead 表单，内部员工用标准 AI 查询处理该 lead，Agentforce 同时执行正常和恶意指令，系统查询 CRM 中敏感 lead 信息，生成的图片请求把数据发送到攻击者控制服务器。The Hacker News 对这五步也做了复述。([Noma Security](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/))

![图4：Noma Security 中 PoC payload 与 Execution Flow 截图](./assets/4.png)

Salesforce 的修复动作集中在外发通道控制上。Noma 披露时间线显示，Salesforce 在 2025 年 9 月 8 日为 Agentforce 与 Einstein AI 实施 Trusted URLs Enforcement。The Hacker News 引述 Salesforce 的说明称，底层服务会强制执行 Trusted URL allowlist，确保潜在提示注入后不会调用或生成恶意链接，从而阻止敏感数据通过外部请求离开客户系统。([Noma Security](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/))

![图5：Salesforce Help 关于 Trusted URLs Enforcement 的页面截图](./assets/5.png)

## 四、技术根因分析

ForcedLeak 的根因不在单一提示词，而在三层边界同时变软。业务输入没有被当作不可信数据隔离，Agentforce 的上下文校验不足，外发通道又依赖存在历史遗留问题的 CSP 允许列表。每一层单独看都像正常业务能力，组合后形成了数据外泄路径。([Noma Security](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/))

Web-to-Lead 数据进入 CRM 后缺少语义隔离。攻击者提交的 Description 字段本应只是线索备注，但 Agentforce 在处理线索时把它读入任务上下文。Noma 认为，模型没有能力可靠区分可信来源的系统指令与外部数据中的恶意指令，结果就是把隐藏指令当成当前任务执行。([Noma Security](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/))

上下文边界也不够紧。Noma 在初始测试中发现，Agentforce 会回答与 Salesforce 数据无关的一般知识问题，这被视为上下文约束不足的信号。报告列出的关键问题包括 AI model boundaries 不足、user-controlled data 字段清洗不足、CSP 允许列表过宽，以及员工处理线索时的可预测人机交互模式。([Noma Security](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/))

CSP 绕过是外泄闭环的关键。Noma 在 Salesforce 的 CSP 中发现 `*.my-salesforce-cms.com` 被允许，但相关域名已经过期并可购买。攻击者控制该域名后，外发图片请求仍落在看似可信的允许列表范围内。传统 DLP 或 URL 阻断很容易把这类请求视为正常资源加载。([Noma Security](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/))

![图6：Noma Security 对 CSP allowlist 与过期域名的分析截图](./assets/6.png)

这不是一个普通 XSS，也不是传统 SQL 注入。攻击者不让浏览器执行脚本，也不直接打数据库。攻击者把外部业务数据写成 Agent 能理解的任务，把 Agent 变成具备 CRM 访问权限的中介，再让它通过被信任的外发域名把数据带出去。漏洞的形态是语义化的，结果却是实际的数据外泄。

## 五、AI 参与证据与责任边界

AI 参与证据来自事件对象和执行路径。受影响组件是 Salesforce Agentforce，这是 Salesforce 面向企业业务流程的 Agent 平台。攻击依赖 Agentforce 读取外部 Web-to-Lead 数据、理解员工查询、执行隐藏指令、访问 CRM 数据并生成带外发 URL 的输出。Noma、The Hacker News、Dark Reading 和 Salesforce Ben 均将该事件定位为 Agentforce 相关 AI Agent 风险。([Noma Security](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/))

本案例是 Agent 的上下文与工具权限设计让外部输入获得了指令地位。Agentforce 本来拥有访问 CRM 数据的合法权限，员工查询也属于正常业务操作。攻击者污染的是 Agent 处理的数据源，使合法查询触发了隐藏动作。([Noma Security](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/))

公开材料显示，这是一个经研究验证、报告并修复的漏洞链，未公开确认某个客户组织已经发生大规模真实泄露。Salesforce 已经实施 Trusted URLs Enforcement，Noma 也说明 Salesforce 接到报告后调查并发布补救措施。([Noma Security](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/))

外部输入进入 Agent 上下文前需要来源标记和不信任隔离，Agent 访问 CRM 时需要最小权限，生成外链时需要严格外发策略。只依赖模型理解哪些文本是数据、哪些文本是命令，并不足以保护企业数据。

![图7：Dark Reading 对 Agentforce 代理式风险的报道截图](./assets/7.png)

## 六、与团队技术报告风险框架的关系

团队报告讨论 AI 代码生成从局部辅助走向全生命周期工具后，安全边界会从代码片段扩展到流程、供应链和人机协同。ForcedLeak 不是代码补全事故，却很适合补充这条主线。它展示的是企业 Agent 运行时如何把业务输入、内部数据和外发动作连成一条新的攻击路径。

这个案例补充了提示注入风险的现实形态。传统提示注入常被理解为让模型说错话。ForcedLeak 里，提示注入不止改变回答文本，还改变了 Agent 对 CRM 数据的访问和输出。外部表单字段通过业务系统进入 Agent 上下文，Agent 再用自己的权限查询内部数据。它说明提示注入在 Agent 场景中会从语言层进入权限层。

业务团队使用 Agentforce，是为了让 AI 帮忙处理线索、回复客户、整理销售数据。流程越顺，越容易把 Agent 的输出看成受控业务结果。ForcedLeak 说明，自动化并没有减少信任边界，只是把信任边界藏在了上下文拼接、工具调用和外链生成里。

供应链边界也被拉长了。传统 CRM 安全关注表单字段校验、用户权限、报表访问和外部集成。Agentforce 之后，Web-to-Lead 表单、AI 上下文、CRM 查询、图片 URL、CSP allowlist 和 Trusted URLs 都进入同一个安全链路。任何一段默认信任外部输入，后面的 Agent 都可能把它放大成内部数据外泄。

![图8：Salesforce Ben 对 Web-to-Lead 与外部线索数据处理风险的报道截图](./assets/8.png)

## 七、影响范围与社会后果

ForcedLeak 的直接影响是 CRM 数据外泄风险。Noma 列出的潜在数据类型包括客户联系信息、销售管道数据、内部通信、第三方集成数据，以及跨越数月或数年的客户历史交互记录。对使用 Agentforce 处理销售线索、营销活动和客户获取流程的组织来说，这些数据往往属于客户隐私、商业秘密和销售策略。([Noma Security](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/))

The Hacker News 与 Dark Reading 都强调，问题影响的是 Salesforce Agentforce 这类企业 Agent 平台，而不是普通聊天机器人。它们连接 CRM 和业务流程，掌握的数据更结构化，权限也更接近实际业务操作。攻击者无需登录系统，只需要把恶意内容放进会被 Agent 处理的外部数据源里。([The Hacker News](https://thehackernews.com/2025/09/salesforce-patches-critical-forcedleak.html))

影响还体现在隐蔽性上。恶意线索可以先进入数据库，等待员工日后用 Agentforce 查询。Noma 报告认为，time-delayed attacks 可能在常规员工交互中被触发，这会让检测和溯源变难。即使企业后来发现外发请求，也要回头排查是哪条历史 lead 数据污染了 Agent 上下文。([Noma Security](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/))

这起事件没有公开固定金额损失，也没有公开命名客户泄露名单。它的社会后果更接近警报：当企业把 Agent 接入 CRM、工单、线索和客户记录时，任何外部业务输入都可能成为延迟触发的提示注入载体。只要 Agent 同时拥有内部数据访问和外部输出能力，数据外泄路径就会变得比传统表单漏洞更短。

## 八、治理建议

治理重点不应停在关闭 Web-to-Lead 或停用 Agentforce。更现实的做法，是把外部业务输入、Agent 上下文和外发通道拆成不同安全层。Web-to-Lead、客服表单、工单描述、客户邮件和会议报名字段，都应作为不可信输入进入 Agent 环境。

Agent 处理外部数据前，需要做输入净化和来源标记。外部字段不能直接与系统指令、员工任务和工具调用参数混在一起。即便模型看到这些数据，也应明确知道它们只是待处理记录，不是可执行指令。Noma 建议审计已有 lead 数据，查找异常指令或格式，实施严格输入验证，并对不可信来源进行清洗。([Noma Security](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/))

CRM 查询权限也要收窄。Agent 不应因为处理一个 lead，就能查询全部 lead 邮箱、销售管道或历史交互。面向外部输入触发的 Agent，应限制可访问对象、字段和行级范围。可以回答当前 lead 的信息，不应汇总其他客户数据。这个边界比提示词规则更可靠。

外发通道需要运行时控制。Salesforce 的 Trusted URLs Enforcement 是一个直接修复方向，它把 Agent 可生成或调用的 URL 限制在可信列表中。类似平台还应增加外发前审计、敏感字段检测、组织外域阻断和异常图片 URL 监控。外链不是普通展示元素，在 Agent 场景中可能就是数据通道。([Salesforce](https://help.salesforce.com/s/articleView?id=005135034&language=en_US&type=1&utm_source=chatgpt.com))

高风险 Agent 需要运行时审计。企业应记录 Agent 读取了哪些外部输入、查询了哪些 CRM 对象、生成了哪些 URL、是否触发外发请求。Noma 在治理建议中强调 AI agent inventory、AI Bill of Materials、tool invocation 追踪和运行时控制。([Noma Security](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/))

## 九、结论

ForcedLeak 是企业 Agent 风险从理论进入业务流程的一个清晰样本。攻击者没有拿到 Salesforce 账号，也没有直接突破 CRM 数据库。攻击入口只是一条 Web-to-Lead 表单。恶意指令被存进 CRM，等到员工用 Agentforce 处理该 lead 时，它被重新解释成任务指令，并借助受信任域名把 CRM 数据带出系统。([Noma Security](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/))

该事件的价值在于说明企业 Agent 的安全边界已经不同于传统 SaaS。外部数据会进入上下文，Agent 会调用内部数据，输出可能触发网络请求。旧的表单校验、CSP 和 URL allowlist 如果没有面向 Agent 语义重新设计，就会留下新的组合型漏洞。

## 参考来源

1. Noma Security，ForcedLeak: AI Agent Risks Exposed in Salesforce Agentforce。用于核验漏洞名称、CVSS 9.4、攻击路径、Web-to-Lead 入口、CSP 绕过、受影响范围、披露时间线和治理建议。([Noma Security](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/))
2. The Hacker News，Salesforce Patches Critical ForcedLeak Bug Exposing CRM Data via AI Prompt Injection。用于核验第三方媒体复核、五步攻击链、Trusted URL allowlist 修复和 Salesforce 相关说明。([The Hacker News](https://thehackernews.com/2025/09/salesforce-patches-critical-forcedleak.html))
3. Dark Reading，Salesforce AI Agents Forced to Leak Sensitive Data。用于核验 Agentforce 作为 autonomous agent 平台、CRM 数据外泄风险和 CVSS 9.4 影响判断。([Dark Reading](https://www.darkreading.com/vulnerabilities-threats/salesforce-ai-agents-leak-sensitive-data))
4. Salesforce Help，Changes to Default Allowlist for Agentforce。用于核验 Salesforce 于 2025 年 9 月 8 日开始执行 Agentforce 与 Einstein AI Trusted URL allowlist。([Salesforce](https://help.salesforce.com/s/articleView?id=005135034&language=en_US&type=1&utm_source=chatgpt.com))
5. Salesforce Ben，Agentforce Web-to-Lead Vulnerability Exposed。用于核验 Web-to-Lead 业务场景、外部 lead 数据进入 CRM，以及 Salesforce 后续补丁防止输出发送到不受信任 URL。([Salesforce Ben](https://www.salesforceben.com/agentforce-web-to-lead-vulnerability-exposed-could-you-be-impacted/))
6. Simon Willison，AI Agent Risks Exposed in Salesforce Agentforce。用于补充攻击 payload、过期受信任域名和图片 URL 外泄机制的独立技术解读。([Simon Willison’s Weblog](https://simonwillison.net/2025/Sep/26/agentforce/))