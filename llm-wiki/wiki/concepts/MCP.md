---
title: "MCP（Model Context Protocol）"
type: "concept"
status: "active"
tags: ["AI", "协议", "MCP", "Agent", "工具集成"]
created: "2026-05-29"
updated: "2026-05-29"
sources:
  - "https://mcp.so/"
  - "https://mcp.so/zh"
  - "https://www.youtube.com/watch?v=iqnE6jt2lPU"
related:
  - "DeepSeek"
  - "AI工具"
  - "AI Agent 知识维护"
  - "Codex"
  - "AI工具"
  - "AI Agent 知识维护"
  - "Codex"
---

# 🔌 MCP（Model Context Protocol）

MCP 是 Anthropic 提出的开放协议，定义了 AI 模型与外部工具、数据源之间的标准化通信方式。

## 一句话定义

MCP 是 AI 应用的「USB-C 接口」——统一的协议让任何 AI 模型都能接入任何外部工具和数据源。

## 核心概念

- **MCP Server**：对外暴露工具、资源、提示词模板的服务端。例如文件系统访问、数据库查询、API 调用
- **MCP Client**：AI 应用侧，通过统一协议调用 MCP Server 的能力
- **工具（Tools）**：Server 暴露的可调用功能，如 `search`、`read_file`、`send_email`
- **资源（Resources）**：Server 提供的数据上下文，如文档内容、数据库 schema

## 为什么重要

- **统一标准**：不再需要为每个 AI 应用单独开发集成插件
- **模型无关**：任何支持 MCP 的模型都可以使用同一个 MCP Server
- **生态效应**：社区可共享 MCP Server，类似 npm 包管理器

## 典型 MCP Server 示例

- 文件系统 Server：AI 读写本地文件
- GitHub Server：AI 管理 Issues、PR、代码
- 数据库 Server：AI 查询和分析数据
- 浏览器 Server：AI 操控网页

## MCP Server 目录

- [mcp.so](https://mcp.so/) — 社区 MCP Server 目录，中英文支持
- VCPToolBox — 多 Agent 协同的 MCP 管理面板

## 与 Codex 的关系

Codex CLI 内置 MCP 支持，可通过 plugin 机制接入 Figma、GitHub、Gmail、Notion 等 MCP Server，实现跨工具工作流编排。

## 资料来源

- MCP 官方规范
- [mcp.so](https://mcp.so/) MCP Server 目录
- CherryStudio MCP 配置教程

