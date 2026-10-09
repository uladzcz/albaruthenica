import urllib.request, urllib.parse, json

title = "Święta Góra Grabarka"
url = f"https://pl.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&prop=images&format=json"
req = urllib.request.Request(url, headers={'User-Agent': 'AlbaruthenicaBot/1.0 (info@albaruthenica.org)'})
with urllib.request.urlopen(req) as resp:
    res = json.loads(resp.read().decode('utf-8'))
    for p in res['query']['pages'].values():
        for img in p.get('images', []):
            print(img['title'])
