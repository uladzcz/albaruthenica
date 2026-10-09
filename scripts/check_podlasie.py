import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/places.json', 'r', encoding='utf-8') as f:
    places = json.load(f)

keywords = ['bialystok', 'беласток', 'гайнаўк', 'hajnowka', 'bielsk', 'бельск', 'супрасль', 'грабарк', 'grabarka']

matches = []
for p in places:
    text_check = (json.dumps(p.get('title', {}), ensure_ascii=False) + ' ' + 
                  json.dumps(p.get('city', {}), ensure_ascii=False) + ' ' + 
                  p['id']).lower()
    if any(k in text_check for k in keywords):
        matches.append(p)

print(f"Total existing Podlasie places: {len(matches)}")
for p in matches:
    print(f"  • {p['id']}: {p['title']['by']} ({p.get('city', {}).get('by')})")
