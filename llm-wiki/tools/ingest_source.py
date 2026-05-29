#!/usr/bin/env python3
"""ingest_source.py - 资料摄取辅助工具。

将原始资料文件复制到 raw/ 对应目录，并生成摄取提示。

用法:
    python ingest_source.py <源文件路径> --type <article|video|pdf|image|transcript>
    python ingest_source.py article.md --type article
"""

import os
import sys
import shutil
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WIKI_DIR = os.path.dirname(SCRIPT_DIR)
RAW_DIR = os.path.join(WIKI_DIR, "raw")

TYPE_DIRS = {
    "article": "sources",
    "video": "videos",
    "pdf": "pdfs",
    "image": "images",
    "transcript": "transcripts",
    "webclip": "web-clips",
}


def main():
    if len(sys.argv) < 2 or "--help" in sys.argv:
        print("用法: python ingest_source.py <源文件路径> --type <类型>")
        print(f"支持类型: {', '.join(TYPE_DIRS.keys())}")
        sys.exit(0)

    src = sys.argv[1]
    src_type = None
    if "--type" in sys.argv:
        idx = sys.argv.index("--type")
        if idx + 1 < len(sys.argv):
            src_type = sys.argv[idx + 1]

    if src_type not in TYPE_DIRS:
        print(f"[错误] 无效类型: {src_type}")
        print(f"支持类型: {', '.join(TYPE_DIRS.keys())}")
        sys.exit(1)

    if not os.path.exists(src):
        print(f"[错误] 源文件不存在: {src}")
        sys.exit(1)

    # 读取源文件内容（如果是文本文件）
    try:
        with open(src, "r", encoding="utf-8") as f:
            content = f.read()
        is_readable = True
    except Exception:
        content = ""
        is_readable = False

    dest_dir = os.path.join(RAW_DIR, TYPE_DIRS[src_type])
    os.makedirs(dest_dir, exist_ok=True)

    dest = os.path.join(dest_dir, os.path.basename(src))
    if os.path.exists(dest):
        print(f"[警告] 目标已存在: {dest}")
        print("请手动处理或删除已有文件后重试。")
        sys.exit(1)

    shutil.copy2(src, dest)
    print(f"✅ 已复制到: {dest}")

    # 输出摄取提示
    print("\n--- 请使用以下提示让 AI Agent 摄取此资料 ---")
    print()
    fname = os.path.basename(src)
    print(f"请阅读并消化 {os.path.relpath(dest, WIKI_DIR)}，按照摄取规则生成或更新 Wiki 页面。")
    print()

    if is_readable and len(content) < 5000:
        print("--- 文件内容预览（前 2000 字符）---")
        print(content[:2000])
        if len(content) > 2000:
            print("\n... (内容已截断)")


if __name__ == "__main__":
    main()