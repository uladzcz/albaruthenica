import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://mostmedia.io/tag/belaruskija-mjasciny-belastoka/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print("HTML length:", len(html))
        # Find article links and titles
        matches = re.findall(r'<h[23][^>]*class=["\']entry-title["\'][^>]*>\s*<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', html, re.I | re.S)
        print(f"Found {len(matches)} articles:")
        for href, title in matches:
            clean = re.sub(r'<[^>]+>', '', title).strip()
            print(f"  * {clean} -> {href}")
        if not matches:
            # find all mostmedia.io links in html
            links = re.findall(r'<a[^>]+href=["\'](https://mostmedia\.io/\d{4}/\d{2}/\d{2}/[^"\']+)["\'][^>]*>(.*?)</a>', html)
            for href, title in links[:20]:
                clean = re.sub(r'<[^>]+>', '', title).strip()
                if clean:
                    print(f"  * {clean} -> {href}")
except Exception as e:
    print("Error:", e)
