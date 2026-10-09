# -*- coding: utf-8 -*-
"""
Add Bulak-Balachowicz memorial plaque in Warsaw (Saska Kępa)
and verify/update exact coordinates for:
- Warsaw Belarusian House (Wiejska 13/3)
- Foksal 3/5 Palace (Magdalena Radziwill / Bourbon)
"""

import json

def run():
    with open('data/places.json', 'r', encoding='utf-8') as f:
        places = json.load(f)

    with open('data/persons.json', 'r', encoding='utf-8') as f:
        persons = json.load(f)

    # 1. Update Warsaw Belarusian House coordinates (Wiejska 13/3)
    for p in places:
        if p['id'] == 'warsaw-belarusian-house':
            p['coordinates'] = [52.22640, 21.02500]
            p['unverifiedCoordinates'] = False
            print('Updated warsaw-belarusian-house coordinates to [52.22640, 21.02500]')

    # 2. Update Foksal Palace coordinates (Foksal 3/5)
    for p in places:
        if p['id'] == 'warsaw-foksal-palace-bourbon':
            p['coordinates'] = [52.23396, 21.02341]
            p['unverifiedCoordinates'] = False
            print('Updated warsaw-foksal-palace-bourbon coordinates to [52.23396, 21.02341]')

    # 3. Add Bulak-Balachowicz memorial plaque (Paryska 27, Saska Kępa)
    plaque_id = 'warsaw-bulak-balachowicz-plaque'
    existing_ids = {p['id'] for p in places}
    if plaque_id not in existing_ids:
        new_plaque = {
            "id": plaque_id,
            "title": {
                "by": "Мемарыяльная дошка генералу Станіславу Булак-Балаховічу ў Варшаве",
                "ru": "Мемориальная доска генералу Станиславу Булак-Балаховичу в Варшаве",
                "en": "Memorial Plaque to General Stanisław Bułak-Bałachowicz in Warsaw"
            },
            "category": "plaque",
            "country": {
                "by": "Польшча",
                "ru": "Польша",
                "en": "Poland"
            },
            "city": {
                "by": "Варшава",
                "ru": "Варшава",
                "en": "Warsaw"
            },
            "coordinates": [52.22909, 21.05723],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/POL_Bulak_Balachowicz_plaque%2C_Warsaw_01.jpg/960px-POL_Bulak_Balachowicz_plaque%2C_Warsaw_01.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Станіслаў_Нікадзімавіч_Булак-Балаховіч",
            "source": "https://www2.polskieradio.pl/eo/print.aspx?iid=107917",
            "personIds": ["stanislaw-bulak-balachowicz"],
            "description": {
                "by": "Памятная шыльда генералу Станіславу Булак-Балаховічу на будынку Праваслаўнай духоўнай семінарыі на вул. Парыжскай, 27 (Саска Кэмпа) у Варшаве. Усталявана недалёка ад месца, дзе 10 мая 1940 года легендарны беларускі вайскавод і камандзір Палескага паходу загінуў у сутычцы з гестапаўцамі. Месца рэгулярных акцый памяці беларускай грамады.",
                "ru": "Памятная доска генералу Станиславу Булак-Балаховичу на здании Православной семинарии на ул. Парижской, 27 (Саска Кемпа) в Варшаве, недалеко от места его гибели в бою с гестапо 10 мая 1940 г.",
                "en": "Memorial plaque commemorating General Stanisław Bułak-Bałachowicz on the Orthodox Seminary building at Paryska 27 (Saska Kępa) in Warsaw, near where he was killed by the Gestapo on May 10, 1940."
            },
            "tags": ["балаховіч", "варшава", "бнр", "дошка", "саска-кэмпа", "памяць"]
        }
        places.append(new_plaque)
        print(f"Added {plaque_id}")

    # 4. Link plaque to person stanislaw-bulak-balachowicz
    for pers in persons:
        if pers['id'] == 'stanislaw-bulak-balachowicz':
            pls = set(pers.get('placeIds', []))
            pls.add(plaque_id)
            pers['placeIds'] = sorted(list(pls))

    # 5. Save all
    with open('data/places.json', 'w', encoding='utf-8') as f:
        json.dump(places, f, ensure_ascii=False, indent=2)
    with open('data/places.js', 'w', encoding='utf-8') as f:
        f.write('window.INITIAL_PLACES = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

    with open('data/persons.json', 'w', encoding='utf-8') as f:
        json.dump(persons, f, ensure_ascii=False, indent=2)
    with open('data/persons.js', 'w', encoding='utf-8') as f:
        f.write('window.INITIAL_PERSONS = ' + json.dumps(persons, ensure_ascii=False, indent=2) + ';\n')

    print('Saved places and persons successfully!')

if __name__ == '__main__':
    run()
