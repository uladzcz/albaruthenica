import json

def main():
    print("=== ADDING SOUTH AMERICA (ARGENTINA & BRAZIL) HERITAGE PLACES & PERSONS ===")

    with open('data/places.json', 'r', encoding='utf-8') as f:
        places = json.load(f)
    with open('data/persons.json', 'r', encoding='utf-8') as f:
        persons = json.load(f)

    # 1. Add Kastus Merlyak to persons
    person_ids = {p['id'] for p in persons}
    if 'kastus-merlyak' not in person_ids:
        persons.append({
            "id": "kastus-merlyak",
            "name": {
                "by": "Кастусь Мерляк",
                "ru": "Константин Мерляк",
                "en": "Kastus Merlyak"
            },
            "dates": "1919–2007",
            "role": {
                "by": "Дзеяч беларускай эміграцыі ў Аргенціне і ЗША, кіраўнік прадстаўніцтва Рады БНР у Аргенціне",
                "ru": "Деятель белорусской эмиграции в Аргентине и США, глава представительства Рады БНР в Аргентине",
                "en": "Leader of the Belarusian diaspora in Argentina and the US, representative of Rada BNR in Argentina"
            },
            "bio": {
                "by": "Нарадзіўся ў вёсцы Дзяцел Навагрудскага павета. Пасля Другой сусветнай вайны прыбыў у Буэнас-Айрэс, дзе ў 1948 годзе стаў адным з заснавальнікаў і старшынёй Згуртавання беларусаў у Аргенціне (ЗБА) і прадстаўніком Рады БНР. Пасля пераезду ў ЗША ўзначальваў Беларуска-Амерыканскую Асацыяцыю (БАЗА) і быў адным з заснавальнікаў сабора Св. Кірылы Тураўскага ў Брукліне.",
                "ru": "Родился в д. Дятел Новогрудского уезда. В 1948 г. в Буэнос-Айресе возглавил Объединение белорусов в Аргентине и представительство Рады БНР. Позднее в США — многолетний председатель БАЗА и деятель прихода св. Кирилла Туровского в Бруклине.",
                "en": "Born in Dziatsel, Navahrudak district. Founded and led the Association of Belarusians in Argentina (1948) and the Rada BNR South American mission. Later in the US, chaired the Belarusian-American Association (BAZA) and co-founded St. Cyril of Turau Cathedral in Brooklyn."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Kal_arg_bel.JPG/800px-Kal_arg_bel.JPG",
            "wiki": "https://be.wikipedia.org/wiki/Кастусь_Мерляк",
            "placeIds": ["buenos-aires-zhurtavannie-belarusau-arhentine-merlyak"],
            "wikidataId": "Q12860875"
        })
        print("Added person: kastus-merlyak")

    # Ensure Yanka Kupala has obera in placeIds
    for p in persons:
        if p['id'] == 'yanka-kupala':
            p_places = set(p.get('placeIds', []))
            p_places.add('obera-parque-de-las-naciones-colectividad-bielorrusa')
            p['placeIds'] = list(p_places)

    # Ensure Kastus Kalinouski has llavallol in placeIds
    for p in persons:
        if p['id'] == 'kastus-kalinouski':
            p_places = set(p.get('placeIds', []))
            p_places.add('llavallol-cultural-center-kastus-kalinouski')
            p['placeIds'] = list(p_places)

    # 2. Add New Places in Argentina and Brazil
    new_places = [
        {
            "id": "berisso-club-vostok-colectividad-bielorrusa",
            "title": {
                "by": "Клуб «Усход» (Club Vostok) — Беларуская грамада ў Берыса",
                "ru": "Клуб «Восток» (Club Vostok) — Белорусская община в Бериссо",
                "en": "Club Vostok — Belarusian Community of Berisso"
            },
            "category": "culture",
            "country": {"by": "Аргенціна", "ru": "Аргентина", "en": "Argentina"},
            "city": {"by": "Берыса", "ru": "Бериссо", "en": "Berisso"},
            "coordinates": [-34.880969, -57.889310],
            "description": {
                "by": "Адрас: Calle 13 y 165 (Calle 13 / Trieste 4381), Berisso, правінцыя Буэнас-Айрэс.\n\nГалоўны гістарычны асяродак беларускай супольнасці ў Аргенціне і ва ўсёй Паўднёвай Амерыцы з бесперапыннай традыцыяй. Заснаваны ў 1941 годзе як Беларускае таварыства (першапачаткова названае ў гонар Францыска Скарыны), пазней стала вядомае як клуб «Усход» (Club Social, Cultural y Deportivo Vostok Colectividad Bielorrusa). Клуб аб'яднаў пакаленні выхадцаў з Заходняй Беларусі. Славуты танцавальны ансамбль «Чайка» ў 1958 годзе заваяваў першую прэмію на ўсеаргентынскім фестывалі фальклору. Клуб нязменна прадстаўляе Беларусь і яе традыцыі на штогадовым Нацыянальным фестывалі імігрантаў у Берыса (Fiesta Provincial del Inmigrante).",
                "ru": "Calle 13 y 165, Бериссо, провинция Буэнос-Айрес. Главный и старейший действующий очаг белорусской общины в Аргентине и Южной Америке (осн. 1941 г. как общество имени Франциска Скорины, ныне клуб «Восток» / Club Vostok). Знаменит танцевальным ансамблем «Чайка» и постоянным участием в ежегодном Фестивале иммигрантов в Бериссо.",
                "en": "Calle 13 & 165, Berisso, Buenos Aires Province. The primary and oldest continuous hub of the Belarusian community in Argentina and South America, founded in 1941 as the Francis Skaryna Society (later Club Vostok / Colectividad Bielorrusa). Home to the award-winning 'Chaika' folk dance ensemble and regular participant in the Berisso National Immigrant Festival."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Colectividad_Bielorrusa_de_Argentina.jpg/800px-Colectividad_Bielorrusa_de_Argentina.jpg",
            "links": [
                {"title": "Беларусы ў Аргенціне (be.wikipedia)", "url": "https://be.wikipedia.org/wiki/Беларусы_ў_Аргенціне"},
                {"title": "Наша Ніва: Беларусы ў Аргенціне", "url": "https://nashaniva.com/34598"}
            ],
            "tags": ["Аргенціна", "Берыса", "дыяспара", "культура", "Скарына", "Усход"],
            "personIds": [],
            "mustSee": True
        },
        {
            "id": "llavallol-cultural-center-kastus-kalinouski",
            "title": {
                "by": "Беларускі культурны цэнтр імя Кастуся Каліноўскага ў Лаваёлі",
                "ru": "Белорусский культурный центр имени Кастуся Калиновского в Лавайоле",
                "en": "Kastus Kalinouski Belarusian Cultural Center in Llavallol"
            },
            "category": "culture",
            "country": {"by": "Аргенціна", "ru": "Аргентина", "en": "Argentina"},
            "city": {"by": "Лаваёль", "ru": "Лавайол", "en": "Llavallol"},
            "coordinates": [-34.803970, -58.435421],
            "description": {
                "by": "Адрас: Calle Duhalde 265, Llavallol, партыда Ламас-дэ-Самора (Lomas de Zamora), правінцыя Буэнас-Айрэс.\n\nАдкрыты 24 сакавіка 2010 года пры клубе «Дніпро» — першы Беларускі культурны цэнтр імя Кастуся Каліноўскага ў Лацінскай Амерыцы. Створаны для захавання і папулярызацыі беларускай мовы, гісторыі, фальклору і традыцыйнай культуры сярод нашчадкаў беларускіх імігрантаў і аргентынцаў. Пры цэнтры дзейнічаў беларускі фальклорны ансамбль «Белавеж», ладзіліся курсы беларускай мовы, выставы народнай вышыўкі і ўрачыстыя вечарыны да юбілеяў Янкі Купалы, Якуба Коласа, Максіма Танка і Кастуся Каліноўскага.",
                "ru": "Calle Duhalde 265, Лавайол (Большой Буэнос-Айрес). Открыт 24 марта 2010 г. при клубе «Днипро» — первый в Латинской Америке культурный центр имени национального героя Беларуси Кастуся Калиновского (ансамбль «Беловеж», курсы языка, выставки, литературные вечера).",
                "en": "Calle Duhalde 265, Llavallol, Greater Buenos Aires. Opened on March 24, 2010 at Club Dnipro as the first Kastus Kalinouski Belarusian Cultural Center in Latin America. Dedicated to preserving Belarusian language, history, folk embroidery, and music ('Bielaviez' ensemble)."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Colectividad_bielorrusa%2C_rusa_y_ucraniana_-_Dia_del_Inmigrante_en_el_Planetario_Galileo_Galilei.jpg/800px-Colectividad_bielorrusa%2C_rusa_y_ucraniana_-_Dia_del_Inmigrante_en_el_Planetario_Galileo_Galilei.jpg",
            "links": [
                {"title": "Беларусы ў Аргенціне (be.wikipedia)", "url": "https://be.wikipedia.org/wiki/Беларусы_ў_Аргенціне"}
            ],
            "tags": ["Аргенціна", "Буэнас-Айрэс", "Лаваёль", "Каліноўскі", "культура", "мова"],
            "personIds": ["kastus-kalinouski"],
            "mustSee": True
        },
        {
            "id": "obera-parque-de-las-naciones-colectividad-bielorrusa",
            "title": {
                "by": "Парк нацыянальнасцей і Дом беларускай грамады з бюстам Янкі Купалы ў Обэры",
                "ru": "Парк национальностей и Дом белорусской общины с бюстом Янки Купалы в Обера",
                "en": "Parque de las Naciones & Belarusian Community House with Yanka Kupala Bust in Oberá"
            },
            "category": "culture",
            "country": {"by": "Аргенціна", "ru": "Аргентина", "en": "Argentina"},
            "city": {"by": "Обэра", "ru": "Обера", "en": "Oberá"},
            "coordinates": [-27.498703, -55.112500],
            "description": {
                "by": "Адрас: Parque de las Naciones, Oberá, правінцыя Місьёнес (Misiones), Аргенціна.\n\nПравінцыя Місьёнес на паўночным усходзе Аргенціны ў міжваенныя дзесяцігоддзі стала галоўным асяродкам сельскагаспадарчай каланізацыі выхадцаў з Заходняй Беларусі. У знакамітым Парку нацыянальнасцей у Обэры, дзе праходзіць маштабны Нацыянальны фестываль імігрантаў (Fiesta Nacional del Inmigrante), пабудаваны аўтэнтычны драўляны Дом-музей супольнасці (Casa de la Colectividad). У яго экспазіцыі дзейнічае пастаянная выстава беларускіх ручнікоў, ткацтва, народных касцюмаў і ўсталяваны скульптурны бюст класіка беларускай літаратуры Янкі Купалы.",
                "ru": "Parque de las Naciones, Обера, провинция Мисьонес. Северо-восточная провинция Мисьонес — исторический центр расселения белорусских крестьян-эмигрантов 1920–30-х гг. В Парке национальностей действует аутентичный Дом-музей общины с экспозицией белорусских рушников, костюмов и бюстом Янки Купалы.",
                "en": "Parque de las Naciones, Oberá, Misiones Province. The subtropical province of Misiones was a primary destination for interwar Belarusian agricultural settlers. The local community house in the Park of Nations features an authentic museum exhibition of Belarusian embroidered rushniks, folk costumes, and a bronze bust of national poet Yanka Kupala."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/DJI_Mini_3_-_Argentina_-_Misiones_-_Ober%C3%A1_-_Parque_de_las_Naciones_%281%29.jpg/800px-DJI_Mini_3_-_Argentina_-_Misiones_-_Ober%C3%A1_-_Parque_de_las_Naciones_%281%29.jpg",
            "links": [
                {"title": "Беларусы ў Аргенціне (be.wikipedia)", "url": "https://be.wikipedia.org/wiki/Беларусы_ў_Аргенціне"}
            ],
            "tags": ["Аргенціна", "Місьёнес", "Обэра", "Купала", "музей", "дыяспара"],
            "personIds": ["yanka-kupala"],
            "mustSee": True
        },
        {
            "id": "comodoro-rivadavia-belarusian-workers-community",
            "title": {
                "by": "Асяродак беларускіх нафтавікоў і музычны ансамбль у Камадора-Рывадавіі",
                "ru": "Очаг белорусских нефтяников и музыкальный ансамбль в Комодоро-Ривадавии",
                "en": "Belarusian Oilfield Workers Community & Ensemble in Comodoro Rivadavia"
            },
            "category": "historical",
            "country": {"by": "Аргенціна", "ru": "Аргентина", "en": "Argentina"},
            "city": {"by": "Камадора-Рывадавія", "ru": "Комодоро-Ривадавия", "en": "Comodoro Rivadavia"},
            "coordinates": [-45.864700, -67.496600],
            "description": {
                "by": "Камадора-Рывадавія (Comodoro Rivadavia), правінцыя Чубут, Патагонія, Аргенціна.\n\nУ міжваенныя 1920–1930-я гады тысячы незаможных выхадцаў з Заходняй Беларусі выпраўляліся на самы поўдзень Аргенціны — у суровую патагонскую правінцыю Чубут. Яны працавалі на нафтавых промыслах дзяржаўнай карпарацыі YPF і будаўніцтве чыгунак. Нягледзячы на цяжкія ўмовы працы, беларускія рабочыя захавалі сваю нацыянальную культуру і мову: у 1930-я гады тут дзейнічаў згуртаваны Музычны ансамбль беларускіх рабочых (Conjunto musical de obreros bielorrusos en Comodoro Rivadavia), фатаграфія якога захавалася як яскравы дакумент беларускай працоўнай эміграцыі ў Паўднёвай Амерыцы.",
                "ru": "Комодоро-Ривадавия, провинция Чубут, Патагония. В 1920–30-х гг. тысячи уроженцев Западной Беларуси трудились на нефтяных промыслах Патагонии. Здесь сложилась сплоченная белорусская рабочая община и действовал известный музыкальный ансамбль белорусских рабочих (ок. 1930 г.).",
                "en": "Comodoro Rivadavia, Chubut Province, Patagonia. Thousands of interwar immigrants from Western Belarus worked in the harsh Patagonian oilfields for YPF. Despite extreme hardships, they maintained their cultural identity, forming a well-known Belarusian workers' musical ensemble around 1930."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Conjunto_musical_de_obreros_bielorrusos_en_Comodoro_Rivadavia_ca.1930.jpg/800px-Conjunto_musical_de_obreros_bielorrusos_en_Comodoro_Rivadavia_ca.1930.jpg",
            "links": [
                {"title": "Беларусы ў Аргенціне (be.wikipedia)", "url": "https://be.wikipedia.org/wiki/Беларусы_ў_Аргенціне"},
                {"title": "Наша Ніва: Беларусы ў Аргенціне", "url": "https://nashaniva.com/34598"}
            ],
            "tags": ["Аргенціна", "Патагонія", "Камадора-Рывадавія", "працоўная эміграцыя", "гісторыя"],
            "personIds": []
        },
        {
            "id": "buenos-aires-zhurtavannie-belarusau-arhentine-merlyak",
            "title": {
                "by": "Згуртаванне беларусаў у Аргенціне і прадстаўніцтва Рады БНР (Кастусь Мерляк)",
                "ru": "Объединение белорусов в Аргентине и представительство Рады БНР (Константин Мерляк)",
                "en": "Association of Belarusians in Argentina & Rada BNR Mission (Kastus Merlyak)"
            },
            "category": "historical",
            "country": {"by": "Аргенціна", "ru": "Аргентина", "en": "Argentina"},
            "city": {"by": "Буэнас-Айрэс", "ru": "Буэнос-Айрес", "en": "Buenos Aires"},
            "coordinates": [-34.603700, -58.381600],
            "description": {
                "by": "Буэнас-Айрэс, Аргенціна.\n\nПасля Другой сусветнай вайны ў Буэнас-Айрэсе сфармаваўся палітычны асяродак беларускай незалежніцкай эміграцыі. У снежні 1947 года сюды прыбыў Кастусь Мерляк, які ў 1948 годзе стаў ініцыятарам стварэння і старшынёй Згуртавання беларусаў у Аргенціне (ЗБА) і адначасова ўзначаліў прадстаўніцтва Рады Беларускай Народнай Рэспублікі (Рады БНР). ЗБА выдавала інфармацыйныя матэрыялы беларускай лацінкай («Infarmacyjny Biuleten», «Kamunikat»), адстойвала нацыянальныя інтарэсы беларусаў і пашырала праўду пра бальшавіцкія рэпрэсіі ў Беларусі.",
                "ru": "Буэнос-Айрес, Аргентина. В 1948 г. здесь было создано Объединение белорусов в Аргентине (ЗБА) под руководством Константина Мерляка, одновременно возглавившего южноамериканское представительство Рады БНР. ЗБА издавало бюллетени на белорусской латинке и объединяло послевоенных эмигрантов.",
                "en": "Buenos Aires, Argentina. In 1948, post-WWII political emigrants established the Association of Belarusians in Argentina (ZBA), led by Kastus Merlyak, who also headed the South American representation of Rada BNR. ZBA published periodicals in Belarusian Latin script ('Infarmacyjny Biuleten', 'Kamunikat') and championed Belarusian independence."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Kal_arg_bel.JPG/800px-Kal_arg_bel.JPG",
            "links": [
                {"title": "Беларусы ў Аргенціне (be.wikipedia)", "url": "https://be.wikipedia.org/wiki/Беларусы_ў_Аргенціне"},
                {"title": "Кастусь Мерляк (be.wikipedia)", "url": "https://be.wikipedia.org/wiki/Кастусь_Мерляк"}
            ],
            "tags": ["Аргенціна", "Буэнас-Айрэс", "БНР", "Мерляк", "дыяспара", "гісторыя"],
            "personIds": ["kastus-merlyak"]
        },
        {
            "id": "buenos-aires-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў Аргенціне (Буэнас-Айрэс)",
                "ru": "Посольство Беларуси в Аргентине (Буэнос-Айрес)",
                "en": "Embassy of Belarus in Argentina (Buenos Aires)"
            },
            "category": "embassy",
            "country": {"by": "Аргенціна", "ru": "Аргентина", "en": "Argentina"},
            "city": {"by": "Буэнас-Айрэс", "ru": "Буэнос-Айрес", "en": "Buenos Aires"},
            "coordinates": [-34.553657, -58.444099],
            "description": {
                "by": "Адрас: Cazadores 2166, C1428AQH Ciudad Autónoma de Buenos Aires (раён Бельграна / Belgrano).\n\nДыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Аргенцінскай Рэспубліцы, заснаванае ў 2000 годзе. Пасольства прадстаўляе інтарэсы Беларусі таксама ў суседніх краінах Паўднёвай Амерыкі — Уругваі, Чылі і Парагваі.",
                "ru": "Cazadores 2166, Буэнос-Айрес (район Бельграно). Посольство Республики Беларусь в Аргентинской Республике (открыто в 2000 г.). Представляет интересы Беларуси также в Уругвае, Чили и Парагвае.",
                "en": "Cazadores 2166, Buenos Aires (Belgrano neighborhood). Official diplomatic mission of Belarus in the Argentine Republic, established in 2000. Also represents Belarus in Uruguay, Chile, and Paraguay."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Colectividad_Bielorrusa_de_Argentina.jpg/800px-Colectividad_Bielorrusa_de_Argentina.jpg",
            "links": [
                {"title": "Посольство Республики Беларусь в Аргентинской Республике", "url": "https://argentina.mfa.gov.by"}
            ],
            "tags": ["Аргенціна", "Буэнас-Айрэс", "пасольства", "embassy", "дыпламатыя"],
            "personIds": []
        },
        {
            "id": "brasilia-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў Бразіліі (Бразіліа)",
                "ru": "Посольство Беларуси в Бразилии (Бразилиа)",
                "en": "Embassy of Belarus in Brazil (Brasília)"
            },
            "category": "embassy",
            "country": {"by": "Бразілія", "ru": "Бразилия", "en": "Brazil"},
            "city": {"by": "Бразіліа", "ru": "Бразилиа", "en": "Brasília"},
            "coordinates": [-15.857645, -47.867184],
            "description": {
                "by": "Адрас: SHIS QL 18, Conjunto 01, Casa 17 - Lago Sul, Brasília - DF, 71650-015, Бразілія.\n\nДыпламатычная місія Рэспублікі Беларусь у Федэратыўнай Рэспубліцы Бразілія, адкрытая ў 2010 годзе. Размешчана ў прэстыжным дыпламатычным сектары Лага-Сул федэральнай сталіцы Бразіліа.",
                "ru": "SHIS QL 18, Conjunto 01, Casa 17 - Lago Sul, Бразилиа. Посольство Республики Беларусь в Федеративной Республике Бразилия, открытое в 2010 году.",
                "en": "SHIS QL 18, Conjunto 01, Casa 17 - Lago Sul, Brasília. Diplomatic mission of the Republic of Belarus to the Federative Republic of Brazil, established in 2010 in the capital's Lago Sul diplomatic zone."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Colectividad_Bielorrusa_de_Argentina.jpg/800px-Colectividad_Bielorrusa_de_Argentina.jpg",
            "links": [
                {"title": "Посольство Республики Беларусь в Федеративной Республике Бразилия", "url": "https://brazil.mfa.gov.by"}
            ],
            "tags": ["Бразілія", "Бразіліа", "пасольства", "embassy", "дыпламатыя"],
            "personIds": []
        },
        {
            "id": "brazil-belarusian-diaspora-peoples-embassy",
            "title": {
                "by": "Народная амбасада Беларусі і беларуская супольнасць у Бразіліі",
                "ru": "Народное посольство Беларуси и белорусская община в Бразилии",
                "en": "People's Embassy of Belarus & Belarusian Community in Brazil"
            },
            "category": "culture",
            "country": {"by": "Бразілія", "ru": "Бразилия", "en": "Brazil"},
            "city": {"by": "Сан-Паўлу", "ru": "Сан-Паулу", "en": "São Paulo"},
            "coordinates": [-23.550520, -46.633308],
            "description": {
                "by": "Сан-Паўлу / Бразіліа, Федэратыўная Рэспубліка Бразілія.\n\nАсяродак беларускай дыяспары і Народнай амбасады Беларусі ў Бразіліі (Embaixada Popular de Belarus no Brasil), заснаваны ў снежні 2020 года. Прадстаўніца — грамадская дзяячка і даследчыца Вольга Ермалаева Франко. Беларуская грамада займаецца культурнай дыпламатыяй: арганізацыяй імпрэз, прасоўваннем беларускай паэзіі і літаратуры, перакладамі беларускіх класікаў і сучасных аўтараў на партугальскую мову, а таксама салідарнасцю і ўзаемадапамогай суайчыннікаў у Бразіліі.",
                "ru": "Сан-Паулу / Бразилиа, Бразилия. Центр белорусской диаспоры и Народного посольства Беларуси в Бразилии (представитель — Ольга Ермолаева Франко). Основное внимание уделяется культурной дипломатии: популяризации белорусской литературы, переводам на португальский язык, адаптации и поддержке соотечественников.",
                "en": "São Paulo / Brasília, Brazil. Hub of the Belarusian diaspora and the People's Embassy of Belarus in Brazil (represented by civic activist Olga Ermolaeva Franco). Engaged in cultural diplomacy: organizing literary events, translating Belarusian literature and poetry into Portuguese, and supporting newcomers across Brazil."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Colectividad_bielorrusa%2C_rusa_y_ucraniana_-_Dia_del_Inmigrante_en_el_Planetario_Galileo_Galilei.jpg/800px-Colectividad_bielorrusa%2C_rusa_y_ucraniana_-_Dia_del_Inmigrante_en_el_Planetario_Galileo_Galilei.jpg",
            "links": [
                {"title": "Радыё Рацыя: Чым жыве беларуская дыяспара ў Бразіліі?", "url": "https://racyja.com/by/hramadstva/cym-zyve-belaruskaja-dyjaspara-u-brazilii/"},
                {"title": "Народныя амбасады Беларусі", "url": "https://belarusabroad.org"}
            ],
            "tags": ["Бразілія", "Сан-Паўлу", "дыяспара", "Народная амбасада", "культура"],
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

    # Save JSON and JS
    with open('data/places.json', 'w', encoding='utf-8') as f:
        json.dump(places, f, ensure_ascii=False, indent=2)
    with open('data/places.js', 'w', encoding='utf-8') as f:
        f.write('window.INITIAL_PLACES = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

    with open('data/persons.json', 'w', encoding='utf-8') as f:
        json.dump(persons, f, ensure_ascii=False, indent=2)
    with open('data/persons.js', 'w', encoding='utf-8') as f:
        f.write('window.INITIAL_PERSONS = ' + json.dumps(persons, ensure_ascii=False, indent=2) + ';\n')

    print("Updated data/places.json, data/places.js, data/persons.json, data/persons.js")

if __name__ == '__main__':
    main()
