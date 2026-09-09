# Contributing

欢迎提交 LLM + statistics / causal inference 的方法论文或元数据更正。

最简单的方式是使用 [Suggest a Paper](https://github.com/sjsj0101/good_llm_stats_papers/issues/new?template=paper-suggestion.yml)：提供论文链接、官方发表或录用证据，以及具体统计/因果贡献。投稿由维护者审核，提交 Issue 不表示自动纳入。

## 纳入要求

- 主目录时间窗为 2022–2026，截至当前覆盖台账所记日期；目标 venue 见 `data/venues.yaml`。
- 必须有官方发表或录用证据。arXiv、作者主页或投稿页面单独不足以证明顶会顶刊发表。
- 写清 LLM 的角色、统计或因果任务，以及纳入理由。摘要未支持的识别假设、理论保证或实验细节保持为空。
- 排除研究 LLM 采用对生产率、就业、学习等现实结果之因果效应的论文。
- 不将 causal language modeling 与因果推断混为一谈；不将模型运行加速当作统计推断。
- 综述、Findings、特别轨、名单外期刊、预印本与边界应用放入 `data/supplementary.yaml`；证据不充分的记录放入 `data/pending.yaml`。

## 修改数据

1. 编辑 `data/papers.yaml`、补充或待定清单；保留现有 `work_id`，按 DOI、arXiv、OpenReview ID 和标题/作者查重。
2. 期刊以首次正式在线发表年为主年份，卷期年另存 `publication_dates`；会议用会议年份。
3. 如果收录数发生变化，同步对应 `data/coverage.yaml` 的 `included_count`。仅在有系统覆盖证据时更改覆盖状态；新增单篇不代表该年度已查全。
4. 运行以下命令，提交数据与生成文件：

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/render.py
python3 scripts/validate.py
python3 scripts/render.py --check
```

不要手工编辑带有 Generated 注释的索引和导出文件。不要提交论文 PDF、复制的完整摘要、访问令牌、EDITH 原文或个人电脑路径。
