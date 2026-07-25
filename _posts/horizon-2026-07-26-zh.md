# Horizon 每日速递 - 2026-07-26

> 从 189 条内容中按规则筛选出 12 条重要资讯。

---

1. [vllm-project/vllm released v0.26.0](#item-1) ⭐️ 8.6/10
2. [Add gate402-mcp (compute + LLM inference + Base data over x402)](#item-2) ⭐️ 8.4/10
3. [ollama/ollama released v0.32.4](#item-3) ⭐️ 8.2/10
4. [Add crimson-crab-mcp-template (Rust, Claude via crimson-crab)](#item-4) ⭐️ 8.1/10
5. [Introducing Claude Opus 5](#item-5) ⭐️ 7.8/10
6. [anomalyco/opencode released v1.18.5](#item-6) ⭐️ 7.7/10
7. [The new rules of context engineering for Claude 5 generation models](#item-7) ⭐️ 7.7/10
8. [(AINews) Claude Opus 5: Fable-level performance at Opus price (half Fable)](#item-8) ⭐️ 7.7/10
9. [Merge pull request #8995 from pgalyen1987/add-gate402-mcp](#item-9) ⭐️ 7.7/10
10. [Ruff v0.16.0](#item-10) ⭐️ 7.4/10
11. [Quoting Boris Cherny](#item-11) ⭐️ 7.4/10
12. [Euclid-MCP: A Model Context Protocol Server for Deterministic Logical Reasoning via Prolog](#item-12) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [vllm-project/vllm released v0.26.0](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 8.6/10

原文摘要：# vLLM v0.26.0 Release Notes ## Highlights This release features 411 commits from 212 contributors (61 new)! * **New Inkling model family** with a full support stack: base modeling (#48799), piecewise CUDA graph support (#48822), Hopper FA4 relative attention (#48858), MTP=1 speculative decoding (#48869), LoRA...

github · khluu · Jul 25, 10:38

**背景**: 项目 vllm-project/vllm 发布 v0.26.0。

**标签**: `#model`, `#inference`, `#open-source`

---

<a id="item-2"></a>
## [Add gate402-mcp (compute + LLM inference + Base data over x402)](https://github.com/punkpeye/awesome-mcp-servers/commit/d26995c2bbce996ee288c2cb98ddf38fedb2611c) ⭐️ 8.4/10

原文摘要：Add gate402-mcp (compute + LLM inference + Base data over x402) Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>

rss · Awesome MCP Servers · Jul 25, 17:50

**背景**: 来自 Awesome MCP Servers 的最新内容。

**标签**: `#mcp`, `#model`, `#inference`

---

<a id="item-3"></a>
## [ollama/ollama released v0.32.4](https://github.com/ollama/ollama/releases/tag/v0.32.4) ⭐️ 8.2/10

原文摘要：## What's Changed - Support Laguna on Apple GPUs via the MLX engine - Quantize draft-model output heads at the requested type when creating speculative-decoding drafts. - Fixed Qwen3 MoE decoding for differently-quantized experts, plus faster packed gate/up projection (~4–9% on M5 Max). **Full Changelog**:...

github · github-actions[bot] · Jul 25, 02:22

**背景**: 项目 ollama/ollama 发布 v0.32.4。

**标签**: `#inference`, `#open-source`

---

<a id="item-4"></a>
## [Add crimson-crab-mcp-template (Rust, Claude via crimson-crab)](https://github.com/punkpeye/awesome-mcp-servers/commit/ecb1d782ce1ecbd499adc38fb77f642f323959b7) ⭐️ 8.1/10

原文摘要：Add crimson-crab-mcp-template (Rust, Claude via crimson-crab)

rss · Awesome MCP Servers · Jul 25, 17:28

**背景**: 来自 Awesome MCP Servers 的最新内容。

**标签**: `#mcp`, `#model`

---

<a id="item-5"></a>
## [Introducing Claude Opus 5](https://simonwillison.net/2026/Jul/24/introducing-claude-opus-5/#atom-everything) ⭐️ 7.8/10

原文摘要：Introducing Claude Opus 5 I've been offline kayaking with sea otters for much of today so I haven't had a chance to put Anthropic's new model Claude Opus 5 through its paces yet. The buzz is positive, and Anthropic's description of it as a "thoughtful and proactive model that comes close to the frontier...

rss · Simon Willison · Jul 24, 23:48

**背景**: 来自 Simon Willison 的最新内容。

**标签**: `#model`, `#ai-engineering`

---

<a id="item-6"></a>
## [anomalyco/opencode released v1.18.5](https://github.com/anomalyco/opencode/releases/tag/v1.18.5) ⭐️ 7.7/10

原文摘要：## Core ### Bugfixes - Improve Claude adaptive thinking handling across more response shapes. - Avoid OpenAI Responses phase handling that could break some conversations. - Preserve grep symlink paths in search results. (@remixz) - Preserve Mistral reasoning history across turns. - Stabilize Mistral prompt caching....

github · opencode-agent[bot] · Jul 24, 22:18

**背景**: 项目 anomalyco/opencode 发布 v1.18.5。

**标签**: `#open-source`

---

<a id="item-7"></a>
## [The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) ⭐️ 7.7/10

原文摘要：The new rules of context engineering for Claude 5 generation models

hackernews · mellosouls · Jul 25, 20:42 · [社区讨论](https://news.ycombinator.com/item?id=49051361)

**社区讨论**: 社区热度 117，讨论 69 条。

**标签**: `#model`

---

<a id="item-8"></a>
## [(AINews) Claude Opus 5: Fable-level performance at Opus price (half Fable)](https://www.latent.space/p/ainews-claude-opus-5-fable-level) ⭐️ 7.7/10

原文摘要：ain't nobody beats Anthropic at distilling Fable!

rss · Latent Space · Jul 25, 07:25

**背景**: 来自 Latent Space 的最新内容。

**标签**: `#model`, `#ai-industry`

---

<a id="item-9"></a>
## [Merge pull request #8995 from pgalyen1987/add-gate402-mcp](https://github.com/punkpeye/awesome-mcp-servers/commit/827b9118219ff374707cc60cd14b5c1e15d5b691) ⭐️ 7.7/10

原文摘要：Merge pull request #8995 from pgalyen1987/add-gate402-mcp Add gate402-mcp (Search & Data Extraction) 🤖🤖🤖

rss · Awesome MCP Servers · Jul 25, 18:00

**背景**: 来自 Awesome MCP Servers 的最新内容。

**标签**: `#mcp`

---

<a id="item-10"></a>
## [Ruff v0.16.0](https://simonwillison.net/2026/Jul/25/ruff/#atom-everything) ⭐️ 7.4/10

原文摘要：Ruff v0.16.0 Astral shipped a significant new version of their Ruff Python linting tool a few days ago on July 23rd. I noticed today because my various CI jobs all started failing thanks to new default Ruff checks and my unpinned "ruff" dev dependency. From Brent Westbrook's announcement post: Ruff now enables 413...

rss · Simon Willison · Jul 25, 22:44

**背景**: 来自 Simon Willison 的最新内容。

**标签**: `#ai-engineering`

---

<a id="item-11"></a>
## [Quoting Boris Cherny](https://simonwillison.net/2026/Jul/25/boris-cherny/#atom-everything) ⭐️ 7.4/10

原文摘要：More than any of these eval scores, what is most exciting to me is something else: Opus 5 is our least prompt injectable model yet. It is a bit buried in the system card, but across PI evals and red teaming, Opus 5 is very hard to prompt inject successfully. — Boris Cherny , here's that System Card section , page...

rss · Simon Willison · Jul 25, 00:42

**背景**: 来自 Simon Willison 的最新内容。

**标签**: `#ai-engineering`

---

<a id="item-12"></a>
## [Euclid-MCP: A Model Context Protocol Server for Deterministic Logical Reasoning via Prolog](https://arxiv.org/abs/2607.21412) ⭐️ 7.0/10

原文摘要：arXiv:2607.21412v1 Announce Type: cross Abstract: Large Language Models (LLMs) excel at natural language understanding and generation but remain unreliable for multi-step logical reasoning, especially in safety-critical or compliance-sensitive domains. Recent neuro-symbolic approaches address this gap by coupling...

rss · arXiv cs.CL · Jul 25, 04:00

**背景**: 来自 arXiv cs.CL 的最新内容。

**标签**: `#mcp`, `#model`, `#inference`, `#research`

---

