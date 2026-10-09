import urllib.request
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://belsat.eu/81551421/belaruskiya-myastsiny-u-belastoku-goradze-yaki-tsyagam-hh-st-6-razou-zmyaniu-dzyarzhavu"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=15) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

# Check __NEXT_DATA__ or other script tags
m = re.search(r'<script[^>]*id=["\']__NEXT_DATA__["\'][^>]*>(.*?)</script>', html, re.S)
if m:
    data = json.loads(m.group(1))
    print("Found NEXT_DATA!")
    # dump sample
    with open('scripts/belsat_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Saved scripts/belsat_data.json")
else:
    # search where text of article is
    print("Searching for article text in html...")
    matches = re.findall(r'<div[^>]*class=["\'][^"\']*text[^"\']*["\'][^>]*>(.*?)</div>', html, re.S)
    print(f"Matches: {len(matches)}")
