import urllib.request
import urllib.parse
import json
import sys
import time

sys.stdout.reconfigure(encoding='utf-8')
headers = {'User-Agent': 'Albaruthenica-Historical-Map/1.0 (https://github.com/bafurt/albaruthenica; contact: bafurt@gmail.com)'}

recent_ids = [
    'tudeley-all-saints-chagall-windows',
    'reims-cathedral-chagall-stained-glass',
    'metz-cathedral-chagall-stained-glass',
    'opera-garnier-chagall-ceiling',
    'mainz-st-stephan-chagall-windows',
    'hadassah-ein-kerem-chagall-synagogue',
    'knesset-jerusalem-chagall-tapestries-mosaics',
    'chicago-art-institute-chagall-windows',
    'metropolitan-opera-chagall-murals',
    'saint-paul-de-vence-chagall-grave',
    'stedelijk-museum-amsterdam-chagall',
    'kunstmuseum-basel-chagall',
    'nice-marc-chagall-national-museum',
    'zurich-fraumunster-chagall-windows',
    'yaroslavl-bahdanovich-museum',
    'yalta-bahdanovich-grave',
    'kaunas-petrasiunai-duzh-dusheuski-grave',
    'kaunas-vytautas-8-duzh-dusheuski-house',
    'warsaw-bulak-balachowicz-plaque',
    'lytham-hall-belarusian-timber',
    'norwich-cathedral-belarusian-timber',
    'st-mary-churche-wood-timber',
    'volchyn-holy-trinity-church-poniatowski',
    'spb-st-catherine-basilica-poniatowski',
    'warsaw-st-john-archcathedral-stanislaw-august-tomb',
]

with open('data/places.json', 'r', encoding='utf-8') as f:
    places = {p['id']: p for p in json.load(f)}

print(f"Checking {len(recent_ids)} places against Wikidata and OSM...")

results = {}

for pid in recent_ids:
    if pid not in places:
        print(f"MISSING: {pid}")
        continue
    p = places[pid]
    cur_coords = p.get('coordinates')
    wiki_url = p.get('wiki') or ''
    title_en = p.get('title', {}).get('en', '')
    
    wiki_coords = None
    wiki_item = None
    if 'wikipedia.org/wiki/' in wiki_url:
        wiki_title = wiki_url.split('/wiki/')[-1]
        lang = wiki_url.split('//')[1].split('.')[0]
        try:
            api_url = f"https://{lang}.wikipedia.org/w/api.php?action=query&prop=coordinates|pageprops&titles={urllib.parse.quote(wiki_title)}&redirects=1&format=json"
            req = urllib.request.Request(api_url, headers=headers)
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read())
                for k, v in data.get('query', {}).get('pages', {}).items():
                    if 'coordinates' in v:
                        c = v['coordinates'][0]
                        wiki_coords = [round(c['lat'], 6), round(c['lon'], 6)]
                    wiki_item = v.get('pageprops', {}).get('wikibase_item')
        except Exception as ex:
            wiki_coords = f"ERR: {ex}"

    print(f"\n{pid}:")
    print(f"  Current:  {cur_coords}")
    print(f"  Wiki:     {wiki_coords} ({wiki_item})")
    results[pid] = {
        'current': cur_coords,
        'wiki_coords': wiki_coords,
        'wiki_item': wiki_item
    }
    time.sleep(0.5)

with open('scripts/audit_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nAudit finished. Results written to scripts/audit_results.json")
