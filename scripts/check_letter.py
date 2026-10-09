import urllib.request
import urllib.parse
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

letter = 'Б'
letter_enc = urllib.parse.quote(letter)
url = f"http://web.archive.org/web/20220331184316/http://www.vkl.by/letter/{letter_enc}"
print("Fetching:", url)
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        print("Final URL:", resp.geturl())
        html = resp.read().decode('utf-8', errors='ignore')
        print("HTML length:", len(html))
        # Look for articles
        articles = re.findall(r'<a[^>]+href=["\']([^"\']*/articles/\d+)["\'][^>]*>(.*?)</a>', html, re.I | re.S)
        print(f"Found {len(articles)} articles:")
        for href, title in articles[:20]:
            clean_title = re.sub(r'<[^>]+>', '', title).strip()
            print(f"  - {clean_title} ({href})")
        
        # Look for pagination
        pages = re.findall(r'<a[^>]+href=["\']([^"\']*/letter/[^"\']*)["\'][^>]*>(.*?)</a>', html, re.I | re.S)
        print("Pagination / letter links:", len(pages))
        for href, p in pages[:15]:
            print("   p:", p.strip(), href)
except Exception as e:
    print("Error:", e)
