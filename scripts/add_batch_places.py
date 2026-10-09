import json
import sys

def main():
    with open('data/places.json', 'r', encoding='utf-8') as f:
        places = json.load(f)

    with open('data/persons.json', 'r', encoding='utf-8') as f:
        persons = json.load(f)

    # 1. Merge Montmorency duplicate
    # Remove 'montmorency-polish-belarusian-pantheon' if present, preserve and upgrade 'montmorency-champeaux-cemetery-pantheon'
    places = [p for p in places if p['id'] != 'montmorency-polish-belarusian-pantheon']
    for p in places:
        if p['id'] == 'montmorency-champeaux-cemetery-pantheon':
            p['coordinates'] = [48.993937, 2.323383] # exact OSM node of Cimetière des Champeaux
            p['title']['by'] = "Могілкі Шампо ў Манмарансі (Пантэон эміграцыі)"
            p['title']['ru'] = "Кладбище Шампо в Монморанси (Пантеон эмиграции)"
            p['title']['en'] = "Champeaux Cemetery in Montmorency (Emigration Pantheon)"
            p['items'] = [
                {
                    "title": "Першапачатковая магіла Адама Міцкевіча і сямейны склеп Міцкевічаў",
                    "person": "Адам Міцкевіч (1798–1855)",
                    "description": "Месца першапачатковага пахавання паэта (1856–1890) да пераносу ў Вавельскі сабор; тут спачываюць яго жонка Цэліна, сын Уладзіслаў і дачка Марыя Гурэцкая.",
                    "personId": "adam-mickiewicz"
                },
                {
                    "title": "Магіла Цыпрыяна Каміля Норвіда",
                    "person": "Цыпрыян Норвід (1821–1883)",
                    "description": "Выбітны паэт, мастак і мысліцель."
                },
                {
                    "title": "Магіла Юльяна Урсына Нямцэвіча",
                    "person": "Юльян Урсын Нямцэвіч (1758–1841)",
                    "description": "Дзяржаўны дзеяч, паплечнік Касцюшкі, адзін з аўтараў Канстытуцыі 3 мая (паходзіў са Скокаў пад Брэстам).",
                    "personId": "yulian-ursyn-nyamtsevich"
                },
                {
                    "title": "Магіла Аляксандра Ходзькі",
                    "person": "Аляксандр Ходзька (1804–1891)",
                    "description": "Філамат, усходазнавец, прафесар Калеж дэ Франс (ураджэнец Крывічоў).",
                    "personId": "aleksandr-chodzko"
                },
                {
                    "title": "Магіла Леанарда Ходзькі",
                    "person": "Леанард Ходзька (1800–1871)",
                    "description": "Гісторык, публіцыст і картограф ВКЛ (ураджэнец Аборка).",
                    "personId": "leonard-chodzko"
                },
                {
                    "title": "Магіла генерала Караля Князевіча",
                    "person": "Караль Князевіч (1762–1842)",
                    "description": "Генерал паўстання 1794 г. і напалеонаўскіх войнаў."
                },
                {
                    "title": "Магіла Вацлава Пелікана",
                    "person": "Вацлаў Пелікан (1790–1873)",
                    "description": "Прафесар хірургіі, рэктар Віленскага ўніверсітэта."
                }
            ]
            p['personIds'] = ["adam-mickiewicz", "yulian-ursyn-nyamtsevich", "aleksandr-chodzko", "leonard-chodzko"]
            p['personId'] = "adam-mickiewicz"

    # Update persons referring to old montmorency ID
    for person in persons:
        if 'placeIds' in person and person['placeIds']:
            person['placeIds'] = [
                'montmorency-champeaux-cemetery-pantheon' if pid == 'montmorency-polish-belarusian-pantheon' else pid
                for pid in person['placeIds']
            ]
        if person['id'] in ["yulian-ursyn-nyamtsevich", "aleksandr-chodzko", "leonard-chodzko"]:
            if 'placeIds' not in person or not person['placeIds']:
                person['placeIds'] = []
            if 'montmorency-champeaux-cemetery-pantheon' not in person['placeIds']:
                person['placeIds'].append('montmorency-champeaux-cemetery-pantheon')

    # Update image for Touliao Mausoleum
    for p in places:
        if p['id'] == 'taiwan-touliao-faina-vakhreva-tomb':
            p['image'] = 'https://upload.wikimedia.org/wikipedia/commons/7/70/Mausoleum_of_Chiang_Ching-kuo.jpg'

    # Check which IDs already exist
    existing_ids = {p['id'] for p in places}

    new_places = [
        # --- Siemiradzki ---
        {
            "id": "rome-villino-siemiradzki-via-gaeta",
            "title": {
                "by": "Віла і майстэрня Генрыха Семірадскага ў Рыме",
                "ru": "Вилла и мастерская Генриха Семирадского в Риме",
                "en": "Villino Siemiradzki in Rome"
            },
            "category": "culture",
            "country": {"by": "Італія", "ru": "Италия", "en": "Italy"},
            "city": {"by": "Рым", "ru": "Рим", "en": "Rome"},
            "coordinates": [41.906883, 12.504786],
            "description": {
                "by": "Адрас: Via Gaeta 1 (на рагу з Viale del Castro Pretorio), Рым.\n\nПышная рэзідэнцыя і майстэрня выбітнага мастака Генрыха Семірадскага (ураджэнца шляхецкага роду з Навагрудчыны). Пабудавана ў 1881–1883 гадах па праекце архітэктара Франчэска Ацуры. Тут Семірадскі стварыў свае манументальныя шэдэўры, уключаючы «Хрысціянскую Дзірку» (1897), і прымаў эліту еўрапейскай культуры — Генрыка Сенкевіча, Ігнацыя Падарэўскага, а таксама каралеву Маргарыту. Дом быў цэнтрам культурнага жыцця да зносу ў 1939 годзе падчас перабудовы квартала.",
                "ru": "Адрес: Via Gaeta 1, Рим.\n\nВилла и мастерская Генриха Семирадского, построенная в 1881–1883 гг. архитектором Франческо Адзурри. Здесь создавались знаменитые академические полотна мастера и собирались видные деятели культуры.",
                "en": "Address: Via Gaeta 1, Rome.\n\nResidence and studio of painter Henryk Siemiradzki, built in 1881–1883 by architect Francesco Azzurri. A prominent cultural hub where Siemiradzki painted monumental canvases until the villa's demolition in 1939."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/PL_Henryk_Siemiradzki_Autoportret_nieukonczony.jpg/800px-PL_Henryk_Siemiradzki_Autoportret_nieukonczony.jpg",
            "links": [
                {"title": "Francesco Azzurri — Villino Siemiradzki (it.wikipedia)", "url": "https://it.wikipedia.org/wiki/Francesco_Azzurri"},
                {"title": "Генрых Семірадскі (be.wikipedia)", "url": "https://be.wikipedia.org/wiki/Генрых_Іпалітавіч_Семірадскі"}
            ],
            "tags": ["Італія", "Рым", "Семірадскі", "мастацтва", "culture"],
            "personId": "henryk-siemiradzki",
            "personIds": ["henryk-siemiradzki"],
            "mustSee": True
        },
        {
            "id": "strzalkow-dwor-siemiradzkiego",
            "title": {
                "by": "Сядзіба і парк Генрыха Семірадскага ў Стшалкова",
                "ru": "Усадьба и парк Генриха Семирадского в Стшалкове",
                "en": "Siemiradzki Manor and Park in Strzałków"
            },
            "category": "culture",
            "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
            "city": {"by": "Стшалкаў", "ru": "Стшалкув", "en": "Strzałków"},
            "coordinates": [51.050234, 19.496170],
            "description": {
                "by": "Сядзібна-паркавы комплекс у вёсцы Стшалкаў (гміна Радамска), які Генрых Семірадскі набыў у жніўні 1884 года як сваю летнюю рэзідэнцыю. Тут мастак праводзіў кожнае лета з сям'ёй, знаходзячы натхненне для пейзажаў і гістарычных кампазіцый. Менавіта ў гэтай сядзібе Семірадскі памёр 23 жніўня 1902 года (пазней перапахаваны ў крыпце заслужаных на Скалцы ў Кракаве). У сяле захаваўся палацава-паркавы ансамбль і мемарыяльныя знакі ў гонар мастака.",
                "ru": "Усадебно-парковый комплекс в Стшалкове под Радомско, приобретенный Генрихом Семирадским в 1884 г. как летняя резиденция. Здесь художник скончался 23 августа 1902 г.",
                "en": "Manor and park in Strzałków near Radomsko, acquired by Henryk Siemiradzki in 1884 as a summer residence. The artist passed away here on August 23, 1902."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Henryk_Siemiradzki_-_Christian_Dirce_-_Google_Art_Project.jpg/960px-Henryk_Siemiradzki_-_Christian_Dirce_-_Google_Art_Project.jpg",
            "links": [
                {"title": "Strzałków (województwo łódzkie) (pl.wikipedia)", "url": "https://pl.wikipedia.org/wiki/Strzałków_(województwo_łódzkie)"},
                {"title": "Генрых Семірадскі (be.wikipedia)", "url": "https://be.wikipedia.org/wiki/Генрых_Іпалітавіч_Семірадскі"}
            ],
            "tags": ["Польшча", "Семірадскі", "сядзіба", "culture"],
            "personId": "henryk-siemiradzki",
            "personIds": ["henryk-siemiradzki"]
        },

        # --- Yakutsk & Exiled Scholars ---
        {
            "id": "yakutsk-exiled-scholars-memorial",
            "title": {
                "by": "Мемарыял ссыльным даследчыкам Сібіры (Ян Чэрскі і Эдвард Пякарскі) у Якуцку",
                "ru": "Мемориал ссыльным исследователям Сибири (Ян Черский и Эдуард Пекарский) в Якутске",
                "en": "Memorial to Exiled Siberian Scholars (Jan Czerski and Edward Piekarski) in Yakutsk"
            },
            "category": "monument",
            "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
            "city": {"by": "Якуцк", "ru": "Якутск", "en": "Yakutsk"},
            "coordinates": [62.034869, 129.731314],
            "description": {
                "by": "Лакацыя: скрыжаванне вуліц Паяркова і Курашова, Якуцк.\n\nМемарыяльны комплекс, адкрыты ў 2001 годзе, уяўляў сабой паўкола з пяці каменных глыб з памятнымі шыльдамі на якуцкай, рускай і польскай мовах у гонар выбітных ссыльных навукоўцаў. Сярод іх — два беларусы:\n• Ян Чэрскі (1845–1892) — ураджэнец Дрысенскага павета, паўстанец 1863 года, першаадкрывальнік хрыбтоў і далін Сібіры;\n• Эдвард Пякарскі (1858–1934) — ураджэнец Ігуменскага павета, стваральнік фундаментальнага трохтамовага «Слоўніка якуцкай мовы» (~38 000 слоў), якога называюць бацькам якуцкай літаратуры.\nУ 2023 годзе мемарыял быў дэмантаваны і знішчаны расійскімі ўладамі.",
                "ru": "Перекрёсток улиц Пояркова и Курашова в Якутске. Памятный комплекс в честь ссыльных исследователей Сибири Яна Черского и Эдуарда Пекарского, демонтированный в 2023 году.",
                "en": "Intersection of Poyarkov and Kurashov Streets in Yakutsk. Former memorial to exiled scholars of Siberia, including Jan Czerski and Edward Piekarski, dismantled in 2023."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Edward_Piekarski.jpg/800px-Edward_Piekarski.jpg",
            "links": [
                {"title": "Наша Ніва: У Якуцку знішчылі помнік ссыльным з імёнамі беларусаў", "url": "https://nashaniva.com/327009"},
                {"title": "Наша Ніва: У Якуцку на месцы мемарыяла беларусам паставяць помнік герою СВА", "url": "https://nashaniva.com/394513"},
                {"title": "Ян Чэрскі (be.wikipedia)", "url": "https://be.wikipedia.org/wiki/Ян_Дамінікавіч_Чэрскі"},
                {"title": "Эдвард Пякарскі (be.wikipedia)", "url": "https://be.wikipedia.org/wiki/Эдвард_Карлавіч_Пякарскі"}
            ],
            "tags": ["Расія", "Якуцк", "Чэрскі", "Пякарскі", "Сібір", "monument"],
            "personIds": ["jan-czerski", "edward-piekarski"]
        },
        {
            "id": "cherkekh-piekarski-house-museum",
            "title": {
                "by": "Юрта-хата Эдварда Пякарскага ў Чаркёхскім музеі",
                "ru": "Юрта-дом Эдуарда Пекарского в Черкёхском музее",
                "en": "Edward Piekarski House in Cherkekh Open-Air Museum"
            },
            "category": "culture",
            "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
            "city": {"by": "Чаркёх", "ru": "Черкёх", "en": "Cherkekh"},
            "coordinates": [62.186771, 133.220428],
            "description": {
                "by": "Хата-юрта ў Чаркёхскім гісторыка-этнаграфічным музеі «Якуцкая палітссылка» (Татцінскі улус, Якуція). Тут ссыльны беларус Эдвард Пякарскі жыў у 1881–1899 гадах, дзе ў цяжкіх умовах сабраў дзясяткі тысяч слоў і стварыў свой знакаміты «Слоўнік якуцкай мовы», заклаўшы аснову пісьмовай якуцкай мовы і літаратуры.",
                "ru": "Юрта в Черкёхском музее «Якутская политссылка», где в 1881–1899 гг. жил ссыльный Эдуард Пекарский и составлял свой фундаментальный словарь якутского языка.",
                "en": "Traditional dwelling in Cherkekh open-air museum, where exiled Belarusian scholar Edward Piekarski lived from 1881 to 1899 and compiled his monumental Yakut language dictionary."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Edward_Piekarski.jpg/800px-Edward_Piekarski.jpg",
            "links": [
                {"title": "Эдвард Пякарскі (be.wikipedia)", "url": "https://be.wikipedia.org/wiki/Эдвард_Карлавіч_Пякарскі"},
                {"title": "Наша Ніва: У Якуцку знішчылі помнік ссыльным", "url": "https://nashaniva.com/327009"}
            ],
            "tags": ["Расія", "Якуція", "Пякарскі", "музей", "culture"],
            "personId": "edward-piekarski",
            "personIds": ["edward-piekarski"]
        },

        # --- Baikal & Siberian Belarusian Diaspora ---
        {
            "id": "turgenevka-belarusian-village-siberia",
            "title": {
                "by": "Вёска Тургенеўка — беларускі аазіс каля Байкала",
                "ru": "Деревня Тургеневка — белорусский оазис у Байкала",
                "en": "Turgenevka Belarusian Village near Lake Baikal"
            },
            "category": "culture",
            "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
            "city": {"by": "Тургенеўка", "ru": "Тургеневка", "en": "Turgenevka"},
            "coordinates": [53.026703, 105.668736],
            "description": {
                "by": "Вёска ў Баяндаеўскім раёне Іркуцкай вобласці, заснаваная ў 1909 годзе беларускімі перасяленцамі з Палесся падчас сталыпінскіх рэформаў. Унікальны аазіс захавання беларускай ідэнтычнасці ў Сібіры: нумары дамоў уздоўж вуліц аздоблены чырвона-белым арнаментам, дзейнічае Цэнтр беларускай культуры, мадэльная бібліятэка з беларускімі кнігамі, этнаграфічны музей беларускага побыту (кросны, аўтэнтычныя рэчы перасяленцаў). Штогод ладзіцца традыцыйнае свята «Гуканне вясны». Вёска з'яўляецца пабрацімам беларускага аграгарадка Моталь.",
                "ru": "Деревня в Баяндаевском районе Иркутской области, основанная в 1909 г. белорусскими переселенцами. Центр белорусской культуры, музей быта, библиотека, орнаменты на домах, побратим агрогородка Мотоль.",
                "en": "Village in Bayandayevsky District, Irkutsk Oblast, founded in 1909 by Belarusian settlers. Preserves Belarusian culture, architectural ornamentation, a museum of folk life, and library; twinned with Motal, Belarus."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Belarusian_ornament.svg/800px-Belarusian_ornament.svg.png",
            "links": [
                {"title": "Наша Ніва: Як нашчадак перасяленцаў зрабіў сяло каля Байкала зноў беларускім", "url": "https://nashaniva.com/393251"},
                {"title": "Тургенеўка (Іркуцкая вобласць) (be.wikipedia)", "url": "https://be.wikipedia.org/wiki/Тургенеўка_(Іркуцкая_вобласць)"},
                {"title": "Беларусы Сібіры (be.wikipedia)", "url": "https://be.wikipedia.org/wiki/Беларусы_Сібіры"}
            ],
            "tags": ["Расія", "Сібір", "Іркуцк", "Байкал", "дыяспара", "culture"],
            "mustSee": True
        },
        {
            "id": "irkutsk-cherny-society-belarusian-culture",
            "title": {
                "by": "Іркуцкае таварыства беларускай культуры імя Яна Чэрскага",
                "ru": "Иркутское товарищество белорусской культуры им. Яна Черского",
                "en": "Irkutsk Society of Belarusian Culture named after Jan Czerski"
            },
            "category": "culture",
            "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
            "city": {"by": "Іркуцк", "ru": "Иркутск", "en": "Irkutsk"},
            "coordinates": [52.280062, 104.239717],
            "description": {
                "by": "Адрас: вул. Чайкоўскага, 13, Іркуцк.\n\nРэгіянальная грамадская арганізацыя, заснаваная ў 1996 годзе Алегам Рудаковым. Арганізоўвае экспедыцыі па беларускіх вёсках Прыбайкалля (Тургенеўка, Чармшанка, Ахіны), збірае фальклор, праводзіць святы Купалля, Грамніц і Дзён беларускай культуры.",
                "ru": "Иркутское общество белорусской культуры имени Яна Черского, созданное в 1996 г. Исследует белорусскую диаспору Сибири и проводит национальные праздники.",
                "en": "Irkutsk regional society of Belarusian culture named after explorer Jan Czerski, founded in 1996 to preserve traditions and support Belarusian villages of Baikal Siberia."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Belarusian_ornament.svg/800px-Belarusian_ornament.svg.png",
            "links": [
                {"title": "Беларусы Іркуччыны (be-tarask.wikipedia)", "url": "https://be-tarask.wikipedia.org/wiki/Беларусы_Іркуччыны"},
                {"title": "Наша Ніва: Грамніцы ў Іркуцку", "url": "https://nashaniva.com/67617"},
                {"title": "Радыё Свабода: Іркуцкія беларусы", "url": "https://www.svaboda.org/a/26529674.html"}
            ],
            "tags": ["Расія", "Іркуцк", "дыяспара", "Чэрскі", "culture"],
            "personIds": ["jan-czerski"]
        },
        {
            "id": "tomsk-belarusian-community-vilenka",
            "title": {
                "by": "Перасяленчая вёска Віленка і беларускі асяродак Томшчыны",
                "ru": "Переселенческая деревня Виленка и белорусы Томской области",
                "en": "Vilenka Village and Belarusian Community of Tomsk Oblast"
            },
            "category": "culture",
            "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
            "city": {"by": "Томск", "ru": "Томск", "en": "Tomsk"},
            "coordinates": [56.469366, 84.946814],
            "description": {
                "by": "Гістарычны асяродак беларускіх перасяленцаў у Томскай губерні. На мяжы XIX–XX стагоддзяў тысячы беларускіх сялян заснавалі паселішчы на Томшчыне, у тым ліку вёску Віленка (названую ў памяць аб Віленскай губерні), а таксама паселішчы ў Шэгарскім раёне. Сёння ў Томску дзейнічае Нацыянальна-культурная аўтаномія беларусаў і створаны архіўны даведнік «Мае продкі — з Беларусі!».",
                "ru": "Исторический центр белорусских переселенцев в Томской губернии (включая деревню Виленка и Шегарский район). Национально-культурная автономия белорусов Томской области.",
                "en": "Historic Belarusian settlement in Tomsk province, including Vilenka village founded by migrants from Vilna governorate, and the modern Belarusian cultural community in Tomsk."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Belarusian_ornament.svg/800px-Belarusian_ornament.svg.png",
            "links": [
                {"title": "Белорусы в Томской области (ru.wikipedia)", "url": "https://ru.wikipedia.org/wiki/Белорусы_в_Томской_области"},
                {"title": "Афіцыйны партал: Белорусы Томска", "url": "https://belarus-tomsk.ru/"}
            ],
            "tags": ["Расія", "Томск", "Віленка", "перасяленцы", "culture"]
        },

        # --- Yanka Kupala Abroad ---
        {
            "id": "monroe-arrow-park-kupala-monument",
            "title": {
                "by": "Помнік Янку Купалу ў Ароў-Парку (Нью-Ёрк)",
                "ru": "Памятник Янке Купале в Эрроу-Парке (Нью-Йорк)",
                "en": "Yanka Kupala Monument in Arrow Park (Monroe, NY)"
            },
            "category": "monument",
            "country": {"by": "ЗША", "ru": "США", "en": "United States"},
            "city": {"by": "Монра", "ru": "Монро", "en": "Monroe"},
            "coordinates": [41.285774, -74.179269],
            "description": {
                "by": "Адрас: Arrow Park Road, Monroe, Orange County, New York, USA.\n\nБронзавы помнік класіку беларускай літаратуры Янку Купалу, усталяваны ў 1973 годзе ў мемарыяльным парку Arrow Park. Аўтар скульптуры — народны мастак Беларусі Анатоль Анікейчык. Помнік стаіць на Алеі славутых паэтаў побач з манументамі Тарасу Шаўчэнку, Уолту Уітмэну і Аляксандру Пушкіну.",
                "ru": "Памятник классику белорусской литературы Янке Купале в парке Эрроу-Парк (Монро, штат Нью-Йорк), установленный в 1973 г. Скульптор — А. Аникейчик.",
                "en": "Bronze statue of Belarusian national poet Yanka Kupala, erected in 1973 in Arrow Park (Monroe, New York). Sculpted by Anatol Anikeychyk alongside Walt Whitman, Taras Shevchenko, and Alexander Pushkin."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Janka_Kupala_1920s.jpg/800px-Janka_Kupala_1920s.jpg",
            "links": [
                {"title": "Янка Купала (be.wikipedia)", "url": "https://be.wikipedia.org/wiki/Янка_Купала"}
            ],
            "tags": ["ЗША", "Нью-Ёрк", "Купала", "помнік", "monument"],
            "personId": "yanka-kupala",
            "personIds": ["yanka-kupala"],
            "mustSee": True
        },
        {
            "id": "moscow-kutuzovsky-kupala-monument",
            "title": {
                "by": "Помнік Янку Купалу на Кутузаўскім праспекце ў Маскве",
                "ru": "Памятник Янке Купале на Кутузовском проспекте в Москве",
                "en": "Yanka Kupala Monument on Kutuzovsky Avenue in Moscow"
            },
            "category": "monument",
            "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
            "city": {"by": "Масква", "ru": "Москва", "en": "Moscow"},
            "coordinates": [55.743160, 37.539191],
            "description": {
                "by": "Адрас: Кутузаўскі праспект, 28 (сквер імя Янкі Купалы), Масква.\n\nБронзавы помнік народнаму паэту Беларусі Янку Купалу, адкрыты ў 1977 годзе да 95-годдзя з дня яго нараджэння. Скульптары — Леў і Сяргей Гумілеўскія, архітэктар — Я. Ражын.",
                "ru": "Памятник белорусскому народному поэту Янке Купале в сквере его имени на Кутузовском проспекте (д. 28) в Москве, открытый в 1977 г. Скульпторы Л. и С. Гумилевские.",
                "en": "Monument to Yanka Kupala in Moscow, unveiled in 1977 in the Kupala park along Kutuzovsky Avenue (near No. 28). Sculpted by Lev and Sergei Gumilevsky."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Janka_Kupala_1920s.jpg/800px-Janka_Kupala_1920s.jpg",
            "links": [
                {"title": "Памятник Янке Купале (Москва) (ru.wikipedia)", "url": "https://ru.wikipedia.org/wiki/Памятник_Янке_Купале_(Москва)"}
            ],
            "tags": ["Расія", "Масква", "Купала", "помнік", "monument"],
            "personId": "yanka-kupala",
            "personIds": ["yanka-kupala"]
        },
        {
            "id": "spb-university-kupala-bust",
            "title": {
                "by": "Бюст Янкі Купалы ў дворыку СПбДУ (Санкт-Пецярбург)",
                "ru": "Бюст Янки Купалы во дворе СПбГУ (Санкт-Петербург)",
                "en": "Bust of Yanka Kupala at Saint Petersburg State University"
            },
            "category": "monument",
            "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
            "city": {"by": "Санкт-Пецярбург", "ru": "Санкт-Петербург", "en": "Saint Petersburg"},
            "coordinates": [59.940166, 30.298188],
            "description": {
                "by": "Адрас: Універсітэцкая наберажная, 11 (двор філалагічнага факультэта СПбДУ), Санкт-Пецярбург.\n\nБюст Янкі Купалы, адкрыты ў 2006 годзе ў парку сучаснай скульптуры СПбДУ. Скульптар — Валяр'ян Янушкевіч. Пецярбург адыграў вырашальную ролю ў лёсе Купалы: тут ён вучыўся на агульнаадукацыйных курсах Чарняева (1909–1913), наведваў асяродак Браніслава Эпімах-Шыпілы і выдаў свае славутыя зборнікі «Гусляр» і «Шляхам жыцця».",
                "ru": "Бюст Янки Купалы в дворике филологического факультета СПбГУ, открытый в 2006 г. Скульптор В. Янушкевич.",
                "en": "Bust of Yanka Kupala in the courtyard of the Philological Faculty of Saint Petersburg State University, unveiled in 2006. Sculptor Valerian Yanushkevich."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Janka_Kupala_1920s.jpg/800px-Janka_Kupala_1920s.jpg",
            "links": [
                {"title": "Янка Купала (be.wikipedia)", "url": "https://be.wikipedia.org/wiki/Янка_Купала"}
            ],
            "tags": ["Расія", "Пецярбург", "Купала", "бюст", "monument"],
            "personId": "yanka-kupala",
            "personIds": ["yanka-kupala"]
        },

        # --- Kosciuszko in the USA ---
        {
            "id": "saratoga-national-park-kosciuszko",
            "title": {
                "by": "Фартыфікацыі Касцюшкі на полі бітвы пад Саратогай",
                "ru": "Фортификации Костюшко на поле битвы при Саратоге",
                "en": "Kosciuszko Fortifications at Saratoga National Historical Park"
            },
            "category": "historical",
            "country": {"by": "ЗША", "ru": "США", "en": "United States"},
            "city": {"by": "Стылуотэр", "ru": "Стиллуотер", "en": "Stillwater"},
            "coordinates": [42.994332, -73.632890],
            "description": {
                "by": "Адрас: Bemis Heights, Saratoga National Historical Park, Stillwater, NY, USA.\n\nМесца гістарычнага трыўмфу інжынернага генія Тадэвуша Касцюшкі. У 1777 годзе ён спраектаваў і пабудаваў умацаванні на вышынях Беміс (Bemis Heights) над ракой Гудзон, дзякуючы якім амерыканскія войскі разграмілі брытанскую армію генерала Бергойна ў бітве пад Саратогай. Гэтая перамога лічыцца пераломным момантам усёй Вайны за незалежнасць ЗША. У парку ўсталяваны мемарыяльны знак Касцюшку.",
                "ru": "Национальный исторический парк Саратога (высоты Бемис-Хайтс). Укрепления, спроектированные Тадеушем Костюшко в 1777 г., обеспечившие решающую победу в битве при Саратоге.",
                "en": "Bemis Heights at Saratoga National Historical Park, NY. American defensive fortifications expertly engineered by Thaddeus Kosciuszko in 1777, decisive in winning the Battle of Saratoga, turning the tide of the American Revolution."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Tadeusz_Kosciuszko_by_Karl_Schweisgut.jpg/800px-Tadeusz_Kosciuszko_by_Karl_Schweisgut.jpg",
            "links": [
                {"title": "Saratoga National Historical Park (NPS)", "url": "https://www.nps.gov/sara/learn/historyculture/thaddeus-kosciuszko.htm"},
                {"title": "Бітва пад Саратогай (be.wikipedia)", "url": "https://be.wikipedia.org/wiki/Бітва_пад_Саратогай"}
            ],
            "tags": ["ЗША", "Саратога", "Касцюшка", "бітва", "historical"],
            "personId": "tadeusz-kosciuszko",
            "personIds": ["tadeusz-kosciuszko"],
            "mustSee": True
        },
        {
            "id": "new-york-kosciuszko-bridge",
            "title": {
                "by": "Мост Касцюшкі ў Нью-Ёрку (Бруклін — Квінс)",
                "ru": "Мост Костюшко в Нью-Йорке (Бруклин — Квинс)",
                "en": "Kosciuszko Bridge in New York City"
            },
            "category": "monument",
            "country": {"by": "ЗША", "ru": "США", "en": "United States"},
            "city": {"by": "Нью-Ёрк", "ru": "Нью-Йорк", "en": "New York"},
            "coordinates": [40.727824, -73.929231],
            "description": {
                "by": "Вантовы мост цераз канал Ньютаўн-Крык (траса I-278 / BQE), які злучае раёны Бруклін (Greenpoint) і Квінс. Адкрыты ў 1939 годзе ў прысутнасці 150 000 чалавек і названы ў гонар героя Вайны за незалежнасць ЗША і кіраўніка паўстання 1794 года Тадэвуша Касцюшкі. У 2017–2019 гадах мадэрнізаваны ў сучасны вантовы мост з эфектнай падсветкай.",
                "ru": "Мост Костюшко в Нью-Йорке, соединяющий Бруклин и Квинс через Ньютаун-Крик. Назван в 1939 г. в честь Тадеуша Костюшко.",
                "en": "Cable-stayed bridge over Newtown Creek carrying I-278 between Brooklyn and Queens in NYC, named in 1939 in honor of American Revolutionary War hero Thaddeus Kosciuszko."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Tadeusz_Kosciuszko_by_Karl_Schweisgut.jpg/800px-Tadeusz_Kosciuszko_by_Karl_Schweisgut.jpg",
            "links": [
                {"title": "Kosciuszko Bridge (en.wikipedia)", "url": "https://en.wikipedia.org/wiki/Kosciuszko_Bridge_(New_York_City)"}
            ],
            "tags": ["ЗША", "Нью-Ёрк", "Касцюшка", "мост", "monument"],
            "personId": "tadeusz-kosciuszko",
            "personIds": ["tadeusz-kosciuszko"]
        },

        # --- Paris 1919 Peace Conference BNR Mission ---
        {
            "id": "paris-bnr-delegation-hotel-moderne",
            "title": {
                "by": "Гатэль «Hôtel Moderne» — Рэзідэнцыя дэлегацыі БНР у Парыжы (1919)",
                "ru": "Отель «Hôtel Moderne» — Резиденция делегации БНР в Париже (1919)",
                "en": "Hôtel Moderne — Residence of BNR Delegation in Paris (1919)"
            },
            "category": "historical",
            "country": {"by": "Францыя", "ru": "Франция", "en": "France"},
            "city": {"by": "Парыж", "ru": "Париж", "en": "Paris"},
            "coordinates": [48.866745, 2.365628],
            "description": {
                "by": "Адрас: 8-10, Place de la République, Paris.\n\nГістарычны гатэль на плошчы Рэспублікі ў Парыжы, дзе ў 1919 годзе падчас Парыжскай мірнай канферэнцыі спынялася і пражывала Надзвычайная дыпламатычная дэлегацыя Беларускай Народнай Рэспублікі на чале са старшынёй Рады Народных Міністраў Антонам Луцкевічам. Адсюль беларускія дыпламаты накіроўвалі ноты і мемарандумы лідарам краін Антанты з патрабаваннем міжнароднага прызнання незалежнасці Беларусі.",
                "ru": "Отель Hôtel Moderne на площади Республики в Париже, где во время Парижской мирной конференции 1919 г. проживала делегация Белорусской Народной Республики во главе с Антоном Луцкевичем.",
                "en": "Hôtel Moderne on Place de la République in Paris, residence of the Extraordinary Diplomatic Mission of the Belarusian Democratic Republic (BNR) during the 1919 Paris Peace Conference led by Prime Minister Anton Lutskevich."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Anton_Luckievic.jpg/800px-Anton_Luckievic.jpg",
            "links": [
                {"title": "Беларуская дэлегацыя на Парыжскай мірнай канферэнцыі (be.wikipedia)", "url": "https://be.wikipedia.org/wiki/Беларуская_дэлегацыя_на_Парыжскай_мірнай_канферэнцыі"},
                {"title": "Антон Луцкевіч (be.wikipedia)", "url": "https://be.wikipedia.org/wiki/Антон_Іванавіч_Луцкевіч"}
            ],
            "tags": ["Францыя", "Парыж", "БНР", "Луцкевіч", "дыпламатыя", "historical"],
            "personId": "anton-lutskevich",
            "personIds": ["anton-lutskevich"],
            "mustSee": True
        },
        {
            "id": "paris-bnr-press-bureau-clichy",
            "title": {
                "by": "Бюро дэлегацыі БНР і Беларускае прэс-бюро ў Парыжы",
                "ru": "Бюро делегации БНР и Белорусское пресс-бюро в Париже",
                "en": "BNR Delegation Bureau and Press Bureau in Paris"
            },
            "category": "historical",
            "country": {"by": "Францыя", "ru": "Франция", "en": "France"},
            "city": {"by": "Парыж", "ru": "Париж", "en": "Paris"},
            "coordinates": [48.877435, 2.330426],
            "description": {
                "by": "Адрас: 15, rue de Clichy, 75009 Paris.\n\nАфіцыйны офіс Бюро дэлегацыі Беларускай Народнай Рэспублікі (Bureau de la délégation de la République Démocratique Biélorusse) і Беларускага прэс-бюро ў Парыжы ў 1919–1921 гадах. Адсюль на французскай і англійскай мовах распаўсюджваліся інфармацыйныя бюлетэні пра Беларусь, этнаграфічныя мапы і звароты да Лігі Нацый і сусветнай супольнасці.",
                "ru": "Официальное бюро делегации БНР и Белорусское пресс-бюро в Париже (15, rue de Clichy), действовавшее во время мирных переговоров 1919–1921 гг.",
                "en": "Official bureau of the BNR delegation and Belarusian Press Bureau in Paris (15, rue de Clichy), operating during the 1919–1921 peace negotiations to distribute maps and bulletins advocating Belarusian independence."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Anton_Luckievic.jpg/800px-Anton_Luckievic.jpg",
            "links": [
                {"title": "Беларуская дэлегацыя на Парыжскай мірнай канферэнцыі (be.wikipedia)", "url": "https://be.wikipedia.org/wiki/Беларуская_дэлегацыя_на_Парыжскай_мірнай_канферэнцыі"}
            ],
            "tags": ["Францыя", "Парыж", "БНР", "дыпламатыя", "historical"],
            "personId": "anton-lutskevich",
            "personIds": ["anton-lutskevich"]
        },

        # --- Benedykt Dybowski in Lviv ---
        {
            "id": "lviv-dybowski-grave",
            "title": {
                "by": "Магіла і помнік Бенядзікту Дыбоўскаму на Лычакаўскіх могілках",
                "ru": "Могила и памятник Бенедикту Дыбовскому на Лычаковском кладбище",
                "en": "Benedykt Dybowski Tomb and Monument at Lychakiv Cemetery"
            },
            "category": "grave",
            "country": {"by": "Украіна", "ru": "Украина", "en": "Ukraine"},
            "city": {"by": "Львоў", "ru": "Львов", "en": "Lviv"},
            "coordinates": [49.832437, 24.055526],
            "description": {
                "by": "Лычакаўскія могілкі, поле 76, Львоў.\n\nМагіла і манументальны помнік выбітнаму прыродазнаўцу, заолагу і антраполагу Бенядзікту Дыбоўскаму (1833–1930). Ураджэнец маёнтка Адамарын Мінскага павета, удзельнік паўстання 1863 года. У сібірскай ссылцы стаў піянерам навуковага даследавання фаўны Байкала і Камчаткі, апісаў сотні новых відаў. З 1884 г. прафесар Львоўскага ўніверсітэта.",
                "ru": "Могила и памятник выдающемуся зоологу и исследователю Байкала Бенедикту Дыбовскому (уроженцу Минского повета, повстанцу 1863 г.) на Лычаковском кладбище во Львове.",
                "en": "Tomb and monument of naturalist, zoologist, and explorer of Lake Baikal Benedykt Dybowski at Lychakiv Cemetery in Lviv. Born in Adamaryn near Minsk, 1863 insurgent, professor at Lviv University."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Benedykt_Dybowski_1928.jpg/800px-Benedykt_Dybowski_1928.jpg",
            "links": [
                {"title": "Бенедыкт Дыбоўскі (be.wikipedia)", "url": "https://be.wikipedia.org/wiki/Бенедыкт_Іванавіч_Дыбоўскі"},
                {"title": "Лычакаўскія могілкі (be.wikipedia)", "url": "https://be.wikipedia.org/wiki/Лычакаўскія_могілкі"}
            ],
            "tags": ["Украіна", "Львоў", "Дыбоўскі", "магіла", "grave"],
            "personId": "benedykt-dybowski",
            "personIds": ["benedykt-dybowski"]
        },
        {
            "id": "lviv-dybowski-zoological-museum",
            "title": {
                "by": "Заалагічны музей імя Бенядзікта Дыбоўскага Львоўскага ўніверсітэта",
                "ru": "Зоологический музей имени Бенедикта Дыбовского Львовского университета",
                "en": "Benedykt Dybowski Zoological Museum of Lviv University"
            },
            "category": "culture",
            "country": {"by": "Украіна", "ru": "Украина", "en": "Ukraine"},
            "city": {"by": "Львоў", "ru": "Львов", "en": "Lviv"},
            "coordinates": [49.833870, 24.032157],
            "description": {
                "by": "Адрас: вул. Міхаіла Грушэўскага, 4, Львоў.\n\nАдзін з найстарэйшых універсітэцкіх музеяў Еўропы, заснаваны Бенядзіктам Дыбоўскім. Тут захоўваюцца ўнікальныя калекцыі байкальскіх і камчацкіх эндэмікаў, сабраных нашым земляком падчас шматгадовых сібірскіх экспедыцый, а таксама яго асабістыя рэчы і навуковыя працы.",
                "ru": "Зоологический музей Львовского университета на ул. Грушевского 4, созданный Бенедиктом Дыбовским. Хранит богатейшие коллекции фауны Байкала и Камчатки.",
                "en": "One of Europe's oldest university museums, developed by Benedykt Dybowski on Hrushevskoho St 4 in Lviv, housing his extensive collections of Lake Baikal and Kamchatka fauna."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Benedykt_Dybowski_1928.jpg/800px-Benedykt_Dybowski_1928.jpg",
            "links": [
                {"title": "Зоологічний музей імені Бенедикта Дибовського (uk.wikipedia)", "url": "https://uk.wikipedia.org/wiki/Зоологічний_музей_імені_Бенедикта_Дибовського"}
            ],
            "tags": ["Украіна", "Львоў", "Дыбоўскі", "музей", "culture"],
            "personId": "benedykt-dybowski",
            "personIds": ["benedykt-dybowski"]
        },

        # --- Belarusian Embassies across Asia ---
        {
            "id": "tokyo-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў Японіі (Токіа)",
                "ru": "Посольство Беларуси в Японии (Токио)",
                "en": "Embassy of Belarus in Japan (Tokyo)"
            },
            "category": "historical",
            "country": {"by": "Японія", "ru": "Япония", "en": "Japan"},
            "city": {"by": "Токіа", "ru": "Токио", "en": "Tokyo"},
            "coordinates": [35.626800, 139.728900],
            "description": {
                "by": "Адрас: 5-6-32, Higashi-Gotanda, Shinagawa-ku, Tokyo 141-0022, Japan.\n\nДыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Японіі.",
                "ru": "Адрес: 5-6-32, Higashi-Gotanda, Shinagawa-ku, Tokyo. Дипломатическое представительство Республики Беларусь в Японии.",
                "en": "Address: 5-6-32, Higashi-Gotanda, Shinagawa-ku, Tokyo. Diplomatic mission of the Republic of Belarus in Japan."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Belarusian_ornament.svg/800px-Belarusian_ornament.svg.png",
            "links": [{"title": "Пасольства Беларусі ў Японіі", "url": "https://japan.mfa.gov.by"}],
            "tags": ["Японія", "Токіа", "пасольства", "historical"]
        },
        {
            "id": "seoul-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў Паўднёвай Карэі (Сеул)",
                "ru": "Посольство Беларуси в Южной Корее (Сеул)",
                "en": "Embassy of Belarus in South Korea (Seoul)"
            },
            "category": "historical",
            "country": {"by": "Паўднёвая Карэя", "ru": "Южная Корея", "en": "South Korea"},
            "city": {"by": "Сеул", "ru": "Сеул", "en": "Seoul"},
            "coordinates": [37.535800, 126.999700],
            "description": {
                "by": "Адрас: Itaewon-ro 45-gil, Yongsan-gu, Seoul, Republic of Korea.\n\nДыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Рэспубліцы Карэя.",
                "ru": "Адрес: Itaewon-ro 45-gil, Yongsan-gu, Seoul. Посольство Беларуси в Республике Корея.",
                "en": "Address: Itaewon-ro 45-gil, Yongsan-gu, Seoul. Diplomatic mission of the Republic of Belarus in the Republic of Korea."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Belarusian_ornament.svg/800px-Belarusian_ornament.svg.png",
            "links": [{"title": "Пасольства Беларусі ў Рэспубліцы Карэя", "url": "https://korea.mfa.gov.by"}],
            "tags": ["Карэя", "Сеул", "пасольства", "historical"]
        },
        {
            "id": "new-delhi-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў Індыі (Нью-Дэлі)",
                "ru": "Посольство Беларуси в Индии (Нью-Дели)",
                "en": "Embassy of Belarus in India (New Delhi)"
            },
            "category": "historical",
            "country": {"by": "Індыя", "ru": "Индия", "en": "India"},
            "city": {"by": "Нью-Дэлі", "ru": "Нью-Дели", "en": "New Delhi"},
            "coordinates": [28.556200, 77.161000],
            "description": {
                "by": "Адрас: F-6/8B, Vasant Vihar, New Delhi 110057, India.\n\nДыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Індыі.",
                "ru": "Адрес: F-6/8B, Vasant Vihar, New Delhi. Посольство Беларуси в Индии.",
                "en": "Address: F-6/8B, Vasant Vihar, New Delhi. Diplomatic mission of the Republic of Belarus in India."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Belarusian_ornament.svg/800px-Belarusian_ornament.svg.png",
            "links": [{"title": "Пасольства Беларусі ў Індыі", "url": "https://india.mfa.gov.by"}],
            "tags": ["Індыя", "Нью-Дэлі", "пасольства", "historical"]
        },
        {
            "id": "hanoi-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў В'етнаме (Ханой)",
                "ru": "Посольство Беларуси во Вьетнаме (Ханой)",
                "en": "Embassy of Belarus in Vietnam (Hanoi)"
            },
            "category": "historical",
            "country": {"by": "В'етнам", "ru": "Вьетнам", "en": "Vietnam"},
            "city": {"by": "Ханой", "ru": "Ханой", "en": "Hanoi"},
            "coordinates": [21.066400, 105.819800],
            "description": {
                "by": "Адрас: Tay Ho District, Hanoi, Vietnam.\n\nДыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Сацыялістычнай Рэспубліцы В'етнам.",
                "ru": "Посольство Республики Беларусь в Социалистической Республике Вьетнам (Ханой).",
                "en": "Diplomatic mission of the Republic of Belarus in the Socialist Republic of Vietnam (Hanoi)."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Belarusian_ornament.svg/800px-Belarusian_ornament.svg.png",
            "links": [{"title": "Пасольства Беларусі ў В'етнаме", "url": "https://vietnam.mfa.gov.by"}],
            "tags": ["В'етнам", "Ханой", "пасольства", "historical"]
        },
        {
            "id": "jakarta-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў Інданезіі (Джакарта)",
                "ru": "Посольство Беларуси в Индонезии (Джакарта)",
                "en": "Embassy of Belarus in Indonesia (Jakarta)"
            },
            "category": "historical",
            "country": {"by": "Інданезія", "ru": "Индонезия", "en": "Indonesia"},
            "city": {"by": "Джакарта", "ru": "Джакарта", "en": "Jakarta"},
            "coordinates": [6.208800, 106.845600],
            "description": {
                "by": "Адрас: Menteng, Central Jakarta, Indonesia.\n\nДыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Інданезіі.",
                "ru": "Посольство Республики Беларусь в Республике Индонезия (Джакарта).",
                "en": "Diplomatic mission of the Republic of Belarus in Indonesia (Jakarta)."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Belarusian_ornament.svg/800px-Belarusian_ornament.svg.png",
            "links": [{"title": "Пасольства Беларусі ў Інданезіі", "url": "https://indonesia.mfa.gov.by"}],
            "tags": ["Інданезія", "Джакарта", "пасольства", "historical"]
        },
        {
            "id": "abu-dhabi-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў ААЭ (Абу-Дабі)",
                "ru": "Посольство Беларуси в ОАЭ (Абу-Даби)",
                "en": "Embassy of Belarus in the UAE (Abu Dhabi)"
            },
            "category": "historical",
            "country": {"by": "ААЭ", "ru": "ОАЭ", "en": "United Arab Emirates"},
            "city": {"by": "Абу-Дабі", "ru": "Абу-Даби", "en": "Abu Dhabi"},
            "coordinates": [24.438400, 54.423900],
            "description": {
                "by": "Адрас: Al Karama, Abu Dhabi, UAE.\n\nДыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Аб'яднаных Арабскіх Эміратах.",
                "ru": "Посольство Республики Беларусь в Объединенных Арабских Эмиратах (Абу-Даби).",
                "en": "Diplomatic mission of the Republic of Belarus in the United Arab Emirates (Abu Dhabi)."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Belarusian_ornament.svg/800px-Belarusian_ornament.svg.png",
            "links": [{"title": "Пасольства Беларусі ў ААЭ", "url": "https://uae.mfa.gov.by"}],
            "tags": ["ААЭ", "Абу-Дабі", "пасольства", "historical"]
        },
        {
            "id": "astana-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў Казахстане (Астана)",
                "ru": "Посольство Беларуси в Казахстане (Астана)",
                "en": "Embassy of Belarus in Kazakhstan (Astana)"
            },
            "category": "historical",
            "country": {"by": "Казахстан", "ru": "Казахстан", "en": "Kazakhstan"},
            "city": {"by": "Астана", "ru": "Астана", "en": "Astana"},
            "coordinates": [51.128300, 71.430400],
            "description": {
                "by": "Адрас: вул. Кенесары, 35 / Дыпламатычны гарадок, Астана, Казахстан.\n\nДыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Рэспубліцы Казахстан.",
                "ru": "Посольство Республики Беларусь в Республике Казахстан (Астана).",
                "en": "Diplomatic mission of the Republic of Belarus in the Republic of Kazakhstan (Astana)."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Belarusian_ornament.svg/800px-Belarusian_ornament.svg.png",
            "links": [{"title": "Пасольства Беларусі ў Казахстане", "url": "https://kazakhstan.mfa.gov.by"}],
            "tags": ["Казахстан", "Астана", "пасольства", "historical"]
        },
        {
            "id": "tashkent-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ва Узбекістане (Ташкент)",
                "ru": "Посольство Беларуси в Узбекистане (Ташкент)",
                "en": "Embassy of Belarus in Uzbekistan (Tashkent)"
            },
            "category": "historical",
            "country": {"by": "Узбекістан", "ru": "Узбекистан", "en": "Uzbekistan"},
            "city": {"by": "Ташкент", "ru": "Ташкент", "en": "Tashkent"},
            "coordinates": [41.311100, 69.279700],
            "description": {
                "by": "Адрас: вул. Гулямава, 75, Ташкент, Узбекістан.\n\nДыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Рэспубліцы Узбекістан.",
                "ru": "Посольство Республики Беларусь в Республике Узбекистан (Ташкент).",
                "en": "Diplomatic mission of the Republic of Belarus in Uzbekistan (Tashkent)."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Belarusian_ornament.svg/800px-Belarusian_ornament.svg.png",
            "links": [{"title": "Пасольства Беларусі ва Узбекістане", "url": "https://uzbekistan.mfa.gov.by"}],
            "tags": ["Узбекістан", "Ташкент", "пасольства", "historical"]
        },
        {
            "id": "tbilisi-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў Грузіі (Тбілісі)",
                "ru": "Посольство Беларуси в Грузии (Тбилиси)",
                "en": "Embassy of Belarus in Georgia (Tbilisi)"
            },
            "category": "historical",
            "country": {"by": "Грузія", "ru": "Грузия", "en": "Georgia"},
            "city": {"by": "Тбілісі", "ru": "Тбилиси", "en": "Tbilisi"},
            "coordinates": [41.715100, 44.827100],
            "description": {
                "by": "Адрас: вул. Крцанісі, 18, Тбілісі, Грузія.\n\nДыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Грузіі.",
                "ru": "Посольство Республики Беларусь в Грузии (Тбилиси).",
                "en": "Diplomatic mission of the Republic of Belarus in Georgia (Tbilisi)."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Belarusian_ornament.svg/800px-Belarusian_ornament.svg.png",
            "links": [{"title": "Пасольства Беларусі ў Грузіі", "url": "https://georgia.mfa.gov.by"}],
            "tags": ["Грузія", "Тбілісі", "пасольства", "historical"]
        },
        {
            "id": "baku-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў Азербайджане (Баку)",
                "ru": "Посольство Беларуси в Азербайджане (Баку)",
                "en": "Embassy of Belarus in Azerbaijan (Baku)"
            },
            "category": "historical",
            "country": {"by": "Азербайджан", "ru": "Азербайджан", "en": "Azerbaijan"},
            "city": {"by": "Баку", "ru": "Баку", "en": "Baku"},
            "coordinates": [40.409300, 49.867100],
            "description": {
                "by": "Адрас: вул. Рафіева, 8, Баку, Азербайджан.\n\nДыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Азербайджанскай Рэспубліцы.",
                "ru": "Посольство Республики Беларусь в Азербайджане (Баку).",
                "en": "Diplomatic mission of the Republic of Belarus in Azerbaijan (Baku)."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Belarusian_ornament.svg/800px-Belarusian_ornament.svg.png",
            "links": [{"title": "Пасольства Беларусі ў Азербайджане", "url": "https://azerbaijan.mfa.gov.by"}],
            "tags": ["Азербайджан", "Баку", "пасольства", "historical"]
        },
        {
            "id": "yerevan-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў Арменіі (Ерэван)",
                "ru": "Посольство Беларуси в Армении (Ереван)",
                "en": "Embassy of Belarus in Armenia (Yerevan)"
            },
            "category": "historical",
            "country": {"by": "Арменія", "ru": "Армения", "en": "Armenia"},
            "city": {"by": "Ерэван", "ru": "Ереван", "en": "Yerevan"},
            "coordinates": [40.179200, 44.499100],
            "description": {
                "by": "Адрас: Катайкскі марз, в. Арындж, вул. М. Баграмяна, 9 / Ерэван, Арменія.\n\nДыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Рэспубліцы Арменія.",
                "ru": "Посольство Республики Беларусь в Республике Армения (Ереван).",
                "en": "Diplomatic mission of the Republic of Belarus in the Republic of Armenia (Yerevan)."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Belarusian_ornament.svg/800px-Belarusian_ornament.svg.png",
            "links": [{"title": "Пасольства Беларусі ў Арменіі", "url": "https://armenia.mfa.gov.by"}],
            "tags": ["Арменія", "Ерэван", "пасольства", "historical"]
        },
        {
            "id": "ulaanbaatar-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў Манголіі (Улан-Батар)",
                "ru": "Посольство Беларуси в Монголии (Улан-Батор)",
                "en": "Embassy of Belarus in Mongolia (Ulaanbaatar)"
            },
            "category": "historical",
            "country": {"by": "Манголія", "ru": "Монголия", "en": "Mongolia"},
            "city": {"by": "Улан-Батар", "ru": "Улан-Батор", "en": "Ulaanbaatar"},
            "coordinates": [47.918800, 106.917600],
            "description": {
                "by": "Адрас: Чынгэлтэйнскі раён, 1-ы харо, Улан-Батар, Манголія.\n\nДыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Манголіі.",
                "ru": "Посольство Республики Беларусь в Монголии (Улан-Батор).",
                "en": "Diplomatic mission of the Republic of Belarus in Mongolia (Ulaanbaatar)."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Belarusian_ornament.svg/800px-Belarusian_ornament.svg.png",
            "links": [{"title": "Пасольства Беларусі ў Манголіі", "url": "https://mongolia.mfa.gov.by"}],
            "tags": ["Манголія", "Улан-Батар", "пасольства", "historical"]
        },
        {
            "id": "tobolsk-kremlin-belarusian-presence",
            "title": {
                "by": "Табольскі крамлін і першыя беларусы ў Сібіры",
                "ru": "Тобольский кремль и первые белорусы в Сибири",
                "en": "Tobolsk Kremlin and Early Belarusians in Siberia"
            },
            "category": "historical",
            "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
            "city": {"by": "Табольск", "ru": "Тобольск", "en": "Tobolsk"},
            "coordinates": [58.199664, 68.251363],
            "description": {
                "by": "Красная плошча, Табольск.\n\nТабольск — гістарычная сталіца Сібіры, куды з канца XVI–XVII стст. ссылалі палонных беларусаў і ліцвінаў. У Табольскім гарнізоне існаваў асобны «літоўскі спіс» служылых людзей і казакаў. Гісторыі беларускіх першапраходцаў і перасяленцаў прысвечаны альманах грамадскага фонду «Адраджэнне Табольска» — «Белорусы и Сибирь».",
                "ru": "Тобольский кремль — историческая столица Сибири, куда с XVI–XVII вв. ссылали пленных литвинов и белорусов. «Литовский список» Тобольского гарнизона. Альманах «Белорусы и Сибирь».",
                "en": "Tobolsk Kremlin, historic capital of Siberia. Starting in the 16th–17th centuries, captured Belarusians and Litvins were exiled here, forming the 'Lithuanian list' of the local garrison."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Tobolsk_Kremlin_view.jpg/800px-Tobolsk_Kremlin_view.jpg",
            "links": [
                {"title": "Альманах: Белорусы и Сибирь (Тобольск)", "url": "https://www.tobolsk.org/index.php/ru/home/stati/251-tobolsk-i-vsya-sibir-belorusy-i-sibir"},
                {"title": "Беларусы Сібіры (be.wikipedia)", "url": "https://be.wikipedia.org/wiki/Беларусы_Сібіры"}
            ],
            "tags": ["Расія", "Табольск", "Сібір", "крамлін", "historical"]
        },
        {
            "id": "tyumen-belarusian-community",
            "title": {
                "by": "Беларускі асяродак у Цюмені (Дні беларускай культуры)",
                "ru": "Белорусская община в Тюмени (Дни белорусской культуры)",
                "en": "Belarusian Community in Tyumen"
            },
            "category": "culture",
            "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
            "city": {"by": "Цюмень", "ru": "Тюмень", "en": "Tyumen"},
            "coordinates": [57.153534, 65.542274],
            "description": {
                "by": "Цюменская абласная грамадская арганізацыя «Беларусы». Цюмень — найстарэйшы горад Сібіры, цесна звязаны з беларускай дыяспарай. Тут штогод ладзяцца Дні беларускай культуры на Цюменскай зямлі, выставы ручнікоў і народнага мастацтва.",
                "ru": "Тюменская областная общественная организация «Белорусы». Проведение Дней белорусской культуры в Тюмени.",
                "en": "Tyumen regional community 'Belarusians', preserving folk heritage and hosting Days of Belarusian Culture in Siberia."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Belarusian_ornament.svg/800px-Belarusian_ornament.svg.png",
            "links": [
                {"title": "Белорусы Тюменской области", "url": "https://belros.org/regional/index.php?nka=3591"},
                {"title": "Дни белорусской культуры на Тюменской земле", "url": "https://vsluh.ru/novosti/obshchestvo/dni-belorusskoy-kultury-prishli-na-tyumenskuyu-zemlyu_179835/"}
            ],
            "tags": ["Расія", "Цюмень", "дыяспара", "culture"]
        },
        {
            "id": "krasnoyarsk-belarusian-autonomy",
            "title": {
                "by": "Беларускі культурны цэнтр «Беларусь» у Краснаярску",
                "ru": "Белорусский культурный центр «Беларусь» в Красноярске",
                "en": "Belarusian Cultural Center 'Belarus' in Krasnoyarsk"
            },
            "category": "culture",
            "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
            "city": {"by": "Краснаярск", "ru": "Красноярск", "en": "Krasnoyarsk"},
            "coordinates": [56.010569, 92.852572],
            "description": {
                "by": "Краснаярская рэгіянальная нацыянальна-культурная аўтаномія «Беларусь». Краснаярскі край з'яўляецца адным з найбуйнейшых рэгіёнаў кампактнага рассялення беларускіх перасяленцаў сталыпінскіх часоў і іх нашчадкаў (Казачынскі, Дзяржынскі, Сухабузімскі раёны).",
                "ru": "Красноярская региональная национально-культурная автономия «Беларусь». История белорусских переселенцев в Енисейской губернии и Красноярском крае.",
                "en": "Krasnoyarsk regional national-cultural autonomy 'Belarus', supporting diaspora culture across the Yenisey basin and Siberian settler villages."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Belarusian_ornament.svg/800px-Belarusian_ornament.svg.png",
            "links": [
                {"title": "Этноатлас Красноярского края: Белорусы", "url": "http://www.krskstate.ru/about/narod/etnoatlas/0/eid/15"}
            ],
            "tags": ["Расія", "Краснаярск", "Сібір", "дыяспара", "culture"]
        },
        {
            "id": "malbork-castle-gd-lithuania-collection",
            "title": {
                "by": "Замак Мальбарк — Калекцыя ўзбраення і манет ВКЛ",
                "ru": "Замок Мальборк — Коллекция вооружения и монет ВКЛ",
                "en": "Malbork Castle — Grand Duchy of Lithuania Collection"
            },
            "category": "culture",
            "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
            "city": {"by": "Мальбарк", "ru": "Мальборк", "en": "Malbork"},
            "coordinates": [54.040018, 19.027818],
            "description": {
                "by": "Замкавы музей у Мальбарку (былая каралеўская рэзідэнцыя Рэчы Паспалітай).\n\nУ калекцыях музея захоўваюцца каштоўныя экспанаты, непасрэдна звязаныя з гісторыяй Вялікага Княства Літоўскага: ліцвінская амуніцыя і халодная зброя, гусарскія даспехі, гарматныя ствалы нясвіжскай ліцейні Радзівілаў, а таксама багатая калекцыя манет віленскага мынца ВКЛ часоў Вітаўта і Ягелонаў.",
                "ru": "Замковый музей в Мальборке хранит уникальные реликвии Великого Княжества Литовского: вооружение и доспехи, пушки несвижской литейной мануфактуры Радзивиллов, а также виленские монеты времен Витовта.",
                "en": "Malbork Castle Museum holds precious artifacts of the Grand Duchy of Lithuania: husar armors, sabres, Radziwiłł cannons from Niasvizh, and a rich numismatic collection from the Vilnius mint."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Malbork_Castle_Poland.jpg/800px-Malbork_Castle_Poland.jpg",
            "links": [
                {"title": "Muzeum Zamkowe w Malborku", "url": "https://zamek.malbork.pl/"},
                {"title": "Zamek w Malborku (pl.wikipedia)", "url": "https://pl.wikipedia.org/wiki/Zamek_w_Malborku"}
            ],
            "tags": ["Польшча", "Мальбарк", "ВКЛ", "замак", "culture"]
        },
        {
            "id": "spb-smolenskoye-vilkitsky-grave",
            "title": {
                "by": "Магіла палярных гідрографаў Андрэя і Барыса Вількіцкіх",
                "ru": "Могила полярных гидрографов Андрея и Бориса Вилькицких",
                "en": "Grave of Polar Explorers Andrey and Boris Vilkitsky"
            },
            "category": "grave",
            "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
            "city": {"by": "Санкт-Пецярбург", "ru": "Санкт-Петербург", "en": "Saint Petersburg"},
            "coordinates": [59.949700, 30.245800],
            "description": {
                "by": "Смаленскія праваслаўныя могілкі, Васільеўскі востраў, Санкт-Пецярбург.\n\nСямейнае пахаванне славутых палярных даследчыкаў Арктыкі беларускага паходжання. Андрэй Іпалітавіч Вількіцкі (1858–1913, ураджэнец маёнтка Тосік Барысаўскага павета Мінскай губерні) — генерал-лейтэнант Корпуса гідрографаў, начальнік Галоўнага гідраграфічнага ўпраўлення. Яго сын Барыс Андрэевіч Вількіцкі (1885–1961) — кіраўнік легендарнай Гідраграфічнай экспедыцыі Паўночнага Ледавітага акіяна (1913–1915) на ледаколах «Таймыр» і «Вайгач», першаадкрывальнік архіпелага Паўночная Зямля і праліва Вількіцкага. У 2003 годзе прах Барыса Вількіцкага быў перанесены з могілак Іксель у Бруселі (Бельгія) і перапахаваны побач з бацькам.",
                "ru": "Смоленское православное кладбище, Санкт-Петербург. Могила полярных гидрографов Андрея Вилькицкого (уроженца Борисовского уезда) и его сына Бориса Вилькицкого (первооткрывателя Северной Земли, прах перенесен из Брюсселя в 2003 г.).",
                "en": "Smolenskoye Orthodox Cemetery, St. Petersburg. Tomb of Arctic hydrographers Andrey Vilkitsky (born in Barysaw district, Minsk governorate) and his son Boris Vilkitsky (discoverer of Severnaya Zemlya and Vilkitsky Strait, reburied from Brussels in 2003)."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Boris_Vilkitsky.jpg/800px-Boris_Vilkitsky.jpg",
            "links": [
                {"title": "Андрэй Вількіцкі (be.wikipedia)", "url": "https://be.wikipedia.org/wiki/Андрэй_Іпалітавіч_Вількіцкі"},
                {"title": "Барыс Вількіцкі (be.wikipedia)", "url": "https://be.wikipedia.org/wiki/Барыс_Андрэевіч_Вількіцкі"}
            ],
            "tags": ["Расія", "Пецярбург", "Вількіцкі", "палярнікі", "Арктыка", "grave"],
            "personIds": ["andrey-vilkitsky", "boris-vilkitsky"]
        },
        {
            "id": "spb-arctic-museum-vollosovich-vilkitsky",
            "title": {
                "by": "Расійскі музей Арктыкі і Антарктыкі (калекцыі Вількіцкіх і Валасовіча)",
                "ru": "Российский музей Арктики и Антарктики (коллекции Вилькицких и Воллосовича)",
                "en": "Russian Museum of the Arctic and Antarctic (Vilkitsky and Vollosovich Collections)"
            },
            "category": "culture",
            "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
            "city": {"by": "Санкт-Пецярбург", "ru": "Санкт-Петербург", "en": "Saint Petersburg"},
            "coordinates": [59.928700, 30.354600],
            "description": {
                "by": "Адрас: вул. Марата, 24А, Санкт-Пецярбург.\n\nНайбуйнейшы музей палярных даследаванняў, дзе захоўваюцца ўнікальныя экспанаты, прыборы і карты экспедыцый Барыса Вількіцкага (адкрыццё Паўночнай Зямлі 1913 г.), а таксама матэрыялы Рускай палярнай экспедыцыі барона Толя на шхуне «Зара» (1900–1902) і раскопак Саннікаўскага маманта, праведзеных беларускім геолагам і даследчыкам Арктыкі Канстанцінам Валасовічам (1869–1919, ураджэнцам Слуцкага павета).",
                "ru": "Музей Арктики и Антарктики в Санкт-Петербурге хранит приборы, карты и материалы экспедиций Бориса Вилькицкого и геолога Константина Воллосовича (уроженца Слуцкого уезда, исследователя Новосибирских островов).",
                "en": "Museum of the Arctic and Antarctic in St. Petersburg, holding instruments, maps, and artifacts from polar expeditions of Boris Vilkitsky and Belarusian Arctic geologist Konstantin Vollosovich."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Boris_Vilkitsky.jpg/800px-Boris_Vilkitsky.jpg",
            "links": [
                {"title": "Расійскі дзяржаўны музей Арктыкі і Антарктыкі", "url": "https://polarmuseum.ru/"},
                {"title": "Канстанцін Валасовіч (be.wikipedia)", "url": "https://be.wikipedia.org/wiki/Канстанцін_Адамавіч_Валасовіч"}
            ],
            "tags": ["Расія", "Пецярбург", "Арктыка", "Вількіцкі", "Валасовіч", "музей", "culture"],
            "personIds": ["boris-vilkitsky", "andrey-vilkitsky", "konstantin-vollosovich"]
        }
    ]

    added_count = 0
    for np in new_places:
        if np['id'] not in existing_ids:
            places.append(np)
            added_count += 1
        else:
            # Update existing
            for idx, p in enumerate(places):
                if p['id'] == np['id']:
                    places[idx] = np
                    break

    print(f"Added {added_count} new places. Total places: {len(places)}")

    # Add missing person records if needed
    person_ids = {p['id'] for p in persons}
    new_persons = [
        {
            "id": "henryk-siemiradzki",
            "name": {
                "by": "Генрых Семірадскі",
                "ru": "Генрих Семирадский",
                "en": "Henryk Siemiradzki"
            },
            "role": {
                "by": "Мастак-акадэміст, майстар манументальнага жывапісу",
                "ru": "Художник-академист, мастер монументальной живописи",
                "en": "Academic painter, master of monumental art"
            },
            "years": "1843–1902",
            "birthPlace": "Новабялгарад (пад Харкавам, сям'я з Навагрудчыны)",
            "description": {
                "by": "Сусветна вядомы мастак, прадстаўнік позняга акадэмізму, выхадзец са старадаўняга беларускага шляхецкага роду Семірадскіх герба «Лебедзь» з Навагрудчыны. Стваральнік манументальных палотнаў на антычныя і біблейскія сюжэты («Светачы хрысціянства / Паходні Нерона», «Хрысціянская Дзірка»).",
                "ru": "Всемирно известный художник, представитель академизма, выходец из белорусского дворянского рода Семирадских Новогрудского воеводства.",
                "en": "World-renowned academic painter from a Belarusian noble family of Navahrudak origin. Master of monumental classical and biblical scenes."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/PL_Henryk_Siemiradzki_Autoportret_nieukonczony.jpg/800px-PL_Henryk_Siemiradzki_Autoportret_nieukonczony.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Генрых_Іпалітавіч_Семірадскі",
            "placeIds": [
                "krakow-sukiennice-siemiradzki",
                "lviv-art-gallery-siemiradzki",
                "rome-villino-siemiradzki-via-gaeta",
                "strzalkow-dwor-siemiradzkiego"
            ]
        },
        {
            "id": "edward-piekarski",
            "name": {
                "by": "Эдвард Пякарскі",
                "ru": "Эдуард Пекарский",
                "en": "Edward Piekarski"
            },
            "role": {
                "by": "Лінгвіст, этнограф, фалькларыст, заснавальнік якуцкай пісьменнасці",
                "ru": "Лингвист, этнограф, фольклорист, основатель якутской письменности",
                "en": "Linguist, ethnographer, founder of Yakut written literature"
            },
            "years": "1858–1934",
            "birthPlace": "в. Пятровічы (Ігуменскі павет / Смалявіцкі раён)",
            "description": {
                "by": "Беларускі шляхціц, лінгвіст і фалькларыст. За ўдзел у народніцкім руху высланы ў Сібір, дзе пражыў больш за 20 гадоў у Якуціі. Стваральнік фундаментальнага «Слоўніка якуцкай мовы» ў 3 тамах (~38 000 слоў), які паклаў пачатак пісьмовай якуцкай мове. Акадэмік АН СССР.",
                "ru": "Белорусский дворянин, лингвист. В якутской ссылке создал фундаментальный «Словарь якутского языка», заложив основы якутской письменности.",
                "en": "Belarusian linguist and folklorist. During his exile in Yakutia, compiled the monumental 3-volume Yakut Language Dictionary (~38,000 words), founding modern Yakut written literature."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Edward_Piekarski.jpg/800px-Edward_Piekarski.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Эдвард_Карлавіч_Пякарскі",
            "placeIds": [
                "yakutsk-exiled-scholars-memorial",
                "cherkekh-piekarski-house-museum"
            ]
        },
        {
            "id": "jan-czerski",
            "name": {
                "by": "Ян Чэрскі",
                "ru": "Ян Черский",
                "en": "Jan Czerski"
            },
            "role": {
                "by": "Геолаг, палеантолаг, геамарфолаг, першаадкрывальнік Сібіры",
                "ru": "Геолог, палеонтолог, геоморфолог, исследователь Сибири",
                "en": "Geologist, paleontologist, pioneer explorer of Siberia"
            },
            "years": "1845–1892",
            "birthPlace": "маёнтак Свольна (Дрысенскі павет / Верхнядзвінскі раён)",
            "description": {
                "by": "Беларускі шляхціц, удзельнік паўстання 1863 года ў атрадзе Кастуся Каліноўскага. Высланы ў Сібір салдатам. Стаў выдатным геолагам і географам, першаадкрывальнікам Байкала, Саянаў і Калымы. У яго гонар названы Хрыбет Чэрскага ў Якуціі і Магадане, Хрыбет Чэрскага ў Забайкаллі, вулкан, горад Чэрскі і ледавік.",
                "ru": "Белорусский дворянин, участник восстания 1863 года под руководством Кастуся Калиновского. Выдающийся геолог и исследователь Сибири.",
                "en": "Belarusian insurgent of 1863 under Kastus Kalinouski and legendary Siberian explorer, geologist, and geographer. The Chersky Range in Yakutia and Transbaikalia are named in his honor."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Jan_%C4%8Cerski._%D0%AF%D0%BD_%D0%A7%D1%8D%D1%80%D1%81%D0%BA%D1%96_%281879%29.jpg/800px-Jan_%C4%8Cerski._%D0%AF%D0%BD_%D0%A7%D1%8D%D1%80%D1%81%D0%BA%D1%96_%281879%29.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Ян_Дамінікавіч_Чэрскі",
            "placeIds": [
                "yakutsk-exiled-scholars-memorial",
                "irkutsk-cherny-society-belarusian-culture"
            ]
        },
        {
            "id": "benedykt-dybowski",
            "name": {
                "by": "Бенядзікт Дыбоўскі",
                "ru": "Бенедикт Дыбовский",
                "en": "Benedykt Dybowski"
            },
            "role": {
                "by": "Заолаг, географ, антраполаг, даследчык Байкала і Сібіры",
                "ru": "Зоолог, географ, антрополог, исследователь Байкала и Сибири",
                "en": "Zoologist, explorer of Lake Baikal and Siberia"
            },
            "years": "1833–1930",
            "birthPlace": "маёнтак Адамарын (Мінскі павет)",
            "description": {
                "by": "Выбітны прыродазнавец, ураджэнец Міншчыны. За ўдзел у паўстанні 1863 года прыгавораны да катаргі ў Сібіры. Стаў піянерам навуковага даследавання фаўны Байкала, Ангары, Амура і Камчаткі, адкрыў сотні новых відаў. З 1884 г. прафесар Львоўскага ўніверсітэта.",
                "ru": "Выдающийся зоолог и географ, уроженец Минщины, повстанец 1863 г. Исследователь Байкала и Камчатки, профессор Львовского университета.",
                "en": "Naturalist and explorer born near Minsk. 1863 insurgent, pioneer researcher of Lake Baikal and Kamchatka fauna, professor at Lviv University."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Benedykt_Dybowski_1928.jpg/800px-Benedykt_Dybowski_1928.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Бенедыкт_Іванавіч_Дыбоўскі",
            "placeIds": [
                "lviv-dybowski-grave",
                "lviv-dybowski-zoological-museum"
            ]
        },
        {
            "id": "anton-lutskevich",
            "name": {
                "by": "Антон Луцкевіч",
                "ru": "Антон Луцкевич",
                "en": "Anton Lutskevich"
            },
            "role": {
                "by": "Прэм'ер-міністр і міністр замежных спраў БНР, гісторык, публіцыст",
                "ru": "Премьер-министр и министр иностранных дел БНР, публицист",
                "en": "Prime Minister and Foreign Minister of BNR, historian"
            },
            "years": "1884–1942",
            "birthPlace": "Шаўлі (Ковенская губерня)",
            "description": {
                "by": "Выбітны дзеяч беларускага нацыянальнага адраджэння, адзін з пачынальнікаў газеты «Наша Ніва», кіраўнік урада Беларускай Народнай Рэспублікі. Узначальваў Надзвычайную дыпламатычную дэлегацыю БНР на Парыжскай мірнай канферэнцыі 1919 года.",
                "ru": "Выдающийся деятель белорусского движения, премьер-министр БНР, глава дипломатической миссии БНР на Парижской мирной конференции 1919 г.",
                "en": "Key figure of the Belarusian national revival, Prime Minister of the Belarusian Democratic Republic, and head of the BNR mission to the Paris Peace Conference in 1919."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Anton_Luckievic.jpg/800px-Anton_Luckievic.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Антон_Іванавіч_Луцкевіч",
            "placeIds": [
                "paris-bnr-delegation-hotel-moderne",
                "paris-bnr-press-bureau-clichy"
            ]
        },
        {
            "id": "andrey-vilkitsky",
            "name": {
                "by": "Андрэй Вількіцкі",
                "ru": "Андрей Вилькицкий",
                "en": "Andrey Vilkitsky"
            },
            "role": {
                "by": "Гідрограф, геадэзіст, палярны даследчык, генерал-лейтэнант",
                "ru": "Гидрограф, геодезист, полярный исследователь, генерал-лейтенант",
                "en": "Hydrographer, geodesist, polar explorer, Lieutenant General"
            },
            "years": "1858–1913",
            "birthPlace": "маёнтак Тосік (Барысаўскі павет, Мінская губерня)",
            "description": {
                "by": "Выбітны беларускі гідрограф і геадэзіст, генерал-лейтэнант Корпуса гідрографаў, начальнік Галоўнага гідраграфічнага ўпраўлення. Даследчык Арктыкі, Карскага мора і вусцяў рэк Об і Енісей.",
                "ru": "Выдающийся белорусский гидрограф и геодезист, генерал-лейтенант, начальник Главного гидрографического управления. Исследователь Карского моря, Оби и Енисея.",
                "en": "Distinguished polar hydrographer and surveyor born in Barysaw district, Minsk governorate. Head of the Main Hydrographic Directorate."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Boris_Vilkitsky.jpg/800px-Boris_Vilkitsky.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Андрэй_Іпалітавіч_Вількіцкі",
            "placeIds": [
                "spb-smolenskoye-vilkitsky-grave",
                "spb-arctic-museum-vollosovich-vilkitsky"
            ]
        },
        {
            "id": "boris-vilkitsky",
            "name": {
                "by": "Барыс Вількіцкі",
                "ru": "Борис Вилькицкий",
                "en": "Boris Vilkitsky"
            },
            "role": {
                "by": "Палярны даследчык, першаадкрывальнік Паўночнай Зямлі",
                "ru": "Полярный исследователь, первооткрыватель Северной Земли",
                "en": "Polar explorer, discoverer of Severnaya Zemlya"
            },
            "years": "1885–1961",
            "birthPlace": "Санкт-Пецярбург (бацька з Барысаўскага павета)",
            "description": {
                "by": "Сын Андрэя Вількіцкага, капітан 2-га рангу. Узначальваў Гідраграфічную экспедыцыю Паўночнага Ледавітага акіяна (1913–1915) на ледаколах «Таймыр» і «Вайгач», якая адкрыла архіпелаг Паўночная Зямля (апошняе вялікае геаграфічнае адкрыццё на Зямлі) і праліў Вількіцкага.",
                "ru": "Сын Андрея Вилькицкого, капитан 2-го ранга. Руководитель экспедиции на ледоколах «Таймыр» и «Вайгач», открывшей Северную Землю и пролив Вилькицкого.",
                "en": "Naval officer and polar explorer, led the expedition that discovered Severnaya Zemlya (the last major archipelago discovered on Earth) and the Vilkitsky Strait."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Boris_Vilkitsky.jpg/800px-Boris_Vilkitsky.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Барыс_Андрэевіч_Вількіцкі",
            "placeIds": [
                "spb-smolenskoye-vilkitsky-grave",
                "spb-arctic-museum-vollosovich-vilkitsky"
            ]
        },
        {
            "id": "konstantin-vollosovich",
            "name": {
                "by": "Канстанцін Валасовіч",
                "ru": "Константин Воллосович",
                "en": "Konstantin Vollosovich"
            },
            "role": {
                "by": "Геолаг, геахімік, палярны даследчык Сібіры і Арктыкі",
                "ru": "Геолог, геохимик, полярный исследователь Сибири и Арктики",
                "en": "Geologist, geochemist, Arctic and Siberian explorer"
            },
            "years": "1869–1919",
            "birthPlace": "в. Старчыцы / Ёдчыцы (Слуцкі павет, Мінская губерня)",
            "description": {
                "by": "Беларускі геолаг і палярны даследчык. Удзельнік Рускай палярнай экспедыцыі барона Толя на шхуне «Зара» (1900–1902), кіраўнік раскопак Саннікаўскага маманта на Новасібірскіх астравах. Яго імем названы востраў і мыс на архіпелагу Паўночная Зямля.",
                "ru": "Белорусский геолог и полярный исследователь (уроженец Слуцкого уезда). Участник Русской полярной экспедиции Толля на шхуне «Заря», исследователь Новосибирских островов.",
                "en": "Belarusian geologist and Arctic explorer born in Slutsk district. Participant in Eduard Toll's polar expedition on the 'Zarya' and excavator of the Sannikov mammoth."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Belarusian_ornament.svg/800px-Belarusian_ornament.svg.png",
            "wiki": "https://be.wikipedia.org/wiki/Канстанцін_Адамавіч_Валасовіч",
            "placeIds": [
                "spb-arctic-museum-vollosovich-vilkitsky"
            ]
        }
    ]

    for npers in new_persons:
        if npers['id'] not in person_ids:
            persons.append(npers)
            person_ids.add(npers['id'])
        else:
            for idx, pers in enumerate(persons):
                if pers['id'] == npers['id']:
                    # Merge placeIds
                    existing_pids = set(pers.get('placeIds', []))
                    existing_pids.update(npers.get('placeIds', []))
                    pers['placeIds'] = sorted(list(existing_pids))
                    break

    # Save JSON files
    with open('data/places.json', 'w', encoding='utf-8') as f:
        json.dump(places, f, ensure_ascii=False, indent=2)

    with open('data/persons.json', 'w', encoding='utf-8') as f:
        json.dump(persons, f, ensure_ascii=False, indent=2)

    # Save JS files
    with open('data/places.js', 'w', encoding='utf-8') as f:
        f.write('window.INITIAL_PLACES = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

    with open('data/persons.js', 'w', encoding='utf-8') as f:
        f.write('window.INITIAL_PERSONS = ' + json.dumps(persons, ensure_ascii=False, indent=2) + ';\n')

    print("Successfully synchronized places and persons datasets!")

if __name__ == '__main__':
    main()
