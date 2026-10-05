# Horizon 每日速递 - 2026-10-05

> 从 34 条内容中按规则筛选出 8 条重要资讯。

---

1. [Merge pull request #4939 from modelcontextprotocol/v2/chore/4938-cont…](#item-1) ⭐️ 8.5/10
2. [Run Qwen 3.8 Flash Next (125B) on consumer hardware (RTX 4090) at 100T/s](#item-2) ⭐️ 8.3/10
3. [chore: sync the bug report form with v2/main after #4965](#item-3) ⭐️ 8.1/10
4. [chore: sync the PR template with v2/main after #4961](#item-4) ⭐️ 8.1/10
5. [ggml-org/llama.cpp released b11401](#item-5) ⭐️ 7.4/10
6. [ggml-org/llama.cpp released b11400](#item-6) ⭐️ 7.4/10
7. [ggml-org/llama.cpp released b11399](#item-7) ⭐️ 7.4/10
8. [We're going to need default hard budget caps on pretty much everything](#item-8) ⭐️ 7.4/10

---

<a id="item-1"></a>
## [Merge pull request #4939 from modelcontextprotocol/v2/chore/4938-cont…](https://github.com/modelcontextprotocol/servers/commit/5abed86c5317b833dd59907492d56c65981642aa) ⭐️ 8.5/10

原文摘要：Merge pull request #4939 from modelcontextprotocol/v2/chore/4938-contribution-policy-to-main chore: bring the contribution policy to main ahead of the v2.0.0 merge

rss · MCP Reference Servers · Oct 4, 04:01

**背景**: 来自 MCP Reference Servers 的最新内容。

**标签**: `#model`, `#mcp`

---

<a id="item-2"></a>
## [Run Qwen 3.8 Flash Next (125B) on consumer hardware (RTX 4090) at 100T/s](https://github.com/Niko1221/Strata) ⭐️ 8.3/10

原文摘要：Run Qwen 3.8 Flash Next (125B) on consumer hardware (RTX 4090) at 100T/s

hackernews · snehesht · Oct 4, 12:51 · [社区讨论](https://news.ycombinator.com/item?id=49953495)

**社区讨论**: 社区热度 611，讨论 284 条。

**标签**: `#model`

---

<a id="item-3"></a>
## [chore: sync the bug report form with v2/main after #4965](https://github.com/modelcontextprotocol/servers/commit/a20778763c78013ee61696f6c3cd7e76f51f81f6) ⭐️ 8.1/10

原文摘要：chore: sync the bug report form with v2/main after #4965 Takes .github/ISSUE_TEMPLATE/1-bug_report.yml from v2/main, whose Server version placeholder now shows both version schemes (#4964), so this branch stays byte-identical to v2/main. Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com> Signed-off-by:...

rss · MCP Reference Servers · Oct 4, 03:59

**背景**: 来自 MCP Reference Servers 的最新内容。

**标签**: `#mcp`

---

<a id="item-4"></a>
## [chore: sync the PR template with v2/main after #4961](https://github.com/modelcontextprotocol/servers/commit/e4e721e3f81be0bcebd7379af4d06fbe60607ef8) ⭐️ 8.1/10

原文摘要：chore: sync the PR template with v2/main after #4961 Takes .github/pull_request_template.md from v2/main, which reduced it to the issues-not-PRs banner (#4960), so this branch stays byte-identical to v2/main. Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com> Signed-off-by: cliffhall <cliff@futurescale.com>

rss · MCP Reference Servers · Oct 4, 03:35

**背景**: 来自 MCP Reference Servers 的最新内容。

**标签**: `#mcp`

---

<a id="item-5"></a>
## [ggml-org/llama.cpp released b11401](https://github.com/ggml-org/llama.cpp/releases/tag/b11401) ⭐️ 7.4/10

原文摘要：log, server: self contained colors, split child commands from logs in router mode (#29895) * log, server: make router child lines carry their own colors The logger writes the color reset after the trailing newline, so the reset opens the next line. On the shared pipe of a router child it lands in front of the next...

github · github-actions[bot] · Oct 5, 00:36

**背景**: 项目 ggml-org/llama.cpp 发布 b11401。

**标签**: `#inference`, `#open-source`

---

<a id="item-6"></a>
## [ggml-org/llama.cpp released b11400](https://github.com/ggml-org/llama.cpp/releases/tag/b11400) ⭐️ 7.4/10

原文摘要：llama: support both embd + raw tokens in batch (#29622) * llama: support both embd + raw tokens in batch * add to test-llama-archs * also check case llm_arch_supports_mixed_batch = false * constant graph topology * have dedicated input for mixed case * rm set_tensor_backend * is_embd --> type * consolidate m-rope...

github · github-actions[bot] · Oct 5, 00:04

**背景**: 项目 ggml-org/llama.cpp 发布 b11400。

**标签**: `#inference`, `#open-source`

---

<a id="item-7"></a>
## [ggml-org/llama.cpp released b11399](https://github.com/ggml-org/llama.cpp/releases/tag/b11399) ⭐️ 7.4/10

原文摘要：CUDA: refactor swizzling code (#29612) * CUDA: refactor swizzling code * fix templates/loop bounds **Website:** - **Attestations:** - **macOS/iOS:** - macOS Apple Silicon (arm64) - macOS Apple Silicon (arm64, KleidiAI enabled) DISABLED - macOS Intel (x64) - iOS XCFramework **Linux:** - Ubuntu x64 (CPU) - Ubuntu...

github · github-actions[bot] · Oct 4, 22:52

**背景**: 项目 ggml-org/llama.cpp 发布 b11399。

**标签**: `#inference`, `#open-source`

---

<a id="item-8"></a>
## [We're going to need default hard budget caps on pretty much everything](https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/) ⭐️ 7.4/10

原文摘要：Here's a product feature which the world is going to need a whole lot more of over the coming months and years: default hard budget caps . I'm talking about the feature of pay-by-usage services and APIs that lets you say "after $X/month, cut this thing off and return errors". These need to be hard limits. Soft...

rss · Simon Willison · Oct 3, 23:34

**背景**: 来自 Simon Willison 的最新内容。

**标签**: `#ai-engineering`

---

