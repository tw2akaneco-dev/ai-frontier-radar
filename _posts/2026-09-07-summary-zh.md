---
layout: default
title: "Horizon Summary: 2026-09-07 (ZH)"
date: 2026-09-07
lang: zh
---

> 从 33 条内容中按规则筛选出 8 条重要资讯。

---

1. [Introducing GPT-6 Astra for developers](#item-1) ⭐️ 7.8/10
2. [ollama/ollama released v0.34.0-rc1](#item-2) ⭐️ 7.4/10
3. [ggml-org/llama.cpp released b10830](#item-3) ⭐️ 7.4/10
4. [ggml-org/llama.cpp released b10829](#item-4) ⭐️ 7.4/10
5. [ggml-org/llama.cpp released b10828](#item-5) ⭐️ 7.4/10
6. [Research acceleration: The view inside OpenAI](#item-6) ⭐️ 7.4/10
7. [The purpose of DNS is to spread scams](#item-7) ⭐️ 7.4/10
8. [google-gemini/gemini-cli released v0.60.0-nightly.20260906.g85aca163f](#item-8) ⭐️ 7.3/10

---

<a id="item-1"></a>
## [Introducing GPT-6 Astra for developers](https://simonwillison.net/2026/Sep/5/introducing-gpt-6-astra-for-developers/) ⭐️ 7.8/10

原文摘要：Introducing GPT-6 Astra for developers Blink and you'll miss it, but there's a familiar creature at 1m59s : Across the board, Astra has more attention to detail, better understanding of the user's prompt, and can build more sophisticated outputs. In particular, it excels at building 3D models. I've seen it make...

rss · Simon Willison · Sep 5, 23:27

**背景**: 来自 Simon Willison 的最新内容。

**标签**: `#model`, `#ai-engineering`

---

<a id="item-2"></a>
## [ollama/ollama released v0.34.0-rc1](https://github.com/ollama/ollama/releases/tag/v0.34.0-rc1) ⭐️ 7.4/10

原文摘要：## Use Ollama models in ChatGPT Desktop Ollama models can now be used directly in ChatGPT Desktop, so you can keep your existing workflow while running open models. Setup is available from the Ollama app on MacOS. This release also improves structured output performance on Apple Silicon, adds support for...

github · github-actions[bot] · Sep 5, 23:49

**背景**: 项目 ollama/ollama 发布 v0.34.0-rc1。

**标签**: `#inference`, `#open-source`

---

<a id="item-3"></a>
## [ggml-org/llama.cpp released b10830](https://github.com/ggml-org/llama.cpp/releases/tag/b10830) ⭐️ 7.4/10

原文摘要：convert : add `--fuse-qkv` flag to fuse Q/K/V into QKV during HF-to-GGUF conversion (#22780) **Website:** - **Attestations:** - **macOS/iOS:** - macOS Apple Silicon (arm64) - macOS Apple Silicon (arm64, KleidiAI enabled) DISABLED - macOS Intel (x64) - iOS XCFramework **Linux:** - Ubuntu x64 (CPU) - Ubuntu arm64...

github · github-actions[bot] · Sep 6, 23:29

**背景**: 项目 ggml-org/llama.cpp 发布 b10830。

**标签**: `#inference`, `#open-source`

---

<a id="item-4"></a>
## [ggml-org/llama.cpp released b10829](https://github.com/ggml-org/llama.cpp/releases/tag/b10829) ⭐️ 7.4/10

原文摘要：models : fix GDN normalization from `max` to `rsqrt` (#28068) * models: use flash-linear-attention's l2norm for gated delta net q/k The GDN q/k normalization is defined by flash-linear-attention as l2norm(x) = x * rsqrt(sum(x*x) + eps) with eps inside the root. Every GDN call site in the tree uses ggml_l2_norm...

github · github-actions[bot] · Sep 6, 23:04

**背景**: 项目 ggml-org/llama.cpp 发布 b10829。

**标签**: `#inference`, `#open-source`

---

<a id="item-5"></a>
## [ggml-org/llama.cpp released b10828](https://github.com/ggml-org/llama.cpp/releases/tag/b10828) ⭐️ 7.4/10

原文摘要：[Model] Support for Spark2_5ForCausalLM implementation (#27868) * Add Spark3 Model * rename spark3 -> spark2_5 Co-authored-by: Sigbjørn Skjæret Co-authored-by: dongjiang **Website:** - **Attestations:** - **macOS/iOS:** - macOS Apple Silicon (arm64) - macOS Apple Silicon (arm64, KleidiAI enabled) DISABLED - macOS...

github · github-actions[bot] · Sep 6, 22:08

**背景**: 项目 ggml-org/llama.cpp 发布 b10828。

**标签**: `#inference`, `#open-source`

---

<a id="item-6"></a>
## [Research acceleration: The view inside OpenAI](https://simonwillison.net/2026/Sep/6/research-acceleration-the-view-inside-openai/) ⭐️ 7.4/10

原文摘要：Research acceleration: The view inside OpenAI Apparently today is RSI day at OpenAI, for Recursive Self-Improvement - I think it's their new AGI. Both this piece and the new essay An Alien Mind (by Chief Scientist Jakub Pachocki) talk about it, and this one doesn't even bother to expand the acronym. Included are...

rss · Simon Willison · Sep 6, 23:57

**背景**: 来自 Simon Willison 的最新内容。

**标签**: `#ai-engineering`

---

<a id="item-7"></a>
## [The purpose of DNS is to spread scams](https://simonwillison.net/2026/Sep/6/the-purpose-of-dns-is-to-spread-scams/) ⭐️ 7.4/10

原文摘要：The purpose of DNS is to spread scams Terence Eden shares some daunting statistics in support of his take that "the Domain Name System's purpose seems to be a vector for criminals to run scams on people at a terrifyingly high rate". On this Interisle report ( via Andrew Campling ), Terence says: It says 85 million...

rss · Simon Willison · Sep 6, 14:40

**背景**: 来自 Simon Willison 的最新内容。

**标签**: `#ai-engineering`

---

<a id="item-8"></a>
## [google-gemini/gemini-cli released v0.60.0-nightly.20260906.g85aca163f](https://github.com/google-gemini/gemini-cli/releases/tag/v0.60.0-nightly.20260906.g85aca163f) ⭐️ 7.3/10

原文摘要：**Full Changelog**: https://github.com/google-gemini/gemini-cli/compare/v0.60.0-nightly.20260905.g85aca163f...v0.60.0-nightly.20260906.g85aca163f

github · gemini-cli-robot · Sep 6, 01:28

**背景**: 项目 google-gemini/gemini-cli 发布 v0.60.0-nightly.20260906.g85aca163f。

**标签**: `#model`, `#open-source`

---