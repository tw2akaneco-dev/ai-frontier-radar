# Horizon 每日速递 - 2026-11-02

> 从 23 条内容中按规则筛选出 6 条重要资讯。

---

1. [ggml-org/llama.cpp released b12032](#item-1) ⭐️ 7.4/10
2. [ggml-org/llama.cpp released b12031](#item-2) ⭐️ 7.4/10
3. [ggml-org/llama.cpp released b12030](#item-3) ⭐️ 7.4/10
4. [If in doubt, delete the uv.lock file](#item-4) ⭐️ 7.4/10
5. [Quoting Kyle Kingsbury](#item-5) ⭐️ 7.4/10
6. [google-gemini/gemini-cli released v0.67.0-nightly.20261102.g6814e00d6](#item-6) ⭐️ 7.3/10

---

<a id="item-1"></a>
## [ggml-org/llama.cpp released b12032](https://github.com/ggml-org/llama.cpp/releases/tag/b12032) ⭐️ 7.4/10

原文摘要：sycl: Try PkgConfig for LevelZero includes / libs (#31076) **Website:** - **Attestations:** - **macOS/iOS:** - macOS Apple Silicon (arm64) - macOS Apple Silicon (arm64, KleidiAI enabled) DISABLED - macOS Intel (x64) - iOS XCFramework **Linux:** - Ubuntu x64 (CPU) - Ubuntu arm64 (CPU) - Ubuntu s390x (CPU) - Ubuntu...

github · github-actions[bot] · Nov 1, 09:00

**背景**: 项目 ggml-org/llama.cpp 发布 b12032。

**标签**: `#inference`, `#open-source`

---

<a id="item-2"></a>
## [ggml-org/llama.cpp released b12031](https://github.com/ggml-org/llama.cpp/releases/tag/b12031) ⭐️ 7.4/10

原文摘要：opencl: add initial iq3 support (#31338) * opencl: add iq3_s AOS mv Assisted-by: Codex * opencl: add iq3_s SOA mv and tiled mm Assisted-by: Codex * opencl: add iq3_s noshuffle gemm/gemv for adreno Co-authored-by: Shaofei Qi Assisted-by: Codex * opencl: add iq3_s dp4a for adreno Co-authored-by: Shaofei Qi...

github · github-actions[bot] · Nov 1, 07:41

**背景**: 项目 ggml-org/llama.cpp 发布 b12031。

**标签**: `#inference`, `#open-source`

---

<a id="item-3"></a>
## [ggml-org/llama.cpp released b12030](https://github.com/ggml-org/llama.cpp/releases/tag/b12030) ⭐️ 7.4/10

原文摘要：hexagon : fix DMA transfers with strides > 24 bits (#31442) * hexagon : fix DMA transfers with strides > 24 bits On v75+ the 2D DMA descriptor stores row_size and strides in 24 bits. dma_queue_push sent oversized strides to fallback_2d, which only splits nrows, so strides of 16 MB or more were truncated - wrong...

github · github-actions[bot] · Nov 1, 07:16

**背景**: 项目 ggml-org/llama.cpp 发布 b12030。

**标签**: `#inference`, `#open-source`

---

<a id="item-4"></a>
## [If in doubt, delete the uv.lock file](https://simonwillison.net/2026/Nov/1/delete-uv-lock-first/) ⭐️ 7.4/10

原文摘要：I've been getting the occasional confusing Python dependency error since switching over to Python 3.15 and the rule I'm having to remember is: If in doubt, delete the uv.lock file Most of my projects are libraries which don't include a uv.lock file, since it's rude for a library dependency to lock versions for...

rss · Simon Willison · Nov 1, 23:24

**背景**: 来自 Simon Willison 的最新内容。

**标签**: `#ai-engineering`

---

<a id="item-5"></a>
## [Quoting Kyle Kingsbury](https://simonwillison.net/2026/Nov/1/kyle-kingsbury/) ⭐️ 7.4/10

原文摘要：More broadly, the use of LLMs erodes trust in documentation, in software, and in the organizations which produce them. Perhaps engineers will begin to treat any new software project with suspicion—the signals we used to rely on as markers of a mature system are now easier to counterfeit. [...] In the age of LLMs,...

rss · Simon Willison · Nov 1, 16:49

**背景**: 来自 Simon Willison 的最新内容。

**标签**: `#ai-engineering`

---

<a id="item-6"></a>
## [google-gemini/gemini-cli released v0.67.0-nightly.20261102.g6814e00d6](https://github.com/google-gemini/gemini-cli/releases/tag/v0.67.0-nightly.20261102.g6814e00d6) ⭐️ 7.3/10

原文摘要：**Full Changelog**: https://github.com/google-gemini/gemini-cli/compare/v0.67.0-nightly.20261101.g6814e00d6...v0.67.0-nightly.20261102.g6814e00d6

github · gemini-cli-robot · Nov 2, 01:22

**背景**: 项目 google-gemini/gemini-cli 发布 v0.67.0-nightly.20261102.g6814e00d6。

**标签**: `#model`, `#open-source`

---

