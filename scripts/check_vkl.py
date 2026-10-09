import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = 'http://web.archive.org/web/20220331184316/http://www.vkl.by/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        content = resp.read()
        # try detect encoding
        for enc in ['utf-8', 'windows-1251', 'cp1251', 'iso-8859-1']:
            try:
                html = content.decode(enc)
                print(f"Decoded with {enc}")
                break
            except:
                pass
        
        # print title
        title = re.search(r'<title>(.*?)</title>', html, re.I | re.S)
        print('Title:', title.group(1).strip() if title else 'No title')
        
        # look for categories / menus
        with open('scripts/vkl_home.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Saved scripts/vkl_home.html, size:", len(html))
        
        # find links
        links = re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', html, re.I | re.S)
        for href, text in links:
            clean_text = re.sub(r'<[^>]+>', '', text).strip()
            if clean_text:
                print(f"{clean_text[:40]} -> {href}")

except Exception as e:
    print('Error:', e)
