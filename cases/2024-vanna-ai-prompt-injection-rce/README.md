# Vanna.AI Prompt Injection Remote Code Execution (2024)
> Vanna.AI 提示注入远程代码执行漏洞

| Field | Value |
|---|---|
| Category | Agent Risks |
| Severity | 🔴 Critical |
| AI Tool | Vanna.AI, Vanna Python library, LLM text-to-SQL application |
| Language | Python |
| Real Incident | ✅ |
| Reproducible | ✅ |
| Disclosed | 2024-05-31 |
| CVE | CVE-2024-5565 |
| CVSS | 9.2 |

## TL;DR
Vanna.AI turned user prompt input into LLM-generated Python visualization code, enabling RCE.
> Vanna.AI 在文本转 SQL 与自动可视化链路中把外部提示转化为可执行 Python 代码，形成提示注入到远程代码执行的漏洞。

---

## 详细分析 / Full Analysis

# Vanna.AI 提示注入远程代码执行漏洞分析：当 text-to-SQL 输出继续进入 Python 可视化执行链

## 基本信息

Vanna.AI 是一个面向数据库分析场景的 Python LLM 库，典型用法是让用户用自然语言提问，由 LLM 生成 SQL，执行查询，并可选地生成 Plotly 可视化代码展示结果。CVE-2024-5565 的核心问题不在 SQL 生成本身，而在 `ask()` 方法默认可视化流程中，用户可控提示影响后续 Python 图表代码生成，最终让恶意输入跨过 LLM 语义边界并进入代码执行边界。

## 摘要

该事件展示了一个典型的集成式提示注入风险：LLM 被嵌入数据库查询和可视化工作流后，外部输入可以影响后续 Python 图表代码生成。攻击者借此绕过应用预设的前置提示和 SQL 检查，使系统执行任意 Python 代码。公开材料的重点在漏洞链与代码执行风险，影响范围应按已披露证据描述。

## 一、事件核验与证据范围

### 证据矩阵

| 来源 | 类型 | 证明内容 | 边界 |
|---|---|---|---|
| JFrog 原始研究 | 主证据 / 技术证据 | Vanna.AI 的 text-to-SQL 与 Plotly 可视化链路可被提示注入转化为代码执行 | 研究报告证明漏洞链，不证明大规模在野利用 |
| NVD: CVE-2024-5565 | 主证据 | CVE、描述、CWE-94、JFrog CVSS 向量、披露时间 | NVD 当前未给出自己的 Base Score |
| GitHub Advisory GHSA-7735-w2jp-gvg6 | 主证据 | 影响包、受影响版本、Critical 9.2、漏洞描述 | 主要确认包版本与评分信息 |
| The Hacker News | 复核证据 | 独立复核 JFrog 研究、CVSS 8.1、攻击路径和厂商加固建议 | 技术细节来自 JFrog，媒体不独立复现漏洞 |
| Vanna.AI Hardening Guide | 生态 / 修复证据 | 官方加固建议，提示可视化链路应沙箱化 | 用于确认治理方向 |

![图1：JFrog 原始研究标题与 CVE-2024-5565 摘要](./assets/1.png)

JFrog 在 2024 年 6 月 27 日公开分析 CVE-2024-5565，明确将其描述为 Vanna.AI 中通过提示注入实现远程代码执行的漏洞。研究指出，Vanna.AI 是 Python text-to-SQL 库，攻击发生在用户输入、LLM 生成 SQL、再生成可视化 Python 代码的组合路径中。([JFrog](https://jfrog.com/blog/prompt-injection-attack-code-execution-in-vanna-ai-cve-2024-5565/))

NVD 记录该漏洞的描述：Vanna 库使用 prompt function 呈现可视化结果，攻击者可通过 prompt injection 修改该流程并运行任意 Python 代码。NVD 还记录该 CVE 由 JFrog 报送，CISA ADP 添加 CWE-94。([NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-5565))

GitHub Advisory Database 将 GHSA-7735-w2jp-gvg6 标为 Critical，CVSS v4 总分 9.2，影响 `pip vanna <= 0.5.5`。该页面明确说明，允许外部输入进入 `ask` 方法且 `visualize=True` 时会导致 RCE。([GitHub Advisory](https://github.com/advisories/GHSA-7735-w2jp-gvg6))

The Hacker News 对该事件做了复核，解释 Vanna 通过 LLM 将自然语言转为 SQL，再用 Plotly 图形库呈现结果；动态生成 Plotly 代码与提示注入结合后，攻击者可提交包含命令执行意图的提示。([The Hacker News](https://thehackernews.com/2024/06/prompt-injection-flaw-in-vanna-ai.html))

### 证据范围

公开证据足以确认 CVE-2024-5565 是一个真实披露并被公开漏洞库收录的 Vanna.AI 漏洞。该漏洞把用户可控提示、LLM 输出和 Python 可视化执行连接起来，风险发生在 AI 应用工作流中。现有材料支持的定性是：这是一次已确认的 LLM 应用集成漏洞，应用没有为模型输出建立足够强的执行控制，导致提示注入越过语义层进入代码执行层。

## 二、系统背景与触发条件

Vanna.AI 的价值在于让业务用户通过自然语言查询数据库。典型调用会把用户问题交给 LLM，生成 SQL，执行 SQL，再生成可视化代码。这个模式在数据分析、BI、内部运营工具中很有吸引力，但它也改变了传统边界：用户输入不再只进入查询构造器，而是可能影响后续代码生成。

![图2：NVD 中 CVE-2024-5565 的漏洞描述和 CWE 信息](./assets/2.png)

典型触发条件是应用把 Vanna 的 `ask()` 能力暴露给外部或低信任用户，同时开启 `visualize` 流程，并让 LLM 生成的 Plotly/Python 代码在缺少沙箱、AST allowlist、进程隔离或人工审批的情况下执行。如果数据库连接、应用主机或运行环境中还存在高权限密钥和网络访问能力，提示注入就可能进一步放大为主机或内网风险。

## 三、攻击链路与处置过程

攻击入口位于用户自然语言问题。攻击者不需要直接提交 Python 文件，而是通过提示诱导模型在可视化代码中写入攻击逻辑。Vanna 的预提示试图约束模型生成合法 SQL 和图表代码，但提示注入可以把用户意图伪装成更高优先级任务或绕过格式约束。

AI 组件是 Vanna.AI 调用的 LLM 生成链路。模型负责把自然语言转为 SQL，也负责在结果展示阶段生成 Plotly 相关 Python 代码。关键权限来自应用运行时：它能访问数据库结果、Python 解释器、本地文件系统、环境变量和网络。

失效点位于模型输出到代码执行之间。系统把 LLM 生成内容视为可信代码；SQL 检查无法覆盖后续 Python 可视化代码；预提示只能提供行为约束，无法替代执行控制；缺少沙箱和最小权限时，代码执行会继承宿主进程能力。

![图3：GitHub Advisory 对受影响版本和 Critical 评分的记录](./assets/3.png)

执行结果是任意 Python 代码运行。根据公开披露，攻击者可让系统执行命令。处置方向应落在降低和隔离代码执行能力上。

## 四、技术根因分析

根因不止于 prompt injection 这个表面现象，而是三层边界叠加失效。

自然语言边界失效：用户输入被设计为业务问题，但 LLM 无法可靠地区分问题内容和控制指令。当用户输入能影响系统后续操作时，它必须被当作不可信程序片段处理。

代码生成边界失效：可视化功能把模型输出转化为 Python 代码。图表代码在工程上常被视为低风险辅助逻辑，但它和其他 Python 代码一样可以访问解释器能力。

运行时边界失效：如果 Python 代码与数据库连接、应用密钥或主机权限处于同一进程或同一权限域内，提示注入就可以升级为系统级执行风险。

这条链路说明，LLM 应用的安全审计不能停留在 prompt 层。凡是模型输出进入 SQL、Shell、Python、浏览器自动化、工作流编排或云 API，都必须用传统安全工程方法重新建模。

## 五、AI 参与方式与风险归因

AI 参与方式明确：Vanna.AI 的核心能力是 LLM text-to-SQL 和可视化代码生成；JFrog、NVD、GitHub Advisory 和媒体报道均把漏洞描述为 prompt injection 导致 Python 代码执行。LLM 生成步骤把自然语言输入连接到后续 Python 可视化执行，是漏洞链中的关键环节。

风险归因集中在应用集成方式：应用把 LLM 输出接入可执行代码路径，默认信任模型输出，并允许外部输入影响这一路径。模型的提示服从性、执行权限、沙箱缺失、输出校验不足和产品默认行为共同构成了漏洞。

## 六、与团队技术报告风险框架的关系

团队技术报告将 AI 代码生成风险归纳为漏洞注入与放大、敏感数据泄露、软件供应链风险、合规风险和安全文化侵蚀。Vanna.AI 案例对应其中的漏洞注入与放大、敏感数据泄露和人机协同治理三类。

它的重点在于 AI 应用运行时生成代码并执行。报告中提到的自动化偏见在这里体现为开发者过度相信预提示和模型输出格式，忽视了模型输出进入 Python 解释器后的真实权限。治理上，应把 LLM 生成代码纳入沙箱、SAST/DAST、数据流审计和权限隔离。

## 七、影响范围与社会后果

直接影响是使用 Vanna.AI 构建 text-to-SQL 或数据库分析应用的组织可能暴露 RCE 风险。如果这类应用连接生产数据库，攻击者不仅可能读取查询结果，还可能借助宿主权限访问环境变量、凭据文件、内网服务或云资源。

![图4：The Hacker News 对 Vanna.AI 提示注入 RCE 的复核报道](./assets/4.png)

社会后果在于 BI 和数据分析工具正在快速接入 LLM。此类工具常被部署在靠近敏感数据的位置，且面向非技术用户开放自然语言查询。一旦自然语言输入与代码执行链路连通，低门槛提示注入会变成高影响系统入侵路径。

## 八、治理建议

治理重点应落在执行控制。面向不可信用户时，应默认关闭自动可视化代码执行，并把 LLM 生成的 SQL 与 Python 分开建模，避免用 SQL 校验替代 Python 执行控制。确需生成图表代码时，应使用 AST allowlist、禁用危险内置函数、隔离解释器和只读文件系统，并让数据库账号、云凭据和运行主机遵循最小权限原则。上线前红队测试也应覆盖 text-to-SQL、图表生成和导出功能，审计日志要记录输入、生成代码、执行结果和调用身份。

## 九、结论

Vanna.AI CVE-2024-5565 的意义在于，它把提示注入从回答污染推进到真实代码执行。该事件证明，只要 LLM 应用把模型输出接入解释器、数据库、图表引擎或自动化工具，传统安全边界就必须前移到模型输出之后、执行之前。安全控制应落在代码执行、权限隔离和审计层，而不能只依赖提示词约束。

## 参考来源

- [JFrog: When Prompts Go Rogue - Vanna.AI CVE-2024-5565](https://jfrog.com/blog/prompt-injection-attack-code-execution-in-vanna-ai-cve-2024-5565/)
- [NVD: CVE-2024-5565](https://nvd.nist.gov/vuln/detail/CVE-2024-5565)
- [GitHub Advisory Database: GHSA-7735-w2jp-gvg6](https://github.com/advisories/GHSA-7735-w2jp-gvg6)
- [The Hacker News: Prompt Injection Flaw in Vanna AI Exposes Databases to RCE Attacks](https://thehackernews.com/2024/06/prompt-injection-flaw-in-vanna-ai.html)
- [Vanna.AI Hardening Guide](https://vanna.ai/docs/hardening-guide/)
