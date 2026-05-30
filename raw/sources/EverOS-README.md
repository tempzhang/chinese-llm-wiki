# EverOS

> 来源：https://github.com/EverMind-AI/EverOS
> 获取时间：2026-05-30

Build, evaluate, and integrate long-term memory for self-evolving agents.

## 项目概要

EverOS 是一个面向自进化 AI Agent 的长期记忆系统统一平台，包含应用、构建和评估三大部分。

### 核心组件

| 组件 | 说明 | 基准成绩 |
|------|------|----------|
| **EverCore** | 自组织记忆操作系统，受生物印记启发 | LoCoMo 93.05%, LongMemEval 83.00% |
| **HyperMem** | 超图分层记忆架构 | LoCoMo 92.73% |
| **EverMemBench** | 三层记忆质量评估基准 | 事实回忆 / 应用推理 / 个性化泛化 |
| **EvoAgentBench** | Agent 自我进化评估 | 成长曲线 / 迁移效率 / 错误规避 |

### 安装方式

```bash
git clone https://github.com/EverMind-AI/EverOS.git
cd methods/EverCore
docker compose up -d
uv sync
# 配置 .env 中的 LLM_API_KEY 和 VECTORIZE_API_KEY
uv run python src/run.py
```

### 与本 Wiki 关联

EverOS 提供了 AI Agent 长期记忆的架构方案，与本 Wiki 中的 [[AI Agent 知识维护]] 和 [[知识编译]] 概念高度相关，可扩展 Agent 的跨会话记忆能力。
