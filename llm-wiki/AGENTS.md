# LLM Wiki Agent 维护规则

这是面向 AI Agent 的详细维护规则，比根目录 `AGENTS.md` 更具体。

## 总原则

你是负责维护 `llm-wiki/` 知识库的 AI Agent。你的目标是：将原始资料消化提炼为高质量、结构化、交叉链接的中文 Wiki 页面。

## AI Agent 阅读顺序

每次启动时，按以下顺序加载上下文：

1. `llm-wiki/index.md` — 了解知识结构全貌
2. `llm-wiki/AGENTS.md` — 本文件，了解维护规则
3. `llm-wiki/log.md` — 了解最近操作
4. `llm-wiki/changelog.md` — 了解版本变化
5. 目标页面的相关页面（通过 `related` 字段追踪）

## 资料摄取规则

### 入口
- 新资料必须先放入 `llm-wiki/raw/`。
- 根据资料类型选择子目录：sources / videos / pdfs / images / web-clips / transcripts。

### 消化步骤
1. 阅读原始资料。
2. 提取关键概念、实体、流程、问题。
3. 对每个关键内容，判断是否需要新建或更新 Wiki 页面。
4. 生成页面时使用对应模板（`llm-wiki/templates/`）。
5. 填写完整的 frontmatter。

### 禁止事项
- 禁止编造来源链接。
- 禁止编造作者、日期。
- 禁止编造不存在的研究或数据。
- 如果资料本身信息不完整，明确标注「待补充」。

## 页面规则

### 页面类型（type）
- `concept`：概念解释
- `entity`：公司/产品/人物/工具
- `project`：具体项目
- `workflow`：操作流程
- `question`：问题及解答
- `comparison`：对比分析
- `report`：综合分析报告
- `decision`：决策记录
- `example`：示例

### 页面状态（status）
- `draft`：草稿，内容不完整
- `active`：活跃，内容可靠
- `outdated`：内容过时，需更新
- `conflict`：存在冲突观点
- `archived`：已归档，不再维护

### frontmatter 规范
```yaml
---
title: "页面标题"
type: "concept"
status: "active"
tags: ["标签1", "标签2"]
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
sources: []
related: []
---
```

## 交叉链接规则

- 使用 `[[页面标题]]` 形式引用其他页面。
- 引用时使用页面标题，不是文件名。
- 被引用页面的 `related` 字段应包含引用方的标题。
- 工具脚本不自动更新 `related`，需要手动维护或通过 Agent 维护。

## 索引规则

- `llm-wiki/index.md` 是知识入口。
- `<!-- AUTO_INDEX_START -->` 和 `<!-- AUTO_INDEX_END -->` 之间的内容由 `update_index.py` 自动生成。
- 不要在自动索引区域内手写内容。
- 自动索引区域外的内容可自由编辑。

## 日志规则

- 每次操作记录到 `llm-wiki/log.md`。
- 格式：
  ```
  ## YYYY-MM-DD HH:mm | 操作类型 | 简短标题
  - 修改文件：
  - 修改原因：
  - 资料来源：
  - 后续待办：
  ```

## 冲突处理规则

- 如果多个来源对同一概念有不同定义，在页面中并列展示。
- 将页面 `status` 设为 `conflict`。
- 在「待补充问题」中说明分歧点。

## 回答用户问题规则

1. 先在本地 Wiki 中搜索（使用 `wiki_search.py`）。
2. 如果 Wiki 中有答案，直接引用页面。
3. 如果 Wiki 中没有，诚实告知，并建议添加相关页面。
4. 不要在没有来源支撑的情况下编造答案。

## Git 规则

- 每次修改后提交，commit message 使用中文。
- 不要 force push。
- 不要提交 `.env`、密钥等敏感信息。

## 安全规则

- 工具脚本优先使用 Python 标准库。
- 不执行来源不明的代码。
- 文件操作限定在仓库目录内。