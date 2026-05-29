# AI Agent 总规则

你是负责维护本仓库的 AI Agent。以下是必须遵守的全局规则。

## 基本规则

- **默认使用中文输出**：所有可见回复、报告、页面内容均使用中文。
- **代码文件名、命令、路径、配置字段**可使用英文。
- **遵循 KISS 原则**：简单、可维护，不做过度设计。

## 维护前必须做的事

1. 首先阅读 `llm-wiki/index.md`，了解当前知识结构。
2. 再阅读 `llm-wiki/AGENTS.md`，了解详细维护规则。
3. 确认当前 Git 状态，确保工作区干净。

## 资料处理规则

- 新资料必须先进入 `llm-wiki/raw/` 对应子目录。
- 原始资料**不得修改**，只做摄取和链接。
- **不允许编造来源**，所有 knowledge claim 必须有明确出处。
- 没有来源的内容需标注 `sources: []` 并写入「待补充问题」。

## 页面修改规则

- 修改 Wiki 页面后，必须同步更新：
  - `llm-wiki/index.md`（通过 `update_index.py`）
  - `llm-wiki/log.md`（手动记录操作）
  - `llm-wiki/changelog.md`（如有版本级变更）
- 不删除 `raw/` 中的原始资料。
- 修改已有页面时不要改变 frontmatter 中的 `created` 日期。

## 安全规则

- 不提交敏感信息：`.env`、API Key、token、SSH 私钥、数据库密码。
- 执行脚本前确认不会造成破坏性操作。
- 工具脚本优先使用 Python 标准库，减少外部依赖。

## Git 规则

- 每次任务结束后提交，commit message 使用中文。
- 不要 force push。
- 提交前运行 `git status` 确认没有意外文件。

## 工具脚本规则

- 所有工具脚本存放在 `llm-wiki/tools/`。
- 脚本应可独立运行，不相互依赖。
- 优先使用 Python 标准库。
- 需要参数时提供清晰的 `--help`。

## 每次任务结束要求

- 输出中文实施报告。
- 更新 `llm-wiki/log.md`。
- 如有版本级变更，更新 `llm-wiki/changelog.md`。
- 运行 `wiki_lint.py` 确保仓库健康。