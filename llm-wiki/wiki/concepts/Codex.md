---
title: "Codex"
type: "concept"
status: "active"
tags: ["AI", "工具", "OpenAI", "Agent", "CLI"]
created: "2026-05-29"
updated: "2026-05-29"
sources: []
related:
  - "AI工具"
  - "AI Agent 知识维护"
  - "Codex+Obsidian自主进化知识库"
---

# 🤖 Codex

Codex CLI 是 OpenAI 开源的终端编程助手，一个能在本地命令行中自主完成编码任务的 AI Agent。

## 一句话定义

Codex 是一个运行在终端中的 AI 编程代理，能读取代码、执行命令、修改文件，自主完成从需求到实现的全流程。

## 核心能力

- **文件读写**：读取项目文件、应用补丁修改代码
- **命令执行**：在沙箱中运行 shell 命令，支持 PowerShell 和 Bash
- **计划驱动**：通过 `update_plan` 工具制定和追踪多步骤任务
- **MCP 集成**：支持 Model Context Protocol，可接入 Figma、Canva、GitHub、Gmail、Notion 等外部工具
- **插件体系**：通过 plugin 扩展技能、MCP 服务器和应用连接器
- **Skill 系统**：通过 `SKILL.md` 定义领域特定工作流

## 工作模式

- **Default 模式**：直接执行，尽量不打断用户
- **Plan 模式**：先制定方案供用户审核，确认后再执行

## 安全机制

- 沙箱文件系统隔离
- 命令审批策略（never / on-failure / untrusted / on-request）
- 不提交敏感信息

## 仓库协作

通过 `AGENTS.md` 文件，项目维护者可以为 Codex 提供编码规范、项目结构和操作指令，让 AI Agent 按照团队约定工作。

## 与其他工具的关系

- 与 [[AI工具]] 中列出的 DeepSeek、OpenRouter 等互补——Codex 是执行层，这些是模型/API 层
- [[Codex + Obsidian 自主进化知识库（Xuan酱）]] 展示了 Codex 在知识管理场景的应用
- [[AI Agent 知识维护]] 阐述了类似的 Agent 维护知识库理念

## 适用场景

- 代码仓库的自动化维护
- 知识库的结构化管理（如本 Wiki）
- 重复性开发任务的批量处理
- 跨工具工作流编排（设计→代码→PR→通知）

## 待补充问题

- Codex 与其他终端 AI 助手（如 Claude Code、Gemini CLI）的详细对比
