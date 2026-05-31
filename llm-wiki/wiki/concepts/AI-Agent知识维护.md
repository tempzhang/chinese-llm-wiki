---
title: "AI Agent 知识维护"
type: "concept"
status: "active"
tags: ["核心概念", "AI Agent", "知识管理"]
created: "2026-05-29"
updated: "2026-05-29"
sources:
  - "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
related:
  - "LLM Wiki"
  - "知识编译"
  - "结构化笔记"
---

# AI Agent 知识维护

## 一句话定义

AI Agent 知识维护是指使用 AI Agent（如 Codex、Claude、ChatGPT）作为知识库的主要维护者，负责资料的消化、提炼、页面编写和更新。

## 核心要点

- AI Agent 是知识库的"编辑"，不是"搜索引擎"
- Agent 按照规则（AGENTS.md）自动维护知识库
- 人类负责审核和最终决策
- Agent 不能编造信息，必须标注来源

## 详细说明

### Agent 的角色

在 LLM Wiki 中，AI Agent 承担以下职责：

| 职责 | 说明 |
|------|------|
| 资料摄取 | 阅读 raw/ 中的原始资料，提取关键信息 |
| 页面编写 | 按照模板和规则创建/更新 Wiki 页面 |
| 交叉链接 | 建立和管理 ```[[页面标题]]``` 链接关系 |
| 健康检查 | 定期运行 wiki_lint.py，发现和修复问题 |
| 索引维护 | 更新 index.md 的自动索引区域 |
| 日志记录 | 在 log.md 中记录每次操作 |

### Agent 的工作方式

1. **阅读规则**：先读 AGENTS.md（根目录）和 llm-wiki/AGENTS.md
2. **了解现状**：读 index.md 和 log.md
3. **执行任务**：摄取资料、编写页面、更新索引
4. **自我检查**：运行 wiki_lint.py
5. **提交变更**：git commit

### Agent 的局限性

- 依赖原始资料质量
- 可能产生"格式正确但内容空洞"的页面
- 需要人工审核交叉链接的准确性
- 不能替代人类的判断力

### 与人类分工

- AI Agent：「做重复性、规则明确的工作」——格式化、索引、检查、初稿
- 人类：「做需要判断力的工作」——审核、决策、创意、方向

## 与其他概念的关系

- [[LLM-Wiki]]：AI Agent 是 LLM Wiki 的维护主体
- [[知识编译]]：Agent 执行知识编译流程
- [[结构化笔记]]：Agent 确保输出符合结构化标准

## 适用场景

- 任何需要持续维护的知识库
- 资料量大、人力有限的场景
- 需要格式统一、规则明确的知识管理

## 资料来源

- Karpathy's LLM Wiki Gist

## 待补充问题

- 多 Agent 协作维护的最佳实践

## Related Notes
- [[Codex]]
- [[MCP]]
- [[RAG]]
- [[LLM-Wiki]]
- [[INDEX]]
