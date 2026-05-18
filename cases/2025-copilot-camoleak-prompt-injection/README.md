# GitHub Copilot CamoLeak Prompt Injection & Data Exfiltration Vulnerability (2025)
> GitHub Copilot CamoLeak 提示词注入与数据外发漏洞

| Field | Value |
|---|---|
| Category | Hallucination & Supply Chain |
| Severity | 🔴 Critical |
| AI Tool | GitHub Copilot Chat |
| Language | Multiple |
| Real Incident | ✅ |
| Reproducible | ❌ |
| Disclosed | 2025-10 |
| CVE | CVE-2025-59145 |
| CVSS | 9.6 |

## TL;DR
Hidden prompt injection in PR/issue descriptions tricks GitHub Copilot Chat into silently scanning, stealing, and exfiltrating source code and secrets via image rendering.
> 攻击者通过 PR/Issue 中的隐藏提示词注入，操控 GitHub Copilot Chat 静默扫描、窃取并外发源代码与密钥。

---

## 详细分析 / Full Analysis

## 基础信息
- **发生/公开时间**：官方修复时间：2025-08/ 正式披露时间：2025-10
- **风险类型**：敏感数据泄露 / 提示词注入 / 供应链安全
- **影响范围**：使用 GitHub Copilot Chat 的开发者与企业，直接威胁私有代码仓库、配置文件与密钥资产安全
- **严重等级**：致命（CVE-2025-59145，CVSS 评分 9.6）

## 一、事件概述
2025 年 10 月，网络安全界披露了一个针对 GitHub Copilot Chat 的高危安全漏洞（被研究团队命名为“CamoLeak”）。该漏洞允许恶意攻击者在受害者完全不知情的情况下，静默窃取其本地开发环境及私有代码仓库中的核心源代码、API 密钥以及其他敏感机密文件。

攻击者通过在 Pull Request 或 Issue 描述中植入隐藏指令，当开发者在 IDE 中查看相关内容时，Copilot Chat 会自动读取并执行恶意逻辑，在无提示、无交互、无异常行为的状态下，扫描本地项目代码、提取密钥与敏感配置，并通过伪装的网络请求将数据外发。

整个攻击不依赖木马、不提升权限、不触发终端安全软件告警，仅通过 IDE 内置 AI 助手的默认权限即可完成完整窃取链条。

在NVD的国家脆弱性数据库中有详细记录CVE-2025-59145该事件的详细情况：
![CVE-2025-59145 Detail](./assets/image1.png)

## 二、风险细节
1. **AI工具**：GitHub Copilot Chat
2. **风险根因**：
    - 存在间接提示词注入缺陷，AI 无法区分用户主动指令与外部不可信内容
    - IDE 对 AI 插件授权过高，未做权限隔离与沙箱限制
    - 开发工具与开发者均对 AI 输出 / 输入存在过度信任，未做安全校验
3. **漏洞表现**：
   - **自动化隐蔽检索**：注入的隐藏恶意提示词会直接越过人类开发者的视线，命令 Copilot 自动扫描受害者当前打开的整个工作区及本地项目文件，重点搜刮包含 `AWS_SECRET_ACCESS_KEY`、`JWT_SECRET` 或密码等敏感字符串。
   - **利用渲染机制外传数据**：在获取敏感信息后，Copilot 会在提示词的操控下将数据进行 Base16 编码，并将其悄悄拼接在预签名的恶意图像 URL 路径中。当 Copilot 试图在 IDE 界面中为用户渲染这些图像时，实际上就通过 GitHub 自身的基础设施将敏感机密数据异步外发到了攻击者的接收服务器上，整个过程无权限申请、无弹窗提醒、无操作日志，攻击行为高度隐蔽
   ![NPM生态系统的协调供应链攻击](./assets/image2.png)
4. **影响结果**：在现有的集成开发环境设计中，AI 插件往往无缝继承了当前登录用户的同等文件系统与网络访问权限。此漏洞证实，攻击者无需在受害者机器上运行任何传统意义上的木马脚本或恶意可执行文件，仅靠操纵受信任的 AI 编程助手，就能在静默状态下完美完成商业机密盗取，使传统的终端防护完全失效。从而导致企业核心源代码、API 密钥、云平台凭证、数据库配置等资产可被直接窃取，并且这种攻击可批量、自动化实施，对企业研发资产构成持续性威胁。

## 三、关联报告风险点
本案例是《AI生成代码在野安全风险研究报告》多项核心风险的真实攻防验证，与报告章节深度对应：

1. **第 3 章 3.2 节 直接安全风险：交互侧数据泄露**
报告明确提出，AI 编码工具的上下文交互过程存在天然数据泄露风险，外部不可信内容进入提示词后，可直接导致敏感数据越界。CamoLeak 正是利用这一设计缺陷，将 “被动泄露” 升级为 “主动窃取”，把 AI 上下文通道转化为数据外发后门，完全验证报告中 “交互侧是最高危泄露面” 的判断。

2. **第 3 章 3.3 节 安全文化侵蚀：自动化偏见**
报告指出，自动化偏见不仅存在于开发者行为中，更会渗透到工具架构设计。本案例中，IDE 默认赋予 AI 插件完整文件访问与网络访问权限，开发者在代码审查中忽略隐藏指令，完全信任 AI 处理结果，双重信任缺失使攻击可在正常研发流程中静默完成，与报告对 “自动化偏见导致安全防线失效” 的分析完全一致。

3. **第 5 章 5.2 节 AI 引入漏洞的特征分布：攻击面网络化**
报告强调，AI 相关漏洞具备跨域、链式、网络化特征，风险分布于工具、平台、流程、人员多个节点。CamoLeak 不依赖单一代码缺陷，而是通过 “外部输入污染 → AI 上下文接管 → IDE 权限滥用 → 数据隐蔽外发” 形成完整攻击链，风险贯穿 AI 工具、开发环境、代码平台与企业边界，属于典型的网络化攻击面，与传统代码漏洞存在本质区别

4. **第 6 章 6.3 节 人机协同治理：零信任机制**
报告将零信任定位为 AI 开发安全的核心治理策略，要求对所有 AI 输入 / 输出执行默认不信任、强制校验、权限最小化。CamoLeak 之所以可被利用，正是因为开发环境未落实零信任：AI 可无授权读取文件、无校验执行外发、无审核处理外部输入。案例结果直接证明，缺失零信任机制会使 AI 工具成为企业最薄弱的安全入口，印证报告治理框架的必要性与紧迫性。

## 四、修复与处置
1. **紧急修复措施**：GitHub 官方在收到漏洞报告后紧急发布了云端热补丁，通过完全禁用 Copilot Chat 在渲染响应结果时的外部图像自动加载与渲染功能，从物理层切断了利用预签名图片外传数据的隐蔽通道。
![GitHub 相关措施](./assets/image.png)

2. **长效治理报告建议=**：
   - **增强模型内在安全**：模型厂商应结合约束解码（Constrained Decoding）与上下文隔离技术，在底层逻辑上严格区分“用户合法的输入指令”与“外部摄取的不可信数据（Data vs. Code）”，防止间接提示词注入。
   - **人机协同治理**：企业必须重塑端点安全规范，在 IDE 边界引入严厉的零信任访问控制，禁止 AI 插件在缺乏明确人工授权的情况下访问工作区以外的敏感系统配置文件（如 `.env`），并在企业网关侧对 AI 组件发起的异常外发流量进行实时审计与强行拦截。


![BlackFog CamoLeak Report](./assets/image3.png)

## 五、参考来源
1. BlackFog Security: CamoLeak – How GitHub Copilot Became an Exfiltration Channel
https://www.blackfog.com/camoleak-how-github-copilot-became-an-exfiltration-channel/
2. NVD: CVE-2025-59145 Detail
https://nvd.nist.gov/vuln/detail/CVE-2025-59145
3. 19 npm Packages Compromised in Major Supply-Chain Attack 
https://www.ox.security/blog/npm-packages-compromised
4. color-name@2.0.1 contains malware after npm account takeover 
https://github.com/colorjs/color-name/security/advisories/GHSA-5fvm-p68v-5wmh