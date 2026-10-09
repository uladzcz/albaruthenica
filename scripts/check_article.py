import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "http://web.archive.org/web/20210512140534/http://vkl.by/articles/203"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print("Length:", len(html))
        # Find title and body
        title = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.I | re.S)
        if title:
            print("Title:", re.sub(r'<[^>]+>', '', title.group(1)).strip())
        content = re.search(r'<div[^>]*class=["\']article-content["\'][^>]*>(.*?)</div>', html, re.I | re.S)
        if not content:
            content = re.search(r'<div[^>]*class=["\']content["\'][^>]*>(.*?)</div>', html, re.I | re.S)
        if content:
            text = re.sub(r'<[^>]+>', ' ', content.group(1)).strip()
            print("Content preview:", text[:500])
        else:
            print("Raw text snippet:")
            # find text near Базельскі
            idx = html.find('Базельскі')
            print(html[idx:idx+600])
except Exception as e:
    print("Error:", e)
