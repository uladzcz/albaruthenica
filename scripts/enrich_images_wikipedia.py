import json
import urllib.request
import urllib.parse
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Load places and persons
with open('data/places.json', 'r', encoding='utf-8') as f:
    places = json.load(f)
with open('data/persons.json', 'r', encoding='utf-8') as f:
    persons = json.load(f)

# Direct verified images for key requested sites
VERIFIED_IMAGES = {
    "jan-bulhak": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Jan_Bu%C5%82hak._%D0%AF%D0%BD_%D0%91%D1%83%D0%BB%D0%B3%D0%B0%D0%BA_%281935%29.jpg/440px-Jan_Bu%C5%82hak._%D0%AF%D0%BD_%D0%91%D1%83%D0%BB%D0%B3%D0%B0%D0%BA_%281935%29.jpg",
    "czeslaw-niemen": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Czes%C5%82aw_Niemen.png/440px-Czes%C5%82aw_Niemen.png",
    "tadeusz-dolega-mostowicz": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Tadeusz_Do%C5%82%C4%99ga-Mostowicz_Polish_writer.jpg/440px-Tadeusz_Do%C5%82%C4%99ga-Mostowicz_Polish_writer.jpg",
    "mieczyslaw-karlowicz": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Mieczys%C5%82aw_Kar%C5%82owicz_big.PNG/440px-Mieczys%C5%82aw_Kar%C5%82owicz_big.PNG",
    "antoni-edward-odyniec": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Antoni_Edward_Odyniec_foto_%28cropped%29.jpg/440px-Antoni_Edward_Odyniec_foto_%28cropped%29.jpg",
    "zofia-chometowska": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Zofia_Chom%C4%99towska_%28lata_1930%29.jpg/440px-Zofia_Chom%C4%99towska_%28lata_1930%29.jpg",
    "tadeusz-korzon": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Tadeusz_Korzon.png/440px-Tadeusz_Korzon.png",
    "trakai-uzutrakis-tyszkiewicz-palace": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Uzutrakis_Palace_2015_01.jpg/960px-Uzutrakis_Palace_2015_01.jpg",
    "lentvaris-tyszkiewicz-palace": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Lentvario_dvaras%2C_2024_vasaris_%282%29.jpg/960px-Lentvario_dvaras%2C_2024_vasaris_%282%29.jpg",
    "vilnia-glaubitz-st-johns": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Vilnius%2C_gate_of_the_Basilian_monastery_of_the_Holy_Trinity.jpg/960px-Vilnius%2C_gate_of_the_Basilian_monastery_of_the_Holy_Trinity.jpg",
    "braniewo-jesuit-college-sirotka-peregrinatio": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Kolegium_Jezuit%C3%B3w_w_Braniewie_%28Collegium_Hosianum%29.jpg/960px-Kolegium_Jezuit%C3%B3w_w_Braniewie_%28Collegium_Hosianum%29.jpg",
    "bielsk-podlaski-szkola-3-hajduk": "",
    "bialystok-skver-tamary-salanevich": "",
    "studziwody-muzej-maloj-backauszcyny": "",
    "grabarka-sviataya-hara": "https://upload.wikimedia.org/wikipedia/commons/2/2a/Transfiguration_of_Jesus_Christ_church_in_Grabarka_-_exterior_%281%29.jpg"
}

# Update persons
for per in persons:
    if per['id'] in VERIFIED_IMAGES:
        per['image'] = VERIFIED_IMAGES[per['id']]

# Update places
for pl in places:
    if pl['id'] in VERIFIED_IMAGES:
        pl['image'] = VERIFIED_IMAGES[pl['id']]

    # Specific fix for Stare Powązki items
    if pl['id'] == 'warsaw-cmentarz-powazkowski-stare-powazki':
        for it in pl.get('items', []):
            if 'Немена' in it.get('title', ''):
                it['image'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/PL_Warsaw_Stare_Pow%C4%85zki_czeslaw_niemen_2.jpg/960px-PL_Warsaw_Stare_Pow%C4%85zki_czeslaw_niemen_2.jpg'
            elif 'Булгака' in it.get('title', ''):
                it['image'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Jan_Bu%C5%82hak_-_gr%C3%B3b.jpg/960px-Jan_Bu%C5%82hak_-_gr%C3%B3b.jpg'
            elif 'Мастовіча' in it.get('title', ''):
                it['image'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Tadeusz_Do%C5%82%C4%99ga-Mostowicz_Polish_writer.jpg/960px-Tadeusz_Do%C5%82%C4%99ga-Mostowicz_Polish_writer.jpg'
            elif 'Карловіча' in it.get('title', ''):
                it['image'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Mieczys%C5%82aw_Kar%C5%82owicz_-_gr%C3%B3b.jpg/960px-Mieczys%C5%82aw_Kar%C5%82owicz_-_gr%C3%B3b.jpg'
            elif 'Адынца' in it.get('title', ''):
                it['image'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Antoni_Edward_Odyniec_-_gr%C3%B3b.jpg/960px-Antoni_Edward_Odyniec_-_gr%C3%B3b.jpg'
            elif 'Хамянтоўскай' in it.get('title', ''):
                it['image'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Zofia_Chom%C4%99towska_%28lata_1930%29.jpg/960px-Zofia_Chom%C4%99towska_%28lata_1930%29.jpg'
            elif 'Корзана' in it.get('title', ''):
                it['image'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Tadeusz_Korzon.png/960px-Tadeusz_Korzon.png'

# 2. Add Bologna and Radziwiłł personalities
existing_person_ids = {p['id'] for p in persons}
if 'aleksandr-lyudvik-radziwill' not in existing_person_ids:
    persons.append({
        "id": "aleksandr-lyudvik-radziwill",
        "name": {
            "by": "Аляксандр Людвік Радзівіл",
            "ru": "Александр Людвик Радзивилл",
            "en": "Aleksander Ludwik Radziwiłł"
        },
        "dates": "1594–1654",
        "role": {
            "by": "Маршалак вялікі літоўскі, ваявода полацкі і берасцейскі",
            "ru": "Маршалок великий литовский, воевода полоцкий",
            "en": "Grand Marshal of Lithuania, Voivode of Polotsk"
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Alaksandar_Ludvik_Radzivill._%D0%90%D0%BB%D1%8F%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%9B%D1%8E%D0%B4%D0%B2%D1%96%D0%BA_%D0%A0%D0%B0%D0%B4%D0%B7%D1%96%D0%B2%D1%96%D0%BB_%28XVII%29_%282%29.jpg/330px-Alaksandar_Ludvik_Radzivill._%D0%90%D0%BB%D1%8F%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%9B%D1%8E%D0%B4%D0%B2%D1%96%D0%BA_%D0%A0%D0%B0%D0%B4%D0%B7%D1%96%D0%B2%D1%96%D0%BB_%28XVII%29_%282%29.jpg",
        "bio": {
            "by": "Дзяржаўны і ваенны дзеяч ВКЛ, сын Мікалая Крыштафа Радзівіла Сіроткі. Вучыўся ў Еўропе, займаў найвышэйшыя пасады ў дзяржаве. Памёр у Балонні ў 1654 годзе.",
            "ru": "Государственный и военный деятель ВКЛ, сын Николая Криштофа Радзивилла Сиротки. Скончался в Болонье в 1654 году.",
            "en": "Statesman of the Grand Duchy of Lithuania, son of Mikołaj Krzysztof 'the Orphan' Radziwiłł. Died in Bologna in 1654."
        },
        "placeIds": ["bologna-archiginnasio-university"]
    })

if 'michal-kazimir-radziwill' not in existing_person_ids:
    persons.append({
        "id": "michal-kazimir-radziwill",
        "name": {
            "by": "Міхал Казімір Радзівіл",
            "ru": "Михаил Казимир Радзивилл",
            "en": "Michał Kazimierz Radziwiłł"
        },
        "dates": "1635–1680",
        "role": {
            "by": "Падканцлер вялікі літоўскі, гетман польны літоўскі",
            "ru": "Подканцлер великий литовский, гетман польный литовский",
            "en": "Sub-Chancellor and Field Hetman of the Grand Duchy of Lithuania"
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Micha%C5%82_Kazimierz_Radziwi%C5%82%C5%82.PNG/330px-Micha%C5%82_Kazimierz_Radziwi%C5%82%C5%82.PNG",
        "bio": {
            "by": "Выбітны дзяржаўны і ваенны дзеяч ВКЛ, сын Аляксандра Людвіка Радзівіла. Абаронца краіны ў войнах XVII стагоддзя, мецэнат і будаўнік. Памёр у Балонні ў 1680 годзе.",
            "ru": "Выдающийся государственный и военный деятель ВКЛ, подканцлер и польный гетман. Скончался в Болонье в 1680 году.",
            "en": "Sub-Chancellor and Field Hetman of Lithuania, prominent military leader and patron. Died in Bologna in 1680."
        },
        "placeIds": ["bologna-archiginnasio-university"]
    })

# Add Bologna place if not present
existing_place_ids = {p['id'] for p in places}
if 'bologna-archiginnasio-university' not in existing_place_ids:
    places.append({
        "id": "bologna-archiginnasio-university",
        "title": {
            "by": "Балонскі ўніверсітэт і палац Архігімназія",
            "ru": "Болонский университет и дворец Архигимназия",
            "en": "University of Bologna & Archiginnasio Palace"
        },
        "category": "culture",
        "country": {
            "by": "Італія",
            "ru": "Италия",
            "en": "Italy"
        },
        "city": {
            "by": "Балоння",
            "ru": "Болонья",
            "en": "Bologna"
        },
        "coordinates": [
            44.4925,
            11.3433
        ],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Bologna-archiginnasio-cortile.jpg/960px-Bologna-archiginnasio-cortile.jpg",
        "description": {
            "by": "Найстарэйшы ўніверсітэт Еўропы (заснаваны ў 1088 г.) і яго гістарычная рэзідэнцыя — Палац Архігімназія (Palazzo dell'Archiginnasio, 1563 г.). Пачынаючы з Адраджэння тут навучаліся ліцвіны — шляхта і інтэлектуалы з беларускіх земляў ВКЛ (Мікалай Сапега, прадстаўнікі родаў Радзівілаў, Хадкевічаў, Валовічаў), на сценах унутранага двара і заляў захаваліся іх гістарычныя гербы. Таксама ў Балонні завяршыўся жыццёвы шлях двух выбітных магнатаў ВКЛ: тут памёр маршалак вялікі літоўскі і ваявода полацкі Аляксандр Людвік Радзівіл (1654 г.), а таксама яго сын — падканцлер і гетман польны літоўскі Міхал Казімір Радзівіл (1680 г.).",
            "ru": "Старейший университет Европы (1088 г.) и его резиденция — дворец Архигимназия (1563 г.). Здесь обучались выходцы из ВКЛ (Сапеги, Радзивиллы, Ходкевичи), в залах сохранились их гербы. В Болонье скончались два видных магната ВКЛ: Александр Людвик Радзивилл (1654 г.) и Михаил Казимир Радзивилл (1680 г.).",
            "en": "The oldest university in the world (founded 1088) and its historic seat, Palazzo dell'Archiginnasio (1563). For centuries, Lithuanian-Belarusian nobility studied here (Sapiehas, Radziwiłłs), leaving their heraldic crests on the walls. Bologna was also the place of death of Grand Marshal Aleksander Ludwik Radziwiłł (1654) and Field Hetman Michał Kazimierz Radziwiłł (1680)."
        },
        "links": [
            {
                "title": "Вікіпедыя: Балонскі ўніверсітэт",
                "url": "https://be.wikipedia.org/wiki/Балонскі_ўніверсітэт"
            },
            {
                "title": "Вікіпедыя: Аляксандр Людвік Радзівіл",
                "url": "https://be.wikipedia.org/wiki/Аляксандр_Людвік_Радзівіл"
            },
            {
                "title": "Вікіпедыя: Міхал Казімір Радзівіл",
                "url": "https://be.wikipedia.org/wiki/Міхал_Казімір_Радзівіл"
            }
        ],
        "tags": [
            "Італія",
            "Балоння",
            "універсітэт",
            "Радзівілы",
            "Сапегі",
            "ВКЛ",
            "адукацыя"
        ],
        "personIds": [
            "aleksandr-lyudvik-radziwill",
            "michal-kazimir-radziwill"
        ],
        "mustSee": True
    })

# Save places and persons
with open('data/places.json', 'w', encoding='utf-8') as f:
    json.dump(places, f, ensure_ascii=False, indent=2)

with open('data/places.js', 'w', encoding='utf-8') as f:
    f.write('window.INITIAL_PLACES = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

with open('data/persons.json', 'w', encoding='utf-8') as f:
    json.dump(persons, f, ensure_ascii=False, indent=2)

with open('data/persons.js', 'w', encoding='utf-8') as f:
    f.write('window.INITIAL_PERSONS = ' + json.dumps(persons, ensure_ascii=False, indent=2) + ';\n')

print("Updated verified images and Bologna successfully!")
