import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://www.svaboda.org/a/24876672.html"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=15) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

# Find the main text container
m = re.search(r'<div[^>]*class=["\']wsw[^"\']*["\'][^>]*>(.*?)</div>\s*<div[^>]*class=["\']footer-toolbar', html, re.I | re.S)
if not m:
    m = re.search(r'(Ганна Сурмач, Прага.*?Беларусы добра глядзяцца)', html, re.I | re.S)

if m:
    text = re.sub(r'<[^>]+>', '\n', m.group(1))
    text = re.sub(r'&quot;', '"', text)
    text = re.sub(r'\n\s*\n', '\n\n', text).strip()
    with open('scripts/svaboda_petersburg_full.txt', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Extracted full text! Length:", len(text))
    print(text[:2000])
else:
    print("Could not locate main container.")
