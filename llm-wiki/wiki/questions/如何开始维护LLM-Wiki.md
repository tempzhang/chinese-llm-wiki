---
title: "如何开始维护LLM-Wiki"
aliases: []
tags: ["ai", "llm"]
category: "question"
status: "review"
---
﻿---
title: "如何开始维护 LLM Wiki"
type: "question"
status: "active"
tags: ["入门", "指南"]
created: "2026-05-29"
updated: "2026-05-29"
sources: []
related:
  - "LLM Wiki"
  - "资料摄取流程"
  - "中文 LLM Wiki 落地方案"
---

# 如何开始维护 LLM Wiki

## 问题

我想开始使用 LLM Wiki 管理知识，应该从哪里开始？

## 简短回答

1. 克隆仓库到本地
2. 放入第一份资料到 `raw/`
3. 让 AI Agent 按照提示词消化资料
4. 审查 Agent 的产出
5. git commit

## 详细解答

### 准备工作

1. **环境要求**：
   - Python 3.8+
   - Git
   - 一个 AI Agent 工具（Codex、Claude Code、ChatGPT with File Access 等）

2. **获取仓库**：
   ```bash
   git clone https://github.com/tempzhang/chinese-llm-wiki.git
   cd chinese-llm-wiki
   ```

3. **了解结构**：
   - 阅读 `llm-wiki/index.md` 了解知识全貌
   - 阅读 `llm-wiki/AGENTS.md` 了解维护规则

### 第一次使用

1. **收集资料**：
   - 找一篇你想消化的文章或视频
   - 放入 `llm-wiki/raw/sources/` 或其他对应目录

2. **让 Agent 工作**：
   - 使用 `llm-wiki/prompts/资料摄取提示词.md` 作为 Agent 的初始提示
   - Agent 会：
     - 阅读资料
     - 检查现有 Wiki 中是否有相关内容
     - 创建新页面或更新已有页面
     - 更新索引和日志

3. **审查产出**：
   - 检查 Agent 创建的页面内容是否准确
   - 检查交叉链接是否合理
   - 运行 `python tools/wiki_lint.py` 做健康检查

4. **保存**：
   ```bash
   git add .
   git commit -m "摄取: [资料名称]"
   git push
   ```

### 常用命令

```bash
# 搜索知识
cd llm-wiki/tools
python wiki_search.py "<关键词>"

# 健康检查
python wiki_lint.py --verbose

# 更新索引
python update_index.py

# 生成报告
python generate_report.py --stats
```

## 涉及的概念

- [[LLM-Wiki]]：了解什么是 LLM Wiki
- [[资料摄取流程]]：详细的资料消化流程
- [[中文 LLM Wiki 落地方案]]：完整的技术方案

## 常见误区

- **误区 1**："我可以直接手动写 Wiki 页面" — 可以，但推荐让 Agent 先消化资料生成初稿
- **误区 2**："Agent 生成的页面不需要审查" — Agent 可能出错，必须人工审查
- **误区 3**："LLM Wiki 是一次性的" — 它是持续维护的系统，需要定期健康检查

## 进一步阅读

- [[RAG 与 LLM Wiki 对比]]：了解 LLM Wiki 和 RAG 的区别
- [[Karpathy LLM Wiki 中文解读]]：深入理解 Karpathy 的原版理念
- [[新手教程：搭建 Karpathy LLM Wiki 知识库（AI大模型应用开发）]]：视频教程，0 代码搭建

## 资料来源

## Related Notes
- [[LLM-Wiki]]
- [[RAG]]
- [[MCP]]
- [[INDEX]]
- [[TOPICS]]
