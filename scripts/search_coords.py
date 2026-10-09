import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('js/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'coordsRequest' in l or 'needsCoords' in l:
        print(f"{i+1}: {l.strip()}")
