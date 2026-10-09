import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open(r'C:\Users\bafur\.gemini\antigravity\brain\8517a009-ef69-4a92-8d2b-77c899685c1e\.system_generated\steps\5238\content.md', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('itemprop="articleBody"')
end = text.find('blrsch')
snippet = text[start:end]
clean = re.sub(r'<[^>]+>', '\n', snippet)
for line in clean.splitlines():
    line = line.strip()
    if len(line) > 25:
        print(line)
        print('---')
