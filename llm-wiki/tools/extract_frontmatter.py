#!/usr/bin/env python3
"""extract_frontmatter.py - 提取 Wiki 页面的 frontmatter 元数据。

用法:
    python extract_frontmatter.py                    # 扫描全库，输出 Markdown 表格
    python extract_frontmatter.py --json             # 扫描全库，输出 JSON
    python extract_frontmatter.py <页面路径>         # 解析单个页面
    python extract_frontmatter.py <页面路径> --json  # 解析单个页面，输出 JSON
"""

import os
import re
import sys
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WIKI_DIR = os.path.dirname(SCRIPT_DIR)
WIKI_PAGES = os.path.join(WIKI_DIR, "wiki")


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


def collect_all_pages() -> list[tuple[str, str, dict]]:
    """收集所有 Wiki 页面的 frontmatter。
    返回 [(标题, 相对路径, frontmatter_dict), ...] 列表。
    """
    pages = []
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
                fm = {}
            title = fm.get("title", os.path.splitext(fname)[0])
            if isinstance(title, list):
                title = title[0] if title else os.path.splitext(fname)[0]
            pages.append((title, relpath, fm))
    return pages


def fmt_val(val) -> str:
    """格式化 frontmatter 值为可读字符串。"""
    if isinstance(val, list):
        return ", ".join(str(v) for v in val)
    return str(val)


def output_table(pages: list):
    """以 Markdown 表格格式输出所有页面的 frontmatter。"""
    # 列：页面标题、类型、状态、标签、创建日期、更新日期、路径
    header = ["页面标题", "类型", "状态", "标签", "创建日期", "更新日期", "路径"]
    print("| " + " | ".join(header) + " |")
    print("|" + "|".join("------" for _ in header) + "|")

    type_map = {
        "concept": "概念", "entity": "实体", "project": "项目",
        "workflow": "流程", "question": "问题", "comparison": "对比",
        "report": "报告", "decision": "决策", "example": "示例",
    }
    status_map = {
        "draft": "草稿", "active": "活跃", "outdated": "过时",
        "conflict": "冲突", "archived": "归档",
    }

    for title, relpath, fm in pages:
        ptype = fm.get("type", "—")
        if isinstance(ptype, list):
            ptype = ptype[0] if ptype else "—"
        ptype_cn = type_map.get(ptype, ptype)

        pstatus = fm.get("status", "—")
        if isinstance(pstatus, list):
            pstatus = pstatus[0] if pstatus else "—"
        pstatus_cn = status_map.get(pstatus, pstatus)

        tags = fm.get("tags", [])
        if isinstance(tags, str):
            tags = [tags]
        tags_str = ", ".join(tags) if tags else "—"

        created = fm.get("created", "—")
        updated = fm.get("updated", "—")

        print(f"| {title} | {ptype_cn} | {pstatus_cn} | {tags_str} | {created} | {updated} | {relpath} |")

    print(f"\n共 {len(pages)} 个 Wiki 页面。")


def output_json(pages: list):
    """以 JSON 格式输出所有页面的 frontmatter。"""
    result = []
    for title, relpath, fm in pages:
        result.append({"标题": title, "路径": relpath, "元数据": fm})
    print(json.dumps(result, ensure_ascii=False, indent=2))


def output_single(fpath: str, use_json: bool):
    """输出单个页面的 frontmatter。"""
    if not os.path.exists(fpath):
        print(f"[错误] 文件不存在: {fpath}")
        sys.exit(1)
    with open(fpath, "r", encoding="utf-8") as f:
        fm = parse_frontmatter(f.read())

    if use_json:
        print(json.dumps(fm, ensure_ascii=False, indent=2))
    else:
        print(f"页面: {os.path.basename(fpath)}")
        print("-" * 40)
        for key, val in fm.items():
            if isinstance(val, list):
                print(f"  {key}: [{', '.join(val)}]")
            else:
                print(f"  {key}: {val}")


def main():
    use_json = "--json" in sys.argv

    # 判断是否有非选项参数（页面路径）
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if args:
        # 单文件模式
        fpath = args[0]
        if not os.path.isabs(fpath):
            fpath = os.path.join(WIKI_DIR, fpath)
        output_single(fpath, use_json)
    else:
        # 全库扫描模式
        pages = collect_all_pages()
        if not pages:
            print("未找到 Wiki 页面。")
            return

        if use_json:
            output_json(pages)
        else:
            output_table(pages)


if __name__ == "__main__":
    main()