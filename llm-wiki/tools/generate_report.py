#!/usr/bin/env python3
"""generate_report.py - 生成 Wiki 健康检查或统计报告。

用法:
    python generate_report.py --title "报告标题"
    python generate_report.py --stats  # 输出统计摘要
"""

import os
import re
import sys
from datetime import datetime
from collections import Counter

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WIKI_DIR = os.path.dirname(SCRIPT_DIR)
WIKI_PAGES = os.path.join(WIKI_DIR, "wiki")
REPORTS_DIR = os.path.join(WIKI_PAGES, "reports")


def parse_frontmatter(content: str) -> dict:
    content = content.lstrip("\ufeff")
    fm_match = re.match(r"^---\s*\r?\n(.*?)\r?\n---", content, re.DOTALL)
    if not fm_match:
        return {}
    fm = {}
    current_key = None
    current_list = []
    for line in fm_match.group(1).split("\n"):
        line = line.rstrip("\r")
        m_list = re.match(r"^\s+-\s+(.*)", line)
        if m_list and current_key:
            val = m_list.group(1).strip().strip('"').strip("'")
            current_list.append(val)
            continue
        m = re.match(r"^(\w[\w_-]*):\s*(.*)", line)
        if m:
            if current_key and current_list:
                fm[current_key] = current_list
                current_list = []
            key = m.group(1)
            val = m.group(2).strip().strip('"').strip("'")
            if val.startswith("[") and val.endswith("]"):
                inner = val[1:-1].strip()
                val_list = [x.strip().strip('"').strip("'") for x in inner.split(",") if x.strip()]
                fm[key] = val_list
                current_key = None
                continue
            if val:
                fm[key] = val
                current_key = None
            else:
                current_key = key
                current_list = []
        elif not line.strip() and current_key and current_list:
            fm[current_key] = current_list
            current_key = None
            current_list = []
    if current_key and current_list:
        fm[current_key] = current_list
    return fm


def collect_stats() -> dict:
    stats = {"total": 0, "by_type": Counter(), "by_status": Counter()}
    for root, _, files in os.walk(WIKI_PAGES):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(root, fname)
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    fm = parse_frontmatter(f.read())
            except Exception:
                continue
            stats["total"] += 1
            ptype = fm.get("type", "unknown")
            if isinstance(ptype, list):
                ptype = ptype[0]
            stats["by_type"][ptype] += 1
            pstatus = fm.get("status", "unknown")
            if isinstance(pstatus, list):
                pstatus = pstatus[0]
            stats["by_status"][pstatus] += 1
    return stats


def main():
    if "--stats" in sys.argv:
        stats = collect_stats()
        print(f"Wiki 页面总数: {stats['total']}")
        print("\n按类型分布:")
        for t, count in stats["by_type"].most_common():
            print(f"  {t}: {count}")
        print("\n按状态分布:")
        for s, count in stats["by_status"].most_common():
            print(f"  {s}: {count}")
        return

    if "--help" in sys.argv or len(sys.argv) < 2:
        print("用法:")
        print("  python generate_report.py --stats          # 输出统计摘要")
        print("  python generate_report.py --title <标题>    # 生成报告模板")
        sys.exit(0)

    title = None
    if "--title" in sys.argv:
        idx = sys.argv.index("--title")
        if idx + 1 < len(sys.argv):
            title = sys.argv[idx + 1]

    if not title:
        title = f"报告-{datetime.now().strftime('%Y%m%d-%H%M')}"

    today = datetime.now().strftime("%Y-%m-%d")
    report_content = f'''---
title: "{title}"
type: "report"
status: "draft"
tags: []
created: "{today}"
updated: "{today}"
sources: []
related: []
---

# {title}

## 报告摘要

## 统计数据

## 分析

## 结论与建议

## 相关页面
'''

    os.makedirs(REPORTS_DIR, exist_ok=True)
    fname = f"{title}.md"
    fpath = os.path.join(REPORTS_DIR, fname)

    if os.path.exists(fpath):
        print(f"[错误] 报告已存在: {fpath}")
        sys.exit(1)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(report_content)

    print(f"报告模板已生成: {os.path.relpath(fpath, WIKI_DIR)}")


if __name__ == "__main__":
    main()