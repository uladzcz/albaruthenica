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
    "id": "istanbul-city-hub",
    "title": {
        "by": "Стамбул (Канстанцінопаль) — беларускія сляды (комплексны аб’ект)",
        "ru": "Стамбул (Константинополь) — белорусские следы (комплексный объект)",
        "en": "Istanbul (Constantinople) — Belarusian Footprints (City Hub)"
    },
    "category": "city",
    "country": {
        "by": "Турцыя",
        "ru": "Турция",
        "en": "Turkey"
    },
    "city": {
        "by": "Стамбул",
        "ru": "Стамбул",
        "en": "Istanbul"
    },
    "coordinates": [
        41.0082,
        28.9784
    ],
    "description": {
        "by": "Гістарычная сталіца Асманскай імперыі і Візантыі, цесна звязаная з лёсамі выбітных ураджэнцаў Беларусі. Тут правёў апошнія месяцы жыцця і памёр паэт Адам Міцкевіч, а ў 1919–1921 гг. дзейнічала Надзвычайная дыпламатычная місія Беларускай Народнай Рэспублікі (БНР), якая ратавала беларускіх вайскоўцаў і эмігрантаў і вяла дыпламатычныя перамовы. Таксама тут у 1582 г. бываў князь Мікалай Крыштаф Радзівіл «Сіротка».",
        "ru": "Исторический центр Османской империи на Босфоре. Здесь провел последние дни и скончался великий поэт Адам Мицкевич. В 1919–1921 годах в Константинополе действовала Дипломатическая миссия Белорусской Народной Республики (БНР), выдававшая паспорта соотечественникам и защищавшая их интересы.",
        "en": "Historic metropolis on the Bosphorus with deep ties to Belarusian history. Here poet Adam Mickiewicz spent his final days and passed away in 1855. In 1919–1921, it hosted the Extraordinary Diplomatic Mission of the Belarusian Democratic Republic (BNR), issuing passports and representing Belarus."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Bosphorus_Bridge_Istanbul.jpg/960px-Bosphorus_Bridge_Istanbul.jpg",
    "links": [
        {
            "title": "Дыпламатычныя прадстаўніцтвы БНР — Вікіпедыя",
            "url": "https://be.wikipedia.org/wiki/Дыпламатычныя_прадстаўніцтвы_БНР"
        },
        {
            "title": "Музей Адама Міцкевіча ў Стамбуле — Вікіпедыя",
            "url": "https://be.wikipedia.org/wiki/Музей_Адама_Міцкевіча_(Стамбул)"
        }
    ],
    "tags": [
        "Турцыя",
        "Стамбул",
        "Канстанцінопаль",
        "БНР",
        "Міцкевіч",
        "дыпламатыя",
        "комплексны аб’ект",
        "city"
    ],
    "personId": "adam-mickiewicz",
    "personIds": [
        "adam-mickiewicz",
        "radziwill-sirotka"
    ],
    "mustSee": True,
    "unverifiedCoordinates": False,
    "isCityHub": True,
    "items": [
        {
            "id": "istanbul-mickiewicz-museum",
            "title": "Дом-музей Адама Міцкевіча ў раёне Тарлабашы (Бейаглу)",
            "person": "Адам Міцкевіч",
            "personId": "adam-mickiewicz",
            "year": "1855 г.",
            "description": "Будынак на рагу вуліц Serdar-ı Ekrem і Tatlı Badem Sokak, дзе паэт Адам Міцкевіч правёў апошнія тыдні жыцця і раптоўна памёр 26 лістапада 1855 года, фармаваўшы атрады польскіх і казацкіх добраахвотнікаў у час Крымскай вайны. Цяпер тут дзейнічае мемарыяльны музей і сімвалічны склеп паэта.",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Adam_Mickiewicz_Museum_Istanbul.jpg/800px-Adam_Mickiewicz_Museum_Istanbul.jpg",
            "wikiUrl": "https://be.wikipedia.org/wiki/Музей_Адама_Міцкевіча_(Стамбул)",
            "needsCoords": False
        },
        {
            "id": "istanbul-bnr-diplomatic-mission",
            "title": "Дыпламатычная місія БНР у Канстанцінопалі (1919–1921)",
            "person": "Дзеячы БНР",
            "year": "1919–1921 гг.",
            "description": "Афіцыйнае дыпламатычнае прадстаўніцтва Беларускай Народнай Рэспублікі ў Асманскай імперыі. Місію ўзначальвалі палкоўнік Аляксандр Чарнушэвіч і князь Павел Шастакоў-Валадарскі. Прадстаўніцтва выдавала беларускія пашпарты грамадзянам БНР, ратавала ад выдачы бальшавікам сотні беларускіх уцекачоў і вайскоўцаў арміі Булак-Балаховіча і вяло перамовы з вярхоўнымі камісарамі Антанты. Дакладны адрас будынка місіі (у раёне Пера / Бейаглу) знаходзіцца ў стадыі архіўнага вывучэння.",
            "wikiUrl": "https://be.wikipedia.org/wiki/Дыпламатычныя_прадстаўніцтвы_БНР",
            "needsCoords": True,
            "coordsRequest": True
        }
    ]
})

with open('data/places.json', 'w', encoding='utf-8') as f:
    json.dump(places, f, ensure_ascii=False, indent=2)
with open('data/places.js', 'w', encoding='utf-8') as f:
    f.write('// Albaruthenica Places Dataset\nwindow.INITIAL_PLACES = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

print(f"Istanbul Hub added! Total places: {len(places)}")
