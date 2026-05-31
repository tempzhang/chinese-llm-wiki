---
title: "Reasonix（DeepSeek-Reasonix）"
type: "concept"
status: "active"
tags: ["AI", "工具", "DeepSeek", "Agent", "CLI", "终端", "编程助手"]
created: "2026-05-30"
updated: "2026-05-30"
sources:
  - "https://github.com/esengine/DeepSeek-Reasonix"
  - "https://esengine.github.io/DeepSeek-Reasonix/"
related:
  - "DeepSeek"
  - "AI工具"
  - "Codex"
  - "AI Agent 知识维护"
---

# Reasonix（DeepSeek-Reasonix）

## 一句话定义

Reasonix 是一个为 DeepSeek 模型深度优化的终端 AI 编程 Agent，围绕前缀缓存稳定性设计，实现超低成本的长时间持续运行。

## 核心特点

- **DeepSeek 原生**：仅支持 DeepSeek，每一层都为字节级前缀缓存调优
- **极致缓存命中**：实际案例 435M tokens 99.82% 缓存命中，仅花费 ~$12
- **三大架构支柱**：
  - Pillar 1 — 缓存优先循环
  - Pillar 2 — 工具调用修复
  - Pillar 3 — 成本控制
- **内置 Web Dashboard**：实时监控 Token、成本、缓存命中率
- **多搜索引擎**：Bing / 百度 / SearXNG / Tavily / Perplexity / Exa 等
- **跨平台**：macOS / Linux / Windows（PowerShell、Git Bash）
- **MIT 开源许可**

## 安装方式

```bash
npm install -g reasonix
reasonix code my-project
```

或短别名：`npm install -g dsnix`

## 常用命令

| 命令 | 用途 |
|------|------|
| `reasonix code [dir]` | 编码 Agent（默认模式） |
| `reasonix chat` | 纯对话（无文件系统工具） |
| `reasonix run "任务"` | 一次性执行 |
| `reasonix doctor` | 健康检查 |
| `reasonix update` | 升级自身 |

## 与本 Wiki 的关联

Reasonix 是 [[DeepSeek]] 生态的核心工具，同为 AI 编程 Agent 类别，与 [[Codex]] 形成对比。可作为本 Wiki 维护的低成本替代 Agent。

## 资料来源

- GitHub: https://github.com/esengine/DeepSeek-Reasonix
- 配置指南: https://esengine.github.io/DeepSeek-Reasonix/configuration.html

## Related Notes
- [[LLM-Wiki]]
- [[RAG]]
- [[MCP]]
- [[INDEX]]
- [[TOPICS]]
