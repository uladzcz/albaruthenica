import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Load files
with open('data/persons.json', 'r', encoding='utf-8') as f:
    persons = json.load(f)

with open('data/places.json', 'r', encoding='utf-8') as f:
    places = json.load(f)

# Merge Suprasl duplicate if exists
suprasl_old = next((p for p in places if p['id'] == 'suprasl-monastery'), None)
suprasl_new = next((p for p in places if p['id'] == 'suprasl-annunciation-monastery'), None)
if suprasl_old and suprasl_new:
    places = [p for p in places if p['id'] != 'suprasl-monastery']
    print("Merged and removed older suprasl duplicate.")

# Add new persons
new_persons_podlasie = [
    {
        "id": "ihnat-hryniavicki",
        "name": {
            "by": "Ігнат Грынявіцкі",
            "ru": "Игнатий Гриневицкий",
            "en": "Ignacy Hryniewiecki (Ihnat Hryniavicki)"
        },
        "role": {
            "by": "Рэвалюцыянер-нарадаволец, выпускнік Беластоцкай гімназіі",
            "ru": "Революционер-народоволец, выпускник Белостокской гимназии",
            "en": "Revolutionary Narodovolets, graduate of the Białystok Gymnasium"
        },
        "dates": "1856–1881",
        "bio": {
            "by": "Нарадзіўся ў фальварку Басін Бабруйскага павета Мінскай губерні ў шляхецкай сям'і. З адзнакай скончыў Беластоцкую гімназію (1875) і паступіў у Пецярбургскі тэхналагічны інстытут. Адзін з заснавальнікаў беларускай фракцыі «Народнай волі», называў сябе літвінам. 1 сакавіка 1881 года ў Пецярбургу кінуў смяротную бомбу пад ногі цара Аляксандра II, загінуўшы ад выбуху сам.",
            "ru": "Родился в имении Басин Бобруйского уезда. С отличием окончил Белостокскую гимназию (1875). Член исполкома «Народной воли», стоял у истоков создания белорусской фракции организации. 1 марта 1881 года смертельно ранил императора Александра II брошенной бомбой, погибнув на месте.",
            "en": "Born in Basin, Bobruysk district (Belarus). Graduated with highest honors from the Białystok Gymnasium (1875). Core member of Narodnaya Volya who initiated its Belarusian circle. On 1 March 1881 in Saint Petersburg, threw the bomb that mortally wounded Tsar Alexander II, dying in the explosion."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Ignacy_Hryniewiecki.jpg/440px-Ignacy_Hryniewiecki.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%86%D0%B3%D0%BD%D0%B0%D1%82_%D0%93%D1%80%D1%8B%D0%BD%D1%8F%D0%B2%D1%96%D1%86%D0%BA%D1%96"
    },
    {
        "id": "tamara-salanevich",
        "name": {
            "by": "Тамара Саланевіч",
            "ru": "Тамара Солоневич",
            "en": "Tamara Sołoniewicz"
        },
        "role": {
            "by": "Выдатная беларуская рэжысёрка-дакументалістка і журналістка з Падляшша",
            "ru": "Белорусский режиссёр-документалист и журналист из Подляшья",
            "en": "Distinguished Belarusian documentary filmmaker and journalist from Podlasie"
        },
        "dates": "1938–2000",
        "bio": {
            "by": "Нарадзілася ў Нараўцы на Беласточчыне. Выдатная польская і беларуская рэжысёрка-дакументалістка, аўтарка дзясяткаў знакавых фільмаў пра лёс, культуру, мову і самабытны свет беларусаў Падляшша («Крэсовая палечка», «Чорныя зоры», «Чалавек з зямлі», «Сям'я»). У Беластоку яе імем названы сквер у гістарычным раёне Бояры.",
            "ru": "Родилась в Наревке на Подляшье. Выдающийся режиссёр документального кино, автор классических фильмов о традициях и самосознании подляшских белорусов («Кресовая полечка», «Чёрные зори»). В Белостоке её именем назван сквер в районе Бояры.",
            "en": "Born in Narewka (Podlasie). Celebrated documentary filmmaker and chronicler of the Belarusian minority in Poland. Her films ('Kresowa poleczka', 'Black Dawn', 'Man from the Earth') captured the living culture and dialect of Podlasie. A public square in Białystok bears her name."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Portrait_Placeholder.png/440px-Portrait_Placeholder.png",
        "wiki": "https://be.wikipedia.org/wiki/%D0%A2%D0%B0%D0%BC%D0%B0%D1%80%D0%B0_%D0%A1%D0%B0%D0%BB%D0%B0%D0%BD%D0%B5%D0%B2%D1%96%D1%87"
    },
    {
        "id": "mikola-hajduk",
        "name": {
            "by": "Мікола Гайдук",
            "ru": "Николай Гайдук",
            "en": "Mikoła Hajduk"
        },
        "role": {
            "by": "Беларускі пісьменнік, фалькларыст і педагог на Падляшшы",
            "ru": "Белорусский писатель, фольклорист и педагог на Подляшье",
            "en": "Belarusian writer, folklorist, and educator in Podlasie"
        },
        "dates": "1933–1998",
        "bio": {
            "by": "Нарадзіўся ў вёсцы Кабыляны на Беласточчыне. Выбітны дзеяч беларускай культуры ў Польшчы, пісьменнік, краязнавец, публіцыст і настаўнік. Выкладаў беларускую мову ў Беларускім ліцэі ў Бельску Падляскім, сабраў сотні ўнікальных народных казак і легенд Падляшша. Яго імя носіць Пачатковая школа №3 з беларускай мовай навучання ў Бельску Падляскім.",
            "ru": "Родился в Кобылянах на Подляшье. Деятель белорусской культуры Польши, фольклорист, преподаватель Белорусского лицея в Бельске-Подляском. Автор сборников легенд и сказок Белосточчины. Его имя носит школа №3 в Бельске-Подляском.",
            "en": "Born in Kobylany (Podlasie). Renowned educator, folklorist, and author who collected oral traditions and taught at the Belarusian Lyceum in Bielsk Podlaski. Primary School No. 3 in Bielsk Podlaski is named in his honor."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Portrait_Placeholder.png/440px-Portrait_Placeholder.png",
        "wiki": "https://be.wikipedia.org/wiki/%D0%9C%D1%96%D0%BA%D0%BE%D0%BB%D0%B0_%D0%93%D0%B0%D0%B9%D0%B4%D1%83%D0%BA"
    }
]

existing_person_ids = {p['id'] for p in persons}
for np in new_persons_podlasie:
    if np['id'] not in existing_person_ids:
        persons.append(np)
        existing_person_ids.add(np['id'])
        print(f"Added person {np['id']}")

# New places
new_places_podlasie = [
    {
        "id": "bialystok-warszawska-11-bgkt",
        "title": {
            "by": "Беларускае грамадска-культурнае таварыства (БГКТ, вул. Варшаўская 11, Беласток)",
            "ru": "Белорусское общественно-культурное общество (БОКО, ул. Варшавская 11, Белосток)",
            "en": "Belarusian Socio-Cultural Association (BTSK, Warszawska 11, Białystok)"
        },
        "category": "culture",
        "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
        "city": {"by": "Беласток", "ru": "Белосток", "en": "Bialystok"},
        "coordinates": [53.1344, 23.1691],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Ulica_Warszawska_w_Bia%C5%82ymstoku.jpg/640px-Ulica_Warszawska_w_Bia%C5%82ymstoku.jpg",
        "description": {
            "by": "Гістарычная галоўная сядзіба Беларускага грамадска-культурнага таварыства ў Польшчы (БГКТ), заснаванага ў 1956 годзе. Найстарэйшая дзеючая арганізацыя беларускай нацыянальнай меншасці ў Польшчы. На працягу дзесяцігоддзяў гэты будынак на вуліцы Варшаўскай з'яўляецца цэнтрам грамадскага, культурнага і асветніцкага жыцця беларусаў Падляшша, арганізатарам агульнапольскіх фестываляў беларускай песні і літаратурных сустрэч.",
            "ru": "Главная штаб-квартира Белорусского общественно-культурного общества в Польше (БОКО / БГКТ), созданного в 1956 году. Старейшая организация белорусского меньшинства в Польше, центр культурной жизни Подляшья.",
            "en": "Headquarters of the Belarusian Socio-Cultural Association in Poland (BTSK / БГКТ), founded in 1956. The oldest continuous institutional organization of the Belarusian national minority in Poland, hosting cultural festivals, choirs, and literary gatherings."
        },
        "mustSee": True,
        "links": [
            {"title": "Беларускае грамадска-культурнае таварыства (Вікіпедыя)", "url": "https://be.wikipedia.org/wiki/%D0%91%D0%B5%D0%BB%D0%B0%D1%80%D1%83%D1%81%D0%BA%D0%B0%D0%B5_%D0%B3%D1%80%D0%B0%D0%BC%D0%B0%D0%B4%D1%81%D0%BA%D0%B0-%D0%BA%D1%83%D0%BB%D1%8C%D1%82%D1%83%D1%80%D0%BD%D0%B0%D0%B5_%D1%82%D0%B0%D0%B2%D0%B0%D1%80%D1%8B%D1%81%D1%82%D0%B2%D0%BE"}
        ]
    },
    {
        "id": "bialystok-redakcyja-niwa",
        "title": {
            "by": "Рэдакцыя штотыднёвіка «Ніва» / Праграмная рада «Ніва» (вул. Заменгофа 27, Беласток)",
            "ru": "Редакция еженедельника «Нива» / Программный совет «Нива» (ул. Заменгофа 27, Белосток)",
            "en": "Editorial Office of Weekly 'Niva' (ul. Zamenhofa 27, Białystok)"
        },
        "category": "culture",
        "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
        "city": {"by": "Беласток", "ru": "Белосток", "en": "Bialystok"},
        "coordinates": [53.1317, 23.1594],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Tygodnik_Niwa_logo.png/440px-Tygodnik_Niwa_logo.png",
        "description": {
            "by": "Рэдакцыя найстарэйшага і найбуйнейшага беларускага штотыднёвіка «Ніва», які няспынна выдаецца ў Беластоку з 1956 года чыстай беларускай літаратурнай мовай. Галоўны летапіс і інтэлектуальны асяродак беларусаў Польшчы, пры якім паўстала Беларускае літаратурнае аб'яднанне «Белавежа» (Сакрат Яновіч, Надзея Артымовіч, Віталь Луба, Яўген Вапа). Пры рэдакцыі дзейнічае знанае кніжнае выдавецтва.",
            "ru": "Редакция старейшего еженедельника белорусов Польши «Нива», издающегося с 1956 года на белорусском языке. Летопись белорусской жизни Подляшья, колыбель литературного объединения «Беловежа» (Сократ Янович).",
            "en": "Editorial headquarters of 'Niva', the foremost Belarusian-language weekly in Poland published continuously since 1956. The intellectual hub of the Podlasie Belarusian community and cradle of the 'Białowieża' literary association (Sokrat Janowicz, Eugeniusz Wappa)."
        },
        "mustSee": True,
        "links": [
            {"title": "Ніва (штотыднёвік) (Вікіпедыя)", "url": "https://be.wikipedia.org/wiki/%D0%9D%D1%96%D0%B2%D0%B0_(%D1%88%D1%82%D1%8B%D0%B4%D0%BD%D1%96%D0%B2%D1%96%D0%BA)"}
        ]
    },
    {
        "id": "bialystok-gimnazija-vi-lo",
        "title": {
            "by": "Беластоцкая гімназія / VI Агульнаадукацыйны ліцэй (вул. Касцельная 9, Беласток)",
            "ru": "Белостокская гимназия / VI Общеобразовательный лицей (ул. Костельная 9, Белосток)",
            "en": "Białystok Gymnasium / VI Lyceum (ul. Kościelna 9, Białystok)"
        },
        "category": "historical",
        "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
        "city": {"by": "Беласток", "ru": "Белосток", "en": "Bialystok"},
        "coordinates": [53.1332, 23.1633],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Ignacy_Hryniewiecki.jpg/440px-Ignacy_Hryniewiecki.jpg",
        "description": {
            "by": "Гістарычны будынак Беластоцкай гімназіі (пазней Беластоцкае рэальнае вучылішча, цяпер VI LO імя Жыгімонта Аўгуста на вул. Касцельнай). Тут навучаліся выдатныя дзеячы: лепшы выпускнік 1875 г. Ігнат Грынявіцкі (нарадаволец, які здзейсніў замах на цара Аляксандра II і ствараў беларускую фракцыю арганізацыі); палкоўнік Мікалай Дзямідаў (выпускнік 1910 г., камендант Гродна ад БНР, камандзір Беларускага асобнага батальёна); і стваральнік эсперанта Людвік Заменгоф.",
            "ru": "Историческое здание Белостокской гимназии (ныне VI лицей). Здесь учились: лучший выпускник 1875 года Игнатий Гриневицкий (народоволец, совершивший покушение на Александра II); комендант Гродно от БНР полковник Николай Демидов (выпускник 1910 года); создатель эсперанто Людвик Заменгоф.",
            "en": "Historic building of the Białystok Gymnasium (now the VI King Zygmunt August Lyceum on ul. Kościelna). Notable alumni include 1875 top graduate Ignacy Hryniewiecki (Narodnaya Volya member who assassinated Tsar Alexander II); BNR military commandant of Grodno Mikołaj Demidov; and Esperanto creator L. L. Zamenhof."
        },
        "personIds": ["ihnat-hryniavicki"],
        "mustSee": True,
        "links": [
            {"title": "Беларускія месцы Беластока: гімназія (MOST Media)", "url": "https://mostmedia.io/2023/03/30/belaruskija-mescy-belastoka-gimnazija/"}
        ]
    },
    {
        "id": "bialystok-skver-tamary-salanevich",
        "title": {
            "by": "Сквер Тамары Саланевіч (гістарычны раён Бояры, Беласток)",
            "ru": "Сквер Тамары Солоневич (исторический район Бояры, Белосток)",
            "en": "Tamara Sołoniewicz Square (Bojary District, Białystok)"
        },
        "category": "monument",
        "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
        "city": {"by": "Беласток", "ru": "Белосток", "en": "Bialystok"},
        "coordinates": [53.1367, 23.1742],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Portrait_Placeholder.png/440px-Portrait_Placeholder.png",
        "description": {
            "by": "Сквер у гістарычным драўляным раёне Бояры ў Беластоку (скрыжаванне вуліц Варшаўскай, Пясчанай і Старабаярскай), урачыста названы ў гонар Тамары Саланевіч (1938–2000) — славутай беларускай кінарэжысёркі-дакументалісткі з Нараўкі. Аўтарка знакавых кінастужак пра самабытную народную культуру, свядомасць і лёс падляшскіх беларусаў («Крэсовая палечка», «Чорныя зоры», «Чалавек з зямлі»).",
            "ru": "Сквер в районе Бояры в Белостоке, названный в честь Тамары Солоневич (1938–2000) — выдающегося белорусского режиссёра документального кино родом из Наревки, автора классических фильмов о традициях и людях Подляшья.",
            "en": "Public square in the historic wooden Bojary district of Białystok, named after Tamara Sołoniewicz (1938–2000), a renowned Belarusian documentary filmmaker from Narewka whose acclaimed films captured the soul and oral heritage of the Podlasie Belarusians."
        },
        "personIds": ["tamara-salanevich"],
        "links": [
            {"title": "Сквер Тамары Саланевіч (MOST Media)", "url": "https://mostmedia.io/2022/02/23/skver-tamary-salanevich/"}
        ]
    },
    {
        "id": "hajnowka-ii-lo-belaruski-licej",
        "title": {
            "by": "Беларускі ліцэй у Гайнаўцы (II LO z Dodatkową Nauką Języka Białoruskiego)",
            "ru": "Белорусский лицей в Гайновке (II LO z Dodatkową Nauką Języka Białoruskiego)",
            "en": "Belarusian Lyceum in Hajnówka (II LO with Belarusian Language Instruction)"
        },
        "category": "culture",
        "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
        "city": {"by": "Гайнаўка", "ru": "Гайновка", "en": "Hajnowka"},
        "coordinates": [52.7431, 23.5822],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/II_Liceum_Og%C3%B3lnokszta%C5%82c%C4%85ce_w_Hajn%C3%B3wce.jpg/640px-II_Liceum_Og%C3%B3lnokszta%C5%82c%C4%85ce_w_Hajn%C3%B3wce.jpg",
        "description": {
            "by": "Агульнаадукацыйны ліцэй з дадатковым навучаннем беларускай мовы ў Гайнаўцы (вул. Пілсудскага 3), заснаваны ў 1949 годзе. Адзін з двух унікальных ліцэяў у Польшчы, дзе ўсе вучні вывучаюць беларускую мову, літаратуру і гісторыю. Сярод выпускнікоў — сотні беларускіх дзеячаў, навукоўцаў, журналістаў і педагогаў Польшчы. Асяродак рэгіянальнага конкурсу «Зорка» і моладзевай беларускай культуры.",
            "ru": "Общеобразовательный лицей с дополнительным обучением белорусскому языку в Гайновке, основанный в 1949 году. Один из двух белорусских лицеев в Польше, где поколения учеников изучают белорусский язык, литературу и историю.",
            "en": "General secondary school with supplementary Belarusian language education in Hajnówka, founded in 1949. One of two specialized lyceums in Poland where students study Belarusian language, literature, and history, shaping the cultural vanguard of Podlasie."
        },
        "mustSee": True,
        "links": [
            {"title": "Liceum z Dodatkową Nauką Języka Białoruskiego w Hajnówce (Вікіпедыя)", "url": "https://pl.wikipedia.org/wiki/Liceum_Og%C3%B3lnokszta%C5%82c%C4%85ce_z_Dodatkow%C4%85_Nauk%C4%85_J%C4%99zyka_Bia%C5%82oruskiego_w_Hajn%C3%B3wce"}
        ]
    },
    {
        "id": "bielsk-podlaski-szkola-3-hajduk",
        "title": {
            "by": "Беларуская пачатковая школа №3 імя Міколы Гайдука ў Бельску Падляскім",
            "ru": "Белорусская начальная школа №3 имени Николая Гайдука в Бельске-Подляском",
            "en": "Primary School No. 3 im. Mikołaja Hajduka with Belarusian Language (Bielsk Podlaski)"
        },
        "category": "culture",
        "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
        "city": {"by": "Бельск Падляскі", "ru": "Бельск-Подляски", "en": "Bielsk Podlaski"},
        "coordinates": [52.7719, 23.1956],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Portrait_Placeholder.png/440px-Portrait_Placeholder.png",
        "description": {
            "by": "Пачатковая школа №3 з дадатковым навучаннем беларускай мовы ў Бельску Падляскім (вул. Панятоўскага 9). Носіць імя выдатнага беларускага пісьменніка, краязнаўца, фалькларыста і настаўніка Міколы Гайдука (1933–1998). Тут выкладаецца беларуская мова, дзеці вывучаюць традыцыі Падляшша, дзейнічаюць беларускія фальклорныя і тэатральныя калектывы.",
            "ru": "Начальная школа №3 с обучением белорусскому языку в Бельске-Подляском. Носит имя писателя, фольклориста и педагога Николая Гайдука. Дети изучают белорусский язык и традиции родного края.",
            "en": "Primary School No. 3 in Bielsk Podlaski with supplementary Belarusian language instruction, named after Belarusian author and folklorist Mikoła Hajduk (1933–1998). Teaches Belarusian language, regional heritage, and folklore."
        },
        "personIds": ["mikola-hajduk"],
        "links": [
            {"title": "Szkoła Podstawowa nr 3 w Bielsku Podlaskim", "url": "https://trojka.szkolnastrona.pl/p,1,szkola"}
        ]
    },
    {
        "id": "studziwody-muzej-maloj-backauszcyny",
        "title": {
            "by": "Музей малой бацькаўшчыны ў Студзіводах (Stowarzyszenie ABBA, Бельск Падляскі)",
            "ru": "Музей малой родины в Студиводах (Stowarzyszenie ABBA, Бельск-Подляски)",
            "en": "Museum of the Small Homeland in Studziwody (ABBA Association, Bielsk Podlaski)"
        },
        "category": "culture",
        "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
        "city": {"by": "Бельск Падляскі", "ru": "Бельск-Подляски", "en": "Bielsk Podlaski"},
        "coordinates": [52.7564, 23.2189],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Studziwody_skansen.jpg/640px-Studziwody_skansen.jpg",
        "description": {
            "by": "Унікальны прыватны скансен і культурна-асветніцкі асяродак традыцыйнай беларускай культуры Падляшша ў гістарычным прадмесці Студзіводы (вул. Сасновая 34, Бельск Падляскі), заснаваны этнографам і гісторыкам Дарафеем Фіёнікам і таварыствам «Музей малой бацькаўшчыны» (ABBA). Складаецца з аўтэнтычных драўляных сядзіб і хат XIX–XX стст., багатага этнаграфічнага архіва, выдавецтва краязнаўчай літаратуры і знанага спеўнага фальклорнага ансамбля «Жэмэрва».",
            "ru": "Этнографический музей-скансен традиционной белорусской культуры Подляшья в предместье Студиводы (Бельск-Подляски), основанный историком Дорофеем Фиоником и ассоциацией ABBA. Включает деревянные усадьбы XIX–XX веков, богатый архив и ансамбль «Жэмерва».",
            "en": "Open-air ethnographic museum and cultural center of traditional Podlasie Belarusian heritage in Studziwody (Bielsk Podlaski), created by historian Doroteusz Fionik and the ABBA Association. Preserves wooden homesteads, vernacular crafts, publishing archives, and the 'Żemerwa' vocal ensemble."
        },
        "mustSee": True,
        "links": [
            {"title": "Stowarzyszenie Muzeum Małej Ojczyzny w Studziwodach (Facebook)", "url": "https://www.facebook.com/stowarzyszenie.abba/"}
        ]
    },
    {
        "id": "grabarka-sviataya-hara",
        "title": {
            "by": "Святая Гара Грабарка (Гара Крыжоў — галоўная святыня беларусаў Падляшша)",
            "ru": "Святая Гора Грабарка (Гора Крестов — главная святыня белорусов Подляшья)",
            "en": "Holy Mount Grabarka (Mountain of Crosses — Sacred Sanctuary of Podlasie)"
        },
        "category": "church",
        "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
        "city": {"by": "Грабарка", "ru": "Грабарка", "en": "Grabarka"},
        "coordinates": [52.4194, 23.0039],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Grabarka_Gora_Krzyzy_2011.jpg/640px-Grabarka_Gora_Krzyzy_2011.jpg",
        "description": {
            "by": "Найважнейшы духоўны праваслаўны цэнтр і святыня беларусаў Падляшша і ўсёй Польшчы, вядомы з 1710 года дзякуючы цудадзейнаму збавенню жыхароў ад эпідэміі холеры. Пагорак пакрыты дзесяткамі тысяч паклонных драўляных крыжоў, якія пілігрымы на працягу стагоддзяў прыносяць падчас свята Спаса (Перайначэння Гасподняга 19 жніўня). На вяршыні стаіць царква Перайначэння Гасподняга і дзейнічае жаночы манастыр Марфы і Марыі.",
            "ru": "Главная православная святыня и место паломничества белорусов Подляшья, известная с 1710 года. Холм покрыт десятками тысяч крестов, приносимых верующими на праздник Преображения Господня (Спас). На вершине — Преображенский храм и монастырь Марфы и Марии.",
            "en": "The spiritual heart and primary pilgrimage destination of the Orthodox Belarusians of Podlasie and Poland, revered since 1710. The sacred hill is covered with tens of thousands of votive crosses brought by pilgrims. Crowned by the Church of the Transfiguration and the Convent of Martha and Mary."
        },
        "mustSee": True,
        "links": [
            {"title": "Святая Гара Грабарка (Вікіпедыя)", "url": "https://be.wikipedia.org/wiki/%D0%93%D1%80%D0%B0%D0%B1%D0%B0%D1%80%D0%BA%D0%B0_(%D1%81%D0%B2%D1%8F%D1%82%D0%BE%D0%B5_%D0%BC%D0%B5%D1%81%D1%86%D0%B0)"},
            {"title": "Цуды і таямніцы падляшскай зямлі (СБ)", "url": "https://www.sb.by/articles/tsudy-tayamn-tsy-padlyashskay-zyaml.html"}
        ]
    }
]

existing_place_ids = {p['id'] for p in places}
added_places = 0
for np in new_places_podlasie:
    if np['id'] not in existing_place_ids:
        places.append(np)
        existing_place_ids.add(np['id'])
        added_places += 1
        print(f"Added place {np['id']}")

print(f"Added {added_places} new Podlasie places. Total places now: {len(places)}")

# Save JSON files
with open('data/persons.json', 'w', encoding='utf-8') as f:
    json.dump(persons, f, ensure_ascii=False, indent=2)

with open('data/places.json', 'w', encoding='utf-8') as f:
    json.dump(places, f, ensure_ascii=False, indent=2)

# Save JS files
with open('data/persons.js', 'w', encoding='utf-8') as f:
    f.write('window.INITIAL_PERSONS = ' + json.dumps(persons, ensure_ascii=False, indent=2) + ';\n')

with open('data/places.js', 'w', encoding='utf-8') as f:
    f.write('window.INITIAL_PLACES = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

print("Sync completed successfully.")
