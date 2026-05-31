---
title: "为什么选择Markdown和Git"
aliases: []
tags: ["ai", "llm"]
category: "decision"
status: "active"
---
﻿---
title: "为什么选择 Markdown 和 Git"
type: "decision"
status: "active"
tags: ["决策", "技术选型", "Markdown", "Git"]
created: "2026-05-29"
updated: "2026-05-29"
sources:
  - "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
related:
  - "Markdown 知识库"
  - "Git 版本化知识库"
  - "LLM Wiki"
---

# 为什么选择 Markdown 和 Git

## 背景

在设计中文 LLM Wiki 时，需要选择知识存储格式和版本控制方案。候选方案包括：

- 存储：Markdown / Notion / Obsidian 专有格式 / 数据库
- 版本控制：Git / 无 / 云服务自动版本

## 可选方案

### 方案 A：Markdown + Git（最终选择）

- **存储**：纯文本 Markdown 文件
- **版本控制**：Git + GitHub
- **优点**：纯文本、跨平台、LLM 友好、精确版本控制、免费托管
- **缺点**：不支持复杂排版、无实时协作

### 方案 B：Notion

- **存储**：Notion 专有格式
- **版本控制**：Notion 内置历史版本
- **优点**：界面友好、实时协作、数据库功能
- **缺点**：不开放格式、不可离线、LLM 访问困难、被平台锁定

### 方案 C：Obsidian

- **存储**：本地 Markdown 文件（同方案 A）
- **版本控制**：Obsidian Sync 或 Git 插件
- **优点**：本地优先、Markdown 格式、图谱视图
- **缺点**：Obsidian 是编辑工具而非存储方案，可以和方案 A 组合使用

## 最终决策

选择 **Markdown + Git**，并兼容 Obsidian 作为可选的编辑前端。

## 决策依据

1. **LLM 友好性**：LLM 训练数据中包含大量 Markdown，理解和生成质量高。
2. **开放格式**：不被任何平台锁定，随时可迁移。
3. **版本控制**：Git 提供精确的 diff、blame、revert，AI Agent 的每次修改可审查。
4. **零成本**：GitHub 免费提供远程仓库和协作功能。
5. **生态兼容**：VS Code、Obsidian、GitHub、GitLab 都原生支持。
6. **AI Agent 友好**：Agent 可以用标准文件 API 读写 Markdown 文件。

## 影响范围

- 所有 Wiki 页面使用 `.md` 格式
- 页面间链接使用 ```[[页面标题]]``` 语法（Obsidian 兼容 + 可自定义解析）
- 使用 GitHub 作为远程仓库
- 兼容 Obsidian 作为前端编辑器（打开仓库目录即可）

## 后续跟进

- 如果未来需要复杂排版，可考虑 Markdown 扩展（GFM + Mermaid）
- 如果协作需求增加，可启用 GitHub PR 流程

## Related Notes
- [[LLM-Wiki]]
- [[RAG]]
- [[MCP]]
- [[INDEX]]
- [[TOPICS]]
