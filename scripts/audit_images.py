import json
import urllib.request
import urllib.parse
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/places.json', 'r', encoding='utf-8') as f:
    places = json.load(f)

img_places = [p for p in places if p.get('image', '').strip()]

def get_filename(url):
    clean = url.split('?')[0]
    fn = clean.split('/')[-1]
    for px in ['960px-', '640px-', '500px-', '440px-', '330px-', '250px-']:
        if fn.startswith(px):
            fn = fn[len(px):]
            break
    return fn

place_by_file = {}
for p in img_places:
    fn = get_filename(p['image'])
    place_by_file.setdefault(fn, []).append(p)

all_files = list(place_by_file.keys())
print(f"Total unique files to verify: {len(all_files)}")

missing_files = []
batch_size = 40
headers = {'User-Agent': 'AlbaruthenicaBot/1.0 (info@albaruthenica.org; mailto:contact@albaruthenica.org)'}

for i in range(0, len(all_files), batch_size):
    batch = all_files[i:i+batch_size]
    titles = '|'.join(['File:' + urllib.parse.unquote(f) for f in batch])
    url = 'https://commons.wikimedia.org/w/api.php?action=query&titles=' + urllib.parse.quote(titles) + '&format=json'
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for page in data.get('query', {}).get('pages', {}).values():
                if 'missing' in page:
                    title = page['title']
                    clean_name = title.replace('File:', '').replace(' ', '_')
                    missing_files.append((title, clean_name))
    except Exception as e:
        print(f"Error in batch {i}: {e}")

print(f"\nMissing files count: {len(missing_files)}")
with open('scripts/missing_images.txt', 'w', encoding='utf-8') as out:
    for mf in missing_files:
        out.write(f"{mf[0]} (clean: {mf[1]})\n")
        # Find which places use this
        for fn, plist in place_by_file.items():
            if urllib.parse.unquote(fn).lower() == mf[1].lower() or fn.lower() == mf[1].lower():
                for p in plist:
                    out.write(f"   -> Place: {p['id']} | {p['title']['by']}\n")
print("Done checking missing images.")
