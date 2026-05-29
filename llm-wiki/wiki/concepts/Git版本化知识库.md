---
title: "Git 版本化知识库"
type: "concept"
status: "active"
tags: ["核心概念", "Git", "版本控制", "知识管理"]
created: "2026-05-29"
updated: "2026-05-29"
sources: []
related:
  - "LLM Wiki"
  - "Markdown 知识库"
---

# Git 版本化知识库

## 一句话定义

使用 Git 对知识库进行版本控制，让每一次知识变更都可追溯、可审查、可回滚。

## 核心要点

- Git 跟踪每一次修改，提供完整的变更历史
- commit message 记录修改原因
- 分支支持并行知识探索
- GitHub/GitLab 提供远程备份和协作平台

## 详细说明

### 为什么用 Git 管理知识

传统知识库的一个大问题是"谁改了什么、为什么改"不可知。Git 解决了这个问题：

- `git log`：查看知识库的完整变更历史
- `git diff`：精确对比任意两个版本
- `git blame`：追踪每一行内容的来源
- `git branch`：在新分支上安全地做大规模改动
- `git revert`：回滚错误的修改

### 在本 Wiki 中的应用

1. 每次 AI Agent 维护后，提交一个清晰的 commit。
2. `log.md` 记录操作说明，`changelog.md` 记录版本变更。
3. 远程仓库（GitHub）提供安全备份。
4. Pull Request 机制可用于人工审查 AI 的修改。

### Git 知识库的优势

| 特性 | 无版本控制 | Git 版本控制 |
|------|-----------|-------------|
| 变更历史 | ❌ | ✅ `git log` |
| 回滚能力 | ❌ | ✅ `git revert` |
| 协作 | 困难 | ✅ PR/MR |
| 审计 | ❌ | ✅ diff/blame |
| 备份 | 手动 | ✅ push 远程 |

## 与其他概念的关系

- [[LLM Wiki]]：Git 是 LLM Wiki 的版本控制方式
- [[Markdown 知识库]]：Git 对 Markdown 天然友好

## 适用场景

- 需要审计的知识库
- 多人协作的知识管理
- AI Agent 维护的知识库（需要人工 review）

## 资料来源

## 待补充问题

- 大规模知识库的 Git 性能优化