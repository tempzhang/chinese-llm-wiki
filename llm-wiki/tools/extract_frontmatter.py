#!/usr/bin/env python3
"""extract_frontmatter.py - 提取 Wiki 页面的 frontmatter 元数据。
用法: python extract_frontmatter.py <页面路径>
"""

import os
import re
import sys
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WIKI_DIR = os.path.dirname(SCRIPT_DIR)


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


def main():
    if len(sys.argv) < 2:
        print("用法: python extract_frontmatter.py <页面路径>")
        sys.exit(1)
    fpath = os.path.join(WIKI_DIR, sys.argv[1]) if not os.path.isabs(sys.argv[1]) else sys.argv[1]
    if not os.path.exists(fpath):
        print(f"[错误] 文件不存在: {fpath}")
        sys.exit(1)
    with open(fpath, "r", encoding="utf-8") as f:
        fm = parse_frontmatter(f.read())
    if "--json" in sys.argv:
        print(json.dumps(fm, ensure_ascii=False, indent=2))
    else:
        for key, val in fm.items():
            if isinstance(val, list):
                print(f"{key}: [{', '.join(val)}]")
            else:
                print(f"{key}: {val}")


if __name__ == "__main__":
    main()