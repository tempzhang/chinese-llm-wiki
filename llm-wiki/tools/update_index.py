#!/usr/bin/env python3
"""update_index.py - 自动更新 llm-wiki/index.md 的自动索引区域。
只更新 <!-- AUTO_INDEX_START --> 和 <!-- AUTO_INDEX_END --> 之间的内容。
用法: python update_index.py
"""

import os
import re
import sys
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WIKI_DIR = os.path.dirname(SCRIPT_DIR)
WIKI_PAGES = os.path.join(WIKI_DIR, "wiki")
INDEX_PATH = os.path.join(WIKI_DIR, "index.md")

PAGE_TYPES = {
    "concept": "核心概念",
    "entity": "实体",
    "project": "项目",
    "workflow": "工作流",
    "question": "问题",
    "comparison": "对比分析",
    "report": "报告",
    "decision": "决策记录",
    "example": "示例",
}


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


def collect_typed_pages() -> dict[str, list[tuple[str, str]]]:
    typed = {}
    for root, _, files in os.walk(WIKI_PAGES):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(root, fname)
            relpath = os.path.relpath(fpath, WIKI_DIR)
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    fm = parse_frontmatter(f.read())
            except Exception:
                continue
            page_type = fm.get("type", "unknown")
            if isinstance(page_type, list):
                page_type = page_type[0]
            title = fm.get("title", os.path.splitext(fname)[0])
            if isinstance(title, list):
                title = title[0]
            typed.setdefault(page_type, []).append((title, relpath))
    return typed


def main():
    if not os.path.exists(INDEX_PATH):
        print(f"[错误] 未找到 index.md: {INDEX_PATH}")
        sys.exit(1)
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        original = f.read()
    typed = collect_typed_pages()
    lines = [f"<!-- 自动生成于 {datetime.now().strftime('%Y-%m-%d %H:%M')} -->", ""]
    for ptype, label in PAGE_TYPES.items():
        pages = typed.get(ptype, [])
        if not pages:
            continue
        lines.append(f"### {label}")
        lines.append("")
        for title, relpath in sorted(pages):
            escaped_title = title.replace("\\", "\\\\")
            lines.append(f"- [{escaped_title}]({relpath})")
        lines.append("")
    auto_section = "\n".join(lines)
    auto_block = "<!-- AUTO_INDEX_START -->\n" + auto_section + "\n<!-- AUTO_INDEX_END -->"

    # 用字符串方法替代复杂正则
    start_marker = "<!-- AUTO_INDEX_START -->"
    end_marker = "<!-- AUTO_INDEX_END -->"
    start_idx = original.find(start_marker)
    end_idx = original.find(end_marker)
    if start_idx != -1 and end_idx != -1:
        new_content = original[:start_idx] + auto_block + original[end_idx + len(end_marker):]
    else:
        new_content = original + "\n\n" + auto_block

    if new_content != original:
        with open(INDEX_PATH, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("index.md 自动索引区域已更新。")
    else:
        print("index.md 自动索引区域未变化。")


if __name__ == "__main__":
    main()