# GPI 与非结构化数据因果推断阅读指南

[返回研究地图](research-map.zh.md) · [因果估计主目录](../topics/causal-estimation.md) · [补充文献](supplementary.md)

定向核验日期：**2026-10-08**。范围沿用 2022–2026，关注生成模型或预训练语言表示如何支持文本、图像及多模态数据中的混杂调整和处理效应估计。本页是精选阅读路线，不代表穷尽检索或论文质量排名。

本轮正式新增 **10 篇**：PNAS GPI 与 9 篇相近工作，分为 **3 篇主目录、7 篇补充**。当前全目录为 **87 篇主目录、34 篇补充、1 篇待核验**。生成式 LLM 直接方法的目标 venue 已发表论文进入主目录；预印本、编码型语言模型方法背景与名单外期刊进入补充。正式发表与预印本、编码器与生成式模型的角色分别注明。

## 起点：本轮已收录的 GPI

**Kosuke Imai、Kentaro Nakamura，Leveraging generative AI for causal inference with unstructured data**，PNAS 2026，123(36)，e2530532123；首次在线发表 2026-09-03。

[出版社链接](https://doi.org/10.1073/pnas.2530532123) · [出版 PDF](https://imai.sites.fas.harvard.edu/research/files/GPI.pdf) · [出版社提交的 Crossref 元数据](https://api.crossref.org/works/10.1073/pnas.2530532123) · [GPI 软件](https://gpi-pack.github.io/)

GPI 从生成模型中取得用于生成或重现文本、图像的内部表示，学习低维混杂调整变量，再估计效应及不确定性。正文展示文本混杂、图像特征处理和文本结构模型三种设置。阅读时应分开检查：原始内容能否由表示恢复、混杂是否已被观测信息覆盖，以及学出的调整变量能否同时保留结果信息和满足重叠。

PNAS 不在当前目标期刊名单，因此列为重点补充。发表身份由出版社提交的 Crossref 登记、出版 PDF 与 PubMed 索引交叉核对；PNAS 网页转 cookie 页面，未将该访问限制写成已读取官方网页。方法核验到正文和 arXiv v4 附录关键段落，未独立审计全部证明或复现实验。

## 六篇优先近邻

| 顺序 | 论文与状态 | 与 GPI 的联系及阅读重点 |
| --- | --- | --- |
| 1 | [Causal Inference with Generative Artificial Intelligence: Application to Texts as Treatments](https://doi.org/10.1080/01621459.2026.2689629) — Imai、Nakamura；**JASA 2026，主目录** | GPI 文本处理方法的直接前序。展开文本特征效应的识别、可分离条件及 DML 估计；与 PNAS 是不同论文。最适合接着读。 |
| 2 | [Adjustment for Confounding using Pre-Trained Representations](https://proceedings.mlr.press/v267/schulte25a.html) — Schulte、Rügamer、Nagler；**ICML 2025，补充** | 研究预训练表示何时足以调整混杂，以及表示维度与变换如何影响 DML。文本实验使用 BERT，影像使用 DenseNet；可用于审视 GPI 的表示充分性条件。 |
| 3 | [Isolated Causal Effects of Natural Language](https://proceedings.mlr.press/v267/lin25k.html) — Lin、Morency、Ben-Michael；**ICML 2025，主目录** | 区分目标语言属性的独立效应与伴随属性效应，结合双重稳健估计、表示信息保真、重叠和遗漏变量敏感性分析。包含 GPT-3.5 抽取协变量方案的比较。 |
| 4 | [DoubleMLDeep: Estimation of Causal Effects with Multimodal Data](https://arxiv.org/abs/2402.01785) — Klaassen 等；**2024 预印本，补充** | 将表格、文本和图像共同用于 nuisance 学习和部分线性 DML。处理主要是标量，非结构化内容主要作混杂信息；实验使用 RoBERTa、ViT、SAINT，不应把架构讨论中的 Llama 写成已完成实验。 |
| 5 | [GenAI Powered Dynamic Causal Inference with Unstructured Data](https://arxiv.org/abs/2605.07834) — Nakamura、Imai；**2026 预印本，补充** | 把静态 GPI 扩展至有序文本片段中的动态随机干预，研究特征出现位置。当前设定中每位受访者有一个最终结果。 |
| 6 | [Causal Inference with Video Features as Treatments](https://arxiv.org/abs/2607.06126) — Nakamura、Breuer、Crespin、Dietrich、Imai；**2026 预印本，补充** | 扩展到视频特征和观众反应的连续轨迹。使用视觉与转录文本表示；实际实现未直接建模原始声学特征。 |

JASA 论文的在线日期 **2026-07-27** 来自 Informa 提交的 [Crossref 登记](https://api.crossref.org/works/10.1080/01621459.2026.2689629)；出版社网页返回 403。DOI 创建日 2026-06-23 不作为发表日。其[复现代码](https://github.com/k-nakam/gpi_replication)已确认，但本轮未运行。

两篇动态扩展均核对到 arXiv **2026-09-15 的 v2**；DoubleMLDeep 核对到 **2024-02-01 的 v1**。本轮未取得这三篇的正式发表或录用证据。本次收录时，预印本按首次预印本年份归档，避免将版本更新当成新论文。

## 两篇方法背景

- [Causal Estimation for Text Data with (Apparent) Overlap Violations](https://iclr.cc/virtual/2023/poster/11330) — Gui、Veitch，**ICLR 2023，补充**。讨论文本属性可由全文预测时的重叠问题，用 DistilBERT 学习处理无关表示。适合作为 GPI 的前置方法背景；估计对象依赖特定文本因果分解，不宜笼统写成所有情形的 ATE。
- [Text-Transport: Toward Learning Causal Effects of Natural Language](https://aclanthology.org/2023.emnlp-main.82/) — Lin、Morency、Ben-Michael，**EMNLP 2023，主目录**。以文本分布比权重迁移语言属性效应，语言模型版本使用 GPT-3 的 text-davinci-003。它侧重跨分布迁移，可与上面的 isolated effects 论文连读；迁移仍要求有效源域与支持条件。

## 与 repo 现有论文连读

- [DoubleLingo: Causal Estimation with Large Language Models](https://aclanthology.org/2024.naacl-short.71/)（NAACL 2024，已在主目录）：比较文本混杂信息如何进入 nuisance 学习与 DML。
- [Evaluating Novel Unstructured Treatments with Generative AI: A Causal Prediction Framework](https://doi.org/10.1177/00222437261476639)（JMR 2026，repo 基线记录为已接收稿）：关注新营销内容的因果效果预测与外推，适合比较“已有内容的混杂调整”和“新内容的效应预测”。本轮未重新核验该已有条目的发表状态。

建议先读 **PNAS GPI → JASA 文本方法 → ICML 表示有效性 → ICML 独立文本效应**；实际数据含多种模态时接 DoubleMLDeep，研究处理顺序或视频时再读两个动态扩展。

## EDITH 发现的应用背景补充

[Uncovering Synergy and Dysergy in Consumer Reviews: A Machine Learning Approach](https://pubsonline.informs.org/doi/10.1287/mnsc.2022.4443)（Zhang、Yang、Zhang、Palmatier，Management Science）首次在线于 **2022-05-27**，卷期年为 2023。它用 Siamese BERT 表示/聚类评论意见，以其余意见和协变量作调整，并使用 GRF、AIPW 和敏感性分析。可作为预训练 NLP 辅助效应分析的应用背景；评分系数或 GRF 输出的因果解释仍取决于识别条件。官方摘要和发表元数据已核对，方法细节来自本轮 EDITH 原文局部阅读。现已列入补充，标注编码型预训练 NLP 的方法角色；不将其表述为生成式 LLM 实验。

另一命中 [Influence via Ethos](https://pubsonline.informs.org/doi/10.1287/mnsc.2023.4762) 虽用 DML/IV 调整论辩文本，但本轮读到的模型为词袋输入的全连接 ReLU 网络，因此未推进为本轮 LLM 候选。它的首次在线年为 2023，不能直接使用 EDITH 的卷期年 2024。

## 证据边界

本轮网络工作核对发表元数据、摘要与部分方法/假设段落；未复现实验，未逐项审核定理证明。主目录与补充的分层是范围与方法角色的编辑判断，不是对所有识别假设成立的保证。EDITH 检索范围和结果另见[来源与核验](sources.md)。
