import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/places.json', 'r', encoding='utf-8') as f:
    places = json.load(f)

# 1. Fix King Jagiello Monument coordinates
for p in places:
    if p['id'] == 'new-york-central-park-king-jagiello':
        p['coordinates'] = [40.778889, -73.966667]
        p['wiki'] = 'https://en.wikipedia.org/wiki/King_Jagiello_Monument'
        p['links'] = [
            {'title': 'Вікіпедыя: King Jagiello Monument (Central Park)', 'url': 'https://en.wikipedia.org/wiki/King_Jagiello_Monument'},
            {'title': 'OpenStreetMap: King Jagiello Monument', 'url': 'https://www.openstreetmap.org/node/357633519'}
        ]
        p.pop('unverifiedCoordinates', None)

# 2. Add KHM Vienna (Dürer - Vankovich provenance from Nasha Niva 381240)
khm_id = 'vienna-khm-durer-venetian-woman-vankovich'
places = [p for p in places if p['id'] != khm_id]
places.append({
    'id': khm_id,
    'title': {
        'by': 'Музей гісторыі мастацтваў у Вене — Шэдэўр Дзюрэра з калекцыі Ваньковічаў',
        'ru': 'Музей истории искусств в Вене — Шедевр Дюрера из коллекции Ваньковичей',
        'en': 'Kunsthistorisches Museum Vienna — Dürer Masterpiece from the Wańkowicz Collection'
    },
    'category': 'culture',
    'country': {'by': 'Аўстрыя', 'ru': 'Австрия', 'en': 'Austria'},
    'city': {'by': 'Вена', 'ru': 'Вена', 'en': 'Vienna'},
    'coordinates': [48.203740, 16.361782],
    'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Albrecht_D%C3%BCrer_089b.jpg/960px-Albrecht_D%C3%BCrer_089b.jpg',
    'wiki': 'https://en.wikipedia.org/wiki/Portrait_of_a_Venetian_Woman',
    'description': {
        'by': 'Адрас: Maria-Theresien-Platz, 1010 Wien, Аўстрыя.\n\nУ карціннай галерэі знакамітага венскага музея захоўваецца адзін з найвыдатнейшых шэдэўраў эпохі Адраджэння — «Партрэт венецыянкі» (1505 г.) Альбрэхта Дзюрэра (яго выява была размешчана на банкноце наміналам 5 нямецкіх марак).\n\nКарціна на працягу стагоддзя належала беларускаму шляхецкаму роду Ваньковічаў і захоўвалася ў іх рэзідэнцыі пад Мінскам (маёнтак Сляпянка). У 1923 годзе польскі дыпламат родам з Міншчыны Вітальд Клеменс Ваньковіч асабіста прадаў карціну венскаму музею, каб уратаваць сродкі сям\'і пасля страты маёнткаў за савецкай мяжой. У музейных інвентарах Вены твор зафіксаваны як набыты ў Ваньковіча з уласнасці «літоўскай» арыстакратычнай сям\'і.',
        'ru': 'Адрес: Maria-Theresien-Platz, 1010 Wien, Австрия.\n\nВ венском Музее истории искусств хранится шедевр Альбрехта Дюрера «Портрет венецианки» (1505 г., изображался на банкноте в 5 немецких марок). Полотно принадлежало шляхетскому роду Ваньковичей и хранилось в их усадьбе под Минском (Слепянка). В 1923 г. дипломат Витольд Ванькович продал картину венскому музею.',
        'en': 'Address: Maria-Theresien-Platz, 1010 Vienna, Austria.\n\nThe Kunsthistorisches Museum houses Albrecht Dürer\'s celebrated Renaissance masterpiece "Portrait of a Venetian Woman" (1505). For generations it belonged to the Belarusian noble Wańkowicz family at their Slepyanka estate near Minsk, until diplomat Witold Wańkowicz sold it to the museum in 1923.'
    },
    'links': [
        {'title': 'Наша Ніва: У Мінску быў свой шэдэўр Альбрэхта Дзюрэра. Дзе ён цяпер?', 'url': 'https://nashaniva.com/381240'},
        {'title': 'Афіцыйны каталог KHM: Bildnis einer Venezianerin (Albrecht Dürer)', 'url': 'https://www.khm.at/objektdb/detail/613/'},
        {'title': 'Вікіпедыя: Portrait of a Venetian Woman', 'url': 'https://en.wikipedia.org/wiki/Portrait_of_a_Venetian_Woman'}
    ],
    'tags': ['дзюрэр', 'ваньковіч', 'вена', 'музей', 'жывапіс', 'аўстрыя', 'мінск'],
    'personId': 'valyantsin-vankovich',
    'personIds': ['valyantsin-vankovich'],
    'mustSee': True
})

# 3. Add Kraslava Plater Palace in Latvia
plater_id = 'kraslava-plater-palace'
places = [p for p in places if p['id'] != plater_id]
places.append({
    'id': plater_id,
    'title': {
        'by': 'Палац графаў Броэль-Плятэраў у Краславе',
        'ru': 'Дворец графов Броэль-Платеров в Краславе',
        'en': 'Plater-Zyberk Palace in Krāslava'
    },
    'category': 'historical',
    'country': {'by': 'Латвія', 'ru': 'Латвия', 'en': 'Latvia'},
    'city': {'by': 'Краслава', 'ru': 'Краслава', 'en': 'Krāslava'},
    'coordinates': [55.899616, 27.159657],
    'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Kraslava_Castle_2016-09-04.jpg/960px-Kraslava_Castle_2016-09-04.jpg',
    'wiki': 'https://lv.wikipedia.org/wiki/Kr%C4%81slavas_jaun%C4%81_pils',
    'description': {
        'by': 'Адрас: Pils iela 6, Krāslava, Латвія.\n\nМанументальны палацава-паркавы ансамбль графаў Броэль-Плятэраў XVIII ст. на высокім беразе Дзвіны ў Інфлянтах (Латгаліі). Пабудаваны пад кіраўніцтвам ваяводы мсціслаўскага і падскарбія надворнага літоўскага Канстанціна Людвіка Плятэра і архітэктара Антоніа Парака. Тут знаходзілася багацейшая бібліятэка, архівы і карцінная галерэя роду Плятэраў, цесна звязанага з беларускім вызвольным рухам (Эмілія Плятэр).',
        'ru': 'Адрес: Pils iela 6, Krāslava, Латвия.\n\nДворцово-парковый комплекс графов Броэль-Плятеров XVIII века над Двиной. Главная резиденция Плятеров в Инфлянтах, возведённая подскарбием литовским Константином Людвиком Плятером.',
        'en': 'Address: Pils iela 6, Krāslava, Latvia.\n\n18th-century palace complex of the Count Plater family overlooking the Daugava/Dzvina River. Built for Grand Duchy dignitary Konstanty Ludwik Plater, housing the famous Plater archives, art collection, and library.'
    },
    'links': [
        {'title': 'Вікіпедыя: Krāslavas jaunā pils', 'url': 'https://lv.wikipedia.org/wiki/Kr%C4%81slavas_jaun%C4%81_pils'}
    ],
    'tags': ['плятэры', 'палац', 'латвія', 'дзвіна', 'латгалія', 'вкл']
})

# 4. Add Bagdoniškis Romer estate in Lithuania
romer_id = 'bagdoniskis-romer-manor'
places = [p for p in places if p['id'] != romer_id]
places.append({
    'id': romer_id,
    'title': {
        'by': 'Сядзіба роду Ромераў у Багданішках',
        'ru': 'Усадьба рода Ромеров в Багдонишкисе',
        'en': 'Romer Family Manor in Bagdoniškis'
    },
    'category': 'historical',
    'country': {'by': 'Літва', 'ru': 'Литва', 'en': 'Lithuania'},
    'city': {'by': 'Багданішкіс (Рокішкіс)', 'ru': 'Багдонишкис (Рокишкис)', 'en': 'Bagdoniškis'},
    'coordinates': [55.892012, 25.722352],
    'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Bagdoni%C5%A1kio_dvaras_2017.jpg/960px-Bagdoni%C5%A1kio_dvaras_2017.jpg',
    'wiki': 'https://lt.wikipedia.org/wiki/Bagdoni%C5%A1kio_dvaras',
    'description': {
        'by': 'Радавое гняздо выбітнага шляхецкага роду Ромераў, які даў Беларусі і Літве цэлую плеяду славутых дзеячаў культуры: мастакоў Альфрэда Ісідара Ромера і Эдварда Матэвуша Ромера, а таксама вядомага юрыста, дзеяча краёўцаў і рэктара ўніверсітэта ў Каўнасе Міхала Ромера (Mykolas Romeris), які нарадзіўся і пахаваны тут.',
        'ru': 'Родовая усадьба дворянского рода Ромеров, давшего художников Альфреда Исидора Ромера, Эдварда Ромера и выдающегося юриста, ректора университета в Каунасе Михала Ромера.',
        'en': 'Ancestral estate of the noble Römer (Romer) family, home to renowned artists Alfred Isidore Romer and Edward Mateusz Romer, as well as jurist and Kaunas university rector Michał Römer.'
    },
    'links': [
        {'title': 'Вікіпедыя: Bagdoniškio dvaras', 'url': 'https://lt.wikipedia.org/wiki/Bagdoni%C5%A1kio_dvaras'}
    ],
    'tags': ['ромеры', 'сядзіба', 'літва', 'жывапіс', 'мастакі']
})

# 5. Add Faina Vakhreva (Chiang Fang-liang) Mausoleum in Taiwan (First Lady of Taiwan, native of Belarus)
faina_id = 'taiwan-touliao-faina-vakhreva-tomb'
places = [p for p in places if p['id'] != faina_id]
places.append({
    'id': faina_id,
    'title': {
        'by': 'Маўзалей Тоўляо — Спачынак Фаіны Вахравай (Першай лэдзі Тайваня)',
        'ru': 'Мавзолей Тоуляо — Усыпальница Фаины Вахревой (Первой леди Тайваня)',
        'en': 'Touliao Mausoleum — Resting Place of Faina Chiang Fang-liang (First Lady of Taiwan)'
    },
    'category': 'grave',
    'country': {'by': 'Тайвань', 'ru': 'Тайвань', 'en': 'Taiwan'},
    'city': {'by': 'Тааюань (Дасі)', 'ru': 'Таоюань (Даси)', 'en': 'Taoyuan (Daxi)'},
    'coordinates': [24.848333, 121.286111],
    'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Daxi_Mausoleum_01_20250514.jpg/960px-Daxi_Mausoleum_01_20250514.jpg',
    'wiki': 'https://en.wikipedia.org/wiki/Faina_Chiang_Fang-liang',
    'description': {
        'by': 'Адрас: Fuxing Rd, Daxi District, Taoyuan City, Тайвань.\n\nМаўзалей Тоўляо — месца спачыну прэзідэнта Кітайскай Рэспублікі (Тайваня) Цзян Цзінго і яго жонкі, Першай лэдзі Тайваня Фаіны Вахравай (Цзян Фанлян, 1916–2004).\n\nФаіна Вахрава паходзіла з беларускай сям\'і. Працуючы на заводзе, пазнаёмілася з сынам кіраўніка Кітая Чан Кайшы — Цзян Цзінго. Яны ажаніліся ў 1935 г., пасля чаго Фаіна пераехала ў Кітай, а пазней на Тайвань. Калі Цзінго стаў прэзідэнтам, Фаіна Вахрава 10 гадоў (1978–1988) выконвала абавязкі Першай лэдзі краіны, карыстаючыся вялікай павагай тайваньцаў за сціпласць, шчодрасць і дабрачыннасць.',
        'ru': 'Мавзолей Тоуляо в Даси (Тайвань) — усыпальница президента Китайской Республики (Тайваня) Цзян Цзинго и его супруги, Первой леди Тайваня Фаины Ипатьевны Вахревой (Цзян Фанлян, 1916–2004), происходившей из белорусской семьи. Фаина была Первой леди Тайваня в 1978–1988 годах.',
        'en': 'Touliao Mausoleum in Daxi, Taiwan — the resting place of President Chiang Ching-kuo and his wife, First Lady Faina Chiang Fang-liang (born Faina Vakhreva, 1916–2004), who hailed from a Belarusian family and served as First Lady of Taiwan from 1978 to 1988.'
    },
    'links': [
        {'title': 'Вікіпедыя: Faina Chiang Fang-liang', 'url': 'https://en.wikipedia.org/wiki/Faina_Chiang_Fang-liang'},
        {'title': 'Вікіпедыя: Маўзалей Тоўляо (Touliao Mausoleum)', 'url': 'https://en.wikipedia.org/wiki/Touliao_Mausoleum'}
    ],
    'tags': ['тайвань', 'вахрава', 'першаялэдзі', 'кітай', 'пахаванне', 'маўзалей']
})

with open('data/places.json', 'w', encoding='utf-8') as f:
    json.dump(places, f, ensure_ascii=False, indent=2)

with open('data/places.js', 'w', encoding='utf-8') as f:
    f.write('window.INITIAL_PLACES = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

print(f"Dataset successfully updated! Total places: {len(places)}")
