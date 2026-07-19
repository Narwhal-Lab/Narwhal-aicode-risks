# SearchLeak: M365 Copilot Parameter Prompt Injection Data Exfiltration 
> SearchLeak：微软365 Copilot参数提示注入企业数据泄露漏洞

| Field | Value |
|---|---|
| Category | agent-risk |
| Severity | 🔴 Critical |
| AI Tool | Microsoft 365 Copilot |
| Language | TypeScript / Web Frontend |
| Real Incident | ✅ |
| Reproducible | ✅ |
| Disclosed | 2026-06-15 |

## TL;DR
In mid-June 2026, Varonis Threat Labs disclosed CVE-2026-42824 (CVSS 9.0) named SearchLeak. Attackers craft malicious search URLs carrying hidden prompt payloads. After victims click the link, M365 Copilot parses URL parameters as trusted instructions, triggers SSRF and HTML rendering race conditions to silently exfiltrate emails, confidential contracts and internal SharePoint files to attacker-controlled external servers.
2026年6月中旬Varonis威胁实验室披露编号CVE-2026-42824高危漏洞（CVSS 9.0），代号SearchLeak。攻击者构造携带隐藏提示载荷的恶意搜索链接，受害者点击后，365 Copilot会将URL参数识别为可信指令，串联服务端请求伪造、HTML渲染竞态缺陷，静默把邮件、保密合同、企业SharePoint内部文件外泄至攻击者外网服务器。
> Malicious search query parameters are parsed as trusted prompts by M365 Copilot, chaining SSRF and rendering race flaws to leak all user-accessible corporate documents with only one click from victims.

---

## 详细分析 / Full Analysis
### 一、事件概况
Microsoft 365 Copilot是微软面向政企推出的办公AI助手，深度集成Outlook、Word、SharePoint、Teams全套件，依托用户自身权限检索、整理企业内部全部办公文档，是大量集团、上市公司日常办公标配工具。2026年6月15日Varonis正式对外发布完整漏洞分析，微软同步完成云端热修复，漏洞编号CVE-2026-42824。
![详情细节](./assets/NST.png)

漏洞核心链路由三段缺陷串联而成：参数转提示注入、HTML渲染竞态、内置SSRF通道。攻击者仅需生成一段看似正常的Copilot搜索短链接，通过邮件、企业IM、外部社群分发。员工点击链接后无需任何额外操作，Copilot会自动读取该员工权限范围内所有内部资料，并借助内置图片外链通道把文件内容分段外传。
某制造业集团财务部门多名员工收到伪装成“季度报表查询”的恶意Copilot链接，多人点击后，全年财务预算、供应商保密合同、内部成本核算文件批量泄露。攻击者拿到资料后向竞争对手兜售，企业出现大额商业损失，同步触发监管部门数据合规调查。漏洞披露一周内，安全厂商监测到数万条恶意链接分发攻击行为。
![51CTO报道详情](./assets/51CTO.png)

### 二、风险细节及危害
#### （一）漏洞底层成因
1. 参数信任逻辑缺陷：Copilot直接把URL内search搜索参数当作可信用户提示，未做恶意指令过滤，形成参数式提示注入入口；
2. HTML渲染竞态漏洞：AI生成内容渲染模块存在时序漏洞，图片标签可绕过内容安全策略CSP访问外部攻击者域名；
3. 内置SSRF通道：Copilot为图表、图片预览开放内网/外网请求能力，未做出站域名黑名单，可主动向攻击者服务器传输文档文本；
4. 权限继承放大危害：AI完全复用员工Office账号权限，员工能查看的全部机密文件都可被一次性导出。
![漏洞的三链接条](./assets/VARONIS.png)

#### （二）核心风险特征
1. 极低攻击门槛：仅一条网页链接，受害者点击即触发，无需下载附件、填写账号；
2. 全链路静默泄露：无弹窗、无异常告警、无操作日志记录，泄露行为完全隐藏；
3. 权限跟随泄露：攻击者无需盗取员工账号，仅依托AI自带权限即可获取对应层级企业机密；
4. 传统办公防护失效：邮件网关、IM审计仅拦截恶意附件，无法识别带注入参数的正常短链接；
5. 批量规模化攻击：攻击者可批量生成大量伪装链接，定向投放企业内部通讯渠道。
![薄弱边界](./assets/image1.png)

#### （三）实际落地危害
1. 商业机密外泄：财务数据、项目合同、研发方案、客户资料流出，直接造成同业竞争损失；
2. 个人隐私批量泄露：员工往来邮件、私人日程、内部沟通记录被抓取；
3. 合规行政处罚：企业内部敏感信息未经许可外传，违反个人信息保护、数据安全法规；
4. 衍生钓鱼攻击：外泄内部组织架构、员工通讯录后，攻击者针对性发起精准电信钓鱼、供应链诈骗。


### 四、与《AI生成代码在野安全风险研究报告（2025.12）》关联说明
#### 1. 印证报告3.2自动化偏见与AI信任边界缺陷
报告明确提出**自动化偏见**不仅存在开发工具，企业办公AI同样存在权限信任盲区：企业默认官方AI办公工具会严格隔离外部不可信输入，完全信任URL、附件等外部传入参数。本次漏洞中Copilot无校验直接采信链接内指令，企业员工无防备点击陌生AI链接，完美印证报告对办公类AI工具信任风险的预判；同时产品优先提升交互便捷性，省略输入过滤安全逻辑，契合报告“AI产品重体验、轻校验”通用设计短板。

#### 2. 匹配报告5.2 AI专属漏洞分布特征
报告统计AI类高危漏洞集中在提示注入、输入信任缺陷两类，办公大模型因天然继承用户高权限，数据泄露危害等级极高。CVE-2026-42824属于典型参数型间接提示注入漏洞，依托办公AI高权限实现全域文件窃取，完全匹配报告AI漏洞风险分布统计规律。

#### 3. 对应报告6.3人机协同零信任治理要求
报告针对企业AI办公系统提出三条强制管控：外部输入全量过滤、AI操作人工复核、外部链接访问风险预警。本次受害企业均未部署AI链接风险拦截、未对Copilot检索输出做审计，事故直接证明报告办公AI安全管控方案具备落地必要性。

#### 4. 印证报告4.1行业发展演化规律
漏洞曝光后大量集团企业出台规范：禁止点击外部Copilot搜索链接、开启AI访问行为日志、配置外部域名外联黑名单，行业从无限制使用办公AI转向风险前置管控，和报告总结的AI应用从盲目落地到安全共治发展路径完全吻合。

### 五、修复建议
1. 云端补丁升级：微软已完成云端热修复，管理员确认租户M365 Copilot后台补丁推送完成；
2. 员工安全培训：禁止点击外部聊天、陌生邮件内的Copilot搜索类链接；
3. 外联域名管控：Office后台配置外部访问域名黑名单，拦截未知第三方图片、数据接收服务器；
4. AI行为审计：开启Copilot全文档检索、外部资源访问完整日志，定期巡检异常批量文件读取行为；
5. 分层权限管控：最小化员工SharePoint、机密文件夹查看权限，缩小漏洞泄露数据范围。

### 六、参考链接
1. Varonis官方完整漏洞研究报告：https://www.varonis.com/blog/searchleak
2. 51CTO国内深度复现分析：https://www.51cto.com/article/846516.html
3. NVD官方CVE收录页面：https://nvd.nist.gov/vuln/detail/CVE-2026-42824
4. Windows Forum行业综合复盘：https://windowsforum.com/threads/searchleak-cve-2026-42824-copilot-prompt-injection-and-enterprise-data-exfiltration.427327

