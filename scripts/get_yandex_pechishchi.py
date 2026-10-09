import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

req = urllib.request.Request('https://yandex.ru/maps/org/muzey_yanki_kupaly/1271109961/', headers=headers)
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8')
        # In Yandex Maps, coordinates are [longitude, latitude] or lat/lon
        matches = re.findall(r'(\d{2}\.\d{4,8})', html)
        # find numbers around 55.78 and 48.95
        lats = [x for x in matches if x.startswith('55.78')]
        lons = [x for x in matches if x.startswith('48.95')]
        print('Yandex Latitude matches:', set(lats))
        print('Yandex Longitude matches:', set(lons))
except Exception as e:
    print('Error:', e)
