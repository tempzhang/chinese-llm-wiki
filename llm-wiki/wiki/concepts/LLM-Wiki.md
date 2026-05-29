---
title: "LLM Wiki"
type: "concept"
status: "active"
tags: ["核心概念", "LLM", "知识管理"]
created: "2026-05-29"
updated: "2026-05-29"
sources:
  - "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
  - "https://www.youtube.com/watch?v=t4lnadkVy8E"
related:
  - "RAG"
  - "知识编译"
  - "双向链接"
  - "Markdown 知识库"
  - "AI Agent 知识维护"
---

# LLM Wiki

## 一句话定义

LLM Wiki 是由 Andrej Karpathy 提出的一种面向 AI Agent 维护的结构化知识编译系统，不同于传统 RAG 或人工 Wiki。

## 核心要点

- AI Agent（而非人类）是 Wiki 的主要维护者
- 知识经过"编译"而非"索引"——从原始资料提炼为结构化页面
- 使用 Markdown + Git 作为存储和版本控制方式
- 通过 [[双向链接]] 连接相关知识页面
- 完整保留原始资料，所有 derived knowledge 可追溯来源

## 详细说明

### 背景

2025 年初，Andrej Karpathy 分享了他用 LLM 维护个人知识库的实验。他的核心洞察是：与其让 LLM 实时搜索外部知识库（RAG），不如让 LLM 事先消化资料、写成结构化的 Wiki 页面，在需要时直接读取这些页面作为上下文。

### 核心机制

1. **原始资料收集**：从网页、视频、PDF、项目文档等多渠道收集原始资料。
2. **AI Agent 消化**：AI Agent 阅读资料，提取关键信息，判断是否需要新建或更新 Wiki 页面。
3. **编译为 Wiki 页面**：按照固定模板和规则，将知识编写为结构化页面。
4. **索引和交叉链接**：通过 `[[双向链接]]` 和索引文件建立知识网络。
5. **版本控制**：所有变更通过 Git 追踪。

### 与普通笔记的区别

| 维度 | 普通笔记 | LLM Wiki |
|------|---------|----------|
| 创建者 | 人类 | AI Agent + 人类 |
| 结构 | 自由/碎片化 | 模板化、结构化 |
| 链接 | 手动/稀少 | 自动交叉链接 |
| 版本 | 通常无 | Git 全量版本 |
| 可被 LLM 理解 | 一般 | 优秀 |

## 与其他概念的关系

- [[RAG]]：LLM Wiki 是为解决 RAG 局限性而设计的替代方案
- [[知识编译]]：LLM Wiki 的核心工作方式
- [[双向链接]]：LLM Wiki 的链接机制
- [[AI Agent 知识维护]]：LLM Wiki 的维护主体

## 适用场景

- 个人知识库管理
- 项目/团队知识管理
- 技术研究沉淀
- 内容生产的知识基础
- 竞品分析

## 资料来源

- Karpathy's LLM Wiki Gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- 相关视频解读: https://www.youtube.com/watch?v=t4lnadkVy8E

## 待补充问题

- Karpathy 的完整工作流细节
- LLM Wiki 在企业场景的实践案例