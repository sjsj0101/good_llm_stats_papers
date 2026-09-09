<!-- Generated from data/*.yaml by scripts/render.py. Do not edit directly. -->

# LLM 辅助统计推断

[返回目录](../README.md) · 19 篇主目录论文

| 年份 / Venue | 论文 | 方法与 LLM 的关系 |
| --- | --- | --- |
| 2026 · ACL | [Valid Survey Simulations with Limited Human Data: The Roles of Prompting, Fine-Tuning, and Rectification](https://aclanthology.org/2026.acl-long.498/) | 比较LLM调查回答的提示、微调与PPI式事后校正，显示仅合成带来显著偏差，而把多数有限真人预算用于校正可大幅降低总体均值估计偏差。 |
| 2026 · AISTATS | [Evaluation of Large Language Models via Coupled Token Generation](https://proceedings.mlr.press/v300/benz26a.html) | 建立共享外生随机性的耦合自回归因果模型，使不同 LLM 在相同随机源下比较，并证明基准评测可显著减少样本。 |
| 2026 · Biometrika · 已接收稿 | [Optimal Watermark Generation under Type I and Type II Errors](https://doi.org/10.1093/biomet/asag049) | 在同时约束第一类和第二类错误下求解LLM水印生成的最小保真损失，并构造达到下界的分布与采样规则。 |
| 2026 · JASA | [Towards Better Statistical Understanding of Watermarking LLMs](https://www.tandfonline.com/doi/full/10.1080/01621459.2026.2618290) | 把红绿词表水印的质量—可检测性权衡写成约束优化问题，并给出在线生成算法和渐近最优性分析。 |
| 2025 · Annals of Statistics | [A statistical framework of watermarks for large language models: Pivot, detection efficiency and optimal rules](https://projecteuclid.org/journals/annals-of-statistics/volume-53/issue-1/A-statistical-framework-of-watermarks-for-large-language-models/10.1214/24-AOS2468.short) | 建立LLM水印统一统计框架，以枢轴量和大偏差效率比较检测规则并推导最优检验。 |
| 2025 · EMNLP | [Benchmarking Debiasing Methods for LLM-based Parameter Estimates](https://aclanthology.org/2025.emnlp-main.1000/) | 在有限专家标注下比较PPI与设计型监督学习对LLM文本标注所致参数偏差的修正，刻画随标注量变化的偏差—方差权衡。 |
| 2025 · ICLR | [Conformal Language Model Reasoning with Coherent Factuality](https://iclr.cc/virtual/2025/poster/30640) | 定义考虑推理步骤依赖的“连贯事实性”，在可推导图的子图上使用分割共形预测，过滤并排序LLM推理声明。 |
| 2025 · JASA | [Debiasing Watermarks for Large Language Models via Maximal Coupling](https://www.tandfonline.com/doi/abs/10.1080/01621459.2025.2520455) | 用最大耦合构造无偏LLM水印，在保持原生成分布的同时维持可检测性，并分析其统计性质。 |
| 2025 · JRSS-B | [Robust detection of watermarks for large language models under human edits](https://doi.org/10.1093/jrsssb/qkaf056) | 研究人工编辑后LLM水印的稳健检测，提出截断拟合优度检验并刻画不同编辑强度下的检测边界。 |
| 2025 · NeurIPS | [Conformal Prediction Beyond the Seen: A Missing Mass Perspective for Uncertainty Quantification in Generative Models](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2e5911cb61db978c225cf62b6c029192-Abstract-Conference.html) | 在仅能查询黑箱生成模型时，以missing mass和Good–Turing估计构造CPQ，联合权衡覆盖、查询预算与预测集合信息量。 |
| 2025 · NeurIPS | [Signal and Noise: A Framework for Reducing Uncertainty in Language Model Evaluation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/18b3b2947174ae9b1a8fc91ff89f4eb6-Abstract-Conference.html) | 定义基准区分模型的信号与对训练步随机性的噪声，分析信噪比对小规模决策和缩放律预测误差的影响，并测试降低噪声的干预。 |
| 2025 · UAI | [Multi-group Uncertainty Quantification for Long-form Text Generation](https://proceedings.mlr.press/v286/liu25a.html) | 揭示长文本声明校准和共形保证在总体上成立却可在群组内失效，并用多重校准与多重有效共形预测改善群组内保证。 |
| 2025 · UAI | [The Consistency Hypothesis in Uncertainty Quantification for Large Language Models](https://proceedings.mlr.press/v286/xiao25a.html) | 把“生成一致性可代理置信度”形式化为三个可检验命题，设计统计检验与符合度指标，并据此构造无数据黑箱UQ方法。 |
| 2024 · ICLR | [Conformal Language Modeling](https://iclr.cc/virtual/2024/poster/17755) | 为语言模型采样校准停止规则和拒绝规则，构造至少含一个可接受回答的候选集合，并对回答片段给出分布无关保证。 |
| 2024 · ICML | [Language Models with Conformal Factuality Guarantees](https://proceedings.mlr.press/v235/mohri24a.html) | 把语言模型输出正确性转化为不确定性集合问题，提出逐步降低回答具体度的共形事实性框架，以少量人工标注获得高概率正确性保证。 |
| 2024 · NAACL | [ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems](https://aclanthology.org/2024.naacl-long.20/) | 以合成训练数据训练轻量语言模型评审器，并用少量人工标注通过PPI校正，估计RAG系统的上下文相关性、忠实性和答案相关性。 |
| 2024 · NeurIPS | [Large language model validity via enhanced conformal prediction methods](https://proceedings.neurips.cc/paper_files/paper/2024/hash/d02ff1aeaa5c268dc34790dd1ad21526-Abstract-Conference.html) | 针对LLM回答过滤的条件有效性与效用损失，扩展条件共形方法以自适应放宽保证，并通过可微条件共形过程改进评分器。 |
| 2024 · NeurIPS | [Prediction-Powered Ranking of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/hash/cd47cd67caa87f5b1944e00f6781598f-Abstract-Conference.html) | 用少量人类两两偏好和大量强LLM偏好构造每个候选模型的排名集合，并给出对人类偏好真排名的渐近覆盖保证。 |
| 2024 · NeurIPS | [Stratified Prediction-Powered Inference for Effective Hybrid Evaluation of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c9fcd02e6445c7dfbad6986abee53d0d-Abstract-Conference.html) | 提出分层预测增强推断StratPPI，以少量人工标签和大量自动标签构造任意维参数的有效置信区间，并通过分层与样本分配提高LLM评估效率。 |
