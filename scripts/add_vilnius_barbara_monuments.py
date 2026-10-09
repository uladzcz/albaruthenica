import json

def main():
    with open('data/places.json', 'r', encoding='utf-8') as f:
        places = json.load(f)

    with open('data/persons.json', 'r', encoding='utf-8') as f:
        persons = json.load(f)

    new_places = [
        {
            "id": "vilnius-monument-sigismund-barbara-radziwill",
            "title": {
                "by": "Помнік Жыгімонту Аўгусту і Барбары Радзівіл («Жыгімонт і Барбара»)",
                "ru": "Памятник Сигизмунду Августу и Барбаре Радзивилл («Сигизмунд и Барбара»)",
                "en": "Monument to Sigismund Augustus & Barbara Radziwill ('Sigismund & Barbara')"
            },
            "category": "monument",
            "country": {
                "by": "Літва",
                "ru": "Литва",
                "en": "Lithuania"
            },
            "city": {
                "by": "Вільня",
                "ru": "Вильнюс",
                "en": "Vilnius"
            },
            "coordinates": [54.6882, 25.2880],
            "description": {
                "by": "Адкрыты 10 верасня 2026 г. у двары Бібліятэкі імя Урублеўскіх Акадэміі навук Літвы (палац Клеменціны Тышкевіч). Скульптар Гядзімінас Пякурас і архітэктарка Аўшра Гвільдзене стварылі глыбока сімвалічную кампазіцыю: два залатыя чарапы — дакладныя анатамічныя копіі сапраўдных чарапоў Жыгімонта Аўгуста і Барбары Радзівіл, выяўленых у каралеўскай крыпце Віленскай кафедры пасля паводкі 1931 г. Кампазіцыя размешчана ў гістарычным раёне Пушкарні, дзе ў XVI ст. знаходзіўся палац Радзівілаў, адкуль цераз раку Вільню вёў таемны мост для спатканняў караля з Барбарай.",
                "ru": "Открыт 10 сентября 2026 г. во дворе Библиотеки имени Врублевских (дворец Клементины Тышкевич). Скульптор Гедиминас Пекурас и архитектор Аушра Гвильдзене создали концептуальный монумент: два золотых черепа — анатомические копии подлинных черепов короля Сигизмунда Августа и Барбары Радзивилл из виленской крипты. Памятник установлен в историческом районе Пушкарни, где стоял дворец Радзивиллов и тайный мост свиданий пары.",
                "en": "Unveiled on September 10, 2026, in the courtyard of the Wroblewski Library (Clementina Tyszkiewicz Palace). Sculptor Gediminas Piekuras and architect Aušra Gvildienė created a conceptual monument featuring two golden skulls — exact anatomical replicas of the skulls of King Sigismund II Augustus and Queen Barbara Radziwill discovered in the Vilnius Cathedral crypt after the 1931 flood. Located where the 16th-century Radziwill palace and secret lovers' bridge once stood."
            },
            "image": "",
            "links": [
                {
                    "title": "Наша Ніва: У Вільні адкрылі незвычайны помнік Жыгімонту Аўгусту і Барбары Радзівіл",
                    "url": "https://nashaniva.com/404473"
                },
                {
                    "title": "Барбара Радзівіл — Вікіпедыя",
                    "url": "https://be.wikipedia.org/wiki/Барбара_Радзівіл"
                }
            ],
            "tags": ["vilnius", "lithuania", "barbara-radziwill", "radziwill", "monument", "art", "sigismund"],
            "personId": "barbara-radziwill",
            "personIds": ["barbara-radziwill", "radziwills"],
            "unverifiedCoordinates": False,
            "mustSee": True
        },
        {
            "id": "vilnius-sculpture-barbara-radziwill-vokieciu",
            "title": {
                "by": "Скульптура Барбары Радзівіл на Нямецкай вуліцы",
                "ru": "Скульптура Барбары Радзивилл на Немецкой улице",
                "en": "Sculpture of Barbara Radziwill on Vokiečių Street"
            },
            "category": "monument",
            "country": {
                "by": "Літва",
                "ru": "Литва",
                "en": "Lithuania"
            },
            "city": {
                "by": "Вільня",
                "ru": "Вильнюс",
                "en": "Vilnius"
            },
            "coordinates": [54.6787, 25.2858],
            "description": {
                "by": "Класічная скульптура вялікай княгіні літоўскай і каралевы Барбары Радзівіл аўтарства выбітнага літоўскага скульптара Уладаса Вільджунаса, усталяваная ў 1982 годзе на пешаходнай Нямецкай вуліцы (Vokiečių g.). У савецкія часы афіцыйна забаранялася згадваць імя Барбары Радзівіл, таму скульптура праходзіла па дакументах як безыменны «дэкаратыўны гарадскі элемент». Сёння гэта адзін з пазнавальных сімвалаў Старога горада Вільні.",
                "ru": "Классическая городская скульптура великой княгини литовской и королевы Барбары Радзивилл работы литовского скульптора Владаса Вильджунаса, установленная в 1982 году на Немецкой улице (Vokiečių g.). В советское время имя королевы было под запретом, и монумент числился просто как «декоративный элемент».",
                "en": "Iconic city sculpture of Grand Duchess of Lithuania and Queen Barbara Radziwill by Lithuanian sculptor Vladas Vildžiūnas, erected in 1982 on pedestrian Vokiečių Street. In Soviet times, mentioning Barbara Radziwill was officially prohibited, so it was documented simply as a decorative element."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/4/47/Vladas_Vild%C5%BEi%C5%ABnas_%22Barbora%22.png",
            "links": [
                {
                    "title": "Наша Ніва: У Вільні адкрылі незвычайны помнік Жыгімонту Аўгусту і Барбары Радзівіл",
                    "url": "https://nashaniva.com/404473"
                },
                {
                    "title": "Барбара Радзівіл — Вікіпедыя",
                    "url": "https://be.wikipedia.org/wiki/Барбара_Радзівіл"
                }
            ],
            "tags": ["vilnius", "lithuania", "barbara-radziwill", "radziwill", "monument", "vildziunas", "vokieciu"],
            "personId": "barbara-radziwill",
            "personIds": ["barbara-radziwill", "radziwills"],
            "unverifiedCoordinates": False,
            "mustSee": False
        }
    ]

    for np in new_places:
        if not any(p['id'] == np['id'] for p in places):
            places.append(np)
            print("Added place:", np['id'])

    # Update barbara-radziwill in persons
    for pers in persons:
        if pers['id'] == 'barbara-radziwill':
            pids = set(pers.get('placeIds', []))
            pids.add("vilnius-monument-sigismund-barbara-radziwill")
            pids.add("vilnius-sculpture-barbara-radziwill-vokieciu")
            pers['placeIds'] = list(pids)
            print("Updated barbara-radziwill placeIds:", pers['placeIds'])
            break

    # Save persons.json and places.json
    with open('data/persons.json', 'w', encoding='utf-8') as f:
        json.dump(persons, f, ensure_ascii=False, indent=2)

    with open('data/places.json', 'w', encoding='utf-8') as f:
        json.dump(places, f, ensure_ascii=False, indent=2)

    # Sync places.js and persons.js
    with open('data/places.js', 'w', encoding='utf-8') as f:
        f.write('window.INITIAL_PLACES = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

    with open('data/persons.js', 'w', encoding='utf-8') as f:
        f.write('window.INITIAL_PERSONS = ' + json.dumps(persons, ensure_ascii=False, indent=2) + ';\n')

    print("Successfully synced. Total places:", len(places), "Total persons:", len(persons))

if __name__ == '__main__':
    main()
