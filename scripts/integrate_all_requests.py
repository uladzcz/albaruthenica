import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

with open('data/places.json', 'r', encoding='utf-8') as f:
    places = json.load(f)
with open('data/persons.json', 'r', encoding='utf-8') as f:
    persons = json.load(f)

# Helper to add or replace person
def upsert_person(p_dict):
    global persons
    existing = next((p for p in persons if p['id'] == p_dict['id']), None)
    if existing:
        # Merge placeIds
        all_pids = list(dict.fromkeys(existing.get('placeIds', []) + p_dict.get('placeIds', [])))
        existing.update(p_dict)
        existing['placeIds'] = all_pids
    else:
        persons.append(p_dict)

# Helper to add or replace place
def upsert_place(p_dict):
    global places
    existing = next((p for p in places if p['id'] == p_dict['id']), None)
    if existing:
        existing.update(p_dict)
    else:
        places.append(p_dict)

# 1. PERSON: Eustachy Tyszkiewicz
upsert_person({
    "id": "eustachy-tyszkiewicz",
    "name": {
        "by": "Яўстах Тышкевіч",
        "ru": "Евстафий Тышкевич",
        "en": "Eustachy Tyszkiewicz"
    },
    "dates": "1814 — 1873",
    "role": {
        "by": "Беларускі археолаг, гісторык, этнограф, стваральнік Віленскага музея старажытнасцяў",
        "ru": "Белорусский археолог, историк, этнограф, основатель Виленского музея древностей",
        "en": "Belarusian archaeologist, historian, ethnographer, founder of the Vilnius Museum of Antiquities"
    },
    "bio": {
        "by": "Ураджэнец Лагойска. Заснавальнік беларускай навуковай археалогіі і музеязнаўства. Стварыў знакаміты Лагойскі музей старажытнасцей (1842) і Віленскі музей старажытнасцей (1855) разам з Віленскай археалагічнай камісіяй. Частку збораў захоўваў у сваім родавым палацы ў Вільні («Дом пад балванамі»). Ганаровы чалец Стакгольмскай каралеўскай акадэміі.",
        "ru": "Уроженец Логойска. Один из основоположников белорусской научной археологии. Создал Логойский музей древностей (1842) и Виленский музей древностей (1855). Часть коллекций хранил в родовом дворце Тышкевичей («Дом под атлантами») в Вильнюсе.",
        "en": "Born in Lahoysk. Founding pioneer of Belarusian scientific archaeology and museology. Founded the Lahoysk Museum of Antiquities (1842) and the Vilnius Museum of Antiquities (1855). Kept his personal archaeological collections at the Tyszkiewicz Palace ('House of Atlantes') in Vilnius."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Eustachy_Tyszkiewicz_%28before_1873%29.jpg/330px-Eustachy_Tyszkiewicz_%28before_1873%29.jpg",
    "wiki": "https://be.wikipedia.org/wiki/Яўстах_Піевіч_Тышкевіч",
    "placeIds": ["vilnia-dom-pad-balvanami"]
})

# 2. PERSON: Yakub Kolas
upsert_person({
    "id": "yakub-kolas",
    "name": {
        "by": "Якуб Колас (Канстанцін Міцкевіч)",
        "ru": "Якуб Колас (Константин Мицкевич)",
        "en": "Yakub Kolas (Kanstantsin Mitskevich)"
    },
    "dates": "1882 — 1956",
    "role": {
        "by": "Класік беларускай літаратуры, народны паэт Беларусі, акадэмік",
        "ru": "Классик белорусской литературы, народный поэт Беларуси, академик",
        "en": "Classic of Belarusian literature, People's Poet of Belarus, academician"
    },
    "bio": {
        "by": "Ураджэнец засценка Акінчыцы (Стаўбцоўшчына). Класік нацыянальнай літаратуры, аўтар эпапей «Новая зямля», «Сымон-музыка», трылогіі «На ростанях». У траўні 1907 г. прыехаў у Вільню ў рэдакцыю «Нашай Нівы» («Дом пад балванамі»), дзе распачаў працу як рэдактар літаратурнага аддзела.",
        "ru": "Уроженец Столбцовского района. Классик белорусской литературы, автор поэм «Новая земля», «Сымон-музыкант», трилогии «На росстанях». В мае 1907 года впервые приехал в Вильнюс в редакцию «Нашай Нівы» («Дом под атлантами»), где начал работу редактором литературного отдела.",
        "en": "Born near Stowbtsy. Titan of Belarusian literature, author of the national epic poems 'The New Land', 'Symon the Musician', and the trilogy 'At the Crossroads'. In May 1907, arrived in Vilnius at the 'Nasha Niva' editorial office in the 'House of Atlantes' on Trakų St."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Kanstantyn_Mickievi%C4%8D_%28Jakub_Ko%C5%82as%29._%D0%9A%D0%B0%D0%BD%D1%81%D1%82%D0%B0%D0%BD%D1%82%D1%8B%D0%BD_%D0%9C%D1%96%D1%86%D0%BA%D0%B5%D0%B2%D1%96%D1%87_%28%D0%AF%D0%BA%D1%83%D0%B1_%D0%9A%D0%BE%D0%BB%D0%B0%D1%81%29_%281925%29.jpg/330px-Kanstantyn_Mickievi%C4%8D_%28Jakub_Ko%C5%82as%29._%D0%9A%D0%B0%D0%BD%D1%81%D1%82%D0%B0%D0%BD%D1%82%D1%8B%D0%BD_%D0%9C%D1%96%D1%86%D0%BA%D0%B5%D0%B2%D1%96%D1%87_%28%D0%AF%D0%BA%D1%83%D0%B1_%D0%9A%D0%BE%D0%BB%D0%B0%D1%81%29_%281925%29.jpg",
    "wiki": "https://be.wikipedia.org/wiki/Якуб_Колас",
    "placeIds": ["vilnia-dom-pad-balvanami"]
})

# 3. Update Francisak Bahusevic placeIds to include vilnia-dom-pad-balvanami
bahusevic = next((p for p in persons if p['id'] == 'francisak-bahusevic'), None)
if bahusevic:
    if 'vilnia-dom-pad-balvanami' not in bahusevic.get('placeIds', []):
        bahusevic.setdefault('placeIds', []).append('vilnia-dom-pad-balvanami')

# 4. Update Kastus Kalinouski placeIds
kalinouski = next((p for p in persons if p['id'] == 'kastus-kalinouski'), None)
if kalinouski:
    if 'vilnia-dom-pad-balvanami' not in kalinouski.get('placeIds', []):
        kalinouski.setdefault('placeIds', []).append('vilnia-dom-pad-balvanami')

# 5. Update vilnia-dom-pad-balvanami place
dom_pad_balvanami = next((p for p in places if p['id'] == 'vilnia-dom-pad-balvanami'), None)
if dom_pad_balvanami:
    dom_pad_balvanami['personIds'] = [
        "eustachy-tyszkiewicz",
        "francisak-bahusevic",
        "yakub-kolas",
        "kastus-kalinouski"
    ]
    dom_pad_balvanami['personId'] = "eustachy-tyszkiewicz"
    print("Updated vilnia-dom-pad-balvanami with all 4 associated figures!")

# 6. PERSON: Alexander Kishchenko
upsert_person({
    "id": "alexander-kishchenko",
    "name": {
        "by": "Аляксандр Кішчанка",
        "ru": "Александр Кищенко",
        "en": "Alexander Kishchenko"
    },
    "dates": "1933 — 1997",
    "role": {
        "by": "Народны мастак Беларусі, аўтар манументальных мазаік і габеленаў",
        "ru": "Народный художник Беларуси, автор монументальных мозаик и гобеленов",
        "en": "People's Artist of Belarus, master of monumental mosaics and tapestries"
    },
    "bio": {
        "by": "Выбітны беларускі мастак-манументаліст і жывапісец, народны мастак Беларусі. Стваральнік знакамітых мазаічных пано на праспекце Незалежнасці ў Мінску («Партызаны», «Горад-ваяр»), сусветна вядомага «Габелена стагоддзя» (занесены ў Кнігу рэкордаў Гінэса як самы вялікі ў свеце) і манументальнага габелена «Чарнобыль», які ў 1991 г. быў перададзены ў дар ААН і экспануецца ў штаб-кватэры ААН у Нью-Ёрку.",
        "ru": "Выдающийся белорусский художник-монументалист, народный художник Беларуси. Создатель знаменитых мозаичных панно на проспекте Независимости в Минске («Партизаны», «Город-воин»), занесённого в Книгу рекордов Гиннесса «Гобелена века» и монументального гобелена «Чернобыль», переданного в дар ООН в 1991 году и украшающего штаб-квартиру ООН в Нью-Йорке.",
        "en": "Prominent Belarusian monumental artist and painter, People's Artist of Belarus. Created the landmark mosaics on Independence Avenue in Minsk, the Guinness Record-holding 'Tapestry of the Century', and the hand-woven masterpiece 'Chernobyl' presented to the United Nations in 1991 and exhibited at UN Headquarters in New York."
    },
    "image": "https://www.un.org/ungifts/sites/www.un.org.ungifts/files/163g_belarus_2.jpg",
    "wiki": "https://ru.wikipedia.org/wiki/Кищенко,_Александр_Михайлович",
    "placeIds": ["un-hq-chernobyl-tapestry"]
})

# 7. PLACE: UN Chernobyl Tapestry
upsert_place({
    "id": "un-hq-chernobyl-tapestry",
    "title": {
        "by": "Габелен «Чарнобыль» у штаб-кватэры ААН (Аляксандр Кішчанка)",
        "ru": "Гобелен «Чернобыль» в штаб-квартире ООН (Александр Кищенко)",
        "en": "\"Chernobyl\" Tapestry at the United Nations Headquarters"
    },
    "category": "culture",
    "country": {
        "by": "ЗША",
        "ru": "США",
        "en": "United States"
    },
    "city": {
        "by": "Нью-Ёрк",
        "ru": "Нью-Йорк",
        "en": "New York"
    },
    "coordinates": [
        40.7499,
        -73.9678
    ],
    "description": {
        "by": "Манументальны сотканны ўручную габелен (памеры 3,8 × 10 метраў) створаны народным мастаком Беларусі Аляксандрам Кішчанкам у памяць пра Чарнобыльскую трагедыю 1986 года. 19 верасня 1991 года габелен быў урачыста перададзены ў дар Арганізацыі Аб'яднаных Нацый ад урада і народа Беларусі міністрам замежных спраў Пятром Краўчанкам і прыняты Генеральным сакратаром ААН Хаўерам Перэсам дэ Куэльлярам. Знаходзіцца ў будынку Генеральнай Асамблеі ААН (3-ці паверх).",
        "ru": "Монументальный сотканный вручную гобелен (размеры 3,8 × 10 метров) создан народным художником Беларуси Александром Кищенко в память о Чернобыльской трагедии 1986 года. 19 сентября 1991 года гобелен был торжественно передан в дар Организации Объединенных Наций от правительства и народа Беларуси министром иностранных дел Петром Кравченко и принят Генеральным секретарем ООН Хавьером Пересом де Куэльяром. Размещен в здании Генеральной Ассамблеи ООН (3-й этаж).",
        "en": "Monumental hand-woven tapestry (approx. 3.8 × 10 meters) created by People's Artist of Belarus Alexander Kishchenko to commemorate the 1986 Chernobyl nuclear disaster. Presented as an official gift to the United Nations from the government and people of Belarus on September 19, 1991 by Foreign Minister Pyotr Kravchenko and accepted by UN Secretary-General Javier Pérez de Cuéllar. Exhibited in the General Assembly Building (3rd floor)."
    },
    "image": "https://www.un.org/ungifts/sites/www.un.org.ungifts/files/163g_belarus_2.jpg",
    "links": [
        {
            "title": "Афіцыйны рэестр падарункаў ААН: Гобелен «Чернобыль»",
            "url": "https://www.un.org/ungifts/ru/%D1%87%D0%B5%D1%80%D0%BD%D0%BE%D0%B1%D1%8B%D0%BB%D1%8C"
        },
        {
            "title": "Аляксандр Кішчанка — Вікіпедыя",
            "url": "https://ru.wikipedia.org/wiki/Кищенко,_Александр_Михайлович"
        }
    ],
    "tags": [
        "ААН",
        "Нью-Ёрк",
        "Кішчанка",
        "Чарнобыль",
        "Мастацтва",
        "culture"
    ],
    "personId": "alexander-kishchenko",
    "personIds": [
        "alexander-kishchenko"
    ],
    "unverifiedCoordinates": False
})
print("Added un-hq-chernobyl-tapestry")

# 8. PERSON: Bona Sforza
upsert_person({
    "id": "bona-sforza",
    "name": {
        "by": "Бона Сфорца",
        "ru": "Бона Сфорца",
        "en": "Bona Sforza"
    },
    "dates": "1494 — 1557",
    "role": {
        "by": "Вялікая княгіня літоўская і каралева польская, герцагіня Бары, рэфарматарка",
        "ru": "Великая княгиня литовская и королева польская, герцогиня Бари, реформатор",
        "en": "Grand Duchess of Lithuania and Queen of Poland, Duchess of Bari, reformer"
    },
    "bio": {
        "by": "Вялікая княгіня літоўская і каралева польская (жонка Жыгімонта I Старога). Ініцыятарка найбуйнейшай аграрнай і эканамічнай рэформы ў ВКЛ — Валочнай памеры (1557), якая на стагоддзі вызначыла планіроўку беларускіх вёсак і землекарыстанне. Кіравала Пінскім, Кобрынскім, Гарадзенскім, Клецкім стараствамі, дзе развівала гандаль, будавала замкі і першыя меліярацыйныя каналы («Канал каралевы Боны»). Прывезла на беларускія землі майстроў і традыцыі італьянскага Рэнесансу. Апошнія гады правяла ў Швабскім замку ў Бары, дзе была атручана. Пахаваная ў базіліцы Святога Мікалая ў Бары.",
        "ru": "Великая княгиня литовская и королева польская (супруга Сигизмунда I Старого). Инициатор масштабной аграрной реформы в ВКЛ — «Волочной померы» (1557), изменившей структуру белорусского села. Владела Пинском, Кобрином, Гродно, Клецком, строила замки и первые мелиорационные каналы («Канал Боны»). Привнесла в культуру ВКЛ идеи итальянского Возрождения. Последние годы провела в Швабском замке в Бари, где была отравлена. Похоронена в базилике Святого Николая в Бари.",
        "en": "Grand Duchess of Lithuania and Queen of Poland (consort of Sigismund I the Old). Instigated the landmark agrarian and fiscal reform in the GDL — the Wallach Measurement ('Valochnaya pamiera', 1557). Governed Pinsk, Kobryn, Hrodna, and Kletsk, developing commerce, founding castles, and digging the first land drainage canals ('Bona Canal'). Championed Renaissance architecture and humanism in Belarus. Spent her final years in the Swabian Castle in Bari where she was poisoned. Buried in the Basilica of Saint Nicholas in Bari."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Bona_Sforza_in_1517.jpg/330px-Bona_Sforza_in_1517.jpg",
    "wiki": "https://be.wikipedia.org/wiki/Бона_Сфорца",
    "placeIds": [
        "bari-castello-svevo-bona-sforza",
        "bari-basilica-san-nicola-bona-sforza-tomb"
    ]
})
print("Added Bona Sforza person")

# 9. PLACE: Swabian Castle in Bari (Castello Svevo)
upsert_place({
    "id": "bari-castello-svevo-bona-sforza",
    "title": {
        "by": "Швабскі замак і барэльеф Боне Сфорцы ў Бары",
        "ru": "Швабский замок и барельеф Боне Сфорца в Бари",
        "en": "Swabian Castle & Bona Sforza Bas-Relief in Bari"
    },
    "category": "historical",
    "country": {
        "by": "Італія",
        "ru": "Италия",
        "en": "Italy"
    },
    "city": {
        "by": "Бары",
        "ru": "Бари",
        "en": "Bari"
    },
    "coordinates": [
        41.1287,
        16.8659
    ],
    "description": {
        "by": "Рэнесансная рэзідэнцыя вялікай княгіні літоўскай і каралевы польскай Боны Сфорцы (1494–1557), якая правяла тут апошнія гады жыцця пасля вяртання з Рэчы Паспалітай і была атручана ў замку ў лістападзе 1557 г. Адна з кутніх вежаў замка носіць імя Боны Сфорцы. 7 кастрычніка 2026 г. у нішы замкавай сцяны адкрыты бронзавы барэльеф Боне Сфорцы з гербамі ВКЛ (Пагоня), Польшчы (Белы Арол), Сфорца і Арагона ды лацінскім тытулам «MAGNA DUX LITHUANIAE» (Вялікая княгіня літоўская).",
        "ru": "Ренессансная резиденция великой княгини литовской и королевы польской Боны Сфорца (1494–1557), где она провела последние годы после отъезда из Речи Посполитой и была отравлена в ноябре 1557 г. 7 октября 2026 г. на замковой стене торжественно открыт бронзовый барельеф Боне Сфорца с гербами ВКЛ («Погоня»), Польши, Сфорца и Арагона, а также титулом «MAGNA DUX LITHUANIAE».",
        "en": "Renaissance residence of Grand Duchess of Lithuania and Queen of Poland Bona Sforza (1494–1557), where she spent her final years after leaving the Polish-Lithuanian Commonwealth and was poisoned in November 1557. On October 7, 2026, a bronze bas-relief in honor of Bona Sforza featuring the GDL Pahonia coat of arms, the Polish White Eagle, and the Latin title 'MAGNA DUX LITHUANIAE' was unveiled on the castle wall."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Bari_BW_2016-10-19_12-32-30.jpg/960px-Bari_BW_2016-10-19_12-32-30.jpg",
    "links": [
        {
            "title": "Наша Ніва: У Швабскім замку ў Бары адкрылі барэльеф Боне Сфорца",
            "url": "https://nashaniva.com/406309"
        },
        {
            "title": "Швабскі замак у Бары — Вікіпедыя",
            "url": "https://en.wikipedia.org/wiki/Castello_Normanno-Svevo_(Bari)"
        }
    ],
    "tags": [
        "Бары",
        "Італія",
        "Бона Сфорца",
        "ВКЛ",
        "Пагоня",
        "Рэнесанс",
        "historical"
    ],
    "personId": "bona-sforza",
    "personIds": [
        "bona-sforza"
    ],
    "unverifiedCoordinates": False
})
print("Added bari-castello-svevo-bona-sforza")

# 10. PLACE: Basilica di San Nicola in Bari (Tomb of Bona Sforza)
upsert_place({
    "id": "bari-basilica-san-nicola-bona-sforza-tomb",
    "title": {
        "by": "Базіліка Святога Мікалая — манументальнае надмагілле Боны Сфорцы",
        "ru": "Базилика Святого Николая — монументальное надгробие Боны Сфорца",
        "en": "Basilica of Saint Nicholas — Mausoleum of Bona Sforza"
    },
    "category": "grave",
    "country": {
        "by": "Італія",
        "ru": "Италия",
        "en": "Italy"
    },
    "city": {
        "by": "Бары",
        "ru": "Бари",
        "en": "Bari"
    },
    "coordinates": [
        41.1306,
        16.8705
    ],
    "description": {
        "by": "У цэнтральнай апсідзе знакамітай базілікі Святога Мікалая ў Бары месціцца пышнае маньерысцкае надмагілле каралевы польскай і вялікай княгіні літоўскай Боны Сфорцы. Створана ў 1593 г. на замову яе дачкі Ганны Ягелонкі славутым скульптарам Санці Гучы (Santi Gucci). Кампазіцыя ўключае выяву каралевы на каленях перад Богам, статуі св. Мікалая і св. Станіслава (заступніка Польшчы і Літвы) ды гербы Польшчы і Вялікага Княства Літоўскага (Пагоня).",
        "ru": "В центральной апсиде базилики Святого Николая в Бари находится величественное надгробие великой княгини литовской и королевы польской Боны Сфорца, созданное в 1593 году скульптором Санти Гуччи по заказу Анны Ягеллонки. Надгробие украшено статуями св. Николая и св. Станислава, а также гербами Польши и Великого Княжества Литовского («Погоня»).",
        "en": "Inside the central apse of the renowned Basilica of Saint Nicholas in Bari stands the mannerist tomb and mausoleum of Grand Duchess of Lithuania and Queen of Poland Bona Sforza. Commissioned in 1593 by her daughter Anna Jagiellon and crafted by Florentine master Santi Gucci, it features kneeling Bona, statues of St. Nicholas and St. Stanislaus, and the coats of arms of Poland and the Grand Duchy of Lithuania (Pahonia)."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Bona_Sforza_tomb_IMG_4657.jpg/960px-Bona_Sforza_tomb_IMG_4657.jpg",
    "links": [
        {
            "title": "Наша Ніва: У Швабскім замку ў Бары адкрылі барэльеф Боне Сфорца",
            "url": "https://nashaniva.com/406309"
        },
        {
            "title": "Базіліка Святога Мікалая ў Бары — Вікіпедыя",
            "url": "https://en.wikipedia.org/wiki/Basilica_di_San_Nicola_(Bari)"
        }
    ],
    "tags": [
        "Бары",
        "Італія",
        "Бона Сфорца",
        "ВКЛ",
        "Пагоня",
        "Санці Гучы",
        "grave"
    ],
    "personId": "bona-sforza",
    "personIds": [
        "bona-sforza"
    ],
    "unverifiedCoordinates": False
})
print("Added bari-basilica-san-nicola-bona-sforza-tomb")

# Write out all files
with open('data/places.json', 'w', encoding='utf-8') as f:
    json.dump(places, f, ensure_ascii=False, indent=2)
with open('data/places.js', 'w', encoding='utf-8') as f:
    f.write('// Albaruthenica Places Dataset\nwindow.INITIAL_PLACES = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

with open('data/persons.json', 'w', encoding='utf-8') as f:
    json.dump(persons, f, ensure_ascii=False, indent=2)
with open('data/persons.js', 'w', encoding='utf-8') as f:
    f.write('// Albaruthenica Persons Dataset\nwindow.INITIAL_PERSONS = ' + json.dumps(persons, ensure_ascii=False, indent=2) + ';\n')

print(f"Total places now: {len(places)}")
print(f"Total persons now: {len(persons)}")
print("All datasets successfully updated and synced!")
