---
title: "HyperFrames"
type: "concept"
status: "active"
tags: ["AI", "工具", "视频", "渲染", "HTML", "HeyGen", "开源"]
created: "2026-05-30"
updated: "2026-05-30"
sources:
  - "https://github.com/heygen-com/hyperframes"
  - "https://hyperframes.heygen.com"
related:
  - "AI工具"
---

# HyperFrames

## 一句话定义

HyperFrames 是 HeyGen 开源的一款 HTML 转视频框架，将 HTML、CSS、动画和媒体文件渲染为确定性 MP4 视频，专为 AI Agent 工作流设计。

## 核心特点

- **HTML 原生创作**：视频合成即 HTML 文件 + data 属性，无框架锁定
- **Agent 友好**：AI Agent 天然会写 HTML，CLI 默认非交互式
- **确定性渲染**：相同输入始终产生相同输出，适合 CI/CD
- **无构建步骤**：index.html 可直接在浏览器中预览
- **适配器式动画**：支持 GSAP、CSS、Lottie、Three.js、Anime.js、WAAPI
- **Apache 2.0 开源许可**：无按渲染次数收费

## 技术栈

| 包名 | 作用 |
|------|------|
| `hyperframes` (CLI) | 脚手架、预览、检查、渲染 |
| `@hyperframes/core` | 类型、解析器、生成器、运行时 |
| `@hyperframes/engine` | Puppeteer + FFmpeg 捕获引擎 |
| `@hyperframes/producer` | 完整渲染流水线 |
| `@hyperframes/studio` | 浏览器编辑器 UI |

## 安装要求

- Node.js 22+
- FFmpeg

```bash
npx hyperframes init my-video
npx hyperframes preview
npx hyperframes render
```

## 资料来源

- GitHub: https://github.com/heygen-com/hyperframes
- 文档: https://hyperframes.heygen.com/introduction
