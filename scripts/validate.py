"""Validate bibliographic scope, coverage, and public artifact integrity."""
import collections
import csv
import json
from pathlib import Path
import re
from urllib.parse import urlparse
import yaml
from common import TOPICS

ROOT = Path(__file__).resolve().parents[1]

def main():
    papers = yaml.safe_load((ROOT / "data/papers.yaml").read_text())
    registry = yaml.safe_load((ROOT / "data/venues.yaml").read_text())["venues"]
    coverage = yaml.safe_load((ROOT / "data/coverage.yaml").read_text())["coverage"]
    allowed = {v["id"] for v in registry}
    errors = []
    ids = set()
    for paper in papers:
        for field in ["work_id", "title", "authors", "venue", "year", "official_url", "summary_zh", "llm_role_zh", "method_zh", "topics", "decision_reason_zh", "evidence_locator"]:
            if not paper.get(field):
                errors.append(f"Missing {field}: {paper.get('title')}")
        if paper.get("work_id") in ids:
            errors.append("Duplicate work_id: " + paper["work_id"])
        ids.add(paper.get("work_id"))
        if paper.get("venue") not in allowed or paper.get("year") not in range(2022, 2027):
            errors.append("Venue/year outside scope: " + paper["title"])
        if paper.get("scope_decision") != "include" or paper.get("publication_status") not in {"published", "accepted"}:
            errors.append("Main record lacks an eligible publication status: " + paper["title"])
        if paper.get("track") in {"workshop", "findings", "position", "demo", "special-ai-for-social-impact"}:
            errors.append("Supplemental track in main: " + paper["title"])
        if not set(paper.get("topics", [])) <= set(TOPICS):
            errors.append("Unknown topic: " + paper["title"])
        if urlparse(paper.get("official_url", "")).scheme not in {"https", "http"}:
            errors.append("Invalid official URL: " + paper["title"])
    for field in ["doi", "arxiv_id", "openreview_id"]:
        seen = collections.Counter(str(p[field]).casefold() for p in papers if p.get(field))
        errors += [f"Duplicate {field}: {value}" for value, n in seen.items() if n > 1]
    expected = {(v["id"], year) for v in registry for year in v["years"]}
    if len(coverage) != len(expected) or {(r["venue"], r["year"]) for r in coverage} != expected:
        errors.append("Coverage units do not match venue registry")
    counts = collections.Counter((p["venue"], p["year"]) for p in papers)
    for row in coverage:
        if row["included_count"] != counts[(row["venue"], row["year"])]:
            errors.append(f"Coverage count mismatch: {row['venue']} {row['year']}")
    csv_rows = list(csv.DictReader((ROOT / "exports/papers.csv").open(encoding="utf-8-sig")))
    if len(csv_rows) != len(papers) or {r["work_id"] for r in csv_rows} != ids:
        errors.append("CSV and YAML records differ")
    bib = (ROOT / "exports/references.bib").read_text()
    if set(re.findall(r"^@\w+\{([^,]+),", bib, re.M)) != ids:
        errors.append("BibTeX and YAML records differ")
    links = 0
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(x.startswith(".") for x in path.relative_to(ROOT).parts) or "__pycache__" in path.parts:
            continue
        if path.suffix in {".yaml", ".jsonl", ".md", ".csv", ".bib"}:
            text = path.read_text()
            if re.search(r"/(?:Users|home)/[A-Za-z0-9]", text):
                errors.append("Private machine path in public artifact: " + str(path.relative_to(ROOT)))
            if path.suffix == ".md":
                for target in re.findall(r"\]\(([^)]+)\)", text):
                    if "://" in target or target.startswith("#"):
                        continue
                    links += 1
                    if not (path.parent / target.split("#")[0]).exists():
                        errors.append(f"Broken link in {path.name}: {target}")
    print(json.dumps({"papers": len(papers), "coverage_units": len(coverage), "relative_links": links, "errors": errors}, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
