---
title: "Wiki 健康检查流程"
type: "workflow"
status: "active"
tags: ["工作流", "健康检查", "维护"]
created: "2026-05-29"
updated: "2026-05-29"
sources: []
related:
  - "LLM Wiki"
  - "资料摄取流程"
---

# Wiki 健康检查流程

## 一句话定义

定期对 LLM Wiki 仓库进行健康检查，发现并修复孤立页面、断链、格式问题等。

## 前置条件

- 仓库已初始化
- `tools/wiki_lint.py` 存在且可运行

## 步骤

### 步骤 1：运行自动检查

```bash
cd llm-wiki/tools
python wiki_lint.py --verbose
```

### 步骤 2：分析检查结果

逐项检查：
- **孤立页面**：是否重要的页面未被引用？是否应该在 index.md 或 related 中添加链接？
- **断链**：检查 ```[[页面标题]]``` 指向的页面是否存在。如果不存在，是拼写错误还是目标页面尚未创建？
- **缺 frontmatter**：补充缺失的必需字段。
- **缺 sources**：是否有来源可以追溯？
- **过期页面**：status 为 outdated 的页面是否需要更新或归档？

### 步骤 3：修复可自动修复的问题

- 补全 frontmatter 字段
- 修正无效的 type 或 status
- 添加明显缺失的 related 链接

### 步骤 4：标记需人工处理的问题

- 断链的目标页面需要新建
- 来源信息需要人类查找
- 过时内容需要人类判断

### 步骤 5：生成健康检查报告

使用 `templates/健康检查报告模板.md` 生成报告，保存到 `wiki/reports/`。

### 步骤 6：更新日志

在 `log.md` 中记录本次健康检查。

## 建议频率

- 日常使用：每次资料摄取后运行
- 周期性：每周做一次全面健康检查
- CI/CD：可配置 GitHub Actions 自动运行