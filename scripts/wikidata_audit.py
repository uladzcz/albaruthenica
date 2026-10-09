import json
import urllib.request
import urllib.parse
import math
import time
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

USER_AGENT = 'AlbaruthenicaBot/1.0 (https://github.com/uladzcz/albaruthenica; albaruthenica-heritage@example.org)'

def haversine(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    R = 6371.0  # km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

CACHE_FILE = 'scripts/wikidata_cache.json'
cache = {}
if os.path.exists(CACHE_FILE):
    try:
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            cache = json.load(f)
    except Exception:
        cache = {}

def save_cache():
    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

def extract_lang_and_title(url):
    if not url or 'wikipedia.org/wiki/' not in url:
        return None, None
    m = re.search(r'https?://([a-z\-]+)\.wikipedia\.org/wiki/([^#?]+)', url)
    if not m:
        return None, None
    lang = m.group(1)
    title = urllib.parse.unquote(m.group(2)).replace('_', ' ')
    return lang, title

def batch_resolve_wikipedia_urls(urls):
    # Group by language
    by_lang = {}
    url_to_title = {}
    for u in urls:
        if u in cache and cache[u] is not None:
            continue
        lang, title = extract_lang_and_title(u)
        if lang and title:
            by_lang.setdefault(lang, []).append((title, u))
            url_to_title[u] = title

    for lang, items in by_lang.items():
        print(f"Resolving {len(items)} Wikipedia URLs in language '{lang}'...")
        # chunks of 40
        chunks = [items[i:i+40] for i in range(0, len(items), 40)]
        for chunk in chunks:
            titles_param = '|'.join(t[0] for t in chunk)
            quoted_titles = urllib.parse.quote(titles_param, safe='|')
            api_url = f"https://{lang}.wikipedia.org/w/api.php?action=query&prop=pageprops&ppprop=wikibase_item&titles={quoted_titles}&redirects=1&format=json"
            req = urllib.request.Request(api_url, headers={'User-Agent': USER_AGENT})
            try:
                with urllib.request.urlopen(req, timeout=15) as resp:
                    data = json.loads(resp.read().decode('utf-8'))
                    pages = data.get('query', {}).get('pages', {})
                    norm_map = {n['from']: n['to'] for n in data.get('query', {}).get('normalized', [])}
                    redir_map = {r['from']: r['to'] for r in data.get('query', {}).get('redirects', [])}

                    title_to_qid = {}
                    for pid, pdata in pages.items():
                        if pid != '-1':
                            t = pdata.get('title')
                            q = pdata.get('pageprops', {}).get('wikibase_item')
                            if t and q:
                                title_to_qid[t] = q

                    for title, orig_url in chunk:
                        cur = norm_map.get(title, title)
                        while cur in redir_map:
                            cur = redir_map[cur]
                        qid = title_to_qid.get(cur) or title_to_qid.get(title)
                        cache[orig_url] = qid
            except Exception as e:
                print(f"Error querying {lang} chunk: {e}")
            time.sleep(0.5)
    save_cache()

def batch_fetch_wikidata_entities(qids):
    to_fetch = list(set([q for q in qids if q and (q not in cache or not isinstance(cache.get(q), dict))]))
    print(f"Fetching {len(to_fetch)} Wikidata entities in batches of 40...")
    chunks = [to_fetch[i:i+40] for i in range(0, len(to_fetch), 40)]
    for idx, chunk in enumerate(chunks):
        ids_param = '|'.join(chunk)
        url = f"https://www.wikidata.org/w/api.php?action=wbgetentities&ids={ids_param}&props=claims|labels|descriptions&languages=be,ru,en,pl&format=json"
        req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                entities = data.get('entities', {})
                for q, edata in entities.items():
                    cache[q] = edata
        except Exception as e:
            print(f"Error fetching Wikidata chunk {idx}: {e}")
        time.sleep(1.0)
    save_cache()

def main():
    print("=== STARTING BATCH WIKIDATA LINKAGE & QUALITY AUDIT ===")

    with open('data/places.json', 'r', encoding='utf-8') as f:
        places = json.load(f)
    with open('data/persons.json', 'r', encoding='utf-8') as f:
        persons = json.load(f)

    # Add bialystok-all-saints-orthodox-cemetery if not present
    places_ids = {p['id'] for p in places}
    if 'bialystok-all-saints-orthodox-cemetery' not in places_ids:
        places.append({
            "id": "bialystok-all-saints-orthodox-cemetery",
            "title": {
                "by": "Праваслаўныя могілкі Усіх Святых у Беластоку",
                "ru": "Православное кладбище Всех Святых в Белостоке",
                "en": "All Saints Orthodox Cemetery in Białystok"
            },
            "category": "grave",
            "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
            "city": {"by": "Беласток", "ru": "Белосток", "en": "Białystok"},
            "coordinates": [53.151700, 23.181200],
            "description": {
                "by": "Адрас: вул. Уладыслава Высоцкага 1 (ul. Władysława Wysockiego 1), раён Ярашоўка / Выгода, Беласток.\n\nГалоўны гістарычны праваслаўны некропаль Беластока, заснаваны ў 1887 годзе і занесены ў рэестр помнікаў Падляшскага ваяводства. Для беларусаў Падляшша гэты некропаль з'яўляецца сапраўдным нацыянальным пантэонам. Тут спачываюць выбітныя дзеячы беларускага руху і культуры Польшчы:\n• Мікола Гайдук (1933–1998) — пісьменнік, навуковец-фалькларыст, педагог, аўтар падручнікаў беларускай мовы і літаратуры;\n• Віктар Швед (1925–2020) — знакаміты беларускі паэт, журналіст і грамадскі дзеяч Беласточчыны;\n• дзеячы Беларускага грамадска-культурнага таварыства (БГКТ), настаўнікі беларускіх школ і творцы;\n• пахаванні сям'і беларускага сенатара і дзеяча БНР Вячаслава Багдановіча.",
                "ru": "Ул. Высоцкого 1, Белосток. Православное кладбище Всех Святых (осн. 1887 г.) — главный православный некрополь Белостока и пантеон белорусских деятелей Подляшья (Николай Гайдук, Виктор Швед и др.).",
                "en": "All Saints Orthodox Cemetery in Białystok (ul. Władysława Wysockiego 1, founded 1887). The main historical Orthodox necropolis and cultural pantheon for Belarusians in Podlasie, interring prominent writer Mikoła Hajduk, poet Viktar Szwed, and community activists."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Bia%C5%82ystok_-_Cmentarz_prawos%C5%82awny_Wszystkich_%C5%9Awi%C4%99tych.jpg/800px-Bia%C5%82ystok_-_Cmentarz_prawos%C5%82awny_Wszystkich_%C5%9Awi%C4%99tych.jpg",
            "links": [
                {"title": "Polskie Radio: Наведваем некропаль у Беластоку", "url": "https://www.polskieradio.pl/396/7819/artykul/3272947"},
                {"title": "Cmentarz Wszystkich Świętych w Białymstoku (pl.wikipedia)", "url": "https://pl.wikipedia.org/wiki/Cmentarz_Wszystkich_%C5%9Awi%C4%99tych_w_Bia%C5%82ymstoku"}
            ],
            "tags": ["Беласток", "Падляшша", "могілкі", "grave"],
            "personIds": ["mikola-hajduk", "viktar-szwed"],
            "mustSee": True
        })

    person_ids = {p['id'] for p in persons}
    if 'viktar-szwed' not in person_ids:
        persons.append({
            "id": "viktar-szwed",
            "name": {
                "by": "Віктар Швед",
                "ru": "Виктор Швед",
                "en": "Viktar Szwed"
            },
            "dates": "1925–2020",
            "role": {
                "by": "Беларускі паэт, перакладчык, грамадскі дзеяч Беласточчыны",
                "ru": "Белорусский поэт, переводчик, общественный деятель Подляшья",
                "en": "Belarusian poet, translator, community activist in Podlasie"
            },
            "bio": {
                "by": "Нарадзіўся ў вёсцы Мора каля Гайнаўкі на Падляшшы. Выдатны паэт беларускага замежжа, аўтар дзясяткаў зборнікаў паэзіі, сябра Беларускага літаратурнага аб'яднання «Белавежа» і Саюза польскіх пісьменнікаў. Пахаваны на могілках Усіх Святых у Беластоку.",
                "ru": "Родился в д. Море близ Гайновки. Известный белорусский поэт Польши, участник литературного объединения «Беловежа». Похоронен на кладбище Всех Святых в Белостоке.",
                "en": "Born in Morze near Hajnówka. Prominent Belarusian poet in Poland, core member of the 'Biełavieža' literary group. Buried at All Saints Cemetery in Białystok."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Bia%C5%82ystok_-_Cmentarz_prawos%C5%82awny_Wszystkich_%C5%9Awi%C4%99tych.jpg/800px-Bia%C5%82ystok_-_Cmentarz_prawos%C5%82awny_Wszystkich_%C5%9Awi%C4%99tych.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Віктар_Нічыпаравіч_Швед",
            "placeIds": ["bialystok-all-saints-orthodox-cemetery"]
        })

    # Collect all Wikipedia URLs from persons and places
    person_urls = [p.get('wiki') for p in persons if p.get('wiki')]
    place_urls = []
    for pl in places:
        for l in pl.get('links', []):
            u = l.get('url', '')
            if 'wikipedia.org/wiki/' in u:
                place_urls.append(u)

    all_urls = list(set([u for u in person_urls + place_urls if u]))
    print(f"Total unique Wikipedia URLs to resolve: {len(all_urls)}")
    batch_resolve_wikipedia_urls(all_urls)

    # Collect all QIDs
    resolved_qids = []
    for p in persons:
        w = p.get('wiki')
        qid = cache.get(w)
        p['wikidataId'] = qid
        if qid:
            resolved_qids.append(qid)

    for pl in places:
        cand_qids = []
        for l in pl.get('links', []):
            u = l.get('url', '')
            if 'wikipedia.org/wiki/' in u:
                qid = cache.get(u)
                if qid:
                    cand_qids.append(qid)
                    resolved_qids.append(qid)
        pl['candidate_qids'] = cand_qids

    resolved_qids = list(set(resolved_qids))
    print(f"Total resolved QIDs: {len(resolved_qids)}")
    batch_fetch_wikidata_entities(resolved_qids)

    # 3. Apply Strict Quality Rules and Compare Coordinates
    CEMETERY_TYPES = {'Q39614'}  # cemetery
    HUMAN_TYPE = 'Q5'

    discrepancies = []
    blocked_grave_to_cemetery = []
    blocked_person_to_place = []
    matched_places = []
    missing_places = []

    for pl in places:
        cand_qids = pl.pop('candidate_qids', [])
        cat = pl.get('category')
        title_by = pl.get('title', {}).get('by', '')

        is_individual_grave = (cat == 'grave' and any(w in title_by.lower() for w in ['магіла', 'надмагілле', 'пахаваны']))
        is_cemetery = (cat == 'grave' and not is_individual_grave and any(w in title_by.lower() for w in ['могілкі', 'некропаль', 'пантэон']))

        best_qid = None
        best_edata = None
        best_has_coords = False

        for qid in cand_qids:
            if not qid or qid not in cache or not isinstance(cache[qid], dict):
                continue
            edata = cache[qid]
            claims = edata.get('claims', {})
            p31_ids = [c['mainsnak']['datavalue']['value']['id'] for c in claims.get('P31', []) if 'datavalue' in c.get('mainsnak', {})]

            # Rule: Don't link human to a place!
            if HUMAN_TYPE in p31_ids:
                blocked_person_to_place.append({
                    'place_id': pl['id'],
                    'title': title_by,
                    'blocked_qid': qid
                })
                continue

            # Rule: Don't link individual grave to a whole cemetery!
            if is_individual_grave and any(cid in CEMETERY_TYPES for cid in p31_ids):
                blocked_grave_to_cemetery.append({
                    'id': pl['id'],
                    'title': title_by,
                    'blocked_qid': qid,
                    'cemetery_name': edata.get('labels', {}).get('be', {}).get('value') or edata.get('labels', {}).get('en', {}).get('value')
                })
                continue

            has_coords = ('P625' in claims)
            if best_qid is None or (has_coords and not best_has_coords):
                best_qid = qid
                best_edata = edata
                best_has_coords = has_coords

        if best_qid and best_edata:
            claims = best_edata.get('claims', {})
            if 'P625' in claims:
                p625 = claims['P625'][0]['mainsnak']['datavalue']['value']
                w_lat = p625['latitude']
                w_lon = p625['longitude']
                dist = haversine(pl['coordinates'], [w_lat, w_lon])

                pl['wikidataCoords'] = [round(w_lat, 6), round(w_lon, 6)]
                pl['wikidataDistKm'] = round(dist, 3)

                if dist > 1.0:
                    discrepancies.append({
                        'id': pl['id'],
                        'title': title_by,
                        'city': pl.get('city', {}).get('by'),
                        'category': cat,
                        'qid': best_qid,
                        'placeCoords': pl['coordinates'],
                        'wikiCoords': [round(w_lat, 6), round(w_lon, 6)],
                        'distKm': round(dist, 2)
                    })

        pl['wikidataId'] = best_qid

        if best_qid:
            matched_places.append(pl['id'])
        else:
            missing_places.append({
                'id': pl['id'],
                'title': title_by,
                'category': cat,
                'city': pl.get('city', {}).get('by')
            })

    # Sort discrepancies descending
    discrepancies.sort(key=lambda x: x['distKm'], reverse=True)

    print("\n" + "="*50)
    print("=== AUDIT SUMMARY RESULTS ===")
    print(f"Total Places in dataset: {len(places)}")
    print(f"Places matched with precise Wikidata QID: {len(matched_places)}")
    print(f"Places without separate Wikidata item: {len(missing_places)}")
    print(f"Individual graves blocked from general cemetery QID (per user rule): {len(blocked_grave_to_cemetery)}")
    print(f"Places with coordinate discrepancies > 1 km: {len(discrepancies)}")
    print("="*50 + "\n")

    report = {
        'total_places': len(places),
        'matched_places_count': len(matched_places),
        'missing_places_count': len(missing_places),
        'total_persons': len(persons),
        'matched_persons_count': len([p for p in persons if p.get('wikidataId')]),
        'blocked_grave_to_cemetery': blocked_grave_to_cemetery,
        'discrepancies_count': len(discrepancies),
        'top_discrepancies': discrepancies[:35],
        'sample_missing_places': missing_places[:25]
    }

    with open('scripts/wikidata_audit_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    # Save updated datasets
    with open('data/places.json', 'w', encoding='utf-8') as f:
        json.dump(places, f, ensure_ascii=False, indent=2)
    with open('data/places.js', 'w', encoding='utf-8') as f:
        f.write('window.INITIAL_PLACES = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

    with open('data/persons.json', 'w', encoding='utf-8') as f:
        json.dump(persons, f, ensure_ascii=False, indent=2)
    with open('data/persons.js', 'w', encoding='utf-8') as f:
        f.write('window.INITIAL_PERSONS = ' + json.dumps(persons, ensure_ascii=False, indent=2) + ';\n')

    print("Successfully updated places.json, places.js, persons.json, persons.js and generated scripts/wikidata_audit_report.json")

if __name__ == '__main__':
    main()
