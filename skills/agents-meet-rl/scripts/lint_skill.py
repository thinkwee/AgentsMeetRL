#!/usr/bin/env python3
"""Lint the agents-meet-rl skill for cross-file consistency.

Run from skills/agents-meet-rl/:
    python3 scripts/lint_skill.py

Exits 0 if no errors, 1 otherwise. Errors are tab-separated for easy
post-processing.
"""
import json
import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(ROOT, ".."))

TEMPLATE_SECTIONS = [
    "## Symptoms",
    "## Root causes",
    "## Diagnosis",
    "## Fixes",
    "## Paper / repo references",
]

TEMPLATE_EXCEPTIONS = {
    "training/grpo-knobs.md", "training/ppo-knobs.md",
    "training/kl-penalty-tuning.md", "training/discount-factor.md",
    "training/token-vs-sequence-loss.md", "training/reward-mixing.md",
    "training/lora-rl.md", "training/algorithm-choice.md",
    "training/sandbox-security.md", "training/mixed-precision.md",
    "training/prm-training.md", "training/rl-from-base.md",
    "training/tool-api-design.md", "training/code-swe-specific.md",
    "training/gui-specific.md", "training/vlm-specific.md",
    "evaluation/benchmark-pitfalls.md", "evaluation/canary-eval.md",
    "evaluation/inference-time-scaling.md",
    "evaluation/llm-judge-evaluation.md",
    "evaluation/long-horizon-eval.md", "evaluation/multi-agent-eval.md",
    "evaluation/ood-evaluation.md", "evaluation/pass-at-k.md",
    "evaluation/reproducibility.md",
    "evaluation/statistical-significance.md",
    "evaluation/train-eval-mismatch.md",
}

PAPER_ONLY_ALGORITHM_WHITELIST = {
    "2503.14476",  # DAPO
    "2503.20783",  # Dr.GRPO
    "2504.05118",  # VAPO
}

CAT_TO_DB = {
    "base-frameworks": "base_framework",
    "general-multitask": "general_multitask",
    "search-rag": "search_rag",
    "web-gui": "web_gui",
    "tool-use": "tool_use",
    "code-swe": "code_swe",
    "reasoning": "reasoning",
    "multi-agent": "multi_agent",
    "memory": "memory",
    "embodied": "embodied",
    "domain-specific": "domain_specific",
    "reward-training": "reward_training",
    "safety": "safety",
    "vlm-agent": "vlm_agent",
    "self-evolution": "self_evolution",
    "environments": "environment",
    "under-review": "under_review",
}


def read(path):
    with open(os.path.join(ROOT, path)) as f:
        return f.read()


def lint():
    errors = []

    # Load db
    db = json.loads(read("database.json"))

    # 1. Five-section template (training/* and evaluation/*)
    for cat in ("training", "evaluation"):
        catdir = os.path.join(ROOT, "problems", cat)
        for fname in sorted(os.listdir(catdir)):
            if not fname.endswith(".md"):
                continue
            rel = f"{cat}/{fname}"
            if rel in TEMPLATE_EXCEPTIONS:
                continue
            txt = read(f"problems/{rel}")
            # Tolerate "## Root cause" (singular)
            sections = list(TEMPLATE_SECTIONS)
            if "## Root causes" not in txt and "## Root cause" in txt:
                sections = [s if s != "## Root causes" else "## Root cause"
                            for s in sections]
            positions = [(s, txt.find(s)) for s in sections]
            missing = [s for s, p in positions if p == -1]
            if missing:
                errors.append(
                    f"FIVE_SEC_MISSING\t{rel}\t" + ",".join(missing))
            present = [(s, p) for s, p in positions if p != -1]
            for i in range(len(present) - 1):
                if present[i][1] > present[i + 1][1]:
                    errors.append(
                        f"FIVE_SEC_ORDER\t{rel}\t"
                        f"{present[i][0]}@{present[i][1]} > "
                        f"{present[i+1][0]}@{present[i+1][1]}")
                    break

    # 2. arxiv URLs must use abs/, not pdf/
    def check_pdf_in(path):
        txt = read(path)
        for m in re.finditer(r"arxiv\.org/(pdf)/(\d{4}\.\d{4,5})", txt):
            errors.append(f"ARXIV_PDF\t{path}\t{m.group(2)}")

    for root, _, files in os.walk(os.path.join(ROOT, "problems")):
        for fname in files:
            if fname.endswith(".md"):
                check_pdf_in(os.path.relpath(
                    os.path.join(root, fname), ROOT))
    for fname in os.listdir(os.path.join(ROOT, "references")):
        if fname.endswith(".md"):
            check_pdf_in(f"references/{fname}")
    # Also scan database.json
    for cat, items in db.items():
        for item in items:
            if not isinstance(item, dict):
                continue
            for p in item.get("papers", []):
                url = p.get("url", "")
                if "/pdf/" in url:
                    errors.append(
                        f"ARXIV_PDF\tdatabase.json\t"
                        f"{item.get('name')}: {url}")

    # 3. db: date matches arxiv ID month
    for cat, items in db.items():
        for item in items:
            if not isinstance(item, dict):
                continue
            date = item.get("date")
            if not date:
                continue
            for p in item.get("papers", []):
                url = p.get("url", "")
                m = re.search(
                    r"arxiv\.org/(?:abs|pdf)/(\d{2})(\d{2})\.", url)
                if not m:
                    continue
                arxiv_yymm = f"20{m.group(1)}.{int(m.group(2))}"
                parts = date.split(".")
                if len(parts) != 2:
                    continue
                d_y, d_m = parts[0], int(parts[1])
                if d_y != "20" + m.group(1) or d_m != int(m.group(2)):
                    errors.append(
                        f"DATE_MISMATCH\t{item.get('name')}\t"
                        f"db_date={date} arxiv={arxiv_yymm}")
                break  # only first paper

    # 4. arxiv IDs in problems/ must be in db (or whitelist)
    known_arxiv = set()
    for cat, items in db.items():
        for item in items:
            if not isinstance(item, dict):
                continue
            for p in item.get("papers", []):
                m = re.search(
                    r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})",
                    p.get("url", ""))
                if m:
                    known_arxiv.add(m.group(1))
            # under_review items embed paper URL in 'url' field
            url = item.get("url", "")
            if url:
                m = re.search(
                    r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})", url)
                if m:
                    known_arxiv.add(m.group(1))

    for root, _, files in os.walk(os.path.join(ROOT, "problems")):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(root, fname), ROOT)
            txt = read(rel)
            for m in re.finditer(
                    r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})", txt):
                arx = m.group(1)
                if arx in known_arxiv:
                    continue
                if arx in PAPER_ONLY_ALGORITHM_WHITELIST:
                    continue
                errors.append(f"ARXIV_NOT_IN_DB\t{rel}\t{arx}")

    # 5. _INDEX.md count matches db and references file
    idx_text = read("references/_INDEX.md")
    for fname, db_key in CAT_TO_DB.items():
        m = re.search(
            rf"\| \[{re.escape(fname)}\.md\]\([^)]+\) \| (\d+) \|",
            idx_text)
        if not m:
            errors.append(f"INDEX_NO_COUNT\t{fname}")
            continue
        idx_count = int(m.group(1))
        db_count = len(db.get(db_key, []))
        rf_text = read(f"references/{fname}.md")
        if fname == "under-review":
            file_count = len(re.findall(
                r"^\| \d+ \|", rf_text, flags=re.M))
        else:
            file_count = len(re.findall(
                r"^### ", rf_text, flags=re.M))
        if not (idx_count == db_count == file_count):
            errors.append(
                f"COUNT_MISMATCH\t{fname}\t"
                f"_INDEX={idx_count} db={db_count} file={file_count}")

    # 6. Same project should have consistent org / date across all
    # problem files. We isolate each reference block by **Name** and
    # only inspect content up to the next blockquote break or next
    # **Name** marker, to avoid attributing fields from neighbouring
    # entries.
    name_to_db_org = {}
    name_to_db_date = {}
    for cat, items in db.items():
        for item in items:
            if not isinstance(item, dict):
                continue
            name = item.get("name")
            if name:
                name_to_db_org[name] = item.get("org")
                name_to_db_date[name] = item.get("date")

    # Match both `Name` and **Name** anchors. Each occurrence is
    # checked; same project appearing multiple times in a file must
    # have consistent date/org at every appearance.
    bold_pat = re.compile(r"`([\w\-\.]+)`|\*\*([\w\-\.]+)\*\*")
    for root, _, files in os.walk(os.path.join(ROOT, "problems")):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(root, fname), ROOT)
            txt = read(rel)
            anchors = list(bold_pat.finditer(txt))
            for i, m in enumerate(anchors):
                name = m.group(1) or m.group(2)
                if name not in name_to_db_org and \
                        name not in name_to_db_date:
                    continue
                start = m.end()
                # block ends at the next anchor or at first blank
                # line outside a blockquote.
                end = anchors[i + 1].start() if i + 1 < len(anchors) \
                    else len(txt)
                blk_end = end
                m2 = re.search(r"\n## |\n\n(?!> )", txt[start:end])
                if m2:
                    blk_end = start + m2.start()
                segment = txt[start:blk_end]

                date_m = re.search(
                    r"date:\s*`?(\d{4}\.\d+)`?", segment)
                if date_m:
                    expected = name_to_db_date.get(name)
                    if expected and expected != date_m.group(1):
                        errors.append(
                            f"PROBLEM_DATE_MISMATCH\t{rel}\t"
                            f"{name}: file={date_m.group(1)} "
                            f"db={expected}")

                # Only check explicit `org: <X>,` form. Implicit
                # forms like "..., UIUC, date: 2025.3" are NOT
                # checked: this skill is a problem-solving handbook,
                # not a survey, so author choices like "UIUC" vs
                # "UIUC/Google" or "ByteDance Seed" vs "ByteDance"
                # don't affect the quality of the recommendation.
                org_m = re.search(
                    r"org:\s*([^\n,\.]+?)(?=\s*[,\.])", segment)
                if org_m:
                    expected = name_to_db_org.get(name)
                    actual = org_m.group(1).strip()
                    if expected and expected != actual:
                        errors.append(
                            f"PROBLEM_ORG_MISMATCH\t{rel}\t"
                            f"{name}: file={actual} db={expected}")

    return errors


def main():
    errs = lint()
    by_kind = defaultdict(int)
    for e in errs:
        by_kind[e.split("\t", 1)[0]] += 1
        print(e)
    print(f"\n--- TOTAL: {len(errs)} errors ---", file=sys.stderr)
    for k, v in sorted(by_kind.items()):
        print(f"  {k}: {v}", file=sys.stderr)
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
