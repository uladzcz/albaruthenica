import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/msg1.txt', 'r', encoding='utf-8') as f:
    t1 = f.read()
m1 = re.search(r'```(?:json)?\s*(\[\s*\{.*\}\s*\])\s*```', t1, re.DOTALL)
data1 = json.loads(m1.group(1)) if m1 else json.loads(t1.strip())

with open('scratch/msg2.txt', 'r', encoding='utf-8') as f:
    t2 = f.read()
data2 = json.loads(t2.strip()).get('historicalSites', [])

with open('scratch/msg3.txt', 'r', encoding='utf-8') as f:
    t3 = f.read()
m3 = re.search(r'```json\s*(\[\s*\{.*\}\s*\])\s*```', t3, re.DOTALL)
data3 = json.loads(m3.group(1))

imgs = []
for d in data1:
    imgs.append((d['id'], d.get('imageUrl') or d.get('image')))
for d in data2:
    imgs.append((d['id'], d.get('imageUrl') or d.get('image')))
for d in data3:
    imgs.append((d['id'], d.get('imageUrl') or d.get('image')))
    for it in d.get('items', []):
        if 'image' in it:
            imgs.append((f"{d['id']} -> {it.get('title')}", it['image']))

print('Total images to check:', len(imgs))
for place_id, url in imgs:
    if not url:
        print('MISSING IMAGE:', place_id)
    elif not url.startswith('http'):
        print('INVALID URL:', place_id, url)
    else:
        # Check thumbnail pattern
        m = re.search(r'/(\d+)px-', url)
        if m:
            px = int(m.group(1))
            if px not in [250, 330, 480, 500, 640, 800, 960, 1024, 1280]:
                print(f'Unusual thumb size {px}px in: {place_id} -> {url}')

print('Done scanning images.')
