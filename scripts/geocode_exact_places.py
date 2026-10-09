import urllib.request
import urllib.parse
import json
import sys
import time

sys.stdout.reconfigure(encoding='utf-8')
headers = {'User-Agent': 'Albaruthenica-Historical-Map/1.0 (https://github.com/bafurt/albaruthenica; contact: bafurt@gmail.com)'}

# Exact queries for OSM Nominatim
queries = {
    'tudeley-all-saints-chagall-windows': "All Saints Church, Crockhurst Street, Tudeley",
    'reims-cathedral-chagall-stained-glass': "Cathédrale Notre-Dame de Reims",
    'paris-opera-garnier-chagall-ceiling': "Opéra Garnier, Paris",
    'metz-cathedral-chagall-stained-glass': "Cathédrale Saint-Étienne de Metz",
    'jerusalem-hadassah-chagall-windows': "Hadassah Ein Kerem Synagogue",
    'jerusalem-knesset-chagall-hall': "Knesset, Jerusalem",
    'mainz-sankt-stephan-chagall-windows': "Sankt Stephan, Mainz",
    'chicago-art-institute-chagall-windows': "Art Institute of Chicago",
    'new-york-met-opera-chagall-murals': "Metropolitan Opera House, New York",
    'saint-paul-de-vence-chagall-grave': "Cimetière de Saint-Paul-de-Vence",
    'amsterdam-stedelijk-chagall': "Stedelijk Museum Amsterdam",
    'basel-kunstmuseum-chagall': "Kunstmuseum Basel",
    'nice-chagall-museum': "Musée National Marc Chagall, Nice",
    'zurich-fraumunster-chagall': "Fraumünster, Zürich",
    'yaroslavl-bahdanovich-museum': "Музей Максима Богдановича, Чайковского 21а, Ярославль",
    'yalta-bahdanovich-grave': "Старое кладбище Ялта Богданович",
    'kaunas-petrasiunai-duzh-dusheuski-grave': "Petrašiūnų kapinės, Kaunas",
    'kaunas-vytautas-8-duzh-dusheuski-house': "Vytauto pr. 8, Kaunas",
    'warsaw-bulak-balachowicz-plaque': "Paryska 27, Warszawa",
    'lytham-hall-belarusian-timber': "Lytham Hall, Ballam Road, Lytham",
}

for pid, q_str in queries.items():
    q = urllib.parse.quote(q_str)
    url = f"https://nominatim.openstreetmap.org/search?q={q}&format=json&limit=1"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as r:
            data = json.loads(r.read())
            if data:
                lat = round(float(data[0]['lat']), 6)
                lon = round(float(data[0]['lon']), 6)
                name = data[0].get('display_name')[:65]
                print(f"'{pid}': [{lat}, {lon}],  # {name}")
            else:
                print(f"'{pid}': NOT FOUND for {q_str}")
    except Exception as e:
        print(f"'{pid}': ERR {e}")
    time.sleep(1.2)
