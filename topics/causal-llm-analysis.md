<!-- Generated from data/*.yaml by scripts/render.py. Do not edit directly. -->

# LLM 的因果与概率分析

[返回目录](../README.md) · 9 篇主目录论文

| 年份 / Venue | 论文 | 方法与 LLM 的关系 |
| --- | --- | --- |
| 2026 · ACL | [METER: Evaluating Multi-Level Contextual Causal Reasoning in Large Language Models](https://aclanthology.org/2026.acl-long.1668/) | 提出 METER，在统一上下文中覆盖因果阶梯三层，并结合错误模式与内部信息流追踪分析 LLM 随层级上升的性能退化。 |
| 2026 · AISTATS | [Evaluation of Large Language Models via Coupled Token Generation](https://proceedings.mlr.press/v300/benz26a.html) | 建立共享外生随机性的耦合自回归因果模型，使不同 LLM 在相同随机源下比较，并证明基准评测可显著减少样本。 |
| 2025 · AAAI | [Causal Prompting: Debiasing Large Language Model Prompting Based on Front-Door Adjustment](https://ojs.aaai.org/index.php/AAAI/article/view/34777) | 将思维链设为中介，利用前门调整构造去偏提示方法。 |
| 2025 · ICML | [Internal Causal Mechanisms Robustly Predict Language Model Out-of-Distribution Behaviors](https://proceedings.mlr.press/v267/huang25af.html) | 用内部因果变量进行反事实模拟和值探测，在符号操作、知识检索和指令跟随任务上预测 LLM 分布外正确性。 |
| 2024 · EMNLP | [Can Large Language Models Learn Independent Causal Mechanisms?](https://aclanthology.org/2024.emnlp-main.381/) | 以独立因果机制原则设计多个稀疏交互语言建模模块，研究这种因果约束能否改善分布外抽象与因果推理。 |
| 2023 · NeurIPS | [Does Localization Inform Editing? Surprising Differences in Causality-Based Localization vs. Knowledge Editing in Language Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/3927bbdcf0e8d1fa8aa23c26f358a281-Abstract-Conference.html) | 检验基于表示去噪的 Causal Tracing 是否能指示知识编辑位置，发现其定位结论通常不能预测最佳编辑层。 |
| 2023 · NeurIPS | [Interpretability at Scale: Identifying Causal Mechanisms in Alpaca](https://proceedings.neurips.cc/paper_files/paper/2023/hash/f6a8b109d4d4fd64c75e94aaf85d9697-Abstract-Conference.html) | 提出 Boundless DAS，以因果抽象和可学习对齐搜索定位 Alpaca 在数值推理任务中的可解释内部因果变量。 |
| 2023 · TMLR | [Causal Parrots: Large Language Models May Talk Causality But Are Not Causal](https://openreview.net/forum?id=tv46tCzs83) | 提出 meta-SCM 视角，区分语言中因果事实的相关性复述与可干预的真正因果模型，并用实验检验大模型是否只是“因果鹦鹉”。 |
| 2022 · NeurIPS | [Locating and Editing Factual Associations in GPT](https://proceedings.neurips.cc/paper_files/paper/2022/hash/6f1d43d5a82a37e89b0665b33bf3a182-Abstract-Conference.html) | 通过因果干预定位 GPT 中决定事实预测的神经激活，并提出 ROME 直接编辑中层前馈权重中的事实关联。 |
