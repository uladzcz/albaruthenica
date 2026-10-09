import sys, urllib.request, json
sys.stdout.reconfigure(encoding='utf-8')

query = """
[out:json];
area["name"="Якутск"]->.a;
way["name"~"Пояркова"](area.a)->.w1;
way["name"~"Курашова"](area.a)->.w2;
node(w.w1)(w.w2);
out;
"""
url = 'https://overpass-api.de/api/interpreter?data=' + urllib.parse.quote(query)
req = urllib.request.Request(url, headers={'User-Agent': 'AlbaruthenicaBot/1.0'})
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        for elem in data.get('elements', []):
            print('Intersection node:', elem['id'], elem['lat'], elem['lon'])
except Exception as e:
    print('Error:', e)
