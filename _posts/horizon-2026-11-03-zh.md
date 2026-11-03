# Horizon 每日速递 - 2026-11-03

> 从 828 条内容中按规则筛选出 22 条重要资讯。

---

1. [vllm-project/vllm released v0.33.0rc3](#item-1) ⭐️ 8.6/10
2. [build(deps-dev): bump typescript-eslint from 8.72.0 to 8.72.1 (#3493)](#item-2) ⭐️ 8.4/10
3. [build(deps): bump @vitest/mocker (#3499)](#item-3) ⭐️ 8.4/10
4. [build(deps-dev): bump glob from 13.0.6 to 14.0.3 (#3494)](#item-4) ⭐️ 8.4/10
5. [Astra can read and write weights to improve Qwen](#item-5) ⭐️ 8.3/10
6. [Ubuntu still has not released patch for Linux 0day RCE in almost 3 weeks](#item-6) ⭐️ 8.2/10
7. [Introducing the Grid Protectors Program](#item-7) ⭐️ 8.2/10
8. [Rewarding defenders with bigger bug bounties](#item-8) ⭐️ 8.2/10
9. [Preparing our next security sprint to harden OpenAI](#item-9) ⭐️ 8.2/10
10. [Launch HN: Momentic (YC W24) – Agents that catch bugs by using your app](#item-10) ⭐️ 8.0/10
11. [Building Legal Agents When You Can't See the Data - Jacob Lauritzen, CTO of Legora](#item-11) ⭐️ 7.9/10
12. [llm 0.37](#item-12) ⭐️ 7.8/10
13. [ollama/ollama released v0.40.14-rc0](#item-13) ⭐️ 7.4/10
14. [ggml-org/llama.cpp released b12063](#item-14) ⭐️ 7.4/10
15. [ggml-org/llama.cpp released b12061](#item-15) ⭐️ 7.4/10
16. [ggml-org/llama.cpp released b12060](#item-16) ⭐️ 7.4/10
17. [The U.S. Census Bureau and “Super Intelligence”](#item-17) ⭐️ 7.4/10
18. [google-gemini/gemini-cli released v0.67.0-nightly.20261103.g0ac57c029](#item-18) ⭐️ 7.3/10
19. [Building AI for Lawyers - Jacob Lauritzen, CTO of Legora](#item-19) ⭐️ 7.3/10
20. [EvoMCP: Co-evolving MCP agents and training data](#item-20) ⭐️ 7.0/10
21. [When Safety Checks Become Privacy Risks: A Privacy-Preserving Paradigm for LLM Agent Safety Auditing](#item-21) ⭐️ 7.0/10
22. [MIRAGE: Auditing Anti-Muslim Bias in Frontier LLMs Across Reasoning, Agentic, and Time-Coupled Conditions](#item-22) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [vllm-project/vllm released v0.33.0rc3](https://github.com/vllm-project/vllm/releases/tag/v0.33.0rc3) ⭐️ 8.6/10

原文摘要：# v0.33.0 ## Highlights This release features 927 commits from 389 contributors (122 new)! * **New models**: Reflection Beam-1.0 (501B MoE, 23B active) with its DFlash2 drafter (#62074), Yandex AliceAI-Foundation-80B-A3B (#57963), Recursive Flint (40B MoE, 2.5B active) (#62938), Muse Spark Open (#61879), Step-5...

github · khluu · Nov 2, 10:10

**背景**: 项目 vllm-project/vllm 发布 v0.33.0rc3。

**标签**: `#model`, `#inference`, `#open-source`

---

<a id="item-2"></a>
## [build(deps-dev): bump typescript-eslint from 8.72.0 to 8.72.1 (#3493)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/a40e90cab4e50219d3274658c2b2f5c550c684c8) ⭐️ 8.4/10

原文摘要：build(deps-dev): bump typescript-eslint from 8.72.0 to 8.72.1 (#3493) Bumps typescript-eslint from 8.72.0 to 8.72.1. - Release notes - Changelog - Commits --- updated-dependencies: - dependency-name: typescript-eslint dependency-version: 8.72.1 dependency-type: direct:development update-type:...

rss · MCP Protocol Commits · Nov 3, 01:13

**背景**: 来自 MCP Protocol Commits 的最新内容。

**标签**: `#mcp`

---

<a id="item-3"></a>
## [build(deps): bump @vitest/mocker (#3499)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/8b2bb08f73611b6c8673e074014794cb352c35b0) ⭐️ 8.4/10

原文摘要：build(deps): bump @vitest/mocker (#3499) Bumps the npm_and_yarn group with 1 update in the /tools/sep-automation directory: @vitest/mocker. Updates `@vitest/mocker` from 4.1.11 to 4.1.12 - Release notes - Changelog - Commits --- updated-dependencies: - dependency-name: "@vitest/mocker" dependency-version: 4.1.12...

rss · MCP Protocol Commits · Nov 3, 01:13

**背景**: 来自 MCP Protocol Commits 的最新内容。

**标签**: `#mcp`

---

<a id="item-4"></a>
## [build(deps-dev): bump glob from 13.0.6 to 14.0.3 (#3494)](https://github.com/modelcontextprotocol/modelcontextprotocol/commit/05dc6d554639eddf39d23c21086b6e5e2e74af7b) ⭐️ 8.4/10

原文摘要：build(deps-dev): bump glob from 13.0.6 to 14.0.3 (#3494) Bumps glob from 13.0.6 to 14.0.3. - Changelog - Commits --- updated-dependencies: - dependency-name: glob dependency-version: 14.0.3 dependency-type: direct:development update-type: version-update:semver-major ... Signed-off-by: dependabot[bot]...

rss · MCP Protocol Commits · Nov 3, 00:43

**背景**: 来自 MCP Protocol Commits 的最新内容。

**标签**: `#mcp`

---

<a id="item-5"></a>
## [Astra can read and write weights to improve Qwen](https://rikiyat.github.io/blog/weight-space-programming/) ⭐️ 8.3/10

原文摘要：Astra can read and write weights to improve Qwen

hackernews · dbreunig · Nov 2, 18:21 · [社区讨论](https://news.ycombinator.com/item?id=50341174)

**社区讨论**: 社区热度 2125，讨论 691 条。

**标签**: `#model`

---

<a id="item-6"></a>
## [Ubuntu still has not released patch for Linux 0day RCE in almost 3 weeks](https://freenode.net/article/ubuntu-lts-kernels-still-unfixed-for-critical-cve-2026-98432) ⭐️ 8.2/10

原文摘要：Ubuntu still has not released patch for Linux 0day RCE in almost 3 weeks

hackernews · majorchord · Nov 2, 18:39 · [社区讨论](https://news.ycombinator.com/item?id=50341462)

**社区讨论**: 社区热度 376，讨论 101 条。

**标签**: `#open-source`

---

<a id="item-7"></a>
## [Introducing the Grid Protectors Program](https://openai.com/index/grid-protectors-program) ⭐️ 8.2/10

原文摘要：OpenAI’s Grid Protectors Program will work with utilities to help future compute campuses support grid reliability and protect consumer electricity costs.

rss · OpenAI News · Nov 2, 15:00

**背景**: 来自 OpenAI News 的最新内容。

**标签**: `#frontier-labs`

---

<a id="item-8"></a>
## [Rewarding defenders with bigger bug bounties](https://openai.com/index/rewarding-defenders-with-bigger-bug-bounties) ⭐️ 8.2/10

原文摘要：OpenAI is raising Security Bug Bounty rewards and introducing report quality, loyalty, and priority campaign bonuses for independent security researchers.

rss · OpenAI News · Nov 2, 18:00

**背景**: 来自 OpenAI News 的最新内容。

**标签**: `#frontier-labs`

---

<a id="item-9"></a>
## [Preparing our next security sprint to harden OpenAI](https://openai.com/index/preparing-our-next-security-sprint-to-harden-openai) ⭐️ 8.2/10

原文摘要：OpenAI is preparing its next internal security sprint with Cathedral Systems to test and strengthen its defenses using AI.

rss · OpenAI News · Nov 2, 18:00

**背景**: 来自 OpenAI News 的最新内容。

**标签**: `#frontier-labs`

---

<a id="item-10"></a>
## [Launch HN: Momentic (YC W24) – Agents that catch bugs by using your app](https://momentic.ai/) ⭐️ 8.0/10

原文摘要：Hey HN, we’re Wei-Wei and Jeff. We’re building Momentic, QA agents that autonomously plan, explore, and bug-bash controls and user flows in your web, iOS, Android, and (soon) desktop apps to catch bugs. Here’s a demo: https://youtu.be/BFsM-Se1Fh8 We’re both software engineers that spent our careers on dev tooling...

hackernews · wuweiweiwu · Nov 2, 17:05 · [社区讨论](https://news.ycombinator.com/item?id=50339913)

**社区讨论**: 社区热度 131，讨论 88 条。

**标签**: `#agent`

---

<a id="item-11"></a>
## [Building Legal Agents When You Can't See the Data - Jacob Lauritzen, CTO of Legora](https://latent.space/p/building_legal_agents_when_you_can_t_see_the_data_-_jacob_lauritzen_cto_of_legora/) ⭐️ 7.9/10

原文摘要：Legora can’t read a single trace of what its agent does for a lawyer. The data belongs to the law firm’s clients. How do you build and test an agent when you can’t see its work? Jacob Lauritzen is the CTO of Legora, one of the fastest-growing companies...

rss · Latent Space · Nov 2, 22:54

**背景**: 来自 Latent Space 的最新内容。

**标签**: `#agent`, `#ai-industry`

---

<a id="item-12"></a>
## [llm 0.37](https://simonwillison.net/2026/Nov/2/llm/) ⭐️ 7.8/10

原文摘要：Release: llm 0.37 There's a lot of stuff in this new release of my LLM CLI tool and Python library, representing around two months of accumulated features and fixes. I added gpt-6.1-sol and gpt-6.1-terra , plus a new llm openai endpoint add command to make it easier to configure additional models that use...

rss · Simon Willison · Nov 2, 23:49

**背景**: 来自 Simon Willison 的最新内容。

**标签**: `#model`, `#ai-engineering`

---

<a id="item-13"></a>
## [ollama/ollama released v0.40.14-rc0](https://github.com/ollama/ollama/releases/tag/v0.40.14-rc0) ⭐️ 7.4/10

原文摘要：## What's Changed * ci: pin buildx to workaround deadlock by @dhiltgen in https://github.com/ollama/ollama/pull/19373 * openai: preserve readable Responses input content by @hoyyeva in https://github.com/ollama/ollama/pull/19192 * mlx: sort long top-k rows in chunks by @dhiltgen in...

github · github-actions[bot] · Nov 3, 01:40

**背景**: 项目 ollama/ollama 发布 v0.40.14-rc0。

**标签**: `#inference`, `#open-source`

---

<a id="item-14"></a>
## [ggml-org/llama.cpp released b12063](https://github.com/ggml-org/llama.cpp/releases/tag/b12063) ⭐️ 7.4/10

原文摘要：dflash: copy hidden features via device copies (#31506) **Website:** - **Attestations:** - **macOS/iOS:** - macOS Apple Silicon (arm64) - macOS Apple Silicon (arm64, KleidiAI enabled) DISABLED - macOS Intel (x64) - iOS XCFramework **Linux:** - Ubuntu x64 (CPU) - Ubuntu arm64 (CPU) - Ubuntu s390x (CPU) - Ubuntu...

github · github-actions[bot] · Nov 3, 01:39

**背景**: 项目 ggml-org/llama.cpp 发布 b12063。

**标签**: `#inference`, `#open-source`

---

<a id="item-15"></a>
## [ggml-org/llama.cpp released b12061](https://github.com/ggml-org/llama.cpp/releases/tag/b12061) ⭐️ 7.4/10

原文摘要：mtmd: Pocket tts - support for voices without voice cloning (#31429) * feat: support PocketTTS voices with no voice cloning The kyutai/pocket-tts-without-voice-cloning weights ship predefined voices as the backbone KV state after the voice prompt. The converter turns each state back into the prompt embeddings and...

github · github-actions[bot] · Nov 2, 23:17

**背景**: 项目 ggml-org/llama.cpp 发布 b12061。

**标签**: `#inference`, `#open-source`

---

<a id="item-16"></a>
## [ggml-org/llama.cpp released b12060](https://github.com/ggml-org/llama.cpp/releases/tag/b12060) ⭐️ 7.4/10

原文摘要：model: add Clover support (#31306) * model : add AR-only Clover MoE support Add GGUF conversion, model loading, and causal hybrid attention for Clover, reusing shared attention, recurrent-state, MoE, and LoRA helpers. * Update tests/test-llama-archs.cpp Co-authored-by: Sigbjørn Skjæret * convert : filter Clover...

github · github-actions[bot] · Nov 2, 23:00

**背景**: 项目 ggml-org/llama.cpp 发布 b12060。

**标签**: `#inference`, `#open-source`

---

<a id="item-17"></a>
## [The U.S. Census Bureau and “Super Intelligence”](https://simonwillison.net/2026/Nov/2/census-bureau-super-intelligence/) ⭐️ 7.4/10

原文摘要：I was reminded today of AI Adoption Rate Trending Down for Large Companies , a chart produced by Apollo Global Management in September 2025, which appeared to show a slowdown in U.S. corporate AI adoption based on numbers collected by the U.S. Census Bureau. At the time I used that chart to demonstrate GPT-5 data...

rss · Simon Willison · Nov 2, 13:31

**背景**: 来自 Simon Willison 的最新内容。

**标签**: `#ai-engineering`

---

<a id="item-18"></a>
## [google-gemini/gemini-cli released v0.67.0-nightly.20261103.g0ac57c029](https://github.com/google-gemini/gemini-cli/releases/tag/v0.67.0-nightly.20261103.g0ac57c029) ⭐️ 7.3/10

原文摘要：## What's Changed * fix(core): prevent interrupted Whisper model downloads from being treated as installed by @tadipavan in https://github.com/google-gemini/gemini-cli/pull/30058 **Full Changelog**:...

github · gemini-cli-robot · Nov 3, 01:18

**背景**: 项目 google-gemini/gemini-cli 发布 v0.67.0-nightly.20261103.g0ac57c029。

**标签**: `#model`, `#open-source`

---

<a id="item-19"></a>
## [Building AI for Lawyers - Jacob Lauritzen, CTO of Legora](https://latent.space/p/building-ai-for-lawyers-jacob-lauritzen-cto-of-legora/) ⭐️ 7.3/10

原文摘要：Evals without traces, million-cell tabular reviews, and cracks in the billable hour as a business model

rss · Latent Space · Nov 2, 23:01

**背景**: 来自 Latent Space 的最新内容。

**标签**: `#ai-industry`

---

<a id="item-20"></a>
## [EvoMCP: Co-evolving MCP agents and training data](https://arxiv.org/abs/2610.41479) ⭐️ 7.0/10

原文摘要：arXiv:2610.41479v1 Announce Type: new Abstract: Supervised fine-tuning of Model Context Protocol (MCP) agents is typically conducted on a static data distribution, which fails to adapt to the student's evolving capabilities and leaves newly exposed weaknesses insufficiently addressed. To address these challenges,...

rss · arXiv cs.AI · Nov 2, 05:00

**背景**: 来自 arXiv cs.AI 的最新内容。

**标签**: `#mcp`, `#agent`, `#research`

---

<a id="item-21"></a>
## [When Safety Checks Become Privacy Risks: A Privacy-Preserving Paradigm for LLM Agent Safety Auditing](https://arxiv.org/abs/2610.41401) ⭐️ 7.0/10

原文摘要：arXiv:2610.41401v1 Announce Type: cross Abstract: Large language model agents interact with online services through tool calls that may access private data or perform sensitive actions. Specialized providers can supply and maintain pre-execution safety auditing capabilities for agent operators. However, sending...

rss · arXiv cs.AI · Nov 2, 05:00

**背景**: 来自 arXiv cs.AI 的最新内容。

**标签**: `#agent`, `#model`, `#inference`, `#research`

---

<a id="item-22"></a>
## [MIRAGE: Auditing Anti-Muslim Bias in Frontier LLMs Across Reasoning, Agentic, and Time-Coupled Conditions](https://arxiv.org/abs/2606.16562) ⭐️ 7.0/10

原文摘要：arXiv:2606.16562v2 Announce Type: replace Abstract: Five years after the discovery of persistent anti-Muslim bias in large language models, most evaluations remain confined to single-turn prompt completion, a setting that no longer reflects how frontier LLMs are deployed. We introduce \textbf{MIRAGE}...

rss · arXiv cs.LG · Nov 2, 05:00

**背景**: 来自 arXiv cs.LG 的最新内容。

**标签**: `#agent`, `#model`, `#inference`, `#research`

---

