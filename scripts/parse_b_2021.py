import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "http://web.archive.org/web/20210512140534/http://vkl.by/letter/%D0%91"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=15) as resp:
    html = resp.read().decode('utf-8', errors='ignore')
    with open('scripts/vkl_letter_b_2021.html', 'w', encoding='utf-8') as f:
        f.write(html)

matches = re.findall(r'<a[^>]+href=["\']([^"\']*/articles/\d+)["\'][^>]*>(.*?)</a>', html, re.I | re.S)
print(f"Total articles found: {len(matches)}")
for href, t in matches:
    title = re.sub(r'<[^>]+>', '', t).strip()
    print(f"  {title} -> {href}")
