# 🛡️ AI 生成代码在野安全风险研究

[English](README.md) | [中文](README_CN.md)

本仓库收录了团队《AI 生成代码在野安全风险研究》技术报告全文。  

该研究基于真实开源项目与公开漏洞数据，从工程实践视角刻画 AI 生成代码在真实世界中的使用方式与安全风险。

- 📄 报告 PDF： [AI_GenCode_Technical_Capability_Report_CN.pdf](reports/AI_GenCode_Technical_Capability_Report_CN.pdf)

如果这份工作对你有帮助，欢迎 Star 本仓库，方便后续获取后续进一步研究更新。

## 📰 News

> - 发布《AI 生成代码在野安全风险研究v1.0》技术报告
> - 发布《AI Code in the Wild: Measuring Security Risks and Ecosystem Shifts of AI-Generated Code in Modern Software》 arXiv 预定本 

## 📚 概览

随着大语言模型与生成式 AI 的普及，AI 编程工具已深度融入现代软件工程流程，从智能补全、样板生成，走向模块级代码与复杂逻辑实现。AI 正在从“辅助工具”演变为新的代码贡献者，也显著改变了软件供应链的安全边界。

本研究基于两类真实世界数据展开：

- **开源代码仓库历史记录**：分析主流开源项目的提交历史，观察 AI 生成代码在不同语言、不同开发阶段中的使用趋势与演化特点。
- **已披露漏洞及修复提交**：聚焦与 CVE 相关的修复行为，刻画 AI 生成代码在漏洞产生与修复中的实际角色与影响。

## ✨ 核心发现

- **分阶段渗透**：

AI 生成代码在开源生态中经历“爆发式探索 → 理性回调 → 稳定协作”三个阶段，最终更集中于测试、文档、样板代码等高重复、易验证任务。

- **语言栈差异显著**：

Python / JavaScript / TypeScript 等语言渗透率较高；Java / Go 等在样板化场景中使用较多；Rust / C++ 等系统级语言中，开发者明显更为谨慎。

- **漏洞生命周期中的双重身份**：

一部分安全敏感场景中，原本由 AI 生成的代码在修复时被人工实现替换；同时也有比例不低的漏洞修复由 AI 生成代码完成，AI 既可能是漏洞源头，也被用作修复加速器。

- **风险呈模式化特征**：

AI 引入的漏洞集中在输入校验缺失、不安全 API 调用、过时密码学实现等片段级缺陷，严重度分布与人工代码相近，但在 API / Web / 协议相关逻辑上的网络暴露风险更为突出。

- **提出三维一体的缓解框架**：

从安全评测基准、模型本体安全增强、人机协同治理三个维度构建纵深防御路径，强调“开发者对 AI 生成代码安全负最终责任”。

## 📑 报告结构

报告的主要结构如下，便于按需查阅：

1. **概述**
2. **AI 代码生成能力和应用概况**
   - 2.1 核心能力分类  
   - 2.2 主流 AI 代码生成产品与平台  
   - 2.3 小结  
3. **AI 生成代码的风险与挑战**
   - 3.1 技术特性与内在矛盾  
   - 3.2 直接安全风险  
   - 3.3 间接与合规性风险  
   - 3.4 小结  
4. **AI 生成代码趋势与特点**
   - 4.1 时间发展趋势  
   - 4.2 编程语言分布  
   - 4.3 小结  
5. **AI 生成代码的安全风险与漏洞特征**
   - 5.1 漏洞生命周期中 AI 的角色演变  
   - 5.2 AI 引入漏洞的特征画像  
   - 5.3 小结  
6. **风险缓解建议**
   - 6.1 建立多维度的评测基准  
   - 6.2 增强模型本体安全性  
   - 6.3 人机协同治理  
   - 6.4 小结  

## 📎 引用方式

如需在论文、报告或演讲中引用本工作，推荐使用如下格式：

**引用本技术报告：**

```Plain
@techreport{wukong2025_aigencode_report,
  title        = {AI-Generated Code in the Wild: Security Risk Study},
  author       = {Tencent Security Platform Department and Narwhal-Lab},
  year         = {2025},
  institution  = {Tencent Security Platform Department, Narwhal-Lab},
  type         = {Technical Report},
  url          = {https://github.com/Narwhal-Lab/aicode-in-the-wild-security-risk-report}
}
```

**引用本研究相关文章：**

该工作相关的英文文章可参考：

> *In-the-Wild Security Risks of AI-Generated Code*, Tencent Security Platform Department and Narwhal-Lab, 2025. 可在 arXiv 上获取。

[![arXiv](https://img.shields.io/badge/arXiv-2512.18567-b31b1b.svg)](https://arxiv.org/abs/2512.18567)

```Plain
@misc{wang2025aicodewildmeasuring,
      title={AI Code in the Wild: Measuring Security Risks and Ecosystem Shifts of AI-Generated Code in Modern Software}, 
      author={Bin Wang and Wenjie Yu and Yilu Zhong and Hao Yu and Keke Lian and Chaohua Lu and Hongfang Zheng and Dong Zhang and Hui Li},
      year={2025},
      eprint={2512.18567},
      archivePrefix={arXiv},
      primaryClass={cs.SE},
      url={https://arxiv.org/abs/2512.18567}, 
}
```

## 👥 项目组成员

<p>
  <img src="./assets/Narwhal-Lab.png" height="30" style="vertical-align: middle;" alt="Narwhal Lab"/>
  <strong style="margin-left: 8px;">Narwhal Lab</strong>
</p>
<table>
  <tr>
    <td align="center" width="90">
      <a href="https://github.com/TheBinKing">
        <img src="https://avatars.githubusercontent.com/TheBinKing" width="70px;" style="border-radius: 50%;" alt=""/>
      </a>
      <br/>
      <a href="mailto:thebinking66@gmail.com">
        <sub><b>王滨</b></sub>
      </a>
    </td>
    <td align="center" width="90">
      <a href="https://github.com/yumkea">
        <img src="https://avatars.githubusercontent.com/yumkea" width="70px;" style="border-radius: 50%;" alt=""/>
      </a>
      <br/>
      <a href="mailto:uuykea@gmail.com">
        <sub><b>喻文杰</b></sub>
      </a>
    </td>
    <td align="center" width="90">
      <a href="https://github.com/YilZhong">
        <img src="https://avatars.githubusercontent.com/YilZhong" width="70px;" style="border-radius: 50%;" alt=""/>
      </a>
      <br/>
      <a href="mailto:tangaaang@gmail.com">
        <sub><b>钟一路</b></sub>
      </a>
    </td>
    <td align="center" width="90">
      <a href="https://github.com/GioldDiorld">
        <img src="https://avatars.githubusercontent.com/GioldDiorld" width="70px;" style="border-radius: 50%;" alt=""/>
      </a>
      <br/>
      <a href="mailto:g.diorld@gmail.com">
        <sub><b>余昊</b></sub>
      </a>
    </td>
  </tr>
</table>


## 🤝 致谢与反馈

感谢所有参与本研究与报告撰写的成员和提供意见改进的同行。如对研究内容有建议、发现问题或希望交流实践经验，欢迎在本仓库提交 Issue 反馈，如果有多方面合作想法的团队或个人可以email联系:thebinking66@gmail.com

## 📄 开源协议

© 2025 Narwhal Lab。

本项目基于 **CC BY 4.0** 许可协议发布。任何形式的使用或引用均需署名 Narwhal Lab。详细条款见 [LICENSE](./LICENSE)。
