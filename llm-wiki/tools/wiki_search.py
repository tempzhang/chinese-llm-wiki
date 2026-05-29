#!/usr/bin/env python3
"""wiki_search.py - 在中文 LLM Wiki 中搜索关键词。

用法:
    python wiki_search.py <关键词>
    python wiki_search.py "知识编译"

输出匹配的文件路径和上下文片段。
"""

import os
import sys
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WIKI_DIR = os.path.dirname(SCRIPT_DIR)
WIKI_PAGES = os.path.join(WIKI_DIR, "wiki")


def search(query: str) -> list[tuple[str, int, str]]:
    """搜索包含关键词的 Wiki 页面，返回 (文件路径, 行号, 行内容) 列表。"""
    results = []
    for root, _, files in os.walk(WIKI_PAGES):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(root, fname)
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    for i, line in enumerate(f, 1):
                        if query.lower() in line.lower():
                            relpath = os.path.relpath(fpath, WIKI_DIR)
                            results.append((relpath, i, line.strip()))
            except Exception as e:
                print(f"[警告] 无法读取 {fpath}: {e}", file=sys.stderr)
    return results


def main():
    if len(sys.argv) < 2:
        print("用法: python wiki_search.py <关键词>")
        sys.exit(1)

    query = sys.argv[1]
    results = search(query)

    if not results:
        print(f"未找到与「{query}」相关的内容。")
        return

    print(f"搜索「{query}」找到 {len(results)} 条结果:\n")
    current_file = None
    for fpath, lineno, line in results:
        if fpath != current_file:
            print(f"\n--- {fpath} ---")
            current_file = fpath
        print(f"  {lineno}: {line}")


if __name__ == "__main__":
    main()