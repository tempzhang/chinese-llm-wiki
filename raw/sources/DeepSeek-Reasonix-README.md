# DeepSeek-Reasonix

> 来源：https://github.com/esengine/DeepSeek-Reasonix
> 获取时间：2026-05-30

A DeepSeek-native AI coding agent for your terminal.
Engineered around prefix-cache stability — so token costs stay low across long sessions, and you can leave it running.

## 项目概要

Reasonix 是一个专为 DeepSeek 模型优化的终端 AI 编程 Agent。围绕 DeepSeek 的前缀缓存特性设计，实现超低成本的长时间运行。

### 核心特点

- DeepSeek 原生：仅支持 DeepSeek，深度优化前缀缓存
- 极致成本控制：99.82% 缓存命中率，435M tokens 仅 ~$12
- 三大支柱架构：缓存优先循环 / 工具调用修复 / 成本控制
- 内置 Web Dashboard
- 可配置搜索引擎（Bing / 百度 / SearXNG / Tavily 等）
- 跨会话持久化
- MIT 开源许可

### 安装方式

```bash
npm install -g reasonix
reasonix code my-project
```

或使用短别名：`npm install -g dsnix`

### 与本 Wiki 关联

Reasonix 是 DeepSeek 生态的重要工具，直接关联到本 Wiki 中的 [[DeepSeek]] 概念页和 [[AI工具]] 页面。
