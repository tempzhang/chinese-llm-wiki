---
title: OpenAI Codex 永久免费！一键接入本地 AI 大模型教程｜Ollama × ChatGPT/Gemma4/Qwen等
source: https://blog.xgdn.com/43.html
author:
  - "[[大家好！我是X超哥，为您分享互联网资讯、实用教程和一些有趣的内容。 请我喝咖啡]]"
published:
created: 2026-05-30
description: 大家好，我是超哥。今天给大家分享一个 OpenAI Codex 免费使用的方法。通过对接 Ollama 本地 AI 大模型，让 Codex 可以直接调用 gpt-oss、Qwen、Gemma 等模型，无需额外 API 费用，实现本地运行、免费使用。
tags:
  - clippings
---
大家好，我是超哥。今天给大家分享一个 **OpenAI Codex** 免费使用的方法。通过对接 **Ollama** 本地 AI 大模型，让 Codex 可以直接调用 **ChatGPT** 、 **Qwen** 、 **Gemma** 等模型， **无需** 额外 **API 费用** ，实现 **本地运行** 、完全 **免费使用** 。

### 一、下载并安装 OpenAI Codex 软件

下载地址： [https://openai.com/zh-Hans-CN/codex/](https://openai.com/zh-Hans-CN/codex/)

![](https://www.xchaoge.com/d/file/efpub/2026/05-29/e193b243423b741900a7399d4adf467c.png)

### 二、下载并安装 Ollama 软件（需最新版本）

![](https://www.xchaoge.com/d/file/efpub/2026/03-26/37bfd39ec8c214436d3f847b8d03e722.png)

下载 **Windows 版** ollama地址： [https://ollama.com/download/windows](https://ollama.com/download/windows)

下载 **Mac版** ollama地址： [https://ollama.com/download/mac](https://ollama.com/download/mac)

![](https://www.xchaoge.com/d/file/efpub/2026/05-29/27023b4c2191a3d93b0c63b2c440b5ed.png)

### 三、下载本地 AI 大模型

全部 AI 大模型网址： [https://ollama.com/search](https://ollama.com/search)

**（1）OpenAI gpt-oss大模型列表网址： [https://ollama.com/library/gpt-oss](https://ollama.com/library/gpt-oss)**

**gpt-oss:20b** 安装命令：

```
ollama pull gpt-oss:20b
```

1.

ollama pull gpt-oss:20b

**（2）gemma4 大模型列表网址： [https://ollama.com/library/gemma4](https://ollama.com/library/gemma4)**

**gemma4:e4b** 安装命令：

```
ollama pull gemma4:e4b
```

1.

ollama pull gemma4:e4b

**（3）qwen3.6 大模型列表网址： [https://ollama.com/library/qwen3.6](https://ollama.com/library/qwen3.6)**

**qwen3.6:27b** 安装命令：

```
ollama pull qwen3.6:27b
```

1.

ollama pull qwen3.6:27b

### 四、把 ollama 接入到 Codex

打开CMD，在CMD里执行命令：

```
ollama launch codex-app
```

1.

ollama launch codex-app

### 五、测试 Codex

```
有8个球，其中1个重量不同（不知道更重还是更轻），只有一个天平，最多称3次，如何找出异常球并判断轻重？
```

1.

有8个球，其中1个重量不同（不知道更重还是更轻），只有一个天平，最多称3次，如何找出异常球并判断轻重？

```
帮我在电脑桌面生成一个漂亮的html密码随机生成的工具
```

1.

帮我在电脑桌面生成一个漂亮的html密码随机生成的工具