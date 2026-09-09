# 营销与 LLM simulation：按应用阅读

[返回目录](../README.md) · [营销索引](../topics/marketing.md) · [Simulation 索引](../topics/simulation.md)

当前营销索引有 **6 篇主目录、3 篇背景补充**；simulation 索引有 **9 篇主目录、6 篇补充**。标签交叉，不能相加。营销目标期刊包括 Marketing Science、Journal of Marketing Research、Journal of Marketing、Journal of Consumer Research。

## 可以从哪些应用入手

| 应用 | 代表论文 | 阅读重点 |
| --- | --- | --- |
| 合成消费者与联合分析 | [Large Language Models for Market Research: A Data-Augmentation Approach](https://pubsonline.informs.org/doi/10.1287/mksc.2025.0009) · Marketing Science 2026 | 用少量真人数据校正合成选择数据；先区分模拟回答与人类偏好估计。 |
| 偏好与品牌感知验证 | [Can Large Language Models Capture Human Preferences?](https://pubsonline.informs.org/doi/10.1287/mksc.2023.0306)、[Automated Perceptual Analysis](https://pubsonline.informs.org/doi/10.1287/mksc.2023.0454) · Marketing Science 2024 | 比较模型与真人的选择、属性评价和品牌感知，关注偏差随任务变化。 |
| 营销访谈与调查 | [AI–Human Hybrids for Marketing Research](https://journals.sagepub.com/doi/10.1177/00222429241276529) · JM 在线 2024 / 卷期 2025 | 合成受访者、访谈和真实企业研究复现；提示与 RAG 如何改变回答。 |
| 个人数字孪生 | [Twin-2K-500](https://pubsonline.informs.org/doi/10.1287/mksc.2025.0262) · Marketing Science 2025，数据库报告 | 用多波真实个体数据和重测基准验证预测；这是数据与验证贡献。 |
| 合成调查的统计校正 | [Valid Survey Simulations with Limited Human Data](https://aclanthology.org/2026.acl-long.498/) · ACL 2026 | 已在最初目录中；结合真人预算讨论提示、微调和事后校正。 |
| 人类实验复现 | [Using Large Language Models to Simulate Multiple Humans and Replicate Human Subject Studies](https://proceedings.mlr.press/v202/aher23a.html) · ICML 2023 | 在经典经济和社会心理实验中比较模拟群体与既有发现，识别系统失真。 |
| 宏观经济模拟 | [EconAgent](https://aclanthology.org/2024.acl-long.829/) · ACL 2024 | 模拟异质主体的劳动、消费与记忆，检查宏观现象是否能合理重现。 |
| 金融市场与社交互动 | [TwinMarket](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5bf234ecf83cd77bc5b77a24ba9338b0-Abstract-Conference.html) · NeurIPS 2025 主会 | 观察交易与社交反馈如何形成集体现象；仿真输出不自动等于现实市场预测。 |
| 新营销内容的因果预测 | [Evaluating Novel Unstructured Treatments with Generative AI](https://journals.sagepub.com/doi/10.1177/00222437261476639) · JMR 2026 已接收稿 | LLM 构造内容表示，拒绝采样限制外推；这是因果方法应用，不是合成受访者 simulation。 |

## 社会代理与经济实验的补充入口

- [Generative Agents](https://doi.org/10.1145/3586183.3606763)：UIST 2023 正式论文，25 个虚拟人物的记忆、反思与规划；UIST 目前未列入目标 venue，因此列补充。
- [LLM Agents Grounded in Self-Reports Enable General-Purpose Simulation of Individuals](https://arxiv.org/abs/2411.10109)：原题为 **Generative Agent Simulations of 1,000 People**；条目采用 2026-06-28 的 v3，保留首次预印本年份 2024。比较访谈、调查和人口学画像构建的个人代理。
- [AgentSociety 的并行模拟框架](https://aclanthology.org/2025.acl-industry.94/)：ACL 2025 **Industry Track**，按特别轨列补充，不能标成 ACL 主会研究论文。
- [Homo Silicus](https://www.nber.org/papers/w31122)：NBER 工作论文，首次 2023、修订 2026；为代理设置禀赋、信息和偏好，探索经济实验及变体。
- [Evaluating the statistical realism of LLM-generated social science data](https://www.pnas.org/doi/10.1073/pnas.2538145123)：PNAS 2026，用于检查合成数据的统计真实性；PNAS 在当前主目录名单之外。

## 范围与证据如何区分

营销应用已加入，但仍排除以 LLM 采用、引入或普及为处理变量、估计其对真实生产率、就业、学习等结果之因果效应的文章。LLM 作为模拟主体、数据生成器、内容表示或因果估计组件的研究可以纳入。纯文案生成、一般采用态度研究或只在参考文献提到 LLM，不因属于营销期刊就自动收录。

Simulation 指对人或社会经济系统的模拟。合成文本用于训练 LLM、模型坍塌理论、普通 Monte Carlo 实验不自动计入这一主题。阅读时分别看行为是否可信、预测是否准确、总体统计量是否校准，以及因果效应是否有识别依据。

JCR 本轮核实并保留了消费研究与定性协作的背景文章，列在[营销索引的补充部分](../topics/marketing.md)。当前没有进入主目录的 JCR 条目；这不表示 JCR 不存在相关研究。四刊全年度关键词扫描和定向网络检索都未达到穷尽文献的程度。
