#!/usr/bin/env python3
"""书签转 Obsidian Vault - 完整转换脚本"""
import html.parser
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from urllib.parse import urlparse

# ─── 配置 ───
BOOKMARKS_FILE = r"D:\文本文档\bookmarks_2026_5_29.html"
VAULT_ROOT = r"D:\chinese-llm-wiki\Bookmarks-Vault"
CATEGORIES = [
    ("00_Dashboard", "仪表盘"),
    ("01_AI", "AI"),
    ("02_Agents", "Agents"),
    ("03_MCP", "MCP"),
    ("04_DeepSeek", "DeepSeek"),
    ("05_Hermes", "Hermes"),
    ("06_OpenClaw", "OpenClaw"),
    ("07_WordPress", "WordPress"),
    ("08_WooCommerce", "WooCommerce"),
    ("09_CloudPanel", "CloudPanel"),
    ("10_SEO", "SEO"),
    ("11_CrossBorder", "跨境电商"),
    ("12_TikTok", "TikTok"),
    ("13_Amazon", "Amazon"),
    ("14_Payment", "支付"),
    ("15_Network", "网络"),
    ("16_OpenWRT", "OpenWRT"),
    ("17_NAS", "NAS"),
    ("18_Docker", "Docker"),
    ("19_GitHub", "GitHub"),
    ("20_Programming", "编程"),
    ("21_VideoLearning", "视频学习"),
    ("22_Tools", "工具"),
    ("90_Reports", "报告"),
    ("99_Archive", "归档"),
]

# 分类关键词映射
CATEGORY_KEYWORDS = {
    "01_AI": ["ai", "chatgpt", "gpt", "claude", "gemini", "grok", "copilot", "llm", 
              "语言模型", "aigc", "openai", "perplexity", "poe", "cursor", "codex",
              "deepseek", "qwen", "通义", "文心", "kimi", "豆包", "midjourney", "dalle",
              "sora", "openrouter", "硅基流动", "siliconflow", "anthropic"],
    "02_Agents": ["agent", "agents", "自动化", "workflow", "工作流", "n8n", "make.com",
                  "zapier", "dify", "coze", "crewai", "autogpt", "langchain", "langgraph"],
    "03_MCP": ["mcp", "model context protocol", "function calling", "tool use"],
    "04_DeepSeek": ["deepseek", "deep seek"],
    "05_Hermes": ["hermes"],
    "06_OpenClaw": ["openclaw", "open claw"],
    "07_WordPress": ["wordpress", "wp", "elementor", "woocommerce"],
    "08_WooCommerce": ["woocommerce", "woo commerce"],
    "09_CloudPanel": ["cloudpanel", "cloud panel"],
    "10_SEO": ["seo", "sem", "google search", "搜索引擎", "关键词", "排名",
               "ahrefs", "semrush", "serp", "backlink", "搜索控制台", "search console",
               "buzzsumo", "majestic"],
    "11_CrossBorder": ["跨境", "cross border", "mercury", "paypal", "stripe", "payoneer",
                       "wise", "万里汇", "连连", "pingpong", "空中云汇", "shopify",
                       "独立站", "外贸", "b2b", "货代", "物流", "fba", "海外仓",
                       "etsy", "ebay", "美客多", "lazada", "shopee"],
    "12_TikTok": ["tiktok", "抖音", "tiktok shop", "tk", "tiktok ads"],
    "13_Amazon": ["amazon", "亚马逊", "fba", "fbm"],
    "14_Payment": ["支付", "收款", "stripe", "paypal", "mercury", "payoneer", "wise",
                   "万里汇", "pingpong", "transferwise"],
    "15_Network": ["网络", "vpn", "代理", "proxy", "ip", "dns", "软路由", "vps",
                   "v2ray", "trojan", "ssr", "clash", "机场", "科学上网", "翻墙",
                   "wireguard", "tailscale", "zerotier"],
    "16_OpenWRT": ["openwrt", "openwrt", "lede", "immortalwrt", "istoreos",
                   "软路由", "n60pro", "路由"],
    "17_NAS": ["nas", "飞牛", "群晖", "synology", "unraid", "truenas", "omv",
               "alist", "emby", "jellyfin", "plex", "网盘", "存储", "cloudsaver",
               "smartstrm", "tvbox", "小雅"],
    "18_Docker": ["docker", "容器", "container", "portainer", "docker compose"],
    "19_GitHub": ["github", "gitlab", "git"],
    "20_Programming": ["编程", "programming", "python", "javascript", "php", "java",
                       "rust", "go", "typescript", "html", "css", "react", "vue",
                       "node", "api", "sql", "数据库", "后端", "前端", "fullstack",
                       "pbootcms", "帝国cms", "opencart", "shopify", "建站", "网站建设",
                       "域名", "服务器", "宝塔", "nginx", "apache"],
    "21_VideoLearning": ["youtube", "bilibili", "教程", "tutorial", "课程", "学习",
                         "视频", "在线课程", "udemy", "coursera", "高考", "初中"],
    "22_Tools": ["工具", "tool", "生成器", "generator", "转换", "convert",
                 "导航", "插件", "extension", "notion", "日历", "邮箱", "mail",
                 "图床", "cdn", "云服务", "短信", "接码", "临时邮箱"],
}

# 关键词 -> 标签映射
TAG_MAP = {
    "01_AI": ["AI", "LLM"],
    "02_Agents": ["Agent", "自动化"],
    "03_MCP": ["MCP", "协议"],
    "04_DeepSeek": ["DeepSeek", "国产AI"],
    "05_Hermes": ["Hermes", "Agent"],
    "06_OpenClaw": ["OpenClaw", "Agent"],
    "07_WordPress": ["WordPress", "建站"],
    "08_WooCommerce": ["WooCommerce", "电商"],
    "09_CloudPanel": ["CloudPanel", "服务器"],
    "10_SEO": ["SEO", "营销"],
    "11_CrossBorder": ["跨境电商", "独立站"],
    "12_TikTok": ["TikTok", "短视频"],
    "13_Amazon": ["Amazon", "电商"],
    "14_Payment": ["支付", "金融"],
    "15_Network": ["网络", "代理"],
    "16_OpenWRT": ["OpenWRT", "路由器"],
    "17_NAS": ["NAS", "存储"],
    "18_Docker": ["Docker", "容器"],
    "19_GitHub": ["GitHub", "开源"],
    "20_Programming": ["编程", "开发"],
    "21_VideoLearning": ["视频", "学习"],
    "22_Tools": ["工具", "效率"],
}

# ─── 解析 ───
class BookmarksParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.root = {"name": "root", "type": "folder", "children": [], "depth": 0}
        self.stack = [self.root]
        self.all_bookmarks = []
        self.all_folders = []
        self.current_text = ""

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "h3":
            name = ""
            add_date = attrs_dict.get("ADD_DATE", "")
            self.stack.append({
                "name": "",
                "type": "folder",
                "children": [],
                "add_date": add_date,
                "depth": len(self.stack),
                "_raw_attrs": attrs_dict,
            })
        elif tag == "a":
            href = attrs_dict.get("HREF", "")
            add_date = attrs_dict.get("ADD_DATE", "")
            icon = attrs_dict.get("ICON", "")
            self.stack.append({
                "name": "",
                "type": "bookmark",
                "url": href,
                "add_date": add_date,
                "icon": icon,
                "depth": len(self.stack),
            })

    def handle_data(self, data):
        if self.stack:
            self.stack[-1]["name"] += data.strip()

    def handle_endtag(self, tag):
        if tag in ("h3", "a"):
            if len(self.stack) > 1:
                item = self.stack.pop()
                parent = self.stack[-1]
                parent["children"].append(item)
                if item["type"] == "folder":
                    self.all_folders.append(item)
                elif item["type"] == "bookmark":
                    self.all_bookmarks.append(item)

    def handle_charref(self, name):
        if name.startswith("x"):
            char = chr(int(name[1:], 16))
        else:
            char = chr(int(name))
        if self.stack:
            self.stack[-1]["name"] += char


def parse_bookmarks():
    print("正在解析书签文件...")
    with open(BOOKMARKS_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    parser = BookmarksParser()
    parser.feed(content)
    print(f"解析完成: {len(parser.all_bookmarks)} 条书签, {len(parser.all_folders)} 个文件夹")
    return parser.all_bookmarks, parser.all_folders, parser.root


def get_folder_path(item, all_nodes):
    """从 root 开始构建完整路径"""
    # 递归查找
    pass


def classify_bookmark(bookmark, folder_path=""):
    """智能分类书签"""
    url = bookmark.get("url", "").lower()
    title = bookmark.get("name", "").lower()
    path = folder_path.lower()
    combined = f"{path} {title} {url}"
    
    scores = defaultdict(int)
    for cat, keywords in CATEGORY_KEYWORDS.items():
        for kw in keywords:
            if kw in combined:
                scores[cat] += 1
    
    if scores:
        best = max(scores, key=scores.get)
        return best
    
    # 默认分类
    if "youtube.com" in url or "bilibili.com" in url:
        return "21_VideoLearning"
    if "github.com" in url:
        return "19_GitHub"
    if any(d in url for d in ["amazon.com", "amazon.co"]):
        return "13_Amazon"
    
    return "99_Archive"


def get_display_name(bookmark):
    """获取简洁显示名"""
    name = bookmark.get("name", "未命名")
    # 去除 YouTube 前缀
    name = re.sub(r'^\(\d+\)\s*', '', name)
    # 限制长度
    if len(name) > 80:
        name = name[:77] + "..."
    return name


def extract_domain(url):
    """提取域名"""
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        if domain.startswith("www."):
            domain = domain[4:]
        return domain
    except:
        return ""


def sanitize_filename(name):
    """安全文件名"""
    name = re.sub(r'[\\/:*?"<>|]', '-', name)
    if len(name) > 100:
        name = name[:97] + "..."
    return name.strip()


def get_rating(bookmark, folder_path=""):
    """智能评分"""
    url = bookmark.get("url", "")
    title = bookmark.get("name", "")
    domain = extract_domain(url)
    score = 3  # 默认三星
    
    # YouTube 教程通常是高价值
    if "youtube.com/watch" in url:
        score = 4
    # GitHub 项目
    if "github.com" in domain:
        score = 4
    # 官方文档
    if any(s in domain for s in ["docs.", "platform.", "api.", "developer."]):
        score = 5
    # 搜索结果/聚合页
    if "search" in url or "results" in url:
        score = 2
    # 失效链接标记
    if "失效" in folder_path.lower():
        score = 1
    
    return score


# ─── 生成 Vault ───
def generate_vault(all_bookmarks, all_folders, root):
    print("\n开始生成 Obsidian Vault...")
    
    # 确保目录
    for cat, _ in CATEGORIES:
        os.makedirs(os.path.join(VAULT_ROOT, cat), exist_ok=True)
    
    # 构建从 root 到每个 bookmark 的路径
    bookmark_paths = []
    seen_urls = set()
    dup_count = 0
    domain_counter = Counter()
    classified = defaultdict(list)
    
    # 递归收集路径
    def collect(node, path_parts=None):
        nonlocal dup_count
        if path_parts is None:
            path_parts = []
        
        if node["type"] == "bookmark":
            url = node.get("url", "")
            if not url:
                return
            domain = extract_domain(url)
            domain_counter[domain] += 1
            
            # 去重检查
            normalized_url = url.rstrip("/")
            if normalized_url in seen_urls:
                dup_count += 1
            seen_urls.add(normalized_url)
            
            folder_path = " > ".join(path_parts) if path_parts else "根目录"
            cat = classify_bookmark(node, folder_path)
            rating = get_rating(node, folder_path)
            
            bookmark_paths.append({
                "bookmark": node,
                "folder_path": folder_path,
                "category": cat,
                "rating": rating,
                "domain": domain,
                "display_name": get_display_name(node),
            })
            classified[cat].append(node)
        elif node["type"] == "folder":
            name = node["name"]
            for child in node.get("children", []):
                collect(child, path_parts + [name])
    
    # 从 root 开始收集（跳过 root 本身）
    for child in root.get("children", []):
        collect(child, [])
    
    total = len(bookmark_paths)
    unique_domains = len(domain_counter)
    print(f"总书签: {total}, 去重后: {len(seen_urls)}, 重复: {dup_count}")
    print(f"不同域名: {unique_domains}")
    
    # 分类统计
    for cat, _ in CATEGORIES:
        if cat in ("00_Dashboard", "90_Reports", "99_Archive"):
            continue
        count = len(classified.get(cat, []))
        print(f"  {cat}: {count} 条")
    
    # ─── 生成 site notes ───
    site_index = {}  # site_name -> {url, count, bookmarks}
    site_counter = 1
    
    for bp in bookmark_paths:
        domain = bp["domain"]
        name = bp["display_name"]
        site_key = domain
        
        if site_key not in site_index:
            site_index[site_key] = {
                "name": domain,
                "urls": set(),
                "bookmarks": [],
                "category": bp["category"],
                "best_rating": bp["rating"],
            }
        site_index[site_key]["urls"].add(bp["bookmark"]["url"])
        site_index[site_key]["bookmarks"].append(bp)
        site_index[site_key]["best_rating"] = max(site_index[site_key]["best_rating"], bp["rating"])
    
    # 生成网站笔记
    print("\n生成网站笔记...")
    for site_key, site_info in site_index.items():
        cat = site_info["category"]
        if cat not in ("00_Dashboard", "90_Reports", "99_Archive"):
            pass  # we''ll handle below
        
        # 为每个主域名生成一个笔记
        if len(site_info["urls"]) > 1:
            # 多个 URL，生成网站级笔记
            pass
    
    # ─── 按分类生成 Markdown ───
    print("\n生成分类笔记...")
    
    # 去重后的书签列表（按 URL 去重）
    url_seen = set()
    unique_bookmarks = []
    for bp in bookmark_paths:
        url = bp["bookmark"]["url"].rstrip("/")
        if url not in url_seen:
            url_seen.add(url)
            unique_bookmarks.append(bp)
    
    # 按分类分组生成
    category_files = defaultdict(list)
    
    for bp in unique_bookmarks:
        cat = bp["category"]
        cat_dir = os.path.join(VAULT_ROOT, cat)
        
        # 文件名
        safe_name = sanitize_filename(bp["display_name"])
        filename = f"{safe_name}.md"
        filepath = os.path.join(cat_dir, filename)
        
        # 避免重名
        counter = 1
        base = safe_name
        while os.path.exists(filepath):
            safe_name = f"{base}_{counter}"
            filename = f"{safe_name}.md"
            filepath = os.path.join(cat_dir, filename)
            counter += 1
        
        # 生成笔记内容
        bm = bp["bookmark"]
        url = bm["url"]
        rating_stars = "★★★★★"[:bp["rating"]] + "☆☆☆☆☆"[bp["rating"]:]
        add_date_str = ""
        if bm.get("add_date"):
            try:
                add_date_str = datetime.fromtimestamp(int(bm["add_date"]), tz=timezone.utc).strftime("%Y-%m-%d")
            except:
                pass
        
        tags = TAG_MAP.get(cat, ["其他"])
        tags_str = " ".join([f"#{t}" for t in tags])
        
        content = f"""---
category: {cat}
rating: {bp["rating"]}
domain: {bp["domain"]}
add_date: {add_date_str}
folder: {bp["folder_path"]}
tags: [{", ".join(tags)}]
---

# {bp["display_name"]}

**URL:** {url}

**分类:** {tags_str}

**来源目录:** {bp["folder_path"]}

**推荐指数:** {rating_stars}

---
*自动生成于 {datetime.now().strftime("%Y-%m-%d %H:%M")}*
"""
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        
        category_files[cat].append({
            "filename": filename,
            "name": bp["display_name"],
            "url": url,
            "rating": bp["rating"],
            "rating_stars": rating_stars,
            "domain": bp["domain"],
            "folder_path": bp["folder_path"],
        })
    
    print(f"生成了 {len(unique_bookmarks)} 个网站笔记")
    
    # ─── 生成 MOC ───
    print("\n生成 MOC 页面...")
    cat_descriptions = {
        "01_AI": "人工智能相关资源，包括 LLM、ChatGPT、Claude、Gemini 等",
        "02_Agents": "AI Agent 框架和自动化工作流",
        "03_MCP": "Model Context Protocol 相关资源",
        "04_DeepSeek": "DeepSeek 大模型相关资源",
        "05_Hermes": "Hermes Agent 框架资源",
        "06_OpenClaw": "OpenClaw 项目相关资源",
        "07_WordPress": "WordPress 建站资源",
        "08_WooCommerce": "WooCommerce 电商插件资源",
        "09_CloudPanel": "CloudPanel 服务器面板资源",
        "10_SEO": "搜索引擎优化相关资源",
        "11_CrossBorder": "跨境电商运营资源",
        "12_TikTok": "TikTok 运营和营销资源",
        "13_Amazon": "Amazon 电商平台资源",
        "14_Payment": "跨境支付和收款资源",
        "15_Network": "网络技术和代理资源",
        "16_OpenWRT": "OpenWRT 软路由相关资源",
        "17_NAS": "NAS 网络存储相关资源",
        "18_Docker": "Docker 容器化相关资源",
        "19_GitHub": "GitHub 开源项目资源",
        "20_Programming": "编程和网站开发资源",
        "21_VideoLearning": "视频教程和学习资源",
        "22_Tools": "实用工具和效率资源",
    }
    
    for cat, desc in cat_descriptions.items():
        files = category_files.get(cat, [])
        cat_name = cat.split("_", 1)[1]
        
        content = f"""---
category: MOC
---

# {cat_name} 资源

{desc}

共 **{len(files)}** 条资源

---

"""
        # 按评分排序
        files_sorted = sorted(files, key=lambda x: -x["rating"])
        for f_item in files_sorted:
            content += f"- {f_item['rating_stars']} [[{f_item['filename'].replace('.md', '')}]] - {f_item['url']}\n"
        
        moc_path = os.path.join(VAULT_ROOT, cat, f"_MOC_{cat_name}.md")
        with open(moc_path, "w", encoding="utf-8") as f:
            f.write(content)
    
    # ─── 生成 Dashboard/README ───
    print("生成仪表盘...")
    dashboard = f"""# 我的知识库 📚

> 从 {total} 条书签构建的第二大脑
> 自动生成于 {datetime.now().strftime("%Y-%m-%d %H:%M")}

## 🚀 快速导航

"""
    for cat, cat_title in CATEGORIES:
        if cat in ("00_Dashboard", "90_Reports", "99_Archive"):
            continue
        cat_name = cat.split("_", 1)[1]
        count = len(category_files.get(cat, []))
        dashboard += f"- [[{cat}/{cat_name} 资源|{cat_name}资源]] ({count}条)\n"
    
    dashboard += f"""
---

## 📊 数据统计

| 指标 | 数值 |
|------|------|
| 总书签数 | {total} |
| 去重URL数 | {len(seen_urls)} |
| 总网站数 | {unique_domains} |
| 总分类数 | {len(CATEGORIES) - 3} |
| 重复率 | {dup_count/total*100:.1f}% |

---

## 🗺️ 推荐学习路线

[[90_Reports/Learning Roadmap|学习路线图]]

## 📋 推荐项目路线

[[90_Reports/Project Roadmap|项目路线图]]

## 🔗 知识图谱

[[90_Reports/Knowledge Graph|知识图谱]]

## 📈 统计报告

[[90_Reports/Statistics|域名统计]]
[[90_Reports/Duplicate Report|去重报告]]
[[90_Reports/High Value Resources|高价值资源]]
[[90_Reports/User Profile|兴趣画像]]
[[90_Reports/Website Directory|网站导航]]
"""
    
    with open(os.path.join(VAULT_ROOT, "00_Dashboard", "README.md"), "w", encoding="utf-8") as f:
        f.write(dashboard)
    
    # ─── 生成报告 ───
    print("生成报告页面...")
    
    # 域名统计
    top_domains = domain_counter.most_common(100)
    stats_content = f"""# 域名统计

> 共 {unique_domains} 个不同域名

## Top 100 域名

| 排名 | 域名 | 出现次数 | 占比 |
|------|------|----------|------|
"""
    for i, (domain, count) in enumerate(top_domains, 1):
        pct = count / total * 100
        stats_content += f"| {i} | {domain} | {count} | {pct:.1f}% |\n"
    
    with open(os.path.join(VAULT_ROOT, "90_Reports", "Statistics.md"), "w", encoding="utf-8") as f:
        f.write(stats_content)
    
    # 去重报告
    dup_content = f"""# 去重报告

## 概览

| 指标 | 数值 |
|------|------|
| 原始书签数 | {total} |
| 去重URL数 | {len(seen_urls)} |
| 重复书签数 | {dup_count} |
| 重复率 | {dup_count/total*100:.1f}% |

## 说明

- 重复 URL 已自动合并为单条笔记
- 相同域名不同路径的 URL 保留为独立资源
- 已在笔记中标明收藏时间和来源目录

---
*此报告基于 URL 精确匹配去重*
"""
    with open(os.path.join(VAULT_ROOT, "90_Reports", "Duplicate Report.md"), "w", encoding="utf-8") as f:
        f.write(dup_content)
    
    # 高价值资源
    high_value = [bp for bp in unique_bookmarks if bp["rating"] >= 4]
    high_value.sort(key=lambda x: -x["rating"])
    
    hv_content = f"""# 高价值资源

> 评分 ≥ ★★★★☆ 的资源，共 {len(high_value)} 条

## ★★★★★ 核心资源

"""
    for bp in high_value:
        if bp["rating"] == 5:
            hv_content += f"- [[{sanitize_filename(bp['display_name'])}]] - {bp['url']}\n"
    
    hv_content += "\n## ★★★★☆ 重要资源\n\n"
    for bp in high_value:
        if bp["rating"] == 4:
            hv_content += f"- [[{sanitize_filename(bp['display_name'])}]] - {bp['url']}\n"
    
    with open(os.path.join(VAULT_ROOT, "90_Reports", "High Value Resources.md"), "w", encoding="utf-8") as f:
        f.write(hv_content)
    
    # 网站导航
    nav_content = f"""# 网站导航

> 按分类整理的所有网站

"""
    for cat, cat_title in CATEGORIES:
        if cat in ("00_Dashboard", "90_Reports", "99_Archive"):
            continue
        files = category_files.get(cat, [])
        if not files:
            continue
        cat_name = cat.split("_", 1)[1]
        nav_content += f"## {cat_name}\n\n"
        for f_item in sorted(files, key=lambda x: -x["rating"])[:20]:
            domain = f_item["domain"]
            nav_content += f"- [{domain}]({f_item['url']}) {f_item['rating_stars']}\n"
        if len(files) > 20:
            nav_content += f"- ... 还有 {len(files) - 20} 个网站\n"
        nav_content += "\n"
    
    with open(os.path.join(VAULT_ROOT, "90_Reports", "Website Directory.md"), "w", encoding="utf-8") as f:
        f.write(nav_content)
    
    # 学习路线图
    roadmap = """# 学习路线图 🗺️

> 基于书签分析推荐的系统学习路径

## 阶段 1：AI 基础认知
- 大语言模型基础
- ChatGPT / Claude 使用技巧
- Prompt Engineering

## 阶段 2：AI Agent 入门
- MCP 协议理解
- Agent 框架选型
- 自动化工作流设计

## 阶段 3：DeepSeek 深入
- DeepSeek API 开发
- 本地部署和调优
- 实际项目集成

## 阶段 4：Agent 实战
- Hermes 框架
- OpenClaw 项目
- 多 Agent 协作

## 阶段 5：建站实战
- WordPress 深度使用
- WooCommerce 电商搭建
- 独立站优化

## 阶段 6：跨境电商
- TikTok 运营
- Amazon 店铺
- 支付体系搭建

## 阶段 7：技术基础
- 网络和代理
- OpenWRT 软路由
- NAS 私有云
- Docker 容器化

## 阶段 8：自动化运营
- SEO 矩阵
- AI 内容生成
- 自动铺货
- 数据监控

---
*所有阶段资源均可在对应分类目录中找到*
"""
    with open(os.path.join(VAULT_ROOT, "90_Reports", "Learning Roadmap.md"), "w", encoding="utf-8") as f:
        f.write(roadmap)
    
    # 项目路线图
    proj_roadmap = """# 项目路线图 📋

## 当前项目

- **WinPower** - 独立站电商品牌
- **AI Agent** - 智能代理系统
- **OpenClaw** - 开源框架
- **Hermes** - Agent 集成
- **飞牛 NAS** - 私有云存储

## 发展路线

```
AI 内容生成
    ↓
自动铺货系统
    ↓
SEO 矩阵建设
    ↓
AI 客服自动化
    ↓
智能营销系统
    ↓
独立站规模化增长
```

## 技术栈

- AI: DeepSeek / Claude / Gemini
- Agent: Hermes / OpenClaw / MCP
- 建站: WordPress / WooCommerce
- 基础设施: Docker / NAS / OpenWRT
- 运营: TikTok / Amazon / SEO

---
*此路线图基于书签分析自动生成*
"""
    with open(os.path.join(VAULT_ROOT, "90_Reports", "Project Roadmap.md"), "w", encoding="utf-8") as f:
        f.write(proj_roadmap)
    
    # 知识图谱
    kg = """# 知识图谱 🧠

```
AI
├── DeepSeek
├── Gemini
├── Claude
├── Grok (xAI)
├── OpenAI / ChatGPT
├── OpenRouter
├── Perplexity
├── Kimi / 月之暗面
├── 通义千问
└── 文心一言

Agent
├── Hermes
├── OpenClaw
├── MCP (Model Context Protocol)
├── Dify
├── Coze
├── n8n
├── CrewAI
└── LangChain

建站
├── WordPress
├── WooCommerce
├── Elementor
├── CloudPanel
├── Shopify
├── OpenCart
└── PbootCMS

跨境电商
├── TikTok Shop
├── Amazon
├── Etsy
├── Shopee
└── Lazada

支付
├── Stripe
├── PayPal
├── Mercury
├── Payoneer
└── Wise

基础设施
├── OpenWRT
├── NAS (飞牛/群晖)
├── Docker
├── VPS
└── 代理/网络

开发
├── GitHub
├── Python
├── JavaScript
├── PHP
└── Docker

运营
├── SEO
├── 社交媒体
├── 广告投放
└── 数据分析
```

---
*基于书签的领域关系自动生成*
"""
    with open(os.path.join(VAULT_ROOT, "90_Reports", "Knowledge Graph.md"), "w", encoding="utf-8") as f:
        f.write(kg)
    
    # 兴趣画像
    profile = f"""# 兴趣画像 👤

## 兴趣领域评分

| 领域 | 书签数 | 熟练度推测 | 学习阶段 |
|------|--------|------------|----------|
| AI / LLM | {len(classified.get('01_AI', []))} | ⭐⭐⭐⭐ | 进阶 |
| Agent | {len(classified.get('02_Agents', []))} | ⭐⭐⭐ | 中级 |
| DeepSeek | {len(classified.get('04_DeepSeek', []))} | ⭐⭐⭐⭐ | 进阶 |
| WordPress | {len(classified.get('07_WordPress', []))} | ⭐⭐⭐⭐ | 进阶 |
| 跨境电商 | {len(classified.get('11_CrossBorder', []))} | ⭐⭐⭐ | 中级 |
| TikTok | {len(classified.get('12_TikTok', []))} | ⭐⭐⭐ | 中级 |
| NAS | {len(classified.get('17_NAS', []))} | ⭐⭐⭐ | 中级 |
| 网络 | {len(classified.get('15_Network', []))} | ⭐⭐⭐⭐ | 进阶 |
| 编程 | {len(classified.get('20_Programming', []))} | ⭐⭐⭐ | 中级 |

## 角色定位

基于书签分析，你是一位：
- **AI 技术探索者** - 对 LLM、Agent 有深度研究
- **跨境电商创业者** - 运营独立站/平台店铺
- **技术 DIY 爱好者** - NAS、软路由、网络搭建
- **终身学习者** - 大量视频教程和在线课程

## 学习建议

1. ✅ 优先巩固 **AI Agent 开发**能力
2. ✅ 将 **SEO 知识**应用到独立站
3. ✅ 完善 **自动化运营**流程
4. 📚 补强 **数据分析**技能
5. 📚 探索 **AI + 电商**结合点

---
*基于 {total} 条书签自动分析*
"""
    with open(os.path.join(VAULT_ROOT, "90_Reports", "User Profile.md"), "w", encoding="utf-8") as f:
        f.write(profile)
    
    # ─── 生成汇总 ───
    print("\n" + "="*60)
    print("📊 最终统计")
    print("="*60)
    print(f"原始书签: {total}")
    print(f"去重后:   {len(seen_urls)}")
    print(f"重复数:   {dup_count} ({dup_count/total*100:.1f}%)")
    print(f"域名数:   {unique_domains}")
    print(f"生成目录: {len(CATEGORIES)}")
    print(f"生成笔记: {len(unique_bookmarks)}")
    print(f"\nVault 路径: {VAULT_ROOT}")
    print("="*60)
    
    # 输出分类统计
    print("\n📁 分类明细:")
    for cat, cat_title in CATEGORIES:
        if cat in ("00_Dashboard", "90_Reports", "99_Archive"):
            continue
        count = len(category_files.get(cat, []))
        print(f"  {cat_title:12s} → {cat} ({count}条)")
    
    return bookmark_paths, classified, category_files


if __name__ == "__main__":
    all_bookmarks, all_folders, root = parse_bookmarks()
    bookmark_paths, classified, category_files = generate_vault(all_bookmarks, all_folders, root)
    print("\n✅ 转换完成！可以用 Obsidian 打开 Bookmarks-Vault 文件夹。")
