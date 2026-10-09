import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://www.svaboda.org/a/24876672.html"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=15) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

# Search for all occurrences of Нікалаеў
for m in re.finditer(r'Нікалаеў', html):
    pos = m.start()
    print(f"Occurrence at {pos}:")
    print(html[pos-100:pos+1500])
    print("="*60)
