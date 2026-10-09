import urllib.request
import urllib.parse
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
headers = {'User-Agent': 'Albaruthenica-Historical-Map/1.0 (https://github.com/bafurt/albaruthenica; contact: bafurt@gmail.com)'}

def check(query):
    q = urllib.parse.quote(query)
    url = f'https://nominatim.openstreetmap.org/search?q={q}&format=json&limit=1'
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as r:
            data = json.loads(r.read())
            if data:
                print(query, '->', data[0]['lat'], data[0]['lon'], '|', data[0].get('display_name'))
            else:
                print(query, '-> NOT FOUND')
    except Exception as e:
        print(query, '-> ERR', e)

check("All Saints' Church, Tudeley")
check("All Saints Church Tudeley Kent")
