<!-- Generated from data/*.yaml by scripts/render.py. Do not edit directly. -->

# 合成数据与调查有效性

[返回目录](../README.md) · 7 篇主目录论文

| 年份 / Venue | 论文 | 方法与 LLM 的关系 |
| --- | --- | --- |
| 2026 · ACL | [Valid Survey Simulations with Limited Human Data: The Roles of Prompting, Fine-Tuning, and Rectification](https://aclanthology.org/2026.acl-long.498/) | 比较LLM调查回答的提示、微调与PPI式事后校正，显示仅合成带来显著偏差，而把多数有限真人预算用于校正可大幅降低总体均值估计偏差。 |
| 2026 · COLT | [Universal Priors: Solving Empirical Bayes via Bayesian Inference and Pretraining](https://proceedings.mlr.press/v336/cannella26a.html) | 把经验贝叶斯问题改写为在合成任务分布上预训练后进行贝叶斯预测，并在Poisson经验贝叶斯中给出接近最优的统一遗憾界与后验收缩结果。 |
| 2025 · CLeaR | [Counterfactual Token Generation in Large Language Models](https://proceedings.mlr.press/v275/chatzi25a.html) | 基于 Gumbel-Max 结构因果模型建立 token 生成的反事实耦合，使现有 LLM 无需微调即可生成“若早先 token 不同”的反事实文本。 |
| 2025 · ICML | [Collapse or Thrive: Perils and Promises of Synthetic Data in a Self-Generating World](https://proceedings.mlr.press/v267/kazdan25a.html) | 比较纯替换、累积混合及固定子样本三种递归合成训练流程，在高斯估计、核密度估计和语言模型微调中区分爆炸崩溃、稳定与缓慢退化。 |
| 2025 · ICML | [How to Synthesize Text Data without Model Collapse?](https://proceedings.mlr.press/v267/zhu25d.html) | 发现合成文本比例与LM性能负相关，并以分布偏移和n-gram过度集中解释；提出对人类文本做token编辑的半合成方案并给出有限测试误差上界。 |
| 2025 · NeurIPS | [Self-Verification Provably Prevents Model Collapse in Recursive Synthetic Training](https://proceedings.neurips.cc/paper_files/paper/2025/hash/3380e8116452e0efbf36f35d95e88c94-Abstract-Conference.html) | 证明递归合成训练在缺少足量真实数据时产生指数误差增长，并给出仅靠模型内部置信度自验证即可避免崩溃的有限样本误差界。 |
| 2024 · NAACL | [ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems](https://aclanthology.org/2024.naacl-long.20/) | 以合成训练数据训练轻量语言模型评审器，并用少量人工标注通过PPI校正，估计RAG系统的上下文相关性、忠实性和答案相关性。 |
