import time
import urllib.request
import json

def search_commons(query):
    import urllib.parse
    time.sleep(1.5)
    url = f"https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(query)}&srnamespace=6&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'AlbaruthenicaBot/1.0 (https://github.com/albaruthenica; mailto:admin@albaruthenica.org)'})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            results = []
            for item in data.get('query', {}).get('search', []):
                title = item['title']
                results.append(title)
            return results
    except Exception as e:
        return [str(e)]

def get_file_url(file_title):
    import urllib.parse
    time.sleep(1.5)
    url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(file_title)}&prop=imageinfo&iiprop=url&iiurlwidth=800&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'AlbaruthenicaBot/1.0 (https://github.com/albaruthenica; mailto:admin@albaruthenica.org)'})

    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        for p in data['query']['pages'].values():
            if 'imageinfo' in p:
                return p['imageinfo'][0]['url']
    return None

with open('scripts/images_found.txt', 'w', encoding='utf-8') as f:
    for q in ["Święta Góra Grabarka", "Grabarka cerkiew", "Studziwody", "Bielsk Podlaski liceum"]:
        res = search_commons(q)
        f.write(f"\n=== Query: {q} ===\n")
        for t in res[:6]:
            u = get_file_url(t)
            f.write(f"{t} --> {u}\n")

print("Done finding images.")
