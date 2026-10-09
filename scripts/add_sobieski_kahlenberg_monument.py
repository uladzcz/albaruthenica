import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update places.json with vienna-kahlenberg-sobieski-pedestal-monument
with open('data/places.json', 'r', encoding='utf-8') as f:
    places = json.load(f)

# Also ensure vienna-kahlenberg-st-joseph-sobieski has category 'church' and exact coords
for p in places:
    if p['id'] == 'vienna-kahlenberg-st-joseph-sobieski':
        p['category'] = 'church'
        p['coordinates'] = [48.275811, 16.334752]

monument_id = 'vienna-kahlenberg-sobieski-pedestal-monument'
places = [p for p in places if p['id'] != monument_id]

places.append({
    'id': monument_id,
    'title': {
        'by': 'Мемарыял Яна III Сабескага на гары Каленберг («Недапомнік» / Пастамент)',
        'ru': 'Мемориал Яна III Собеского на горе Каленберг («Недопамятник» / Постамент)',
        'en': 'John III Sobieski Memorial on Mount Kahlenberg (The Unfinished Monument Pedestal)'
    },
    'category': 'monument',
    'country': {
        'by': 'Аўстрыя',
        'ru': 'Австрия',
        'en': 'Austria'
    },
    'city': {
        'by': 'Вена',
        'ru': 'Вена',
        'en': 'Vienna'
    },
    'coordinates': [48.275562, 16.336768],
    'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Kahlenberg-Aussichtsterrasse.jpg/960px-Kahlenberg-Aussichtsterrasse.jpg',
    'wiki': 'https://be.wikipedia.org/wiki/Венская_бітва_(1683)',
    'description': {
        'by': 'Адрас: Am Kahlenberg, 1190 Wien, Аўстрыя (аглядная тэраса каля паркоўкі).\n\nГранітны пастамент на ўзгорку Каленберг над Венай — на гістарычным месцы бітвы 12 верасня 1683 года, адкуль 20-тысячная кавалерыя Рэчы Паспалітай і саюзнікаў на чале з каралём і вялікім князем літоўскім Янам III Сабескім нанесла сакрушальны ўдар па асманскім войску і выратавала горад ад аблогі.\n\nДа 335-й гадавіны бітвы (2018 г.) тут быў падрыхтаваны і ўзведзены пастамент пад 8-метровы бронзавы помнік Сабескаму аўтарства польскага скульптара Чэслава Дзвігая. Аднак венскі магістрат заблакаваў усталяванне статуі праз палітычныя спрэчкі, пакінуўшы пусты цокаль. Гэты «недапомнік» стаў сімвалам дыпламатычных спрэчак і рэгулярна прыцягвае грамадскія акцыі.',
        'ru': 'Адрес: Am Kahlenberg, 1190 Wien, Австрия.\n\nГранитный постамент на смотровой террасе горы Каленберг в Вене — на месте знаменитой Венской битвы 12 сентября 1683 года, где конница Речи Посполитой под командованием Яна III Собеского разбила турецкую армию и сняла двухмесячную осаду Вены.\n\nВ 2018 году к юбилею битвы был возведён постамент для 8-метрового конного монумента Собеского, однако мэрия Вены заблокировала установку готовой бронзовой скульптуры. Пустой цоколь («недопамятник») неоднократно становился объектом дипломатических споров и акций.',
        'en': 'Address: Am Kahlenberg, 1190 Vienna, Austria.\n\nMemorial pedestal on the observation terrace of Mount Kahlenberg overlooking Vienna. Site of the decisive 1683 Battle of Vienna where the allied army commanded by King and Grand Duke John III Sobieski broke the Ottoman siege. In 2018, the pedestal was erected for an 8-meter bronze equestrian statue, but installation was halted by Vienna authorities, leaving the controversial empty pedestal known as the "unfinished monument".'
    },
    'links': [
        {
            'title': 'Наша Ніва: Спрэчкі вакол помніка Яну III Сабескаму ў Вене',
            'url': 'https://nashaniva.com/404567'
        },
        {
            'title': 'OpenStreetMap: Вузел Sobieski-Denkmal am Kahlenberg',
            'url': 'https://www.openstreetmap.org/node/10793617195'
        },
        {
            'title': 'Вікіпедыя: Венская бітва 1683 года',
            'url': 'https://be.wikipedia.org/wiki/Венская_бітва_(1683)'
        }
    ],
    'tags': [
        'сабескі',
        'вена',
        'каленберг',
        'помнік',
        'вкл',
        'аўстрыя',
        'бітва'
    ],
    'personId': 'yan-iii-sabeski',
    'personIds': ['yan-iii-sabeski'],
    'mustSee': True
})

with open('data/places.json', 'w', encoding='utf-8') as f:
    json.dump(places, f, ensure_ascii=False, indent=2)

with open('data/places.js', 'w', encoding='utf-8') as f:
    f.write('window.INITIAL_PLACES = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

# 2. Update persons.json with placeIds for yan-iii-sabeski
with open('data/persons.json', 'r', encoding='utf-8') as f:
    persons = json.load(f)

for per in persons:
    if per['id'] == 'yan-iii-sabeski':
        pids = set(per.get('placeIds', []))
        pids.add(monument_id)
        pids.add('vienna-kahlenberg-st-joseph-sobieski')
        per['placeIds'] = list(pids)

with open('data/persons.json', 'w', encoding='utf-8') as f:
    json.dump(persons, f, ensure_ascii=False, indent=2)

with open('data/persons.js', 'w', encoding='utf-8') as f:
    f.write('window.INITIAL_PERSONS = ' + json.dumps(persons, ensure_ascii=False, indent=2) + ';\n')

print(f"Added {monument_id} to places and persons successfully!")
