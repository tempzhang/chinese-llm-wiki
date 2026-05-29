# LLM Wiki

## 一句话定义

LLM Wiki 是一种面向 AI Agent 维护的结构化知识编译系统，将原始资料经 AI 消化提炼后编译为可被人类和 LLM 同时理解的结构化页面。

## 它解决什么问题

- **知识碎片化**：普通笔记散落各处，难以形成体系。
- **RAG 局限性**：直接分块检索易丢失上下文，产生幻觉。
- **维护成本高**：传统 Wiki 需要大量人工维护。
- **AI 不可理解**：多数知识库格式对 LLM 不友好。

## LLM Wiki 与 RAG 对比

| 维度 | RAG | LLM Wiki |
|------|-----|----------|
| 核心机制 | 向量检索 + 分块 | 结构化编译 + 索引 |
| 知识质量 | 依赖分块策略 | 经 AI 提炼的页面 |
| 上下文保持 | 容易断裂 | 页面内完整 |
| 交叉引用 | 无 | 双向链接 [[...]] |
| 可审计性 | 低（黑盒分块） | 高（Git diff） |
| 更新方式 | 重新索引 | Agent 增量修改 |
| 虚构风险 | 中高 | 低（来源可追溯） |
| 适合场景 | 大量非结构化文档 | 需要深度理解的知识 |

## 为什么使用 Markdown + Git

1. **纯文本**：任何工具都能读写。
2. **LLM 友好**：Markdown 是 LLM 训练数据的重要组成部分。
3. **版本控制**：每次修改可审查、可回滚。
4. **协作**：GitHub/GitLab 提供协作基础设施。
5. **无锁定**：不会被任何特定工具绑定。

## 标准工作流

```
收集资料 → 放入 raw/ → AI Agent 摄取 → 生成 Wiki 页面 → 更新索引和日志 → Git commit
```

1. 人类或爬虫收集原始资料，放入 `raw/` 对应目录。
2. AI Agent 读取 `raw/` 中的资料，按规则消化提炼。
3. Agent 在 `wiki/` 中创建或更新结构化页面。
4. Agent 更新 `index.md`、`log.md`、交叉链接。
5. 人类审查后提交到 Git。

## 适用场景

- 个人知识库管理
- 项目文档和团队知识库
- 技术研究和竞品分析
- 内容生产和 SEO 研究
- 企业知识管理

## 快速开始

```bash
# 克隆仓库
git clone https://github.com/tempzhang/chinese-llm-wiki.git
cd chinese-llm-wiki

# 查看知识索引
cat llm-wiki/index.md

# 放置新资料
cp your-article.md llm-wiki/raw/sources/

# 让 AI Agent 摄取
# 使用 llm-wiki/prompts/资料摄取提示词.md

# 运行健康检查
cd llm-wiki/tools
python wiki_lint.py
```

## 后续维护规则

- 遵循 `AGENTS.md`（根目录）和 `llm-wiki/AGENTS.md`。
- 每次修改后更新 log 和索引。
- 定期运行健康检查。
- 不要修改 `raw/` 中的原始资料。