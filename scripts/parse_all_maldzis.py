import urllib.request
import re
import os
import sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
os.makedirs('scripts/extracted_articles', exist_ok=True)

urls = [
    ('1_budzma_warsaw', 'https://budzma.org/news/gayd-pa-belaruskay-varshave.html'),
    ('2_maldzis_georgia', 'https://maldzis.world/gajd-pa-belaruskih-mjascinah-sakartvjela/'),
    ('3_maldzis_rome', 'https://maldzis.world/belaruskija-mjasciny-vechnym-goradze/'),
    ('4_maldzis_warsaw1', 'https://maldzis.world/belarusskaja-varshava-chast-i-kolonna-sigizmunda-tretego/'),
    ('5_maldzis_warsaw2', 'https://maldzis.world/belarusskaja-varshava-chast-2-bronzovyj-vsadnik-bez-shtanov/'),
    ('6_maldzis_warsaw3', 'https://maldzis.world/belaruskaja-varshava-chastka-3-palac-zavisha/'),
    ('7_maldzis_warsaw4', 'https://maldzis.world/belaruskaja-varshava-chastka-4-palac-burbona/'),
    ('8_maldzis_krakow', 'https://maldzis.world/dze-na-karce-polskaga-krakava-znajsci-belarus/'),
    ('9_maldzis_prague', 'https://maldzis.world/belaruskaja-praga-sabrali-gistoryi-pra-ajchynnyh-litaratara-i-zvjazanyja-z-imi-mescy-stalicy-chjehii/'),
    ('10_maldzis_vilnius', 'https://maldzis.world/scezhkami-vkl-u-vilni-jakija-mescy-vazhnyja-dlja-belaruskaj-gistoryi/'),
    ('11_maldzis_switzerland', 'https://maldzis.world/shagal-po-cjurihu-ne-tolko-mark-ili-belarusskie-mesta-v-shvejcarii/')
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

for name, u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=12) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            soup = BeautifulSoup(html, 'html.parser')
            for s in soup(['script', 'style', 'nav', 'footer']):
                s.decompose()
            title = soup.title.string.strip() if soup.title else name
            
            # For budzma
            if 'budzma.org' in u:
                content = soup.find('div', class_='news-detail') or soup.find('div', class_=re.compile(r'content')) or soup.body
            else:
                # For maldzis.world
                content = soup.find('article') or soup.find('main') or soup.body
                
            text = content.get_text(separator='\n', strip=True) if content else ''
            
            with open(f'scripts/extracted_articles/{name}.txt', 'w', encoding='utf-8') as out:
                out.write(f'URL: {u}\nTITLE: {title}\n\n{text}')
            print(f'Successfully extracted {name}.txt ({len(text)} chars)')
    except Exception as e:
        print(f'Failed {name}: {e}')
