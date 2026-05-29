# 操作日志

> 按时间倒序记录所有维护操作。

## 2026-05-29 22:15 | 资料摄取 | 批量摄取 4 篇第二大脑/思维工具资料

- 修改文件：
  - `llm-wiki/wiki/reports/12个思维工具命令.md`（新建）
  - `llm-wiki/wiki/reports/AI+Obsidian第二大脑.md`（新建）
  - `llm-wiki/wiki/reports/从0搭建AI第二大脑.md`（新建）
  - `llm-wiki/wiki/reports/Codex+Obsidian自主进化知识库.md`（新建）
  - `llm-wiki/wiki/entities/@internetvin.md`（新建）
  - `llm-wiki/wiki/entities/Martina在进化.md`（新建）
  - `llm-wiki/wiki/entities/Xuan酱.md`（新建）
  - `llm-wiki/index.md`（更新索引）
- 修改原因：将 raw/ 中剩余 4 篇资料摄取为结构化资料摘要，含飞书文档和 3 篇 YouTube 视频笔记
- 资料来源：飞书文档 + 2 个 YouTube 频道
- 后续待办：
  - 补全「12 个思维工具命令」中剩余 9 个命令的详情
  - 从 Bookmarks-Vault 中提取有价值的书签进入 wiki

## 2026-05-29 21:30 | Obsidian 导入 | 导入跨境电商知识库（6 篇笔记）

- 修改文件：
  - `llm-wiki/wiki/projects/建站.md`（新建）
  - `llm-wiki/wiki/projects/跨境电商.md`（新建）
  - `llm-wiki/wiki/workflows/自动SEO.md`（新建）
  - `llm-wiki/wiki/workflows/自动铺货.md`（新建）
  - `llm-wiki/wiki/concepts/AI工具.md`（新建）
  - `llm-wiki/wiki/reports/跨境电商知识库.md`（新建）
  - `llm-wiki/index.md`（更新索引）
- 修改原因：从 `D:\文本文档\obsidian_knowledgehub\` 导入 Obsidian 跨境电商笔记，添加 frontmatter 和交叉链接
- 资料来源：个人知识库笔记
- 后续待办：
  - 可逐步丰富各笔记内容

## 2026-05-29 21:10 | 资料摄取 | 批量摄取 5 篇 X/Twitter 帖子

- 修改文件：
  - `llm-wiki/wiki/reports/YouTube学习频道推荐.md`（新建）
  - `llm-wiki/wiki/reports/YouTube免费教育资源.md`（新建）
  - `llm-wiki/wiki/reports/Mega云存储介绍.md`（新建）
  - `llm-wiki/wiki/reports/暴力美学电影清单.md`（新建）
  - `llm-wiki/wiki/reports/Pinterest副业赚钱方法.md`（新建）
  - `llm-wiki/index.md`（更新索引）
- 修改原因：将 raw/ 中的 5 篇原始资料摄取为结构化资料摘要
- 资料来源：
  - https://x.com/wanerfu/status/1726850656978481253
  - https://x.com/laobaishare/status/1726787957166907813
  - https://x.com/laobaishare/status/1729301420808253943
  - https://x.com/UnicornBitcoin/status/1730114629798695203
  - https://x.com/wanerfu/status/1807932582644138011
- 后续待办：
  - 提取各帖子配图中的详细内容（频道列表、电影清单等）
  - 如内容已过期可删除或归档 raw/ 中的原始文件

- 修改文件：全仓初始化
- 修改原因：基于 Karpathy LLM Wiki 概念建立中文知识管理仓库
- 资料来源：https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- 后续待办：
  - 持续添加实际知识内容
  - 接入 GitHub 远程仓库
  - 配置 Obsidian 打开方式
## 2026-05-29 22:29 | 新建页面 | 创建 Codex 概念页

- 修改文件：
  - llm-wiki/wiki/concepts/Codex.md（新建）
  - llm-wiki/index.md（更新索引）
- 修改原因：新增 Codex CLI 工具介绍页面
- 资料来源：Codex CLI 官方文档及实际使用经验
- 后续待办：
  - 可补充 Codex 与其他终端 AI 助手的对比

## 2026-05-29 22:40 | 仓库合并 | 合并 Obsidian 多仓库为单一结构

- 修改文件：
  - Bookmarks-Vault/ → 整体移入 llm-wiki/raw/bookmarks/（~2900 个书签页面）
  - 第二大脑/ → 删除（仅含 Obsidian 默认模板，无实质内容）
  - 各 vault 内置 .obsidian/ → 清理，统一使用根目录配置
  - llm-wiki/index.md（更新索引）
- 修改原因：仓库中存在三个独立 Obsidian vault，合并为单一结构
- 资料来源：本地仓库
- 后续待办：
  - 可从 aw/bookmarks/ 中按需摄取有价值资料为 Wiki 页面
