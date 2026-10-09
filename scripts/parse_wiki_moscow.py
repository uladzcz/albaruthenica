import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\bafur\.gemini\antigravity\brain\8517a009-ef69-4a92-8d2b-77c899685c1e\.system_generated\steps\2326\content.md', 'r', encoding='utf-8') as f:
    html = f.read()

# find articles in mw-category
links = re.findall(r'<li[^>]*><a[^>]+href=["\'](/wiki/[^"\']+)["\'][^>]*>(.*?)</a></li>', html)
print(f"Total category items: {len(links)}")
for href, title in links:
    clean = re.sub(r'<[^>]+>', '', title).strip()
    if not clean.startswith('Вікіпедыя:') and not clean.startswith('Стварыць') and not clean.startswith('Галоўная'):
        print(f"  • {clean} ({href})")
