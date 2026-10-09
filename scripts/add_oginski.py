import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

with open('data/persons.json', 'r', encoding='utf-8') as f:
    persons = json.load(f)

oginski = {
    "id": "michal-kazimir-oginski",
    "name": {
        "by": "Міхал Казімір Агінскі",
        "ru": "Михаил Казимир Огинский",
        "en": "Michał Kazimierz Ogiński"
    },
    "dates": "1728 — 1800",
    "role": {
        "by": "Вялікі гетман літоўскі, кампазітар, мецэнат, паэт, стваральнік Агінскага канала і Слонімскага тэатра",
        "ru": "Великий гетман литовский, композитор, меценат, создатель Огинского канала и Слонимского театра",
        "en": "Grand Hetman of Lithuania, composer, patron of arts, builder of the Oginski Canal and Slonim Theater"
    },
    "bio": {
        "by": "Выбітны дзяржаўны дзеяч ВКЛ, паэт, музыкант і асветнік. Ператварыў сваю рэзідэнцыю ў Слоніме ў «Палескія Афіны» з адным з найбуйнейшых у Еўропе прыдворных тэатраў і сімфанічным аркестрам. Збудаваў знакаміты Агінскі канал, які злучыў басейны Балтыйскага і Чорнага мораў. Шмат падарожнічаў па Італіі і Еўропе, вывучаючы опернае мастацтва і механіку.",
        "ru": "Выдающийся государственный деятель ВКЛ, композитор, меценат. Превратил Слоним в культурную столицу края («Полесские Афины») с великолепным оперным театром. Построил Огинский канал, соединивший Балтийское и Черное моря. Путешествовал по Италии, в том числе посещал Флоренцию.",
        "en": "Grand Hetman of Lithuania, composer, writer, and Renaissance man. Transformed Slonim into a vibrant cultural hub ('Athens of Polesia') with an opera house and orchestra. Financed the construction of the Oginski Canal connecting the Baltic and Black Sea basins. Traveled extensively across Italy, including Florence."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Micha%C5%82_Kazimierz_Ogi%C5%84ski.jpg/330px-Micha%C5%82_Kazimierz_Ogi%C5%84ski.jpg",
    "wiki": "https://be.wikipedia.org/wiki/Міхал_Казімір_Агінскі",
    "placeIds": ["florence-city-hub"]
}

existing = next((p for p in persons if p['id'] == oginski['id']), None)
if existing:
    existing.update(oginski)
else:
    persons.append(oginski)

with open('data/persons.json', 'w', encoding='utf-8') as f:
    json.dump(persons, f, ensure_ascii=False, indent=2)
with open('data/persons.js', 'w', encoding='utf-8') as f:
    f.write('// Albaruthenica Persons Dataset\nwindow.INITIAL_PERSONS = ' + json.dumps(persons, ensure_ascii=False, indent=2) + ';\n')

print(f"Added Oginski! Total persons: {len(persons)}")
