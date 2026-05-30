# Understand Anything

> 来源：https://github.com/Lum1104/Understand-Anything
> 获取时间：2026-05-30

Turn any codebase, knowledge base, or docs into an interactive knowledge graph you can explore, search, and ask questions about.
Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more.

## 项目概要

Understand Anything 是一个 Claude Code Plugin，通过多 Agent 管道分析项目，构建包含每个文件、函数、类和依赖的知识图谱，并提供交互式仪表盘进行可视化探索。

### 核心功能

- 结构图谱：将代码库渲染为交互式知识图谱
- 业务逻辑分析：将代码映射到实际业务流程
- 知识库分析：支持 Karpathy 模式 LLM Wiki 分析 (`/understand-knowledge`)
- 引导式导览：按依赖顺序自动生成架构导览
- 模糊与语义搜索：按名称或含义搜索
- Diff 影响分析：查看变更影响范围
- 多平台支持：Claude Code / Codex / OpenCode / Cursor / Copilot / Gemini CLI 等

### 技术架构

- Tree-sitter（确定性解析）+ LLM（语义理解）混合架构
- 多 Agent 管道：project-scanner / file-analyzer / architecture-analyzer / tour-builder / graph-reviewer / domain-analyzer
- 支持增量更新
- 支持中文等多语言输出

### 安装方式

Claude Code 插件市场：`/plugin marketplace add Lum1104/Understand-Anything`
Windows 一键安装：`iwr -useb https://raw.githubusercontent.com/Lum1104/Understand-Anything/main/install.ps1 | iex`
