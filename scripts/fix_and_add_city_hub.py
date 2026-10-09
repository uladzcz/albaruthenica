import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

with open('data/places.json', 'r', encoding='utf-8') as f:
    places = json.load(f)
with open('data/persons.json', 'r', encoding='utf-8') as f:
    persons = json.load(f)

def upsert_person(p_dict):
    global persons
    existing = next((p for p in persons if p['id'] == p_dict['id']), None)
    if existing:
        all_pids = list(dict.fromkeys(existing.get('placeIds', []) + p_dict.get('placeIds', [])))
        existing.update(p_dict)
        existing['placeIds'] = all_pids
    else:
        persons.append(p_dict)

def upsert_place(p_dict):
    global places
    existing = next((p for p in places if p['id'] == p_dict['id']), None)
    if existing:
        existing.update(p_dict)
    else:
        places.append(p_dict)

# 1. PERSON: Euphrosyne of Polotsk
upsert_person({
    "id": "euphrosyne-polotsk",
    "name": {
        "by": "Еўфрасіння Полацкая",
        "ru": "Евфросиния Полоцкая",
        "en": "Euphrosyne of Polotsk"
    },
    "dates": "~1104 — 1167",
    "role": {
        "by": "Асветніца, ігумення, нябесная апякунка Беларусі, кананізаваная святая",
        "ru": "Просветительница, игумения, небесная покровительница Беларуси, святая",
        "en": "Enlightener, abbess, patron saint of Belarus, revered in Eastern Orthodoxy"
    },
    "bio": {
        "by": "Унучка полацкага князя Усяслава Чарадзея. Выдатная дзеячка асветніцтва і культуры Полацкага княства. Заснавала Спаса-Еўфрасіннеўскі манастыр, адкрыла скрыпторыі і школы для дзяўчат, замовіла Лазару Богшу шэдэўр сакральнага мастацтва — славуты Крыж Еўфрасінні Полацкай (1161). Памерла падчас паломніцтва ў Іерусалім. Яе святыя мошчы больш за 700 гадоў (1187–1910) захоўваліся ў Дальніх пячорах Кіева-Пячэрскай лаўры, пакуль не былі ўрачыста перанесены ў Полацк.",
        "ru": "Внучка полоцкого князя Всеслава Чародея. Выдающаяся просветительница Полоцкого княжества. Основала монастырь, скриптории и школы, заказала знаменитый напрестольный Крест Евфросинии Полоцкой (1161 г.). Скончалась во время паломничества в Иерусалиме. Её мощи более семи веков (1187–1910) покоились в Киево-Печерской лавре перед перенесением в Полоцк.",
        "en": "Granddaughter of Prince Usiaslaw the Sorcerer. Leading intellectual and spiritual leader of 12th-century Polotsk. Founded monasteries, female schools, scriptoriums, and commissioned the iconic Cross of Saint Euphrosyne by Lazar Bohsha (1161). Died on pilgrimage in Jerusalem; her holy relics rested in the Kyiv-Pechersk Lavra for over seven centuries (1187–1910) before returning to Polotsk."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Euphrosyne_of_Polotsk_icon.jpg/330px-Euphrosyne_of_Polotsk_icon.jpg",
    "wiki": "https://be.wikipedia.org/wiki/Еўфрасіння_Полацкая",
    "placeIds": ["kyiv-pechersk-lavra-hleb-minskirad"]
})

# 2. PERSON: Santi Gucci
upsert_person({
    "id": "santi-gucci",
    "name": {
        "by": "Санці Гучы",
        "ru": "Санти Гуччи",
        "en": "Santi Gucci"
    },
    "dates": "~1530 — ~1600",
    "role": {
        "by": "Фларэнційскі архітэктар і скульптар эпохі маньерызму і Рэнесансу, прыдворны майстар ВКЛ і Рэчы Паспалітай",
        "ru": "Флорентийский архитектор и скульптор эпохи Возрождения и маньеризма, придворный мастер в ВКЛ и Польше",
        "en": "Florentine architect and sculptor of the Renaissance and Mannerism, court master in the GDL and Poland"
    },
    "bio": {
        "by": "Ураджэнец Фларэнцыі. Адзін з найвыдатнейшых майстроў Рэнесансу і маньерызму, які працаваў у землях Вялікага Княства Літоўскага і Польшчы пры дварах Стэфана Баторыя і Ганны Ягелонкі. Аўтар грандыёзнага маўзалея-надмагілля вялікай княгіні літоўскай і каралевы Боны Сфорцы ў базіліцы Святога Мікалая ў Бары (Італія, 1593), а таксама надмагілляў і замкаў у Вільні, Кракаве і Ксёнжы Вельскім.",
        "ru": "Уроженец Флоренции. Один из ведущих мастеров эпохи Возрождения и маньеризма, придворный скульптор и архитектор Стефана Батория и Анны Ягеллонки. Создатель монументального надгробия Боны Сфорца в базилике Святого Николая в Бари (Италия, 1593 г.), а также ряда замков и усыпальниц в ВКЛ и Польше.",
        "en": "Born in Florence. Preeminent Florentine Mannerist architect and sculptor who became court artist to King Stefan Batory and Queen Anna Jagiellon. Sculpted the monumental Renaissance mausoleum of Grand Duchess of Lithuania Bona Sforza in the Basilica of Saint Nicholas in Bari, Italy (1593)."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Bona_Sforza_tomb_IMG_4657.jpg/960px-Bona_Sforza_tomb_IMG_4657.jpg",
    "wiki": "https://be.wikipedia.org/wiki/Санці_Гучы",
    "placeIds": ["bari-basilica-san-nicola-bona-sforza-tomb", "florence-city-hub"]
})

# 3. PERSON: Mikolaj Krzysztof Radziwill "Sirotka"
upsert_person({
    "id": "radziwill-sirotka",
    "name": {
        "by": "Мікалай Крыштаф Радзівіл «Сіротка»",
        "ru": "Николай Христофор Радзивилл «Сиротка»",
        "en": "Mikołaj Krzysztof Radziwiłł \"the Orphan\""
    },
    "dates": "1549 — 1616",
    "role": {
        "by": "Дзяржаўны і вайсковы дзеяч ВКЛ, пісьменнік, мецэнат, фундатар Нясвіжскага замка і Радзівілаўскай карты",
        "ru": "Государственный деятель ВКЛ, путешественник, меценат, создатель Несвижского замка и карты ВКЛ 1613 года",
        "en": "Grand Marshal of Lithuania, traveler, patron of arts, creator of Nesvizh Castle and the 1613 GDL Map"
    },
    "bio": {
        "by": "Князь, маршалак вялікі літоўскі, ваявода віленскі. Фундатар Нясвіжскага замка, касцёла Божага Цела і калегіума езуітаў у Нясвіжы. У 1582–1584 гг. здзейсніў знакамітую пілігрымку ў Іерусалім, Егіпет і па Італіі, апісаўшы яе ў папулярнай па ўсёй Еўропе кнізе «Перэгрынацыя». Ініцыятар і фундатар стварэння першай высокадакладнай карты ВКЛ (1613), выгравіраванай Тамашам Макоўскім.",
        "ru": "Государственный и военный деятель ВКЛ, воевода виленский. Превратил Несвиж в каменную европейскую резиденцию. В 1582–1584 гг. совершил путешествие в Палестину, Египет и Италию, написав знаменитую «Перегринацию». Финансировал создание первой фундаментальной карты ВКЛ (1613 г.).",
        "en": "Grand Marshal of Lithuania, Voivode of Vilnius, lord of Nesvizh. Transformed Nesvizh into a Renaissance center. Chronicled his 1582–1584 journey across Italy, Egypt, and the Holy Land in 'Peregrination'. Commissioned Tomasz Makowski to engrave the landmark 1613 Radziwill Map of the Grand Duchy of Lithuania."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Mika%C5%82aj_Kry%C5%A1taf_Radzivi%C5%82_Sirotka._%D0%9C%D1%96%D0%BA%D0%B0%D0%BB%D0%B0%D0%B9_%D0%9A%D1%80%D1%8B%D1%88%D1%82%D0%B0%D1%84_%D0%A0%D0%B0%D0%B4%D0%B7%D1%96%D0%B2%D1%96%D0%BB_%D0%A1%D1%96%D1%80%D0%BE%D1%82%D0%BA%D0%B0_%28XVII%29.jpg/330px-Mika%C5%82aj_Kry%C5%A1taf_Radzivi%C5%82_Sirotka._%D0%9C%D1%96%D0%BA%D0%B0%D0%BB%D0%B0%D0%B9_%D0%9A%D1%80%D1%8B%D1%88%D1%82%D0%B0%D1%84_%D0%A0%D0%B0%D0%B4%D0%B7%D1%96%D0%B2%D1%96%D0%BB_%D0%A1%D1%96%D1%80%D0%BE%D1%82%D0%BA%D0%B0_%28XVII%29.jpg",
    "wiki": "https://be.wikipedia.org/wiki/Мікалай_Крыштаф_Радзівіл_Сіротка",
    "placeIds": ["florence-city-hub", "uppsala-carolina-rediviva-belarustreasures"]
})

# 4. Update Bona Sforza tomb place to link Santi Gucci
bona_tomb = next((p for p in places if p['id'] == 'bari-basilica-san-nicola-bona-sforza-tomb'), None)
if bona_tomb:
    if 'santi-gucci' not in bona_tomb.get('personIds', []):
        bona_tomb.setdefault('personIds', []).append('santi-gucci')

# 5. CITY COMPOSITE HUB: Florence (Фларэнцыя)
upsert_place({
    "id": "florence-city-hub",
    "title": {
        "by": "Фларэнцыя — беларускія і рэнесансныя сляды (комплексны аб’ект)",
        "ru": "Флоренция — белорусские и ренессансные следы (комплексный объект)",
        "en": "Florence — Belarusian & Renaissance Footprints (City Hub)"
    },
    "category": "city",
    "country": {
        "by": "Італія",
        "ru": "Италия",
        "en": "Italy"
    },
    "city": {
        "by": "Фларэнцыя",
        "ru": "Флоренция",
        "en": "Florence"
    },
    "coordinates": [
        43.7696,
        11.2558
    ],
    "description": {
        "by": "Сталіца Тасканы і калыска еўрапейскага Рэнесансу, з якой звязаны выбітныя постаці і падзеі гісторыі Беларусі і Вялікага Княства Літоўскага. Тут нарадзіўся і сфармаваўся вялікі скульптар Санці Гучы, які ствараў шэдэўры для каралёў Рэчы Паспалітай і пахаванне Боны Сфорцы. У 1582 г. Фларэнцыю наведаў князь Мікалай Крыштаф Радзівіл «Сіротка», якога ўрачыста прымаў вялікі герцаг тасканскі Франчэска I Медычы. Таксама тут бываў і вывучаў мастацтва вялікі гетман літоўскі Міхал Казімір Агінскі.",
        "ru": "Колыбель европейского Возрождения, тесно связанная с культурной историей Беларуси и ВКЛ. Родина скульптора Санти Гуччи, творившего для королей и магнатов ВКЛ. В 1582 году город посетил князь Николай Христофор Радзивилл «Сиротка», принятый герцогом Медичи. Город также посещал великий гетман литовский и композитор Михаил Казимир Огинский.",
        "en": "Cradle of the Italian Renaissance with deep historic connections to Belarus and the Grand Duchy of Lithuania. Birthplace of master sculptor Santi Gucci, who crafted monuments for GDL royalty including Bona Sforza's tomb. Visited in 1582 by Prince Mikołaj Krzysztof Radziwiłł 'the Orphan' during his pilgrimage, where he was received by Grand Duke Francesco I de' Medici, as well as Grand Hetman Michał Kazimierz Ogiński."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Florence_Duomo_from_Michelangelo_esplanade.jpg/960px-Florence_Duomo_from_Michelangelo_esplanade.jpg",
    "links": [
        {
            "title": "Фларэнцыя — Вікіпедыя",
            "url": "https://be.wikipedia.org/wiki/Фларэнцыя"
        },
        {
            "title": "Санці Гучы — Вікіпедыя",
            "url": "https://be.wikipedia.org/wiki/Санці_Гучы"
        },
        {
            "title": "Мікалай Крыштаф Радзівіл Сіротка — Вікіпедыя",
            "url": "https://be.wikipedia.org/wiki/Мікалай_Крыштаф_Радзівіл_Сіротка"
        }
    ],
    "tags": [
        "Італія",
        "Фларэнцыя",
        "Рэнесанс",
        "Санці Гучы",
        "Радзівіл Сіротка",
        "Агінскі",
        "комплексны аб’ект",
        "city"
    ],
    "personId": "santi-gucci",
    "personIds": [
        "santi-gucci",
        "radziwill-sirotka",
        "michal-kazimir-oginski"
    ],
    "unverifiedCoordinates": False,
    "isCityHub": True,
    "items": [
        {
            "id": "florence-birthplace-santi-gucci",
            "title": "Месца нараджэння і сталення каралеўскага дойліда Санці Гучы",
            "author": "Санці Гучы",
            "person": "Санці Гучы",
            "personId": "santi-gucci",
            "year": "каля 1530 г.",
            "description": "Санці Гучы нарадзіўся ў сям'і фларэнційскага разьбяра і архітэктара Джавані Гучы. Атрымаў выдатную мастацкую адукацыю ў майстэрнях Фларэнцыі, адкуль быў запрошаны ў землі Рэчы Паспалітай і ВКЛ. Стварыў непаўторныя помнікі высокага маньерызму і Рэнесансу, у тым ліку надмагілле Боны Сфорцы ў Бары і пахаванні ў Кракаве і Вільні.",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Bona_Sforza_tomb_IMG_4657.jpg/960px-Bona_Sforza_tomb_IMG_4657.jpg",
            "wikiUrl": "https://be.wikipedia.org/wiki/Санці_Гучы"
        },
        {
            "id": "florence-visit-radziwill-sirotka",
            "title": "Візіт князя Мікалая Крыштафа Радзівіла «Сіроткі» і прыём у герцага Медычы",
            "author": "Мікалай Крыштаф Радзівіл «Сіротка»",
            "person": "Мікалай Крыштаф Радзівіл «Сіротка»",
            "personId": "radziwill-sirotka",
            "year": "1582 г.",
            "description": "Па дарозе ў Святую Зямлю князь Сіротка прыбыў у Фларэнцыю, дзе быў з найвышэйшай пашанай прыняты вялікім герцагам тасканскім Франчэска I Медычы. Сіротка аглядаў мастацкія скарбы палацаў Медычы і знакамітыя сады, што натхніла яго на стварэнне рэнесанснага палацава-паркавага ансамбля ў Нясвіжы.",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Mika%C5%82aj_Kry%C5%A1taf_Radzivi%C5%82_Sirotka._%D0%9C%D1%96%D0%BA%D0%B0%D0%BB%D0%B0%D0%B9_%D0%9A%D1%80%D1%8B%D1%88%D1%82%D0%B0%D1%84_%D0%A0%D0%B0%D0%B4%D0%B7%D1%96%D0%B2%D1%96%D0%BB_%D0%A1%D1%96%D1%80%D0%BE%D1%82%D0%BA%D0%B0_%28XVII%29.jpg/330px-Mika%C5%82aj_Kry%C5%A1taf_Radzivi%C5%82_Sirotka._%D0%9C%D1%96%D0%BA%D0%B0%D0%BB%D0%B0%D0%B9_%D0%9A%D1%80%D1%8B%D1%88%D1%82%D0%B0%D1%84_%D0%A0%D0%B0%D0%B4%D0%B7%D1%96%D0%B2%D1%96%D0%BB_%D0%A1%D1%96%D1%80%D0%BE%D1%82%D0%BA%D0%B0_%28XVII%29.jpg",
            "wikiUrl": "https://be.wikipedia.org/wiki/Мікалай_Крыштаф_Радзівіл_Сіротка"
        },
        {
            "id": "florence-visit-michal-kazimir-oginski",
            "title": "Знаходжанне і вывучэнне оперы вялікім гетманам Міхалам Казімірам Агінскім",
            "author": "Міхал Казімір Агінскі",
            "person": "Міхал Казімір Агінскі",
            "personId": "michal-kazimir-oginski",
            "year": "1760-я гг.",
            "description": "Вялікі гетман літоўскі, кампазітар, паэт і інжынер Міхал Казімір Агінскі правёў у Фларэнцыі і гарадах Італіі працяглы час, захапляючыся італьянскай операй і тэатральнай сцэнаграфіяй. Гэты фларэнційскі вопыт пазней увасобіўся ў яго знакамітым Слонімскім прыдворным тэатры («Сядзібе музаў») з «плаваючым тэатрам» і сімфанічным аркестрам.",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Micha%C5%82_Kazimierz_Ogi%C5%84ski.jpg/330px-Micha%C5%82_Kazimierz_Ogi%C5%84ski.jpg",
            "wikiUrl": "https://be.wikipedia.org/wiki/Міхал_Казімір_Агінскі"
        }
    ]
})

# Save files
with open('data/places.json', 'w', encoding='utf-8') as f:
    json.dump(places, f, ensure_ascii=False, indent=2)
with open('data/places.js', 'w', encoding='utf-8') as f:
    f.write('// Albaruthenica Places Dataset\nwindow.INITIAL_PLACES = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

with open('data/persons.json', 'w', encoding='utf-8') as f:
    json.dump(persons, f, ensure_ascii=False, indent=2)
with open('data/persons.js', 'w', encoding='utf-8') as f:
    f.write('// Albaruthenica Persons Dataset\nwindow.INITIAL_PERSONS = ' + json.dumps(persons, ensure_ascii=False, indent=2) + ';\n')

print(f"Total places: {len(places)}, Total persons: {len(persons)}")
