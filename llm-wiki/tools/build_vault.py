#!/usr/bin/env python3
import html.parser, os, re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from urllib.parse import urlparse

B = r'D:\u6587\u6863\bookmarks_2026_5_29.html'
V = r'D:\chinese-llm-wiki\Bookmarks-Vault'
print('config ok')
