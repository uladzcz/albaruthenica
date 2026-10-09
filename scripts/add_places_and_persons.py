# -*- coding: utf-8 -*-
"""
Populate and synchronize all new persons and places in Albaruthenica.
"""

import json

def run():
    with open('data/persons.json', 'r', encoding='utf-8') as f:
        persons = json.load(f)

    with open('data/places.json', 'r', encoding='utf-8') as f:
        places = json.load(f)

    existing_person_ids = {p['id'] for p in persons}
    existing_place_ids = {p['id'] for p in places}

    # 1. New Persons
    new_persons = [
        {
            "id": "klaudziy-duzh-dusheuski",
            "name": {
                "by": "Клаўдзій Дуж-Душэўскі",
                "ru": "Клавдий Дуж-Душевский",
                "en": "Klaudziy Duzh-Dusheuski"
            },
            "dates": "1891–1959",
            "role": {
                "by": "Аўтар бел-чырвона-белага сцяга, архітэктар, дыпламат БНР, Праведнік народаў свету",
                "ru": "Создатель бело-красно-белого флага, архитектор, дипломат БНР, Праведник народов мира",
                "en": "Creator of the White-Red-White Flag, architect, BNR diplomat, Righteous Among the Nations"
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/1/11/K%C5%82a%C5%ADdzi_Du%C5%BE-Du%C5%A1e%C5%ADski._%D0%9A%D0%BB%D0%B0%D1%9E%D0%B4%D0%B7%D1%96_%D0%94%D1%83%D0%B6-%D0%94%D1%83%D1%88%D1%8D%D1%9E%D1%81%D0%BA%D1%96_%281920-29%29.jpg",
            "bio": {
                "by": "Ураджэнец Глыбокага. Стваральнік эскіза нацыянальнага бел-чырвона-белага сцяга (1917 г.). Дыпламатычны прадстаўнік БНР у краінах Балтыі, сакратар урада БНР у Коўне. Выдатны архітэктар міжваеннай Літвы, чые мадэрнісцкія будынкі ў Каўнасе ўключаны ў спіс Сусветнай спадчыны ЮНЕСКА. У гады Другой сусветнай вайны ратаваў габрэйскіх дзяцей з гета, за што прызнаны Праведнікам народаў свету. Пахаваны ў Каўнасе на Пятрашунскіх могілках.",
                "ru": "Уроженец Глубокого. Создатель эскиза национального бело-красно-белого флага (1917). Дипломат БНР, архитектор каунасского модернизма (ЮНЕСКО). В годы нацистской оккупации спасал еврейских детей, признан Праведником народов мира. Похоронен на Петрашюнском кладбище в Каунасе.",
                "en": "Born in Hlybokaye. Designer of the Belarusian national White-Red-White flag (1917), BNR diplomat, prominent architect of Kaunas interwar modernism (UNESCO). Recognized as Righteous Among the Nations for saving Jewish children during the Holocaust. Buried at Petrašiūnai Cemetery in Kaunas."
            },
            "placeIds": [
                "kaunas-petrasiunai-duzh-dusheuski-grave",
                "kaunas-vytautas-8-duzh-dusheuski-house"
            ],
            "wiki": "https://be.wikipedia.org/wiki/Клаўдзій_Сцяпанавіч_Дуж-Душэўскі"
        },
        {
            "id": "anton-lutskevich",
            "name": {
                "by": "Антон Луцкевіч",
                "ru": "Антон Луцкевич",
                "en": "Anton Lutskevich"
            },
            "dates": "1884–1942",
            "role": {
                "by": "Старшыня Рады Народных Міністраў БНР, гісторык, публіцыст, заснавальнік Беларускага музея ў Вільні",
                "ru": "Председатель Рады Народных Министров БНР, историк, основатель Белорусского музея в Вильно",
                "en": "Prime Minister of the Belarusian Democratic Republic (BNR), historian, founder of the Belarusian Museum in Vilnius"
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Anton_Luckievi%C4%8D._%D0%90%D0%BD%D1%82%D0%BE%D0%BD_%D0%9B%D1%83%D1%86%D0%BA%D0%B5%D0%B2%D1%96%D1%87_%281918%29_%282%29.jpg/960px-Anton_Luckievi%C4%8D._%D0%90%D0%BD%D1%82%D0%BE%D0%BD_%D0%9B%D1%83%D1%86%D0%BA%D0%B5%D0%B2%D1%96%D1%87_%281918%29_%282%29.jpg",
            "bio": {
                "by": "Адзін з галоўных айцоў-заснавальнікаў БНР, прэм'ер-міністр і міністр замежных спраў БНР (1918–1919 гг.), лідар Беларускай сацыялістычнай грамады, рэдактар «Нашай Нівы», дырэктар Беларускага музея імя Івана Луцкевіча ў Вільні.",
                "ru": "Один из отцов-основателей БНР, премьер-министр и министр иностранных дел БНР, редактор газеты «Наша Ніва», директор Белорусского музея в Вильнюсе.",
                "en": "Leading founding father and Prime Minister of the Belarusian Democratic Republic (BNR), editor of 'Nasha Niva', and director of the Belarusian Museum in Vilnius."
            },
            "placeIds": [
                "vilnius-vilniaus-29-nasha-niva",
                "kaunas-vytautas-8-duzh-dusheuski-house"
            ],
            "wiki": "https://be.wikipedia.org/wiki/Антон_Іванавіч_Луцкевіч"
        },
        {
            "id": "vasil-zaharka",
            "name": {
                "by": "Васіль Захарка",
                "ru": "Василий Захарко",
                "en": "Vasil Zaharka"
            },
            "dates": "1877–1943",
            "role": {
                "by": "Старшыня (Прэзідэнт) Рады БНР у Празе (1928–1943)",
                "ru": "Председатель (Президент) Рады БНР в Праге (1928–1943)",
                "en": "President of the Rada of the Belarusian Democratic Republic in Prague (1928–1943)"
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Vasil_Zacharka._%D0%92%D0%B0%D1%81%D1%96%D0%BB%D1%8C_%D0%97%D0%B0%D1%85%D0%B0%D1%80%D0%BA%D0%B0_%281919-20%29.jpg/960px-Vasil_Zacharka._%D0%92%D0%B0%D1%81%D1%96%D0%BB%D1%8C_%D0%97%D0%B0%D1%85%D0%B0%D1%80%D0%BA%D0%B0_%281919-20%29.jpg",
            "bio": {
                "by": "Дзяржаўны і палітычны дзеяч БНР, намеснік старшыні Рады БНР, з 1928 года — Старшыня Рады БНР. Жыў у эміграцыі ў Чэхаславакіі, захаваў архівы і пераемнасць урада БНР, катэгарычна адмовіўся супрацоўнічаць з нацыстамі падчас акупацыі Прагі. Пахаваны на Ольшанскіх могілках.",
                "ru": "Государственный деятель БНР, председатель Рады БНР с 1928 г. Жил в Праге, сохранил государственные архивы БНР, отверг сотрудничество с нацистами. Похоронен на Ольшанском кладбище в Праге.",
                "en": "Statesman and President of the Rada BNR in exile from 1928 until 1943. Preserved the state archives of the BNR in Prague and refused any collaboration with the Nazi occupation regime. Buried at Olšany Cemetery in Prague."
            },
            "placeIds": [
                "prague-olsany-belarusian-pantheon"
            ],
            "wiki": "https://be.wikipedia.org/wiki/Васіль_Іванавіч_Захарка"
        },
        {
            "id": "ciotka",
            "name": {
                "by": "Цётка (Алаіза Пашкевіч)",
                "ru": "Тётка (Алоиза Пашкевич)",
                "en": "Ciotka (Ałaiza Paškievič)"
            },
            "dates": "1876–1916",
            "role": {
                "by": "Паэтэса, публіцыстка, асветніца, дзяячка Беларускай сацыялістычнай грамады",
                "ru": "Поэтесса, публицистка, просветительница, деятельница БСГ",
                "en": "Pioneering Belarusian poet, essayist, and national renaissance leader"
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/A%C5%82aiza_Pa%C5%A1kievi%C4%8D_%28Ciotka%29._%D0%90%D0%BB%D0%B0%D1%96%D0%B7%D0%B0_%D0%9F%D0%B0%D1%88%D0%BA%D0%B5%D0%B2%D1%96%D1%87_%28%D0%A6%D1%8F%D1%82%D0%BA%D0%B0%29_%281900-16%29.jpg/960px-A%C5%82aiza_Pa%C5%A1kievi%C4%8D_%28Ciotka%29._%D0%90%D0%BB%D0%B0%D1%96%D0%B7%D0%B0_%D0%9F%D0%B0%D1%88%D0%BA%D0%B5%D0%B2%D1%96%D1%87_%28%D0%A6%D1%8F%D1%82%D0%BA%D0%B0%29_%281900-16%29.jpg",
            "bio": {
                "by": "Адна з заснавальніц новай беларускай літаратуры, аўтарка зборнікаў «Хрэст на душу» і «Скрыпка беларуская», выдаваных у Львове і Кракаве. Вывучала філасофію ў Ягелонскім універсітэце ў Кракаве і Львоўскім універсітэце, стварала беларускія чытанкі для дзяцей.",
                "ru": "Одна из основоположниц современной белорусской литературы, автор поэтических сборников, изданных в Кракове и Львове. Училась в Ягеллонском и Львовском университетах.",
                "en": "Founding mother of modern Belarusian literature and revolutionary leader. Studied at the Jagiellonian University in Kraków and Lviv University; published seminal poetry collections 'Chrest na dušu' and 'Skrypka biełaruskaja'."
            },
            "placeIds": [
                "krakow-jagiellonian-ciotka"
            ],
            "wiki": "https://be.wikipedia.org/wiki/Алаіза_Сцяпанаўна_Пашкевіч"
        },
        {
            "id": "maksim-haretski",
            "name": {
                "by": "Максім Гарэцкі",
                "ru": "Максим Горецкий",
                "en": "Maksim Haretski"
            },
            "dates": "1893–1938",
            "role": {
                "by": "Класік беларускай літаратуры, навуковец-літаратуразнаўца, фалькларыст",
                "ru": "Классик белорусской литературы, литературовед, фольклорист",
                "en": "Classic Belarusian writer, literary scholar, and national revival figure"
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Maksim_Harecki._%D0%9C%D0%B0%D0%BA%D1%81%D1%96%D0%BC_%D0%93%D0%B0%D1%80%D1%8D%D1%86%D0%BA%D1%96_%281920%29.jpg/960px-Maksim_Harecki._%D0%9C%D0%B0%D0%BA%D1%81%D1%96%D0%BC_%D0%93%D0%B0%D1%80%D1%8D%D1%86%D0%BA%D1%96_%281920%29.jpg",
            "bio": {
                "by": "Выбітны празаік («Ціхія песні», «Рунь», «Дзве душы», «На імперыялістычнай вайне»), аўтар першай «Гісторыі беларускае літаратуры». Працаваў у Вільні, Менску і Горках. Рэпрэсаваны савецкімі ўладамі, расстраляны ў Вязьме ў лютым 1938 года.",
                "ru": "Выдающийся прозаик, автор фундаментальной «Истории белорусской литературы». Репрессирован и расстрелян в Вязьме в 1938 году.",
                "en": "Renowned Belarusian novelist and author of the first comprehensive 'History of Belarusian Literature'. Repressed by the Soviet regime and executed in Vyazma in 1938."
            },
            "placeIds": [
                "vyazma-haretski-memorial"
            ],
            "wiki": "https://be.wikipedia.org/wiki/Максім_Іванавіч_Гарэцкі"
        }
    ]

    for p in new_persons:
        if p['id'] not in existing_person_ids:
            persons.append(p)
            existing_person_ids.add(p['id'])
            print(f"Added person {p['id']}")

    # Update existing persons' placeIds
    person_updates = {
        "maksim-bahdanovich": ["yalta-bahdanovich-grave", "yaroslavl-bahdanovich-museum", "koreiz-bahdanovich-monument"],
        "pyotra-krecheuski": ["prague-olsany-belarusian-pantheon"],
        "yanka-kupala": ["pechishchi-kupala-museum", "moscow-hotel-moskva-kupala"],
        "yakub-kolas": ["tashkent-kolas-monument-museum"],
        "ivan-lutskevich": ["zakopane-luczkiewicz-sanatorium"],
        "vaclau-lastouski": ["kaunas-lastouski-bnr-government"],
        "mikhas-zabejda-sumitski": ["prague-olsany-belarusian-pantheon"],
        "marc-chagall": [
            "reims-cathedral-chagall-stained-glass",
            "paris-opera-garnier-chagall-ceiling",
            "metz-cathedral-chagall-stained-glass",
            "jerusalem-hadassah-chagall-windows",
            "jerusalem-knesset-chagall-hall",
            "mainz-sankt-stephan-chagall-windows",
            "tudeley-all-saints-chagall-windows",
            "chicago-art-institute-chagall-windows",
            "new-york-met-opera-chagall-murals",
            "saint-paul-de-vence-chagall-grave",
            "amsterdam-stedelijk-chagall",
            "basel-kunstmuseum-chagall"
        ]
    }

    for pers in persons:
        pid = pers['id']
        if pid in person_updates:
            cur_places = set(pers.get('placeIds', []))
            for new_pl in person_updates[pid]:
                cur_places.add(new_pl)
            pers['placeIds'] = sorted(list(cur_places))

    # 2. Recategorize existing historical diplomatic missions into 'embassy'
    embassy_recat = {
        "un-mission-new-york",
        "berlin-bnr-diplomatic-mission",
        "tbilisi-unr-bnr-mission",
        "basel-munster-vkl-embassy"
    }
    for pl in places:
        if pl['id'] in embassy_recat:
            pl['category'] = 'embassy'
            print(f"Recategorized {pl['id']} as embassy")

    # 3. New Places to Add
    new_places = [
        # --- Timber Heritage (Nasha Niva 378830) ---
        {
            "id": "lytham-hall-belarusian-timber",
            "title": {
                "by": "Сядзіба Лайтам-хол (палац з беларускага лесу)",
                "ru": "Усадьба Лайтэм-холл (дворец из белорусского леса)",
                "en": "Lytham Hall (Constructed with Belarusian Timber)"
            },
            "category": "historical",
            "country": {
                "by": "Вялікабрытанія",
                "ru": "Великобритания",
                "en": "United Kingdom"
            },
            "city": {
                "by": "Лайтам-Сент-Анс",
                "ru": "Лайтэм-Сент-Анс",
                "en": "Lytham St Annes"
            },
            "coordinates": [53.7428, -2.9818],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Lytham_Hall_01.jpg/960px-Lytham_Hall_01.jpg",
            "wiki": "https://en.wikipedia.org/wiki/Lytham_Hall",
            "source": "https://nashaniva.com/378830",
            "description": {
                "by": "Велічны ангельскі палац XVIII ст. у Ланкашыры, помнік вышэйшай катэгорыі (Grade I). Дэндрахраналагічныя даследаванні навукоўцаў (М. Ермахін, М. Зундэ, часопіс «Dendrochronologia») пацвердзілі, што драўляныя канструкцыі і кроквы палаца збудаваны з беларускай хвоі («рыжскай хвоі»), сплаўленай па Дзвіне і Дняпры.",
                "ru": "Величественный английский особняк XVIII в. в Ланкашире (Grade I). Дендрохронологические исследования ученых подтвердили, что несущие конструкции возведены из белорусской сосны («рижской сосны»), сплавленной по Двине.",
                "en": "Georgian country house in Lancashire (Grade I). Dendrochronological research confirmed that its roof timbers were built using 18th-century Belarusian pine ('Riga pine') shipped down the Dzvina and Dnieper rivers."
            },
            "tags": ["спадчына", "эканоміка", "архітэктура", "вкл", "вялікабрытанія"]
        },
        {
            "id": "danson-house-belarusian-timber",
            "title": {
                "by": "Сядзіба Дэнсан-хаўс (палац з беларускага лесу)",
                "ru": "Усадьба Дэнсон-хаус (дворец из белорусского леса)",
                "en": "Danson House (Constructed with Belarusian Timber)"
            },
            "category": "historical",
            "country": {
                "by": "Вялікабрытанія",
                "ru": "Великобритания",
                "en": "United Kingdom"
            },
            "city": {
                "by": "Лондан",
                "ru": "Лондон",
                "en": "London"
            },
            "coordinates": [51.4552, 0.1293],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Danson_Mansion.jpg/960px-Danson_Mansion.jpg",
            "wiki": "https://en.wikipedia.org/wiki/Danson_House",
            "source": "https://nashaniva.com/378830",
            "description": {
                "by": "Шэдэўр паладыянскай архітэктуры ў Вялікім Лондане (Grade I), узведзены сэрам Робертам Тэйларам у 1766 г. Дэндрахраналагічны аналіз даказаў, што перакрыцці і бэлькі маёнтка выкананы з высакаякаснай беларускай драўніны эпохі Рэчы Паспалітай.",
                "ru": "Шедевр палладианской архитектуры в Большом Лондоне (Grade I), построенный в 1766 г. Дендрохронологический анализ доказал, что балки и перекрытия выполнены из белорусского леса.",
                "en": "Grade I listed Palladian mansion in Bexley, London, built in 1766 by Sir Robert Taylor. Dendrochronology established that its structural roof timbers came from historical Belarusian forests."
            },
            "tags": ["спадчына", "эканоміка", "лондан", "архітэктура", "вялікабрытанія"]
        },
        {
            "id": "riga-dannenstern-house-timber",
            "title": {
                "by": "Камяніца Данэнштэрна (лес з маёнткаў Чартарыйскіх)",
                "ru": "Дом Данненштерна (лес из имений Чарторыйских)",
                "en": "Dannenstern House (Timber from Czartoryski Belarusian Estates)"
            },
            "category": "historical",
            "country": {
                "by": "Латвія",
                "ru": "Латвия",
                "en": "Latvia"
            },
            "city": {
                "by": "Рыга",
                "ru": "Рига",
                "en": "Riga"
            },
            "coordinates": [56.9452, 24.1086],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Dannensternhaus_Riga.JPG/960px-Dannensternhaus_Riga.JPG",
            "wiki": "https://en.wikipedia.org/wiki/Dannenstern_House",
            "source": "https://nashaniva.com/378830",
            "description": {
                "by": "Знакаміты барочны будынак XVII ст. у Старой Рызе (вул. Марсталю, 21), узведзены багатым гандляром Эрнстам Метсу фон Данэнштэрнам. Навуковы аналіз драўніны выявіў, што яна паходзіць з беларускіх маёнткаў князёў Чартарыйскіх і сплаўлялася па Заходняй Дзвіне.",
                "ru": "Знаменитый барочный дом XVII века в Старой Риге (ул. Марсталю, 21). Исследование подтвердило, что несущие бревна доставлены из белорусских имений князей Чарторыйских сплавом по Западной Двине.",
                "en": "Prominent 17th-century baroque merchant house in Old Riga. Dendrochronological dating proved that its massive timbers originated from the Belarusian estates of the Czartoryski princes."
            },
            "tags": ["рыга", "латвія", "гандаль", "дзвіна", "чартарыйскія"]
        },

        # --- Marc Chagall Catalogue Raisonné & Monumental Sites (Nasha Niva 399979 & marcchagall.com) ---
        {
            "id": "reims-cathedral-chagall-stained-glass",
            "title": {
                "by": "Рэймскі сабор — вітражы Марка Шагала",
                "ru": "Реймсский собор — витражи Марка Шагала",
                "en": "Reims Cathedral — Marc Chagall Stained Glass Windows"
            },
            "category": "church",
            "mustSee": True,
            "country": {
                "by": "Францыя",
                "ru": "Франция",
                "en": "France"
            },
            "city": {
                "by": "Рэймс",
                "ru": "Реймс",
                "en": "Reims"
            },
            "coordinates": [49.2537, 4.0340],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Reims_-_Cath%C3%A9drale_Notre-Dame%2C_int%C3%A9rieur%2C_vitraux_de_Marc_Chagall_%284%29.jpg/960px-Reims_-_Cath%C3%A9drale_Notre-Dame%2C_int%C3%A9rieur%2C_vitraux_de_Marc_Chagall_%284%29.jpg",
            "wiki": "https://fr.wikipedia.org/wiki/Cath%C3%A9drale_Notre-Dame_de_Reims",
            "source": "https://nashaniva.com/399979",
            "personIds": ["marc-chagall"],
            "description": {
                "by": "Славутыя вітражы Марка Шагала ў вокнах восевай капліцы Рэймскага сабора (1974 г.), створаныя разам з рэймскімі майстрамі Шарлем Маркам і Брыжыт Сімон з аднаўленнем сярэднявечных тэхналогій XIII ст. Трохаконная кампазіцыя з непаўторным шагалаўскім сінім колерам спалучае біблейскую гісторыю (Аўраам, Дрэва Есея) і гісторыю каралёў Францыі.",
                "ru": "Знаменитые витражи Марка Шагала в центральной капелле Реймсского собора (1974 г.), созданные в сотрудничестве с мастерами Симон-Марк с возрождением средневекового синего стекла XIII века.",
                "en": "Masterpiece stained glass windows designed by Marc Chagall in the axial chapel of Reims Cathedral (1974), featuring the iconic 'Chagall blue' glass created in collaboration with the historic Simon-Marq workshop."
            },
            "tags": ["шагал", "вітражы", "рэймс", "юнеска", "мастацтва"]
        },
        {
            "id": "paris-opera-garnier-chagall-ceiling",
            "title": {
                "by": "Опера Гарнье — плафон Марка Шагала",
                "ru": "Опера Гарнье — плафон Марка Шагала",
                "en": "Palais Garnier (Paris Opera) — Marc Chagall Ceiling"
            },
            "category": "culture",
            "mustSee": True,
            "country": {
                "by": "Францыя",
                "ru": "Франция",
                "en": "France"
            },
            "city": {
                "by": "Парыж",
                "ru": "Париж",
                "en": "Paris"
            },
            "coordinates": [48.8719, 2.3316],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Plafond_Chagall_Garnier.jpg/960px-Plafond_Chagall_Garnier.jpg",
            "wiki": "https://fr.wikipedia.org/wiki/Op%C3%A9ra_Garnier",
            "personIds": ["marc-chagall"],
            "description": {
                "by": "Манументальны роспіс столі парыжскай Оперы Гарнье плошчай 220 кв. метраў, замоўлены міністрам культуры Андрэ Мальро і створаны Шагалам у 1964 годзе. Плафон прысвечаны 14 выдатным кампазітарам (Моцарт, Вагнер, Чайкоўскі, Равель, Стравінскі) і з'яўляецца сусветнай візітоўкай Парыжа.",
                "ru": "Монументальный потолочный плафон Парижской оперы площадью 220 кв. м, созданный Марком Шагалом в 1964 г. по заказу Андре Мальро. Посвящен 14 композиторам.",
                "en": "The iconic 220 sq.m painted ceiling of the Palais Garnier auditorium, commissioned by André Malraux and painted by Marc Chagall in 1964 as a tribute to 14 great composers."
            },
            "tags": ["шагал", "парыж", "опера", "мастацтва", "плафон"]
        },
        {
            "id": "metz-cathedral-chagall-stained-glass",
            "title": {
                "by": "Сабор Святога Стэфана ў Мецы — вітражы Марка Шагала",
                "ru": "Собор Святого Стефана в Меце — витражи Марка Шагала",
                "en": "Metz Cathedral — Marc Chagall Stained Glass"
            },
            "category": "church",
            "country": {
                "by": "Францыя",
                "ru": "Франция",
                "en": "France"
            },
            "city": {
                "by": "Мец",
                "ru": "Мец",
                "en": "Metz"
            },
            "coordinates": [49.1202, 6.1755],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Metz_cathedrale_chagall_01.JPG/960px-Metz_cathedrale_chagall_01.JPG",
            "wiki": "https://en.wikipedia.org/wiki/Metz_Cathedral",
            "personIds": ["marc-chagall"],
            "description": {
                "by": "Гатычны сабор у Мецы («Ліхтар Гасподні») змяшчае больш за 40 кв. метраў вітражоў Шагала (1960–1968 гг.) з біблейскімі сюжэтамі (Стварэнне свету, Сон Якава, Майсей, Цар Давід), якія напаўняюць храм містычным сінім і жоўтым святлом.",
                "ru": "Готический собор Меца с витражами Шагала (1960–1968 гг.) на библейские темы, наполняющими неф мистическим сиянием.",
                "en": "Famed stained glass windows in Metz Cathedral created by Chagall between 1960 and 1968 depicting Genesis, Exodus, and prophetic visions."
            },
            "tags": ["шагал", "мец", "вітражы", "готыка"]
        },
        {
            "id": "jerusalem-hadassah-chagall-windows",
            "title": {
                "by": "Сінагога шпіталя Хадаса ў Ерусаліме — 12 вітражоў Шагала",
                "ru": "Синагога больницы Хадасса в Иерусалиме — 12 витражей Шагала",
                "en": "Hadassah Hospital Synagogue — Chagall's Twelve Tribes Windows"
            },
            "category": "church",
            "mustSee": True,
            "country": {
                "by": "Ізраіль",
                "ru": "Израиль",
                "en": "Israel"
            },
            "city": {
                "by": "Ерусалім",
                "ru": "Иерусалим",
                "en": "Jerusalem"
            },
            "coordinates": [31.7656, 35.1492],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Hadassah_Hospital_Jerusalem_Chagall_windows_Synagogue_BW_13.JPG/960px-Hadassah_Hospital_Jerusalem_Chagall_windows_Synagogue_BW_13.JPG",
            "wiki": "https://en.wikipedia.org/wiki/Chagall_windows_(Jerusalem)",
            "personIds": ["marc-chagall"],
            "description": {
                "by": "Сусветна вядомыя 12 вітражоў у сінагозе медыцынскага цэнтра Хадаса ў Эйн-Керэме (1962 г.), прысвечаныя дванаццаці плямёнам (каленам) Ізраіля. Адзін з галоўных шэдэўраў сакральнага мастацтва XX стагоддзя.",
                "ru": "12 всемирно известных витражей Шагала (1962 г.), посвященных двенадцати коленам Израилевым, в синагоге больницы Хадасса.",
                "en": "Chagall's renowned Twelve Tribes of Israel stained glass windows (1962) in the Abbell Synagogue at Hadassah University Medical Center in Ein Kerem."
            },
            "tags": ["шагал", "ерусалім", "ізраіль", "вітражы", "хадаса"]
        },
        {
            "id": "jerusalem-knesset-chagall-hall",
            "title": {
                "by": "Кнесет Ізраіля — Заля Марка Шагала",
                "ru": "Кнессет Израиля — Зал Марка Шагала",
                "en": "The Knesset (Jerusalem) — Chagall State Hall"
            },
            "category": "culture",
            "country": {
                "by": "Ізраіль",
                "ru": "Израиль",
                "en": "Israel"
            },
            "city": {
                "by": "Ерусалім",
                "ru": "Иерусалим",
                "en": "Jerusalem"
            },
            "coordinates": [31.7767, 35.2054],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/The_Knesset_Chagall_Hall.jpg/960px-The_Knesset_Chagall_Hall.jpg",
            "wiki": "https://en.wikipedia.org/wiki/Knesset",
            "personIds": ["marc-chagall"],
            "description": {
                "by": "Урачыстая заля прыёмаў у парламенце Ізраіля (Кнесеце), упрыгожаная трыма гіганцкімі габеленамі, насценнай мазаікай «Сцяна плачу» і 12 мазаічнымі пано на падлозе, створанымі Маркам Шагалам у 1966–1969 гг.",
                "ru": "Парадный зал в здании Кнессета с тремя гигантскими гобеленами, настенной мозаикой «Стена плача» и напольными мозаиками работы Марка Шагала.",
                "en": "The State Hall of the Israeli Parliament (Knesset), featuring three monumental tapestries, a wall mosaic of the Western Wall, and 12 floor mosaics designed by Marc Chagall."
            },
            "tags": ["шагал", "кнесет", "ерусалім", "мазаіка", "габелены"]
        },
        {
            "id": "mainz-sankt-stephan-chagall-windows",
            "title": {
                "by": "Царква Святога Стэфана ў Майнцы — вітражы прымірэння Шагала",
                "ru": "Церковь Святого Стефана в Майнце — витражи примирения Шагала",
                "en": "St. Stephan's Church (Mainz) — Chagall Peace Windows"
            },
            "category": "church",
            "country": {
                "by": "Германія",
                "ru": "Германия",
                "en": "Germany"
            },
            "city": {
                "by": "Майнц",
                "ru": "Майнц",
                "en": "Mainz"
            },
            "coordinates": [49.9959, 8.2687],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Mainz-Stephanskirche-Chagallfenster.jpg/960px-Mainz-Stephanskirche-Chagallfenster.jpg",
            "wiki": "https://en.wikipedia.org/wiki/St._Stephan,_Mainz",
            "personIds": ["marc-chagall"],
            "description": {
                "by": "Дзевяць велічных блакітных вітражоў (1978–1985 гг.) у царкве Св. Стэфана ў Майнцы. Гэта адзіная праца Шагала ў нямецкіх храмах, якую мастак пагадзіўся выканаць на схіле гадоў як сімвал габрэйска-хрысціянскага прымірэння і міру пасля Другой сусветнай вайны.",
                "ru": "Девять синих витражей (1978–1985 гг.) в церкви Св. Стефана в Майнце — единственная работа Шагала для немецкой церкви, созданная как символ еврейско-христианского примирения.",
                "en": "Nine luminous blue stained glass windows created by Marc Chagall between 1978 and 1985 as a historic symbol of Jewish-Christian and German-Jewish reconciliation."
            },
            "tags": ["шагал", "майнц", "германія", "вітражы", "прымірэнне"]
        },
        {
            "id": "tudeley-all-saints-chagall-windows",
            "title": {
                "by": "Царква Усіх Святых у Т'юдлі — усе 12 вітражоў Марка Шагала",
                "ru": "Церковь Всех Святых в Тьюдли — все 12 витражей Марка Шагала",
                "en": "All Saints' Church, Tudeley — Complete Chagall Windows"
            },
            "category": "church",
            "country": {
                "by": "Вялікабрытанія",
                "ru": "Великобритания",
                "en": "United Kingdom"
            },
            "city": {
                "by": "Т'юдлі",
                "ru": "Тьюдли",
                "en": "Tudeley"
            },
            "coordinates": [51.1884, 0.3347],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/All_Saints_Church_Tudeley_east_window.jpg/960px-All_Saints_Church_Tudeley_east_window.jpg",
            "wiki": "https://en.wikipedia.org/wiki/All_Saints'_Church,_Tudeley",
            "personIds": ["marc-chagall"],
            "description": {
                "by": "Адзіная царква ў свеце, дзе ВСЕ 12 акон аформлены вітражамі Марка Шагала (1967–1985 гг.) у графстве Кент. Прысвечаны памяці загінулай у 21 год Сары д'Авігдор-Голдсмід. Усходняе акно малюе дзяўчыну пад вадой, якую суцяшае анёл.",
                "ru": "Единственная церковь в мире, где ВСЕ 12 окон выполнены Марком Шагалом (1967–1985 гг.) в память о Саре д'Авигдор-Голдсмид.",
                "en": "The only church in the entire world where all twelve windows were designed by Marc Chagall, commissioned in memory of Sarah d'Avigdor-Goldsmid."
            },
            "tags": ["шагал", "вялікабрытанія", "вітражы", "кент"]
        },
        {
            "id": "chicago-art-institute-chagall-windows",
            "title": {
                "by": "Чыкагскі інстытут мастацтваў і Чэйз-Плаза — «Вокны Амерыкі» і мазаіка «Чатыры пары года»",
                "ru": "Чикагский институт искусств и Чейз-Плаза — «Окна Америки» и мозаика Шагала",
                "en": "Art Institute of Chicago & Chase Tower Plaza — America Windows and Four Seasons"
            },
            "category": "culture",
            "mustSee": True,
            "country": {
                "by": "ЗША",
                "ru": "США",
                "en": "United States"
            },
            "city": {
                "by": "Чыкага",
                "ru": "Чикаго",
                "en": "Chicago"
            },
            "coordinates": [41.8796, -87.6237],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Chagall_America_Windows.jpg/960px-Chagall_America_Windows.jpg",
            "wiki": "https://en.wikipedia.org/wiki/America_Windows",
            "personIds": ["marc-chagall"],
            "description": {
                "by": "Славутыя вітражы «Вокны Амерыкі» (America Windows, 1977 г., 36 панэляў у гонар свабоды і амерыканскага двухсотгоддзя) у Чыкагскім інстытуце мастацтваў, а таксама грандыёзная адкрытая чатырохбаковая мазаіка «Чатыры пары года» (The Four Seasons, 1974 г., 21 метр даўжынёй) на плошчы Chase Tower Plaza ў цэнтры Чыкага.",
                "ru": "Знаменитые витражи «Окна Америки» (1977 г.) в Чикагском институте искусств и грандиозная 21-метровая уличная мозаика «Четыре времени года» (1974 г.) на Chase Tower Plaza.",
                "en": "The celebrated America Windows (1977) at the Art Institute of Chicago, and the monumental 70-foot outdoor mosaic 'The Four Seasons' (1974) at Chase Tower Plaza."
            },
            "tags": ["шагал", "чыкага", "зша", "вітражы", "мазаіка"]
        },
        {
            "id": "new-york-met-opera-chagall-murals",
            "title": {
                "by": "Метрапалітэн-опера (Лінкальн-цэнтр) — насценныя пано Марка Шагала",
                "ru": "Метрополитен-опера (Линкольн-центр) — монументальные панно Марка Шагала",
                "en": "Metropolitan Opera House (Lincoln Center) — Chagall Murals"
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
            "coordinates": [40.7729, -73.9845],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Metropolitan_Opera_House_Lincoln_Center_September_2021_004.jpg/960px-Metropolitan_Opera_House_Lincoln_Center_September_2021_004.jpg",
            "wiki": "https://en.wikipedia.org/wiki/Metropolitan_Opera_House_(Lincoln_Center)",
            "personIds": ["marc-chagall"],
            "description": {
                "by": "Два гіганцкія палатна памерам 9х11 метраў «Вытокі музыкі» і «Трыумф музыкі» (1966 г.), упрыгожваюць параднае фае опернага тэатра Метрапалітэн-опера ў Лінкальн-цэнтры Нью-Ёрка. Іх відаць праз шкляны фасад будынка з плошчы.",
                "ru": "Два гигантских панно (9х11 м) «Источники музыки» и «Триумф музыки» (1966 г.), украшающие парадное фойе театра Метрополитен-опера в Линкольн-центре.",
                "en": "Two colossal murals (30x36 ft), 'The Sources of Music' and 'The Triumph of Music' (1966), adorning the grand lobby of the Metropolitan Opera House at Lincoln Center."
            },
            "tags": ["шагал", "нью-ёрк", "опера", "зша", "мастацтва"]
        },
        {
            "id": "saint-paul-de-vence-chagall-grave",
            "title": {
                "by": "Сэн-Поль-дэ-Ванс — магіла Марка Шагала і мазаіка Fondation Maeght",
                "ru": "Сен-Поль-де-Ванс — могила Марка Шагала и мозаика Fondation Maeght",
                "en": "Saint-Paul-de-Vence — Chagall's Grave and Maeght Foundation Mosaic"
            },
            "category": "grave",
            "country": {
                "by": "Францыя",
                "ru": "Франция",
                "en": "France"
            },
            "city": {
                "by": "Сэн-Поль-дэ-Ванс",
                "ru": "Сен-Поль-де-Ванс",
                "en": "Saint-Paul-de-Vence"
            },
            "coordinates": [43.6953, 7.1226],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Tombe_de_Marc_Chagall.jpg/960px-Tombe_de_Marc_Chagall.jpg",
            "wiki": "https://fr.wikipedia.org/wiki/Saint-Paul-de-Vence",
            "personIds": ["marc-chagall"],
            "description": {
                "by": "Жывапіснае праванскае мястэчка, дзе Марк Шагал жыў апошнія два дзесяцігоддзі і дзе ён пахаваны на вясковых могілках побач з жонкай Валянцінай (Вавай). Непадалёк у музеі сучаснага мастацтва Fondation Maeght знаходзіцца вялікая насценная мазаіка Шагала «Закаханыя» (Les Amoureux, 1968 г.).",
                "ru": "Прованский городок, где Марк Шагал прожил последние два десятилетия и похоронен на местном кладбище. Рядом в музее Fondation Maeght расположена его настенная мозаика «Влюбленные» (1968).",
                "en": "The picturesque Provençal village where Marc Chagall spent his final decades and is buried at the local cemetery. Nearby at Fondation Maeght is his monumental wall mosaic 'The Lovers' (1968)."
            },
            "tags": ["шагал", "магіла", "францыя", "мазаіка", "пахаванне"]
        },
        {
            "id": "amsterdam-stedelijk-chagall",
            "title": {
                "by": "Гарадскі музей Амстэрдама (Stedelijk Museum) — калекцыя Марка Шагала",
                "ru": "Городской музей Амстердама (Стеделейк) — коллекция Марка Шагала",
                "en": "Stedelijk Museum Amsterdam — Chagall Masterpiece Collection"
            },
            "category": "culture",
            "country": {
                "by": "Нідэрланды",
                "ru": "Нидерланды",
                "en": "Netherlands"
            },
            "city": {
                "by": "Амстэрдам",
                "ru": "Амстердам",
                "en": "Amsterdam"
            },
            "coordinates": [52.3581, 4.8799],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Stedelijk_Museum_Amsterdam_%282012%29.JPG/960px-Stedelijk_Museum_Amsterdam_%282012%29.JPG",
            "wiki": "https://en.wikipedia.org/wiki/Stedelijk_Museum_Amsterdam",
            "personIds": ["marc-chagall"],
            "description": {
                "by": "Адзін з галоўных еўрапейскіх музеяў сучаснага мастацтва захоўвае знакамітыя шэдэўры Шагала віцебскага і раннепарыжскага перыяду, у тым ліку палотны «Аўтапартрэт з сямю пальцамі» (1912–1913 гг.), «Скрыпач» (1912 г.), «Цяжарная жанчына» і «Сінагога ў Цфаце».",
                "ru": "Один из ведущих европейских музеев современного искусства хранит шедевры Шагала: «Автопортрет с семью пальцами» (1912–1913), «Скрипач» (1912) и др.",
                "en": "Premier Dutch modern art museum holding major Chagall masterpieces including 'Self-Portrait with Seven Fingers' (1912–13), 'The Fiddler' (1912), and 'The Synagogue at Safed'."
            },
            "tags": ["шагал", "амстэрдам", "нідэрланды", "музей", "жывапіс"]
        },
        {
            "id": "basel-kunstmuseum-chagall",
            "title": {
                "by": "Мастацкі музей Базеля (Kunstmuseum Basel) — калекцыя Марка Шагала",
                "ru": "Художественный музей Базеля — коллекция Марка Шагала",
                "en": "Kunstmuseum Basel — Marc Chagall Collection"
            },
            "category": "culture",
            "country": {
                "by": "Швейцарыя",
                "ru": "Швейцария",
                "en": "Switzerland"
            },
            "city": {
                "by": "Базель",
                "ru": "Базель",
                "en": "Basel"
            },
            "coordinates": [47.5540, 7.5942],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Kunstmuseum_Basel_Neubau_2016.jpg/960px-Kunstmuseum_Basel_Neubau_2016.jpg",
            "wiki": "https://en.wikipedia.org/wiki/Kunstmuseum_Basel",
            "personIds": ["marc-chagall"],
            "description": {
                "by": "Найстарэйшы публічны музей Еўропы валодае адной з найлепшых калекцый шэдэўраў Шагала, у тым ліку культавымі карцінамі «Гандляр скацінай» (Le Marchand de bestiaux, 1912 г.), «Драбка табакі» (1912 г.), а таксама малюнкамі і эскізамі.",
                "ru": "Базельский художественный музей владеет одной из лучших европейских коллекций ранних шедевров Шагала: «Торговец скотом» (1912), «Щепотка табака» (1912) и др.",
                "en": "One of the most important European museum collections of Chagall's early masterworks, featuring 'The Cattle Dealer' (1912), 'The Pinch of Snuff', and key avant-garde studies."
            },
            "tags": ["шагал", "базель", "швейцарыя", "музей", "жывапіс"]
        },

        # --- Maksim Bahdanovich ---
        {
            "id": "yalta-bahdanovich-grave",
            "title": {
                "by": "Магіла і помнік Максіма Багдановіча ў Ялце",
                "ru": "Могила и памятник Максима Богдановича в Ялте",
                "en": "Grave and Monument of Maksim Bahdanovich in Yalta"
            },
            "category": "grave",
            "mustSee": True,
            "country": {
                "by": "Украіна",
                "ru": "Украина",
                "en": "Ukraine"
            },
            "city": {
                "by": "Ялта",
                "ru": "Ялта",
                "en": "Yalta"
            },
            "coordinates": [44.5019, 34.1772],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/%D0%9C%D0%BE%D0%B3%D0%B8%D0%BB%D0%B0_%D0%9C%D0%B0%D0%BA%D1%81%D0%B8%D0%BC%D0%B0_%D0%91%D0%BE%D0%B3%D0%B4%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%87%D0%B0.jpg/960px-%D0%9C%D0%BE%D0%B3%D0%B8%D0%BB%D0%B0_%D0%9C%D0%B0%D0%BA%D1%81%D0%B8%D0%BC%D0%B0_%D0%91%D0%BE%D0%B3%D0%B4%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%87%D0%B0.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Максім_Багдановіч",
            "personIds": ["maksim-bahdanovich"],
            "description": {
                "by": "Магіла класіка беларускай літаратуры Максіма Багдановіча на Старых гарадскіх могілках у Ялце (вул. Палікураўская). Сюды хворы на сухоты паэт прыехаў лячыцца і памёр 25 мая 1917 года ва ўзросце 25 гадоў, трымаючы пры сабе адзіны прыжыццёвы зборнік «Вянок». На магіле ўсталяваны выразны помнік з барэльефам паэта.",
                "ru": "Могила классика белорусской литературы Максима Богдановича на Старом городском кладбище в Ялте (ул. Поликуровская), где поэт скончался в мае 1917 года в возрасте 25 лет.",
                "en": "Grave of classic Belarusian poet Maksim Bahdanovich at the Old City Cemetery in Yalta, Crimea. Bahdanovich died here of tuberculosis in May 1917 at the age of 25, clutching his sole published poetry collection 'Vianok'."
            },
            "tags": ["багдановіч", "ялта", "пахаванне", "магіла", "крым", "літаратура"]
        },
        {
            "id": "yaroslavl-bahdanovich-museum",
            "title": {
                "by": "Дом-музей Максіма Багдановіча ў Яраслаўлі",
                "ru": "Дом-музей Максима Богдановича в Ярославле",
                "en": "Maksim Bahdanovich Museum in Yaroslavl"
            },
            "category": "culture",
            "country": {
                "by": "Расія",
                "ru": "Россия",
                "en": "Russia"
            },
            "city": {
                "by": "Яраслаўль",
                "ru": "Ярославль",
                "en": "Yaroslavl"
            },
            "coordinates": [57.6258, 39.8732],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/%D0%94%D0%BE%D0%BC%2C_%D0%B3%D0%B4%D0%B5_%D0%B6%D0%B8%D0%BB_%D0%9C._%D0%90._%D0%91%D0%BE%D0%B3%D0%B4%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%87.JPG/960px-%D0%94%D0%BE%D0%BC%2C_%D0%B3%D0%B4%D0%B5_%D0%B6%D0%B8%D0%BB_%D0%9C._%D0%90._%D0%91%D0%BE%D0%B3%D0%B4%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%87.JPG",
            "wiki": "https://ru.wikipedia.org/wiki/Музей_Максима_Богдановича_(Ярославль)",
            "personIds": ["maksim-bahdanovich"],
            "description": {
                "by": "Мемарыяльны дом-музей на вул. Чайкоўскага, 21, дзе сям'я Багдановічаў жыла ў 1912–1914 гг. Менавіта тут Максім скончыў Яраслаўскі юрыдычны ліцэй Дзямідава і напісаў многія свае лепшыя паэтычныя шэдэўры. Каля Яраслаўскага ўніверсітэта таксама стаіць помнік паэту.",
                "ru": "Мемориальный дом-музей на ул. Чайковского, 21, где семья Богдановичей жила в 1912–1914 гг. Здесь поэт окончил Демидовский лицей и создал шедевры белорусской лирики.",
                "en": "Memorial House Museum on Chaykovskogo St. 21 in Yaroslavl, where the Bahdanovich family lived from 1912 to 1914 while Maksim studied at the Demidov Lyceum."
            },
            "tags": ["багдановіч", "яраслаўль", "музей", "літаратура"]
        },
        {
            "id": "koreiz-bahdanovich-monument",
            "title": {
                "by": "Помнік Максіму Багдановічу ў Карэізе (санаторый «Беларусь»)",
                "ru": "Памятник Максиму Богдановичу в Кореизе (санаторий «Белоруссия»)",
                "en": "Maksim Bahdanovich Monument in Koreiz"
            },
            "category": "monument",
            "country": {
                "by": "Украіна",
                "ru": "Украина",
                "en": "Ukraine"
            },
            "city": {
                "by": "Карэіз",
                "ru": "Кореиз",
                "en": "Koreiz"
            },
            "coordinates": [44.4297, 34.0924],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/%D0%9F%D0%B0%D0%BC%D1%8F%D1%82%D0%BD%D0%B8%D0%BA_%D0%9C%D0%B0%D0%BA%D1%81%D0%B8%D0%BC%D1%83_%D0%91%D0%BE%D0%B3%D0%B4%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%87%D1%83.jpg/960px-%D0%9F%D0%B0%D0%BC%D1%8F%D1%82%D0%BD%D0%B8%D0%BA_%D0%9C%D0%B0%D0%BA%D1%81%D0%B8%D0%BC%D1%83_%D0%91%D0%BE%D0%B3%D0%B4%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%87%D1%83.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Максім_Багдановіч",
            "personIds": ["maksim-bahdanovich"],
            "description": {
                "by": "Помнік паэту, усталяваны ў 1957 годзе ў парку беларускага санаторыя «Беларусь» у пасёлку Карэіз на Паўднёвым беразе Крыма (Місхорскі спуск).",
                "ru": "Памятник поэту, установленный в 1957 г. в парке санатория «Белоруссия» в Кореизе на Южном берегу Крыма.",
                "en": "Monument to Maksim Bahdanovich erected in 1957 in the park of Sanatorium Belarus in Koreiz, Southern Crimea."
            },
            "tags": ["багдановіч", "помнік", "крым", "карэіз"]
        },

        # --- Klaudziy Duzh-Dusheuski (Nasha Niva 375085) ---
        {
            "id": "kaunas-petrasiunai-duzh-dusheuski-grave",
            "title": {
                "by": "Магіла Клаўдзія Дуж-Душэўскага (Пятрашунскія могілкі, Каўнас)",
                "ru": "Могила Клавдия Дуж-Душевского (Петрашюнское кладбище, Каунас)",
                "en": "Grave of Klaudziy Duzh-Dusheuski (Petrašiūnai Cemetery, Kaunas)"
            },
            "category": "grave",
            "mustSee": True,
            "country": {
                "by": "Літва",
                "ru": "Литва",
                "en": "Lithuania"
            },
            "city": {
                "by": "Каўнас",
                "ru": "Каунас",
                "en": "Kaunas"
            },
            "coordinates": [54.8906, 24.0042],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Klaudiusz_Du%C5%BC-Duszewski_gr%C3%B3b.JPG/960px-Klaudiusz_Du%C5%BC-Duszewski_gr%C3%B3b.JPG",
            "wiki": "https://be.wikipedia.org/wiki/Клаўдзій_Сцяпанавіч_Дуж-Душэўскі",
            "source": "https://nashaniva.com/375085",
            "personIds": ["klaudziy-duzh-dusheuski"],
            "description": {
                "by": "Магіла аўтара бел-чырвона-белага сцяга, выбітнага архітэктара і дзеяча БНР Клаўдзія Дуж-Душэўскага на Пятрашунскім пантэоне ў Каўнасе. У 2023 годзе на магіле адкрыты новы мемарыяльны помнік з выявай герба «Пагоня» і нацыянальнага сцяга.",
                "ru": "Могила создателя бело-красно-белого флага, выдающегося архитектора и дипломата БНР Клавдия Дуж-Душевского на Петрашюнском кладбище в Каунасе.",
                "en": "Grave of Klaudziy Duzh-Dusheuski, creator of the Belarusian White-Red-White flag, BNR diplomat, and renowned architect, located at the prestigious Petrašiūnai Cemetery in Kaunas."
            },
            "tags": ["душэўскі", "каўнас", "магіла", "бнр", "сцяг", "літва"]
        },
        {
            "id": "kaunas-vytautas-8-duzh-dusheuski-house",
            "title": {
                "by": "Дом Клаўдзія Дуж-Душэўскага ў Каўнасе (пр. Вітаўта, 8)",
                "ru": "Дом Клавдия Дуж-Душевского в Каунасе (пр. Витаутаса, 8)",
                "en": "House of Klaudziy Duzh-Dusheuski in Kaunas (Vytauto pr. 8)"
            },
            "category": "historical",
            "country": {
                "by": "Літва",
                "ru": "Литва",
                "en": "Lithuania"
            },
            "city": {
                "by": "Каўнас",
                "ru": "Каунас",
                "en": "Kaunas"
            },
            "coordinates": [54.8931, 23.9248],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Petrasiunai_2022b.jpg/960px-Petrasiunai_2022b.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Клаўдзій_Сцяпанавіч_Дуж-Душэўскі",
            "source": "https://nashaniva.com/375085",
            "personIds": ["klaudziy-duzh-dusheuski", "anton-lutskevich"],
            "description": {
                "by": "Гістарычны дом на праспекце Вітаўта, 8 (кв. 5) у Каўнасе, дзе жыў і працаваў Клаўдзій Дуж-Душэўскі. Адсюль ён падтрымліваў Беларускі музей у Вільні і паўгалоднага Антона Луцкевіча, сюды прыязджалі дзеячы беларускага руху, і тут сям'я Дуж-Душэўскіх ратавала габрэйскіх дзяцей у гады Халакосту.",
                "ru": "Исторический дом на проспекте Витаутаса, 8 в Каунасе, где жил архитектор Дуж-Душевский, помогал Антону Луцкевичу и спасал еврейских детей в годы войны.",
                "en": "Historic residence of architect Klaudziy Duzh-Dusheuski on Vytauto Avenue in Kaunas, from where he supported the Belarusian Museum in Vilnius and sheltered Jewish children during WWII."
            },
            "tags": ["душэўскі", "каўнас", "луцкевіч", "салідарнасць", "літва"]
        },

        # --- BNR Prague Pantheon ---
        {
            "id": "prague-olsany-belarusian-pantheon",
            "title": {
                "by": "Ольшанскія могілкі — Беларускі пантэон у Празе (Крэчэўскі, Захарка, Забэйда-Суміцкі)",
                "ru": "Ольшанское кладбище — Белорусский пантеон в Праге",
                "en": "Olšany Cemetery — Belarusian Pantheon in Prague"
            },
            "category": "grave",
            "mustSee": True,
            "country": {
                "by": "Чэхія",
                "ru": "Чехия",
                "en": "Czech Republic"
            },
            "city": {
                "by": "Прага",
                "ru": "Прага",
                "en": "Prague"
            },
            "coordinates": [50.0815, 14.4705],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Ol%C5%A1ansk%C3%A9_h%C5%99bitovy_br%C3%A1na_1.jpg/960px-Ol%C5%A1ansk%C3%A9_h%C5%99bitovy_br%C3%A1na_1.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Ольшанскія_могілкі",
            "personIds": ["pyotra-krecheuski", "vasil-zaharka", "mikhas-zabejda-sumitski"],
            "description": {
                "by": "Галоўны некропаль беларускай эміграцыі ў міжваеннай Чэхаславакіі. Каля царквы Успення Багародзіцы (участак 2bis) пахаваныя Старшыні Рады Беларускай Народнай Рэспублікі Пётр Крэчэўскі (1879–1928) і Васіль Захарка (1877–1943), а таксама славуты оперны спявак Міхась Забэйда-Суміцкі (1900–1981).",
                "ru": "Главный некрополь белорусской эмиграции в Праге. Здесь похоронены президенты Рады БНР Петр Кречевский и Василий Захарко, а также оперный тенор Михась Забейдо-Сумицкий.",
                "en": "Main necropolis of the Belarusian diaspora in interwar Czechoslovakia. Located near the Dormition Church (section 2bis), it contains the graves of Rada BNR Presidents Pyotra Krecheuski and Vasil Zaharka, and opera tenor Mikhas Zabejda-Sumitski."
            },
            "tags": ["прага", "бнр", "крэчэўскі", "захарка", "забэйда", "пахаванне"]
        },

        # --- Yanka Kupala ---
        {
            "id": "pechishchi-kupala-museum",
            "title": {
                "by": "Музей Янкі Купалы ў Пячышчах (Татарстан)",
                "ru": "Музей Янки Купалы в Печищах (Татарстан)",
                "en": "Yanka Kupala Memorial Museum in Pechishchi"
            },
            "category": "culture",
            "country": {
                "by": "Расія",
                "ru": "Россия",
                "en": "Russia"
            },
            "city": {
                "by": "Пячышчы",
                "ru": "Печищи",
                "en": "Pechishchi"
            },
            "coordinates": [55.7761, 48.9744],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/%D0%92%D0%B8%D0%B4_%D0%BD%D0%B0_%D1%81%D0%B5%D0%BB%D0%BE_%D0%9F%D0%B5%D1%87%D0%B8%D1%89%D0%B8_%D1%81%D0%BE_%D1%81%D1%82%D0%BE%D1%80%D0%BE%D0%BD%D1%8B_%D0%9A%D0%B0%D0%B7%D0%B0%D0%BD%D0%B8.JPG/960px-%D0%92%D0%B8%D0%B4_%D0%BD%D0%B0_%D1%81%D0%B5%D0%BB%D0%BE_%D0%9F%D0%B5%D1%87%D0%B8%D1%89%D0%B8_%D1%81%D0%BE_%D1%81%D1%82%D0%BE%D1%80%D0%BE%D0%BD%D1%8B_%D0%9A%D0%B0%D0%B7%D0%B0%D0%BD%D0%B8.JPG",
            "wiki": "https://ru.wikipedia.org/wiki/Музей_Янки_Купалы_в_селе_Печищи",
            "personIds": ["yanka-kupala"],
            "description": {
                "by": "Адзіны музей Янкі Купалы ў Расіі, адкрыты ў 1975 годзе ў будынку старога млына на беразе Волгі, дзе народны паэт Беларусі жыў у эвакуацыі з лістапада 1941 па чэрвень 1942 года. Тут напісаны вершы «Зноў будзем шчасце мець і волю», «Беларускім партызанам».",
                "ru": "Единственный музей Янки Купалы в России, открытый в здании мельницы на Волге, где поэт жил в эвакуации с осени 1941 по июнь 1942 года.",
                "en": "The only Yanka Kupala museum in Russia, located in a historic Volga mill in Pechishchi near Kazan where the Belarusian national poet lived in wartime evacuation (1941–1942)."
            },
            "tags": ["купала", "музей", "эвакуацыя", "татарстан", "волга"]
        },
        {
            "id": "moscow-hotel-moskva-kupala",
            "title": {
                "by": "Гатэль «Масква» — месца трагічнай гібелі Янкі Купалы",
                "ru": "Гостиница «Москва» — место гибели Янки Купалы",
                "en": "Hotel Moskva — Site of Yanka Kupala's Tragic Death"
            },
            "category": "historical",
            "country": {
                "by": "Расія",
                "ru": "Россия",
                "en": "Russia"
            },
            "city": {
                "by": "Масква",
                "ru": "Москва",
                "en": "Moscow"
            },
            "coordinates": [55.7572, 37.6166],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Moskva_Hotel_in_MSK_%28img1%29.jpg/960px-Moskva_Hotel_in_MSK_%28img1%29.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Янка_Купала",
            "personIds": ["yanka-kupala"],
            "description": {
                "by": "Гістарычны будынак гатэля «Масква» на Ахотным радзе, дзе 28 чэрвеня 1942 года пры нявысветленых і загадкавых акалічнасцях (падзенне ў лесвічны пралёт паміж 9 і 10 паверхамі) загінуў пясняр Беларусі Янка Купала.",
                "ru": "Гостиница «Москва» в Охотном ряду, где 28 июня 1942 года при невыясненных трагических обстоятельствах оборвалась жизнь национального поэта Беларуси Янки Купалы.",
                "en": "Site of the mysterious and tragic death of Belarus's greatest national poet, Yanka Kupala, who fell down the stairwell of Hotel Moskva on June 28, 1942."
            },
            "tags": ["купала", "масква", "трагедыя", "гісторыя"]
        },

        # --- Yakub Kolas ---
        {
            "id": "tashkent-kolas-monument-museum",
            "title": {
                "by": "Помнік і вуліца Якуба Коласа ў Ташкенце",
                "ru": "Памятник и улица Якуба Коласа в Ташкенте",
                "en": "Yakub Kolas Monument and Street in Tashkent"
            },
            "category": "monument",
            "country": {
                "by": "Узбекістан",
                "ru": "Узбекистан",
                "en": "Uzbekistan"
            },
            "city": {
                "by": "Ташкент",
                "ru": "Ташкент",
                "en": "Tashkent"
            },
            "coordinates": [41.3039, 69.2789],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Kanstantin_Mickievi%C4%8D_%28Jakub_Ko%C5%82as%29._%D0%9A%D0%B0%D0%BD%D1%81%D1%82%D0%B0%D0%BD%D1%82%D1%96%D0%BD_%D0%9C%D1%96%D1%86%D0%BA%D0%B5%D0%B2%D1%96%D1%87_%28%D0%AF%D0%BA%D1%83%D0%B1_%D0%9A%D0%BE%D0%BB%D0%B0%D1%81%29_%281908%29.jpg/960px-Kanstantin_Mickievi%C4%8D_%28Jakub_Ko%C5%82as%29._%D0%9A%D0%B0%D0%BD%D1%81%D1%82%D0%B0%D0%BD%D1%82%D1%96%D0%BD_%D0%9C%D1%96%D1%86%D0%BA%D0%B5%D0%B2%D1%96%D1%87_%28%D0%AF%D0%BA%D1%83%D0%B1_%D0%9A%D0%BE%D0%BB%D0%B0%D1%81%29_%281908%29.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Якуб_Колас",
            "personIds": ["yakub-kolas"],
            "description": {
                "by": "Бронзавы бюст класіка беларускай літаратуры Якуба Коласа, адкрыты ў скверы на вуліцы Якуба Коласа ў цэнтры Ташкента. Узбекістан стаў для паэта прытулкам у гады эвакуацыі (1941–1943 гг.), дзе ён напісаў паэму «Салавей» і дзясяткі патрыятычных вершаў.",
                "ru": "Бронзовый бюст классика белорусской литературы Якуба Коласа на одноименной улице в Ташкенте, где поэт жил в эвакуации в 1941–1943 годах.",
                "en": "Bronze bust of classic Belarusian writer Yakub Kolas in Tashkent, Uzbekistan, commemorating his evacuation years (1941–1943) during which he penned poems of wartime resistance."
            },
            "tags": ["колас", "ташкент", "помнік", "узбекістан", "літаратура"]
        },

        # --- Ivan Lutskevich ---
        {
            "id": "zakopane-luczkiewicz-sanatorium",
            "title": {
                "by": "Закапанэ — месца смерці Івана Луцкевіча (1919)",
                "ru": "Закопане — место смерти Ивана Луцкевича (1919)",
                "en": "Zakopane — Deathplace of Ivan Lutskevich (1919)"
            },
            "category": "historical",
            "country": {
                "by": "Польшча",
                "ru": "Польша",
                "en": "Poland"
            },
            "city": {
                "by": "Закапанэ",
                "ru": "Закопане",
                "en": "Zakopane"
            },
            "coordinates": [49.2992, 19.9496],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Suprasl_monastery_interior_view_18.jpg/960px-Suprasl_monastery_interior_view_18.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Іван_Іванавіч_Луцкевіч",
            "personIds": ["ivan-lutskevich"],
            "description": {
                "by": "Горны курорт у Татрах, куды цяжка хворы на сухоты ідэолаг беларускага адраджэння і заснавальнік БНР Іван Луцкевіч накіраваўся на лячэнне ў санаторый і дзе ён памёр 20 жніўня 1919 года ва ўзросце 38 гадоў. Быў пахаваны на Новых могілках у Закапанэ (у 1991 г. прах урачыста перапахаваны на могілках Росы ў Вільні).",
                "ru": "Горный курорт в Татрах, где в санатории 20 августа 1919 года скончался идеолог белорусского национального возрождения Иван Луцкевич.",
                "en": "Tatra mountain resort where founding father of the Belarusian national revival Ivan Lutskevich passed away in a sanatorium in August 1919 before his eventual reburial in Vilnius."
            },
            "tags": ["луцкевіч", "закапанэ", "бнр", "польшча", "гісторыя"]
        },

        # --- Maksim Haretski ---
        {
            "id": "vyazma-haretski-memorial",
            "title": {
                "by": "Вязьма — месца расстрэлу Максіма Гарэцкага",
                "ru": "Вязьма — место расстрела Максима Горецкого",
                "en": "Vyazma — Execution and Memorial Site of Maksim Haretski"
            },
            "category": "grave",
            "country": {
                "by": "Расія",
                "ru": "Россия",
                "en": "Russia"
            },
            "city": {
                "by": "Вязьма",
                "ru": "Вязьма",
                "en": "Vyazma"
            },
            "coordinates": [55.2104, 34.2951],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Maksim_Harecki._%D0%9C%D0%B0%D0%BA%D1%81%D1%96%D0%BC_%D0%93%D0%B0%D1%80%D1%8D%D1%86%D0%BA%D1%96_%281920%29.jpg/960px-Maksim_Harecki._%D0%9C%D0%B0%D0%BA%D1%81%D1%96%D0%BC_%D0%93%D0%B0%D1%80%D1%8D%D1%86%D0%BA%D1%96_%281920%29.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Максім_Іванавіч_Гарэцкі",
            "personIds": ["maksim-haretski"],
            "description": {
                "by": "Месца трагічнай гібелі класіка беларускай літаратуры Максіма Гарэцкага, які пасля ссылкі працаваў настаўнікам у мястэчку Пясочня, быў паўторна арыштаваны НКУС і расстраляны 10 лютага 1938 года ў Вязьме. У горадзе ўсталяваны памятны знак рэпрэсаваным.",
                "ru": "Место гибели классика белорусской литературы Максима Горецкого, расстрелянного органами НКВД в Вязьме 10 февраля 1938 года.",
                "en": "Execution site of classic Belarusian prose writer Maksim Haretski, who was falsely condemned and executed by the Soviet NKVD in Vyazma on February 10, 1938."
            },
            "tags": ["гарэцкі", "вязьма", "рэпрэсіі", "літаратура", "памяць"]
        },

        # --- Ciotka (Alaiza Pashkievich) ---
        {
            "id": "krakow-jagiellonian-ciotka",
            "title": {
                "by": "Ягелонскі ўніверсітэт — вучоба Цёткі (Алаізы Пашкевіч)",
                "ru": "Ягеллонский университет — учеба Тётки (Алоизы Пашкевич)",
                "en": "Jagiellonian University — Studies of Ciotka (Ałaiza Paškievič)"
            },
            "category": "culture",
            "country": {
                "by": "Польшча",
                "ru": "Польша",
                "en": "Poland"
            },
            "city": {
                "by": "Кракаў",
                "ru": "Краков",
                "en": "Krakow"
            },
            "coordinates": [50.0617, 19.9338],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/A%C5%82aiza_Pa%C5%A1kievi%C4%8D_%28Ciotka%29._%D0%90%D0%BB%D0%B0%D1%96%D0%B7%D0%B0_%D0%9F%D0%B0%D1%88%D0%BA%D0%B5%D0%B2%D1%96%D1%87_%28%D0%A6%D1%8F%D1%82%D0%BA%D0%B0%29_%281900-16%29.jpg/960px-A%C5%82aiza_Pa%C5%A1kievi%C4%8D_%28Ciotka%29._%D0%90%D0%BB%D0%B0%D1%96%D0%B7%D0%B0_%D0%9F%D0%B0%D1%88%D0%BA%D0%B5%D0%B2%D1%96%D1%87_%28%D0%A6%D1%8F%D1%82%D0%BA%D0%B0%29_%281900-16%29.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Алаіза_Сцяпанаўна_Пашкевіч",
            "personIds": ["ciotka"],
            "description": {
                "by": "Старажытны Ягелонскі ўніверсітэт (Collegium Novum), дзе Алаіза Пашкевіч (Цётка) навучалася на філасофскім факультэце ў 1908–1909 гг. пад чужым імем, хаваючыся ад пераследу расійскай паліцыі, і адкуль яна кіравала выданнем беларускіх кніг.",
                "ru": "Ягеллонский университет в Кракове, где Алоиза Пашкевич (Тётка) изучала философию в 1908–1909 гг., скрываясь от царской полиции.",
                "en": "The prestigious Jagiellonian University in Kraków, where pioneer poet and activist Ciotka (Ałaiza Paškievič) studied philosophy in 1908–1909 while living under assumed identity."
            },
            "tags": ["цётка", "кракаў", "ўніверсітэт", "польшча", "літаратура"]
        },

        # --- Vatslau Lastouski ---
        {
            "id": "kaunas-lastouski-bnr-government",
            "title": {
                "by": "Каўнас — рэзідэнцыя ўрада БНР і рэдакцыя «Крывіча» Вацлава Ластоўскага",
                "ru": "Каунас — резиденция правительства БНР и редакция Вацлава Ластовского",
                "en": "Kaunas — BNR Government Residence and Lastouski's 'Kryvich'"
            },
            "category": "historical",
            "country": {
                "by": "Літва",
                "ru": "Литва",
                "en": "Lithuania"
            },
            "city": {
                "by": "Каўнас",
                "ru": "Каунас",
                "en": "Kaunas"
            },
            "coordinates": [54.8978, 23.9036],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Suprasl_monastery_interior_view_18.jpg/960px-Suprasl_monastery_interior_view_18.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Вацлаў_Юсцінавіч_Ластоўскі",
            "personIds": ["vaclau-lastouski"],
            "description": {
                "by": "У часовай сталіцы міжваеннай Літвы дзейнічаў урад Беларускай Народнай Рэспублікі на чале з прэм'ер-міністрам Вацлавам Ластоўскім (1920–1923 гг.). Тут знаходзілася Беларускае прэс-бюро, Міністэрства беларускіх спраў Літвы і выдаваўся навукова-літаратурны часопіс «Крывіч».",
                "ru": "В Каунасе действовало правительство БНР во главе с премьер-министром Вацлавом Ластовским (1920–1923), издавался журнал «Крывіч».",
                "en": "Interwar Lithuanian provisional capital where the Council of Ministers of the Belarusian Democratic Republic resided under Prime Minister Vatslau Lastouski (1920–1923)."
            },
            "tags": ["ластоўскі", "каўнас", "бнр", "крывіч", "літва"]
        },

        # --- Diplomatic Missions ('embassy') ---
        {
            "id": "ankara-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў Турцыі (Анкара)",
                "ru": "Посольство Беларуси в Турции (Анкара)",
                "en": "Embassy of Belarus in Turkey (Ankara)"
            },
            "category": "embassy",
            "country": {
                "by": "Турцыя",
                "ru": "Турция",
                "en": "Turkey"
            },
            "city": {
                "by": "Анкара",
                "ru": "Анкара",
                "en": "Ankara"
            },
            "coordinates": [39.8732, 32.8427],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Historical_peninsula_and_modern_skyline_of_Istanbul.jpg/960px-Historical_peninsula_and_modern_skyline_of_Istanbul.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Пасольства_Беларусі_ў_Турцыі",
            "description": {
                "by": "Афіцыйная дыпламатычная місія Рэспублікі Беларусь у Турэцкай Рэспубліцы, адкрытая ў 1997 годзе ў дыпламатычным квартале Чанкая ў Анкары (Abidin Daver Sk. 17).",
                "ru": "Официальная дипломатическая миссия Республики Беларусь в Турецкой Республике, открытая в 1997 году в Анкаре.",
                "en": "Official diplomatic mission of the Republic of Belarus to the Republic of Turkey, located in the Çankaya district of Ankara."
            },
            "tags": ["дыпламатыя", "пасольства", "турцыя", "анкара"]
        },
        {
            "id": "istanbul-consulate-belarus",
            "title": {
                "by": "Генеральнае консульства Беларусі ў Стамбуле",
                "ru": "Генеральное консульство Беларуси в Стамбуле",
                "en": "Consulate General of Belarus in Istanbul"
            },
            "category": "embassy",
            "country": {
                "by": "Турцыя",
                "ru": "Турция",
                "en": "Turkey"
            },
            "city": {
                "by": "Стамбул",
                "ru": "Стамбул",
                "en": "Istanbul"
            },
            "coordinates": [40.9786, 28.8711],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Historical_peninsula_and_modern_skyline_of_Istanbul.jpg/960px-Historical_peninsula_and_modern_skyline_of_Istanbul.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Генеральнае_консульства_Беларусі_ў_Стамбуле",
            "description": {
                "by": "Генеральнае консульства Рэспублікі Беларусь у найбуйнейшым мегаполісе Турцыі — Стамбуле, якое ажыццяўляе консульскую дапамогу беларускім грамадзянам і падтрымлівае эканамічныя кантакты.",
                "ru": "Генеральное консульство Республики Беларусь в Стамбуле.",
                "en": "Consulate General of the Republic of Belarus in Istanbul, Turkey."
            },
            "tags": ["дыпламатыя", "консульства", "турцыя", "стамбул"]
        },
        {
            "id": "washington-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў ЗША (Вашынгтон)",
                "ru": "Посольство Беларуси в США (Вашингтон)",
                "en": "Embassy of Belarus in the United States (Washington, D.C.)"
            },
            "category": "embassy",
            "country": {
                "by": "ЗША",
                "ru": "США",
                "en": "United States"
            },
            "city": {
                "by": "Вашынгтон",
                "ru": "Вашингтон",
                "en": "Washington, D.C."
            },
            "coordinates": [38.9135, -77.0682],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Embassy_of_Belarus.jpg/960px-Embassy_of_Belarus.jpg",
            "wiki": "https://en.wikipedia.org/wiki/Embassy_of_Belarus,_Washington,_D.C.",
            "description": {
                "by": "Дыпламатычная місія Рэспублікі Беларусь у Злучаных Штатах Амерыкі, размешчаная ў Вашынгтоне (1619 New Hampshire Ave NW).",
                "ru": "Дипломатическое представительство Республики Беларусь в США, расположенное в Вашингтоне.",
                "en": "Diplomatic mission of the Republic of Belarus to the United States, located on New Hampshire Avenue in Washington, D.C."
            },
            "tags": ["дыпламатыя", "пасольства", "зша", "вашынгтон"]
        },
        {
            "id": "london-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў Вялікабрытаніі (Лондан)",
                "ru": "Посольство Беларуси в Великобритании (Лондон)",
                "en": "Embassy of Belarus in the United Kingdom (London)"
            },
            "category": "embassy",
            "country": {
                "by": "Вялікабрытанія",
                "ru": "Великобритания",
                "en": "United Kingdom"
            },
            "city": {
                "by": "Лондан",
                "ru": "Лондон",
                "en": "London"
            },
            "coordinates": [51.4921, -0.1983],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Embassy_of_Belarus_in_London.jpg/960px-Embassy_of_Belarus_in_London.jpg",
            "wiki": "https://en.wikipedia.org/wiki/Embassy_of_Belarus,_London",
            "description": {
                "by": "Дыпламатычная місія Рэспублікі Беларусь у Злучаным Каралеўстве, размешчаная ў раёне Кенсінгтан у Лондане (6 Kensington Court).",
                "ru": "Дипломатическая миссия Республики Беларусь в Великобритании, расположенная в Кенсингтоне в Лондоне.",
                "en": "Official diplomatic mission of Belarus to the United Kingdom, located at Kensington Court in London."
            },
            "tags": ["дыпламатыя", "пасольства", "лондан", "вялікабрытанія"]
        },
        {
            "id": "paris-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў Францыі (Парыж)",
                "ru": "Посольство Беларуси во Франции (Париж)",
                "en": "Embassy of Belarus in France (Paris)"
            },
            "category": "embassy",
            "country": {
                "by": "Францыя",
                "ru": "Франция",
                "en": "France"
            },
            "city": {
                "by": "Парыж",
                "ru": "Париж",
                "en": "Paris"
            },
            "coordinates": [48.8654, 2.2687],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Ambassade_de_Bi%C3%A9lorussie_en_France%2C_38_boulevard_Suchet%2C_Paris_16e_2.jpg/960px-Ambassade_de_Bi%C3%A9lorussie_en_France%2C_38_boulevard_Suchet%2C_Paris_16e_2.jpg",
            "wiki": "https://fr.wikipedia.org/wiki/Ambassade_de_Bi%C3%A9lorussie_en_France",
            "description": {
                "by": "Дыпламатычная місія Рэспублікі Беларусь у Французскай Рэспубліцы (38 Boulevard Suchet, XVI акруга Парыжа).",
                "ru": "Посольство Республики Беларусь во Франции (38 Boulevard Suchet, Париж).",
                "en": "Embassy of Belarus in France, located on Boulevard Suchet in the 16th arrondissement of Paris."
            },
            "tags": ["дыпламатыя", "пасольства", "парыж", "францыя"]
        },
        {
            "id": "berlin-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў Германіі (Берлін)",
                "ru": "Посольство Беларуси в Германии (Берлин)",
                "en": "Embassy of Belarus in Germany (Berlin)"
            },
            "category": "embassy",
            "country": {
                "by": "Германія",
                "ru": "Германия",
                "en": "Germany"
            },
            "city": {
                "by": "Берлін",
                "ru": "Берлин",
                "en": "Berlin"
            },
            "coordinates": [52.5786, 13.4116],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Suprasl_monastery_interior_view_18.jpg/960px-Suprasl_monastery_interior_view_18.jpg",
            "wiki": "https://de.wikipedia.org/wiki/Belarussische_Botschaft_in_Berlin",
            "description": {
                "by": "Дыпламатычнае прадстаўніцтва Рэспублікі Беларусь у ФРГ (Am Treptower Park 32, Берлін).",
                "ru": "Посольство Республики Беларусь в Германии (Am Treptower Park 32, Берлин).",
                "en": "Embassy of Belarus in Germany, situated at Am Treptower Park in Berlin."
            },
            "tags": ["дыпламатыя", "пасольства", "берлін", "германія"]
        },
        {
            "id": "rome-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў Італіі (Рым)",
                "ru": "Посольство Беларуси в Италии (Рим)",
                "en": "Embassy of Belarus in Italy (Rome)"
            },
            "category": "embassy",
            "country": {
                "by": "Італія",
                "ru": "Италия",
                "en": "Italy"
            },
            "city": {
                "by": "Рым",
                "ru": "Рим",
                "en": "Rome"
            },
            "coordinates": [41.9168, 12.4939],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Suprasl_monastery_interior_view_18.jpg/960px-Suprasl_monastery_interior_view_18.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Пасольства_Беларусі_ў_Італіі",
            "description": {
                "by": "Афіцыйнае дыпламатычнае прадстаўніцтва Беларусі ў Італьянскай Рэспубліцы (Via Nomentana 361, Рым).",
                "ru": "Посольство Республики Беларусь в Италии (Рим).",
                "en": "Embassy of Belarus in Italy, located on Via Nomentana in Rome."
            },
            "tags": ["дыпламатыя", "пасольства", "рым", "італія"]
        },
        {
            "id": "warsaw-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў Польшчы (Варшава)",
                "ru": "Посольство Беларуси в Польше (Варшава)",
                "en": "Embassy of Belarus in Poland (Warsaw)"
            },
            "category": "embassy",
            "country": {
                "by": "Польшча",
                "ru": "Польша",
                "en": "Poland"
            },
            "city": {
                "by": "Варшава",
                "ru": "Варшава",
                "en": "Warsaw"
            },
            "coordinates": [52.2131, 21.0267],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Ambasada_Bia%C5%82orusi_w_Warszawie_ul._Wiertnicza_58.jpg/960px-Ambasada_Bia%C5%82orusi_w_Warszawie_ul._Wiertnicza_58.jpg",
            "wiki": "https://pl.wikipedia.org/wiki/Ambasada_Bia%C5%82orusi_w_Polsce",
            "description": {
                "by": "Дыпламатычная місія Рэспублікі Беларусь у Польшчы (вул. Вертнічая 58, Варшава).",
                "ru": "Посольство Республики Беларусь в Польше (ул. Вертнича 58, Варшава).",
                "en": "Embassy of Belarus in Poland, situated on Wiertnicza Street in Warsaw."
            },
            "tags": ["дыпламатыя", "пасольства", "варшава", "польшча"]
        },
        {
            "id": "vilnius-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў Літве (Вільня)",
                "ru": "Посольство Беларуси в Литве (Вильнюс)",
                "en": "Embassy of Belarus in Lithuania (Vilnius)"
            },
            "category": "embassy",
            "country": {
                "by": "Літва",
                "ru": "Литва",
                "en": "Lithuania"
            },
            "city": {
                "by": "Вільня",
                "ru": "Вильнюс",
                "en": "Vilnius"
            },
            "coordinates": [54.6978, 25.2673],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Suprasl_monastery_interior_view_18.jpg/960px-Suprasl_monastery_interior_view_18.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Пасольства_Беларусі_ў_Літве",
            "description": {
                "by": "Дыпламатычная місія Рэспублікі Беларусь у Літоўскай Рэспубліцы (вул. Міндаўга 13, Вільня).",
                "ru": "Посольство Республики Беларусь в Литве (ул. Миндауго 13, Вильнюс).",
                "en": "Embassy of Belarus in Lithuania, located on Mindaugo Street in Vilnius."
            },
            "tags": ["дыпламатыя", "пасольства", "вільня", "літва"]
        },
        {
            "id": "riga-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў Латвіі (Рыга)",
                "ru": "Посольство Беларуси в Латвии (Рига)",
                "en": "Embassy of Belarus in Latvia (Riga)"
            },
            "category": "embassy",
            "country": {
                "by": "Латвія",
                "ru": "Латвия",
                "en": "Latvia"
            },
            "city": {
                "by": "Рыга",
                "ru": "Рига",
                "en": "Riga"
            },
            "coordinates": [56.9664, 24.1165],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Suprasl_monastery_interior_view_18.jpg/960px-Suprasl_monastery_interior_view_18.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Пасольства_Беларусі_ў_Латвіі",
            "description": {
                "by": "Дыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Латвійскай Рэспубліцы (вул. Езусбазніцас 12, Рыга).",
                "ru": "Посольство Республики Беларусь в Латвии (ул. Езусбазницас 12, Рига).",
                "en": "Embassy of Belarus in Latvia, located on Jēzusbaznīcas Street in Riga."
            },
            "tags": ["дыпламатыя", "пасольства", "рыга", "латвія"]
        },
        {
            "id": "bern-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў Швейцарыі (Берн)",
                "ru": "Посольство Беларуси в Швейцарии (Берн)",
                "en": "Embassy of Belarus in Switzerland (Bern)"
            },
            "category": "embassy",
            "country": {
                "by": "Швейцарыя",
                "ru": "Швейцария",
                "en": "Switzerland"
            },
            "city": {
                "by": "Берн",
                "ru": "Берн",
                "en": "Bern"
            },
            "coordinates": [46.9388, 7.4645],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Suprasl_monastery_interior_view_18.jpg/960px-Suprasl_monastery_interior_view_18.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Пасольства_Беларусі_ў_Швейцарыі",
            "description": {
                "by": "Дыпламатычная місія Беларусі ў Швейцарскай Канфедэрацыі (Quartierweg 6, Лібефельд/Берн).",
                "ru": "Посольство Республики Беларусь в Швейцарии (Берн).",
                "en": "Embassy of Belarus in Switzerland, located in Liebefeld/Bern."
            },
            "tags": ["дыпламатыя", "пасольства", "берн", "швейцарыя"]
        },
        {
            "id": "vienna-embassy-belarus",
            "title": {
                "by": "Пасольства Беларусі ў Аўстрыі (Вена)",
                "ru": "Посольство Беларуси в Австрии (Вена)",
                "en": "Embassy of Belarus in Austria (Vienna)"
            },
            "category": "embassy",
            "country": {
                "by": "Аўстрыя",
                "ru": "Австрия",
                "en": "Austria"
            },
            "city": {
                "by": "Вена",
                "ru": "Вена",
                "en": "Vienna"
            },
            "coordinates": [48.1878, 16.3129],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Suprasl_monastery_interior_view_18.jpg/960px-Suprasl_monastery_interior_view_18.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Пасольства_Беларусі_ў_Аўстрыі",
            "description": {
                "by": "Пасольства Беларусі ў Аўстрыйскай Рэспубліцы і пастаяннае прадстаўніцтва пры АБСЕ і міжнародных арганізацыях у Вене (Hüttelbergstrasse 6).",
                "ru": "Посольство Республики Беларусь в Австрии и постоянное представительство при международных организациях в Вене.",
                "en": "Embassy of Belarus in Austria and Permanent Mission to international organizations in Vienna."
            },
            "tags": ["дыпламатыя", "пасольства", "вена", "аўстрыя"]
        }
    ]

    for pl in new_places:
        if pl['id'] not in existing_place_ids:
            places.append(pl)
            existing_place_ids.add(pl['id'])
            print(f"Added place {pl['id']}")

    # Save data/persons.json and data/persons.js
    with open('data/persons.json', 'w', encoding='utf-8') as f:
        json.dump(persons, f, ensure_ascii=False, indent=2)
    with open('data/persons.js', 'w', encoding='utf-8') as f:
        f.write('const personsData = ' + json.dumps(persons, ensure_ascii=False, indent=2) + ';\n')
    print("Saved persons data")

    # Save data/places.json and data/places.js
    with open('data/places.json', 'w', encoding='utf-8') as f:
        json.dump(places, f, ensure_ascii=False, indent=2)
    with open('data/places.js', 'w', encoding='utf-8') as f:
        f.write('const placesData = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')
    print("Saved places data")

if __name__ == '__main__':
    run()
