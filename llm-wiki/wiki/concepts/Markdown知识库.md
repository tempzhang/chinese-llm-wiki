---
title: "Markdown 知识库"
type: "concept"
status: "active"
tags: ["核心概念", "Markdown", "知识管理"]
created: "2026-05-29"
updated: "2026-05-29"
sources: []
related:
  - "LLM Wiki"
  - "Git 版本化知识库"
  - "双向链接"
---

# Markdown 知识库

## 一句话定义

Markdown 知识库是以 Markdown 格式组织和存储知识内容的系统，因其纯文本、人类可读、LLM 友好的特性成为 AI 时代知识管理的首选格式。

## 核心要点

- Markdown 是纯文本格式，跨平台、跨工具
- LLM 训练数据中包含大量 Markdown，天然友好
- Git 可以对其进行精确的版本控制和 diff
- 支持 `[[双向链接]]`、表格、代码块、Mermaid 图表

## 详细说明

### Markdown 的优势

1. **纯文本**：任何编辑器都能打开，不会被特定工具锁定。
2. **人类可读**：即使不渲染，结构化内容也清晰可见。
3. **LLM 友好**：OpenAI、Anthropic 等模型的训练数据中大量使用 Markdown，理解质量高。
4. **Git 兼容**：纯文本文件可以精确 diff、merge，支持协作。
5. **生态丰富**：Obsidian、Notion、GitHub、VS Code 等都原生支持。

### 在本 Wiki 中的使用

- 所有 Wiki 页面使用 `.md` 后缀
- YAML frontmatter 存储元数据
- ```[[页面标题]]``` 语法实现双向链接
- 表格、代码块用于结构化内容
- Mermaid 图表用于可视化

### Markdown vs 其他格式

| 格式 | 人类可读 | LLM 友好 | Git 兼容 | 富文本 | 离线可用 |
|------|---------|---------|---------|--------|---------|
| Markdown | ✅ | ✅ | ✅ | 部分 | ✅ |
| Notion | ✅ | ❌ | ❌ | ✅ | ❌ |
| Word | ✅ | ❌ | ❌ | ✅ | 部分 |
| HTML | ❌ | 一般 | 一般 | ✅ | ✅ |
| 纯文本 | ✅ | ✅ | ✅ | ❌ | ✅ |

## 与其他概念的关系

- [[LLM Wiki]]：Markdown 是 LLM Wiki 的存储格式
- [[Git 版本化知识库]]：Markdown + Git = 完美的知识库版本控制
- [[双向链接]]：```[[页面标题]]``` 是在 Markdown 中实现双向链接的通用语法

## 适用场景

- 知识库
- 技术文档
- API 文档
- 博客
- 项目文档

## 资料来源

## 待补充问题

- Markdown 扩展语法（GFM、Obsidian 风味）的兼容性