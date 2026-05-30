# HyperFrames

> 来源：https://github.com/heygen-com/hyperframes
> 获取时间：2026-05-30

Write HTML. Render video. Built for agents.

## 项目概要

HyperFrames 是 HeyGen 开源的一个 HTML 转视频渲染框架。将 HTML、CSS、媒体和可搜索动画转换为确定性的 MP4 视频。可通过 CLI 本地使用，也可通过 AI 编码 Agent 调用。

### 核心特点

- HTML 原生：使用 HTML 文件 + data 属性定义视频合成
- Agent 友好：Agent 天然会写 HTML
- 确定性渲染：相同输入始终产生相同输出
- 无构建步骤：index.html 可直接预览
- 适配器式动画：支持 GSAP、CSS、Lottie、Three.js 等
- Apache 2.0 开源许可

### 快速开始

```bash
npx hyperframes init my-video
cd my-video
npx hyperframes preview
npx hyperframes render
```

### 技术栈

- CLI / Core / Engine / Producer
- Catalog（可复用组件库）
- Agent skills
- Studio（浏览器编辑器）
- AWS Lambda 分布式渲染

### 与 Remotion 对比

| 维度 | HyperFrames | Remotion |
|------|-------------|----------|
| 创作方式 | HTML + CSS + 动画 | React 组件 |
| 构建步骤 | 无 | 需要打包器 |
| Agent 协作 | 纯 HTML 文件 | JSX/React 项目 |
| 许可 | Apache 2.0 | 源码可用许可 |
