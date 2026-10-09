import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def extract_article(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    start = text.find('itemprop="articleBody"')
    end = text.find('blrsch')
    snippet = text[start:end]
    clean = re.sub(r'<[^>]+>', '\n', snippet)
    lines = []
    for line in clean.splitlines():
        line = line.strip()
        if len(line) > 25:
            lines.append(line)
    return lines

print("=== ARTICLE 381240 (DÜRER / VAŃKOVIČ) ===")
lines1 = extract_article(r'C:\Users\bafur\.gemini\antigravity\brain\8517a009-ef69-4a92-8d2b-77c899685c1e\.system_generated\steps\5363\content.md')
for l in lines1:
    print(l)
    print('---')

print("\n=== ARTICLE 402922 (RADZIWIŁŁ PAINTINGS) ===")
lines2 = extract_article(r'C:\Users\bafur\.gemini\antigravity\brain\8517a009-ef69-4a92-8d2b-77c899685c1e\.system_generated\steps\5370\content.md')
for l in lines2:
    print(l)
    print('---')
