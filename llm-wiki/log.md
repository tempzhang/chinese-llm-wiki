# 操作日志

> 按时间倒序记录所有维护操作。

## 2026-05-30 20:00 | 优化 | 版本 v0.3.0：术语表扩展 + GitHub Actions + 路线图更新

- 修改文件：
  - `llm-wiki/glossary.md`（5 → 34 条目，覆盖全部核心概念和工具）
  - `llm-wiki/roadmap.md`（标记 v0.2.0 完成，新增 v0.3.0/v0.4.0 规划）
  - `llm-wiki/wiki/00-总览.md`（更新版本号和统计信息）
  - `llm-wiki/changelog.md`（新增 v0.3.0）
  - `llm-wiki/index.md`（自动索引更新）
  - `.github/workflows/wiki-health.yml`（新建，CI 自动健康检查）
- 修改原因：对齐 road map 与实际状态，完善术语表，添加 CI 基础设施
- 后续待办：
  - 摄取 raw/ 中的新手教程 YouTube 资料
  - 从 raw/bookmarks/ 按需摄取分类书签

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

## 2026-05-29 22:47 | 页面创建 | 从书签摄取：MCP 概念、AI工具扩充、自动化工具对比

- 修改文件：
  - llm-wiki/wiki/concepts/MCP.md（新建）
  - llm-wiki/wiki/concepts/AI工具.md（扩充）
  - llm-wiki/wiki/comparisons/自动化工具对比.md（新建）
  - llm-wiki/index.md（更新索引）
- 修改原因：从 raw/bookmarks/ 中提取 AI/Agent/MCP 相关书签，消化为结构化 Wiki 页面
- 资料来源：
  - raw/bookmarks/01_AI/（AI 工具书签）
  - raw/bookmarks/02_Agents/（自动化工具书签）
  - raw/bookmarks/03_MCP/（MCP 协议书签）
- 后续待办：
  - 可继续从其他书签分类（DeepSeek、WordPress、SEO 等）中摄取

## 2026-05-29 22:50 | 页面创建 | 第二批书签摄取：DeepSeek、SEO工具、AI Agent 框架、建站/跨境电商扩充

- 修改文件：
  - llm-wiki/wiki/concepts/DeepSeek.md（新建）
  - llm-wiki/wiki/concepts/SEO工具.md（新建）
  - llm-wiki/wiki/comparisons/AI-Agent框架.md（新建）
  - llm-wiki/wiki/projects/建站.md（扩充）
  - llm-wiki/wiki/projects/跨境电商.md（扩充）
  - llm-wiki/index.md（更新索引）
- 修改原因：从 raw/bookmarks/ 提取第二批书签，消化为 Wiki 页面
- 资料来源：
  - raw/bookmarks/04_DeepSeek/
  - raw/bookmarks/10_SEO/
  - raw/bookmarks/05_Hermes/ + 06_OpenClaw/
  - raw/bookmarks/20_Programming/（建站相关）
- 后续待办：
  - 可继续从 WordPress、WooCommerce、Docker、NAS 等分类中摄取

## 2026-05-29 22:50 | 页面创建 | 第三批书签摄取：WordPress、NAS与自建服务

- 修改文件：
  - llm-wiki/wiki/concepts/WordPress.md（新建）
  - llm-wiki/wiki/concepts/NAS与自建服务.md（新建）
  - llm-wiki/index.md（更新索引）
- 修改原因：从 raw/bookmarks/ 继续摄取 WordPress 和 NAS 相关书签
- 资料来源：
  - raw/bookmarks/07_WordPress/
  - raw/bookmarks/17_NAS/
  - raw/bookmarks/18_Docker/
- 后续待办：
  - 视频学习（21_VideoLearning，506 个书签）可单独消化
  - 跨境工具（11_CrossBorder，145 个）可扩充

## 2026-05-29 22:51 | 页面创建 | 第四批书签摄取：跨境支付、TikTok电商、亚马逊运营

- 修改文件：
  - llm-wiki/wiki/concepts/跨境支付.md（新建）
  - llm-wiki/wiki/concepts/TikTok电商.md（新建）
  - llm-wiki/wiki/concepts/亚马逊运营.md（新建）
  - llm-wiki/index.md（更新索引）
- 修改原因：从 raw/bookmarks/ 继续摄取支付、TikTok、Amazon 相关书签
- 资料来源：
  - raw/bookmarks/14_Payment/
  - raw/bookmarks/12_TikTok/
  - raw/bookmarks/13_Amazon/
- 后续待办：
  - 继续 VideoLearning、Tools 等分类

## 2026-05-29 22:52 | 页面创建 | 第五批：Docker速查

- 修改文件：
  - llm-wiki/wiki/concepts/Docker速查.md（新建）
  - llm-wiki/index.md（更新索引）
- 修改原因：从 raw/bookmarks/18_Docker/ 摄取
- 资料来源：raw/bookmarks/18_Docker/

## 2026-05-30 08:27 | 页面创建 | 第六批书签摄取：OpenWRT软路由、工具导航站

- 修改文件：
  - llm-wiki/wiki/concepts/OpenWRT与软路由.md（新建）
  - llm-wiki/wiki/concepts/工具导航站.md（新建）
  - llm-wiki/index.md（更新索引）
- 修改原因：从 raw/bookmarks/16_OpenWRT/ 和 22_Tools/ 摄取
- 资料来源：raw/bookmarks/16_OpenWRT/, raw/bookmarks/22_Tools/

## 2026-05-30 08:27 | 页面创建 | 第七批：跨境工具

- 修改文件：
  - llm-wiki/wiki/concepts/跨境工具.md（新建）
  - llm-wiki/index.md（更新索引）
- 修改原因：从 raw/bookmarks/11_CrossBorder/ 摄取
- 资料来源：raw/bookmarks/11_CrossBorder/

## 2026-05-30 08:48 | 交叉链接 + 页面扩充 + 仓库清理

- 修改文件：
  - 多个页面交叉链接：AI工具、跨境电商、建站、自动SEO、NAS与自建服务、SEO工具、MCP
  - llm-wiki/wiki/workflows/自动铺货.md（扩充）
  - 清理根目录残留文件（未命名.md、YouTube 学习频道推荐.md）
  - 移动 build_vault.py、gen_vault.py → llm-wiki/tools/
  - llm-wiki/index.md（更新索引）
- 修改原因：减少孤立页面至零、扩充薄页面、清理仓库根目录

## 2026-05-30 08:49 | 页面扩充 | 跨境电商知识库枢纽页重写

- 修改文件：
  - llm-wiki/wiki/reports/跨境电商知识库.md（重写为知识枢纽）
  - llm-wiki/index.md（更新索引）
- 修改原因：将薄页面升级为全面的知识导航枢纽

## 2026-05-30 11:01 | 页面扩充 | 扩充实体页 + 更新 changelog

- 修改文件：
  - llm-wiki/wiki/entities/@wanerfu.md（扩充）
  - llm-wiki/wiki/entities/@laobaishare.md（扩充）
  - llm-wiki/wiki/entities/@UnicornBitcoin.md（扩充）
  - llm-wiki/wiki/entities/@internetvin.md（扩充）
  - llm-wiki/wiki/entities/Martina在进化.md（扩充）
  - llm-wiki/wiki/entities/Xuan酱.md（扩充）
  - llm-wiki/changelog.md（新增 v0.2.0）
  - llm-wiki/index.md（更新索引）
- 修改原因：实体页过于单薄，补充分享领域和交叉引用；记录版本变更

## 2026-05-30 11:03 | 配置更新 | 更新 mkdocs.yml 导航结构

- 修改文件：
  - mkdocs.yml（新增 跨境电商、基础设施分组，补充所有新建页面）
- 修改原因：导航配置落后于 Wiki 页面增长，需要同步

## 2026-05-30 11:16 | 配置更新 | 更新总览页 + mkdocs.yml

- 修改文件：
  - llm-wiki/wiki/00-总览.md（更新知识版图、页面统计、快速导航）
  - mkdocs.yml（导航从 15 条目 → 38 条目）
  - llm-wiki/index.md（更新索引）
- 修改原因：总览页描述仍为 v0.1.0 状态，需同步到 v0.2.0
