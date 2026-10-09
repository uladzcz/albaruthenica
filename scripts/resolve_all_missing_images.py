import json
import urllib.request
import urllib.parse
import re
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

HEADERS = {'User-Agent': 'AlbaruthenicaBot/1.0 (info@albaruthenica.org)'}

def fetch_wiki_lead_image(wiki_url):
    m = re.match(r'https?://([a-z-]+)\.wikipedia\.org/wiki/(.+)', wiki_url)
    if not m:
        return None
    lang, title = m.groups()
    title_unquoted = urllib.parse.unquote(title)
    api_url = f'https://{lang}.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(title_unquoted)}&prop=pageimages&piprop=original&format=json'
    try:
        req = urllib.request.Request(api_url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for page in pages.values():
                src = page.get('original', {}).get('source')
                if src:
                    return src
    except Exception as e:
        # print(f"Error fetching wiki img for {title}: {e}", flush=True)
        pass
    return None

def search_commons_image(query):
    api_url = 'https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch=' + urllib.parse.quote(query) + '&gsrnamespace=6&prop=imageinfo&iiprop=url&format=json&gsrlimit=1'
    try:
        req = urllib.request.Request(api_url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for page in pages.values():
                info = page.get('imageinfo', [])
                if info and info[0].get('url'):
                    return info[0]['url']
    except Exception:
        pass
    return None

def verify_wikimedia_file(filename):
    clean_fn = urllib.parse.unquote(filename).replace('_', ' ')
    api_url = 'https://commons.wikimedia.org/w/api.php?action=query&titles=File:' + urllib.parse.quote(clean_fn) + '&prop=imageinfo&iiprop=url&format=json'
    try:
        req = urllib.request.Request(api_url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for page in pages.values():
                if 'missing' not in page and page.get('imageinfo'):
                    return page['imageinfo'][0]['url']
    except Exception:
        pass
    return None

def main():
    print("Loading data...", flush=True)
    with open('data/places.json', 'r', encoding='utf-8') as f:
        places = json.load(f)
    with open('data/persons.json', 'r', encoding='utf-8') as f:
        persons = json.load(f)

    # Specific known fixes for personalities
    for per in persons:
        if per['id'] == 'mikola-abramchyk':
            per['wiki'] = 'https://be.wikipedia.org/wiki/Мікола_Абрамчык'
            per['image'] = 'https://upload.wikimedia.org/wikipedia/be/2/21/Мікола_Абрамчык.jpg'
        elif per['id'] == 'nina-abramchyk':
            per['wiki'] = 'https://be.wikipedia.org/wiki/Ніна_Абрамчык'

    # Specific known fixes for places
    known_place_fixes = {
        'florence-city-hub': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Firenze_-_Piazzale_Michelangelo%2C_Firenze%2C_Italy_-_April_6%2C_2015_02.jpg/960px-Firenze_-_Piazzale_Michelangelo%2C_Firenze%2C_Italy_-_April_6%2C_2015_02.jpg',
        'uppsala-carolina-rediviva-belarustreasures': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Carolina_Rediviva_in_summer.jpg/960px-Carolina_Rediviva_in_summer.jpg',
        'istanbul-city-hub': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Historical_peninsula_and_modern_skyline_of_Istanbul.jpg/960px-Historical_peninsula_and_modern_skyline_of_Istanbul.jpg',
        'padua-palazzo-bo-vkl-students': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Cortile_interno_di_Palazzo_Bo.jpg/960px-Cortile_interno_di_Palazzo_Bo.jpg',
        'padua-skaryna-aula-magna': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Palazzo_Bo_%28Padua%29.jpg/960px-Palazzo_Bo_%28Padua%29.jpg',
        'london-st-cyril-church': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Church_of_St_Cyril_of_Turau_and_All_the_Patron_Saints_of_the_Belarusian_People_%282016-11-24%29.jpg/960px-Church_of_St_Cyril_of_Turau_and_All_the_Patron_Saints_of_the_Belarusian_People_%282016-11-24%29.jpg',
        'montmorency-polish-belarusian-pantheon': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Gr%C3%B3bNorwida.jpg/960px-Gr%C3%B3bNorwida.jpg',
        'santiago-domeiko-university': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Domeyko.jpg/960px-Domeyko.jpg',
        'paris-cmentarz-pere-lachaise': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/P%C3%A8re-Lachaise_-_Division_59_-_Abramtchik_01.jpg/960px-P%C3%A8re-Lachaise_-_Division_59_-_Abramtchik_01.jpg'
    }

    for pl in places:
        if pl['id'] in known_place_fixes:
            pl['image'] = known_place_fixes[pl['id']]

        # If place has items, check Abramchyk on Père Lachaise
        if pl['id'] == 'paris-cmentarz-pere-lachaise':
            for it in pl.get('items', []):
                if 'Абрамчык' in it.get('title', ''):
                    it['image'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/P%C3%A8re-Lachaise_-_Division_59_-_Abramtchik_01.jpg/500px-P%C3%A8re-Lachaise_-_Division_59_-_Abramtchik_01.jpg'

    # Audit all images in places
    missing_places = []
    for pl in places:
        img = pl.get('image', '').strip()
        if not img:
            continue
        # Extract filename
        fn = img.split('?')[0].split('/')[-1]
        fn = re.sub(r'^\d+px-', '', fn)
        # Check if verified or verify
        # If image url contains wikipedia/be/ or images.unsplash, it's non-commons valid
        if 'wikipedia/be/' in img or 'unsplash.com' in img:
            continue
        v_url = verify_wikimedia_file(fn)
        if v_url:
            # Update place image with exact canonical url
            pass
        else:
            missing_places.append((pl, fn))

    print(f"Places with non-working images: {len(missing_places)}", flush=True)

    fixed_count = 0
    cleared_count = 0

    for pl, bad_fn in missing_places:
        new_img = None
        # 1. Try wikipedia links
        for l in pl.get('links', []):
            w = l.get('url', '')
            if 'wikipedia.org' in w:
                wiki_img = fetch_wiki_lead_image(w)
                if wiki_img:
                    new_img = wiki_img
                    break
        # 2. Try commons search by place title
        if not new_img:
            q = pl.get('title', {}).get('en') or pl.get('title', {}).get('by')
            if q:
                c_img = search_commons_image(q)
                if c_img:
                    new_img = c_img

        if new_img:
            pl['image'] = new_img
            fixed_count += 1
            print(f"Fixed place {pl['id']} -> {new_img[:60]}...", flush=True)
        else:
            pl['image'] = ""
            cleared_count += 1
            print(f"Cleared broken image on place {pl['id']}", flush=True)

    # Audit persons
    missing_persons = []
    for per in persons:
        img = per.get('image', '').strip()
        if not img or 'Portrait_Placeholder' in img:
            continue
        if 'wikipedia/be/' in img:
            continue
        fn = img.split('?')[0].split('/')[-1]
        fn = re.sub(r'^\d+px-', '', fn)
        v_url = verify_wikimedia_file(fn)
        if not v_url:
            missing_persons.append((per, fn))

    print(f"Persons with non-working images: {len(missing_persons)}", flush=True)

    for per, bad_fn in missing_persons:
        new_img = None
        if per.get('wiki') and 'wikipedia.org' in per['wiki']:
            wiki_img = fetch_wiki_lead_image(per['wiki'])
            if wiki_img:
                new_img = wiki_img

        if not new_img:
            name_en = per.get('name', {}).get('en') or per.get('name', {}).get('by')
            c_img = search_commons_image(name_en)
            if c_img:
                new_img = c_img

        if new_img:
            per['image'] = new_img
            print(f"Fixed person {per['id']} -> {new_img[:60]}...", flush=True)
        else:
            per['image'] = ""
            print(f"Cleared broken image on person {per['id']}", flush=True)

    # Save results
    with open('data/places.json', 'w', encoding='utf-8') as f:
        json.dump(places, f, ensure_ascii=False, indent=2)
    with open('data/places.js', 'w', encoding='utf-8') as f:
        f.write('window.INITIAL_PLACES = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

    with open('data/persons.json', 'w', encoding='utf-8') as f:
        json.dump(persons, f, ensure_ascii=False, indent=2)
    with open('data/persons.js', 'w', encoding='utf-8') as f:
        f.write('window.INITIAL_PERSONS = ' + json.dumps(persons, ensure_ascii=False, indent=2) + ';\n')

    print(f"\nDone! Fixed: {fixed_count}, Cleared broken: {cleared_count}", flush=True)

if __name__ == '__main__':
    main()
