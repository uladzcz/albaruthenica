import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

# Load files
with open('data/places.json', 'r', encoding='utf-8') as f:
    places = json.load(f)
with open('data/persons.json', 'r', encoding='utf-8') as f:
    persons = json.load(f)

# 1. Update vilnia-kvatera-paznyaka
paznyak_place = next((p for p in places if p['id'] == 'vilnia-kvatera-paznyaka'), None)
if paznyak_place:
    paznyak_place['personId'] = 'yanka-paznyak'
    paznyak_place['personIds'] = ['yanka-paznyak']
    paznyak_place['title']['ru'] = 'Квартира Янки Позняка'
    paznyak_place['title']['en'] = 'Apartment of Yanka Paznyak'
    paznyak_place['description']['ru'] = 'Адрес: Liejyklos, 1.\n\nВ доме, во дворе которого размещалась типография им. Ф. Скорины, находился книжный магазин «Пагоня» и жил один из лидеров белорусского христианско-демократического движения Янка Позняк.'
    paznyak_place['description']['en'] = 'Address: Liejyklos, 1.\n\nIn the building where the F. Skaryna printing house was located in the courtyard, there was the Pahonia bookstore and the residence of Yanka Paznyak, one of the leaders of the Belarusian Christian Democratic movement.'
    print('Updated vilnia-kvatera-paznyaka')

# 2. Update vilnia-drukarnya-imya-f-skaryny-1926-30
druk_1926 = next((p for p in places if p['id'] == 'vilnia-drukarnya-imya-f-skaryny-1926-30'), None)
if druk_1926:
    druk_1926['personId'] = 'yanka-paznyak'
    druk_1926['personIds'] = ['yanka-paznyak']
    print('Updated vilnia-drukarnya-imya-f-skaryny-1926-30')

# 3. Update vilnia-drukarnya-imya-f-skaryny-1930-36
druk_1930 = next((p for p in places if p['id'] == 'vilnia-drukarnya-imya-f-skaryny-1930-36'), None)
if druk_1930:
    druk_1930['personId'] = None
    druk_1930['personIds'] = []
    print('Updated vilnia-drukarnya-imya-f-skaryny-1930-36')

# 4. Remove these from francysk-skaryna
skaryna = next((p for p in persons if p['id'] == 'francysk-skaryna'), None)
if skaryna:
    skaryna['placeIds'] = [pid for pid in skaryna['placeIds'] if pid not in ['vilnia-kvatera-paznyaka', 'vilnia-drukarnya-imya-f-skaryny-1926-30', 'vilnia-drukarnya-imya-f-skaryny-1930-36']]
    print('Cleaned Skaryna placeIds. New count:', len(skaryna['placeIds']))

# 5. Add yanka-paznyak to persons
paznyak_person = {
    'id': 'yanka-paznyak',
    'name': {
        'by': 'Янка Пазняк',
        'ru': 'Янка Позняк',
        'en': 'Yanka Paznyak'
    },
    'dates': '1887 — ~1940',
    'role': {
        'by': 'Грамадска-палітычны дзеяч, публіцыст, выдавец, дзед Зянона Пазняка',
        'ru': 'Общественно-политический деятель, публицист, издатель, дед Зенона Позняка',
        'en': 'Socio-political activist, publisher, journalist, grandfather of Zianon Pazniak'
    },
    'bio': {
        'by': 'Ураджэнец мястэчка Самаравічы Ваўкавыскага павета. Выбітны дзеяч беларускага хрысціянска-дэмакратычнага руху на Віленшчыне і ў міжваеннай Польшчы, старшыня Беларускай хрысціянскай дэмакратыі (з 1936 г.), рэдактар газеты «Biełaruskaja krynica» і часопіса «Хрысьціянская думка». Жыў і кіраваў выдавецтвам у Вільні па вул. Liejyklos, 1. У кастрычніку 1939 г. арыштаваны органамі НКУС, загінуў у зняволенні.',
        'ru': 'Уроженец Волковысского уезда. Выдающийся деятель белорусского христианско-демократического движения в Вильне и межвоенной Польше, председатель Белорусской христианской демократии (с 1936 г.), редактор газеты «Biełaruskaja krynica» и журнала «Хрысьціянская думка». Жил и руководил издательской деятельностью в Вильнюсе на ул. Liejyklos, 1. В октябре 1939 г. арестован органами НКВД, погиб в заключении. Дед Зенона Позняка.',
        'en': 'Born in the Vawkavysk district. Leading figure of the Belarusian Christian democratic movement in Vilnius and interwar Poland, chairman of Belarusian Christian Democracy (from 1936), editor of Biełaruskaja krynica and Chryscijanskaja Dumka. Lived and ran publishing operations at Liejyklos 1 in Vilnius. Arrested by the NKVD in October 1939 and died in Soviet custody. Grandfather of Zianon Pazniak.'
    },
    'image': 'https://upload.wikimedia.org/wikipedia/commons/f/f2/Jan_Po%C5%BAniak.png',
    'wiki': 'https://be.wikipedia.org/wiki/Ян_Пазняк',
    'placeIds': [
        'vilnia-kvatera-paznyaka',
        'vilnia-drukarnya-imya-f-skaryny-1926-30'
    ]
}

# Check if already present
existing_paznyak = next((p for p in persons if p['id'] == 'yanka-paznyak'), None)
if existing_paznyak:
    persons.remove(existing_paznyak)
persons.append(paznyak_person)
print('Added yanka-paznyak to persons list')

# Save all 4 files
with open('data/places.json', 'w', encoding='utf-8') as f:
    json.dump(places, f, ensure_ascii=False, indent=2)
with open('data/places.js', 'w', encoding='utf-8') as f:
    f.write('// Albaruthenica Places Dataset\nwindow.INITIAL_PLACES = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

with open('data/persons.json', 'w', encoding='utf-8') as f:
    json.dump(persons, f, ensure_ascii=False, indent=2)
with open('data/persons.js', 'w', encoding='utf-8') as f:
    f.write('// Albaruthenica Persons Dataset\nwindow.INITIAL_PERSONS = ' + json.dumps(persons, ensure_ascii=False, indent=2) + ';\n')

print('All 4 data files updated successfully!')
