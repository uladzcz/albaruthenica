import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update Mieczyslaw Karlowicz portrait in persons
with open('data/persons.json', 'r', encoding='utf-8') as f:
    persons = json.load(f)

monument_id = 'tatra-kamien-karlowicza-monument'

for p in persons:
    if p['id'] == 'mieczyslaw-karlowicz':
        p['image'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Mieczys%C5%82aw_Kar%C5%82owicz_%28-1909%29.jpg/960px-Mieczys%C5%82aw_Kar%C5%82owicz_%28-1909%29.jpg'
        pids = set(p.get('placeIds', []))
        pids.add(monument_id)
        p['placeIds'] = list(pids)

with open('data/persons.json', 'w', encoding='utf-8') as f:
    json.dump(persons, f, ensure_ascii=False, indent=2)

with open('data/persons.js', 'w', encoding='utf-8') as f:
    f.write('window.INITIAL_PERSONS = ' + json.dumps(persons, ensure_ascii=False, indent=2) + ';\n')

# 2. Add Kamień Karłowicza monument to places
with open('data/places.json', 'r', encoding='utf-8') as f:
    places = json.load(f)

places = [p for p in places if p['id'] != monument_id]

places.append({
    'id': monument_id,
    'title': {
        'by': 'Камень Карловіча ў Татрах (Мемарыял Мечыслава Карловіча)',
        'ru': 'Камень Карловича в Татрах (Мемориал Мечислава Карловича)',
        'en': 'Karłowicz Stone in the Tatras (Mieczysław Karłowicz Memorial)'
    },
    'category': 'monument',
    'country': {
        'by': 'Польшча',
        'ru': 'Польша',
        'en': 'Poland'
    },
    'city': {
        'by': 'Закапанэ (Татры)',
        'ru': 'Закопане (Татры)',
        'en': 'Zakopane (Tatras)'
    },
    'coordinates': [49.2385, 20.010944],
    'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Memorial_stone_to_Mieczys%C5%82aw_Kar%C5%82owicz_%281909%29a.jpg/960px-Memorial_stone_to_Mieczys%C5%82aw_Kar%C5%82owicz_%281909%29a.jpg',
    'wiki': 'https://pl.wikipedia.org/wiki/Kamie%C5%84_Kar%C5%82owicza',
    'description': {
        'by': 'Гранітны мемарыяльны валун ва ўсходняга схілу Малога Касцельца (Mały Kościelec) у Татрах, па сцежцы ад Галы Гансяніцавай да Чорнага става. Усталяваны ў 1910 г. на месцы, дзе 8 лютага 1909 года пад снежнай лавінай трагічна загінуў 32-гадовы кампазітар Мечыслаў Карловіч — выдатны сімфаніст, аўтар «Літоўскай рапсодыі» і піянер татранскага альпінізму і лыжнага спорту.\n\nНа камені выбіты лацінскі надпіс «Non omnis moriar» («Не ўвесь я памру») і старажытны сонечны крыж (які Карловіч выкарыстоўваў як асабістую альпійскую эмблему).',
        'ru': 'Гранитный мемориальный валун у восточного склона Малого Косцельца в Татрах (по тропе от Халы Гонсеницовой к Чёрному ставу). Установлен в 1910 г. на месте, где 8 февраля 1909 года под снежной лавиной трагически погиб 32-летний композитор Мечислав Карлович — уроженец Вишнево, выдающийся симфонист, автор «Литовской рапсодии» и пионер горнолыжного спорта в Татрах. На камне выбита латинская надпись «Non omnis moriar» («Не весь я умру»).',
        'en': 'Granite memorial boulder on the eastern slope of Mały Kościelec in the Tatra Mountains (along the trail from Hala Gąsienicowa to Czarny Staw). Erected in 1910 at the exact spot where 32-year-old composer and pioneer mountaineer Mieczysław Karłowicz perished in an avalanche on 8 February 1909. Inscribed with the Latin motto "Non omnis moriar" ("Not all of me shall die").'
    },
    'links': [
        {
            'title': 'Вікіпедыя: Kamień Karłowicza',
            'url': 'https://pl.wikipedia.org/wiki/Kamie%C5%84_Kar%C5%82owicza'
        },
        {
            'title': 'Вікіпедыя: Мечыслаў Карловіч',
            'url': 'https://be.wikipedia.org/wiki/Мечыслаў_Карловіч'
        }
    ],
    'tags': [
        'карловіч',
        'татры',
        'помнік',
        'музыка',
        'закапанэ',
        'кампазітар',
        'альпінізм'
    ],
    'personId': 'mieczyslaw-karlowicz',
    'personIds': ['mieczyslaw-karlowicz'],
    'mustSee': True
})

with open('data/places.json', 'w', encoding='utf-8') as f:
    json.dump(places, f, ensure_ascii=False, indent=2)

with open('data/places.js', 'w', encoding='utf-8') as f:
    f.write('window.INITIAL_PLACES = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

print(f"Updated Karłowicz portrait and added Kamień Karłowicza ({monument_id}). Total places: {len(places)}")
