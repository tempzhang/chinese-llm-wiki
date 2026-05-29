---
title: "中文 LLM Wiki 落地方案"
type: "report"
status: "active"
tags: ["报告", "落地方案", "实践"]
created: "2026-05-29"
updated: "2026-05-29"
sources:
  - "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
related:
  - "LLM Wiki"
  - "Markdown 知识库"
  - "Git 版本化知识库"
---

# 中文 LLM Wiki 落地方案

## 一句话总结

基于 Karpathy 的 LLM Wiki 理念，结合中文知识管理需求，设计了一套完整的本地 Markdown + Git 知识库方案。

## 方案概览

### 技术选型

| 层次 | 选型 | 理由 |
|------|------|------|
| 存储 | Markdown (.md) | 纯文本、LLM 友好、跨平台 |
| 版本控制 | Git | 完整变更历史、免费托管 |
| 远程托管 | GitHub | 全球最大开源平台 |
| AI Agent | Codex / Claude / ChatGPT | 文件读写 + 规则遵守 |
| 前端编辑 | Obsidian（可选） | 双向链接、图谱视图 |
| 搜索 | `wiki_search.py` + `grep` | 本地极速搜索 |
| 自动化 | Python 脚本 + 标准库 | 无外部依赖 |

### 目录结构

```
chinese-llm-wiki/
├── README.md
├── AGENTS.md
├── CONTRIBUTING.md
├── LICENSE
├── .gitignore
└── llm-wiki/
    ├── raw/          # 原始资料（不修改）
    ├── wiki/         # 知识编译层
    ├── templates/    # 页面模板
    ├── tools/        # 自动化工具
    └── prompts/      # AI 提示词
```

## 关键设计决策

1. **全部使用中文**：面向中文用户，所有说明文档和 Wiki 页面使用中文。
2. **文件名可用英文**：因技术限制，代码文件名、命令、路径使用英文。
3. **模板化**：9 种标准页面模板，确保知识结构统一。
4. **Agent 规则化**：通过 AGENTS.md 定义 Agent 行为，无需编程。
5. **工具脚本零依赖**：所有 Python 脚本只使用标准库。

## 落地步骤

### 第一步：搭建仓库

```bash
mkdir chinese-llm-wiki
cd chinese-llm-wiki
git init
# 创建目录结构
# 创建模板和工具
```

### 第二步：配置 Agent

- 根目录 `AGENTS.md`：Agent 总规则
- `llm-wiki/AGENTS.md`：详细维护规则

### 第三步：开始摄取知识

1. 收集资料放入 `raw/`
2. 使用 Agent + `资料摄取提示词.md` 消化
3. Agent 自动生成/更新 Wiki 页面

### 第四步：持续维护

- 每次修改后运行 `wiki_lint.py`
- 定期做健康检查
- Git commit + push

## 适用场景分析

| 场景 | 适用度 | 说明 |
|------|--------|------|
| 个人知识库 | ⭐⭐⭐⭐⭐ | 最核心的场景 |
| 独立站运营知识库 | ⭐⭐⭐⭐ | SEO、内容策略等 |
| 产品资料库 | ⭐⭐⭐⭐ | 功能、竞品、用户反馈 |
| 技术研究 | ⭐⭐⭐⭐⭐ | 论文、博客、视频消化 |
| 竞品分析 | ⭐⭐⭐⭐ | 结构化对比、决策记录 |
| 企业知识管理 | ⭐⭐⭐ | 需要更多协作功能 |

## 风险与局限

- 需要 AI Agent 配合使用（纯人工维护成本高）
- 不适合超大规模（数万页面以上）
- Markdown 对复杂排版支持有限
- 依赖 Agent 的规则遵守能力

## 后续规划

见 `llm-wiki/roadmap.md`。