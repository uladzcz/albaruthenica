import urllib.request
import sys

url = "http://web.archive.org/web/20220524084258/http://vkl.by/letter/%D0%91"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=15) as resp:
    html = resp.read().decode('utf-8', errors='ignore')
    with open('scripts/vkl_letter_b.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Saved scripts/vkl_letter_b.html")
