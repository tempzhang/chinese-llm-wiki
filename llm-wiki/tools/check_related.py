#!/usr/bin/env python3
"""检查 Wiki 页面 related 字段双向一致性。"""

import os
import re

WIKI_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "wiki")


def collect_pages():
    pages = {}
    for root, _, files in os.walk(WIKI_DIR):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(root, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()

            title = None
            related = []
            in_related = False
            for line in content.split("\n"):
                m_title = re.match(r'^title:\s*"(.+)"', line)
                if m_title:
                    title = m_title.group(1)
                    continue
                m_title2 = re.match(r"^title:\s*(.+)", line)
                if m_title2 and not title:
                    title = m_title2.group(1).strip().strip('"')
                    continue
                if re.match(r"^related:", line):
                    in_related = True
                    continue
                if in_related:
                    m_rel = re.match(r'^\s+-\s+"?(.+?)"?\s*$', line)
                    if m_rel:
                        related.append(m_rel.group(1).strip().strip('"'))
                    elif re.match(r"^\w", line):
                        in_related = False

            if not title:
                title = os.path.splitext(fname)[0]

            relpath = os.path.relpath(fpath, WIKI_DIR)
            pages[title] = {"path": relpath, "related": related}
    return pages


def main():
    pages = collect_pages()
    issues = []

    for title, info in pages.items():
        for ref in info["related"]:
            if ref not in pages:
                issues.append(
                    f'{info["path"]} -> related 指向不存在的页面 "{ref}"'
                )
                continue
            if title not in pages[ref]["related"]:
                issues.append(
                    f'{info["path"]} -> "{ref}" 的 related 列表中缺少 "{title}"（单向链接）'
                )

    if issues:
        print(f"发现 {len(issues)} 个问题：\n")
        for i in issues:
            print(f"  - {i}")
        return 1
    else:
        print(f"全部 {len(pages)} 个页面的 related 字段双向一致！")
        return 0


if __name__ == "__main__":
    exit(main())
