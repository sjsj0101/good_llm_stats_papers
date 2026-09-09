import re
import unicodedata


TOPICS = {
    "stats-inference": "LLM 辅助统计推断",
    "statistical-theory": "统计学习理论与上下文学习",
    "uncertainty": "不确定性、校准与统计评测",
    "causal-discovery": "因果发现与识别",
    "causal-estimation": "因果估计与推断",
    "causal-reasoning": "因果推理能力与评测",
    "causal-llm-analysis": "LLM 的因果与概率分析",
    "synthetic-data": "合成数据与调查有效性",
}

def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", unicodedata.normalize("NFKD", value).casefold()).strip("-")

def table(rows: list[dict]) -> str:
    lines = ["| 年份 / Venue | 论文 | 方法与 LLM 的关系 |", "| --- | --- | --- |"]
    for r in rows:
        title = r["title"].replace("|", "\\|")
        link = r.get("official_url") or r.get("paper_url")
        label = f"[{title}]({link})" if link else title
        summary = (r.get("summary_zh") or r.get("decision_reason_zh") or "").replace("|", "\\|").replace("\n", " ")
        status_label = " · 已接收稿" if r.get("publication_status") == "accepted" else ""
        lines.append(f"| {r.get('year') or '未定'} · {r['venue']}{status_label} | {label} | {summary} |")
    return "\n".join(lines) + "\n"

def bibtex(rows: list[dict]) -> str:
    output = []
    for r in rows:
        def clean(value):
            return str(value).replace("\\", "\\textbackslash{}").replace("%", "\\%").replace("&", "\\&").replace("_", "\\_")
        entry = "inproceedings" if r["venue_group"] == "cs-conference" else "article"
        fields = {"title": "{" + r["title"] + "}", "author": " and ".join(r.get("authors") or []), "year": r["year"]}
        fields["booktitle" if entry == "inproceedings" else "journal"] = r["venue"]
        fields["url"] = r["official_url"]
        if r.get("doi"):
            fields["doi"] = r["doi"]
        output.append("@" + entry + "{" + r["work_id"] + ",\n" + ",\n".join("  " + k + " = {" + (str(v) if k in {"url", "doi"} else clean(v)) + "}" for k, v in fields.items()) + "\n}\n")
    return "\n".join(output)
