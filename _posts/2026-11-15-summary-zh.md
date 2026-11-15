---
layout: default
title: "Horizon Summary: 2026-11-15 (ZH)"
date: 2026-11-15
lang: zh
---

> 从 38 条内容中按规则筛选出 10 条重要资讯。

---

1. [datasette-llm 0.1a11](#item-1) ⭐️ 8.1/10
2. [langchain-ai/langgraph released 1.2.22](#item-2) ⭐️ 7.7/10
3. [langchain-ai/langgraph released prebuilt==1.1.2](#item-3) ⭐️ 7.7/10
4. [langchain-ai/langgraph released checkpointpostgres==3.2.1](#item-4) ⭐️ 7.7/10
5. [browser-use/browser-use released 1.0.5](#item-5) ⭐️ 7.7/10
6. [datasette-vega 0.7](#item-6) ⭐️ 7.7/10
7. [ggml-org/llama.cpp released b12387](#item-7) ⭐️ 7.4/10
8. [ggml-org/llama.cpp released b12386](#item-8) ⭐️ 7.4/10
9. [ggml-org/llama.cpp released b12385](#item-9) ⭐️ 7.4/10
10. [(AINews) The No AI Slop Manifesto](#item-10) ⭐️ 7.3/10

---

<a id="item-1"></a>
## [datasette-llm 0.1a11](https://simonwillison.net/2026/Nov/14/datasette-llm/) ⭐️ 8.1/10

原文摘要：Release: datasette-llm 0.1a11 datasette-llm is the intermediate plugin for Datasette that supports configuring LLMs for use with other Datasette plugins. This release adds support for OpenAI-compatible endpoints, so you can configure Datasette to use an LLM hosted anywhere that talks the OpenAI pseudo-standard web...

rss · Simon Willison · Nov 14, 23:59

**背景**: 来自 Simon Willison 的最新内容。

**标签**: `#model`, `#research`, `#ai-engineering`

---

<a id="item-2"></a>
## [langchain-ai/langgraph released 1.2.22](https://github.com/langchain-ai/langgraph/releases/tag/1.2.22) ⭐️ 7.7/10

原文摘要：Changes since 1.2.21 * release(langgraph): 1.2.22 (#9702) * release(checkpoint-postgres): 3.2.1 (#9700) * release(prebuilt): 1.1.2 (#9701) * release(checkpoint): 4.3.2 (#9699) * fix(langgraph): stream a child graph on its own thread to a caller streaming subgraphs (#9698) * perf(langgraph): skip message conversion...

github · github-actions[bot] · Nov 14, 01:43

**背景**: 项目 langchain-ai/langgraph 发布 1.2.22。

**标签**: `#open-source`

---

<a id="item-3"></a>
## [langchain-ai/langgraph released prebuilt==1.1.2](https://github.com/langchain-ai/langgraph/releases/tag/prebuilt%3D%3D1.1.2) ⭐️ 7.7/10

原文摘要：Changes since prebuilt==1.1.1 * release(langgraph): 1.2.22 (#9702) * release(checkpoint-postgres): 3.2.1 (#9700) * release(prebuilt): 1.1.2 (#9701) * release(checkpoint): 4.3.2 (#9699) * perf(prebuilt): only format the call_model error message when raising (#9628) * release(langgraph): 1.2.21 (#9683) * chore(deps):...

github · github-actions[bot] · Nov 14, 01:33

**背景**: 项目 langchain-ai/langgraph 发布 prebuilt==1.1.2。

**标签**: `#open-source`

---

<a id="item-4"></a>
## [langchain-ai/langgraph released checkpointpostgres==3.2.1](https://github.com/langchain-ai/langgraph/releases/tag/checkpointpostgres%3D%3D3.2.1) ⭐️ 7.7/10

原文摘要：Changes since checkpointpostgres==3.2.0 * release(checkpoint-postgres): 3.2.1 (#9700) * release(checkpoint): 4.3.2 (#9699) * perf(checkpoint-postgres): run a lone store read outside a pipeline (#9635) * perf(checkpoint-postgres): skip the async saver's lock for connection pools (#9638) * perf(checkpoint-postgres):...

github · github-actions[bot] · Nov 14, 01:39

**背景**: 项目 langchain-ai/langgraph 发布 checkpointpostgres==3.2.1。

**标签**: `#open-source`

---

<a id="item-5"></a>
## [browser-use/browser-use released 1.0.5](https://github.com/browser-use/browser-use/releases/tag/1.0.5) ⭐️ 7.7/10

原文摘要：`pip install 'browser-use==1.0.5'` - Every run is judged by your own model: one more low-effort request checks the run against the task and fills `result.judgement` with `success`, `failure_reason`, `description`, `prompt_injection_detected`, `bot_block_or_captcha_detected` and `gotchas`. `judge_context=` gives it...

github · sarath-menon · Nov 14, 08:24

**背景**: 项目 browser-use/browser-use 发布 1.0.5。

**标签**: `#open-source`

---

<a id="item-6"></a>
## [datasette-vega 0.7](https://simonwillison.net/2026/Nov/14/datasette-vega/) ⭐️ 7.7/10

原文摘要：Release: datasette-vega 0.7 A new release of Datasette's longest untouched plugin, for rendering charts (using Vega-Lite ) against data in a table or custom query. The last release was in July 2018! I finally bumped it for compatibility with the latest Datasette alphas, plus some cosmetic tweaks to make it work...

rss · Simon Willison · Nov 14, 17:09

**背景**: 来自 Simon Willison 的最新内容。

**标签**: `#research`, `#ai-engineering`

---

<a id="item-7"></a>
## [ggml-org/llama.cpp released b12387](https://github.com/ggml-org/llama.cpp/releases/tag/b12387) ⭐️ 7.4/10

原文摘要：Fix ctz64 on 32bit (#32273) **Website:** - **Attestations:** - **macOS/iOS:** - macOS Apple Silicon (arm64) - macOS Apple Silicon (arm64, KleidiAI enabled) DISABLED - macOS Intel (x64) - iOS XCFramework **Linux:** - Ubuntu x64 (CPU) - Ubuntu arm64 (CPU) - Ubuntu 24.04 s390x (CPU) - Ubuntu 26.04 s390x (CPU) - Ubuntu...

github · github-actions[bot] · Nov 14, 19:26

**背景**: 项目 ggml-org/llama.cpp 发布 b12387。

**标签**: `#inference`, `#open-source`

---

<a id="item-8"></a>
## [ggml-org/llama.cpp released b12386](https://github.com/ggml-org/llama.cpp/releases/tag/b12386) ⭐️ 7.4/10

原文摘要：hexagon: fix fa no-mask tail (#32243) **Website:** - **Attestations:** - **macOS/iOS:** - macOS Apple Silicon (arm64) - macOS Apple Silicon (arm64, KleidiAI enabled) DISABLED - macOS Intel (x64) - iOS XCFramework **Linux:** - Ubuntu x64 (CPU) - Ubuntu arm64 (CPU) - Ubuntu 24.04 s390x (CPU) - Ubuntu 26.04 s390x...

github · github-actions[bot] · Nov 14, 19:07

**背景**: 项目 ggml-org/llama.cpp 发布 b12386。

**标签**: `#inference`, `#open-source`

---

<a id="item-9"></a>
## [ggml-org/llama.cpp released b12385](https://github.com/ggml-org/llama.cpp/releases/tag/b12385) ⭐️ 7.4/10

原文摘要：qwen2vl : apply FFN weight scales (#32241) The qwen2vl graph passed NULL for the ffn_up/gate/down scales, so the per-tensor NVFP4 scales loaded by the generic pass were never applied and the model produced garbage (PPL ~1e6 on CUDA, NaN on CPU). Pass the scales to build_ffn like qwen2 does. Fixes #32101...

github · github-actions[bot] · Nov 14, 18:48

**背景**: 项目 ggml-org/llama.cpp 发布 b12385。

**标签**: `#inference`, `#open-source`

---

<a id="item-10"></a>
## [(AINews) The No AI Slop Manifesto](https://latent.space/p/ainews-the-no-ai-slop-manifesto/) ⭐️ 7.3/10

原文摘要：November 13, 2026 — AIE speakers unite to lay out how to fight slop.

rss · Latent Space · Nov 14, 08:31

**背景**: 来自 Latent Space 的最新内容。

**标签**: `#ai-industry`

---