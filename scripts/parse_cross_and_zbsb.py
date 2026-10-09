import sys
import re
import html

sys.stdout.reconfigure(encoding='utf-8')

print("=== PARSING 400340 (CROSS) ===")
c1 = open(r'C:\Users\bafur\.gemini\antigravity\brain\8517a009-ef69-4a92-8d2b-77c899685c1e\.system_generated\steps\1814\content.md', encoding='utf-8').read()
ps1 = re.findall(r'<p[^>]*>(.*?)</p>', c1, re.DOTALL)
for p in ps1:
    txt = html.unescape(re.sub(r'<[^>]+>', ' ', p).strip())
    if len(txt) > 40 and not txt.startswith('var '):
        print('-', txt[:200])

print("\n=== PARSING 5536 (ZBSB) ===")
c2 = open(r'C:\Users\bafur\.gemini\antigravity\brain\8517a009-ef69-4a92-8d2b-77c899685c1e\.system_generated\steps\1819\content.md', encoding='utf-8').read()
title2 = re.search(r'<title>(.*?)</title>', c2, re.DOTALL)
if title2: print('ZBSB Title:', title2.group(1).strip())
ps2 = re.findall(r'<p[^>]*>(.*?)</p>', c2, re.DOTALL)
for p in ps2:
    txt = html.unescape(re.sub(r'<[^>]+>', ' ', p).strip())
    if len(txt) > 40:
        print('-', txt[:200])
