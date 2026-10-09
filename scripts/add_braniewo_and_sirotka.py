# -*- coding: utf-8 -*-
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

with open('data/places.json', 'r', encoding='utf-8') as f:
    places = json.load(f)
with open('data/persons.json', 'r', encoding='utf-8') as f:
    persons = json.load(f)

def upsert_place(p_dict):
    global places
    existing = next((p for p in places if p['id'] == p_dict['id']), None)
    if existing:
        existing.update(p_dict)
    else:
        places.append(p_dict)

upsert_place({
    "id": "braniewo-jesuit-college-sirotka-peregrinatio",
    "title": {
        "by": "Езуіцкі калегіум у Браневе — першае выданне «Перэгрынацыі» Радзівіла Сіроткі (1601)",
        "ru": "Иезуитский коллегиум в Бранево — первое издание «Перегринации» Радзивилла Сиротки (1601)",
        "en": "Collegium Hosianum in Braniewo — First Edition of Radziwiłł's \"Peregrination\" (1601)"
    },
    "category": "culture",
    "country": {
        "by": "Польшча",
        "ru": "Польша",
        "en": "Poland"
    },
    "city": {
        "by": "Бранева",
        "ru": "Бранево",
        "en": "Braniewo"
    },
    "coordinates": [
        54.3797,
        19.8242
    ],
    "description": {
        "by": "Славуты езуіцкі калегіум (Collegium Hosianum), заснаваны ў 1565 г. кардыналам Станіславам Гозіем, найважнейшы адукацыйны цэнтр, дзе вучыліся многія выхадцы з Вялікага Княства Літоўскага і Беларусі. У 1601 годзе ў друкарні калегіума выдавец Георг Шонфельс упершыню надрукаваў знакамітую «Перэгрынацыю» князя Мікалая Крыштафа Радзівіла «Сіроткі» («Hierosolymitana peregrinatio...») у лацінскім перакладзе Томаша Трэтэра. Кніга пра падарожжа ў Святую Зямлю і Егіпет стала першым сусветным бестселерам, напісаным ураджэнцам Беларусі, вытрымаўшы дзясяткі перавыданняў на розных еўрапейскіх мовах.",
        "ru": "Знаменитый иезуитский коллегиум (Collegium Hosianum) в Вармии, основанный в 1565 году, где учились многие уроженцы ВКЛ. В 1601 году в типографии коллегиума Георгом Шёнфельсом было впервые напечатано латинское издание «Перегринации» князя Николая Христофора Радзивилла «Сиротки» в переводе Томаша Третера — один из популярнейших европейских путеводителей XVII века.",
        "en": "Renowned Jesuit college (Collegium Hosianum) in Warmia founded in 1565 by Cardinal Stanislaus Hosius, alma mater of many GDL scholars. In 1601, printer Georg Schönfels published the first edition of Prince Mikołaj Krzysztof Radziwiłł 'the Orphan's' celebrated travelogue 'Hierosolymitana Peregrinatio', translated into Latin by Thomas Treter, becoming an international European bestseller."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Braniewo_Collegium_Hosianum.jpg/960px-Braniewo_Collegium_Hosianum.jpg",
    "links": [
        {
            "title": "Нацыянальная бібліятэка Беларусі: 420 год «Перэгрынацыі» Радзівіла Сіроткі",
            "url": "https://www.nlb.by/content/news/national-library-of-belarus/420-let-chitaem-peregrinatsiyu-radzivilla-sirotki/"
        },
        {
            "title": "Collegium Hosianum — Wikipedia",
            "url": "https://pl.wikipedia.org/wiki/Collegium_Hosianum"
        }
    ],
    "tags": [
        "Польшча",
        "Бранева",
        "Вармія",
        "Радзівіл Сіротка",
        "Перэгрынацыя",
        "старадрукі",
        "езуіты",
        "culture"
    ],
    "personId": "radziwill-sirotka",
    "personIds": [
        "radziwill-sirotka"
    ],
    "mustSee": True,
    "unverifiedCoordinates": False
})

# Update radziwill-sirotka placeIds
sirotka = next((p for p in persons if p['id'] == 'radziwill-sirotka'), None)
if sirotka:
    if 'braniewo-jesuit-college-sirotka-peregrinatio' not in sirotka.get('placeIds', []):
        sirotka.setdefault('placeIds', []).append('braniewo-jesuit-college-sirotka-peregrinatio')

with open('data/places.json', 'w', encoding='utf-8') as f:
    json.dump(places, f, ensure_ascii=False, indent=2)
with open('data/places.js', 'w', encoding='utf-8') as f:
    f.write('// Albaruthenica Places Dataset\nwindow.INITIAL_PLACES = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

with open('data/persons.json', 'w', encoding='utf-8') as f:
    json.dump(persons, f, ensure_ascii=False, indent=2)
with open('data/persons.js', 'w', encoding='utf-8') as f:
    f.write('// Albaruthenica Persons Dataset\nwindow.INITIAL_PERSONS = ' + json.dumps(persons, ensure_ascii=False, indent=2) + ';\n')

print(f"Dataset updated! Places: {len(places)}, Persons: {len(persons)}")
