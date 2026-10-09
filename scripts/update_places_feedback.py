import json

def update_all():
    with open('data/places.json', 'r', encoding='utf-8') as f:
        places = json.load(f)

    with open('data/persons.json', 'r', encoding='utf-8') as f:
        persons = json.load(f)

    places_map = {p['id']: p for p in places}
    persons_map = {p['id']: p for p in persons}

    # 1. FIX ASIAN EMBASSIES CATEGORY
    asian_embassies = [
        "tokyo-embassy-belarus", "seoul-embassy-belarus", "new-delhi-embassy-belarus",
        "hanoi-embassy-belarus", "jakarta-embassy-belarus", "abu-dhabi-embassy-belarus",
        "astana-embassy-belarus", "tashkent-embassy-belarus", "tbilisi-embassy-belarus",
        "baku-embassy-belarus", "yerevan-embassy-belarus", "ulaanbaatar-embassy-belarus"
    ]
    for eid in asian_embassies:
        if eid in places_map:
            places_map[eid]['category'] = 'embassy'
            tags = places_map[eid].get('tags', [])
            tags = [t for t in tags if t != 'historical']
            if 'embassy' not in tags:
                tags.append('embassy')
            places_map[eid]['tags'] = tags

    # 2. UPDATE DETENTION / PRISON PLACES TO CATEGORY 'prison'
    prison_place_ids = [
        "vilnia-lukishskaya-turma",
        "vilnia-kellya-konrada",
        "moscow-butyrka-fabian-abrantovich-martyrdom",
        "gulag-solovki-slon",
        "gulag-inta-geniyush",
        "gulag-vorkuta-repost",
        "gulag-kengir-steplag",
        "gulag-karlag-dolinka",
        "gulag-norillag-memorial",
        "gulag-kolyma-maska-smutku",
        "nazi-camp-auschwitz-birkenau",
        "nazi-camp-sobibor-revolt",
        "nazi-camp-mauthausen-memorial",
        "nazi-camp-buchenwald-memorial",
        "nazi-camp-ravensbruck-women",
        "nazi-camp-sachsenhausen",
        "nazi-camp-dachau-memorial",
        "nazi-camp-stutthof-memorial",
        "solovki-monastery-gulag-clergy-memorial"
    ]
    for pid in prison_place_ids:
        if pid in places_map:
            places_map[pid]['category'] = 'prison'
            tags = places_map[pid].get('tags', [])
            if 'prison' not in tags:
                tags.append('prison')
            places_map[pid]['tags'] = tags

    # 3. FIX HAJNOWKA AND BIELSK PODLASKI COORDINATES
    # Remove duplicate hajnowka-museum-belarusian-culture
    if 'hajnowka-museum-belarusian-culture' in places_map:
        del places_map['hajnowka-museum-belarusian-culture']

    # Update hajnowka-museum-belarusian
    if 'hajnowka-museum-belarusian' in places_map:
        places_map['hajnowka-museum-belarusian']['coordinates'] = [52.737462, 23.586646]
        places_map['hajnowka-museum-belarusian']['unverifiedCoordinates'] = False

    # Update hajnowka-ii-lo-belaruski-licej
    if 'hajnowka-ii-lo-belaruski-licej' in places_map:
        places_map['hajnowka-ii-lo-belaruski-licej']['coordinates'] = [52.735547, 23.592505]
        places_map['hajnowka-ii-lo-belaruski-licej']['unverifiedCoordinates'] = False

    # Add Holy Trinity Cathedral in Hajnówka
    if 'hajnowka-holy-trinity-orthodox-cathedral' not in places_map:
        places_map['hajnowka-holy-trinity-orthodox-cathedral'] = {
            "id": "hajnowka-holy-trinity-orthodox-cathedral",
            "title": {
                "by": "Сабор Святой Тройцы ў Гайнаўцы",
                "ru": "Собор Святой Троицы в Гайновке",
                "en": "Holy Trinity Orthodox Cathedral in Hajnówka"
            },
            "category": "church",
            "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
            "city": {"by": "Гайнаўка", "ru": "Гайновка", "en": "Hajnówka"},
            "coordinates": [52.745691, 23.579045],
            "description": {
                "by": "Адрас: вул. ксяндза Антонія Дзевятоўскага 11 (ul. Ks. Dziewiatowskiego 11), Гайнаўка.\n\nМанументальны двухпавярховы сабор з арыгінальнымі хвалістымі жалезабетоннымі скляпеннямі, пабудаваны ў 1974–1992 гг. паводле наватарскага праекта прафесара Аляксандра Грыгар'евіча. Галоўная святыня і духоўны цэнтр праваслаўнага Падляшша. Дзякуючы ўнікальнай акустыцы тут штогод праходзіць сусветна вядомы Міжнародны фестываль царкоўнай музыкі «Гайнаўка» (Międzynarodowy Festiwal Muzyki Cerkiewnej).",
                "ru": "Ул. Дзевятовского 11, Гайновка. Кафедральный собор Святой Троицы (арх. Александр Григорович), главная святыня православного Подляшья и место проведения Международного фестиваля церковной музыки «Гайновка».",
                "en": "Holy Trinity Orthodox Cathedral in Hajnówka (designed by Aleksander Grygorowicz, built 1974–1992). An architectural landmark with exceptional acoustics, hosting the renowned International Festival of Orthodox Church Music."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Sob%C3%B3r_%C5%9Awi%C4%99tej_Tr%C3%B3jcy_w_Hajn%C3%B3wce.jpg/800px-Sob%C3%B3r_%C5%9Awi%C4%99tej_Tr%C3%B3jcy_w_Hajn%C3%B3wce.jpg",
            "links": [
                {"title": "Sobór Świętej Trójcy w Hajnówce (pl.wikipedia)", "url": "https://pl.wikipedia.org/wiki/Sob%C3%B3r_%C5%9Awi%C4%99tej_Tr%C3%B3jcy_w_Hajn%C3%B3wce"}
            ],
            "tags": ["Гайнаўка", "Падляшша", "царква", "church"],
            "mustSee": True
        }

    # Fix Bielsk Podlaski coordinates
    if 'bielsk-podlaski-szkola-3-hajduk' in places_map:
        places_map['bielsk-podlaski-szkola-3-hajduk']['coordinates'] = [52.766891, 23.193512]
    if 'studziwody-muzej-maloj-backauszcyny' in places_map:
        places_map['studziwody-muzej-maloj-backauszcyny']['coordinates'] = [52.743353, 23.188919]

    # 4. FIX ARROW PARK KUPALA MONUMENT
    if 'monroe-arrow-park-kupala-monument' in places_map:
        ap = places_map['monroe-arrow-park-kupala-monument']
        ap['title'] = {
            "by": "Помнік Янку Купалу ў Ароў-Парку (Манро, штат Нью-Ёрк)",
            "ru": "Памятник Янке Купале в Эрроу-Парке (Монро, штат Нью-Йорк)",
            "en": "Yanka Kupala Monument in Arrow Park (Monroe, NY)"
        }
        ap['coordinates'] = [41.286401, -74.182610]
        ap['description'] = {
            "by": "Адрас: 1061 Orange Turnpike, Monroe, Orange County, New York 10950, USA.\n\nБронзавы помнік класіку беларускай літаратуры Янку Купалу, усталяваны ў 1973 годзе ў мемарыяльным парку Arrow Park (мястэчка Манро, акруга Орандж, за 80 км на поўнач ад Нью-Ёрка каля парку Харыман). Аўтар скульптуры — народны мастак Беларусі Анатоль Анікейчык (архітэктар С. Баткоўскі). Помнік стаіць у мемарыяльным Садзе паэтаў («Чатыры бессмяротныя») побач з манументамі Тарасу Шаўчэнку, Уолту Уітмэну і Аляксандру Пушкіну. Адзіны помнік Янку Купалу ў Заходнім паўшар'і.",
            "ru": "1061 Orange Turnpike, Monroe, NY 10950. Памятник белорусскому классику Янке Купале в Эрроу-Парке (Монро, штат Нью-Йорк, в 80 км к северу от Манхэттена), установленный в 1973 г. Скульптор — А. Аникейчик.",
            "en": "1061 Orange Turnpike, Monroe, NY 10950. Bronze monument to Belarusian national poet Yanka Kupala erected in 1973 in Arrow Park (Monroe, Orange County, New York, ~80 km north of NYC). Sculpted by Anatol Anikeychyk in the 'Poets Garden' alongside Taras Shevchenko, Walt Whitman, and Alexander Pushkin."
        }

    # 5. EXPAND BERNARDINE CEMETERY IN VILNIUS
    bp_id = "vilnia-bernardynskiya-mohilki-dze-pakhavany-stanisla"
    if bp_id in places_map:
        bp = places_map[bp_id]
        bp['title'] = {
            "by": "Бернардзінскія могілкі ў Вільні",
            "ru": "Бернардинское кладбище в Вильнюсе",
            "en": "Bernardine Cemetery in Vilnius"
        }
        bp['image'] = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Bernardine_Cemetery1.jpg/800px-Bernardine_Cemetery1.jpg"
        bp['description'] = {
            "by": "Адрас: Žvirgždyno g. 3, Užupis (Зарэчча), Вільня.\n\nАдзін з найстарэйшых і найбольш каштоўных гістарычных некропаляў Вільні, заснаваны ў 1810 годзе на маляўнічым беразе ракі Вільні. На ўваходнай класіцыстычнай браме (1820) высечаны лацінскі дэвіз «Non omnis moriar» («Увесь я не памру»). Тут спачываюць выбітныя дзеячы навукі, культуры, мастацтва і вызвольнага руху Беларусі і Літвы XIX–XX стагоддзяў:\n• Станіслаў Баніфацы Юндзіл (1761–1847) — прафесар батанікі і заалогіі Віленскага ўніверсітэта, даследчык прыроды Беларусі, і яго пляменнік Юзаф Юндзіл (1794–1877);\n• Каміла Марцінкевіч (1837–1887) — піяністка, кампазітарка, дачка Вінцэнта Дуніна-Марцінкевіча, удзельніца патрыятычных маніфестацый 1861–1863 гг., сасланая ў Салікамск;\n• Францішак Рамейка (1885–1931) — беларускі каталіцкі святар, паслядоўны дзеяч Беларускай хрысціянскай дэмакратыі (БХД);\n• Апалінар Багушэвіч (1846–1930) — родны брат Францішка Багушэвіча, удзельнік паўстання 1863 года;\n• Канут Русецкі (1800–1860) і яго сын Баляслаў Русецкі (1824–1913) — славутыя мастакі віленскай школы («Літвінка з вербамі», «Жняя»);\n• Лявон Бароўскі (1784–1846) — ураджэнец Піншчыны, прафесар рыторыкі і паэзіі, духоўны настаўнік Адама Міцкевіча і філаматаў;\n• Сям'я Здановічаў: гісторык Аляксандр Здановіч (1805–1868) і кенатаф яго сына Ігната Здановіча (1841–1864) — кіраўніка паўстання Каліноўскага ў Вільні, пакаранага на Лукішках;\n• Юзаф Чаховіч (1819–1888) — пачынальнік мастацкай фатаграфіі ў Беларусі і Літве (ураджэнец Полаччыны);\n• Францішак Нарвойш (1742–1819) — матэматык і астраном;\n• Вікенцій і Аляксандр Сляндзінскія — мастакі;\n• Люцыян Узембла (1864–1942) — гісторык культуры і краязнавец.",
            "ru": "Žvirgždyno g. 3, Вильнюс. Один из старейших некрополей Вильнюса (осн. 1810 г.) в Заречье (Ужупис). Здесь похоронены выдающиеся деятели науки, культуры и освободительного движения Беларуси и Литвы: профессор С. Б. Юндзилл, пианистка и повстанка Камилла Марцинкевич (дочь В. Дунина-Марцинкевича), ксёндз-возрожденец Ф. Ромейко, брат Франтишка Богушевича Аполлинарий Богушевич, художники Канутий и Болеслав Русецкие, профессор Леон Боровский (учитель А. Мицкевича), фотограф Юзеф Чехович, семья Здановичей с кенотафом повстанца Игнатия Здановича.",
            "en": "Žvirgždyno g. 3, Užupis, Vilnius. Founded in 1810, the Bernardine Cemetery is one of Vilnius's most significant historical necropolises. Inscribed above its gate is 'Non omnis moriar'. Interred here are prominent figures of Belarusian and Lithuanian history: botanist Stanisław Bonifacy Jundziłł, composer and 1863 rebel Kamila Martsinkevich (daughter of Vincent Dunin-Marcinkievič), Belarusian revivalist priest Franciszak Ramejka, Apolinar Bahushevich (brother of Francišak Bahuševič), classic painters Kanuty and Bolesław Rusiecki, professor Leon Borowski (tutor to Adam Mickiewicz), pioneering photographer Józef Czechowicz, and the Zdanowicz family memorial (including 1863 insurgent Ignat Zdanowicz)."
        }
        bp['links'] = [
            {"title": "Бернардзінскія могілкі (be.wikipedia)", "url": "https://be.wikipedia.org/wiki/Бернардзінскія_могілкі_(Вільня)"},
            {"title": "Карта «Беларуская Вільня»", "url": "https://www.google.com/maps/d/viewer?mid=1fohygMcC3bikWPX5K1r288vnOFs"}
        ]
        bp['mustSee'] = True
        bp['personIds'] = [
            "stanislaw-bonifacy-jundzill",
            "kamila-martsinkevich",
            "franciszak-ramejka",
            "apolinar-bahusevic",
            "kanuty-rusiecki",
            "leon-borowski",
            "ignat-zdanovich",
            "jozef-czechowicz"
        ]
        bp['items'] = [
            {
                "title": "Магіла прафесара Станіслава Баніфацыя Юндзіла",
                "person": "Станіслаў Баніфацы Юндзіл (1761–1847)",
                "personId": "stanislaw-bonifacy-jundzill",
                "year": "1847",
                "description": "Магіла выбітнага прыродазнаўца, даследчыка флоры і фаўны Беларусі і Літвы, прафесара батанікі і заалогіі Віленскага ўніверсітэта. Побач пахаваны яго пляменнік і паслядоўнік прафесар Юзаф Юндзіл (1794–1877)."
            },
            {
                "title": "Магіла Камілы Марцінкевіч",
                "person": "Каміла Марцінкевіч (1837–1887)",
                "personId": "kamila-martsinkevich",
                "year": "1887",
                "description": "Месца спачыну таленавітай піяністкі, кампазітаркі і педагога, дачкі класіка беларускай літаратуры Вінцэнта Дуніна-Марцінкевіча. За патрыятычныя выступы ў Мінску была арыштаваная і высланая ў Сібір (Салікамск)."
            },
            {
                "title": "Магіла ксяндза Францішка Рамейкі",
                "person": "Францішак Рамейка (1885–1931)",
                "personId": "franciszak-ramejka",
                "year": "1931",
                "description": "Магіла беларускага каталіцкага святара-адраджэнца, дзеяча Беларускай хрысціянскай дэмакратыі (БХД), які паслядоўна ўводзіў беларускую мову ў набажэнствы і змагаўся за правы беларусаў у міжваеннай Польшчы."
            },
            {
                "title": "Магіла Апалінара Багушэвіча",
                "person": "Апалінар Багушэвіч (1846–1930)",
                "personId": "apolinar-bahusevic",
                "year": "1930",
                "description": "Магіла роднага брата пачынальніка новай беларускай літаратуры Францішка Багушэвіча. Удзельнік вызвольнага паўстання 1863 года, судовы дзеяч у Вільні."
            },
            {
                "title": "Надмагілле мастакоў Канута і Баляслава Русецкіх",
                "person": "Канут Русецкі (1800–1860), Баляслаў Русецкі (1824–1913)",
                "personId": "kanuty-rusiecki",
                "year": "1860",
                "description": "Фамільнае пахаванне славутых жывапісцаў віленскай школы. Канут Русецкі — аўтар культавых палотнаў «Літвінка з вербамі», «Жняя» і фрэсак віленскіх храмаў; яго сын Баляслаў працягнуў традыцыі бацькі."
            },
            {
                "title": "Магіла прафесара Лявона Бароўскага",
                "person": "Лявон Бароўскі (1784–1846)",
                "personId": "leon-borowski",
                "year": "1846",
                "description": "Магіла ўраджэнца Піншчыны, літаратуразнаўцы і прафесара Віленскага ўніверсітэта, які быў духоўным настаўнікам Адама Міцкевіча і філаматаў."
            },
            {
                "title": "Сямейны помнік Здановічаў (кенатаф паўстанца Ігната Здановіча)",
                "person": "Аляксандр Здановіч (1805–1868), Ігнат Здановіч (1841–1864)",
                "personId": "ignat-zdanovich",
                "year": "1868",
                "description": "Сямейная магіла гісторыка і педагога Аляксандра Здановіча. На надмагільным помніку высечаны мемарыяльны надпіс (кенатаф) у гонар яго сына Ігната Здановіча — кіраўніка паўстання Каліноўскага ў Вільні, пакаранага Мураўёвым на Лукішках."
            },
            {
                "title": "Магіла фатографа Юзафа Чаховіча",
                "person": "Юзаф Чаховіч (1819–1888)",
                "personId": "jozef-czechowicz",
                "year": "1888",
                "description": "Магіла выбітнага майстра святлапісу, ураджэнца Полацкага павета. Піянер гарадской фатаграфіі, які пакінуў неацэнныя відавыя здымкі Вільні, Віцебска і Беларусі другой паловы XIX ст."
            }
        ]

    # Link vilnia-dom-yundzila to stanislaw-bonifacy-jundzill
    if 'vilnia-dom-yundzila' in places_map:
        places_map['vilnia-dom-yundzila']['personIds'] = ["stanislaw-bonifacy-jundzill"]

    # 6. ADD / UPDATE PERSONS
    new_persons = [
        {
            "id": "stanislaw-bonifacy-jundzill",
            "name": {
                "by": "Станіслаў Баніфацы Юндзіл",
                "ru": "Станислав Бонифаций Юндзилл",
                "en": "Stanisław Bonifacy Jundziłł"
            },
            "dates": "1761–1847",
            "role": {
                "by": "Прыродазнавец, батанік, прафесар Віленскага ўніверсітэта",
                "ru": "Естествоиспытатель, ботаник, профессор Виленского университета",
                "en": "Naturalist, botanist, professor at Vilnius University"
            },
            "bio": {
                "by": "Нарадзіўся ў вёсцы Ясянцы Лідскага павета. Адзін з першых даследчыкаў расліннага і жывёльнага свету Беларусі і Літвы. Аўтар фундаментальных прац «Апісанне раслін, якія растуць у правінцыі ВКЛ» (1791) і «Прыкладная батаніка» (1799). Заснавальнік Батанічнага саду Віленскага ўніверсітэта ў Сэрэкішках.",
                "ru": "Родился в д. Ясенцы Лидского уезда. Выдающийся естествоиспытатель, автор первых научных трудов о флоре и фауне земель ВКЛ и основатель Вильнюсского ботанического сада.",
                "en": "Born in Jasiency, Lida district. Pioneer of botanical and zoological research in Belarus and Lithuania. Founded the Botanical Garden of Vilnius University."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Stanis%C5%82aw_Bonifacy_Jundzi%C5%82%C5%82.jpg/800px-Stanis%C5%82aw_Bonifacy_Jundzi%C5%82%C5%82.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Станіслаў_Баніфацый_Юндзіл",
            "placeIds": [
                "vilnia-dom-yundzila",
                "vilnia-bernardynskiya-mohilki-dze-pakhavany-stanisla"
            ]
        },
        {
            "id": "kamila-martsinkevich",
            "name": {
                "by": "Каміла Марцінкевіч",
                "ru": "Камилла Марцинкевич",
                "en": "Kamila Martsinkevich"
            },
            "dates": "1837–1887",
            "role": {
                "by": "Піяністка, кампазітарка, педагог, удзельніца паўстання 1863 года",
                "ru": "Пианистка, композитор, педагог, участница восстания 1863 года",
                "en": "Pianist, composer, educator, 1863 January Uprising activist"
            },
            "bio": {
                "by": "Дачка класіка беларускай літаратуры Вінцэнта Дуніна-Марцінкевіча. Таленавітая піяністка і кампазітарка, выступала з канцэртамі ў Мінску, Вільні і Варшаве. Арганізатарка нелегальнай школы для бедных дзяцей у Мінску і патрыятычных маніфестацый 1861 года. Была арыштаваная царскімі ўладамі і сасланая ў Салікамск. Пасля вызвалення жыла і памерла ў Вільні.",
                "ru": "Дочь классика белорусской литературы В. Дунина-Марцинкевича. Пианистка и композитор. Активная участница национально-освободительного движения в Минске перед восстанием 1863 г., была сослана в Соликамск.",
                "en": "Daughter of Belarusian literary classic Vincent Dunin-Marcinkievič. Accomplished pianist, composer, and educator. Exiled to Solikamsk for her patriotic activism prior to the 1863 Uprising."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Kamila_Martsinkevich.jpg/600px-Kamila_Martsinkevich.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Каміла_Марцінкевіч",
            "placeIds": [
                "vilnia-bernardynskiya-mohilki-dze-pakhavany-stanisla"
            ]
        },
        {
            "id": "franciszak-ramejka",
            "name": {
                "by": "Францішак Рамейка",
                "ru": "Франтишек Ромейко",
                "en": "Franciszak Ramejka"
            },
            "dates": "1885–1931",
            "role": {
                "by": "Беларускі каталіцкі святар, грамадскі і асветніцкі дзеяч",
                "ru": "Белорусский католический священник, общественный деятель",
                "en": "Belarusian Catholic priest, national revival activist"
            },
            "bio": {
                "by": "Дзеяч беларускага хрысціянскага адраджэння, актывіст Беларускай хрысціянскай дэмакратыі (БХД). Паслядоўна выступаў за беларусізацыю касцельнага жыцця, гаварыў казанні на беларускай мове, адкрываў беларускія школы і падтрымліваў нацыянальны друк у Заходняй Беларусі. Пахаваны на Бернардзінскіх могілках.",
                "ru": "Деятель белорусского католического возрождения, соратник Белорусской христианской демократии. Последовательно внедрял белорусский язык в костёлах Западной Беларуси.",
                "en": "Prominent Belarusian Catholic priest and advocate of the Belarusian Christian Democratic movement who fought for the use of Belarusian in church liturgy."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Franciszak_Ramejka.jpg/600px-Franciszak_Ramejka.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Францішак_Рамейка",
            "placeIds": [
                "vilnia-bernardynskiya-mohilki-dze-pakhavany-stanisla"
            ]
        },
        {
            "id": "apolinar-bahusevic",
            "name": {
                "by": "Апалінар Багушэвіч",
                "ru": "Аполлинарий Богушевич",
                "en": "Apolinar Bahusevic"
            },
            "dates": "1846–1930",
            "role": {
                "by": "Удзельнік паўстання 1863 года, брат Францішка Багушэвіча",
                "ru": "Участник восстания 1863 года, брат Франтишка Богушевича",
                "en": "1863 Insurgent, brother of Francišak Bahuševič"
            },
            "bio": {
                "by": "Родны брат пачынальніка новай беларускай літаратуры Францішка Багушэвіча. Разам з братам браў чынны ўдзел у паўстанні 1863–1864 гадоў. Пазней працаваў у віленскім акруговым судзе і быў прысяжным павераным.",
                "ru": "Брат белорусского поэта Франтишка Богушевича. Участник восстания 1863 года, юрист Виленского окружного суда.",
                "en": "Brother of national poet Francišak Bahuševič. Veteran of the 1863 January Uprising and attorney in Vilnius."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Bernardine_Cemetery7.jpg/600px-Bernardine_Cemetery7.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Бернардзінскія_могілкі_(Вільня)",
            "placeIds": [
                "vilnia-bernardynskiya-mohilki-dze-pakhavany-stanisla"
            ]
        },
        {
            "id": "leon-borowski",
            "name": {
                "by": "Лявон Бароўскі",
                "ru": "Леон Боровский",
                "en": "Leon Borowski"
            },
            "dates": "1784–1846",
            "role": {
                "by": "Філолаг, прафесар Віленскага ўніверсітэта, настаўнік Адама Міцкевіча",
                "ru": "Филолог, профессор Виленского университета, учитель Адама Мицкевича",
                "en": "Philologist, Vilnius University professor, mentor to Adam Mickiewicz"
            },
            "bio": {
                "by": "Нарадзіўся ў вёсцы Баравая на Піншчыне. Выбітны літаратуразнаўца і тэарэтык літаратуры, прафесар красамоўства і паэзіі Віленскага ўніверсітэта. Духоўны настаўнік Адама Міцкевіча і філаматаў, які першым распазнаў геній Міцкевіча і падтрымаў рамантычны кірунак у літаратуры.",
                "ru": "Уроженец Пинщины, профессор риторики и поэзии Виленского университета. Духовный наставник Адама Мицкевича и филоматов.",
                "en": "Born in Pinsk district. Professor of rhetoric and literature at Vilnius University, critical mentor to Adam Mickiewicz and the Philomaths."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Leon_Borowski.jpg/600px-Leon_Borowski.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Лявон_Бароўскі",
            "placeIds": [
                "vilnia-bernardynskiya-mohilki-dze-pakhavany-stanisla"
            ]
        },
        {
            "id": "ignat-zdanovich",
            "name": {
                "by": "Ігнат Здановіч",
                "ru": "Игнатий Зданович",
                "en": "Ignat Zdanovich"
            },
            "dates": "1841–1864",
            "role": {
                "by": "Кіраўнік паўстання 1863 года ў Вільні, паплечнік Кастуся Каліноўскага",
                "ru": "Руководитель восстания 1863 года в Вильне, соратник Кастуся Калиновского",
                "en": "Leader of the 1863 Uprising in Vilnius, associate of Kastuś Kalinoŭski"
            },
            "bio": {
                "by": "Нарадзіўся ў Вільні ў сям'і гісторыка Аляксандра Здановіча (родам з Ігуменшчыны). Публіцыст, адзін з кіраўнікоў віленскай паўстанцкай арганізацыі ў 1863 г., блізкі паплечнік Кастуся Каліноўскага. Пакараны смерцю праз павешанне на Лукішскім пляцы 2 студзеня 1864 года. На сямейнай магіле Здановічаў на Бернардзінскіх могілках усталяваны яго сімвалічны кенатаф.",
                "ru": "Публицист, один из руководителей виленской повстанческой организации, соратник К. Калиновского. Казнён на Лукишках в 1864 г. Символический кенотаф находится на семейном участке на Бернардинском кладбище.",
                "en": "Publicist and key organizer of the 1863 January Uprising in Vilnius alongside Kastuś Kalinoŭski. Executed on Lukiškių Square in 1864; commemorated on the family tomb at Bernardine Cemetery."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Ihnat_Zdanovi%C4%8D._%D0%86%D0%B3%D0%BD%D0%B0%D1%82_%D0%97%D0%B4%D0%B0%D0%BD%D0%BE%D0%B2%D1%96%D1%87_%281863%29.jpg/600px-Ihnat_Zdanovi%C4%8D._%D0%86%D0%B3%D0%BD%D0%B0%D1%82_%D0%97%D0%B4%D0%B0%D0%BD%D0%BE%D0%B2%D1%96%D1%87_%281863%29.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Ігнат_Аляксандравіч_Здановіч",
            "placeIds": [
                "vilnia-bernardynskiya-mohilki-dze-pakhavany-stanisla"
            ]
        },
        {
            "id": "jozef-czechowicz",
            "name": {
                "by": "Юзаф Чаховіч",
                "ru": "Юзеф Чехович",
                "en": "Józef Czechowicz"
            },
            "dates": "1819–1888",
            "role": {
                "by": "Фатограф, піянер мастацкай фатаграфіі ў Беларусі і Літве",
                "ru": "Фотограф, пионер художественной фотографии в Беларуси и Литве",
                "en": "Pioneering landscape and urban photographer"
            },
            "bio": {
                "by": "Нарадзіўся ў маёнтку Паперня Полацкага павета. Выдатны майстар святлапісу, заснавальнік аднаго з першых фотаатэлье ў Вільні. Стварыў неацэнную серыю фатаграфій Вільні, Полацка, Віцебска і Кіева 1860–1880-х гадоў.",
                "ru": "Уроженец Полоцкого уезда, выдающийся мастер фотографии, автор бесценных видовых фотолетописей Вильны и городов Беларуси XIX века.",
                "en": "Born in Polotsk district. Pioneering 19th-century photographer who captured historic urban landscapes of Vilnius, Polotsk, and Vitebsk."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/J%C3%B3zef_Czechowicz_autoportret.jpg/600px-J%C3%B3zef_Czechowicz_autoportret.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Юзаф_Чаховіч_(фатограф)",
            "placeIds": [
                "vilnia-bernardynskiya-mohilki-dze-pakhavany-stanisla"
            ]
        }
    ]

    for np in new_persons:
        persons_map[np['id']] = np

    # Also update kanuty-rusiecki to reference Bernardine Cemetery
    if 'kanuty-rusiecki' in persons_map:
        pids = persons_map['kanuty-rusiecki'].get('placeIds', [])
        if bp_id not in pids:
            pids.append(bp_id)
        persons_map['kanuty-rusiecki']['placeIds'] = pids

    # Reconstruct lists
    final_places = list(places_map.values())
    final_persons = list(persons_map.values())

    with open('data/places.json', 'w', encoding='utf-8') as f:
        json.dump(final_places, f, ensure_ascii=False, indent=2)

    with open('data/persons.json', 'w', encoding='utf-8') as f:
        json.dump(final_persons, f, ensure_ascii=False, indent=2)

    with open('data/places.js', 'w', encoding='utf-8') as f:
        f.write('window.INITIAL_PLACES = ' + json.dumps(final_places, ensure_ascii=False, indent=2) + ';\n')

    with open('data/persons.js', 'w', encoding='utf-8') as f:
        f.write('window.INITIAL_PERSONS = ' + json.dumps(final_persons, ensure_ascii=False, indent=2) + ';\n')

    print(f"Done! Places count: {len(final_places)}, Persons count: {len(final_persons)}")

if __name__ == '__main__':
    update_all()
