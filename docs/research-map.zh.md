# 中文研究地图与阅读顺序

[返回目录](../README.md) · [覆盖说明](coverage.md)

本轮主目录 75 篇。按你的筛选要求，研究 LLM 使用、引入或普及对生产率、就业等现实结果之因果效应的文章不纳入。以下阅读顺序按与统计/因果研究设计的直接联系排列，不是论文质量排名。

## 建议先读

| 顺序 | 问题 | 论文 | 阅读重点 |
| --- | --- | --- | --- |
| 1 | 文本进入因果估计 | [DoubleLingo: Causal Estimation with Large Language Models](https://aclanthology.org/2024.naacl-short.71/) · NAACL 2024 | 看 LLM 如何服务 nuisance 函数与双重机器学习；估计对象、文本混杂是否充分及 nuisance 收敛条件仍要分开检查。 |
| 2 | 模型代理标签进入统计推断 | [Stratified Prediction-Powered Inference for Effective Hybrid Evaluation of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c9fcd02e6445c7dfbad6986abee53d0d-Abstract-Conference.html) · NeurIPS 2024 | 看如何用真人标签校正模型误差，再考虑分层与有限标注预算；代理预测准确率不能直接替代推断有效性。 |
| 3 | 合成调查的有效性 | [Valid Survey Simulations with Limited Human Data: The Roles of Prompting, Fine-Tuning, and Rectification](https://aclanthology.org/2026.acl-long.498/) · ACL 2026 | 把提示、微调与事后校正放在同一预算问题下比较，适合连接统计方法与社会科学应用。 |
| 4 | LLM 先验与因果识别 | [Causal Order: The Key to Leveraging Imperfect Experts in Causal Inference](https://openreview.net/forum?id=9juyeCqL0u) · ICLR 2025 | 比较让 LLM 给因果边与给变量顺序的区别，检查不完美专家信息如何影响下游发现及估计。 |
| 5 | 工具变量发现 | [IV Co-Scientist: Multi-Agent LLM Framework for Causal Instrumental Variable Discovery](https://proceedings.mlr.press/v323/sheth26a.html) · CLeaR 2026 | 看候选生成、批判和检验流程；候选工具变量的排除限制需要研究设计与领域证据，不能由语言模型自证。 |
| 6 | 生成回答的置信保证 | [Conformal Language Modeling](https://iclr.cc/virtual/2024/poster/17755) · ICLR 2024 | 明确保证针对候选回答集合中的可接受答案，而非每一句回答都正确；随后查校准与分布条件。 |
| 7 | 上下文学习的统计理论 | [Trained Transformers Learn Linear Models In-Context](https://jmlr.org/papers/v25/23-1042.html) · JMLR 2024 | 先读线性回归、单层线性注意力这一可分析设定，区分受控理论对象与现实通用 LLM。 |
| 8 | LLM 文本上的统计检验 | [A statistical framework of watermarks for large language models: Pivot, detection efficiency and optimal rules](https://projecteuclid.org/journals/annals-of-statistics/volume-53/issue-1/A-statistical-framework-of-watermarks-for-large-language-models/10.1214/24-AOS2468.short) · Annals of Statistics 2025 | 从枢轴量、检测效率与最优规则理解统计学顶刊的切入点；这条线主要是统计方法用于 LLM。 |

## 方法之间的关系

**LLM 辅助统计/因果研究**最值得先沿两条线读。一条把模型预测、标签或合成回答当作带误差的辅助数据，再用真实观测做校正；另一条把模型当作提供图结构、变量顺序或 IV 候选的知识来源。两条线的关键区别在于：前者主要处理估计误差，后者还必须处理识别信息是否可信。上述 DoubleLingo、分层 PPI、调查校正、Causal Order 与 IV Co-Scientist 分别提供了具体入口。

**因果发现中的知识与数据结合**可对照 [Causal Modelling Agents](https://openreview.net/forum?id=pAoqRlTBtY) 和 [LLM-CD](https://doi.org/10.1145/3711896.3736874)。它们将语言模型的元数据知识与数据驱动的结构学习结合；官方摘要支持这一区分，但本轮没有逐项审计其因果充分性、忠实性或模型设定。读到一个因果图时，仍需追问每条边来自观测数据、背景知识还是额外假设。

**用统计方法研究 LLM**包括生成不确定性、评测、排名与水印检验。例如 [Prediction-Powered Ranking](https://proceedings.neurips.cc/paper_files/paper/2024/hash/cd47cd67caa87f5b1944e00f6781598f-Abstract-Conference.html) 研究带人类偏好参考的排名集合，官方摘要给出的是渐近覆盖；水印论文则研究检验功效与最优性。它们与实证因果效应估计的目标不同，已通过主题标签区分。

**因果推理 benchmark 与识别方法要分别读。** CLadder、Corr2Cause、CounterBench 等用于检验模型在构造任务上的表现；它们能说明某类题目能否做对。将模型用于一个新的真实因果问题时，仍要单独建立估计对象、识别条件、测量方案和不确定性评估。内部机制干预、因果对齐等文章也另有主题标签，方便按兴趣筛选。

**上下文学习理论**中，线性回归或经验贝叶斯模型提供清楚的数学对象。[Universal Priors](https://proceedings.mlr.press/v336/cannella26a.html) 将预训练与经验贝叶斯联系起来；其 Poisson 模型与理想化预测器假设应和通用聊天模型区分。本轮保留这些直接研究 Transformer/预训练统计机制的论文，并在条目中标明外推边界。

## 经济学与 EDITH 的结果

按当前名单与方法口径，经济学目标期刊尚未出现进入主目录的高置信条目。EDITH 五大刊全部年份的 13,038 条原文及摘要做了关键词扫描，并结合网络补查；这不足以得出‘经济学顶刊没有相关研究’的结论。

几类相邻材料值得保留：用小规模真人数据校正合成调查/市场研究结果的方法；讨论 AI 生成回归变量误差的计量预印本；经济学顶刊中仅把 LLM 用作测量或实验材料生成的应用。它们在[补充列表](supplementary.md)中标明 venue 与贡献边界。QJE 的 Generative AI at Work 已按你的要求排除。

## 可进一步考察的问题（研究线索）

这些是基于当前目录提出的研究问题，不是已证明的文献空白：

- LLM 构造的处理、结果或混杂变量存在非经典测量误差时，如何把验证样本、PPI 与 DML 结合，并给出可用的标准误？
- LLM 提出的图或 IV 若经过同一数据集筛选，选择过程与提示迭代会怎样改变后续推断的有效性？
- 合成调查从总体均值扩展到异质效应、尾部或分组差异时，有限真人预算如何分配，哪些保证能够保留？

逐篇的 estimand、假设和理论保证只有在来源支持时才填写；未确认项留空。大多数记录核查到官方摘要，部分读取了 PDF 相关内容；尚未完成逐篇证明审计或实验复现。
