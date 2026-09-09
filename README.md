<!-- Generated from data/*.yaml by scripts/render.py. Do not edit directly. -->

<div align="center">

# Good LLM Stats Papers

Curated research on LLMs, statistics, causal inference, marketing, and behavioral simulation.

2022–2026 · 计算机、统计、经济与营销：方法和应用

[![Papers](https://img.shields.io/badge/Papers-84-0B7285?style=flat-square)](#paper-index) [![Target%20venues](https://img.shields.io/badge/Target_venues-33-364FC7?style=flat-square)](docs/coverage.md) [![Verified](https://img.shields.io/badge/Verified-2026--09--09-5F3DC4?style=flat-square)](data/coverage.yaml) [![License](https://img.shields.io/badge/License-CC_BY_4.0-2B8A3E?style=flat-square)](LICENSE)

[**Suggest a Paper**](https://github.com/sjsj0101/good_llm_stats_papers/issues/new?template=paper-suggestion.yml)

</div>

## Scope

收集 LLM 与统计推断、因果发现/识别/估计、统计学习理论、不确定性评测和合成数据有效性有实质结合的研究，同时纳入营销研究、消费者/经济行为模拟、数字孪生与多智能体社会模拟的实证应用及验证数据集。主目录要求目标 venue 的正式发表或官方录用证据。

**排除**：以 LLM 使用、引入或普及为处理变量，研究其对生产率、就业、工资、学习或其他现实结果之因果效应的论文；仅将 causal language modeling 当作因果推断、仅讨论 inference acceleration、以及仅使用 LLM 写代码或润色的论文也不纳入。

期刊按首次正式在线发表年份归类，另保留卷期年份；会议采用会议年份。Findings、特别轨、综述、名单外期刊与预印本保留在补充列表。

本仓库是持续整理的证据目录，已补充营销与 simulation 应用。覆盖状态为 partial / search-only，不宣称逐年穷尽；未命中不代表该领域没有相关论文。保存原创中文摘要和来源链接，论文版权属于原作者及出版方。

## At a Glance

| Metric | Value |
| --- | ---: |
| 主目录论文 | 84 |
| 正式发表 / 官方已接收稿 | 82 / 2 |
| 补充 / 待核验 | 27 / 1 |
| 目标 venue / 年份单元 | 33 / 165 |
| 检索截止日 | 2026-09-09 |

## How to Use

- [中文研究地图与 8 篇方法优先阅读](docs/research-map.zh.md)
- [营销与 simulation 应用指南](docs/marketing-simulation.md)
- [覆盖与缺口](docs/coverage.md) · [数据字段与口径](docs/metadata.md) · [来源与核验](docs/sources.md)
- [补充文献](docs/supplementary.md) · [待核验候选](docs/pending.md) · [官方已接收稿](docs/accepted.md)
- [CSV](exports/papers.csv) · [BibTeX](exports/references.bib) · [结构化主目录](data/papers.yaml)

## Browse by Topic

- [LLM 辅助统计推断](topics/stats-inference.md)：20 篇
- [统计学习理论与上下文学习](topics/statistical-theory.md)：23 篇
- [不确定性、校准与统计评测](topics/uncertainty.md)：23 篇
- [因果发现与识别](topics/causal-discovery.md)：12 篇
- [因果估计与推断](topics/causal-estimation.md)：9 篇
- [因果推理能力与评测](topics/causal-reasoning.md)：18 篇
- [LLM 的因果与概率分析](topics/causal-llm-analysis.md)：9 篇
- [合成数据与调查有效性](topics/synthetic-data.md)：13 篇
- [营销研究与消费者洞察](topics/marketing.md)：6 篇
- [LLM 行为、经济与社会模拟](topics/simulation.md)：9 篇

主题允许交叉，数量不可直接相加。

## Coverage: 2022–2026

| Venue | 2026 | 2025 | 2024 | 2023 | 2022 |
| --- | ---: | ---: | ---: | ---: | ---: |
| ICML | 0 | [6](papers/2025/icml.md) | [1](papers/2024/icml.md) | [2](papers/2023/icml.md) | 0 |
| NeurIPS | 0 | [7](papers/2025/neurips.md) | [8](papers/2024/neurips.md) | [7](papers/2023/neurips.md) | [2](papers/2022/neurips.md) |
| ICLR | 0 | [2](papers/2025/iclr.md) | [3](papers/2024/iclr.md) | [1](papers/2023/iclr.md) | [1](papers/2022/iclr.md) |
| AISTATS | [2](papers/2026/aistats.md) | [2](papers/2025/aistats.md) | 0 | 0 | 0 |
| UAI | [1](papers/2026/uai.md) | [2](papers/2025/uai.md) | [1](papers/2024/uai.md) | 0 | 0 |
| COLT | [1](papers/2026/colt.md) | 0 | [1](papers/2024/colt.md) | 0 | 0 |
| CLeaR | [2](papers/2026/clear.md) | [1](papers/2025/clear.md) | 0 | 0 | 0 |
| ACL | [4](papers/2026/acl.md) | [1](papers/2025/acl.md) | [1](papers/2024/acl.md) | 0 | 0 |
| EMNLP | 0 | [1](papers/2025/emnlp.md) | [1](papers/2024/emnlp.md) | 0 | 0 |
| NAACL | 0 | 0 | [2](papers/2024/naacl.md) | 0 | 0 |
| AAAI | [1](papers/2026/aaai.md) | [1](papers/2025/aaai.md) | 0 | 0 | 0 |
| IJCAI | 0 | [1](papers/2025/ijcai.md) | 0 | 0 | 0 |
| KDD | 0 | [1](papers/2025/kdd.md) | 0 | 0 | 0 |
| JMLR | [1](papers/2026/jmlr.md) | 0 | [1](papers/2024/jmlr.md) | 0 | 0 |
| TMLR | 0 | 0 | [2](papers/2024/tmlr.md) | [1](papers/2023/tmlr.md) | 0 |
| TACL | 0 | 0 | 0 | 0 | 0 |
| AER | 0 | 0 | 0 | 0 | 0 |
| Econometrica | 0 | 0 | 0 | 0 | 0 |
| QJE | 0 | 0 | 0 | 0 | 0 |
| JPE | 0 | 0 | 0 | 0 | 0 |
| REStud | 0 | 0 | 0 | 0 | 0 |
| Review of Economics and Statistics | 0 | 0 | 0 | 0 | 0 |
| Journal of Econometrics | 0 | 0 | 0 | 0 | 0 |
| Quantitative Economics | 0 | 0 | 0 | 0 | 0 |
| Econometric Theory | 0 | 0 | 0 | 0 | 0 |
| JASA | [1](papers/2026/jasa.md) | [2](papers/2025/jasa.md) | 0 | 0 | 0 |
| JRSS-B | 0 | [1](papers/2025/jrss-b.md) | 0 | 0 | 0 |
| Annals of Statistics | 0 | [1](papers/2025/annals-of-statistics.md) | 0 | 0 | 0 |
| Biometrika | [1](papers/2026/biometrika.md) | 0 | 0 | 0 | 0 |
| Marketing Science | [1](papers/2026/marketing-science.md) | [1](papers/2025/marketing-science.md) | [2](papers/2024/marketing-science.md) | 0 | 0 |
| Journal of Marketing Research | [1](papers/2026/journal-of-marketing-research.md) | 0 | 0 | 0 | 0 |
| Journal of Marketing | 0 | 0 | [1](papers/2024/journal-of-marketing.md) | 0 | 0 |
| Journal of Consumer Research | 0 | 0 | 0 | 0 | 0 |

表格为已核验收录数；所有来源均未宣称穷尽，详细状态见 [coverage.yaml](data/coverage.yaml)。

## Browse by Year and Venue

- **2026** · [UAI](papers/2026/uai.md) — 1 篇
- **2026** · [Marketing Science](papers/2026/marketing-science.md) — 1 篇
- **2026** · [Journal of Marketing Research](papers/2026/journal-of-marketing-research.md) — 1 篇
- **2026** · [JMLR](papers/2026/jmlr.md) — 1 篇
- **2026** · [JASA](papers/2026/jasa.md) — 1 篇
- **2026** · [COLT](papers/2026/colt.md) — 1 篇
- **2026** · [CLeaR](papers/2026/clear.md) — 2 篇
- **2026** · [Biometrika](papers/2026/biometrika.md) — 1 篇
- **2026** · [AISTATS](papers/2026/aistats.md) — 2 篇
- **2026** · [ACL](papers/2026/acl.md) — 4 篇
- **2026** · [AAAI](papers/2026/aaai.md) — 1 篇
- **2025** · [UAI](papers/2025/uai.md) — 2 篇
- **2025** · [NeurIPS](papers/2025/neurips.md) — 7 篇
- **2025** · [Marketing Science](papers/2025/marketing-science.md) — 1 篇
- **2025** · [KDD](papers/2025/kdd.md) — 1 篇
- **2025** · [JRSS-B](papers/2025/jrss-b.md) — 1 篇
- **2025** · [JASA](papers/2025/jasa.md) — 2 篇
- **2025** · [IJCAI](papers/2025/ijcai.md) — 1 篇
- **2025** · [ICML](papers/2025/icml.md) — 6 篇
- **2025** · [ICLR](papers/2025/iclr.md) — 2 篇
- **2025** · [EMNLP](papers/2025/emnlp.md) — 1 篇
- **2025** · [CLeaR](papers/2025/clear.md) — 1 篇
- **2025** · [Annals of Statistics](papers/2025/annals-of-statistics.md) — 1 篇
- **2025** · [AISTATS](papers/2025/aistats.md) — 2 篇
- **2025** · [ACL](papers/2025/acl.md) — 1 篇
- **2025** · [AAAI](papers/2025/aaai.md) — 1 篇
- **2024** · [UAI](papers/2024/uai.md) — 1 篇
- **2024** · [TMLR](papers/2024/tmlr.md) — 2 篇
- **2024** · [NeurIPS](papers/2024/neurips.md) — 8 篇
- **2024** · [NAACL](papers/2024/naacl.md) — 2 篇
- **2024** · [Marketing Science](papers/2024/marketing-science.md) — 2 篇
- **2024** · [Journal of Marketing](papers/2024/journal-of-marketing.md) — 1 篇
- **2024** · [JMLR](papers/2024/jmlr.md) — 1 篇
- **2024** · [ICML](papers/2024/icml.md) — 1 篇
- **2024** · [ICLR](papers/2024/iclr.md) — 3 篇
- **2024** · [EMNLP](papers/2024/emnlp.md) — 1 篇
- **2024** · [COLT](papers/2024/colt.md) — 1 篇
- **2024** · [ACL](papers/2024/acl.md) — 1 篇
- **2023** · [TMLR](papers/2023/tmlr.md) — 1 篇
- **2023** · [NeurIPS](papers/2023/neurips.md) — 7 篇
- **2023** · [ICML](papers/2023/icml.md) — 2 篇
- **2023** · [ICLR](papers/2023/iclr.md) — 1 篇
- **2022** · [NeurIPS](papers/2022/neurips.md) — 2 篇
- **2022** · [ICLR](papers/2022/iclr.md) — 1 篇

## Contributing

通过 [Suggest a Paper](https://github.com/sjsj0101/good_llm_stats_papers/issues/new?template=paper-suggestion.yml) 提交论文链接与方法相关性说明，由维护者审核。也可修改 `data/*.yaml` 后提交 PR。

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/render.py
python3 scripts/validate.py
python3 scripts/render.py --check
```

详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## Paper Index

### UAI 2026

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2026 · UAI | [Leveraging Large Language Models for Causal Discovery: a Constraint-based, Argumentation-driven Approach](https://proceedings.mlr.press/v337/li26e.html) | 提出 ABAPC-LLM，将 LLM 从变量名和描述提取的语义结构约束作为不完美专家意见，与统计证据通过因果假设论证框架保守整合。 |

### Marketing Science 2026

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2026 · Marketing Science | [Large Language Models for Market Research: A Data-Augmentation Approach](https://pubsonline.informs.org/doi/10.1287/mksc.2025.0009) | 用少量人类数据校正 LLM 合成选择数据，提高联合分析中的偏好估计效率。 |

### Journal of Marketing Research 2026

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2026 · Journal of Marketing Research · 已接收稿 | [EXPRESS: Evaluating Novel Unstructured Treatments with Generative AI: A Causal Prediction Framework](https://journals.sagepub.com/doi/10.1177/00222437261476639) | 用 LLM 表示历史营销内容，并通过拒绝采样约束外推，预测新内容的因果效果。 |

### JMLR 2026

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2026 · JMLR | [UQLM: A Python Package for Uncertainty Quantification in Large Language Models](https://www.jmlr.org/papers/v27/25-1557.html) | 提供统一的LLM不确定性量化软件接口，把多类幻觉检测和回答可靠性评分标准化为0到1的置信分数，并支持黑盒与白盒模型。 |

### JASA 2026

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2026 · JASA | [Towards Better Statistical Understanding of Watermarking LLMs](https://www.tandfonline.com/doi/full/10.1080/01621459.2026.2618290) | 把红绿词表水印的质量—可检测性权衡写成约束优化问题，并给出在线生成算法和渐近最优性分析。 |

### COLT 2026

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2026 · COLT | [Universal Priors: Solving Empirical Bayes via Bayesian Inference and Pretraining](https://proceedings.mlr.press/v336/cannella26a.html) | 把经验贝叶斯问题改写为在合成任务分布上预训练后进行贝叶斯预测，并在Poisson经验贝叶斯中给出接近最优的统一遗憾界与后验收缩结果。 |

### CLeaR 2026

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2026 · CLeaR | [IV Co-Scientist: Multi-Agent LLM Framework for Causal Instrumental Variable Discovery](https://proceedings.mlr.press/v323/sheth26a.html) | 提出多智能体 IV Co-Scientist，为给定处理—结果对提出、批判和改进工具变量，并检验能否复现已知及避开失效 IV。 |
| 2026 · CLeaR | [Retrieving Classes of Causal Orders with Inconsistent Knowledge Bases](https://proceedings.mlr.press/v323/baldo26a.html) | 把易幻觉的 LLM 因果知识转化为成对一致性分数，恢复因果顺序的抽象与最优无环竞赛图集合，并用于效应估计。 |

### Biometrika 2026

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2026 · Biometrika · 已接收稿 | [Optimal Watermark Generation under Type I and Type II Errors](https://doi.org/10.1093/biomet/asag049) | 在同时约束第一类和第二类错误下求解LLM水印生成的最小保真损失，并构造达到下界的分布与采样规则。 |

### AISTATS 2026

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2026 · AISTATS | [An Information-Theoretic Approach to Understanding Transformers’ In-Context Learning of Variable-Order Markov Chains](https://proceedings.mlr.press/v300/zhou26b.html) | 研究Transformer在上下文中学习变阶马尔可夫链的有限样本准确率，并构造可精确实现贝叶斯context-tree weighting的多层Transformer。 |
| 2026 · AISTATS | [Evaluation of Large Language Models via Coupled Token Generation](https://proceedings.mlr.press/v300/benz26a.html) | 建立共享外生随机性的耦合自回归因果模型，使不同 LLM 在相同随机源下比较，并证明基准评测可显著减少样本。 |

### ACL 2026

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2026 · ACL | [Can Large Language Models Infer Causal Relationships from Real-World Text?](https://aclanthology.org/2026.acl-long.1003/) | 构建来自真实学术文献的 ReCITE 基准，按显式性、关系数量、文本长度和领域评估 LLM 从复杂文本推断因果关系。 |
| 2026 · ACL | [METER: Evaluating Multi-Level Contextual Causal Reasoning in Large Language Models](https://aclanthology.org/2026.acl-long.1668/) | 提出 METER，在统一上下文中覆盖因果阶梯三层，并结合错误模式与内部信息流追踪分析 LLM 随层级上升的性能退化。 |
| 2026 · ACL | [NoisyCausal: A Benchmark for Evaluating Causal Reasoning Under Structured Noise](https://aclanthology.org/2026.acl-long.1833/) | 构建从真值因果图生成、含干扰项、数值扰动、混杂与部分可观测性的 NoisyCausal，并提出显式构图后再推理的模块化方法。 |
| 2026 · ACL | [Valid Survey Simulations with Limited Human Data: The Roles of Prompting, Fine-Tuning, and Rectification](https://aclanthology.org/2026.acl-long.498/) | 比较LLM调查回答的提示、微调与PPI式事后校正，显示仅合成带来显著偏差，而把多数有限真人预算用于校正可大幅降低总体均值估计偏差。 |

### AAAI 2026

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2026 · AAAI | [CounterBench: Evaluating and Improving Counterfactual Reasoning in Large Language Models](https://ojs.aaai.org/index.php/AAAI/article/view/40287) | 构建 1200 道基于形式规则的 CounterBench，覆盖多种因果图、难度和无意义名称，并提出迭代推理与回溯方法 CoIn。 |

### UAI 2025

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2025 · UAI | [Multi-group Uncertainty Quantification for Long-form Text Generation](https://proceedings.mlr.press/v286/liu25a.html) | 揭示长文本声明校准和共形保证在总体上成立却可在群组内失效，并用多重校准与多重有效共形预测改善群组内保证。 |
| 2025 · UAI | [The Consistency Hypothesis in Uncertainty Quantification for Large Language Models](https://proceedings.mlr.press/v286/xiao25a.html) | 把“生成一致性可代理置信度”形式化为三个可检验命题，设计统计检验与符合度指标，并据此构造无数据黑箱UQ方法。 |

### NeurIPS 2025

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2025 · NeurIPS | [Conformal Information Pursuit for Interactively Guiding Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2025/hash/823a3d2cf462fb815978314023e48f65-Abstract-Conference.html) | 用共形预测集合平均大小替代失准的LLM条件熵来指导顺序提问，在交互问答中减少查询并保持预测能力。 |
| 2025 · NeurIPS | [Conformal Prediction Beyond the Seen: A Missing Mass Perspective for Uncertainty Quantification in Generative Models](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2e5911cb61db978c225cf62b6c029192-Abstract-Conference.html) | 在仅能查询黑箱生成模型时，以missing mass和Good–Turing估计构造CPQ，联合权衡覆盖、查询预算与预测集合信息量。 |
| 2025 · NeurIPS | [Exploiting LLMs for Automatic Hypothesis Assessment via a Logit-Based Calibrated Prior](https://proceedings.neurips.cc/paper_files/paper/2025/hash/338b4df24eeed6767d6f72b983b845ce-Abstract-Conference.html) | 从LLM输出logit诱导变量对相关系数的连续校准先验，用先验预期程度衡量观察相关关系的新颖性，并报告可信区间覆盖。 |
| 2025 · NeurIPS | [Revealing Multimodal Causality with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2025/hash/92e9846e694ccee9c80260d47053d8b5-Abstract-Conference.html) | 提出 MLLM-CD，从多模态非结构化数据发现因果因子与关系，结合对比因子发现、统计结构学习和多模态反事实迭代。 |
| 2025 · NeurIPS | [Self-Verification Provably Prevents Model Collapse in Recursive Synthetic Training](https://proceedings.neurips.cc/paper_files/paper/2025/hash/3380e8116452e0efbf36f35d95e88c94-Abstract-Conference.html) | 证明递归合成训练在缺少足量真实数据时产生指数误差增长，并给出仅靠模型内部置信度自验证即可避免崩溃的有限样本误差界。 |
| 2025 · NeurIPS | [Signal and Noise: A Framework for Reducing Uncertainty in Language Model Evaluation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/18b3b2947174ae9b1a8fc91ff89f4eb6-Abstract-Conference.html) | 定义基准区分模型的信号与对训练步随机性的噪声，分析信噪比对小规模决策和缩放律预测误差的影响，并测试降低噪声的干预。 |
| 2025 · NeurIPS | [TwinMarket: A Scalable Behavioral and Social Simulation for Financial Markets](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5bf234ecf83cd77bc5b77a24ba9338b0-Abstract-Conference.html) | 在股票市场与社交环境中模拟异质投资者，研究个体互动形成的市场集体现象。 |

### Marketing Science 2025

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2025 · Marketing Science · 数据报告 | [Database Report: Twin-2K-500: A Data Set for Building Digital Twins of over 2,000 People Based on Their Answers to over 500 Questions](https://pubsonline.informs.org/doi/10.1287/mksc.2025.0262) | 提供 2,058 人、四轮、500 多道问题的数据及重测基准，用于构建和验证个人数字孪生。 |

### KDD 2025

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2025 · KDD | [Causal Discovery through Synergizing Large Language Model and Data-Driven Reasoning](https://doi.org/10.1145/3711896.3736874) | LLM-CD 将变量语义先验与数据驱动的因果发现迭代结合。 |

### JRSS-B 2025

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2025 · JRSS-B | [Robust detection of watermarks for large language models under human edits](https://doi.org/10.1093/jrsssb/qkaf056) | 研究人工编辑后LLM水印的稳健检测，提出截断拟合优度检验并刻画不同编辑强度下的检测边界。 |

### JASA 2025

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2025 · JASA | [Debiasing Watermarks for Large Language Models via Maximal Coupling](https://www.tandfonline.com/doi/abs/10.1080/01621459.2025.2520455) | 用最大耦合构造无偏LLM水印，在保持原生成分布的同时维持可检测性，并分析其统计性质。 |
| 2025 · JASA | [On the Algorithmic Bias of Aligning Large Language Models with RLHF: Preference Collapse and Matching Regularization](https://www.tandfonline.com/doi/abs/10.1080/01621459.2025.2555067) | 研究RLHF中标准KL正则化导致奖励最大化与目标偏好分布错配的算法偏差，并提出概率匹配正则化。 |

### IJCAI 2025

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2025 · IJCAI | [Causal-aware Large Language Models: Enhancing Decision-Making Through Learning, Adapting and Acting](https://www.ijcai.org/proceedings/2025/478) | 用 LLM 初始化环境因果图，再利用环境反馈更新结构并指导决策。 |

### ICML 2025

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2025 · ICML | [Can Transformers Learn Full Bayesian Inference in Context?](https://proceedings.mlr.press/v267/reuter25a.html) | 构建可在上下文中输出完整后验样本的Transformer框架，覆盖广义线性模型与潜因子模型，并与MCMC和变分推断比较。 |
| 2025 · ICML | [Collapse or Thrive: Perils and Promises of Synthetic Data in a Self-Generating World](https://proceedings.mlr.press/v267/kazdan25a.html) | 比较纯替换、累积混合及固定子样本三种递归合成训练流程，在高斯估计、核密度估计和语言模型微调中区分爆炸崩溃、稳定与缓慢退化。 |
| 2025 · ICML | [How to Synthesize Text Data without Model Collapse?](https://proceedings.mlr.press/v267/zhu25d.html) | 发现合成文本比例与LM性能负相关，并以分布偏移和n-gram过度集中解释；提出对人类文本做token编辑的半合成方案并给出有限测试误差上界。 |
| 2025 · ICML | [Internal Causal Mechanisms Robustly Predict Language Model Out-of-Distribution Behaviors](https://proceedings.mlr.press/v267/huang25af.html) | 用内部因果变量进行反事实模拟和值探测，在符号操作、知识检索和指令跟随任务上预测 LLM 分布外正确性。 |
| 2025 · ICML | [Preference Learning for AI Alignment: a Causal Perspective](https://proceedings.mlr.press/v267/kobalczyk25a.html) | 将 LLM 奖励模型的偏好学习放入因果框架，识别因果错识别、偏好异质性和用户特定混杂，并提出面向干预的数据收集要求。 |
| 2025 · ICML | [Teaching Transformers Causal Reasoning through Axiomatic Training](https://proceedings.mlr.press/v267/vashishtha25a.html) | 提出因果公理训练，将传递性和 d-separation 等规则转化为示范，使小型 transformer 能从线性链泛化到更长、反序和分支图。 |

### ICLR 2025

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2025 · ICLR | [Causal Order: The Key to Leveraging Imperfect Experts in Causal Inference](https://openreview.net/forum?id=9juyeCqL0u) | 指出成对提示无法区分直接与间接效应，提出以因果顺序作为 LLM 专家接口，并用三变量提示和投票减少环与下游效应误差。 |
| 2025 · ICLR | [Conformal Language Model Reasoning with Coherent Factuality](https://iclr.cc/virtual/2025/poster/30640) | 定义考虑推理步骤依赖的“连贯事实性”，在可推导图的子图上使用分割共形预测，过滤并排序LLM推理声明。 |

### EMNLP 2025

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2025 · EMNLP | [Benchmarking Debiasing Methods for LLM-based Parameter Estimates](https://aclanthology.org/2025.emnlp-main.1000/) | 在有限专家标注下比较PPI与设计型监督学习对LLM文本标注所致参数偏差的修正，刻画随标注量变化的偏差—方差权衡。 |

### CLeaR 2025

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2025 · CLeaR | [Counterfactual Token Generation in Large Language Models](https://proceedings.mlr.press/v275/chatzi25a.html) | 基于 Gumbel-Max 结构因果模型建立 token 生成的反事实耦合，使现有 LLM 无需微调即可生成“若早先 token 不同”的反事实文本。 |

### Annals of Statistics 2025

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2025 · Annals of Statistics | [A statistical framework of watermarks for large language models: Pivot, detection efficiency and optimal rules](https://projecteuclid.org/journals/annals-of-statistics/volume-53/issue-1/A-statistical-framework-of-watermarks-for-large-language-models/10.1214/24-AOS2468.short) | 建立LLM水印统一统计框架，以枢轴量和大偏差效率比较检测规则并推导最优检验。 |

### AISTATS 2025

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2025 · AISTATS | [On Subjective Uncertainty Quantification and Calibration in Natural Language Generation](https://proceedings.mlr.press/v258/wang25i.html) | 从贝叶斯决策论定义自由文本生成的任务相关主观不确定性与校准，并以缺失数据和超额风险刻画认知不确定性。 |
| 2025 · AISTATS | [What and How does In-Context Learning Learn? Bayesian Model Averaging, Parameterization, and Generalization](https://proceedings.mlr.press/v258/zhang25d.html) | 证明理想预训练LLM在动态提示模型下执行贝叶斯模型平均，并用PAC-Bayes界分解预训练误差，得到上下文平均误差率。 |

### ACL 2025

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2025 · ACL | [On the Reliability of Large Language Models for Causal Discovery](https://aclanthology.org/2025.acl-long.471/) | 利用可访问预训练语料的 OLMo 和 BLOOM 分析 LLM 因果发现的可靠性，区分记忆、错误预训练关系和上下文变化的影响。 |

### AAAI 2025

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2025 · AAAI | [Causal Prompting: Debiasing Large Language Model Prompting Based on Front-Door Adjustment](https://ojs.aaai.org/index.php/AAAI/article/view/34777) | 将思维链设为中介，利用前门调整构造去偏提示方法。 |

### UAI 2024

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2024 · UAI | [Optimizing Language Models for Human Preferences is a Causal Inference Problem](https://proceedings.mlr.press/v244/lin24a.html) | 把基于直接结果数据的语言模型偏好优化形式化为因果问题，提出 CPO 与双重稳健 DR-CPO 以降低偏差和方差。 |

### TMLR 2024

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2024 · TMLR | [Causal Reasoning and Large Language Models: Opening a New Frontier for Causality](https://openreview.net/forum?id=mqoxLkX210) | 系统评测 LLM 生成因果论证的能力，涵盖成对因果发现、反事实推理和事件必要性/充分性，并讨论与形式因果工具结合。 |
| 2024 · TMLR | [Generating with Confidence: Uncertainty Quantification for Black-box Large Language Models](https://openreview.net/forum?id=DWkJCSxKU5) | 面向只能采样、不能读取logit的黑盒LLM，区分候选回答间的语义离散度与单个回答的可靠置信度，并用该不确定性支持选择性生成和幻觉检测。 |

### NeurIPS 2024

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2024 · NeurIPS | [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/hash/1bdcb065d40203a00bd39831153338bb-Abstract-Datasets_and_Benchmarks_Track.html) | 建立把共形预测不确定性纳入LLM基准评估的框架，比较九个模型系列在五类NLP任务中的准确率与确定性。 |
| 2024 · NeurIPS | [COLD: Causal reasOning in cLosed Daily activities](https://proceedings.neurips.cc/paper_files/paper/2024/hash/09265e2568cf7a6ff47b506acbc2c6eb-Abstract-Conference.html) | 构建基于日常封闭活动的约 900 万个因果查询，在现实语义和形式验证之间搭桥，并以背门准则衡量事件因果强度。 |
| 2024 · NeurIPS | [Discovery of the Hidden World with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/hash/b99a07486702417d3b1bd64ec2cf74ad-Abstract-Conference.html) | 提出 COAT，让 LLM 从非结构化观测提出并标注高层变量，再由因果发现算法构图并反馈迭代改进变量。 |
| 2024 · NeurIPS | [Does Reasoning Emerge? Examining the Probabilities of Causation in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/hash/d5a1f97d2b922da92e880d13b7d2bf02-Abstract-Conference.html) | 以因果必要性概率和充分性概率为核心，建立评估 LLM 是否能近似现实推理机制的理论与实践框架。 |
| 2024 · NeurIPS | [Large language model validity via enhanced conformal prediction methods](https://proceedings.neurips.cc/paper_files/paper/2024/hash/d02ff1aeaa5c268dc34790dd1ad21526-Abstract-Conference.html) | 针对LLM回答过滤的条件有效性与效用损失，扩展条件共形方法以自适应放宽保证，并通过可微条件共形过程改进评分器。 |
| 2024 · NeurIPS | [Prediction-Powered Ranking of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/hash/cd47cd67caa87f5b1944e00f6781598f-Abstract-Conference.html) | 用少量人类两两偏好和大量强LLM偏好构造每个候选模型的排名集合，并给出对人类偏好真排名的渐近覆盖保证。 |
| 2024 · NeurIPS | [Stratified Prediction-Powered Inference for Effective Hybrid Evaluation of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c9fcd02e6445c7dfbad6986abee53d0d-Abstract-Conference.html) | 提出分层预测增强推断StratPPI，以少量人工标签和大量自动标签构造任意维参数的有效置信区间，并通过分层与样本分配提高LLM评估效率。 |
| 2024 · NeurIPS | [Unveiling Causal Reasoning in Large Language Models: Reality or Mirage?](https://proceedings.neurips.cc/paper_files/paper/2024/hash/af2bb2b2280d36f8842e440b4e275152-Abstract-Conference.html) | 以新鲜语料 CausalProbe-2024 区分参数记忆与真正因果推理，并提出结合一般知识和目标提示的 G²-Reasoner。 |

### NAACL 2024

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2024 · NAACL | [ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems](https://aclanthology.org/2024.naacl-long.20/) | 以合成训练数据训练轻量语言模型评审器，并用少量人工标注通过PPI校正，估计RAG系统的上下文相关性、忠实性和答案相关性。 |
| 2024 · NAACL | [DoubleLingo: Causal Estimation with Large Language Models](https://aclanthology.org/2024.naacl-short.71/) | 将 LLM 作为文本混杂变量的灵活 nuisance 模型嵌入双重机器学习，获得理论一致的因果效应估计。 |

### Marketing Science 2024

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2024 · Marketing Science | [Frontiers: Can Large Language Models Capture Human Preferences?](https://pubsonline.informs.org/doi/10.1287/mksc.2023.0306) | 比较 LLM 与人类跨期偏好，并用 chain-of-thought conjoint 分析偏好差异。 |
| 2024 · Marketing Science | [Frontiers: Determining the Validity of Large Language Models for Automated Perceptual Analysis](https://pubsonline.informs.org/doi/10.1287/mksc.2023.0454) | 研究 LLM 生成品牌感知数据与人类调查数据的一致性及适用范围。 |

### Journal of Marketing 2024

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2024 · Journal of Marketing | [AI–Human Hybrids for Marketing Research: Leveraging Large Language Models (LLMs) as Collaborators](https://journals.sagepub.com/doi/10.1177/00222429241276529) | 通过合成受访者、访谈和调查复现，评估人类与 LLM 协作开展营销研究的有效性。 |

### JMLR 2024

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2024 · JMLR | [Trained Transformers Learn Linear Models In-Context](https://jmlr.org/papers/v25/23-1042.html) | 分析单层线性自注意力在随机线性回归任务上的梯度流，证明合适初始化下收敛到全局最优，并刻画新提示分布中的预测误差与协变量偏移脆弱性。 |

### ICML 2024

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2024 · ICML | [Language Models with Conformal Factuality Guarantees](https://proceedings.mlr.press/v235/mohri24a.html) | 把语言模型输出正确性转化为不确定性集合问题，提出逐步降低回答具体度的共形事实性框架，以少量人工标注获得高概率正确性保证。 |

### ICLR 2024

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2024 · ICLR | [Can Large Language Models Infer Causation from Correlation?](https://openreview.net/forum?id=vqIH0ObdqL) | 构建超过 20 万样本的 Corr2Cause 基准，把相关性陈述映射为因果关系问题，显示多种 LLM 在分布外扰动下接近随机表现。 |
| 2024 · ICLR | [Causal Modelling Agents: Causal Graph Discovery through Synergising Metadata- and Data-driven Reasoning](https://openreview.net/forum?id=pAoqRlTBtY) | 提出 Causal Modelling Agent，将 LLM 从变量元数据提取的知识与深层结构因果模型的数据证据协同用于因果图发现。 |
| 2024 · ICLR | [Conformal Language Modeling](https://iclr.cc/virtual/2024/poster/17755) | 为语言模型采样校准停止规则和拒绝规则，构造至少含一个可接受回答的候选集合，并对回答片段给出分布无关保证。 |

### EMNLP 2024

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2024 · EMNLP | [Can Large Language Models Learn Independent Causal Mechanisms?](https://aclanthology.org/2024.emnlp-main.381/) | 以独立因果机制原则设计多个稀疏交互语言建模模块，研究这种因果约束能否改善分布外抽象与因果推理。 |

### COLT 2024

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2024 · COLT | [Training Dynamics of Multi-Head Softmax Attention for In-Context Learning: Emergence, Convergence, and Optimality (extended abstract)](https://proceedings.mlr.press/v247/siyu24a.html) | 研究多头softmax注意力学习多任务线性回归时的梯度流，证明适当初始化下全局收敛、注意力头发生任务分配，并给出相对最优多头模型的常数因子性能界。 |

### ACL 2024

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2024 · ACL | [EconAgent: Large Language Model-Empowered Agents for Simulating Macroeconomic Activities](https://aclanthology.org/2024.acl-long.829/) | 用带感知与记忆的异质 LLM agents 模拟劳动、消费决策及宏观经济动态。 |

### TMLR 2023

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2023 · TMLR | [Causal Parrots: Large Language Models May Talk Causality But Are Not Causal](https://openreview.net/forum?id=tv46tCzs83) | 提出 meta-SCM 视角，区分语言中因果事实的相关性复述与可干预的真正因果模型，并用实验检验大模型是否只是“因果鹦鹉”。 |

### NeurIPS 2023

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2023 · NeurIPS | [CLadder: Assessing Causal Reasoning in Language Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/631bb9434d718ea309af82566347d607-Abstract-Conference.html) | 构建 CLadder 自然语言因果推理基准，覆盖关联、干预和反事实查询，并提出 CausalCoT 提示策略。 |
| 2023 · NeurIPS | [Does Localization Inform Editing? Surprising Differences in Causality-Based Localization vs. Knowledge Editing in Language Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/3927bbdcf0e8d1fa8aa23c26f358a281-Abstract-Conference.html) | 检验基于表示去噪的 Causal Tracing 是否能指示知识编辑位置，发现其定位结论通常不能预测最佳编辑层。 |
| 2023 · NeurIPS | [Interpretability at Scale: Identifying Causal Mechanisms in Alpaca](https://proceedings.neurips.cc/paper_files/paper/2023/hash/f6a8b109d4d4fd64c75e94aaf85d9697-Abstract-Conference.html) | 提出 Boundless DAS，以因果抽象和可学习对齐搜索定位 Alpaca 在数值推理任务中的可解释内部因果变量。 |
| 2023 · NeurIPS | [MoCa: Measuring Human-Language Model Alignment on Causal and Moral Judgment Tasks](https://proceedings.neurips.cc/paper_files/paper/2023/hash/f751c6f8bfb52c60f43942896fe65904-Abstract-Conference.html) | 汇集认知科学中的因果与道德判断情境，用统计分析比较 LLM 与人类对规范、可避免性等因素的权重。 |
| 2023 · NeurIPS | [Passive learning of active causal strategies in agents and language models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/045c87def0c02e3ad0d3d849766d7f1e-Abstract-Conference.html) | 研究仅从被动数据学习的智能体能否在测试时形成主动干预策略，并显示语言解释可帮助语言模型泛化到新因果结构。 |
| 2023 · NeurIPS | [Pretraining task diversity and the emergence of non-Bayesian in-context learning for regression](https://proceedings.neurips.cc/paper_files/paper/2023/hash/2e10b2c2e1aa4f8083c37dfe269873f8-Abstract-Conference.html) | 发现预训练任务多样性存在上下文学习涌现阈值：阈值下模型接近基于预训练任务先验的贝叶斯估计，阈值上则转向近似岭回归并能处理新任务。 |
| 2023 · NeurIPS | [Transformers as Statisticians: Provable In-Context Learning with In-Context Algorithm Selection](https://proceedings.neurips.cc/paper_files/paper/2023/hash/b2e63e36c57e153b9015fece2352a9f9-Abstract-Conference.html) | 构造并分析可在上下文中实现最小二乘、岭回归、Lasso与广义线性模型学习的Transformer，并证明预测能力、规模与预训练样本复杂度。 |

### ICML 2023

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2023 · ICML | [Transformers as Algorithms: Generalization and Stability in In-context Learning](https://proceedings.mlr.press/v202/li23l.html) | 把上下文学习形式化为算法学习问题，以算法稳定性连接Transformer的超额风险，并给出多任务与新任务泛化界。 |
| 2023 · ICML | [Using Large Language Models to Simulate Multiple Humans and Replicate Human Subject Studies](https://proceedings.mlr.press/v202/aher23a.html) | 用 Turing Experiments 模拟参与者群体，复现经济学、语言和社会心理实验并识别系统偏差。 |

### ICLR 2023

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2023 · ICLR | [Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation](https://iclr.cc/virtual/2023/oral/12609) | 提出语义熵，把意义等价的不同表述聚类后度量LLM生成不确定性，在问答上比词面或概率基线更能预测正确性。 |

### NeurIPS 2022

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2022 · NeurIPS | [Locating and Editing Factual Associations in GPT](https://proceedings.neurips.cc/paper_files/paper/2022/hash/6f1d43d5a82a37e89b0665b33bf3a182-Abstract-Conference.html) | 通过因果干预定位 GPT 中决定事实预测的神经激活，并提出 ROME 直接编辑中层前馈权重中的事实关联。 |
| 2022 · NeurIPS | [What Can Transformers Learn In-Context? A Case Study of Simple Function Classes](https://proceedings.neurips.cc/paper_files/paper/2022/hash/c529dba08a146ea8d6cf715ae8930cbe-Abstract-Conference.html) | 用线性、稀疏线性及非线性函数类检验Transformer的上下文学习能力，显示其在受控问题上可接近最小二乘、Lasso等经典估计器。 |

### ICLR 2022

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2022 · ICLR | [An Explanation of In-context Learning as Implicit Bayesian Inference](https://iclr.cc/virtual/2022/poster/6893) | 在预训练文本由混合隐马尔可夫模型生成的理论设定中，把上下文学习解释为对共享潜在概念的隐式贝叶斯推断，并刻画预训练与提示分布失配时仍能成立的条件。 |

## Acknowledgements and License

目录组织参考 [Good Quant AI Papers](https://github.com/sjsj0101/good-quant-ai-papers)。本仓库的原创文献整理与说明采用 [CC BY 4.0](LICENSE)；链接的论文、代码和数据适用各自许可。
