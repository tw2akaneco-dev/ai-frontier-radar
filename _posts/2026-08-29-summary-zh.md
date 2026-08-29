---
layout: default
title: "Horizon Summary: 2026-08-29 (ZH)"
date: 2026-08-29
lang: zh
---

> 从 846 条内容中按规则筛选出 18 条重要资讯。

---

1. [test(filesystem): add MCP SDK regression coverage for directory_tree …](#item-1) ⭐️ 8.9/10
2. [Supporting Thailand’s next generation of AI startups](#item-2) ⭐️ 8.2/10
3. [fix(filesystem): create_directory doesn't create parent directories (…](#item-3) ⭐️ 8.1/10
4. [fix(sequentialthinking): restore nextThoughtNeeded in the advertised …](#item-4) ⭐️ 8.1/10
5. [anomalyco/opencode released v1.18.25](#item-5) ⭐️ 7.7/10
6. [anomalyco/opencode released v1.18.24](#item-6) ⭐️ 7.7/10
7. [ggml-org/llama.cpp released b10679](#item-7) ⭐️ 7.4/10
8. [ggml-org/llama.cpp released b10678](#item-8) ⭐️ 7.4/10
9. [ggml-org/llama.cpp released b10677](#item-9) ⭐️ 7.4/10
10. [Just a rumour of a bug is enough to find a security exploit these days](#item-10) ⭐️ 7.4/10
11. [google-gemini/gemini-cli released v0.59.0-nightly.20260829.g0bd1d4397](#item-11) ⭐️ 7.3/10
12. [google-gemini/gemini-cli released v0.59.0-nightly.20260828.g3c311beac](#item-12) ⭐️ 7.3/10
13. [(AINews) OpenAI to reach AGI bar by end-2026](#item-13) ⭐️ 7.3/10
14. [Autonomous Mathematical Discovery in an Open-World Multi-Agent Environment](#item-14) ⭐️ 7.1/10
15. [Benchmarking AI Agents for Hardware Design Automation via MCP Tool Calling](#item-15) ⭐️ 7.0/10
16. [BekchiAI: Measuring, Observing, and Controlling LLM Agents in One Click](#item-16) ⭐️ 7.0/10
17. [ProvenanceGuard: Source-Aware Factuality Verification for MCP-Based LLM Agents](#item-17) ⭐️ 7.0/10
18. [ClueWeaver: Reward-Guided Dual-Agent Evidence Reasoning for Compact LLMs on Literary Long Narratives](#item-18) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [test(filesystem): add MCP SDK regression coverage for directory_tree …](https://github.com/modelcontextprotocol/servers/commit/71e3cfbd1e7e0ff88fa24ce5406f8e220ceae5c4) ⭐️ 8.9/10

原文摘要：test(filesystem): add MCP SDK regression coverage for directory_tree (#3245) * test(filesystem): add directory_tree MCP SDK regression coverage * docs(filesystem): drop troubleshooting note from README

rss · MCP Reference Servers · Aug 28, 02:17

**背景**: 来自 MCP Reference Servers 的最新内容。

**标签**: `#mcp`

---

<a id="item-2"></a>
## [Supporting Thailand’s next generation of AI startups](https://openai.com/index/supporting-next-generation-ai-startups-thailand) ⭐️ 8.2/10

原文摘要：OpenAI and Thailand’s MHESI launch an eight-week accelerator helping 10 health, wellness, and education startups turn AI prototypes into trusted products.

rss · OpenAI News · Aug 28, 02:00

**背景**: 来自 OpenAI News 的最新内容。

**标签**: `#frontier-labs`

---

<a id="item-3"></a>
## [fix(filesystem): create_directory doesn't create parent directories (…](https://github.com/modelcontextprotocol/servers/commit/cda92bdaacd558192fedf1a60d2bb27510792388) ⭐️ 8.1/10

原文摘要：fix(filesystem): create_directory doesn't create parent directories (#4631) validatePath()'s ENOENT fallback checked only the immediate parent directory before allowing a new path through. Creating a path with more than one missing level (e.g. a/b/c when none of a, b, c exist) made the immediate parent check fail...

rss · MCP Reference Servers · Aug 28, 17:58

**背景**: 来自 MCP Reference Servers 的最新内容。

**标签**: `#mcp`

---

<a id="item-4"></a>
## [fix(sequentialthinking): restore nextThoughtNeeded in the advertised …](https://github.com/modelcontextprotocol/servers/commit/d6402efee6cc6446b23adbcb63051f9dc8612be5) ⭐️ 8.1/10

原文摘要：fix(sequentialthinking): restore nextThoughtNeeded in the advertised inputSchema required array (#4652) * fix(sequentialthinking): restore nextThoughtNeeded in the advertised inputSchema required array commit 1cdf806d (#3533) wrapped nextThoughtNeeded in a z.preprocess-based coercedBoolean to fix a real footgun...

rss · MCP Reference Servers · Aug 28, 17:57

**背景**: 来自 MCP Reference Servers 的最新内容。

**标签**: `#mcp`

---

<a id="item-5"></a>
## [anomalyco/opencode released v1.18.25](https://github.com/anomalyco/opencode/releases/tag/v1.18.25) ⭐️ 7.7/10

原文摘要：## Core ### Bugfixes - Fixed Azure authentication so Azure CLI sign-in works without requiring Bun.

github · opencode-agent[bot] · Aug 28, 05:58

**背景**: 项目 anomalyco/opencode 发布 v1.18.25。

**标签**: `#open-source`

---

<a id="item-6"></a>
## [anomalyco/opencode released v1.18.24](https://github.com/anomalyco/opencode/releases/tag/v1.18.24) ⭐️ 7.7/10

原文摘要：## Core ### Bugfixes - Bedrock reasoning responses no longer get cached into unreplayable empty messages. ### Improvements - Azure providers can now sign in with Microsoft Entra ID through the Azure CLI instead of requiring an API key. - V1 now reads supported V2 config fields so newer config files keep working in...

github · opencode-agent[bot] · Aug 28, 04:10

**背景**: 项目 anomalyco/opencode 发布 v1.18.24。

**标签**: `#open-source`

---

<a id="item-7"></a>
## [ggml-org/llama.cpp released b10679](https://github.com/ggml-org/llama.cpp/releases/tag/b10679) ⭐️ 7.4/10

原文摘要：bench: add --tensor-read-lazy (#27881) * bench: add --tensor-read-lazy * rm the alias * rename to LLAMA_LAZY_MODE_* **Website:** - **Attestations:** - **macOS/iOS:** - macOS Apple Silicon (arm64) - macOS Apple Silicon (arm64, KleidiAI enabled) DISABLED - macOS Intel (x64) - iOS XCFramework **Linux:** - Ubuntu x64...

github · github-actions[bot] · Aug 28, 19:23

**背景**: 项目 ggml-org/llama.cpp 发布 b10679。

**标签**: `#inference`, `#open-source`

---

<a id="item-8"></a>
## [ggml-org/llama.cpp released b10678](https://github.com/ggml-org/llama.cpp/releases/tag/b10678) ⭐️ 7.4/10

原文摘要：model: qwen4exp: reduce number of graph splits (#27880) **Website:** - **Attestations:** - **macOS/iOS:** - macOS Apple Silicon (arm64) - macOS Apple Silicon (arm64, KleidiAI enabled) DISABLED - macOS Intel (x64) - iOS XCFramework **Linux:** - Ubuntu x64 (CPU) - Ubuntu arm64 (CPU) - Ubuntu s390x (CPU) - Ubuntu x64...

github · github-actions[bot] · Aug 28, 18:51

**背景**: 项目 ggml-org/llama.cpp 发布 b10678。

**标签**: `#inference`, `#open-source`

---

<a id="item-9"></a>
## [ggml-org/llama.cpp released b10677](https://github.com/ggml-org/llama.cpp/releases/tag/b10677) ⭐️ 7.4/10

原文摘要：vulkan: fix missing view-alias dependencies in ggml_vk_graph_optimize (#27812) * vulkan: fix missing view-alias dependencies in ggml_vk_graph_optimize is_src_of doesn't treat two views of one tensor as dependent, so the optimizer reorders nodes across aliased reads and writes. Result: silently wrong tokens under...

github · github-actions[bot] · Aug 28, 18:27

**背景**: 项目 ggml-org/llama.cpp 发布 b10677。

**标签**: `#inference`, `#open-source`

---

<a id="item-10"></a>
## [Just a rumour of a bug is enough to find a security exploit these days](https://simonwillison.net/2026/Aug/28/just-a-rumour-of-a-bug/) ⭐️ 7.4/10

原文摘要：Just a rumour of a bug is enough to find a security exploit these days Anil Madhavapeddy is a professor of computer science at Cambridge and a core maintainer of the OCaml compiler. In this somewhat alarming post he reports that security issues in OCaml projects are seeing evidence of attempted exploits within...

rss · Simon Willison · Aug 28, 22:12

**背景**: 来自 Simon Willison 的最新内容。

**标签**: `#ai-engineering`

---

<a id="item-11"></a>
## [google-gemini/gemini-cli released v0.59.0-nightly.20260829.g0bd1d4397](https://github.com/google-gemini/gemini-cli/releases/tag/v0.59.0-nightly.20260829.g0bd1d4397) ⭐️ 7.3/10

原文摘要：## What's Changed * fix(core): enforce fail-closed workspace trust and filter mcpServers in restricted mode by @luisfelipe-alt in https://github.com/google-gemini/gemini-cli/pull/29099 **Full Changelog**:...

github · gemini-cli-robot · Aug 29, 01:56

**背景**: 项目 google-gemini/gemini-cli 发布 v0.59.0-nightly.20260829.g0bd1d4397。

**标签**: `#model`, `#open-source`

---

<a id="item-12"></a>
## [google-gemini/gemini-cli released v0.59.0-nightly.20260828.g3c311beac](https://github.com/google-gemini/gemini-cli/releases/tag/v0.59.0-nightly.20260828.g3c311beac) ⭐️ 7.3/10

原文摘要：**Full Changelog**: https://github.com/google-gemini/gemini-cli/compare/v0.59.0-nightly.20260827.g3c311beac...v0.59.0-nightly.20260828.g3c311beac

github · gemini-cli-robot · Aug 28, 03:53

**背景**: 项目 google-gemini/gemini-cli 发布 v0.59.0-nightly.20260828.g3c311beac。

**标签**: `#model`, `#open-source`

---

<a id="item-13"></a>
## [(AINews) OpenAI to reach AGI bar by end-2026](https://www.latent.space/p/ainews-openai-to-reach-agi-bar-by) ⭐️ 7.3/10

原文摘要：It’s Time. We’re in the Endgame now.

rss · Latent Space · Aug 28, 07:12

**背景**: 来自 Latent Space 的最新内容。

**标签**: `#ai-industry`

---

<a id="item-14"></a>
## [Autonomous Mathematical Discovery in an Open-World Multi-Agent Environment](https://arxiv.org/abs/2608.23691) ⭐️ 7.1/10

原文摘要：Autonomous Mathematical Discovery in an Open-World Multi-Agent Environment

hackernews · stephenchung · Aug 28, 17:01 · [社区讨论](https://news.ycombinator.com/item?id=49481455)

**社区讨论**: 社区热度 88，讨论 23 条。

**标签**: `#agent`

---

<a id="item-15"></a>
## [Benchmarking AI Agents for Hardware Design Automation via MCP Tool Calling](https://arxiv.org/abs/2608.26199) ⭐️ 7.0/10

原文摘要：arXiv:2608.26199v1 Announce Type: new Abstract: We ask whether AI agents powered by locally deployed large language models can reliably automate expert-defined hardware design workflows in an industry-realistic tool-calling setting. In these environments, engineers issue repetitive, dependency-ordered...

rss · arXiv cs.AI · Aug 28, 04:00

**背景**: 来自 arXiv cs.AI 的最新内容。

**标签**: `#mcp`, `#agent`, `#research`

---

<a id="item-16"></a>
## [BekchiAI: Measuring, Observing, and Controlling LLM Agents in One Click](https://arxiv.org/abs/2608.26867) ⭐️ 7.0/10

原文摘要：arXiv:2608.26867v1 Announce Type: new Abstract: Large language model agents reason, call tools, and act autonomously over many steps, but their agentic skills-correctly sequencing tools, planning under dependencies, judging untrusted inputs, and grounding generated arguments-are hard to measure with accuracy-only...

rss · arXiv cs.AI · Aug 28, 04:00

**背景**: 来自 arXiv cs.AI 的最新内容。

**标签**: `#agent`, `#model`, `#inference`, `#research`

---

<a id="item-17"></a>
## [ProvenanceGuard: Source-Aware Factuality Verification for MCP-Based LLM Agents](https://arxiv.org/abs/2606.18037) ⭐️ 7.0/10

原文摘要：arXiv:2606.18037v3 Announce Type: replace-cross Abstract: Tool-using LLM agents increasingly use the Model Context Protocol (MCP) to answer from heterogeneous evidence sources, including search, APIs, databases, clinical records, and formulary tools. Standard factuality metrics usually test whether an answer is...

rss · arXiv cs.CL · Aug 28, 04:00

**背景**: 来自 arXiv cs.CL 的最新内容。

**标签**: `#mcp`, `#agent`, `#model`, `#research`

---

<a id="item-18"></a>
## [ClueWeaver: Reward-Guided Dual-Agent Evidence Reasoning for Compact LLMs on Literary Long Narratives](https://arxiv.org/abs/2608.25531) ⭐️ 7.0/10

原文摘要：arXiv:2608.25531v2 Announce Type: replace Abstract: Humanities and social science research requires close reading of long narrative materials such as novels, scripts, archives, and case reports, yet many users have limited access to costly proprietary long-context models. Compact, locally deployable language models...

rss · arXiv cs.CL · Aug 28, 04:00

**背景**: 来自 arXiv cs.CL 的最新内容。

**标签**: `#agent`, `#model`, `#inference`, `#research`

---