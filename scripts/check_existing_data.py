import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/places.json', 'r', encoding='utf-8') as f:
    places = json.load(f)

print(f"Total places: {len(places)}")

target_persons = ['stanislaw-moniuszko', 'chaim-soutine', 'ossip-zadkine', 'leon-bakst']

for p in places:
    p_persons = p.get('personIds', [])
    for tp in target_persons:
        if tp in p_persons:
            print(f"[{tp}] {p['id']}: {p['title']['by']} ({p['city']})")
