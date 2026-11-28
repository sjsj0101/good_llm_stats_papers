<!-- Generated from data/*.yaml by scripts/render.py. Do not edit directly. -->

# LLM 行为、经济与社会模拟

[返回目录](../README.md) · 9 篇主目录论文

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2026 · ACL | [Valid Survey Simulations with Limited Human Data: The Roles of Prompting, Fine-Tuning, and Rectification](https://aclanthology.org/2026.acl-long.498/) | 比较LLM调查回答的提示、微调与PPI式事后校正，显示仅合成带来显著偏差，而把多数有限真人预算用于校正可大幅降低总体均值估计偏差。 |
| 2026 · Marketing Science | [Large Language Models for Market Research: A Data-Augmentation Approach](https://pubsonline.informs.org/doi/10.1287/mksc.2025.0009) | 用少量人类数据校正 LLM 合成选择数据，提高联合分析中的偏好估计效率。 |
| 2025 · Marketing Science · 数据报告 | [Database Report: Twin-2K-500: A Data Set for Building Digital Twins of over 2,000 People Based on Their Answers to over 500 Questions](https://pubsonline.informs.org/doi/10.1287/mksc.2025.0262) | 提供 2,058 人、四轮、500 多道问题的数据及重测基准，用于构建和验证个人数字孪生。 |
| 2025 · NeurIPS | [TwinMarket: A Scalable Behavioral and Social Simulation for Financial Markets](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5bf234ecf83cd77bc5b77a24ba9338b0-Abstract-Conference.html) | 在股票市场与社交环境中模拟异质投资者，研究个体互动形成的市场集体现象。 |
| 2024 · ACL | [EconAgent: Large Language Model-Empowered Agents for Simulating Macroeconomic Activities](https://aclanthology.org/2024.acl-long.829/) | 用带感知与记忆的异质 LLM agents 模拟劳动、消费决策及宏观经济动态。 |
| 2024 · Journal of Marketing | [AI–Human Hybrids for Marketing Research: Leveraging Large Language Models (LLMs) as Collaborators](https://journals.sagepub.com/doi/10.1177/00222429241276529) | 通过合成受访者、访谈和调查复现，评估人类与 LLM 协作开展营销研究的有效性。 |
| 2024 · Marketing Science | [Frontiers: Can Large Language Models Capture Human Preferences?](https://pubsonline.informs.org/doi/10.1287/mksc.2023.0306) | 比较 LLM 与人类跨期偏好，并用 chain-of-thought conjoint 分析偏好差异。 |
| 2024 · Marketing Science | [Frontiers: Determining the Validity of Large Language Models for Automated Perceptual Analysis](https://pubsonline.informs.org/doi/10.1287/mksc.2023.0454) | 研究 LLM 生成品牌感知数据与人类调查数据的一致性及适用范围。 |
| 2023 · ICML | [Using Large Language Models to Simulate Multiple Humans and Replicate Human Subject Studies](https://proceedings.mlr.press/v202/aher23a.html) | 用 Turing Experiments 模拟参与者群体，复现经济学、语言和社会心理实验并识别系统偏差。 |

## 补充阅读（13 篇）

预印本、名单外 venue、特别轨或背景指南，均不计入上方主目录数。具体理由见[补充列表](../docs/supplementary.md)。

| 年份 / Venue | 论文 | 方法或应用与 LLM 的关系 |
| --- | --- | --- |
| 2026 · Proceedings of the National Academy of Sciences | [Evaluating the statistical realism of LLM-generated social science data](https://www.pnas.org/doi/10.1073/pnas.2538145123) | 提出SSDataBench，以五类总体统计模式和显著性检验评估15个LLM生成社会科学样本的统计现实性。 |
| 2026 · arXiv · 预印本 | [Valid Inference with Synthetic Data via Task Exchangeability](https://arxiv.org/abs/2606.13629) | 利用同时具有真实与合成数据的历史任务，为当前仅有合成数据的任务构造具有有效性保证的推断。 |
| 2023 · UIST | [Generative Agents: Interactive Simulacra of Human Behavior](https://doi.org/10.1145/3586183.3606763) | 用记忆、反思和规划构建 25 个虚拟人物，展示个体与群体行为的交互式模拟。 |
| 2024 · arXiv · 预印本 | [LLM Agents Grounded in Self-Reports Enable General-Purpose Simulation of Individuals](https://arxiv.org/abs/2411.10109) | 基于 1,052 人的访谈、调查或二者组合构建个人代理，并对照人类重测表现验证预测。 |
| 2025 · ACL · industry | [A Parallelized Framework for Simulating Large-Scale LLM Agents with Realistic Environments and Interactions](https://aclanthology.org/2025.acl-industry.94/) | AgentSociety 将现实社会环境与并行交互结合，支持大规模 LLM 社会代理仿真。 |
| 2023 · NBER Working Paper · 预印本 | [Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?](https://www.nber.org/papers/w31122) | 给 LLM 设定禀赋、信息和偏好，模拟经济行为并对照既有实验结果。 |
| 2026 · arXiv · 预印本 | [Causally Fair Generation with Large Language Models](https://arxiv.org/abs/2610.04444) | 以参考人群数据和因果图约束LLM生成，选择性移除用户指定的因果路径效应，并保留被允许的路径；同时处理不按因果顺序给出信息的查询。 |
| 2026 · NBER Working Paper · 预印本 | [HouseholdBench: Evaluating Large Language Models as Predictors of Household Economic Behavior](https://www.nber.org/papers/w35927) | 将家庭调查中的消费、收入、劳动、预期与住房行为组织为多类型预测任务，对照不变预测和梯度提升树，评估LLM作为家庭行为代理的预测能力及偏差。 |
| 2026 · AI | [Are Human and LLM-Generated Observations Statistically Comparable? Rethinking Sampling Units, Variability, and Statistical Inference](https://www.mdpi.com/2673-2688/7/11/446) | 区分人群抽样的异质性与LLM重复生成的算法变异，提出按推断目标、抽样单位、依赖结构和验证证据组织人机数据比较的流程。 |
| 2026 · Nature Computational Science | [Cognitive grounding improves LLM simulation of collective human behavior](https://www.nature.com/articles/s43588-026-01080-z) | 向供应链博弈中的LLM角色提供行为决策规则的定性描述，再比较多角色交互轨迹与人类校准参照。作者报告轨迹拟合得到改善，但不同角色和模型的参数对齐并不均匀。 |
| 2026 · arXiv · 预印本 | [Validating LLM-Generated Synthetic Survey Samples: A Use-Dependent Multi-Dimensional Framework for Social-Science Applications](https://arxiv.org/abs/2611.00256) | 以合成样本的使用目的区分个体预测、边际分布与实质关系三种验证目标，在欧盟居民AI态度调查上比较由真实受访者画像条件生成的LLM回答。作者报告不同模型、结果和验证维度表现不一致，不能用单一准确率判断可用性。 |
| 2026 · SSRN · 预印本 | [Completions, Not Convictions: Can LLM Outputs Proxy for Human Expectations?](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7265538) | 对照预测市场、分析师预测和家庭调查，检验LLM生成预期能否替代人类测量。作者报告替代会扭曲部分群体差异与下游回归结论，真人验证数据可减小部分估计偏差。 |
| 2026 · arXiv · 预印本 | [Training decision models for simulating human respondents](https://arxiv.org/abs/2611.31613) | 用历史个体选择数据训练决策模型，再在未参与训练的研究中评估合成受访者对下游偏好与处理效应的恢复。作者报告跨研究训练能降低部分任务误差，但更低的选择预测损失不必然带来更准确的效应估计。 |

[按应用场景阅读](../docs/marketing-simulation.md)。
