<!-- Generated from data/*.yaml by scripts/render.py. Do not edit directly. -->

# 合成数据与调查有效性

[返回目录](../README.md) · 13 篇主目录论文

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2026 · ACL | [Valid Survey Simulations with Limited Human Data: The Roles of Prompting, Fine-Tuning, and Rectification](https://aclanthology.org/2026.acl-long.498/) | 比较LLM调查回答的提示、微调与PPI式事后校正，显示仅合成带来显著偏差，而把多数有限真人预算用于校正可大幅降低总体均值估计偏差。 |
| 2026 · COLT | [Universal Priors: Solving Empirical Bayes via Bayesian Inference and Pretraining](https://proceedings.mlr.press/v336/cannella26a.html) | 把经验贝叶斯问题改写为在合成任务分布上预训练后进行贝叶斯预测，并在Poisson经验贝叶斯中给出接近最优的统一遗憾界与后验收缩结果。 |
| 2026 · Marketing Science | [Large Language Models for Market Research: A Data-Augmentation Approach](https://pubsonline.informs.org/doi/10.1287/mksc.2025.0009) | 用少量人类数据校正 LLM 合成选择数据，提高联合分析中的偏好估计效率。 |
| 2025 · CLeaR | [Counterfactual Token Generation in Large Language Models](https://proceedings.mlr.press/v275/chatzi25a.html) | 基于 Gumbel-Max 结构因果模型建立 token 生成的反事实耦合，使现有 LLM 无需微调即可生成“若早先 token 不同”的反事实文本。 |
| 2025 · ICML | [Collapse or Thrive: Perils and Promises of Synthetic Data in a Self-Generating World](https://proceedings.mlr.press/v267/kazdan25a.html) | 比较纯替换、累积混合及固定子样本三种递归合成训练流程，在高斯估计、核密度估计和语言模型微调中区分爆炸崩溃、稳定与缓慢退化。 |
| 2025 · ICML | [How to Synthesize Text Data without Model Collapse?](https://proceedings.mlr.press/v267/zhu25d.html) | 发现合成文本比例与LM性能负相关，并以分布偏移和n-gram过度集中解释；提出对人类文本做token编辑的半合成方案并给出有限测试误差上界。 |
| 2025 · Marketing Science · 数据报告 | [Database Report: Twin-2K-500: A Data Set for Building Digital Twins of over 2,000 People Based on Their Answers to over 500 Questions](https://pubsonline.informs.org/doi/10.1287/mksc.2025.0262) | 提供 2,058 人、四轮、500 多道问题的数据及重测基准，用于构建和验证个人数字孪生。 |
| 2025 · NeurIPS | [Self-Verification Provably Prevents Model Collapse in Recursive Synthetic Training](https://proceedings.neurips.cc/paper_files/paper/2025/hash/3380e8116452e0efbf36f35d95e88c94-Abstract-Conference.html) | 证明递归合成训练在缺少足量真实数据时产生指数误差增长，并给出仅靠模型内部置信度自验证即可避免崩溃的有限样本误差界。 |
| 2024 · Journal of Marketing | [AI–Human Hybrids for Marketing Research: Leveraging Large Language Models (LLMs) as Collaborators](https://journals.sagepub.com/doi/10.1177/00222429241276529) | 通过合成受访者、访谈和调查复现，评估人类与 LLM 协作开展营销研究的有效性。 |
| 2024 · Marketing Science | [Frontiers: Can Large Language Models Capture Human Preferences?](https://pubsonline.informs.org/doi/10.1287/mksc.2023.0306) | 比较 LLM 与人类跨期偏好，并用 chain-of-thought conjoint 分析偏好差异。 |
| 2024 · Marketing Science | [Frontiers: Determining the Validity of Large Language Models for Automated Perceptual Analysis](https://pubsonline.informs.org/doi/10.1287/mksc.2023.0454) | 研究 LLM 生成品牌感知数据与人类调查数据的一致性及适用范围。 |
| 2024 · NAACL | [ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems](https://aclanthology.org/2024.naacl-long.20/) | 以合成训练数据训练轻量语言模型评审器，并用少量人工标注通过PPI校正，估计RAG系统的上下文相关性、忠实性和答案相关性。 |
| 2023 · ICML | [Using Large Language Models to Simulate Multiple Humans and Replicate Human Subject Studies](https://proceedings.mlr.press/v202/aher23a.html) | 用 Turing Experiments 模拟参与者群体，复现经济学、语言和社会心理实验并识别系统偏差。 |
