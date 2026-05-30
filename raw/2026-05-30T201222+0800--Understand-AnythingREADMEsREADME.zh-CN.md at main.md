---
title: Understand-Anything/READMEs/README.zh-CN.md at main
source: https://github.com/Lum1104/Understand-Anything/tree/main
author:
published:
created: 2026-05-30
description: Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more. - Understand-Anything/READMEs/README.zh-CN.md at main · Lum1104/Understand-Anything
tags:
  - clippings
---
## Understand Anything

**Turn any codebase, knowledge base, or docs into an interactive knowledge graph you can explore, search, and ask questions about.**  
*Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more.*

[![Lum1104%2FUnderstand-Anything | Trendshift](https://camo.githubusercontent.com/62ef89b8109c48963cdf0c9ae0f6901bf62bb04d07afbb798d44166fbeac8083/68747470733a2f2f7472656e6473686966742e696f2f6170692f62616467652f7265706f7369746f726965732f3233343832)](https://trendshift.io/repositories/23482)

[English](https://github.com/Lum1104/Understand-Anything/blob/main/README.md) | [简体中文](https://github.com/Lum1104/Understand-Anything/blob/main/READMEs/README.zh-CN.md) | [繁體中文](https://github.com/Lum1104/Understand-Anything/blob/main/READMEs/README.zh-TW.md) | [日本語](https://github.com/Lum1104/Understand-Anything/blob/main/READMEs/README.ja-JP.md) | [한국어](https://github.com/Lum1104/Understand-Anything/blob/main/READMEs/README.ko-KR.md) | [Español](https://github.com/Lum1104/Understand-Anything/blob/main/READMEs/README.es-ES.md) | [Türkçe](https://github.com/Lum1104/Understand-Anything/blob/main/READMEs/README.tr-TR.md) | [Русский](https://github.com/Lum1104/Understand-Anything/blob/main/READMEs/README.ru-RU.md)

[![Understand Anything — Turn any codebase into an interactive knowledge graph](https://github.com/Lum1104/Understand-Anything/raw/main/assets/hero.png)](https://github.com/Lum1104/Understand-Anything/blob/main/assets/hero.png)

**💬 [Join the Discord community →](https://discord.gg/pydat66RY)**  
*Ask questions, share what you've built, get help from the community.*

---

**You just joined a new team. The codebase is 200,000 lines of code. Where do you even start?**

Understand Anything is a [Claude Code Plugin](https://code.claude.com/docs/en/plugins-reference#plugins-reference) that analyzes your project with a multi-agent pipeline, builds a knowledge graph of every file, function, class, and dependency, then gives you an interactive dashboard to explore it all visually. Stop reading code blind. Start seeing the big picture.

> **The goal isn't a graph that wows you with how complex your codebase is — it's a graph that quietly teaches you how every piece fits together.**

---

## ✨ Features

> [!note] Note
> **Want to skip the reading?** Try the [live demo](https://understand-anything.com/demo/) in our [homepage](https://understand-anything.com/) — a fully interactive dashboard you can pan, zoom, search, and explore right in your browser.

### Explore the structural graph

Navigate your codebase as an interactive knowledge graph — every file, function, and class is a node you can click, search, and explore. Select any node to see plain-English summaries, relationships, and guided tours.

### Understand business logic

Switch to the domain view and see how your code maps to real business processes — domains, flows, and steps laid out as a horizontal graph.

### Analyze knowledge bases

Point `/understand-knowledge` at a [Karpathy-pattern LLM wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) and get a force-directed knowledge graph with community clustering. The deterministic parser extracts wikilinks and categories from `index.md`, then LLM agents discover implicit relationships, extract entities, and surface claims — turning your wiki into a navigable graph of interconnected ideas.

| ### 🧭 Guided Tours  Auto-generated walkthroughs of the architecture, ordered by dependency. Learn the codebase in the right order. | ### 🔍 Fuzzy & Semantic Search  Find anything by name or by meaning. Search "which parts handle auth?" and get relevant results across the graph. |
| --- | --- |
| ### 📊 Diff Impact Analysis  See which parts of the system your changes affect before you commit. Understand ripple effects across the codebase. | ### 🎭 Persona-Adaptive UI  The dashboard adjusts its detail level based on who you are — junior dev, PM, or power user. |
| ### 🏗️ Layer Visualization  Automatic grouping by architectural layer — API, Service, Data, UI, Utility — with color-coded legend. | ### 📚 Language Concepts  12 programming patterns (generics, closures, decorators, etc.) explained in context wherever they appear. |

---

## 🚀 Quick Start

### 1\. Install the plugin

```
/plugin marketplace add Lum1104/Understand-Anything
/plugin install understand-anything
```

### 2\. Analyze your codebase

```
/understand
```

A multi-agent pipeline scans your project, extracts every file, function, class, and dependency, then builds a knowledge graph saved to `.understand-anything/knowledge-graph.json`.

**Localized output:** Use `--language` to generate content in your preferred language:

```
# Generate Chinese content (知识图节点描述和 Dashboard UI)
/understand --language zh

# Supported languages: en (default), zh, zh-TW, ja, ko, ru
```

The `--language` parameter affects:

- Node summaries and descriptions in the knowledge graph
- Dashboard UI labels, buttons, and tooltips
- Guided tour explanations

### 3\. Explore the dashboard

```
/understand-dashboard
```

An interactive web dashboard opens with your codebase visualized as a graph — color-coded by architectural layer, searchable, and clickable. Select any node to see its code, relationships, and a plain-English explanation.

### 4\. Keep learning

```
# Ask anything about the codebase
/understand-chat How does the payment flow work?

# Analyze impact of your current changes
/understand-diff

# Deep-dive into a specific file or function
/understand-explain src/auth/login.ts

# Generate an onboarding guide for new team members
/understand-onboard

# Extract business domain knowledge (domains, flows, steps)
/understand-domain

# Analyze a Karpathy-pattern LLM wiki knowledge base
/understand-knowledge ~/path/to/wiki

# Re-run anytime — incremental by default (only re-analyzes changed files)
/understand

# Auto-update on every commit via a post-commit hook
/understand --auto-update

# Scope to a subdirectory (for huge monorepos)
/understand src/frontend
```

---

## 🌐 Multi-Platform Installation

Understand-Anything works across multiple AI coding platforms.

### Claude Code (Native)

```
/plugin marketplace add Lum1104/Understand-Anything
/plugin install understand-anything
```

### One-line install (Codex / OpenCode / OpenClaw / Antigravity / Gemini CLI / Pi Agent / Vibe CLI / VS Code Copilot / Hermes / Cline / KIMI CLI / Trae)

**macOS / Linux:**

```
curl -fsSL https://raw.githubusercontent.com/Lum1104/Understand-Anything/main/install.sh | bash
# or skip the prompt by passing the platform:
curl -fsSL https://raw.githubusercontent.com/Lum1104/Understand-Anything/main/install.sh | bash -s codex
```

**Windows (PowerShell):**

```
iwr -useb https://raw.githubusercontent.com/Lum1104/Understand-Anything/main/install.ps1 | iex
```

The installer clones the repo to `~/.understand-anything/repo` and creates the right symlinks for the chosen platform. Restart your CLI/IDE afterwards.

- Supported `<platform>` values: `gemini`, `codex`, `opencode`, `pi`, `openclaw`, `antigravity`, `vibe`, `vscode`, `hermes`, `cline`, `kimi`, `trae`
- Update later: `./install.sh --update`
- Uninstall: `./install.sh --uninstall <platform>`

### Cursor

Cursor auto-discovers the plugin via `.cursor-plugin/plugin.json` when this repo is cloned. No manual installation needed — just clone and open in Cursor.

If auto-discovery doesn't pick it up, install it manually: open **Cursor Settings → Plugins**, paste `https://github.com/Lum1104/Understand-Anything` into the search field, and add it from there.

### VS Code + GitHub Copilot

VS Code with GitHub Copilot (v1.108+) auto-discovers the plugin via `.copilot-plugin/plugin.json` when this repo is cloned. No manual installation needed — just clone and open in VS Code.

For personal skills (available across all projects), run the `install.sh` above with the `vscode` platform.

### Copilot CLI

```
copilot plugin install Lum1104/Understand-Anything:understand-anything-plugin
```

### Platform Compatibility

| Platform | Status | Install Method |
| --- | --- | --- |
| Claude Code | ✅ Native | Plugin marketplace |
| Cursor | ✅ Supported | Auto-discovery |
| VS Code + GitHub Copilot | ✅ Supported | Auto-discovery |
| Copilot CLI | ✅ Supported | Plugin install |
| Codex | ✅ Supported | `install.sh codex` |
| OpenCode | ✅ Supported | `install.sh opencode` |
| OpenClaw | ✅ Supported | `install.sh openclaw` |
| Antigravity | ✅ Supported | `install.sh antigravity` |
| Gemini CLI | ✅ Supported | `install.sh gemini` |
| Pi Agent | ✅ Supported | `install.sh pi` |
| Vibe CLI | ✅ Supported | `install.sh vibe` |
| Hermes | ✅ Supported | `install.sh hermes` |
| Cline | ✅ Supported | `install.sh cline` |
| KIMI CLI | ✅ Supported | `install.sh kimi` |
| Trae | ✅ Supported | `install.sh trae` |

---

The graph is just JSON — **commit it once, and teammates skip the pipeline**. Good for onboarding, PR reviews, and docs-as-code.

> **Example:** [GoogleCloudPlatform/microservices-demo (fork)](https://github.com/Lum1104/microservices-demo) — Go / Java / Python / Node reference with a committed graph.

**What to commit:** everything in `.understand-anything/` *except* `intermediate/` and `diff-overlay.json` (those are local scratch).

```
.understand-anything/intermediate/
.understand-anything/diff-overlay.json
```

**Keep it fresh:** enable `/understand --auto-update` — a post-commit hook incrementally patches the graph so each commit lands with a matching graph. Or re-run `/understand` manually before releases.

**Large graphs (10 MB+):** track with **git-lfs**.

```
git lfs install
git lfs track ".understand-anything/*.json"
git add .gitattributes .understand-anything/
```

---

## 🔧 Under the Hood

### Tree-sitter + LLM hybrid

Static analysis and LLMs do what each does best:

- **Tree-sitter (deterministic)** — parses source into a concrete syntax tree and extracts structural facts: imports, exports, function/class definitions, call sites, inheritance. Pre-resolved into an `importMap` during the scan phase and passed to file-analyzers so they don't re-derive imports from source. Same input → same output, every run. Also powers fingerprint-based change detection for incremental updates.
- **LLM (semantic)** — reads the parsed structure alongside the original source to produce what parsers can't: plain-English summaries, tags, architectural layer assignments, business-domain mapping, guided tours, language concept callouts.

This split is why the graph is reproducible on the structural side (the same code always yields the same edges) while still capturing intent on the semantic side (what a file is *for*, not just what it imports).

### Multi-Agent Pipeline

The `/understand` command orchestrates 5 specialized agents, and `/understand-domain` adds a 6th:

| Agent | Role |
| --- | --- |
| `project-scanner` | Discover files, detect languages and frameworks |
| `file-analyzer` | Extract functions, classes, imports; produce graph nodes and edges |
| `architecture-analyzer` | Identify architectural layers |
| `tour-builder` | Generate guided learning tours |
| `graph-reviewer` | Validate graph completeness and referential integrity (runs inline by default; use `--review` for full LLM review) |
| `domain-analyzer` | Extract business domains, flows, and process steps (used by `/understand-domain`) |
| `article-analyzer` | Extract entities, claims, and implicit relationships from wiki articles (used by `/understand-knowledge`) |

File analyzers run in parallel (up to 5 concurrent, 20-30 files per batch). Supports incremental updates — only re-analyzes files that changed since the last run.

---

## 🎥 Community

A community-made walkthrough by **Better Stack**.

[![Community walkthrough by Better Stack — watch on YouTube](https://camo.githubusercontent.com/83110e67e7cfc1d6c6a16e67fb3014d3a9e421963627cdc68f45952b016afd62/68747470733a2f2f696d672e796f75747562652e636f6d2f76692f566d495558566c74375f492f6d617872657364656661756c742e6a7067)](https://www.youtube.com/watch?v=VmIUXVlt7_I)  
*[Watch on YouTube →](https://www.youtube.com/watch?v=VmIUXVlt7_I)*

Made a video, blog post, or tutorial? Open an issue or PR — happy to feature it here.

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Run the tests (`pnpm --filter @understand-anything/core test`)
4. Commit your changes and open a pull request

Please open an issue first for major changes so we can discuss the approach.

---

**Stop reading code blind. Start understanding everything.**

## Star History

[

![Star History Chart](https://camo.githubusercontent.com/625d4a6f49563ca3ebf8f1921c330a9fefd3879c9839254b6aeac825a2a11ec9/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f696d6167653f7265706f733d4c756d313130342f556e6465727374616e642d416e797468696e6726747970653d64617465266c6567656e643d746f702d6c656674)

](https://www.star-history.com/?repos=Lum1104%2FUnderstand-Anything&type=date&legend=top-left)

*Thanks to everyone who's used and contributed — knowing this saves people time is what made it worth building.*