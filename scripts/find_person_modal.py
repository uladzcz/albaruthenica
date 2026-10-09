import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('js/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'person' in l.lower() and ('modal' in l.lower() or 'detail' in l.lower() or 'dialog' in l.lower()):
        print(f"{i+1}: {l.strip()[:100]}")
