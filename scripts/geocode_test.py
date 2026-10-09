import sys, urllib.request, json
sys.stdout.reconfigure(encoding='utf-8')

def geocode(q):
    url = 'https://nominatim.openstreetmap.org/search?format=json&limit=1&q=' + urllib.parse.quote(q)
    req = urllib.request.Request(url, headers={'User-Agent': 'AlbaruthenicaBot/1.0'})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if data:
                lat = data[0]['lat']
                lon = data[0]['lon']
                name = data[0]['display_name'][:70]
                print(f"{q} --> [{lat}, {lon}] ({name})")
            else:
                print(f"{q} --> NOT FOUND")
    except Exception as e:
        print(f"{q} --> ERROR: {e}")

queries = [
    'улица Пояркова, 8 Якутск',
    'перекресток Пояркова Курашова Якутск',
    'улица Курашова, Якутск',
    'Arrow Park, Monroe, New York',
    'Кутузовский проспект, 28, Москва',
    'Университетская набережная 11 Санкт-Петербург',
    'Bemis Heights Saratoga National Historical Park',
    'Kosciuszko Bridge Brooklyn Queens',
    '15 rue de Clichy 75009 Paris',
    '8 Place de la Republique 75011 Paris',
    'Zamek w Malborku',
    'Cmentarz Łyczakowski Lwów',
    'вулиця Михайла Грушевського, 4, Львів',
    'Strzałkowo, Radomsko',
    'Черкех Таттинский'
]

for q in queries:
    geocode(q)
