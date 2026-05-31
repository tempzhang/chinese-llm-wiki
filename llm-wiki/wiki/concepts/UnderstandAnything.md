---
title: "Understand Anything"
type: "concept"
status: "active"
tags: ["AI", "工具", "知识图谱", "代码分析", "Claude Code", "Plugin"]
created: "2026-05-30"
updated: "2026-05-30"
sources:
  - "https://github.com/Lum1104/Understand-Anything"
  - "https://understand-anything.com"
related:
  - "AI工具"
  - "LLM Wiki"
  - "知识编译"
  - "MCP（Model Context Protocol）"
---

# Understand Anything

## 一句话定义

Understand Anything 是一个多 AI 编码平台兼容的插件，能将代码库、知识库或文档转换为交互式知识图谱，支持探索、搜索和问答。

## 核心特点

- **多 Agent 分析管道**：5 个专业化 Agent（project-scanner、file-analyzer、architecture-analyzer、tour-builder、graph-reviewer）协同工作
- **Tree-sitter + LLM 混合架构**：确定性解析获取结构事实 + LLM 获取语义理解
- **Karpathy LLM Wiki 支持**：`/understand-knowledge` 命令可直接分析 LLM Wiki，解析 wikilinks 和分类，发现隐式关系
- **增量更新**：仅重新分析变更的文件
- **多平台兼容**：支持 Claude Code、Codex、OpenCode、Cursor、Copilot、Gemini CLI 等 15+ 平台
- **多语言输出**：支持中文、日文、韩文等

## 安装方式

- **Claude Code**：`/plugin marketplace add Lum1104/Understand-Anything`
- **Windows 一键安装**：`iwr -useb https://raw.githubusercontent.com/.../install.ps1 | iex`
- **Codex / OpenCode 等**：`curl -fsSL ... | bash -s codex`

## 与本 Wiki 的关联

Understand Anything 的 `/understand-knowledge` 命令可直接分析本 Wiki（Karpathy 模式 LLM Wiki），将其渲染为可导航的知识图谱。这是与本 Wiki 最直接相关的工具。

## 资料来源

- GitHub: https://github.com/Lum1104/Understand-Anything
- 官网: https://understand-anything.com
- 在线演示: https://understand-anything.com/demo/

## Related Notes
- [[LLM-Wiki]]
- [[RAG]]
- [[MCP]]
- [[INDEX]]
- [[TOPICS]]
