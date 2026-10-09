import urllib.request
import re
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = 'https://maldzis.world/gajd-pa-belaruskih-mjascinah-sakartvjela/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
req = urllib.request.Request(url, headers=headers)
html = urllib.request.urlopen(req).read().decode('utf-8')
print('HTML length:', len(html))

soup = BeautifulSoup(html, 'html.parser')
# Print article tag or main tags
for tag in ['article', 'main', 'section']:
    found = soup.find_all(tag)
    print(f'Tag <{tag}> count: {len(found)}')
    for f in found:
        print(f'  <{tag} class="{f.get("class")}">: {len(f.get_text())} chars')

# Look for text with "Тбілісі" or "Батумі"
for p in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'li', 'div']):
    txt = p.get_text(strip=True)
    if 'Тбілісі' in txt or 'Батумі' in txt or 'Сакартвэла' in txt:
        if len(txt) > 40:
            print(f'Found: {p.name} ({p.get("class")}): {txt[:120]}...')
            break
