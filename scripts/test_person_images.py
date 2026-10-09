import json
import urllib.request
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/persons.json', 'r', encoding='utf-8') as f:
    persons = json.load(f)

print(f"Testing {len(persons)} person images...")
broken = []
for p in persons:
    url = p.get('image', '')
    if not url:
        print(f"NO URL: {p['id']}")
        broken.append((p['id'], url, "No URL"))
        continue
    req = urllib.request.Request(url, headers={'User-Agent': 'AlbaruthenicaBot/1.0 (https://github.com/uladzcz/albaruthenica; contact@example.com)'})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            if resp.status != 200:
                print(f"FAIL status {resp.status}: {p['id']}")
                broken.append((p['id'], url, resp.status))
            else:
                pass
    except Exception as e:
        print(f"FAIL {e}: {p['id']} -> {url}")
        broken.append((p['id'], url, str(e)))

print(f"\nTotal broken images: {len(broken)} / {len(persons)}")
