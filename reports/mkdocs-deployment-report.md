# MkDocs Deployment Report

## 新增与更新文件
- mkdocs.yml
- .github/workflows/deploy.yml
- docs/index.md
- docs/robots.txt
- docs/INDEX.md
- docs/TOPICS.md
- docs/ROADMAP.md
- docs/KNOWLEDGE_GRAPH.md
- docs/Knowledge-Hub/*
- docs/MOCs/*
- docs/Learning-Paths/*
- docs/Playbooks/*
- docs/Knowledge/*
- reports/mkdocs-readiness.md

## 导航结构
- Home
- Getting Started（START HERE / Quick Links / Use Cases）
- Knowledge（Core Topics / Models / Agent / MCP / RAG）
- Learning Paths
- Playbooks
- Knowledge Graph
- Roadmap

## 插件与主题
- Theme: Material for MkDocs
- Plugins:
  - search
  - awesome-pages
  - git-revision-date-localized-plugin
  - minify-plugin
  - redirects
- Features:
  - search
  - dark mode / light mode
  - navigation.instant
  - navigation.tabs
  - navigation.sections
  - content.code.copy
  - content.action.edit

## GitHub Actions 配置
- Workflow: .github/workflows/deploy.yml
- Trigger: push 到 main
- Steps:
  1) 安装依赖
  2) mkdocs build --strict
  3) mkdocs gh-deploy --force

## SEO 配置
- site_name: Chinese LLM Wiki
- site_description: Open Source AI Knowledge Hub
- site_url: https://tempzhang.github.io/chinese-llm-wiki/
- robots: docs/robots.txt
- social preview: GitHub repo social link
- sitemap: 由 MkDocs 基于 site_url 生成

## 本地验证
- 命令: mkdocs build
- 结果: 构建成功（无错误）
- 说明: 存在历史文档内部链接警告（来自既有 Markdown 相对路径），不影响本次网站框架部署。

## GitHub Pages 地址
- https://tempzhang.github.io/chinese-llm-wiki/
