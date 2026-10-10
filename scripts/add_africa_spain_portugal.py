import json

def main():
    print("=== ADDING EMBASSIES IN AFRICA, SPAIN AND PORTUGAL DIASPORA HUB ===")

    with open('data/places.json', 'r', encoding='utf-8') as f:
        places = json.load(f)

    new_places = [
        {
            "id": "madrid-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў Іспаніі (Мадрыд)",
                "ru": "Посольство Беларуси в Испании (Мадрид)",
                "en": "Embassy of Belarus in Spain (Madrid)"
            },
            "category": "embassy",
            "country": {"by": "Іспанія", "ru": "Испания", "en": "Spain"},
            "city": {"by": "Мадрыд", "ru": "Мадрид", "en": "Madrid"},
            "coordinates": [40.483392, -3.668087],
            "description": {
                "by": "Адрас: Calle de Caleruega 81, oficina 2A, 28033 Madrid, Іспанія (раён Сьюдад-Лінеаль / Costillares, станцыя метро Pinar de Chamartín).\n\nДыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Каралеўстве Іспанія, афіцыйна адкрытае ў снежні 2016 года. Пасольства каардынуе двухбаковыя адносіны, гандлёва-эканамічныя і культурныя сувязі, а таксама прадстаўляе інтарэсы Беларусі пры Сусветнай турысцкай арганізацыі ААН (UN Tourism / ЮНВТО), штаб-кватэра якой знаходзіцца ў Мадрыдзе.",
                "ru": "Calle de Caleruega 81, оф. 2A, 28033 Мадрид (метро Pinar de Chamartín). Посольство Республики Беларусь в Королевстве Испания, открытое в декабре 2016 года. Представляет интересы Беларуси также при Всемирной туристской организации ООН (UN Tourism) со штаб-квартирой в Мадриде.",
                "en": "Calle de Caleruega 81, office 2A, 28033 Madrid, Spain (metro Pinar de Chamartín). Diplomatic mission of the Republic of Belarus to the Kingdom of Spain, opened in December 2016. Also represents Belarus at the UN Tourism headquarters based in Madrid."
            },
            "image": "https://thumb.wikimedia.org/wikipedia/commons/thumb/1/14/Madrid_-_Sky_Bar_360%C2%BA_%28Hotel_Riu_Plaza_Espa%C3%B1a%29%2C_vistas_19.jpg/960px-Madrid_-_Sky_Bar_360%C2%BA_%28Hotel_Riu_Plaza_Espa%C3%B1a%29%2C_vistas_19.jpg",
            "links": [
                {"title": "Посольство Республики Беларусь в Королевстве Испания", "url": "https://spain.mfa.gov.by"}
            ],
            "tags": ["Іспанія", "Мадрыд", "пасольства", "embassy", "дыпламатыя"],
            "personIds": []
        },
        {
            "id": "cairo-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў Егіпце (Каір)",
                "ru": "Посольство Беларуси в Египте (Каир)",
                "en": "Embassy of Belarus in Egypt (Cairo)"
            },
            "category": "embassy",
            "country": {"by": "Егіпет", "ru": "Египет", "en": "Egypt"},
            "city": {"by": "Каір", "ru": "Каир", "en": "Cairo"},
            "coordinates": [30.038896, 31.212556],
            "description": {
                "by": "Адрас: 26, Gaber Ebn Hayan str., Dokki-Giza, Cairo, Егіпет.\n\nДыпламатычная місія Рэспублікі Беларусь у Арабскай Рэспубліцы Егіпет, адкрытая ў 1997 годзе. Размешчана ў дыпламатычным раёне Докі каля заходняга берага ракі Ніл. Галоўны дыпламатычны хаб Беларусі ў Паўночнай Афрыцы і на Блізкім Усходзе, па сумяшчальніцтве прадстаўляе інтарэсы Беларусі ў Алжыры, Судане і Амане, а таксама пры Лізе арабскіх дзяржаў.",
                "ru": "26, Gaber Ebn Hayan str., Докки-Гиза, Каир. Посольство Республики Беларусь в Арабской Республике Египет (открыто в 1997 г.). Главный дипломатический хаб Беларуси в Северной Африке; по совместительству представляет интересы в Алжире, Судане и Омане, а также при Лиге арабских государств.",
                "en": "26, Gaber Ebn Hayan str., Dokki-Giza, Cairo, Egypt. Diplomatic mission of the Republic of Belarus to the Arab Republic of Egypt, opened in 1997 in the Dokki district near the Nile. Serves as Belarus's primary diplomatic hub in North Africa, concurrently accredited to Algeria, Sudan, Oman, and the Arab League."
            },
            "image": "https://thumb.wikimedia.org/wikipedia/commons/thumb/7/72/Cairo_Opera_House%2C_Al_Hurriyah_Park_and_the_Nile_river_%2814797782354%29.jpg/960px-Cairo_Opera_House%2C_Al_Hurriyah_Park_and_the_Nile_river_%2814797782354%29.jpg",
            "links": [
                {"title": "Посольство Республики Беларусь в Арабской Республике Египет", "url": "https://egypt.mfa.gov.by"}
            ],
            "tags": ["Егіпет", "Каір", "Афрыка", "пасольства", "embassy", "дыпламатыя"],
            "personIds": []
        },
        {
            "id": "pretoria-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў ПАР (Прэторыя)",
                "ru": "Посольство Беларуси в ЮАР (Претория)",
                "en": "Embassy of Belarus in South Africa (Pretoria)"
            },
            "category": "embassy",
            "country": {"by": "Паўднёва-Афрыканская Рэспубліка", "ru": "Южно-Африканская Республика", "en": "South Africa"},
            "city": {"by": "Прэторыя", "ru": "Претория", "en": "Pretoria"},
            "coordinates": [-25.792499, 28.232406],
            "description": {
                "by": "Адрас: 164 Orion Avenue, Sterrewag, Pretoria 0181, ПАР.\n\nДыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Паўднёва-Афрыканскай Рэспубліцы (адкрыта ў 2000 годзе). Першае пасольства Беларусі ў субсахарскай Афрыцы, размешчанае ў адміністрацыйнай сталіцы Прэторыі. Пасольства таксама курыруе двухбаковыя адносіны з краінамі паўднёвага рэгіёна Афрыкі (Ангола, Батсвана, Мазамбік, Намібія, Эсваціні).",
                "ru": "164 Orion Avenue, Стерревах, Претория 0181, ЮАР. Посольство Республики Беларусь в Южно-Африканской Республике (открыто в 2000 г.) — первое дипломатическое представительство Беларуси в странах Африки южнее Сахары. Курирует также отношения с Анголой, Ботсваной, Мозамбиком, Намибией.",
                "en": "164 Orion Avenue, Sterrewag, Pretoria 0181, South Africa. Diplomatic mission of the Republic of Belarus to the Republic of South Africa, established in 2000. Belarus's first embassy in Sub-Saharan Africa, also covering relations with Angola, Botswana, Mozambique, and Namibia."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/6/6b/Uniegebou.jpg",
            "links": [
                {"title": "Посольство Республики Беларусь в Южно-Африканской Республике", "url": "https://rsa.mfa.gov.by"}
            ],
            "tags": ["ПАР", "Прэторыя", "Афрыка", "пасольства", "embassy", "дыпламатыя"],
            "personIds": []
        },
        {
            "id": "abuja-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў Нігерыі (Абуджа)",
                "ru": "Посольство Беларуси в Нигерии (Абуджа)",
                "en": "Embassy of Belarus in Nigeria (Abuja)"
            },
            "category": "embassy",
            "country": {"by": "Нігерыя", "ru": "Нигерия", "en": "Nigeria"},
            "city": {"by": "Абуджа", "ru": "Абуджа", "en": "Abuja"},
            "coordinates": [9.042346, 7.519686],
            "description": {
                "by": "Адрас: 1866 Deng Xiaoping Street, Plot 2148, Asokoro, Abuja, Нігерыя.\n\nДыпламатычная місія Рэспублікі Беларусь у Федэратыўнай Рэспубліцы Нігерыя, адкрытая ў снежні 2011 года. Размешчана ў дыпламатычным квартале Асакора федэральнай сталіцы Абуджа. Галоўнае прадстаўніцтва Беларусі ў Заходняй Афрыцы, адказвае таксама за адносіны з Ганай, Кот-д'Івуарам, Камерунам і ЭКОВАС (Эканамічнай супольнасцю краін Заходняй Афрыкі).",
                "ru": "1866 Deng Xiaoping Street, Asokoro, Абуджа, Нигерия. Посольство Республики Беларусь в Федеративной Республике Нигерия (открыто в декабре 2011 г.). Главное дипломатическое представительство Беларуси в Западной Африке, аккредитованное также в Гане, Кот-д'Ивуаре, Камеруне и при ЭКОВАС.",
                "en": "1866 Deng Xiaoping Street, Asokoro, Abuja, Nigeria. Diplomatic mission of the Republic of Belarus to the Federal Republic of Nigeria, opened in December 2011 in the Asokoro district. Serves as Belarus's primary diplomatic outpost in West Africa, concurrently covering Ghana, Côte d'Ivoire, Cameroon, and ECOWAS."
            },
            "image": "https://thumb.wikimedia.org/wikipedia/commons/thumb/1/1b/Abuja_heritages_30.jpg/960px-Abuja_heritages_30.jpg",
            "links": [
                {"title": "Посольство Республики Беларусь в Федеративной Республике Нигерия", "url": "https://nigeria.mfa.gov.by"}
            ],
            "tags": ["Нігерыя", "Абуджа", "Афрыка", "пасольства", "embassy", "дыпламатыя"],
            "personIds": []
        },
        {
            "id": "nairobi-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў Кеніі (Найробі)",
                "ru": "Посольство Беларуси в Кении (Найроби)",
                "en": "Embassy of Belarus in Kenya (Nairobi)"
            },
            "category": "embassy",
            "country": {"by": "Кенія", "ru": "Кения", "en": "Kenya"},
            "city": {"by": "Найробі", "ru": "Найроби", "en": "Nairobi"},
            "coordinates": [-1.276734, 36.787901],
            "description": {
                "by": "Адрас: Dik Dik Gardens, House 8, Kileleshwa, Nairobi, Кенія.\n\nДыпламатычная місія Рэспублікі Беларусь у Рэспубліцы Кенія, адкрытая ў 2018 годзе ў раёне Кілелешва. З'яўляецца пастаянным прадстаўніцтвам Беларусі пры праграмах ААН у Найробі (ЮНЕП — Праграма ААН па навакольным асяроддзі і ААН-Хабітат). Прадстаўляе інтарэсы Беларусі ва Усходняй Афрыцы (па сумяшчальніцтве ва Угандзе, Танзаніі, Эфіопіі).",
                "ru": "Dik Dik Gardens, дом 8, Килелешва, Найроби, Кения. Посольство Республики Беларусь в Республике Кения (открыто в 2018 г.). Является постоянным представительством при структурах ООН в Найроби (ЮНЕП и ООН-Хабитат); представляет интересы также в Уганде, Танзании и Эфиопии.",
                "en": "Dik Dik Gardens, House 8, Kileleshwa, Nairobi, Kenya. Diplomatic mission of Belarus to the Republic of Kenya, opened in 2018. Serves as permanent representation to UN bodies in Nairobi (UNEP and UN-Habitat) and covers relations with Uganda, Tanzania, and Ethiopia."
            },
            "image": "https://thumb.wikimedia.org/wikipedia/commons/thumb/b/be/Nairobi_skyline_from_Gem_Hotel.jpg/960px-Nairobi_skyline_from_Gem_Hotel.jpg",
            "links": [
                {"title": "Посольство Республики Беларусь в Республике Кения", "url": "https://kenya.mfa.gov.by"}
            ],
            "tags": ["Кенія", "Найробі", "Афрыка", "пасольства", "embassy", "ААН", "дыпламатыя"],
            "personIds": []
        },
        {
            "id": "harare-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў Зімбабвэ (Харарэ)",
                "ru": "Посольство Беларуси в Зимбабве (Хараре)",
                "en": "Embassy of Belarus in Zimbabwe (Harare)"
            },
            "category": "embassy",
            "country": {"by": "Зімбабвэ", "ru": "Зимбабве", "en": "Zimbabwe"},
            "city": {"by": "Харарэ", "ru": "Хараре", "en": "Harare"},
            "coordinates": [-17.788451, 31.118514],
            "description": {
                "by": "Адрас: 47A Dover Road, Chisipite, Harare, Зімбабвэ.\n\nДыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Рэспубліцы Зімбабвэ, афіцыйна адкрытае ў ліпені 2022 года ў прадмесці Чызіпіт сталіцы Харарэ. Створана як ключавы партнёрскі і лагістычны вузел Беларусі на поўдні Афрыкі для каардынацыі маштабных паставак сельскагаспадарчай і кар'ернай тэхнікі, адукацыйных і прамысловых праектаў.",
                "ru": "47A Dover Road, Чизипит, Хараре, Зимбабве. Посольство Республики Беларусь в Республике Зимбабве, официально открытое в июле 2022 года. Ключевой партнёрский центр Беларуси на юге Африки для координации сельскохозяйственных, промышленных и образовательных проектов.",
                "en": "47A Dover Road, Chisipite, Harare, Zimbabwe. Official diplomatic mission of Belarus to Zimbabwe, opened in July 2022. Established as a strategic economic and technological partner hub in Southern Africa for agricultural machinery supply and joint projects."
            },
            "image": "https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d0/Crowne_Plaza%2C_Harare.png/960px-Crowne_Plaza%2C_Harare.png",
            "links": [
                {"title": "Посольство Республики Беларусь в Республике Зимбабве", "url": "https://zimbabwe.mfa.gov.by"}
            ],
            "tags": ["Зімбабвэ", "Харарэ", "Афрыка", "пасольства", "embassy", "дыпламатыя"],
            "personIds": []
        },
        {
            "id": "portugal-belarusian-diaspora-peoples-embassy",
            "title": {
                "by": "Народная амбасада Беларусі і беларуская супольнасць у Партугаліі (Лісабон)",
                "ru": "Народное посольство Беларуси и белорусская община в Португалии (Лиссабон)",
                "en": "People's Embassy of Belarus & Belarusian Community in Portugal (Lisbon)"
            },
            "category": "culture",
            "country": {"by": "Партугалія", "ru": "Португалия", "en": "Portugal"},
            "city": {"by": "Лісабон", "ru": "Лиссабон", "en": "Lisbon"},
            "coordinates": [38.707751, -9.136592],
            "description": {
                "by": "Лісабон / Порту, Партугальская Рэспубліка.\n\nАсяродак беларускай дыяспары і Народнай амбасады Беларусі ў Партугаліі (Embaixada Popular de Belarus em Portugal). Афіцыйнага рэзідэнтнага пасольства Рэспублікі Беларусь у Партугаліі няма (двухбаковыя адносіны курыруюцца пасольствам у Францыі / Іспаніі па сумяшчальніцтве). Беларуская грамада ў Лісабоне з 2020 года аб'ядноўвае суайчыннікаў, ладзіць культурныя і грамадскія імпрэзы, знаёміць партугальцаў з беларускай культурай, гісторыяй і традыцыямі, а таксама аказвае прававую і адаптацыйную падтрымку беларусам у Партугаліі.",
                "ru": "Лиссабон / Порту, Португалия. Центр белорусской диаспоры и Народного посольства Беларуси в Португалии (Embaixada Popular de Belarus em Portugal). Официального посольства Беларуси в Португалии нет (аккредитовано посольство во Франции/Испании). Сообщество проводит культурные мероприятия, знакомит жителей Португалии с белорусской культурой и поддерживает соотечественников.",
                "en": "Lisbon / Porto, Portugal. Hub of the Belarusian diaspora and the People's Embassy of Belarus in Portugal (Embaixada Popular de Belarus em Portugal). Belarus maintains no resident official embassy in Portugal (covered concurrently via Paris/Madrid). The local community organizes cultural events, promotes Belarusian identity, and assists newcomers in Portugal."
            },
            "image": "https://thumb.wikimedia.org/wikipedia/commons/thumb/f/f2/Lisboa_-_Portugal_%2852597836992%29.jpg/960px-Lisboa_-_Portugal_%2852597836992%29.jpg",
            "links": [
                {"title": "Народныя амбасады Беларусі", "url": "https://belarusabroad.org"}
            ],
            "tags": ["Партугалія", "Лісабон", "дыяспара", "Народная амбасада", "культура"],
            "personIds": [],
            "mustSee": True
        }
    ]

    places_ids = {p['id'] for p in places}
    added_count = 0
    for np in new_places:
        if np['id'] not in places_ids:
            places.append(np)
            added_count += 1
            print(f"Added place: {np['id']}")

    print(f"Total places added: {added_count}")

    # Fix Jakarta Embassy coordinates (Southern hemisphere negative latitude!)
    for p in places:
        if p['id'] == 'jakarta-embassy-belarus':
            p['coordinates'] = [-6.232704, 106.832043]
            p['description']['by'] = "Адрас: Jl. Patra Kuningan VII, no.3, Kuningan, Jakarta Selatan 12950, Інданезія.\n\nДыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Рэспубліцы Інданезія (адкрыта ў 2011 г.). Размешчана ў дыпламатычным квартале Патра-Кунінган у Паўднёвай Джакарце. Таксама па сумяшчальніцтве прадстаўляе інтарэсы Беларусі ў Сінгапуры, Малайзіі, Філіпінах і пры АСЕАН."
            p['description']['ru'] = "Jl. Patra Kuningan VII, no.3, Кунинган, Южная Джакарта 12950. Посольство Республики Беларусь в Республике Индонезия (открыто в 2011 г.). По совместительству представляет интересы в Сингапуре, Малайзии, на Филиппинах и при АСЕАН."
            p['description']['en'] = "Jl. Patra Kuningan VII, no.3, Kuningan, South Jakarta 12950. Diplomatic mission of Belarus to the Republic of Indonesia (opened in 2011). Concurrently accredited to Singapore, Malaysia, the Philippines, and ASEAN."
            print("Fixed Jakarta Embassy coordinates to [-6.232704, 106.832043]")

    with open('data/places.json', 'w', encoding='utf-8') as f:
        json.dump(places, f, ensure_ascii=False, indent=2)
    with open('data/places.js', 'w', encoding='utf-8') as f:
        f.write('window.INITIAL_PLACES = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

    print("Successfully updated data/places.json and data/places.js")

if __name__ == '__main__':
    main()
