import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://belsat.eu/81551421/belaruskiya-myastsiny-u-belastoku-goradze-yaki-tsyagam-hh-st-6-razou-zmyaniu-dzyarzhavu"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print("HTML length:", len(html))
        # Find article paragraphs
        m = re.findall(r'<p>(.*?)</p>', html, re.I | re.S)
        print(f"Paragraphs: {len(m)}")
        text = "\n\n".join([re.sub(r'<[^>]+>', '', p).strip() for p in m if len(p) > 20])
        print(text[:3000])
        with open('scripts/belsat_bialystok.txt', 'w', encoding='utf-8') as f:
            f.write(text)
except Exception as e:
    print("Error:", e)
