# 中文 LLM Wiki 仓库

一个基于 Markdown + Git 的中文 LLM（大语言模型）知识管理系统，灵感来源于 [Andrej Karpathy 的 LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)。

## 什么是 LLM Wiki

LLM Wiki 不是普通的笔记系统，也不是传统的 RAG（检索增强生成）管道。它是一个**面向 AI Agent 维护的、结构化、版本化的知识编译系统**。

核心思路：把原始资料（网页、视频、PDF、截图）经过 AI Agent 的消化、提炼、交叉链接，编译成结构化的 Wiki 页面。这些页面既是人类可读的知识文档，也是 LLM 可以直接理解的高质量上下文。

## 它和普通笔记、RAG、文档站的区别

| 特性 | 传统笔记 | RAG | 文档站 | LLM Wiki |
|------|---------|-----|--------|----------|
| 维护者 | 人类 | 自动索引 | 人类 | **AI Agent + 人类** |
| 知识形态 | 碎片化 | 原始分块 | 静态文档 | **编译后的结构化页面** |
| 交叉链接 | 手动 | 无 | 手动 | **自动 + 手动** |
| 版本控制 | 通常无 | 无 | 弱 | **Git 全量版本控制** |
| 可被 LLM 直接理解 | 一般 | 有限 | 一般 | **优秀** |
| 虚构风险 | 低 | 高（分块失真） | 低 | **低（来源可追溯）** |

## 为什么使用 Markdown + Git

- **Markdown**：纯文本、人类可读、LLM 天然友好、跨平台。
- **Git**：完整变更历史、协作友好、免费托管（GitHub/GitLab）、分支管理。
- **组合优势**：每个 Wiki 页面都是一个可 diff 的文本文件，AI Agent 可以直接修改并提交，过程可审查。

## 仓库目录结构

```
chinese-llm-wiki/
├── README.md              # 本文件
├── AGENTS.md              # AI Agent 总规则
├── CONTRIBUTING.md        # 贡献指南
├── LICENSE                # MIT License
├── .gitignore
└── llm-wiki/
    ├── README.md          # LLM Wiki 详细介绍
    ├── AGENTS.md          # Agent 详细规则
    ├── index.md           # 知识索引
    ├── log.md             # 操作日志
    ├── changelog.md       # 版本变更
    ├── glossary.md        # 术语表
    ├── roadmap.md         # 路线图
    ├── raw/               # 原始资料（不修改）
    │   ├── sources/       # 网页文章、Markdown
    │   ├── videos/        # 视频笔记
    │   ├── pdfs/          # PDF 文档
    │   ├── images/        # 截图、图片
    │   ├── web-clips/     # 网页剪藏
    │   └── transcripts/   # 转录文本
    ├── wiki/              # 知识编译层
    │   ├── concepts/      # 概念页
    │   ├── entities/      # 实体页
    │   ├── projects/      # 项目页
    │   ├── workflows/     # 流程页
    │   ├── questions/     # 问题页
    │   ├── comparisons/   # 对比分析
    │   ├── reports/       # 综合报告
    │   ├── decisions/     # 决策记录
    │   └── examples/      # 示例
    ├── templates/         # 页面模板
    ├── tools/             # 自动化工具
    └── prompts/           # AI 提示词
```

## 如何新增资料

1. 将原始资料放入 `llm-wiki/raw/` 对应子目录。
2. 让 AI Agent 运行资料摄取流程（参考 `llm-wiki/prompts/资料摄取提示词.md`）。
3. Agent 会生成一个或多个 Wiki 页面，更新索引和日志。

## 如何让 Codex / Claude / ChatGPT 维护

1. 将本仓库克隆到本地。
2. 在 Codex / Claude Code 中打开仓库目录。
3. 使用 `llm-wiki/prompts/` 中的提示词指导 Agent。
4. Agent 会按照 `AGENTS.md` 和 `llm-wiki/AGENTS.md` 的规则自动维护。

## 如何运行工具脚本

```bash
# 搜索 Wiki
cd llm-wiki/tools
python wiki_search.py "搜索关键词"

# 健康检查
python wiki_lint.py

# 更新索引
python update_index.py

# 摄取新资料
python ingest_source.py path/to/source.md --type article

# 生成报告
python generate_report.py --title "报告标题"
```

## 推荐使用流程

1. **收集资料** → 放入 `raw/`
2. **摄取消化** → AI Agent 读取资料，生成 Wiki 页面
3. **交叉链接** → 更新 related 和索引
4. **健康检查** → 运行 `wiki_lint.py`
5. **提交保存** → Git commit + push
6. **定期维护** → 运行健康检查和周期维护提示词

## 后续扩展方向

- 自动生成 Mermaid 知识图谱
- 接入 Obsidian 作为前端编辑工具
- 添加 GitHub Actions 自动化健康检查
- 支持多语言 Wiki 页面
- 集成向量搜索增强检索