---
title: "AI Agent 框架（Dify / Coze / Hermes / OpenClaw）"
type: "comparison"
status: "active"
tags: ["AI", "Agent", "Dify", "Coze", "Hermes", "OpenClaw", "自动化"]
created: "2026-05-29"
updated: "2026-05-29"
sources:
  - "https://dify.ai/"
  - "https://www.coze.com/"
  - "https://www.youtube.com/watch?v=3JnD31KZGz8"
related:
  - "自动化工具对比（n8n / Zapier / Make / Dify / Coze）"
  - "AI工具"
  - "MCP（Model Context Protocol）"
  - "自动铺货"
---

# 🤖 AI Agent 框架

Dify、Coze、Hermes、OpenClaw 等 AI Agent 框架横向对比。

## 框架速览

| 框架 | 定位 | 开源 | 部署 |
|------|------|------|------|
| **Dify** | LLM 应用开发平台 | ✅ | 自部署 / 云 |
| **Coze** | AI Bot 搭建 + 商店 | ❌ | 仅云端 |
| **Hermes** | 自托管 AI Agent（NAS） | ✅ | 自部署 |
| **OpenClaw** | 自动化采集 + AI 上货 | ❌ | 自部署 |

## 核心差异

- **Dify**：最全面的 LLM 应用平台，支持 RAG、Agent、工作流、对话应用，企业级
- **Coze**：字节跳动出品，Bot 商店 + 插件 + 多平台发布（飞书/微信/Web），上手最快
- **Hermes**：可部署在 NAS 上的 AI Agent，对接微信实现个人助手
- **OpenClaw**：专注电商自动化——采集阿里巴巴产品 + AI 洗稿 + WordPress 自动上货

## 选型建议

| 场景 | 推荐 |
|------|------|
| 构建 LLM 驱动的业务应用 | Dify |
| 快速搭建 Bot 发布多渠道 | Coze |
| NAS 上跑个人 AI 助手 | Hermes |
| 跨境电商自动采集上货 | OpenClaw |

## 与本 Wiki 关系

- [[自动铺货]] 工作流可通过 OpenClaw 实现全自动
- [[自动化工具对比（n8n / Zapier / Make / Dify / Coze）]] 涵盖通用工作流工具
- [[MCP（Model Context Protocol）]] 提供 Agent 与工具的标准通信协议
