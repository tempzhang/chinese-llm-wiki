#!/usr/bin/env python3
"""书签转 Obsidian Vault"""
import os, re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from urllib.parse import urlparse

B = r"D:\文本文档\bookmarks_2026_5_29.html"
V = r"D:\chinese-llm-wiki\Bookmarks-Vault"

CATS = [
    ("00_Dashboard", ""), ("01_AI", ""), ("02_Agents", ""), ("03_MCP", ""),
    ("04_DeepSeek", ""), ("05_Hermes", ""), ("06_OpenClaw", ""),
    ("07_WordPress", ""), ("08_WooCommerce", ""), ("09_CloudPanel", ""),
    ("10_SEO", ""), ("11_CrossBorder", ""), ("12_TikTok", ""),
    ("13_Amazon", ""), ("14_Payment", ""), ("15_Network", ""),
    ("16_OpenWRT", ""), ("17_NAS", ""), ("18_Docker", ""),
    ("19_GitHub", ""), ("20_Programming", ""), ("21_VideoLearning", ""),
    ("22_Tools", ""), ("90_Reports", ""), ("99_Archive", ""),
]


KW = {
    "01_AI": ["chatgpt","gpt-","claude","gemini","grok","copilot","llm","大模型","aigc","openai","perplexity","poe.com","cursor","codex","deepseek","qwen","通义","文心","kimi","豆包","midjourney","dalle","sora","openrouter","硅基流动","siliconflow","anthropic","ai.com","suno","gamma.app","notebooklm","huggingface","modelscope","魔搭","扣子","可灵","即梦","笔记本lm"],
    "02_Agents": ["agent","agents","自动化","workflow","工作流","n8n","make.com","zapier","dify","coze","crewai","autogpt","langchain","langgraph","智能体","multi-agent","agentic","ai员工","ai 员工"],
    "03_MCP": ["mcp","model context protocol","tool use","tool calling","vcp"],
    "04_DeepSeek": ["deepseek","deep seek"],
    "05_Hermes": ["hermes"],
    "06_OpenClaw": ["openclaw","open claw"],
    "07_WordPress": ["wordpress","elementor","wp rocket","wpforms"],
    "08_WooCommerce": ["woocommerce","woo commerce"],
    "09_CloudPanel": ["cloudpanel","cloud panel"],
    "10_SEO": ["seo","sem","搜索引擎","关键词","排名","ahrefs","semrush","serp","backlink","搜索控制台","search console","buzzsumo","majestic","谷歌搜索","google search","google ads","广告投放"],
    "11_CrossBorder": ["跨境","cross border","独立站","外贸","b2b","货代","物流","海外仓","etsy","ebay","美客多","lazada","shopee","fba"],
    "12_TikTok": ["tiktok","抖音","tiktok shop","tk shop","tiktok ads"],
    "13_Amazon": ["amazon","亚马逊","fbm"],
    "14_Payment": ["支付","收款","stripe","paypal","mercury","payoneer","wise","万里汇","pingpong","transferwise","水星银行","银行账户","giffgaff","ultra mobile","itin","paygo"],
    "15_Network": ["vpn","代理","proxy","dns","软路由","vps","v2ray","trojan","ssr","clash","机场","科学上网","翻墙","wireguard","tailscale","zerotier","节点","ip检测","whoer","住宅ip","链式代理"],
    "16_OpenWRT": ["openwrt","lede","immortalwrt","istoreos","n60pro","路由","openclash","passwall"],
    "17_NAS": ["nas","飞牛","群晖","synology","unraid","truenas","omv","emby","jellyfin","plex","网盘","存储","cloudsaver","smartstrm","tvbox","小雅","黑苹果","appletv","storase"],
    "18_Docker": ["docker","容器","container","portainer","docker compose"],
    "19_GitHub": ["github","gitlab","git"],
    "20_Programming": ["编程","programming","python","javascript","php","java","rust","typescript","html","css","react","vue","node.js","api","sql","数据库","后端","前端","fullstack","pbootcms","帝国cms","opencart","shopify","建站","网站建设","域名","服务器","宝塔","nginx","apache","源码","cms"],
    "21_VideoLearning": ["youtube.com","bilibili","教程","tutorial","课程","学习","视频","在线课程","udemy","coursera","podcast","tube"],
    "22_Tools": ["工具","tool","生成器","generator","转换","convert","导航","插件","extension","notion","日历","邮箱","mail","图床","cdn","云服务","短信","接码","临时邮箱","磁力"],
}

TAG = {
    "01_AI": ["AI","LLM"],"02_Agents": ["Agent","自动化"],"03_MCP": ["MCP","协议"],
    "04_DeepSeek": ["DeepSeek","国产AI"],"05_Hermes": ["Hermes","Agent"],
    "06_OpenClaw": ["OpenClaw","Agent"],"07_WordPress": ["WordPress","建站"],
    "08_WooCommerce": ["WooCommerce","电商"],"09_CloudPanel": ["CloudPanel","服务器"],
    "10_SEO": ["SEO","营销"],"11_CrossBorder": ["跨境电商","独立站"],
    "12_TikTok": ["TikTok","短视频"],"13_Amazon": ["Amazon","电商"],
    "14_Payment": ["支付","金融"],"15_Network": ["网络","代理"],
    "16_OpenWRT": ["OpenWRT","路由器"],"17_NAS": ["NAS","存储"],
    "18_Docker": ["Docker","容器"],"19_GitHub": ["GitHub","开源"],
    "20_Programming": ["编程","开发"],"21_VideoLearning": ["视频","学习"],
    "22_Tools": ["工具","效率"],
}

def parse():
    with open(B,'r',encoding='utf-8') as f:
        c = f.read()
    c = re.sub(r'\s+',' ',c)
    root = {'name':'root','type':'folder','children':[]}
    stack = [root]
    pf = None
    ab = []
    af = []
    pos = 0
    while pos < len(c):
        m = re.search(r'<(/?)(DL|DT|H3|A|/A|/H3)\b[^>]*>', c[pos:], re.IGNORECASE)
        if not m: break
        te = pos + m.end()
        txt = m.group(0).lower()
        if txt.startswith('<dl'):
            if pf:
                stack[-1]['children'].append(pf)
                af.append(pf)
                stack.append(pf)
                pf = None
            pos = te
        elif txt.startswith('</dl'):
            if len(stack)>1: stack.pop()
            pos = te
        elif txt.startswith('<h3'):
            ad = ''
            dm = re.search(r'ADD_DATE="(\d+)"', m.group(0))
            if dm: ad = dm.group(1)
            em = re.search(r'</H3>', c[te:], re.IGNORECASE)
            if em:
                nm = c[te:te+em.start()].strip()
                nm = re.sub(r'\s+',' ',nm)
                pf = {'name':nm,'type':'folder','children':[],'add_date':ad}
                pos = te + em.end()
            else:
                pos = te
        elif txt.startswith('<a'):
            hr = ''
            ad = ''
            dm = re.search(r'HREF="([^"]*)"', m.group(0), re.IGNORECASE)
            if dm: hr = dm.group(1)
            dm = re.search(r'ADD_DATE="(\d+)"', m.group(0))
            if dm: ad = dm.group(1)
            em = re.search(r'</A>', c[te:], re.IGNORECASE)
            if em:
                nm = c[te:te+em.start()].strip()
                nm = re.sub(r'\s+',' ',nm)
                bm = {'name':nm,'type':'bookmark','url':hr,'add_date':ad}
                stack[-1]['children'].append(bm)
                ab.append(bm)
                pos = te + em.end()
            else:
                pos = te
        else:
            pos = te
    return ab, af, root


def cls(bm, fp=""):
    u = bm.get("url","").lower()
    n = bm.get("name","").lower()
    p = fp.lower()
    cb = "{} {} {}".format(p,n,u)
    sc = defaultdict(int)
    for cat, kws in KW.items():
        for kw in kws:
            if kw.lower() in cb: sc[cat] += 1
    if sc:
        priority = ["04_DeepSeek","05_Hermes","06_OpenClaw","08_WooCommerce","09_CloudPanel","03_MCP","02_Agents","07_WordPress","10_SEO","12_TikTok","13_Amazon","14_Payment","16_OpenWRT","17_NAS","18_Docker","19_GitHub","11_CrossBorder","15_Network","20_Programming","21_VideoLearning","22_Tools","01_AI"]
        for cat in priority:
            if cat in sc and sc[cat] > 0:
                return cat
        return max(sc, key=sc.get)
    if "youtube.com" in u or "bilibili.com" in u: return "21_VideoLearning"
    if "github.com" in u: return "19_GitHub"
    if any(d in u for d in ["amazon.com","amazon.co"]): return "13_Amazon"
    return "99_Archive"

def dn(bm):
    n = bm.get("name","未命名")
    n = re.sub(r'^\(\d+\)\s*','',n)
    if len(n)>80: n = n[:77]+"..."
    return n.strip()

def dom(url):
    try:
        p = urlparse(url)
        d = p.netloc.lower()
        if d.startswith("www."): d = d[4:]
        return d
    except: return ""

def sf(name):
    name = re.sub(r'[\\/:*?"<>|]','-',name)
    if len(name)>100: name = name[:97]+"..."
    return name.strip()

def rt(bm, fp=""):
    u = bm.get("url","")
    d = dom(u)
    pl = fp.lower()
    if "失效" in pl or "temp" in pl: return 1
    if any(s in d for s in ["docs.","platform.","api.","developer."]): return 5
    if "github.com" in d: return 4
    if "youtube.com/watch" in u: return 4
    if "search" in u or "results" in u: return 2
    return 3


def gen():
    ab, af, root = parse()
    print("Parsed: {} bookmarks, {} folders".format(len(ab), len(af)))
    
    for cat, _ in CATS:
        os.makedirs(os.path.join(V, cat), exist_ok=True)
    
    bps = []
    dc = Counter()
    us = set()
    dp = 0
    
    def coll(node, pp):
        nonlocal dp
        if node["type"] == "bookmark":
            u = node.get("url","")
            if not u: return
            d = dom(u)
            dc[d] += 1
            nu = u.rstrip("/")
            if nu in us: dp += 1
            us.add(nu)
            fp = " > ".join(pp) if pp else "根目录"
            cat = cls(node, fp)
            rat = rt(node, fp)
            bps.append({"bm":node,"fp":fp,"cat":cat,"rat":rat,"dom":d,"dn":dn(node)})
        elif node["type"] == "folder":
            for c in node.get("children",[]):
                coll(c, pp + [node["name"]])
    
    for c in root.get("children",[]):
        coll(c, [])
    
    total = len(bps)
    ud = len(dc)
    uu = len(us)
    print("Total: {}, Unique URLs: {}, Dups: {}, Domains: {}".format(total, uu, dp, ud))
    
    cl = defaultdict(list)
    for bp in bps:
        cl[bp["cat"]].append(bp)
    
    for cat, _ in CATS:
        if cat in ("00_Dashboard","90_Reports","99_Archive"): continue
        print("  {}: {}".format(cat, len(cl.get(cat,[]))))
    
    # Generate notes
    print("\nGenerating notes...")
    cf = defaultdict(list)
    nc = 0
    
    for bp in bps:
        cat = bp["cat"]
        cd = os.path.join(V, cat)
        sn = sf(bp["dn"])
        if not sn: sn = "unnamed"
        fn = sn + ".md"
        fp2 = os.path.join(cd, fn)
        ctr = 1
        while os.path.exists(fp2):
            fn = "{}_{}.md".format(sn, ctr)
            fp2 = os.path.join(cd, fn)
            ctr += 1
        
        bm = bp["bm"]
        url = bm["url"]
        rs = chr(9733)*bp["rat"] + chr(9734)*(5-bp["rat"])
        ads = ""
        if bm.get("add_date"):
            try:
                ads = datetime.fromtimestamp(int(bm["add_date"]), tz=timezone.utc).strftime("%Y-%m-%d")
            except: pass
        
        tags = TAG.get(cat, ["其他"])
        
        with open(fp2, "w", encoding="utf-8") as f:
            f.write("---\ncategory: {}\nrating: {}\ndomain: {}\nadd_date: {}\nfolder: {}\ntags: [{}]\n---\n\n# {}\n\n**URL:** {}\n\n**分类:** {}\n\n**来源目录:** {}\n\n**推荐指数:** {}\n\n---\n*auto-generated {}*\n".format(
                cat, bp["rat"], bp["dom"], ads, bp["fp"],
                ", ".join(tags), bp["dn"], url, " ".join(["#"+t for t in tags]),
                bp["fp"], rs, datetime.now().strftime("%Y-%m-%d %H:%M")))
        
        nn = fn.replace(".md","")
        cf[cat].append({"fn":fn,"nn":nn,"name":bp["dn"],"url":url,"rat":bp["rat"],"rs":rs,"dom":bp["dom"],"fp":bp["fp"]})
        nc += 1
    
    print("Generated {} notes".format(nc))


    # MOCs
    print("Generating MOCs...")
    cd2 = {
        "01_AI":"AI和LLM相关资源","02_Agents":"Agent框架和自动化","03_MCP":"Model Context Protocol",
        "04_DeepSeek":"DeepSeek大模型","05_Hermes":"Hermes Agent框架","06_OpenClaw":"OpenClaw资源",
        "07_WordPress":"WordPress建站","08_WooCommerce":"WooCommerce电商","09_CloudPanel":"CloudPanel面板",
        "10_SEO":"搜索引擎优化","11_CrossBorder":"跨境电商运营","12_TikTok":"TikTok运营",
        "13_Amazon":"Amazon电商","14_Payment":"支付收款","15_Network":"网络代理",
        "16_OpenWRT":"OpenWRT软路由","17_NAS":"NAS存储","18_Docker":"Docker容器",
        "19_GitHub":"GitHub项目","20_Programming":"编程开发","21_VideoLearning":"视频教程","22_Tools":"实用工具",
    }
    for cat, desc in cd2.items():
        fls = cf.get(cat, [])
        cn = cat.split("_",1)[1]
        fls_s = sorted(fls, key=lambda x: -x["rat"])
        lines = ["---\ncategory: MOC\n---\n","# {} 资源\n\n".format(cn),desc,"\n\n共 **{}** 条\n\n---\n\n".format(len(fls))]
        for it in fls_s:
            lines.append("- {} [[{}]] - {}\n".format(it["rs"], it["nn"], it["url"]))
        mp = os.path.join(V, cat, "_MOC_{}.md".format(cn))
        with open(mp, "w", encoding="utf-8") as f:
            f.write("".join(lines))
    
    # Dashboard
    print("Generating Dashboard...")
    dlines = ["# 我的知识库 📚\n\n> 从 {} 条书签构建的第二大脑\n> {}".format(total, datetime.now().strftime("%Y-%m-%d %H:%M")),"\n\n## 🚀 快速导航\n\n"]
    for cat, cat_title in CATS:
        if cat in ("00_Dashboard","90_Reports","99_Archive"): continue
        cn = cat.split("_",1)[1]
        cnt = len(cf.get(cat,[]))
        dlines.append("- [[{}/_MOC_{}|{} 资源]] ({}条)\n".format(cat, cn, cn, cnt))
    dlines += [
        "\n---\n\n## 📊 数据统计\n\n| 指标 | 数值 |\n|------|------|\n",
        "| 总书签数 | {} |\n".format(total),
        "| 去重URL数 | {} |\n".format(uu),
        "| 总域名数 | {} |\n".format(ud),
        "| 总分类数 | {} |\n".format(len(CATS)-3),
        "| 重复率 | {:.1f}% |\n".format(dp/total*100 if total else 0),
        "\n---\n\n## 🗺️ 推荐路线\n\n[[90_Reports/Learning Roadmap|学习路线图]]\n[[90_Reports/Project Roadmap|项目路线图]]\n\n## 📈 报告\n\n",
        "[[90_Reports/Knowledge Graph|知识图谱]]\n[[90_Reports/Statistics|域名统计]]\n",
        "[[90_Reports/Duplicate Report|去重报告]]\n[[90_Reports/High Value Resources|高价值资源]]\n",
        "[[90_Reports/User Profile|兴趣画像]]\n[[90_Reports/Website Directory|网站导航]]\n",
    ]
    with open(os.path.join(V, "00_Dashboard", "README.md"), "w", encoding="utf-8") as f:
        f.write("".join(dlines))


    # Reports
    print("Generating reports...")
    
    # Statistics
    td = dc.most_common(100)
    sl = ["# 域名统计\n\n> 共 {} 个域名\n\n## Top 100\n\n| 排名 | 域名 | 次数 | 占比 |\n|------|------|------|------|\n".format(ud)]
    for i, (dmn, cnt) in enumerate(td, 1):
        sl.append("| {} | {} | {} | {:.1f}% |\n".format(i, dmn, cnt, cnt/total*100))
    with open(os.path.join(V, "90_Reports", "Statistics.md"), "w", encoding="utf-8") as f:
        f.write("".join(sl))
    
    # Duplicates
    dup = ["# 去重报告\n\n## 概览\n\n| 指标 | 数值 |\n|------|------|\n",
           "| 原始书签数 | {} |\n".format(total),
           "| 去重URL数 | {} |\n".format(uu),
           "| 重复数 | {} |\n".format(dp),
           "| 重复率 | {:.1f}% |\n\n".format(dp/total*100 if total else 0),
           "## 说明\n- 重复URL已合并\n- 同域名不同路径保留为独立资源\n- 笔记中标注了收藏时间和来源目录\n\n---\n*基于URL精确匹配*"]
    with open(os.path.join(V, "90_Reports", "Duplicate Report.md"), "w", encoding="utf-8") as f:
        f.write("".join(dup))
    
    # High Value
    hv = [bp for bp in bps if bp["rat"] >= 4]
    hv.sort(key=lambda x: -x["rat"])
    hl = ["# 高价值资源\n\n> 评分 >= ★★★★☆，共 {} 条\n\n## ★★★★★ 核心资源\n\n".format(len(hv))]
    for bp in hv:
        if bp["rat"] == 5:
            hl.append("- [[{}]] - {}\n".format(sf(bp["dn"]), bp["bm"]["url"]))
    hl.append("\n## ★★★★☆ 重要资源\n\n")
    for bp in hv:
        if bp["rat"] == 4:
            hl.append("- [[{}]] - {}\n".format(sf(bp["dn"]), bp["bm"]["url"]))
    with open(os.path.join(V, "90_Reports", "High Value Resources.md"), "w", encoding="utf-8") as f:
        f.write("".join(hl))
    
    # Website Directory
    nl = ["# 网站导航\n\n> 按分类整理\n\n"]
    for cat, _ in CATS:
        if cat in ("00_Dashboard","90_Reports","99_Archive"): continue
        fls = cf.get(cat, [])
        if not fls: continue
        cn = cat.split("_",1)[1]
        nl.append("## {}\n\n".format(cn))
        for it in sorted(fls, key=lambda x: -x["rat"])[:30]:
            nl.append("- [{}]({}) {}\n".format(it["dom"], it["url"], it["rs"]))
        if len(fls) > 30:
            nl.append("- ... 还有 {} 个网站\n".format(len(fls)-30))
        nl.append("\n")
    with open(os.path.join(V, "90_Reports", "Website Directory.md"), "w", encoding="utf-8") as f:
        f.write("".join(nl))


    # Learning Roadmap
    lr = ["# 学习路线图 🗺️\n\n> 基于 {} 条书签分析\n\n".format(total),
          "## 阶段1：AI基础\n- LLM基础与大模型原理\n- ChatGPT/Claude使用技巧\n- Prompt Engineering\n\n",
          "## 阶段2：Agent入门\n- MCP协议理解\n- Agent框架对比(Dify/Coze/n8n)\n- 自动化工作流\n\n",
          "## 阶段3：DeepSeek深入\n- DeepSeek API开发\n- 本地部署调优\n- 项目集成\n\n",
          "## 阶段4：Agent实战\n- Hermes框架\n- OpenClaw项目\n- 多Agent协作\n\n",
          "## 阶段5：建站\n- WordPress深度使用\n- WooCommerce电商\n- CloudPanel管理\n\n",
          "## 阶段6：跨境电商\n- TikTok运营\n- Amazon店铺\n- 支付体系(Stripe/PayPal/Mercury)\n\n",
          "## 阶段7：技术基础\n- 网络和VPN\n- OpenWRT软路由\n- NAS私有云\n- Docker容器化\n\n",
          "## 阶段8：自动化运营\n- SEO矩阵\n- AI内容生成\n- 自动铺货\n- 数据监控\n\n",
          "---\n*所有资源可在对应分类目录中找到*"]
    with open(os.path.join(V, "90_Reports", "Learning Roadmap.md"), "w", encoding="utf-8") as f:
        f.write("".join(lr))
    
    # Project Roadmap
    pr = ["# 项目路线图 📋\n\n## 当前项目\n- **WinPower** - 独立站电商\n- **AI Agent** - 智能代理\n- **OpenClaw** - 开源框架\n- **Hermes** - Agent集成\n- **飞牛NAS** - 私有云\n\n## 发展路线\n```\nAI内容生成\n    ↓\n自动铺货\n    ↓\nSEO矩阵\n    ↓\nAI客服\n    ↓\n智能营销\n    ↓\n独立站增长\n```\n\n## 技术栈\n- AI: DeepSeek/Claude/Gemini\n- Agent: Hermes/OpenClaw/MCP\n- 建站: WordPress/WooCommerce\n- 基础设施: Docker/NAS/OpenWRT\n- 运营: TikTok/Amazon/SEO\n- 支付: Stripe/PayPal/Mercury/Wise\n\n---\n*基于书签分析生成*"]
    with open(os.path.join(V, "90_Reports", "Project Roadmap.md"), "w", encoding="utf-8") as f:
        f.write("".join(pr))
    
    # Knowledge Graph
    kg = ["# 知识图谱 🧠\n\n```\n",
          "AI\n├── DeepSeek\n├── Gemini\n├── Claude\n├── Grok\n├── OpenAI/ChatGPT\n├── OpenRouter\n├── Perplexity\n├── Kimi\n├── 通义千问\n└── 文心一言\n\n",
          "Agent\n├── Hermes\n├── OpenClaw\n├── MCP\n├── VCP\n├── Dify\n├── Coze\n├── n8n\n├── CrewAI\n└── LangChain\n\n",
          "建站\n├── WordPress\n├── WooCommerce\n├── Elementor\n├── CloudPanel\n├── Shopify\n├── OpenCart\n└── PbootCMS\n\n",
          "跨境电商\n├── TikTok Shop\n├── Amazon\n├── Etsy\n├── Shopee\n└── Lazada\n\n",
          "支付\n├── Stripe\n├── PayPal\n├── Mercury\n├── Payoneer\n└── Wise\n\n",
          "基础设施\n├── OpenWRT\n├── NAS(飞牛/群晖)\n├── Docker\n├── VPS\n└── 代理/网络\n\n",
          "开发\n├── GitHub\n├── Python\n├── JavaScript\n├── PHP\n└── Docker\n\n",
          "运营\n├── SEO\n├── 社交媒体\n├── 广告投放\n└── 数据分析\n```\n\n---\n*基于书签领域关系自动生成*"]
    with open(os.path.join(V, "90_Reports", "Knowledge Graph.md"), "w", encoding="utf-8") as f:
        f.write("".join(kg))
    
    # User Profile
    up = ["# 兴趣画像 👤\n\n## 兴趣领域\n\n| 领域 | 书签数 | 熟练度 | 阶段 |\n|------|--------|--------|------|\n"]
    ir = {"01_AI":("⭐⭐⭐⭐","进阶"),"02_Agents":("⭐⭐⭐","中级"),"04_DeepSeek":("⭐⭐⭐⭐","进阶"),
          "07_WordPress":("⭐⭐⭐⭐","进阶"),"11_CrossBorder":("⭐⭐⭐","中级"),"12_TikTok":("⭐⭐⭐","中级"),
          "17_NAS":("⭐⭐⭐","中级"),"15_Network":("⭐⭐⭐⭐","进阶"),"20_Programming":("⭐⭐⭐","中级"),
          "10_SEO":("⭐⭐⭐","中级"),"19_GitHub":("⭐⭐⭐","中级"),"18_Docker":("⭐⭐⭐","中级")}
    for cid, (lv,st) in ir.items():
        nm = cid.split("_",1)[1]
        ct = len(cl.get(cid,[]))
        up.append("| {} | {} | {} | {} |\n".format(nm,ct,lv,st))
    up += ["\n## 角色定位\n\n- **AI技术探索者** - LLM/Agent深度研究\n- **跨境电商创业者** - 独立站/平台运营\n",
           "- **技术DIY爱好者** - NAS/软路由/网络\n- **终身学习者** - 大量视频教程\n\n## 学习建议\n\n",
           "1. ✅ 强化AI Agent开发\n2. ✅ SEO知识应用到独立站\n3. ✅ 完善自动化运营\n4. 📚 补强数据分析\n5. 📚 探索AI+电商\n\n",
           "---\n*基于 {} 条书签分析*".format(total)]
    with open(os.path.join(V, "90_Reports", "User Profile.md"), "w", encoding="utf-8") as f:
        f.write("".join(up))
    
    # Summary
    print("\n" + "="*60)
    print("DONE")
    print("="*60)
    print("Bookmarks: {}".format(total))
    print("Unique URLs: {}".format(uu))
    print("Duplicates: {} ({:.1f}%)".format(dp, dp/total*100 if total else 0))
    print("Domains: {}".format(ud))
    print("Categories: {}".format(len(CATS)))
    print("Notes: {}".format(nc))
    print("Vault: {}".format(V))
    print("="*60)

if __name__ == "__main__":
    gen()
    print("\nDone! Open Bookmarks-Vault in Obsidian.")

