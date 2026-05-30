---
title: DeepSeek-Reasonix/README.zh-CN.md at main
source: https://github.com/esengine/DeepSeek-Reasonix/tree/main
author:
published:
created: 2026-05-30
description: DeepSeek-native AI coding agent for your terminal. Engineered around prefix-cache stability — leave it running. - DeepSeek-Reasonix/README.zh-CN.md at main · esengine/DeepSeek-Reasonix
tags:
  - clippings
---
[![Reasonix](https://github.com/esengine/DeepSeek-Reasonix/raw/main/docs/logo.svg)](https://github.com/esengine/DeepSeek-Reasonix/blob/main/docs/logo.svg)

**English** · [简体中文](https://github.com/esengine/DeepSeek-Reasonix/blob/main/README.zh-CN.md) · [日本語](https://github.com/esengine/DeepSeek-Reasonix/blob/main/README.ja-JP.md) · [Website](https://esengine.github.io/DeepSeek-Reasonix/) · [Guide](https://esengine.github.io/DeepSeek-Reasonix/configuration.html) · [Architecture](https://github.com/esengine/DeepSeek-Reasonix/blob/main/docs/ARCHITECTURE.md) · [Benchmarks](https://github.com/esengine/DeepSeek-Reasonix/blob/main/benchmarks) · **[Discord](https://discord.gg/XF78rEME2D)**

### A DeepSeek-native AI coding agent for your terminal.

Engineered around prefix-cache stability — so token costs stay low across long sessions, and you can leave it running.

[![Reasonix code mode — assistant proposes a SEARCH/REPLACE edit; nothing on disk until /apply](https://github.com/esengine/DeepSeek-Reasonix/raw/main/docs/assets/hero-terminal.svg)](https://github.com/esengine/DeepSeek-Reasonix/blob/main/docs/assets/hero-terminal.svg)

> [!tip] Tip
> **Cache stability isn't a feature you turn on; it's an invariant the loop is designed around.** That's the whole reason Reasonix is DeepSeek-only — every layer is tuned to the byte-stable prefix-cache mechanic.

> [!note] Note
> **Real user, single day (2026-05-01):** 435M input tokens, **99.82% cache hit**, ~$12 instead of the ~$61 the same workload would cost with no cache on `v4-flash` — see the [case study](https://github.com/esengine/DeepSeek-Reasonix/blob/main/benchmarks/real-world-cache/README.md). DeepSeek provides the cacheable bytes; the four mechanisms in [Pillar 1](https://github.com/esengine/DeepSeek-Reasonix/blob/main/docs/ARCHITECTURE.md#pillar-1--cache-first-loop) are how Reasonix keeps them cacheable across long sessions.

> [!important] Important
> **Community · 加入社区** — bilingual Discord with channels for setup help (`#help` / `#求助`), workflow showcases, feature ideas, and contributor-only PR coordination. Verify your GitHub in-server to get the **Contributor** role automatically. → **[https://discord.gg/XF78rEME2D](https://discord.gg/XF78rEME2D)**

## Install

Requires Node ≥ 22. Works on macOS · Linux · Windows (PowerShell · Git Bash · Windows Terminal).

Install Reasonix globally if you want the `reasonix` command available on your `PATH`:

```
npm install -g reasonix
reasonix code my-project   # paste a DeepSeek API key on first run; persists after
```

Or run it once without installing globally:

```
cd my-project
npx reasonix code          # always uses the latest package by default
```

Grab a [DeepSeek API key →](https://platform.deepseek.com/api_keys) · `reasonix code --help` for flags.

If you use Reasonix daily, global install is the simplest path. If you just want to try it, use `npx`.

**Prefer fewer keystrokes?** The shorter `dsnix` alias resolves to the same CLI:

```
npm install -g dsnix       # exposes \`dsnix\` on PATH, depends on reasonix
npx dsnix@latest code      # one-shot via the shorter command
```

A global `npm install -g reasonix` also drops a `dsnix` shim on PATH, so the two are interchangeable.

Bare `reasonix` (no subcommand) launches `code` in the current directory — typing `reasonix` and `reasonix code` are equivalent.

| Command | When |
| --- | --- |
| `reasonix` / `reasonix code [dir]` | The coding agent. **Start here.** |
| `reasonix chat` | Plain chat — no filesystem or shell tools. |
| `reasonix run "task"` | One-shot, streams to stdout. Good for pipes. |
| `reasonix doctor` | Health check: Node, API key, MCP wiring. |
| `reasonix update` | Upgrade Reasonix itself. |

Other subcommands (`replay` · `diff` · `events` · `stats` · `index` · `mcp` · `prune-sessions`) are in `reasonix --help` and the [CLI reference](https://esengine.github.io/DeepSeek-Reasonix/#cli).

### QQ channel

QQ can extend an existing `chat`, `code`, or desktop session as a remote channel. It is part of the current session flow, not a separate runtime mode.

- CLI: start a session, then run `/qq connect`
- Desktop: open `Settings -> General -> QQ Channel`

Once connected, QQ messages can enter the current session, assistant replies route back to QQ, and follow-up interactions can continue remotely.

For full setup, desktop quick start, and troubleshooting, see [QQ channel setup](https://github.com/esengine/DeepSeek-Reasonix/blob/main/docs/qq-connect.md).

### Desktop client (prerelease)

A native Tauri client for users who want a GUI over the same loop. Multi-tab, the right-panel shows files the agent has read or edited this session, the same cost / cache / token meters live at the bottom. Same DeepSeek API key, same `~/.reasonix` config — the desktop bundles its own Node runtime, no separate `npm install` step.

Download platform installers from [GitHub Releases](https://github.com/esengine/DeepSeek-Reasonix/releases). The desktop ships as a **prerelease**: the loop and protocol are the same as the CLI, but the UI is still being polished and the installers aren't code-signed yet.

- **macOS** — first launch hits Gatekeeper. One-time fix: `xattr -dr com.apple.quarantine /Applications/Reasonix.app` (or right-click → Open → confirm).
- **Windows** — SmartScreen warns "Unknown publisher". Click **More info → Run anyway**.
- **Linux** — `.deb` and `.AppImage` ship plain, no extra step.

The CLI remains the canonical surface. Anything that lands in the CLI is also available from the desktop's composer.

**Working in another folder · chat vs. code · author a skill**

**Working in a different folder.** Reasonix scopes filesystem tools to the launch directory; pass `--dir` to retarget. Mid-session switching isn't supported by design (memory paths would tangle with stale roots) — quit and relaunch.

```
npx reasonix code --dir /path/to/project
```

**Picking `chat` vs `code`.** `code` is the default and the only mode with filesystem / shell tools and SEARCH/REPLACE review. `chat` is the lighter, tools-off shell — reach for it when you want a thinking partner with MCP attached but no disk access.

| What you get | `code` | `chat` |
| --- | --- | --- |
| Filesystem tools + `edit_file` | ✓ | — |
| SEARCH/REPLACE → `/apply` review | ✓ | — |
| Shell tool (gated) | ✓ | — |
| Plan mode · `/todo` · `/skill new` · `/mcp add` | ✓ | — |
| Memory (`remember` / `recall_memory`) | project + global | global only |
| MCP servers from config · web search · `ask_choice` | ✓ | ✓ |
| Coding system prompt | ✓ | generic |
| Session scope | per-directory | shared default |

**Author your first skill.** No remote registry — write them directly. Edit the file (`description:` frontmatter + body), then `/skill list`. Add `runAs: subagent` to spawn an isolated subagent loop instead of inlining the body.

```
/skill new my-skill              # <project>/.reasonix/skills/my-skill.md
/skill new my-skill --global     # ~/.reasonix/skills for cross-project use
```

**Claude-format skills also load.** `<project>/.claude/skills/<name>/SKILL.md` and `~/.claude/skills/` are read alongside Reasonix's native paths, so tooling that emits Claude-format skills works out of the box. Example — drop OpenSpec workflows in without an upstream adapter:

```
npx openspec init --tools claude    # writes .claude/skills/openspec-*/SKILL.md
/skill openspec-propose <task>      # then invoke from Reasonix
```

## Configuration

One JSON file at `~/.reasonix/config.json` plus per-project overrides under `<project>/.reasonix/`. The full bilingual reference — every key, every slash command, the on-disk shape of skills/memory/hooks — lives at:

> 📘 **[Configuration Guide](https://esengine.github.io/DeepSeek-Reasonix/configuration.html)** · [中文](https://esengine.github.io/DeepSeek-Reasonix/configuration.html?lang=zh)

| Topic | Quick read |
| --- | --- |
| [MCP servers](https://esengine.github.io/DeepSeek-Reasonix/configuration.html#mcp) | stdio · SSE · Streamable HTTP. One spec format works for both `config.json` and `--mcp`. |
| [Skills](https://esengine.github.io/DeepSeek-Reasonix/configuration.html#skills) | Markdown playbooks the model can invoke. `inline` or `subagent` mode. |
| [Memory](https://esengine.github.io/DeepSeek-Reasonix/configuration.html#memory) | User-private knowledge pinned into the prefix. `user` / `feedback` / `project` / `reference` types. |
| [Hooks](https://esengine.github.io/DeepSeek-Reasonix/configuration.html#hooks) | Shell commands on lifecycle events. `PreToolUse` (gating) · `PostToolUse` · `UserPromptSubmit` · `Stop`. |
| [Permissions](https://esengine.github.io/DeepSeek-Reasonix/configuration.html#permissions) | Per-workspace shell allowlist. Exact-prefix match. |
| [Web search](https://esengine.github.io/DeepSeek-Reasonix/configuration.html#search) | Bing by default; switch to Baidu AI Search, self-hosted SearXNG, Metaso, Tavily, Perplexity, Exa, Brave, or Ollama with `/search-engine`. |
| [Semantic index](https://esengine.github.io/DeepSeek-Reasonix/configuration.html#index) | `reasonix index` — local Ollama or any OpenAI-compatible embedding endpoint. |

## What makes Reasonix different

The loop is organized around three pillars. Each one solves a problem generic agent frameworks don't even see — because they were designed for a different cache mechanic.

<sub align="center"><p dir="auto">Click through to the full architecture writeup → <a href="https://github.com/esengine/DeepSeek-Reasonix/blob/main/docs/ARCHITECTURE.md#pillar-1--cache-first-loop">Pillar 1 — Cache-first loop</a> · <a href="https://github.com/esengine/DeepSeek-Reasonix/blob/main/docs/ARCHITECTURE.md#pillar-2--tool-call-repair">Pillar 2 — Tool-call repair</a> · <a href="https://github.com/esengine/DeepSeek-Reasonix/blob/main/docs/ARCHITECTURE.md#pillar-3--cost-control-v06">Pillar 3 — Cost control</a></p></sub>  

## Capabilities

[![Reasonix capabilities — cell-diff renderer, MCP, plan mode, permissions, dashboard, persistent sessions, hooks/skills/memory, semantic search, auto-checkpoints, /effort knob, transcript replay, event log](https://github.com/esengine/DeepSeek-Reasonix/raw/main/docs/assets/feature-grid.svg)](https://github.com/esengine/DeepSeek-Reasonix/blob/main/docs/assets/feature-grid.svg)

## How it compares

|  | Reasonix | Claude Code | Cursor | Aider |
| --- | --- | --- | --- | --- |
| Backend | DeepSeek | Anthropic | OpenAI / Anthropic | any (OpenRouter) |
| License | **MIT** | closed | closed | Apache 2 |
| Cost profile | **low per task** | premium | subscription + use | varies |
| DeepSeek prefix-cache | **engineered** | not applicable | not applicable | incidental |
| Embedded web dashboard | yes | — | n/a (IDE) | — |
| Configurable web search engine | `/search-engine` | — | — | — |
| Persistent per-workspace sessions | yes | partial | n/a | — |
| Plan mode · MCP · hooks · skills | yes | yes | yes | partial |
| Web search (Bing + Baidu + SearXNG + API engines) | yes | yes | yes | yes |
| Open community development | yes | — | — | yes |

For live cache-hit rates, costs, and methodology, see [`benchmarks/`](https://github.com/esengine/DeepSeek-Reasonix/blob/main/benchmarks) — the numbers move with model pricing, so they live with the harness, not in the README.

## Documentation

- [**Architecture**](https://github.com/esengine/DeepSeek-Reasonix/blob/main/docs/ARCHITECTURE.md) — three pillars: cache-first loop, tool-call repair, cost control
- [**CLI Reference**](https://github.com/esengine/DeepSeek-Reasonix/blob/main/docs/CLI-REFERENCE.md) — every shell subcommand, every slash command, every keybinding
- [**QQ channel setup**](https://github.com/esengine/DeepSeek-Reasonix/blob/main/docs/qq-connect.md) — CLI first-connect flow, desktop entry, and QQ Open Platform credentials
- [**Benchmarks**](https://github.com/esengine/DeepSeek-Reasonix/blob/main/benchmarks) — τ-bench-lite harness, transcripts, cost methodology
- [**Website**](https://esengine.github.io/DeepSeek-Reasonix/) — getting started, dashboard mockup, TUI mockup
- [**Contributing**](https://github.com/esengine/DeepSeek-Reasonix/blob/main/CONTRIBUTING.md) — comment policy, error-handling rules, library-over-hand-rolled
- [**Code of Conduct**](https://github.com/esengine/DeepSeek-Reasonix/blob/main/CODE_OF_CONDUCT.md) · [**Security policy**](https://github.com/esengine/DeepSeek-Reasonix/blob/main/SECURITY.md)

## Community

> [!note] Note
> Reasonix is open source and community-developed. Every avatar in the Acknowledgments wall at the bottom of this file is a real PR that shipped.

Scoped starter tickets — each with background, code pointers, acceptance criteria, and hints — live under the [`good first issue`](https://github.com/esengine/reasonix/labels/good%20first%20issue) label. Pick anything open.

**Open Discussions — opinions wanted:**

- [#20 · CLI / TUI design](https://github.com/esengine/reasonix/discussions/20) — what's broken, what's missing, what would you change?
- [#21 · Dashboard design](https://github.com/esengine/reasonix/discussions/21) — react against the [proposed mockup](https://esengine.github.io/DeepSeek-Reasonix/design/agent-dashboard.html)
- [#22 · Future feature wishlist](https://github.com/esengine/reasonix/discussions/22) — what would you build into Reasonix next?

**Already using Reasonix and willing to help others discover it?** Publish blog posts, articles, screenshots, talks, or videos to [**Show and tell**](https://github.com/esengine/reasonix/discussions/categories/show-and-tell). The project has no marketing budget — community word of mouth is how new users find it. Sustained advocates earn the badge below, displayed next to the contributors wall once awarded:

**Before your first PR**: read [`CONTRIBUTING.md`](https://github.com/esengine/DeepSeek-Reasonix/blob/main/CONTRIBUTING.md) — short, strict rules (comments, errors, libraries-over-hand-rolled). `tests/comment-policy.test.ts` enforces the comment ones; `npm run verify` is the pre-push gate. By participating you agree to the [Code of Conduct](https://github.com/esengine/DeepSeek-Reasonix/blob/main/CODE_OF_CONDUCT.md). Security issues → [SECURITY.md](https://github.com/esengine/DeepSeek-Reasonix/blob/main/SECURITY.md).

## Non-goals

> [!important] Important
> Reasonix is opinionated. Some things it deliberately *doesn't* do — listed here so you can pick the right tool for your work.

- **Multi-provider flexibility.** DeepSeek-only on purpose. Coupling to one backend is the feature, not a limitation.
- **IDE integration.** Terminal-first. The diff lives in `git diff`, the file tree in `ls`. The dashboard is a companion, not a Cursor replacement.
- **Hardest-leaderboard reasoning.** Claude Opus still wins some benchmarks. DeepSeek is competitive on coding; if your work is "solve this PhD proof" rather than "fix this auth bug," start with Claude.
- **Air-gapped / fully-free.** Reasonix needs a paid DeepSeek API key. For air-gapped or zero-cost runs see Aider + Ollama or [Continue](https://continue.dev/).

## Star History

[

![Star History Chart](https://camo.githubusercontent.com/f97e60e63d0265d7b47b7e51409a7f0026be560b94b009606746617e1d7080d5/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f63686172743f7265706f733d6573656e67696e652f446565705365656b2d526561736f6e697826747970653d64617465266c6567656e643d746f702d6c656674)

](https://www.star-history.com/?repos=esengine%2FDeepSeek-Reasonix&type=date&legend=top-left)  

## Support

If Reasonix has been useful and you'd like to say thanks, you can. It stays a coffee, not a contract — donations don't buy feature priority or change how issues get triaged.

- **International** — PayPal: [paypal.me/yuhuahui](https://paypal.me/yuhuahui)
- **国内** — 微信支付（扫码）

[![WeChat Pay QR code](https://github.com/esengine/DeepSeek-Reasonix/raw/main/.github/sponsor/wechat-pay.jpg)](https://github.com/esengine/DeepSeek-Reasonix/blob/main/.github/sponsor/wechat-pay.jpg)

## Acknowledgments

A small list of folks whose work has shaped Reasonix the most — measured by both commit count and code volume. **Listed alphabetically, no ordering of importance.** The full contributor graph is on [GitHub](https://github.com/esengine/DeepSeek-Reasonix/graphs/contributors).

- [**ctharvey**](https://github.com/ctharvey)
- [**dimasd-angga**](https://github.com/dimasd-angga) (Dimas D. Angga)
- [**Evan-Pycraft**](https://github.com/Evan-Pycraft)
- [**ForeverYoungPp**](https://github.com/ForeverYoungPp)
- [**GTC2080**](https://github.com/GTC2080) (TaoMu)
- [**kabaka9527**](https://github.com/kabaka9527)
- [**lisniuse**](https://github.com/lisniuse) (Richie)
- [**wade19990814-hue**](https://github.com/wade19990814-hue)
- [**wviana**](https://github.com/wviana) (Wesley Viana)

Also a separate thank-you to [**Bernardxu123**](https://github.com/Bernardxu123) for designing the project logo (see [`docs/brand/`](https://github.com/esengine/DeepSeek-Reasonix/blob/main/docs/brand)), and to [AIGC Link](https://xhslink.com/m/80ngts127cA) for promoting the project on XiaoHongShu.

[![Contributors to esengine/DeepSeek-Reasonix](https://camo.githubusercontent.com/4a029d585015d2f1b2c23f7cb8cf43a69d7be70471443656c23bc3b26bc241be/68747470733a2f2f636f6e747269622e726f636b732f696d6167653f7265706f3d6573656e67696e652f446565705365656b2d526561736f6e6978266d61783d31303026636f6c756d6e733d3132)](https://github.com/esengine/DeepSeek-Reasonix/graphs/contributors)

---

<sub>MIT — see <a href="https://github.com/esengine/DeepSeek-Reasonix/blob/main/LICENSE">LICENSE</a></sub>  
<sub>Built by the community at <a href="https://github.com/esengine/DeepSeek-Reasonix/graphs/contributors">esengine/DeepSeek-Reasonix</a></sub>