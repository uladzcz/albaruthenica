import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://belsat.eu/81551421/belaruskiya-myastsiny-u-belastoku-goradze-yaki-tsyagam-hh-st-6-razou-zmyaniu-dzyarzhavu"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=15) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

# Search for Беласток
for m in re.finditer(r'Беласток', html):
    pos = m.start()
    print(f"Match at {pos}:")
    snippet = re.sub(r'<[^>]+>', ' ', html[pos-50:pos+1000])
    print(snippet[:600])
    print("="*60)
    break
