#!/usr/bin/env python3
"""
Yandex & Bing IndexNow Instant Indexing Notification Script
Reads sitemap.xml and submits all canonical URLs of tianyalimestone.com
to Yandex (https://yandex.com/indexnow) and IndexNow API (https://api.indexnow.org/indexnow).
"""
import os
import re
import json
import urllib.request
import urllib.error

_curr = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(_curr) if os.path.basename(_curr) == "scripts" else _curr
SITEMAP_PATH = os.path.join(BASE_DIR, "sitemap.xml")
HOST = "tianyalimestone.com"
KEY = "e8a4c9f21b0d4637a9e52c3f8b7d6e21"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"

ENDPOINTS = [
    "https://yandex.com/indexnow",
    "https://api.indexnow.org/indexnow"
]

def load_urls_from_sitemap():
    if not os.path.exists(SITEMAP_PATH):
        raise FileNotFoundError(f"sitemap.xml not found at {SITEMAP_PATH}")
    with open(SITEMAP_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    # Extract only <loc> inside <url>, not <image:loc>
    url_blocks = re.findall(r"<url>(.*?)</url>", content, flags=re.S)
    urls = []
    for block in url_blocks:
        m = re.search(r"<loc>(https://tianyalimestone\.com[^<]+)</loc>", block)
        if m:
            urls.append(m.group(1).strip())
    return list(dict.fromkeys(urls))

def submit_indexnow(urls):
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls
    }
    data = json.dumps(payload).encode("utf-8")
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "User-Agent": "TianyaLimestone-IndexNow-Client/1.2"
    }

    for endpoint in ENDPOINTS:
        req = urllib.request.Request(endpoint, data=data, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                print(f"[SUCCESS] {endpoint} -> HTTP {resp.status} ({len(urls)} URLs submitted)")
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="ignore")
            print(f"[WARN] {endpoint} -> HTTP {e.code}: {body[:200]}")
        except Exception as e:
            print(f"[ERROR] {endpoint} -> {e}")

if __name__ == "__main__":
    urls = load_urls_from_sitemap()
    print(f"Loaded {len(urls)} canonical URLs from sitemap.xml for IndexNow submission...")
    submit_indexnow(urls)
