# Horizon 每日速递 - 2026-10-13

> 从 948 条内容中按规则筛选出 20 条重要资讯。

---

1. [docs: serve the TypeScript quickstart server with serveStdio (#3427)](#item-1) ⭐️ 8.4/10
2. [How Anthropic’s Dynamic Workflows Coordinate Claude Agents](#item-2) ⭐️ 8.3/10
3. [Launch HN: Agent37 (YC F26) – Low-cost agent sandboxes for running agents](#item-3) ⭐️ 7.9/10
4. [langchain-ai/langgraph released 1.2.15](#item-4) ⭐️ 7.7/10
5. [langchain-ai/langgraph released sdk==0.4.7](#item-5) ⭐️ 7.7/10
6. [langchain-ai/langgraph released checkpointsqlite==3.1.2](#item-6) ⭐️ 7.7/10
7. [OpenHands/OpenHands released v1.27.1](#item-7) ⭐️ 7.7/10
8. [OpenHands/OpenHands released v1.27.0](#item-8) ⭐️ 7.7/10
9. [datasette-ports 0.4](#item-9) ⭐️ 7.7/10
10. [ollama/ollama released v0.40.4-rc0](#item-10) ⭐️ 7.4/10
11. [ggml-org/llama.cpp released b11577](#item-11) ⭐️ 7.4/10
12. [ggml-org/llama.cpp released b11576](#item-12) ⭐️ 7.4/10
13. [ggml-org/llama.cpp released b11575](#item-13) ⭐️ 7.4/10
14. [Hello Python 3.15, goodbye 3.10, and now I can use 3.11](#item-14) ⭐️ 7.4/10
15. [web-edit 0.1a0](#item-15) ⭐️ 7.4/10
16. [google-gemini/gemini-cli released v0.65.0-nightly.20261013.g51617c1bc](#item-16) ⭐️ 7.3/10
17. [google-gemini/gemini-cli released v0.65.0-nightly.20261012.g9b6e0265d](#item-17) ⭐️ 7.3/10
18. [Can Agents Price a Reaction? Evaluating LLMs on Chemical Cost Reasoning](#item-18) ⭐️ 7.0/10
19. [Let Large Language Models Judge Each Other: Multi-Agent Peer-Reviewed Reasoning for Medical Question Answering](#item-19) ⭐️ 7.0/10
20. [Taking Tokenization off the Host for Agentic LLM Serving](#item-20) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [docs: serve the TypeScript quickstart server with serveStdio (#3427)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/3778656b2e0ba6725035e816fe3085374cbaa736) ⭐️ 8.4/10

原文摘要：docs: serve the TypeScript quickstart server with serveStdio (#3427) * docs: serve the TypeScript quickstart server with serveStdio The 2026-07-28 "Build an MCP server" quickstart wired its TypeScript server with `server.connect(new StdioServerTransport())`, which only serves clients that open with the 2025-era...

rss · MCP Protocol Commits · Oct 12, 16:26

**背景**: 来自 MCP Protocol Commits 的最新内容。

**标签**: `#mcp`

---

<a id="item-2"></a>
## [How Anthropic’s Dynamic Workflows Coordinate Claude Agents](https://www.latent.space/p/claude-dynamic-workflows) ⭐️ 8.3/10

原文摘要：At AI Engineer New York, Anthropic drew on lessons from Unix and Linux to explain how agents can tackle bigger projects without overwhelming developers.

rss · Latent Space · Oct 12, 18:18

**背景**: 来自 Latent Space 的最新内容。

**标签**: `#agent`, `#model`, `#ai-industry`

---

<a id="item-3"></a>
## [Launch HN: Agent37 (YC F26) – Low-cost agent sandboxes for running agents](https://news.ycombinator.com/item?id=50059096) ⭐️ 7.9/10

原文摘要：Hey HN, I’m Vishnu from Agent37 ( https://agent37.com ). We build sandboxes for running AI agents at under 10% of the cost of most sandbox providers. Our customers spend an average of $0.37/month per sandbox. You can view a video walkthrough of the product here: https://youtu.be/DK5ISR2tbNo We started as one of...

hackernews · vishnukool · Oct 12, 16:46

**社区讨论**: 社区热度 116，讨论 78 条。

**标签**: `#agent`

---

<a id="item-4"></a>
## [langchain-ai/langgraph released 1.2.15](https://github.com/langchain-ai/langgraph/releases/tag/1.2.15) ⭐️ 7.7/10

原文摘要：Changes since 1.2.14 * release(langgraph): 1.2.15 (#9283) * fix(langgraph): give every message written to a messages DeltaChannel an id (#9275) * fix(langgraph): save a cached node's writes like a node that ran (#9259) * fix(langgraph): stop at an interrupt_before breakpoint when a drain is requested before it...

github · github-actions[bot] · Oct 12, 22:38

**背景**: 项目 langchain-ai/langgraph 发布 1.2.15。

**标签**: `#open-source`

---

<a id="item-5"></a>
## [langchain-ai/langgraph released sdk==0.4.7](https://github.com/langchain-ai/langgraph/releases/tag/sdk%3D%3D0.4.7) ⭐️ 7.7/10

原文摘要：Changes since sdk==0.4.6 * release(sdk-py): 0.4.7 (#9289) * release(langgraph): 1.2.15 (#9283) * fix(sdk-py): end a thread stream's run only on a root lifecycle event (#9228) * fix: order delta channel replay by task path (#8544) * release(langgraph): 1.2.14 (#9215)

github · github-actions[bot] · Oct 12, 22:54

**背景**: 项目 langchain-ai/langgraph 发布 sdk==0.4.7。

**标签**: `#open-source`

---

<a id="item-6"></a>
## [langchain-ai/langgraph released checkpointsqlite==3.1.2](https://github.com/langchain-ai/langgraph/releases/tag/checkpointsqlite%3D%3D3.1.2) ⭐️ 7.7/10

原文摘要：Changes since checkpointsqlite==3.1.1 * release(checkpoint-sqlite): 3.1.2 (#9288) * fix(checkpoint-postgres,checkpoint-sqlite): treat an empty checkpoint_id as the latest in delta history (#9262) * fix(checkpoint,checkpoint-postgres,checkpoint-sqlite): validate namespace labels before store dispatch (#9217) * fix:...

github · github-actions[bot] · Oct 12, 22:54

**背景**: 项目 langchain-ai/langgraph 发布 checkpointsqlite==3.1.2。

**标签**: `#open-source`

---

<a id="item-7"></a>
## [OpenHands/OpenHands released v1.27.1](https://github.com/OpenHands/OpenHands/releases/tag/v1.27.1) ⭐️ 7.7/10

原文摘要：## 1.27.1 (2026-10-12) ## What's Changed ### Bug Fixes * fix(docker): copy MARS web bridge modules into the image by @VascoSch92 in https://github.com/OpenHands/OpenHands/pull/18343 * fix(themes): make warning feedback theme-aware by @enyst in https://github.com/OpenHands/OpenHands/pull/18333 ### Documentation *...

github · openhands-release-bot[bot] · Oct 12, 19:33

**背景**: 项目 OpenHands/OpenHands 发布 v1.27.1。

**标签**: `#open-source`

---

<a id="item-8"></a>
## [OpenHands/OpenHands released v1.27.0](https://github.com/OpenHands/OpenHands/releases/tag/v1.27.0) ⭐️ 7.7/10

原文摘要：## 1.27.0 (2026-10-12) ## What's Changed ### Features * feat(verify-openhands): drive the mock-LLM e2e behaviors on DeepSeek and map the gaps by @enyst in https://github.com/OpenHands/OpenHands/pull/18191 * feat(verify-openhands): record videos of the browser with `browser record` by @enyst in...

github · openhands-release-bot[bot] · Oct 12, 15:06

**背景**: 项目 OpenHands/OpenHands 发布 v1.27.0。

**标签**: `#open-source`

---

<a id="item-9"></a>
## [datasette-ports 0.4](https://simonwillison.net/2026/Oct/12/datasette-ports/) ⭐️ 7.7/10

原文摘要：Release: datasette-ports 0.4 My plugin for detecting and listing all Datasette instances on the current machine now works with the latest version, and displays the detected PID as well. Knowing the PID makes it easier to attach the new Python 3.15 profiler . Tags: datasette

rss · Simon Willison · Oct 12, 04:57

**背景**: 来自 Simon Willison 的最新内容。

**标签**: `#research`, `#ai-engineering`

---

<a id="item-10"></a>
## [ollama/ollama released v0.40.4-rc0](https://github.com/ollama/ollama/releases/tag/v0.40.4-rc0) ⭐️ 7.4/10

原文摘要：## What's Changed * llama: update llama.cpp to b11521 for decision models and EmbeddingGemma 2 by @jmorganca in https://github.com/ollama/ollama/pull/18917 * server: reuse verified manifests and loaded models in inference routes by @dhiltgen in https://github.com/ollama/ollama/pull/18947 * mlx: compact restored...

github · github-actions[bot] · Oct 12, 19:00

**背景**: 项目 ollama/ollama 发布 v0.40.4-rc0。

**标签**: `#inference`, `#open-source`

---

<a id="item-11"></a>
## [ggml-org/llama.cpp released b11577](https://github.com/ggml-org/llama.cpp/releases/tag/b11577) ⭐️ 7.4/10

原文摘要：model: fix vllm d3 multi seq case (#30408) * model: fix vllm d3 multi seq case * add TODO **Website:** - **Attestations:** - **macOS/iOS:** - macOS Apple Silicon (arm64) - macOS Apple Silicon (arm64, KleidiAI enabled) DISABLED - macOS Intel (x64) - iOS XCFramework **Linux:** - Ubuntu x64 (CPU) - Ubuntu arm64 (CPU)...

github · github-actions[bot] · Oct 12, 22:55

**背景**: 项目 ggml-org/llama.cpp 发布 b11577。

**标签**: `#inference`, `#open-source`

---

<a id="item-12"></a>
## [ggml-org/llama.cpp released b11576](https://github.com/ggml-org/llama.cpp/releases/tag/b11576) ⭐️ 7.4/10

原文摘要：graph: pad the KV dimension of the no-cache attention to 256 (#30416) The no-cache path builds a [n_tokens, n_tokens] mask and passes K and V unpadded, so FLASH_ATTN_EXT sees K->ne[1] == n_tokens. The CUDA kernels for head size 512 require a multiple of FATTN_KQ_STRIDE, so the op falls back to the CPU for most...

github · github-actions[bot] · Oct 12, 21:30

**背景**: 项目 ggml-org/llama.cpp 发布 b11576。

**标签**: `#inference`, `#open-source`

---

<a id="item-13"></a>
## [ggml-org/llama.cpp released b11575](https://github.com/ggml-org/llama.cpp/releases/tag/b11575) ⭐️ 7.4/10

原文摘要：metal: fix metal tensor kernel_mul_mm error for large tensor (#28748) * metal: fix metal tensor kernel_mul_mm error for large tensor Assisted-by: Codex * Update ggml/src/ggml-metal/kernels/mul_mm.metal Co-authored-by: YiChen Lv --------- Co-authored-by: 向锡铭 Co-authored-by: YiChen Lv **Website:** - **Attestations:**...

github · github-actions[bot] · Oct 12, 20:43

**背景**: 项目 ggml-org/llama.cpp 发布 b11575。

**标签**: `#inference`, `#open-source`

---

<a id="item-14"></a>
## [Hello Python 3.15, goodbye 3.10, and now I can use 3.11](https://simonwillison.net/2026/Oct/12/python-3-15/) ⭐️ 7.4/10

原文摘要：Python 3.15 is here ! Here's the essential What's new in Python 3.15 guide, this year curated by 3.14 and 3.15 release manager Hugo van Kemenade. As someone who builds open source software that works in every supported Python version, I get to say goodbye to Python 3.10 and start embracing features from Python...

rss · Simon Willison · Oct 12, 18:15

**背景**: 来自 Simon Willison 的最新内容。

**标签**: `#ai-engineering`

---

<a id="item-15"></a>
## [web-edit 0.1a0](https://simonwillison.net/2026/Oct/12/web-edit/) ⭐️ 7.4/10

原文摘要：Release: web-edit 0.1a0 I was working on a project from my phone using Codex Remote when I found myself wanting to edit a credentials file without round-tripping those credentials through the LLM itself. So... I had Codex and GPT-6 Astra Extra High build this Python web app which provides a web UI for viewing and...

rss · Simon Willison · Oct 12, 15:54

**背景**: 来自 Simon Willison 的最新内容。

**标签**: `#ai-engineering`

---

<a id="item-16"></a>
## [google-gemini/gemini-cli released v0.65.0-nightly.20261013.g51617c1bc](https://github.com/google-gemini/gemini-cli/releases/tag/v0.65.0-nightly.20261013.g51617c1bc) ⭐️ 7.3/10

原文摘要：## What's Changed * fix(cli): keep loading other extensions when one fails the allowlist check by @jesussamuel-byte in https://github.com/google-gemini/gemini-cli/pull/29720 **Full Changelog**: https://github.com/google-gemini/gemini-cli/compare/v0.65.0-nightly.20261012.g9b6e0265d...v0.65.0-nightly.20261013.g51617c1bc

github · gemini-cli-robot · Oct 13, 01:36

**背景**: 项目 google-gemini/gemini-cli 发布 v0.65.0-nightly.20261013.g51617c1bc。

**标签**: `#model`, `#open-source`

---

<a id="item-17"></a>
## [google-gemini/gemini-cli released v0.65.0-nightly.20261012.g9b6e0265d](https://github.com/google-gemini/gemini-cli/releases/tag/v0.65.0-nightly.20261012.g9b6e0265d) ⭐️ 7.3/10

原文摘要：**Full Changelog**: https://github.com/google-gemini/gemini-cli/compare/v0.65.0-nightly.20261010.g9b6e0265d...v0.65.0-nightly.20261012.g9b6e0265d

github · gemini-cli-robot · Oct 12, 01:29

**背景**: 项目 google-gemini/gemini-cli 发布 v0.65.0-nightly.20261012.g9b6e0265d。

**标签**: `#model`, `#open-source`

---

<a id="item-18"></a>
## [Can Agents Price a Reaction? Evaluating LLMs on Chemical Cost Reasoning](https://arxiv.org/abs/2605.07251) ⭐️ 7.0/10

原文摘要：arXiv:2605.07251v2 Announce Type: replace Abstract: Large Language Models (LLMs) have become increasingly capable as tool-using agents, with benchmarks spanning diverse general agentic tasks. Yet rigorous evaluation of scientific tool use remains limited. In chemistry, recent agents can plan syntheses and invoke...

rss · arXiv cs.AI · Oct 12, 04:00

**背景**: 来自 arXiv cs.AI 的最新内容。

**标签**: `#agent`, `#model`, `#inference`, `#research`

---

<a id="item-19"></a>
## [Let Large Language Models Judge Each Other: Multi-Agent Peer-Reviewed Reasoning for Medical Question Answering](https://arxiv.org/abs/2606.15419) ⭐️ 7.0/10

原文摘要：arXiv:2606.15419v2 Announce Type: replace-cross Abstract: Objective: To enhance the accuracy, interpretability, and robustness of large language models (LLMs) in medical question answering (MedQA). Method: We designed a multi-agent peer-reviewed reasoning method in which multiple LLM agents independently generate...

rss · arXiv cs.AI · Oct 12, 04:00

**背景**: 来自 arXiv cs.AI 的最新内容。

**标签**: `#agent`, `#model`, `#inference`, `#research`

---

<a id="item-20"></a>
## [Taking Tokenization off the Host for Agentic LLM Serving](https://arxiv.org/abs/2610.13325) ⭐️ 7.0/10

原文摘要：arXiv:2610.13325v1 Announce Type: cross Abstract: Agentic workloads resend long contexts that barely change between calls. Prefix caching now skips most of their prefill, yet every request must still be tokenized in full before the cache can even be consulted. Tokenization, a CPU stage long treated as negligible,...

rss · arXiv cs.LG · Oct 12, 04:00

**背景**: 来自 arXiv cs.LG 的最新内容。

**标签**: `#agent`, `#model`, `#inference`, `#research`

---

