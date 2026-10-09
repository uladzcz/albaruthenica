import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\bafur\.gemini\antigravity\brain\8517a009-ef69-4a92-8d2b-77c899685c1e\.system_generated\steps\2462\content.md', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'<div[^>]*class=["\']content-inner[^"\']*["\'][^>]*>(.*?)</div>\s*<div[^>]*class=["\']jnews_inline_related_post', html, re.I | re.S)
if not m:
    m = re.search(r'<div[^>]*class=["\']entry-content[^"\']*["\'][^>]*>(.*?)</div>', html, re.I | re.S)

if m:
    text = re.sub(r'<[^>]+>', '\n', m.group(1))
    text = re.sub(r'\n\s*\n', '\n\n', text).strip()
    print("Article extracted! Length:", len(text))
    print(text[:2500])
else:
    # search where 'Грынявіцкі' appears
    print("Searching for Грынявіцкі...")
    idx = html.find('Грынявіцкі')
    if idx != -1:
        snippet = re.sub(r'<[^>]+>', '\n', html[idx-200:idx+3000])
        print(snippet[:2500])
