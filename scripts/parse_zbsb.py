import sys
import re
import html

sys.stdout.reconfigure(encoding='utf-8')
c = open(r'C:\Users\bafur\.gemini\antigravity\brain\8517a009-ef69-4a92-8d2b-77c899685c1e\.system_generated\steps\1819\content.md', encoding='utf-8').read()

m = re.findall(r'<(article|main|div)[^>]*>(.*?)</\1>', c, re.DOTALL)
for tag, content in m:
    if 'парыж' in content.lower() or 'беларус' in content.lower():
        clean = re.sub(r'<[^>]+>', '\n', content)
        for l in clean.splitlines():
            t = html.unescape(l.strip())
            if len(t) > 30 and 'Бацькаўшчына' not in t and 'Каментар' not in t and 'Катэгорыі' not in t:
                print(t)
        break
