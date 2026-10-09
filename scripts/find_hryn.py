import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\bafur\.gemini\antigravity\brain\8517a009-ef69-4a92-8d2b-77c899685c1e\.system_generated\steps\2462\content.md', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('Грынявіцкі')
while idx != -1:
    print(f"Index: {idx}")
    print(re.sub(r'<[^>]+>', ' ', html[idx-100:idx+600]))
    print("="*60)
    idx = html.find('Грынявіцкі', idx+1)
