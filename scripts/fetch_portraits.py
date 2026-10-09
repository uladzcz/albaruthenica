import urllib.request
import urllib.parse
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

people = [
    ('magdalena-radziwill', 'be', 'Марыя_Магдалена_Радзівіл'),
    ('jan-zawisza', 'ru', 'Завиша,_Ян_Тадеушевич'),
    ('yazep-khodzko', 'be', 'Язэп_Ходзька'),
    ('yanka-luchyna', 'be', 'Янка_Лучына'),
    ('pyotra-krecheuski', 'be', 'Пётр_Антонавіч_Крэчэўскі'),
    ('larysa-heniyush', 'be', 'Ларыса_Антонаўна_Геніюш'),
    ('vasil-bykau', 'be', 'Васіль_Уладзіміравіч_Быкаў'),
    ('hanna-tumarkina', 'be', 'Ганна_Паўлаўна_Тумаркіна'),
    ('emeryk-hutten-czapski', 'be', 'Эмерык_Гутэн-Чапскі'),
    ('jazafat-kuncevic', 'be', 'Язафат_Кунцэвіч'),
    ('celina-borzencka', 'be', 'Цэліна_Бажэнцкая'),
    ('aleksandr-valkovich', 'be', 'Аляксандр_Іванавіч_Вальковіч')
]

results = {}
for pid, lang, title in people:
    quoted = urllib.parse.quote(title)
    url = f'https://{lang}.wikipedia.org/api/rest_v1/page/summary/{quoted}'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'AlbaruthenicaBot/1.0 (https://github.com/uladzcz/albaruthenica)'})
        data = json.loads(urllib.request.urlopen(req, timeout=8).read().decode('utf-8'))
        thumb = data.get('thumbnail', {}).get('source', '')
        if thumb:
            thumb = thumb.split('?')[0]
        results[pid] = {
            'title': data.get('title'),
            'thumb': thumb,
            'wiki': data.get('content_urls', {}).get('desktop', {}).get('page', f'https://{lang}.wikipedia.org/wiki/{quoted}')
        }
        print(f'{pid}: OK -> {thumb[:70]}...')
    except Exception as e:
        print(f'{pid}: FAILED ({e})')

with open('scripts/new_persons_images.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
