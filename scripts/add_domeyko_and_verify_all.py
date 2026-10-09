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

# 1. Montevideo Cathedral (Domeyko)
upsert_place({
    "id": "montevideo-cathedral-domeyko",
    "title": {
        "by": "Кафедральная базіліка Мантавідэа і запісы Ігната Дамейкі (1838)",
        "ru": "Кафедральная базилика Монтевидео и путевые заметки Игнатия Домейко (1838)",
        "en": "Metropolitan Cathedral of Montevideo & Ignacy Domeyko's Journal (1838)"
    },
    "category": "church",
    "country": {
        "by": "Уругвай",
        "ru": "Уругвай",
        "en": "Uruguay"
    },
    "city": {
        "by": "Мантавідэа",
        "ru": "Монтевидео",
        "en": "Montevideo"
    },
    "coordinates": [
        -34.9069,
        -56.2039
    ],
    "description": {
        "by": "Галоўны каталіцкі храм сталіцы Уругвая на плошчы Канстытуцыі (Plaza Constitución). 25 красавіка 1838 года паштовы карабель з Ігнацыем Дамейкам, які плыў з Еўропы ў Паўднёвую Амерыку, зрабіў прыпынак у Мантавідэа. Дамейка падрабязна апісаў горад і сабор у сваёй кнізе «Мае падарожжы»: «Адзіная аздоба гэтага горада — касцёл, адмыслова пабудаваны на галоўным пляцы. У гэтым касцёле бачыў некалькі прыгожых абразоў, а ўсе алтары чыстыя і старанна дагледжаныя...».",
        "ru": "Главный собор столицы Уругвая на площади Конституции. В апреле 1838 г. почтовый корабль с Игнатием Домейко зашел в порт Монтевидео. Домейко подробно описал город и собор в мемуарах «Мои путешествия», восхищаясь убранством его алтарей.",
        "en": "The mother church of Montevideo situated on Plaza Constitución. On April 25, 1838, the ship carrying Ignacy Domeyko from Europe to South America anchored in Montevideo. Domeyko vividly described the city and cathedral in his travel memoirs 'My Travels'."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Catedral_Metropolitana_de_Montevideo.jpg/960px-Catedral_Metropolitana_de_Montevideo.jpg",
    "links": [
        {
            "title": "Наша вера: Ігнат Дамейка. Мае падарожжы",
            "url": "https://media.catholic.by/nv/n20/art5.htm"
        },
        {
            "title": "Catedral Metropolitana de Montevideo — Wikipedia",
            "url": "https://es.wikipedia.org/wiki/Catedral_metropolitana_de_Montevideo"
        }
    ],
    "tags": [
        "Уругвай",
        "Мантавідэа",
        "Ігнат Дамейка",
        "сабор",
        "Мае падарожжы",
        "church"
    ],
    "personId": "ignacy-domeyko",
    "personIds": [
        "ignacy-domeyko"
    ],
    "mustSee": False,
    "unverifiedCoordinates": False
})

# 2. Buenos Aires - Plaza de Mayo / Cathedral (Domeyko)
upsert_place({
    "id": "buenos-aires-mayo-domeyko",
    "title": {
        "by": "Плошча Мая і прыбыццё Ігната Дамейкі ў Буэнас-Айрэс (1838)",
        "ru": "Пласа-де-Майо и прибытие Игнатия Домейко в Буэнос-Айрес (1838)",
        "en": "Plaza de Mayo & Arrival of Ignacy Domeyko in Buenos Aires (1838)"
    },
    "category": "historical",
    "country": {
        "by": "Аргенціна",
        "ru": "Аргентина",
        "en": "Argentina"
    },
    "city": {
        "by": "Буэнас-Айрэс",
        "ru": "Буэнос-Айрес",
        "en": "Buenos Aires"
    },
    "coordinates": [
        -34.6083,
        -58.3712
    ],
    "description": {
        "by": "Гістарычнае сэрца Буэнас-Айрэса, куды напрыканцы красавіка 1838 года ступіў Ігнат Дамейка пасля шматмесячнага акіянскага плавання з Францыі. Як занатаваў вучоны: «Ледзь толькі чалавек дакрануўся сухой зямлі, забыўся пра цяжкасці ды невыгоды плавання… Пайшоў сама перш падзякаваць Богу за шчасліва скончанае марское падарожжа…». Адсюль пачаўся легендарны пераход Дамейкі на мулах праз бязмежную аргенцінскую пампу і перавал у Андах да Чылі.",
        "ru": "Историческое сердце Буэнос-Айреса (Пласа-де-Майо и собор), куда в конце апреля 1838 года прибыл Игнатий Домейко после плавания через Атлантику. Отсюда начался его знаменитый переход через пампу и перевалы Анд в Чили.",
        "en": "Historic core of Buenos Aires (Plaza de Mayo and Metropolitan Cathedral) where Ignacy Domeyko set foot on the South American mainland in late April 1838 after his transatlantic voyage, before embarking on his mule trek across the Pampas and Andes to Chile."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Plaza_de_Mayo_Buenos_Aires_2013.jpg/960px-Plaza_de_Mayo_Buenos_Aires_2013.jpg",
    "links": [
        {
            "title": "Наша вера: Ігнат Дамейка. Мае падарожжы",
            "url": "https://media.catholic.by/nv/n20/art5.htm"
        }
    ],
    "tags": [
        "Аргенціна",
        "Буэнас-Айрэс",
        "Ігнат Дамейка",
        "Пласа дэ Мая",
        "падарожжа",
        "historical"
    ],
    "personId": "ignacy-domeyko",
    "personIds": [
        "ignacy-domeyko"
    ],
    "mustSee": False,
    "unverifiedCoordinates": False
})

# 3. Volcan Antuco & Araucania (Domeyko)
upsert_place({
    "id": "araucania-antuco-domeyko-expedition",
    "title": {
        "by": "Вулкан Антука і даследаванні Араўканіі Ігнатам Дамейкам",
        "ru": "Вулкан Антуко и исследования Араукании Игнатием Домейко",
        "en": "Volcán Antuco & Ignacy Domeyko's Araucanía Expedition"
    },
    "category": "historical",
    "country": {
        "by": "Чылі",
        "ru": "Чили",
        "en": "Chile"
    },
    "city": {
        "by": "Антука / Бія-Бія",
        "ru": "Антуко / Био-Био",
        "en": "Antuco / Biobío"
    },
    "coordinates": [
        -37.4000,
        -71.3500
    ],
    "description": {
        "by": "Вулкан у Кардыльерах (2979 м), на кратэр якога ў сакавіку 1845 года ўзняўся выбітны навуковец Ігнат Дамейка, апісаўшы яго геалогію і зрабіўшы падрабязныя малюнкі. У час сваёй гістарычнай экспедыцыі ў Араўканію Дамейка першым з еўрапейскіх навукоўцаў увайшоў у давер да карэннага народа мапучэ (араўканаў), вывучыў іх мову і звычаі і напісаў фундаментальную працу «Араўканія і яе жыхары» (1845), у якой гарача выступіў у абарону правоў індзейцаў перад урадам Чылі, выратаваўшы іх ад знішчэння.",
        "ru": "Стратовулкан в Андах (2979 м), на вершину которого в марте 1845 г. поднялся Игнатий Домейко. В ходе экспедиции по Араукании Домейко исследовал жизнь и язык индейцев мапуче, создав книгу «Араукания и её жители», предотвратившую войну на уничтожение коренных народов.",
        "en": "Stratovolcano in the Andes (2,979 m) ascended by scientist Ignacy Domeyko in March 1845. During his historic expedition into Araucanía, Domeyko gained the trust of the Mapuche people, authoring 'Araucanía and Its Inhabitants' (1845) which defended indigenous rights before the Chilean government and averted war."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Volcan_Antuco_Chile.jpg/960px-Volcan_Antuco_Chile.jpg",
    "links": [
        {
            "title": "Наша вера: Ігнат Дамейка. Мае падарожжы ў Араўканію",
            "url": "https://media.catholic.by/nv/n21/art11.htm"
        },
        {
            "title": "Volcán Antuco — Wikipedia",
            "url": "https://es.wikipedia.org/wiki/Volc%C3%A1n_Antuco"
        }
    ],
    "tags": [
        "Чылі",
        "Антука",
        "Араўканія",
        "Ігнат Дамейка",
        "мапучэ",
        "вулкан",
        "экспедыцыя",
        "historical"
    ],
    "personId": "ignacy-domeyko",
    "personIds": [
        "ignacy-domeyko"
    ],
    "mustSee": True,
    "unverifiedCoordinates": False
})

# Update ignacy-domeyko placeIds
domeyko = next((p for p in persons if p['id'] == 'ignacy-domeyko'), None)
if domeyko:
    for pid in ['montevideo-cathedral-domeyko', 'buenos-aires-mayo-domeyko', 'araucania-antuco-domeyko-expedition']:
        if pid not in domeyko.get('placeIds', []):
            domeyko.setdefault('placeIds', []).append(pid)

with open('data/places.json', 'w', encoding='utf-8') as f:
    json.dump(places, f, ensure_ascii=False, indent=2)
with open('data/places.js', 'w', encoding='utf-8') as f:
    f.write('// Albaruthenica Places Dataset\nwindow.INITIAL_PLACES = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

with open('data/persons.json', 'w', encoding='utf-8') as f:
    json.dump(persons, f, ensure_ascii=False, indent=2)
with open('data/persons.js', 'w', encoding='utf-8') as f:
    f.write('// Albaruthenica Persons Dataset\nwindow.INITIAL_PERSONS = ' + json.dumps(persons, ensure_ascii=False, indent=2) + ';\n')

print(f"Dataset updated! Places: {len(places)}, Persons: {len(persons)}")
