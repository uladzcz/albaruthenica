import urllib.request
import re
import urllib.parse
import sys
import time
import json

sys.stdout.reconfigure(encoding='utf-8')

letters = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'І', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Э', 'Ю', 'Я']

results = {}

for l in letters:
    l_enc = urllib.parse.quote(l)
    url = f"http://web.archive.org/web/20210512140534/http://vkl.by/letter/{l_enc}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            articles = re.findall(r'<a[^>]+href=["\']([^"\']*/articles/\d+)["\'][^>]*>(.*?)</a>', html, re.I | re.S)
            art_list = []
            for href, t in articles:
                title = re.sub(r'<[^>]+>', '', t).strip()
                if title and not title.startswith('кнігі пра ВКЛ') and title != 'гісторыя':
                    art_list.append({'title': title, 'href': href})
            results[l] = art_list
            print(f"Letter '{l}': {len(art_list)} articles on page 1")
    except Exception as e:
        print(f"Letter '{l}' failed: {e}")
    time.sleep(0.3)

with open('scripts/vkl_sample_articles.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print("Saved scripts/vkl_sample_articles.json")
