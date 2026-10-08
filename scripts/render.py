"""Render the public catalog from canonical YAML. Run with --check in CI."""
from __future__ import annotations
import argparse
import collections
import csv
import io
from pathlib import Path
import yaml
from common import TOPICS, bibtex, slug, table

ROOT = Path(__file__).resolve().parents[1]
REPO = "https://github.com/sjsj0101/good_llm_stats_papers"
NOTICE = "<!-- Generated from data/*.yaml by scripts/render.py. Do not edit directly. -->\n\n"

def generate():
    def read(name):
        return yaml.safe_load((ROOT / "data" / name).read_text())
    papers = sorted(read("papers.yaml"), key=lambda r: (-r["year"], r["venue"], r["title"]))
    supplements, pending = read("supplementary.yaml"), read("pending.yaml")
    coverage, registry = read("coverage.yaml"), read("venues.yaml")
    accepted = [r for r in papers if r["publication_status"] == "accepted"]
    cutoff = coverage["cutoff"]
    groups = collections.defaultdict(list)
    for p in papers:
        groups[(p["year"], p["venue"])].append(p)
    output = {}
    for (year, venue), rows in groups.items():
        output[f"papers/{year}/{slug(venue)}.md"] = NOTICE + f"# {venue} {year}\n\n[返回目录](../../README.md) · {len(rows)} 篇\n\n" + table(rows)
    for topic, label in TOPICS.items():
        rows = [r for r in papers if topic in r["topics"]]
        output[f"topics/{topic}.md"] = NOTICE + f"# {label}\n\n[返回目录](../README.md) · {len(rows)} 篇主目录论文\n\n" + table(rows)
        if topic in {"marketing", "simulation"}:
            extra = [r for r in supplements if topic in r["topics"]]
            output[f"topics/{topic}.md"] += f"\n## 补充阅读（{len(extra)} 篇）\n\n预印本、名单外 venue、特别轨或背景指南，均不计入上方主目录数。具体理由见[补充列表](../docs/supplementary.md)。\n\n" + table(extra)
            output[f"topics/{topic}.md"] += "\n[按应用场景阅读](../docs/marketing-simulation.md)。\n"
    for filename, title, rows, description in [
        ("supplementary", "补充文献", supplements, "方法相关，但 venue、track 或贡献类型不符合主目录口径。预印本与已发表材料分别标明状态。"),
        ("pending", "待核验候选", pending, "未计入主目录；所缺官方证据见每条说明。"),
        ("accepted", "官方已接收稿", accepted, "有官方已接收稿或录用记录，计入主目录并与正式发表记录分开标注。"),
    ]:
        output[f"docs/{filename}.md"] = NOTICE + f"# {title}\n\n[返回目录](../README.md)\n\n{description}\n\n" + table(rows) + "\n## 范围与证据\n\n" + "\n".join(f"- **{r['title']}**（{r['publication_status']}）：{r['decision_reason_zh']}" for r in rows) + "\n"
    main = [NOTICE + '<div align="center">',
        "",
        "# Good LLM Stats Papers",
        "",
        "Curated research on LLMs, statistics, causal inference, marketing, and behavioral simulation.",
        "",
        "2022–2026 · 计算机、统计、经济与营销：方法和应用",
        "",
        f"[![Papers](https://img.shields.io/badge/Papers-{len(papers)}-0B7285?style=flat-square)](#paper-index) [![Target%20venues](https://img.shields.io/badge/Target_venues-{len(registry['venues'])}-364FC7?style=flat-square)](docs/coverage.md) [![Verified](https://img.shields.io/badge/Verified-{cutoff.replace('-', '--')}-5F3DC4?style=flat-square)](data/coverage.yaml) [![License](https://img.shields.io/badge/License-CC_BY_4.0-2B8A3E?style=flat-square)](LICENSE)",
        "",
        f"[**Suggest a Paper**]({REPO}/issues/new?template=paper-suggestion.yml)",
        "",
        "</div>",
        "",
        "## Scope",
        "",
        "收集 LLM 与统计推断、因果发现/识别/估计、统计学习理论、不确定性评测和合成数据有效性有实质结合的研究，同时纳入营销研究、消费者/经济行为模拟、数字孪生与多智能体社会模拟的实证应用及验证数据集。主目录要求目标 venue 的正式发表或官方录用证据。",
        "",
        "**排除**：以 LLM 使用、引入或普及为处理变量，研究其对生产率、就业、工资、学习或其他现实结果之因果效应的论文；仅将 causal language modeling 当作因果推断、仅讨论 inference acceleration、以及仅使用 LLM 写代码或润色的论文也不纳入。",
        "",
        "期刊按首次正式在线发表年份归类，另保留卷期年份；会议采用会议年份。Findings、特别轨、综述、名单外期刊与预印本保留在补充列表。",
        "",
        "本仓库是持续整理的证据目录，已补充营销与 simulation 应用。覆盖状态为 partial / search-only，不宣称逐年穷尽；未命中不代表该领域没有相关论文。保存原创中文摘要和来源链接，论文版权属于原作者及出版方。",
        "",
        "## At a Glance",
        "",
        "| Metric | Value |",
        "| --- | ---: |",
        f"| 主目录论文 | {len(papers)} |",
        f"| 正式发表 / 官方已接收稿 | {len(papers)-len(accepted)} / {len(accepted)} |",
        f"| 补充 / 待核验 | {len(supplements)} / {len(pending)} |",
        f"| 目标 venue / 年份单元 | {len(registry['venues'])} / {len(coverage['coverage'])} |",
        f"| 基础检索截止日 | {cutoff} |",
        "",
        "后续定向增补的范围、日期与限制见[来源与核验](docs/sources.md)；不代表其他主题或全部 venue 已同步更新。",
        "",
        "## How to Use",
        "",
        "- [中文研究地图与 8 篇方法优先阅读](docs/research-map.zh.md)",
        "- [营销与 simulation 应用指南](docs/marketing-simulation.md)",
        "- [覆盖与缺口](docs/coverage.md) · [数据字段与口径](docs/metadata.md) · [来源与核验](docs/sources.md)",
        "- [补充文献](docs/supplementary.md) · [待核验候选](docs/pending.md) · [官方已接收稿](docs/accepted.md)",
        "- [CSV](exports/papers.csv) · [BibTeX](exports/references.bib) · [结构化主目录](data/papers.yaml)",
        "",
        "## Browse by Topic",
        ""]
    main += [f"- [{label}](topics/{topic}.md)：{sum(topic in p['topics'] for p in papers)} 篇" for topic, label in TOPICS.items()]
    main += ["", "主题允许交叉，数量不可直接相加。", "", "## Coverage: 2022–2026", "", "| Venue | 2026 | 2025 | 2024 | 2023 | 2022 |", "| --- | ---: | ---: | ---: | ---: | ---: |"]
    for venue in registry["venues"]:
        cells = []
        for year in range(2026, 2021, -1):
            n = len(groups[(year, venue["id"])])
            cells.append(f"[{n}](papers/{year}/{slug(venue['id'])}.md)" if n else "0")
        main.append("| " + venue["id"] + " | " + " | ".join(cells) + " |")
    main += ["", "表格为已核验收录数；所有来源均未宣称穷尽，详细状态见 [coverage.yaml](data/coverage.yaml)。", "", "## Browse by Year and Venue", ""]
    main += [f"- **{year}** · [{venue}](papers/{year}/{slug(venue)}.md) — {len(rows)} 篇" for (year, venue), rows in sorted(groups.items(), reverse=True) if rows]
    main += ["", "## Contributing", "", f"通过 [Suggest a Paper]({REPO}/issues/new?template=paper-suggestion.yml) 提交论文链接与方法相关性说明，由维护者审核。也可修改 `data/*.yaml` 后提交 PR。", "", "```bash", "python3 -m pip install -r requirements-dev.txt", "python3 scripts/render.py", "python3 scripts/validate.py", "python3 scripts/render.py --check", "```", "", "详见 [CONTRIBUTING.md](CONTRIBUTING.md)。", "", "## Paper Index", ""]
    for (year, venue), rows in sorted(groups.items(), reverse=True):
        if rows:
            main += [f"### {venue} {year}", "", table(rows)]
    main += ["## Acknowledgements and License", "", "目录组织参考 [Good Quant AI Papers](https://github.com/sjsj0101/good-quant-ai-papers)。本仓库的原创文献整理与说明采用 [CC BY 4.0](LICENSE)；链接的论文、代码和数据适用各自许可。", ""]
    output["README.md"] = "\n".join(main)
    columns = ["work_id", "title", "authors", "venue", "year", "track", "publication_status", "topics", "summary_zh", "llm_role_zh", "method_zh", "doi", "official_url", "paper_url", "code_url", "limitations_zh"]
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=columns, lineterminator="\n")
    writer.writeheader()
    for p in papers:
        writer.writerow({k: "; ".join(p[k]) if isinstance(p.get(k), list) else p.get(k) for k in columns})
    output["exports/papers.csv"] = "\ufeff" + stream.getvalue()
    output["exports/references.bib"] = bibtex(papers)
    return output

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    check = parser.parse_args().check
    expected = generate()
    changed = []
    for name, text in expected.items():
        path = ROOT / name
        if check:
            if not path.exists() or path.read_bytes() != text.encode():
                changed.append(name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(text.encode())
    stale = [str(p.relative_to(ROOT)) for pattern in ("papers/*/*.md", "topics/*.md") for p in ROOT.glob(pattern) if str(p.relative_to(ROOT)) not in expected]
    if check and (changed or stale):
        raise SystemExit("Generated files out of date: " + ", ".join(changed + stale))
    print(f"{'Checked' if check else 'Rendered'} {len(expected)} generated files.")

if __name__ == "__main__":
    main()
