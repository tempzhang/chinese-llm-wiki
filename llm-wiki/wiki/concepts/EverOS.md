---
title: "EverOS（EverMind）"
type: "concept"
status: "active"
tags: ["AI", "记忆", "Agent", "长期记忆", "自进化", "开源"]
created: "2026-05-30"
updated: "2026-05-30"
sources:
  - "https://github.com/EverMind-AI/EverOS"
  - "https://evermind.ai"
  - "https://arxiv.org/abs/2601.02163"
related:
  - "AI Agent 知识维护"
  - "知识编译"
  - "AI工具"
---

# EverOS（EverMind）

## 一句话定义

EverOS 是一个面向自进化 AI Agent 的长期记忆系统统一平台，提供记忆系统的应用、构建和评估三大能力。

## 核心组件

### EverCore

自组织记忆操作系统，受生物印记启发。从对话中提取、结构化和检索长期知识，使 Agent 能记忆、理解和持续进化。

- 基准成绩：LoCoMo 93.05%, LongMemEval 83.00%
- 论文：https://arxiv.org/abs/2601.02163

### HyperMem

基于超图的分层记忆架构，通过超边捕捉高阶关联，按主题/事件/事实三层实现粗到细的对话检索。

- 基准成绩：LoCoMo 92.73%
- 论文：https://arxiv.org/abs/2604.08256

### 评估基准

- **EverMemBench**：三层记忆质量评估（事实回忆 / 应用推理 / 个性化泛化）
- **EvoAgentBench**：Agent 自我进化评估（成长曲线 / 迁移效率 / 错误规避）

## 安装要求

- Python 3.12
- Docker

```bash
git clone https://github.com/EverMind-AI/EverOS.git
cd methods/EverCore
docker compose up -d
uv sync
# 配置 LLM_API_KEY 和 VECTORIZE_API_KEY
uv run python src/run.py
```

## 与本 Wiki 的关联

EverOS 提供了 AI Agent 长期记忆的基础设施方案，与本 Wiki 的 [[AI Agent 知识维护]] 理念高度契合。其记忆系统可扩展 Agent 维护知识库时的跨会话上下文保持能力。

## 资料来源

- GitHub: https://github.com/EverMind-AI/EverOS
- 官网: https://evermind.ai
- 文档: https://docs.evermind.ai

## Related Notes
- [[LLM-Wiki]]
- [[RAG]]
- [[MCP]]
- [[INDEX]]
- [[TOPICS]]
