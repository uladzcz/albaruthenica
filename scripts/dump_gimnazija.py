import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\bafur\.gemini\antigravity\brain\8517a009-ef69-4a92-8d2b-77c899685c1e\.system_generated\steps\2462\content.md', 'r', encoding='utf-8') as f:
    html = f.read()

snippet = html[95000:115000]
text = re.sub(r'<[^>]+>', '\n', snippet)
text = re.sub(r'&#8230;', '...', text)
text = re.sub(r'&nbsp;', ' ', text)
text = re.sub(r'\n\s*\n', '\n', text)
print(text[:4000])
