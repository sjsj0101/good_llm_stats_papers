# 数据字段与口径

[返回目录](../README.md)

`data/papers.yaml` 是主目录的唯一数据来源；补充、待核验记录和覆盖台账分别维护。生成器不依赖私人文献库，可以在克隆仓库后直接运行。

| 字段 | 含义 |
| --- | --- |
| work_id | 稳定的文献标识，更新时保留 |
| title / authors | 官方标题与作者 |
| venue / venue_group | 冻结名单中的 venue 与领域 |
| year / publication_dates | 主发表年份与独立保存的在线、录用、卷期日期 |
| track | 主会、期刊、Findings 或其他轨道 |
| publication_status | published、accepted、preprint 或 unknown |
| official_url / paper_url | 官方发表证据与可得的论文链接 |
| doi / arxiv_id / openreview_id | 版本匹配与查重标识 |
| topics | 可交叉的八类主题标签 |
| summary_zh / llm_role_zh / method_zh | 原创中文摘要、LLM 的角色和方法 |
| estimand_zh / assumptions_zh / guarantee_zh | 来源支持的估计对象、假设与保证；未知为 null |
| evidence_basis / evidence_locator | 实际读取的证据类型与位置 |
| verification_status / fulltext_status | 发表核验和全文阅读状态，二者分开 |
| scope_decision / decision_reason_zh | include、supplement、pending、exclude 与理由 |
| limitations_zh | 论文限制或本轮阅读深度限制 |
| discovered_via / source_urls | 网络/本地来源类别与公开证据链接 |

`available-partially-read` 表示取得并局部读取文本，不表示已逐页审计全文。官方元数据核实也不代表定理和实证结论已被独立验证。

覆盖台账中的 `partial` 表示有单篇核验或本地关键词扫描，`search-only` 表示有定向查询；二者都不等于穷尽年度目录。零收录不等于不存在相关论文。
