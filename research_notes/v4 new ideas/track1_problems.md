# Track 1 candidate problems: self-improving agent team on Luminal Cloud

c0mpiled-15, Penn State, 2026-10-11. Judged on **relative improvement on fresh held-out tests** and **problem difficulty**. Judge: Joe Fioti (Luminal: search-based ML compiler, kernel search, megakernels, inference cloud).

**Method caveat:** I used WebSearch only. WebFetch failed with DNS errors (`ENOTFOUND blog.luminal.com`, `ENOTFOUND luminal.com`), so I read no primary page in full. Every claim below comes from search-result extracts, and each is cited to the URL the extract came from. Numbers marked (unverified) appeared in only one secondary source. I found no public page for the c0mpiled-15 event itself.

---

## 0. Luminal context (what the judge cares about)

- **Compiler approach:** Luminal is an open-source Rust compiler. It reduces models to a small set of primitive ops, then *searches* over logically equivalent kernels instead of applying fixed passes. In their words: "We do that without using LLMs or AI - rather, we pose it as a search problem... generates millions of possible kernels, and then searches through it to minimize runtime." ([HN Show HN](https://hn.svelte.dev/item/44963135), [AI Engineer talk](https://www.ai.engineer/talks/luminal-search-based-deep-learning-compilers-joe-fioti)).
- **Search mechanics:** A job listing describes it as a small IR, plus candidates from equality-saturation rewrite rules (tiling, unrolling, vectorization, memory layout), guided by "cost models and bandit style search". A wiki says op selection is written as egglog rewrites (secondary source) ([3b1b Talent](https://www.3blue1brown.com/talent/luminal), [aiwiki](https://aiwiki.ai/wiki/luminal)).
- **Claims:** The search rediscovers a FlashAttention-style fusion from naive attention. aiwiki notes the demo had no reproducible budget or timing. Luminal is moving to "2.0" with large-scale kernel search in `crates/luminal_2` ([gitee mirror](https://gitee.com/mirrors/luminal), [aiwiki](https://aiwiki.ai/wiki/luminal)).
- **Megakernels:** Their blog post "Compiling Models to Megakernels" fuses a whole model into one kernel with a dynamic global instruction queue, building on Hazy Research's Llama-1B megakernel ([aiwiki](https://aiwiki.ai/wiki/luminal), [Hazy Research](https://hazyresearch.stanford.edu/blog/2025-05-27-no-bubbles)).
- **Company:** YC S25. A $5.3M seed led by Felicis. Cofounders are Joe Fioti (CEO), Matthew Gunton and Jake Stevens. Luminal Cloud is serverless inference with auto-batching and scale-to-zero, in early access ([extruct](https://extruct.ai/hub/luminalai-com/), [apis.io](https://apis.io/providers/luminal/), [toolradar](https://toolradar.com/tools/luminal)). Caplight lists $5.8M total ([Caplight](https://www.caplight.com/company/luminalai)).
- **Where agents fit:** Luminal's search is LLM-free and works at the level of IR rewrite rules. An LLM agent team helps in three places. It can propose *new rewrite rules or schedule templates* that open the search space. It can write *cost-model heuristics and priors* for the bandit. It can work on the *non-compiler* layers (serving configs, batching policy) that the compiler does not touch. Pitch it as "LLM agents as the outer loop around a search compiler," not as a replacement for search. That is the framing most likely to land with this judge.

### Luminal API: is it OpenAI-compatible? What are the rate limits?
- **Not verified.** No search turned up docs.luminal.com or a description of the API format. Directory listings only describe "serverless endpoints" from HF models ([apis.io](https://apis.io/providers/luminal/), [toolradar](https://toolradar.com/tools/luminal)).
- **Upstream limits for reference, not Luminal's own:** DeepSeek reportedly uses dynamic, account-level *concurrency* limits rather than published RPM/TPM, and returns HTTP 429 when exceeded. GLM/Z.ai publishes no tiered table ([fast.io](https://fast.io/resources/deepseek-rate-limit/), [layer3labs](https://www.layer3labs.io/guides/glm-5-2-limits)).
- **Engineering plan:** Write a thin `llm()` adapter. Try `openai.OpenAI(base_url=..., api_key=...)` first, and fall back to raw `requests` if the schema differs. Add an `asyncio.Semaphore` cap of about 8 to 16 concurrent calls, exponential backoff on 429 and 5xx, an on-disk response cache keyed by prompt hash, and a token counter per round. Ask the organizers for the base URL, model IDs, max concurrency and context length at kickoff.

---

## Ranking summary

| # | Problem | Scorer | Fresh held-out | CPU eval time | Judge fit | Difficulty story |
|---|---|---|---|---|---|---|
| 1 | CPU tensor-kernel / schedule optimization ("KernelBench-CPU-lite") | speedup vs numpy/torch-CPU, gated by allclose | new shapes, new random op-graph compositions | ~0.1 to 2 s | **highest** | KernelBench: frontier models beat PyTorch in fewer than 20% of cases |
| 2 | AlgoTune-style numerical code speedups | speedup vs SciPy/sklearn reference + verifier | held-out tasks + new random instances | ~1 s | high | models make "surface-level" changes, avg 1.58x |
| 3 | LLM-serving config/policy search on a simulator (Vidur) | cost/throughput under SLO in the simulator | new request traces, models, SLOs | seconds | **very high** (Luminal Cloud) | real search took 42K GPU-h; configs don't transfer across traces |
| 4 | Cache eviction policy on real traces | miss ratio vs LRU/ARC/S3-FIFO | held-out traces and cache sizes | seconds | medium | decades of human heuristics; PolicySmith/Vulcan |
| 5 | Combinatorial heuristics (bin packing, CVRP, ALE-Bench AHC) | excess bins / gap to BKS / AHC score | generator-sampled instances | seconds | medium | NP-hard; FunSearch/AlphaEvolve lineage |
| 6 | DuckDB SQL rewrite | latency ratio + result equality | new templated TPC-H/DS queries | ~0.1 to 1 s at SF0.1 to 1 | medium | E3-Rewrite and LLM-R2 still leave gaps; equivalence is hard |
| 7 | Prompt/agent-program optimization (GEPA-style) | task accuracy/F1 | standard train/val/test splits | LLM-bound | medium-low | well-trodden; GEPA already strong |
| 8 | Format-aware compression transform search (OpenZL) | compression ratio at a speed floor | new files of the same format | seconds | medium | Meta's production work |

---

## 1. CPU tensor-kernel / schedule optimization (TOP PICK)

**Task:** Give each agent a small op graph: matmul+bias+GELU, softmax, LayerNorm, attention block, conv1d, or a fused residual MLP. It writes a faster CPU implementation, either as a schedule/tiling choice or as code in numba, numpy or C via `cffi`. Score it against the torch-CPU or numpy reference.
- **Benchmarks:** [KernelBench](https://scalingintelligence.stanford.edu/pubs/kernelbench) ([arXiv 2502.10517](https://arxiv.org/pdf/2502.10517)) has 250 PyTorch workloads at three levels: single ops, fused sequences, full architectures. Its metric is `fast_p`, the share that is correct *and* faster than PyTorch by more than a factor p. KernelBench is GPU/CUDA-oriented, and I found no CPU backend. [MultiKernelBench](https://arxiv.org/pdf/2507.17773) has a pluggable backend interface, but I could not confirm a CPU backend. [TritonBench](https://papers.cool/arxiv/2502.14752) has 184 real Triton ops and is GPU-only. **Feasible on a laptop:** port KernelBench Level-1/2 problem *definitions* (the PyTorch `Model` classes) and run them on CPU, with candidates in numba, numpy or C. You build the harness yourself in about an hour.
- **Fresh held-out:** Randomize shapes, including odd and non-power-of-2 sizes, dtypes and strides. Randomly *compose* new op chains from a grammar of primitives, which mirrors Luminal's primitive-op IR. Held-out graphs never appear in training rounds.
- **Baseline:** torch-CPU eager, numpy, and optionally `torch.compile` on CPU as a strong reference.
- **Plausible gain in 3 to 5 rounds:** Fusion of elementwise chains, cache-blocked matmul, avoiding temporaries and parallel numba usually give 1.2x to 3x on L2-style fused ops versus eager. Gains on single big GEMMs against MKL will be near 1x, so report those honestly.
- **Difficulty argument:** KernelBench reports frontier models matched the PyTorch baseline in **fewer than 20%** of cases, and that difficulty rises with p ([Stanford](https://scalingintelligence.stanford.edu/pubs/kernelbench)).
- **Reward hacking is the main risk, and also a demo point.** Sakana's AI CUDA Engineer claimed up to 100x, then admitted reward hacking: a memory exploit skipped the correctness check. A 2026 re-analysis says the aggregate fell from 3.13x to 1.49x after excluding cheaters (unverified) ([TechCrunch via kowatek](https://blog.kowatek.com/?p=99251), [Kernel Contracts](https://arxiv.org/pdf/2604.22032), [KernelBench v0.1](https://scalingintelligence.stanford.edu/blogs/kernelbenchv01)). Mitigations: fresh random inputs on every eval, an output buffer the candidate cannot alias, a timing harness in a separate process, multiple input seeds, and a check that the output is not constant.
- **Why Joe:** This is Luminal's problem domain. Pitch: "agents propose rewrite rules and schedules, and the search/eval loop is the judge," which is the LLM complement to an LLM-free search compiler.
- **Market:** Kernel and inference efficiency compounds over the inference market, about $106B in 2025 growing to about $255B by 2030 (single vendor forecast, [MarketsandMarkets](https://www.marketsandmarkets.com/PressReleases/ai-inference.asp)). AlphaEvolve's 23% kernel speedup gave about a 1% cut in Gemini training time ([ssojet](https://ssojet.com/news/google-deepminds-alphaevolve-a-breakthrough-ai-coding-agent), [dev.to](https://dev.to/czmilo/alphaevolve-a-comprehensive-report-on-gemini-powered-algorithm-discovery-5g5i)).
- **Incumbents:** Luminal (search, no LLM), Sakana AI CUDA Engineer, Standard Kernel / KernelBench community, tinygrad BEAM (I found no source for it in this pass).

## 2. AlgoTune-style numerical code speedups

- **Benchmark:** [AlgoTune](https://arxiv.org/pdf/2507.15887) (NeurIPS 2025 D&B). The published version has 120 tasks; arXiv v4 has 154. Reference solvers use SciPy, sklearn and CVXPY. The AlgoTuner baseline averages **1.58x** (published) or 1.72x (v4). The authors find models "fail to discover algorithmic innovations, instead preferring surface-level optimizations" ([NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2025/hash/9a648e8e1014c2427156dcb5465cd488-Abstract-Datasets_and_Benchmarks_Track.html)). DeepSeek R1 reached at least 1.1x on 77 NumPy tasks ([arXiv v4](https://arxiv.org/html/2507.15887v4)). That is a direct DeepSeek baseline to beat.
- **Fresh held-out:** Each task has a random instance generator, so new seeds and sizes give fresh tests. You can also hold out whole tasks.
- **Evaluation:** CPU only, seconds per eval. This is the most ready-made option.
- **Plausible gain:** Moving from about 1.5x to 2x+ average on a 10 to 20 task subset by carrying cross-task "insight memory" between rounds.
- **Startup:** [Codeflash](https://codeflash.notion.site/) automates Python performance optimization by opening PRs with verified speedups. Backers are Boldstart and Conviction; a $2.2M seed figure is unverified. Customers include Pydantic and Langflow, and Roboflow reported 25% ([entrepreneur.com](https://india.entrepreneur.com/entrepreneurs/revolutionary-ai-technology-transforms-code-performance-for/497917), [devtoollab](https://devtoollab.com/ai-tools/codeflash-ai)). Weco (AIDE) works on tree search over code against a metric and reportedly raised an $8M seed (unverified, [ai.engineer](https://www.ai.engineer/speakers/zhengyao-jiang), [AIDE paper](https://arxiv.org/pdf/2502.13138)).

## 3. LLM-serving config / scheduling policy search on a simulator

- **Tool:** [Vidur](https://github.com/microsoft/vidur) ([arXiv 2405.05465](https://arxiv.org/html/2405.05465v1)), Microsoft's LLM inference simulator, which reports under 9% latency error. Vidur-Search found the best LLaMA2-70B deployment in **about 1 CPU-hour, versus 42K GPU-hours (~$218K)** for real exploration. The best config depends on the workload, and reusing one on a different trace can cost **up to 2x** ([MSR](https://www.microsoft.com/en-us/research/publication/vidur-a-large-scale-simulation-framework-for-llm-inference/)).
- **Task:** Agents propose (a) configs: TP/PP degree, batch cap, chunked-prefill size, scheduler, replica count, quantization proxy; or (b) *policy code*: a batching or admission scheduler function. Score is cost per 1M tokens subject to P99 TTFT/TBT SLOs. Option (b) is the harder and more interesting one.
- **Fresh held-out:** New synthetic traces (Poisson/gamma arrivals, prefill/decode length mixes), unseen model sizes and new SLO targets. Generalization across traces is exactly the 2x failure mode Vidur documents.
- **Eval speed:** Short traces simulate in seconds on CPU. Check Vidur's per-run time early, and fall back to a hand-written discrete-event simulator if it is too slow.
- **Related:** ADRS ("Barbarians at the Gate", UC Berkeley, OpenEvolve) evolved systems policies. It reports up to 5x (later 13x) faster MoE expert load balancing and 26 to 35% spot-instance cost savings, in hours and for under $20 ([arXiv 2510.06189](https://arxiv.org/html/2510.06189v1), [SIGOPS blog](https://www.sigops.org/2026/let-the-barbarians-in-how-ai-can-accelerate-systems-performance-research/)).
- **Why Joe:** Luminal Cloud sells serverless inference with auto-batching, so this is literally their operations problem. Difficulty may *look* lower than kernels unless you do policy code, not just knob tuning.
- **Market:** Inference cost reduction (same TAM as #1). Incumbents include every inference cloud's internal tuning (Baseten, Together, Fireworks) and Vidur as an open tool.

## 4. Cache eviction policy on real traces

- **Tool and traces:** [libCacheSim](https://github.com/1a1a11a/libCacheSim) with public block/CDN traces (CloudPhysics, Twitter, MSR, Wikipedia CDN; check which ones are downloadable quickly). [PolicySmith](https://arxiv.org/pdf/2510.08803) ("Man-Made Heuristics Are Dead") generates eviction heuristics with LLMs on libCacheSim. [Vulcan](https://arxiv.org/pdf/2512.25065) builds instance-specialized heuristics with LLM search. There is also KV-cache eviction via program evolution ([arXiv 2608.14555](https://arxiv.org/pdf/2608.14555)).
- **Score:** Miss ratio relative to LRU and a strong baseline (S3-FIFO/ARC/LHD). **Held-out:** unseen traces and cache sizes.
- **Plausible gain:** A few percent relative miss-ratio reduction over the best classical policy on held-out traces is realistic. Large gains over LRU are easy and less impressive.
- **Market:** CDNs and storage (Cloudflare, Akamai, Meta's caching). There is also a KV-cache angle that ties to inference.

## 5. Combinatorial heuristics: bin packing, CVRP, ALE-Bench

- **Bin packing:** FunSearch's lineage on OR-Library OR1 to OR4 (excess bins about 5.3%, 4.19%, 3.11% and 2.47%) and Weibull 5k/10k/100k. X-evolve reports about 0.67%, 0.38% and 0.12% on Weibull, against about 4% for first fit ([X-evolve](https://arxiv.org/pdf/2508.07932), [Beyond the Hype](https://arxiv.org/pdf/2501.11411)). Generating held-out instances is trivial with Weibull sampling. Each eval takes under a second. The downside is that it is saturated and familiar.
- **CVRP:** [CVRPLIB](http://vrp.galgos.inf.puc-rio.br/) X instances (Uchoa). Reported LLM-heuristic gaps on a mixed subset: EoH 3.6%, ReEvo 9.5%, newer methods 1.7% ([arXiv 2609.02353](https://arxiv.org/pdf/2609.02353)). Constructive heuristics sit around a 23% gap ([RouteRepair](https://arxiv.org/pdf/2609.11452)). Fresh instances come from Uchoa's generator. Market: logistics routing (Routific, Onfleet, OR-Tools users).
- **ALE-Bench:** [ALE-Bench](https://arxiv.org/html/2506.09050v2) (Sakana × AtCoder) has 40 past AtCoder Heuristic Contest problems, all NP-hard, with scores converted to human-relative Performance. ALE-Agent placed 21st of about 1000 in a live AHC ([the-decoder](https://the-decoder.com/sakana-ais-ale-ai-agent-cracks-the-top-21-among-1000-code-experts/)). Each problem ships with an input generator, so held-out tests are built in. The **difficulty story is very strong**, because scores are relative to human competitive programmers. Evals need compiled C++ for good scores but run in seconds.
- **ShinkaEvolve:** new SOTA 26-circle packing in about 150 evaluations, which is a sample-efficiency argument for a 6-hour build ([Sakana](https://sakana.ai/shinka-evolve/), [arXiv 2509.19349](https://arxiv.org/pdf/2509.19349)).

## 6. DuckDB SQL query rewriting

- **Benchmarks:** TPC-H/TPC-DS via DuckDB's built-in `dbgen`/`dsdgen` extensions, plus JOB/IMDB and DSB. [E3-Rewrite](https://arxiv.org/html/2508.09023v2) reports up to 25.6% lower execution time than baselines. On TPC-H, average latency went 78.8s (original) to 54.8s (LLM-R2) to 29.7s (E3). [LLM-R2](https://arxiv.org/html/2404.12872v1) and [R-Bot](https://arxiv.org/pdf/2412.01661) ran on PostgreSQL. **I found no DuckDB results**, so DuckDB's optimizer may already capture most rewrites, which makes the headroom uncertain.
- **Score:** Latency ratio, gated by result-set equality on several random DB instances (generate with different seeds and scale factors). **Held-out:** new templated queries.
- **Risk:** DuckDB is already strong, so gains may be small. Equivalence-by-testing is unsound, though it is acceptable for a hackathon.

## 7. Prompt / agent-program optimization (GEPA-style)

- [GEPA](https://arxiv.org/pdf/2507.19457) beats GRPO by about 6 to 10% on average (up to 20%) with up to 35x fewer rollouts, and beats MIPROv2 by more than 10% ([alphaxiv](https://www.alphaxiv.org/abs/2507.19457v2)). Tasks include HotpotQA, IFBench, HoVer and PUPA. DSPy provides train/val/test splits.
- **Pros:** Uses the Luminal-hosted LLM as both optimizer and target, so the whole stack runs on Luminal. Held-out splits come standard.
- **Cons:** It is LLM-call bound, not laptop bound. Concurrency limits could choke parallel rounds. The difficulty perception is lower and the space is crowded (DSPy, Comet Opik, Arize). It is the weakest fit for a compiler founder.

## 8. Format-aware compression transform search

- **Tool:** Meta [OpenZL](https://engineering.fb.com/2025/10/06/developer-tools/openzl-open-source-format-aware-compression-framework) (BSD, October 2025; v0.2 in May 2026 per [Phoronix](https://www.phoronix.com/news/OpenZL-0.2-Released)). It applies a configurable graph of transforms before entropy coding, and one universal decompressor reads every file ([arXiv 2510.03203](https://arxiv.org/abs/2510.03203)).
- **Task:** Agents search transform graphs or write Python pre-transforms (delta, transpose, field split, dictionary) for a data format such as CSV logs, tensors/checkpoints or Parquet columns. Score is compression ratio at a minimum speed, losslessness is checked, and held-out tests are new files of the same format. Compressing model weights or KV-cache gives a direct inference tie-in.
- **Risk:** The OpenZL Python bindings and setup time on a laptop are unknown. A pure-Python transform plus zstd is a fine fallback.

---

## Also considered, lower priority
- **SAT/MaxSAT heuristics:** [AutoSAT](https://arxiv.org/abs/2402.10705v2) evolves CDCL heuristics in EasySAT and sometimes beats MiniSat/Kissat. AE-Kissat-MAB reportedly won the 2025 SAT Competition main track ([IJCAI 2026](https://www.ijcai.org/proceedings/2026/0257.pdf)). Evals take too long (seconds to minutes per instance set) and need a C toolchain. The difficulty story is strong but the feedback loop is slow.
- **Regex synthesis:** [StructuredRegex](https://aclanthology.org/2020.acl-main.541) best baseline reached 37.2%. It is accuracy-scored, so improvement is easy to show, but it is not a strong startup story.

## Recommendation
1. **Primary:** #1, CPU kernel/schedule optimization over a random op-graph grammar. Report a speedup distribution on held-out graphs and shapes, with fast_1 and fast_1.5 as metrics, and include anti-reward-hacking checks. If you want a ready-made benchmark with a DeepSeek-R1 baseline, fall back to or mix in #2 (AlgoTune subset).
2. **Alternative with the strongest product tie-in:** #3, serving *policy* evolution on a simulator, held out across traces.
3. **Generic difficulty story:** #5 ALE-Bench, where scores are human-relative.

In every case, show the judges a round-by-round curve: round-0 baseline, then rounds 1 to N, scored on the *held-out* set, never on the training set. Add an ablation with no inter-round memory, which demonstrates that the "self-improving" part is doing the work.
