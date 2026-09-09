<!-- Generated from data/*.yaml by scripts/render.py. Do not edit directly. -->

# 统计学习理论与上下文学习

[返回目录](../README.md) · 23 篇主目录论文

| 年份 / Venue | 论文 | 方法与 LLM 的关系 |
| --- | --- | --- |
| 2026 · AISTATS | [An Information-Theoretic Approach to Understanding Transformers’ In-Context Learning of Variable-Order Markov Chains](https://proceedings.mlr.press/v300/zhou26b.html) | 研究Transformer在上下文中学习变阶马尔可夫链的有限样本准确率，并构造可精确实现贝叶斯context-tree weighting的多层Transformer。 |
| 2026 · AISTATS | [Evaluation of Large Language Models via Coupled Token Generation](https://proceedings.mlr.press/v300/benz26a.html) | 建立共享外生随机性的耦合自回归因果模型，使不同 LLM 在相同随机源下比较，并证明基准评测可显著减少样本。 |
| 2026 · Biometrika · 已接收稿 | [Optimal Watermark Generation under Type I and Type II Errors](https://doi.org/10.1093/biomet/asag049) | 在同时约束第一类和第二类错误下求解LLM水印生成的最小保真损失，并构造达到下界的分布与采样规则。 |
| 2026 · COLT | [Universal Priors: Solving Empirical Bayes via Bayesian Inference and Pretraining](https://proceedings.mlr.press/v336/cannella26a.html) | 把经验贝叶斯问题改写为在合成任务分布上预训练后进行贝叶斯预测，并在Poisson经验贝叶斯中给出接近最优的统一遗憾界与后验收缩结果。 |
| 2026 · JASA | [Towards Better Statistical Understanding of Watermarking LLMs](https://www.tandfonline.com/doi/full/10.1080/01621459.2026.2618290) | 把红绿词表水印的质量—可检测性权衡写成约束优化问题，并给出在线生成算法和渐近最优性分析。 |
| 2025 · AISTATS | [On Subjective Uncertainty Quantification and Calibration in Natural Language Generation](https://proceedings.mlr.press/v258/wang25i.html) | 从贝叶斯决策论定义自由文本生成的任务相关主观不确定性与校准，并以缺失数据和超额风险刻画认知不确定性。 |
| 2025 · AISTATS | [What and How does In-Context Learning Learn? Bayesian Model Averaging, Parameterization, and Generalization](https://proceedings.mlr.press/v258/zhang25d.html) | 证明理想预训练LLM在动态提示模型下执行贝叶斯模型平均，并用PAC-Bayes界分解预训练误差，得到上下文平均误差率。 |
| 2025 · Annals of Statistics | [A statistical framework of watermarks for large language models: Pivot, detection efficiency and optimal rules](https://projecteuclid.org/journals/annals-of-statistics/volume-53/issue-1/A-statistical-framework-of-watermarks-for-large-language-models/10.1214/24-AOS2468.short) | 建立LLM水印统一统计框架，以枢轴量和大偏差效率比较检测规则并推导最优检验。 |
| 2025 · ICML | [Can Transformers Learn Full Bayesian Inference in Context?](https://proceedings.mlr.press/v267/reuter25a.html) | 构建可在上下文中输出完整后验样本的Transformer框架，覆盖广义线性模型与潜因子模型，并与MCMC和变分推断比较。 |
| 2025 · ICML | [Collapse or Thrive: Perils and Promises of Synthetic Data in a Self-Generating World](https://proceedings.mlr.press/v267/kazdan25a.html) | 比较纯替换、累积混合及固定子样本三种递归合成训练流程，在高斯估计、核密度估计和语言模型微调中区分爆炸崩溃、稳定与缓慢退化。 |
| 2025 · ICML | [How to Synthesize Text Data without Model Collapse?](https://proceedings.mlr.press/v267/zhu25d.html) | 发现合成文本比例与LM性能负相关，并以分布偏移和n-gram过度集中解释；提出对人类文本做token编辑的半合成方案并给出有限测试误差上界。 |
| 2025 · JASA | [Debiasing Watermarks for Large Language Models via Maximal Coupling](https://www.tandfonline.com/doi/abs/10.1080/01621459.2025.2520455) | 用最大耦合构造无偏LLM水印，在保持原生成分布的同时维持可检测性，并分析其统计性质。 |
| 2025 · JASA | [On the Algorithmic Bias of Aligning Large Language Models with RLHF: Preference Collapse and Matching Regularization](https://www.tandfonline.com/doi/abs/10.1080/01621459.2025.2555067) | 研究RLHF中标准KL正则化导致奖励最大化与目标偏好分布错配的算法偏差，并提出概率匹配正则化。 |
| 2025 · JRSS-B | [Robust detection of watermarks for large language models under human edits](https://doi.org/10.1093/jrsssb/qkaf056) | 研究人工编辑后LLM水印的稳健检测，提出截断拟合优度检验并刻画不同编辑强度下的检测边界。 |
| 2025 · NeurIPS | [Exploiting LLMs for Automatic Hypothesis Assessment via a Logit-Based Calibrated Prior](https://proceedings.neurips.cc/paper_files/paper/2025/hash/338b4df24eeed6767d6f72b983b845ce-Abstract-Conference.html) | 从LLM输出logit诱导变量对相关系数的连续校准先验，用先验预期程度衡量观察相关关系的新颖性，并报告可信区间覆盖。 |
| 2025 · NeurIPS | [Self-Verification Provably Prevents Model Collapse in Recursive Synthetic Training](https://proceedings.neurips.cc/paper_files/paper/2025/hash/3380e8116452e0efbf36f35d95e88c94-Abstract-Conference.html) | 证明递归合成训练在缺少足量真实数据时产生指数误差增长，并给出仅靠模型内部置信度自验证即可避免崩溃的有限样本误差界。 |
| 2024 · COLT | [Training Dynamics of Multi-Head Softmax Attention for In-Context Learning: Emergence, Convergence, and Optimality (extended abstract)](https://proceedings.mlr.press/v247/siyu24a.html) | 研究多头softmax注意力学习多任务线性回归时的梯度流，证明适当初始化下全局收敛、注意力头发生任务分配，并给出相对最优多头模型的常数因子性能界。 |
| 2024 · JMLR | [Trained Transformers Learn Linear Models In-Context](https://jmlr.org/papers/v25/23-1042.html) | 分析单层线性自注意力在随机线性回归任务上的梯度流，证明合适初始化下收敛到全局最优，并刻画新提示分布中的预测误差与协变量偏移脆弱性。 |
| 2023 · ICML | [Transformers as Algorithms: Generalization and Stability in In-context Learning](https://proceedings.mlr.press/v202/li23l.html) | 把上下文学习形式化为算法学习问题，以算法稳定性连接Transformer的超额风险，并给出多任务与新任务泛化界。 |
| 2023 · NeurIPS | [Pretraining task diversity and the emergence of non-Bayesian in-context learning for regression](https://proceedings.neurips.cc/paper_files/paper/2023/hash/2e10b2c2e1aa4f8083c37dfe269873f8-Abstract-Conference.html) | 发现预训练任务多样性存在上下文学习涌现阈值：阈值下模型接近基于预训练任务先验的贝叶斯估计，阈值上则转向近似岭回归并能处理新任务。 |
| 2023 · NeurIPS | [Transformers as Statisticians: Provable In-Context Learning with In-Context Algorithm Selection](https://proceedings.neurips.cc/paper_files/paper/2023/hash/b2e63e36c57e153b9015fece2352a9f9-Abstract-Conference.html) | 构造并分析可在上下文中实现最小二乘、岭回归、Lasso与广义线性模型学习的Transformer，并证明预测能力、规模与预训练样本复杂度。 |
| 2022 · ICLR | [An Explanation of In-context Learning as Implicit Bayesian Inference](https://iclr.cc/virtual/2022/poster/6893) | 在预训练文本由混合隐马尔可夫模型生成的理论设定中，把上下文学习解释为对共享潜在概念的隐式贝叶斯推断，并刻画预训练与提示分布失配时仍能成立的条件。 |
| 2022 · NeurIPS | [What Can Transformers Learn In-Context? A Case Study of Simple Function Classes](https://proceedings.neurips.cc/paper_files/paper/2022/hash/c529dba08a146ea8d6cf715ae8930cbe-Abstract-Conference.html) | 用线性、稀疏线性及非线性函数类检验Transformer的上下文学习能力，显示其在受控问题上可接近最小二乘、Lasso等经典估计器。 |
