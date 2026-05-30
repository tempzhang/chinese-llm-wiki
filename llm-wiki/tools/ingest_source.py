#!/usr/bin/env python3
"""ingest_source.py - 资料摄取辅助工具。

将原始资料文件复制到 raw/ 对应目录，并生成摄取提示。

用法:
    python ingest_source.py <源文件路径> --type <类型>
    python ingest_source.py article.md --type article

支持类型:
    article    → raw/sources/
    video      → raw/videos/
    pdf        → raw/pdfs/
    image      → raw/images/
    transcript → raw/transcripts/
    webclip    → raw/web-clips/

选项:
    --type <类型>   资料类型（必填）
    --dry-run       仅预览，不实际复制
    --preview       显示文件内容预览（默认：文件<5KB时自动显示）
    --help          显示此帮助信息
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


def print_help():
    print(__doc__)
    sys.exit(0)


def print_header(msg):
    print(f"\n{'=' * 50}")
    print(f"  {msg}")
    print(f"{'=' * 50}")


def main():
    # 解析参数
    src = None
    src_type = None
    dry_run = False
    force_preview = False

    args = sys.argv[1:]
    skip_next = False
    for i, arg in enumerate(args):
        if skip_next:
            skip_next = False
            continue
        if arg in ("--help", "-h"):
            print_help()
        elif arg == "--type":
            if i + 1 < len(args):
                src_type = args[i + 1]
                skip_next = True
            else:
                print("[错误] --type 缺少参数")
                sys.exit(1)
        elif arg == "--dry-run":
            dry_run = True
        elif arg == "--preview":
            force_preview = True
        elif not arg.startswith("--"):
            src = arg

    if not src or not src_type:
        print("错误：必须指定源文件路径和 --type。")
        print("用法: python ingest_source.py <源文件路径> --type <类型>")
        print(f"支持类型: {', '.join(TYPE_DIRS.keys())}")
        sys.exit(1)

    if src_type not in TYPE_DIRS:
        print(f"[错误] 无效类型: '{src_type}'")
        print(f"支持类型: {', '.join(TYPE_DIRS.keys())}")
        sys.exit(1)

    if not os.path.exists(src):
        print(f"[错误] 源文件不存在: {src}")
        sys.exit(1)

    # 读取源文件内容
    content = ""
    is_readable = False
    try:
        with open(src, "r", encoding="utf-8") as f:
            content = f.read()
        is_readable = True
    except Exception:
        pass

    dest_dir = os.path.join(RAW_DIR, TYPE_DIRS[src_type])
    dest = os.path.join(dest_dir, os.path.basename(src))

    print_header("资料摄取概览")
    print(f"  来源: {os.path.abspath(src)}")
    print(f"  类型: {src_type}")
    print(f"  目标: {dest}")
    print(f"  大小: {os.path.getsize(src)} bytes")
    if is_readable:
        print(f"  行数: {content.count(chr(10)) + 1}")
    print()

    # 检查目标是否存在
    if os.path.exists(dest):
        print(f"[警告] 目标文件已存在: {os.path.relpath(dest, RAW_DIR)}")
        print("  可选择：删除旧文件后重试，或手动处理。")
        sys.exit(1)

    if dry_run:
        print("[DRY RUN] 未执行复制。使用 --dry-run 时仅显示预览。")
    else:
        os.makedirs(dest_dir, exist_ok=True)
        shutil.copy2(src, dest)
        print(f"[完成] 已复制到: {os.path.relpath(dest, WIKI_DIR)}")

    # 文件内容预览
    show_preview = force_preview or (is_readable and len(content) < 5000)
    if show_preview and content:
        preview_len = 2000
        print_header("文件内容预览")
        print(content[:preview_len])
        if len(content) > preview_len:
            print(f"\n... (共 {len(content)} 字符，仅显示前 {preview_len} 字符)")

    # 输出摄取提示
    print_header("AI Agent 摄取提示")
    relpath = os.path.relpath(dest if not dry_run else src, WIKI_DIR)
    print(f"请阅读并消化 `{relpath}`，按照 llm-wiki/AGENTS.md 的摄取规则")
    print(f"生成或更新 Wiki 页面，然后运行 `python tools/wiki_lint.py`")
    print(f"检查健康状态，最后更新 index.md 和 log.md。")
    print()


if __name__ == "__main__":
    main()