import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/find_belsat_text.py', 'r') as f:
    pass

url = "https://belsat.eu/81551421/belaruskiya-myastsiny-u-belastoku-goradze-yaki-tsyagam-hh-st-6-razou-zmyaniu-dzyarzhavu"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=15) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

with open('scripts/belsat_raw.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Saved scripts/belsat_raw.html, size:", len(html))

for kw in ['Warszawska', 'Варшаўск', 'Ніва', 'Луцкевіч', 'Тарашкевіч', 'Грынявіцкі', 'Заменгоф', 'Гайдук', 'БГКТ']:
    idx = html.find(kw)
    print(f"Keyword '{kw}': pos {idx}")
    if idx != -1:
        print("  Context:", re.sub(r'<[^>]+>', ' ', html[idx-50:idx+400])[:300])
