import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\bafur\.gemini\antigravity\brain\8517a009-ef69-4a92-8d2b-77c899685c1e\.system_generated\steps\2324\content.md', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's find all occurrences of 'Беларускі Пецярбург'
for match in re.finditer(r'Беларускі Пецярбург', html):
    pos = match.start()
    print(f"Match at {pos}:")
    snippet = re.sub(r'<[^>]+>', ' ', html[pos:pos+2000])
    snippet = re.sub(r'\s+', ' ', snippet)
    print(snippet)
    print("="*60)
