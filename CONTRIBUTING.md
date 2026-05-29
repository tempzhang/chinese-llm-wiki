# 贡献指南

欢迎你为中文 LLM Wiki 仓库做出贡献！以下是参与方式。

## 如何新增资料

1. 将原始资料放入 `llm-wiki/raw/` 对应子目录：
   - `sources/`：网页文章、Markdown 文件
   - `videos/`：视频文件或视频笔记
   - `pdfs/`：PDF 文档
   - `images/`：截图、图片素材
   - `web-clips/`：网页剪藏内容
   - `transcripts/`：音视频转录文本
2. 确保文件名清晰、可追溯来源。
3. 不要伪造来源链接或作者信息。

## 如何新增 Wiki 页面

1. 确定页面类型（concept / entity / project / workflow / question / comparison / report / decision / example）。
2. 在 `llm-wiki/wiki/` 对应子目录下创建 `.md` 文件。
3. 使用 `llm-wiki/templates/` 中对应的模板。
4. 填写完整的 YAML frontmatter（title、type、status、tags、created、updated、sources、related）。
5. 填写页面正文结构。

## 如何命名页面

- 使用中文标题，文件名与 `title` 保持一致。
- 概念页：`{概念名}.md`
- 实体页：`{实体名}.md`
- 流程页：`{流程名}.md`
- 问题页：`{问题标题}.md`
- 示例：`概念页模板.md`、`RAG与LLM-Wiki对比.md`

## 如何更新索引

运行工具脚本自动更新索引：

```bash
cd llm-wiki/tools
python update_index.py
```

该脚本只更新 `llm-wiki/index.md` 中 `<!-- AUTO_INDEX_START -->` 与 `<!-- AUTO_INDEX_END -->` 之间的内容。

## 如何提交 Pull Request

1. Fork 本仓库。
2. 在本地创建新分支。
3. 提交修改，确保 commit message 清晰。
4. 发起 Pull Request，说明修改内容和原因。

## 如何做健康检查

运行健康检查脚本：

```bash
cd llm-wiki/tools
python wiki_lint.py
```

该脚本会检查：
- 孤立页面（未被任何页面引用）
- 断链（引用了不存在的页面）
- 缺少 frontmatter 的页面
- 缺少 sources 的页面
- 过期页面（status 为 outdated）

## 如何避免编造信息

- 所有知识页面必须标注 `sources`。
- 如果没有来源，明确标注 `sources: []` 并写入「待补充问题」。
- 不允许 AI 凭空编造事实性内容。
- 引用 Karpathy 或其他专家观点时，必须给出原始链接。

## 行为准则

- 保持中文文档质量。
- 尊重他人贡献。
- 讨论聚焦内容本身。