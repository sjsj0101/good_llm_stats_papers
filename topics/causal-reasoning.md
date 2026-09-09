<!-- Generated from data/*.yaml by scripts/render.py. Do not edit directly. -->

# 因果推理能力与评测

[返回目录](../README.md) · 18 篇主目录论文

| 年份 / Venue | 论文 | 方法与 LLM 的关系 |
| --- | --- | --- |
| 2026 · AAAI | [CounterBench: Evaluating and Improving Counterfactual Reasoning in Large Language Models](https://ojs.aaai.org/index.php/AAAI/article/view/40287) | 构建 1200 道基于形式规则的 CounterBench，覆盖多种因果图、难度和无意义名称，并提出迭代推理与回溯方法 CoIn。 |
| 2026 · ACL | [Can Large Language Models Infer Causal Relationships from Real-World Text?](https://aclanthology.org/2026.acl-long.1003/) | 构建来自真实学术文献的 ReCITE 基准，按显式性、关系数量、文本长度和领域评估 LLM 从复杂文本推断因果关系。 |
| 2026 · ACL | [METER: Evaluating Multi-Level Contextual Causal Reasoning in Large Language Models](https://aclanthology.org/2026.acl-long.1668/) | 提出 METER，在统一上下文中覆盖因果阶梯三层，并结合错误模式与内部信息流追踪分析 LLM 随层级上升的性能退化。 |
| 2026 · ACL | [NoisyCausal: A Benchmark for Evaluating Causal Reasoning Under Structured Noise](https://aclanthology.org/2026.acl-long.1833/) | 构建从真值因果图生成、含干扰项、数值扰动、混杂与部分可观测性的 NoisyCausal，并提出显式构图后再推理的模块化方法。 |
| 2025 · ACL | [On the Reliability of Large Language Models for Causal Discovery](https://aclanthology.org/2025.acl-long.471/) | 利用可访问预训练语料的 OLMo 和 BLOOM 分析 LLM 因果发现的可靠性，区分记忆、错误预训练关系和上下文变化的影响。 |
| 2025 · CLeaR | [Counterfactual Token Generation in Large Language Models](https://proceedings.mlr.press/v275/chatzi25a.html) | 基于 Gumbel-Max 结构因果模型建立 token 生成的反事实耦合，使现有 LLM 无需微调即可生成“若早先 token 不同”的反事实文本。 |
| 2025 · ICML | [Teaching Transformers Causal Reasoning through Axiomatic Training](https://proceedings.mlr.press/v267/vashishtha25a.html) | 提出因果公理训练，将传递性和 d-separation 等规则转化为示范，使小型 transformer 能从线性链泛化到更长、反序和分支图。 |
| 2025 · IJCAI | [Causal-aware Large Language Models: Enhancing Decision-Making Through Learning, Adapting and Acting](https://www.ijcai.org/proceedings/2025/478) | 用 LLM 初始化环境因果图，再利用环境反馈更新结构并指导决策。 |
| 2025 · NeurIPS | [Revealing Multimodal Causality with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2025/hash/92e9846e694ccee9c80260d47053d8b5-Abstract-Conference.html) | 提出 MLLM-CD，从多模态非结构化数据发现因果因子与关系，结合对比因子发现、统计结构学习和多模态反事实迭代。 |
| 2024 · ICLR | [Can Large Language Models Infer Causation from Correlation?](https://openreview.net/forum?id=vqIH0ObdqL) | 构建超过 20 万样本的 Corr2Cause 基准，把相关性陈述映射为因果关系问题，显示多种 LLM 在分布外扰动下接近随机表现。 |
| 2024 · NeurIPS | [COLD: Causal reasOning in cLosed Daily activities](https://proceedings.neurips.cc/paper_files/paper/2024/hash/09265e2568cf7a6ff47b506acbc2c6eb-Abstract-Conference.html) | 构建基于日常封闭活动的约 900 万个因果查询，在现实语义和形式验证之间搭桥，并以背门准则衡量事件因果强度。 |
| 2024 · NeurIPS | [Does Reasoning Emerge? Examining the Probabilities of Causation in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/hash/d5a1f97d2b922da92e880d13b7d2bf02-Abstract-Conference.html) | 以因果必要性概率和充分性概率为核心，建立评估 LLM 是否能近似现实推理机制的理论与实践框架。 |
| 2024 · NeurIPS | [Unveiling Causal Reasoning in Large Language Models: Reality or Mirage?](https://proceedings.neurips.cc/paper_files/paper/2024/hash/af2bb2b2280d36f8842e440b4e275152-Abstract-Conference.html) | 以新鲜语料 CausalProbe-2024 区分参数记忆与真正因果推理，并提出结合一般知识和目标提示的 G²-Reasoner。 |
| 2024 · TMLR | [Causal Reasoning and Large Language Models: Opening a New Frontier for Causality](https://openreview.net/forum?id=mqoxLkX210) | 系统评测 LLM 生成因果论证的能力，涵盖成对因果发现、反事实推理和事件必要性/充分性，并讨论与形式因果工具结合。 |
| 2023 · NeurIPS | [CLadder: Assessing Causal Reasoning in Language Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/631bb9434d718ea309af82566347d607-Abstract-Conference.html) | 构建 CLadder 自然语言因果推理基准，覆盖关联、干预和反事实查询，并提出 CausalCoT 提示策略。 |
| 2023 · NeurIPS | [MoCa: Measuring Human-Language Model Alignment on Causal and Moral Judgment Tasks](https://proceedings.neurips.cc/paper_files/paper/2023/hash/f751c6f8bfb52c60f43942896fe65904-Abstract-Conference.html) | 汇集认知科学中的因果与道德判断情境，用统计分析比较 LLM 与人类对规范、可避免性等因素的权重。 |
| 2023 · NeurIPS | [Passive learning of active causal strategies in agents and language models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/045c87def0c02e3ad0d3d849766d7f1e-Abstract-Conference.html) | 研究仅从被动数据学习的智能体能否在测试时形成主动干预策略，并显示语言解释可帮助语言模型泛化到新因果结构。 |
| 2023 · TMLR | [Causal Parrots: Large Language Models May Talk Causality But Are Not Causal](https://openreview.net/forum?id=tv46tCzs83) | 提出 meta-SCM 视角，区分语言中因果事实的相关性复述与可干预的真正因果模型，并用实验检验大模型是否只是“因果鹦鹉”。 |
