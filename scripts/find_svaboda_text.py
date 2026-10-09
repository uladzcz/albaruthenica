import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/get_svaboda.py', 'r', encoding='utf-8') as f:
    pass

import urllib.request
url = "https://www.svaboda.org/a/24876672.html"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=15) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

idx = html.find('Мікола Нікалаеў')
if idx != -1:
    print("Found 'Мікола Нікалаеў' at", idx)
    print(html[idx-100:idx+2500])
else:
    print("'Мікола Нікалаеў' not found in raw text. Checking other snippets...")
    idx2 = html.find('Пецярбург')
    print("Found 'Пецярбург' at", idx2)
    print(html[idx2-50:idx2+500])
