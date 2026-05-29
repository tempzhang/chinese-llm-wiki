#!/usr/bin/env python3
"""wiki_lint.py - 中文 LLM Wiki 健康检查工具。

检查项:
    - 孤立页面（未被任何其他页面引用）
    - 断链（引用了不存在的页面）
    - 缺少 frontmatter 的页面
    - 缺少 sources 的页面
    - 过期页面（status 为 outdated）
    - 缺少 required frontmatter 字段的页面

用法:
    python wiki_lint.py
    python wiki_lint.py --verbose
"""

import os
import sys
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WIKI_DIR = os.path.dirname(SCRIPT_DIR)
WIKI_PAGES = os.path.join(WIKI_DIR, "wiki")

REQUIRED_FIELDS = ["title", "type", "status", "created", "updated"]
VALID_TYPES = {"concept", "entity", "project", "workflow", "question", "comparison", "report", "decision", "example"}
VALID_STATUSES = {"draft", "active", "outdated", "conflict", "archived"}


def parse_frontmatter(content: str) -> dict:
    """解析 YAML frontmatter，支持 BOM、多行列表值和 Windows 换行。"""
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


def collect_pages() -> dict[str, dict]:
    pages = {}
    for root, _, files in os.walk(WIKI_PAGES):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(root, fname)
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception:
                continue
            fm = parse_frontmatter(content)
            title = fm.get("title", os.path.splitext(fname)[0])
            if isinstance(title, list):
                title = title[0] if title else os.path.splitext(fname)[0]
            pages[title] = {
                "path": os.path.relpath(fpath, WIKI_DIR),
                "frontmatter": fm,
                "content": content,
            }
    return pages


def extract_links(content: str) -> set[str]:
    """从页面内容中提取 [[...]] 链接，跳过代码块和 fenced code 中的。"""
    # 去掉 fenced code blocks (``` ... ```)
    cleaned = re.sub(r"```.*?```", "", content, flags=re.DOTALL)
    # 去掉 inline code (`...`)
    cleaned = re.sub(r"`[^`]+`", "", cleaned)
    return set(re.findall(r"\[\[([^\]]+)\]\]", cleaned))


def check_missing_frontmatter(pages: dict, verbose: bool) -> list[str]:
    issues = []
    for title, info in pages.items():
        fm = info["frontmatter"]
        if not fm:
            issues.append(f"{info['path']} - 缺少 frontmatter")
            continue
        for field in REQUIRED_FIELDS:
            if field not in fm:
                issues.append(f"{info['path']} - 缺少必需字段: {field}")
        ftype = fm.get("type")
        if isinstance(ftype, list):
            ftype = ftype[0]
        if ftype and ftype not in VALID_TYPES:
            issues.append(f"{info['path']} - 无效 type: {ftype}")
        fstatus = fm.get("status")
        if isinstance(fstatus, list):
            fstatus = fstatus[0]
        if fstatus and fstatus not in VALID_STATUSES:
            issues.append(f"{info['path']} - 无效 status: {fstatus}")
    return issues


def check_orphan_pages(pages: dict, verbose: bool) -> list[str]:
    all_titles = set(pages.keys())
    referenced = set()
    for title, info in pages.items():
        links = extract_links(info["content"])
        referenced.update(links)
    index_path = os.path.join(WIKI_DIR, "index.md")
    if os.path.exists(index_path):
        try:
            with open(index_path, "r", encoding="utf-8") as f:
                index_links = extract_links(f.read())
                referenced.update(index_links)
        except Exception:
            pass
    orphaned = all_titles - referenced - {"00-总览"}
    return [f"{pages[t]['path']} - 孤立页面" for t in sorted(orphaned)]


def check_broken_links(pages: dict, verbose: bool) -> list[str]:
    all_titles = set(pages.keys())
    issues = []
    for title, info in pages.items():
        links = extract_links(info["content"])
        for link in links:
            if link not in all_titles:
                issues.append(f"{info['path']} - 断链: [[{link}]]")
    return issues


def check_missing_sources(pages: dict, verbose: bool) -> list[str]:
    issues = []
    for title, info in pages.items():
        if "sources" not in info["frontmatter"]:
            issues.append(f"{info['path']} - 缺少 sources 字段")
    return issues


def check_outdated(pages: dict, verbose: bool) -> list[str]:
    result = []
    for title, info in pages.items():
        fstatus = info["frontmatter"].get("status")
        if isinstance(fstatus, list):
            fstatus = fstatus[0]
        if fstatus == "outdated":
            result.append(f"{info['path']} - 状态为 outdated")
    return result


def main():
    verbose = "--verbose" in sys.argv
    pages = collect_pages()

    if not pages:
        print("未找到 Wiki 页面。")
        return

    print(f"检查 {len(pages)} 个 Wiki 页面...\n")

    checks = [
        ("缺少 frontmatter / 无效字段", check_missing_frontmatter),
        ("孤立页面（无引用）", check_orphan_pages),
        ("断链（引用不存在页面）", check_broken_links),
        ("缺少 sources 字段", check_missing_sources),
        ("过期页面 (outdated)", check_outdated),
    ]

    total_issues = 0
    for name, checker in checks:
        issues = checker(pages, verbose)
        count = len(issues)
        total_issues += count
        icon = "OK" if count == 0 else "!!"
        print(f"[{icon}] {name}: {count}")
        if verbose and issues:
            for issue in issues:
                print(f"    - {issue}")

    print(f"\n总计: {total_issues} 个问题。")
    if total_issues > 0 and not verbose:
        print("使用 --verbose 查看详情。")


if __name__ == "__main__":
    main()