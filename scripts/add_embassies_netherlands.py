import json
import urllib.request, urllib.parse

def get_commons_url(file_name):
    url = 'https://commons.wikimedia.org/w/api.php?action=query&titles=' + urllib.parse.quote('File:' + file_name) + '&prop=imageinfo&iiprop=url&format=json'
    req = urllib.request.Request(url, headers={'User-Agent': 'AlbaruthenicaBot/1.0 (info@albaruthenica.org)'})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for p in data['query']['pages'].values():
                if 'imageinfo' in p and p['imageinfo']:
                    return p['imageinfo'][0]['url']
    except Exception as e:
        print(f"Error fetching {file_name}: {e}")
    return ''

embassy_places = [
    {
        "id": "netherlands-hague-belarusians-mara",
        "title": {
            "by": "Згуртаванне беларусаў у Нідэрландах і суполка «Мара»",
            "ru": "Объединение белорусов в Нидерландах и сообщество «Мара»",
            "en": "Association of Belarusians in the Netherlands & 'Mara' (The Hague)"
        },
        "category": "culture",
        "country": {
            "by": "Нідэрланды",
            "ru": "Нидерланды",
            "en": "Netherlands"
        },
        "city": {
            "by": "Гаага",
            "ru": "Гаага",
            "en": "The Hague"
        },
        "coordinates": [
            52.0786,
            4.3164
        ],
        "image": "",
        "description": {
            "by": "Згуртаванне беларусаў у Нідэрландах (Stichting Belarussen in Nederland) і беларуская суполка «Мара» аб'ядноўваюць беларусаў Гаагі, Амстэрдама, Ратэрдама і іншых гарадоў. Арганізацыя праводзіць культурныя фестывалі, выставы беларускіх мастакоў, дні роднай мовы, літаратурныя сустрэчы і акцыі салідарнасці.",
            "ru": "Объединение белорусов в Нидерландах (Stichting Belarussen in Nederland) и сообщество «Мара» координируют культурную и общественную жизнь диаспоры в Гааге, Амстердаме и Роттердаме.",
            "en": "The Association of Belarusians in the Netherlands (Stichting Belarussen in Nederland) and community group 'Mara' organize cultural festivals, language classes, art exhibits, and diaspora events across The Hague and Amsterdam."
        },
        "links": [
            {
                "title": "Афіцыйны сайт: Belarussen in Nederland",
                "url": "https://www.belarusians.nl/be"
            },
            {
                "title": "Вікіпедыя: Беларусы Нідэрландаў",
                "url": "https://be.wikipedia.org/wiki/Беларусы_Нідэрландаў"
            }
        ],
        "tags": [
            "Нідэрланды",
            "Гаага",
            "Амстэрдам",
            "дыяспара",
            "Мара",
            "культура"
        ],
        "mustSee": True
    },
    {
        "id": "netherlands-embassy-hague",
        "title": {
            "by": "Пасольства Беларусі ў Нідэрландах (Гаага)",
            "ru": "Посольство Беларуси в Нидерландах (Гаага)",
            "en": "Embassy of Belarus in the Netherlands (The Hague)"
        },
        "category": "culture",
        "country": {
            "by": "Нідэрланды",
            "ru": "Нидерланды",
            "en": "Netherlands"
        },
        "city": {
            "by": "Гаага",
            "ru": "Гаага",
            "en": "The Hague"
        },
        "coordinates": [
            52.0838,
            4.2842
        ],
        "image": "",
        "description": {
            "by": "Дыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Каралеўстве Нідэрланды (Groot Hertoginnelaan 26, 2517 EG Den Haag). Здзяйсняе дыпламатычныя, консульскія і двухбаковыя сувязі паміж Беларуссю і Нідэрландамі, а таксама прадстаўніцтва пры Арганізацыі па забароне хімічнай зброі (ААЗХЗ / OPCW) у Гаазе.",
            "ru": "Дипломатическое представительство Республики Беларусь в Нидерландах (Groot Hertoginnelaan 26, Гаага). Обеспечивает дипломатические и консульские функции, а также работу при ОЗХО.",
            "en": "Embassy of the Republic of Belarus in the Kingdom of the Netherlands (Groot Hertoginnelaan 26, The Hague). Facilitates bilateral relations and representation to the OPCW."
        },
        "links": [
            {
                "title": "Афіцыйны сайт пасольства ў Нідэрландах",
                "url": "https://netherlands.mfa.gov.by"
            }
        ],
        "tags": [
            "Нідэрланды",
            "Гаага",
            "пасольства",
            "дыпламатыя"
        ],
        "mustSee": False
    },
    {
        "id": "poland-embassy-warsaw",
        "title": {
            "by": "Пасольства Беларусі ў Польшчы (Варшава)",
            "ru": "Посольство Беларуси в Польше (Варшава)",
            "en": "Embassy of Belarus in Poland (Warsaw)"
        },
        "category": "culture",
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
        "coordinates": [
            52.1818,
            21.0772
        ],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Ambasada_Bia%C5%82orusi_w_Warszawie_ul._Wiertnicza_58.jpg/960px-Ambasada_Bia%C5%82orusi_w_Warszawie_ul._Wiertnicza_58.jpg",
        "description": {
            "by": "Афіцыйнае дыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Польшчы (ul. Wiertnicza 58, 02-952 Warszawa). Комплекс будынкаў амбасады ў раёне Віланаў.",
            "ru": "Посольство Республики Беларусь в Республике Польша (ул. Вертнича 58, Варшава).",
            "en": "Embassy of Belarus in Poland, located at ul. Wiertnicza 58 in Warsaw."
        },
        "links": [
            {
                "title": "Афіцыйны сайт пасольства ў Польшчы",
                "url": "https://poland.mfa.gov.by"
            }
        ],
        "tags": [
            "Польшча",
            "Варшава",
            "пасольства",
            "дыпламатыя"
        ],
        "mustSee": False
    },
    {
        "id": "poland-consulate-bialystok",
        "title": {
            "by": "Генеральнае консульства Беларусі ў Беластоку",
            "ru": "Генеральное консульство Беларуси в Белостоке",
            "en": "Consulate General of Belarus in Białystok"
        },
        "category": "culture",
        "country": {
            "by": "Польшча",
            "ru": "Польша",
            "en": "Poland"
        },
        "city": {
            "by": "Беласток",
            "ru": "Белосток",
            "en": "Białystok"
        },
        "coordinates": [
            53.1365,
            23.1415
        ],
        "image": "",
        "description": {
            "by": "Генеральнае консульства Беларусі на Падляшшы (вул. Радзыміньска 9, Беласток / ul. Radzymińska 9, Białystok). Забяспечвае консульскае абслугоўванне грамадзян у Падляскім рэгіёне.",
            "ru": "Генеральное консульство Беларуси в Белостоке (ул. Радзиминьска 9).",
            "en": "Consulate General of Belarus in Białystok, Poland (ul. Radzymińska 9)."
        },
        "links": [
            {
                "title": "Афіцыйны сайт консульства ў Беластоку",
                "url": "https://poland.mfa.gov.by/be/consular_issues/bialystok/"
            }
        ],
        "tags": [
            "Польшча",
            "Беласток",
            "Падляшша",
            "консульства",
            "дыпламатыя"
        ],
        "mustSee": False
    },
    {
        "id": "lithuania-embassy-vilnius",
        "title": {
            "by": "Пасольства Беларусі ў Літве (Вільня)",
            "ru": "Посольство Беларуси в Литве (Вильнюс)",
            "en": "Embassy of Belarus in Lithuania (Vilnius)"
        },
        "category": "culture",
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
        "coordinates": [
            54.6756,
            25.2755
        ],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Embassy_of_Belarus_in_Vilnius.jpg/960px-Embassy_of_Belarus_in_Vilnius.jpg",
        "description": {
            "by": "Дыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Літоўскай Рэспубліцы (Mindaugo g. 13, 03225 Vilnius, раён Наўямесціс).",
            "ru": "Посольство Республики Беларусь в Литве (ул. Миндауго 13, Вильнюс).",
            "en": "Embassy of Belarus in Lithuania (Mindaugo g. 13, Vilnius)."
        },
        "links": [
            {
                "title": "Афіцыйны сайт пасольства ў Літве",
                "url": "https://lithuania.mfa.gov.by"
            }
        ],
        "tags": [
            "Літва",
            "Вільня",
            "пасольства",
            "дыпламатыя"
        ],
        "mustSee": False
    },
    {
        "id": "latvia-embassy-riga",
        "title": {
            "by": "Пасольства Беларусі ў Латвіі (Рыга)",
            "ru": "Посольство Беларуси в Латвии (Рига)",
            "en": "Embassy of Belarus in Latvia (Riga)"
        },
        "category": "culture",
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
        "coordinates": [
            56.9422,
            24.1251
        ],
        "image": "",
        "description": {
            "by": "Пасольства Рэспублікі Беларусь у Латвійскай Рэспубліцы (Jēzusa baznīcas iela 12, LV-1050 Rīga).",
            "ru": "Посольство Республики Беларусь в Латвии (ул. Езусбазницас 12, Рига).",
            "en": "Embassy of Belarus in Latvia (Jēzusa baznīcas iela 12, Riga)."
        },
        "links": [
            {
                "title": "Афіцыйны сайт пасольства ў Латвіі",
                "url": "https://latvia.mfa.gov.by"
            }
        ],
        "tags": [
            "Латвія",
            "Рыга",
            "пасольства",
            "дыпламатыя"
        ],
        "mustSee": False
    },
    {
        "id": "germany-embassy-berlin",
        "title": {
            "by": "Пасольства Беларусі ў Германіі (Берлін)",
            "ru": "Посольство Беларуси в Германии (Берлин)",
            "en": "Embassy of Belarus in Germany (Berlin)"
        },
        "category": "culture",
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
        "coordinates": [
            52.4891,
            13.4682
        ],
        "image": "",
        "description": {
            "by": "Дыпламатычнае прадстаўніцтва Беларусі ў Федэратыўнай Рэспубліцы Германія (Am Treptower Park 32, 12435 Berlin). Будынак размешчаны насупраць Трэптаў-парка.",
            "ru": "Посольство Республики Беларусь в Германии (Am Treptower Park 32, Берлин).",
            "en": "Embassy of Belarus in Germany, located at Am Treptower Park 32, Berlin."
        },
        "links": [
            {
                "title": "Афіцыйны сайт пасольства ў Германіі",
                "url": "https://germany.mfa.gov.by"
            }
        ],
        "tags": [
            "Германія",
            "Берлін",
            "пасольства",
            "дыпламатыя"
        ],
        "mustSee": False
    },
    {
        "id": "france-embassy-paris",
        "title": {
            "by": "Пасольства Беларусі ў Францыі (Парыж)",
            "ru": "Посольство Беларуси во Франции (Париж)",
            "en": "Embassy of Belarus in France (Paris)"
        },
        "category": "culture",
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
        "coordinates": [
            48.8522,
            2.2612
        ],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Ambassade_de_Bi%C3%A9lorussie_en_France%2C_38_boulevard_Suchet%2C_Paris_16e_2.jpg/960px-Ambassade_de_Bi%C3%A9lorussie_en_France%2C_38_boulevard_Suchet%2C_Paris_16e_2.jpg",
        "description": {
            "by": "Пасольства Рэспублікі Беларусь у Французскай Рэспубліцы (38 Boulevard Suchet, 75016 Paris, 16-я акруга Парыжа ля Булонскага лесу). Таксама з'яўляецца пастаянным прадстаўніцтвам Беларусі пры ЮНЕСКА.",
            "ru": "Посольство Беларуси во Франции и постоянное представительство при ЮНЕСКО (38 Boulevard Suchet, Париж).",
            "en": "Embassy of Belarus in France and permanent delegation to UNESCO, situated at 38 Boulevard Suchet in the 16th arrondissement of Paris."
        },
        "links": [
            {
                "title": "Афіцыйны сайт пасольства ў Францыі",
                "url": "https://france.mfa.gov.by"
            }
        ],
        "tags": [
            "Францыя",
            "Парыж",
            "пасольства",
            "ЮНЕСКА",
            "дыпламатыя"
        ],
        "mustSee": False
    },
    {
        "id": "uk-embassy-london",
        "title": {
            "by": "Пасольства Беларусі ў Вялікабрытаніі (Лондан)",
            "ru": "Посольство Беларуси в Великобритании (Лондон)",
            "en": "Embassy of Belarus in the United Kingdom (London)"
        },
        "category": "culture",
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
        "coordinates": [
            51.5015,
            -0.1887
        ],
        "image": "",
        "description": {
            "by": "Дыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Злучаным Каралеўстве Вялікабрытаніі і Паўночнай Ірландыі (6 Kensington Court, London W8 5DL, раён Кенсінгтан).",
            "ru": "Посольство Республики Беларусь в Великобритании (6 Kensington Court, Лондон).",
            "en": "Embassy of Belarus in the United Kingdom (6 Kensington Court, London W8 5DL)."
        },
        "links": [
            {
                "title": "Афіцыйны сайт пасольства ў Вялікабрытаніі",
                "url": "https://uk.mfa.gov.by"
            }
        ],
        "tags": [
            "Вялікабрытанія",
            "Лондан",
            "пасольства",
            "дыпламатыя"
        ],
        "mustSee": False
    },
    {
        "id": "usa-embassy-washington",
        "title": {
            "by": "Пасольства Беларусі ў ЗША (Вашынгтон)",
            "ru": "Посольство Беларуси в США (Вашингтон)",
            "en": "Embassy of Belarus in the United States (Washington, D.C.)"
        },
        "category": "culture",
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
        "coordinates": [
            38.9118,
            -77.0422
        ],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Embassy_of_Belarus.jpg/960px-Embassy_of_Belarus.jpg",
        "description": {
            "by": "Дыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Злучаных Штатах Амерыкі (1619 New Hampshire Ave NW, Washington, DC 20009, раён Dupont Circle).",
            "ru": "Посольство Республики Беларусь в США (1619 New Hampshire Ave NW, Вашингтон).",
            "en": "Embassy of Belarus in the United States, located at 1619 New Hampshire Ave NW, Washington, D.C."
        },
        "links": [
            {
                "title": "Афіцыйны сайт пасольства ў ЗША",
                "url": "https://usa.mfa.gov.by"
            }
        ],
        "tags": [
            "ЗША",
            "Вашынгтон",
            "пасольства",
            "дыпламатыя"
        ],
        "mustSee": False
    },
    {
        "id": "un-mission-new-york",
        "title": {
            "by": "Пастаяннае прадстаўніцтва Беларусі пры ААН (Нью-Ёрк)",
            "ru": "Постоянное представительство Беларуси при ООН (Нью-Йорк)",
            "en": "Permanent Mission of Belarus to the United Nations (New York)"
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
            40.7675,
            -73.9641
        ],
        "image": "",
        "description": {
            "by": "Пастаяннае прадстаўніцтва Рэспублікі Беларусь пры Арганізацыі Аб'яднаных Нацый (136 E 67th St, New York, NY 10065, Манхэтэн). Беларусь з'яўляецца адной з дзяржаў-заснавальніц ААН з 1945 года.",
            "ru": "Постоянное представительство Беларуси при ООН (136 E 67th St, Нью-Йорк). Беларусь — государство-основатель ООН с 1945 года.",
            "en": "Permanent Mission of Belarus to the United Nations (136 E 67th St, Manhattan, New York). Belarus is an original founding member state of the UN since 1945."
        },
        "links": [
            {
                "title": "Афіцыйны сайт прадстаўніцтва пры ААН",
                "url": "https://un.mfa.gov.by"
            }
        ],
        "tags": [
            "ЗША",
            "Нью-Ёрк",
            "ААН",
            "дыпламатыя"
        ],
        "mustSee": False
    },
    {
        "id": "belgium-embassy-brussels",
        "title": {
            "by": "Пасольства Беларусі ў Бельгіі і прадстаўніцтва пры ЕС (Брусель)",
            "ru": "Посольство Беларуси в Бельгии и миссия при ЕС (Брюссель)",
            "en": "Embassy of Belarus in Belgium & Mission to EU (Brussels)"
        },
        "category": "culture",
        "country": {
            "by": "Бельгія",
            "ru": "Бельгия",
            "en": "Belgium"
        },
        "city": {
            "by": "Брусель",
            "ru": "Брюссель",
            "en": "Brussels"
        },
        "coordinates": [
            50.8168,
            4.3541
        ],
        "image": "",
        "description": {
            "by": "Дыпламатычнае прадстаўніцтва Беларусі ў Каралеўстве Бельгія і пастаяннае прадстаўніцтва пры Еўрапейскім Саюзе (Avenue Molière 192, 1050 Ixelles, Bruxelles).",
            "ru": "Посольство Республики Беларусь в Бельгии и постоянное представительство при ЕС (Avenue Molière 192, Брюссель).",
            "en": "Embassy of Belarus in Belgium and Permanent Mission to the European Union (Avenue Molière 192, Brussels)."
        },
        "links": [
            {
                "title": "Афіцыйны сайт пасольства ў Бельгіі",
                "url": "https://belgium.mfa.gov.by"
            }
        ],
        "tags": [
            "Бельгія",
            "Брусель",
            "пасольства",
            "ЕС",
            "дыпламатыя"
        ],
        "mustSee": False
    },
    {
        "id": "austria-embassy-vienna",
        "title": {
            "by": "Пасольства Беларусі ў Аўстрыі і пры АБСЕ (Вена)",
            "ru": "Посольство Беларуси в Австрии и при ОБСЕ (Вена)",
            "en": "Embassy of Belarus in Austria & Mission to OSCE (Vienna)"
        },
        "category": "culture",
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
        "coordinates": [
            48.2091,
            16.2552
        ],
        "image": "",
        "description": {
            "by": "Пасольства Рэспублікі Беларусь у Аўстрыі і пастаяннае прадстаўніцтва пры АБСЕ і міжнародных арганізацыях у Вене (Hüttelbergstraße 6, 1140 Wien).",
            "ru": "Посольство Республики Беларусь в Австрии и постоянное представительство при ОБСЕ (Hüttelbergstraße 6, Вена).",
            "en": "Embassy of Belarus in Austria and Permanent Mission to the OSCE and international organizations in Vienna."
        },
        "links": [
            {
                "title": "Афіцыйны сайт пасольства ў Аўстрыі",
                "url": "https://austria.mfa.gov.by"
            }
        ],
        "tags": [
            "Аўстрыя",
            "Вена",
            "пасольства",
            "АБСЕ",
            "дыпламатыя"
        ],
        "mustSee": False
    },
    {
        "id": "switzerland-embassy-bern",
        "title": {
            "by": "Пасольства Беларусі ў Швейцарыі (Берн)",
            "ru": "Посольство Беларуси в Швейцарии (Берн)",
            "en": "Embassy of Belarus in Switzerland (Bern)"
        },
        "category": "culture",
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
        "coordinates": [
            46.9366,
            7.4883
        ],
        "image": "",
        "description": {
            "by": "Дыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Швейцарскай Канфедэрацыі (Quartierweg 6, 3074 Muri bei Bern).",
            "ru": "Посольство Республики Беларусь в Швейцарии (Quartierweg 6, Мури-бай-Берн).",
            "en": "Embassy of Belarus in Switzerland, located at Quartierweg 6 in Muri bei Bern."
        },
        "links": [
            {
                "title": "Афіцыйны сайт пасольства ў Швейцарыі",
                "url": "https://switzerland.mfa.gov.by"
            }
        ],
        "tags": [
            "Швейцарыя",
            "Берн",
            "пасольства",
            "дыпламатыя"
        ],
        "mustSee": False
    },
    {
        "id": "czech-embassy-prague",
        "title": {
            "by": "Пасольства Беларусі ў Чэхіі (Прага)",
            "ru": "Посольство Беларуси в Чехии (Прага)",
            "en": "Embassy of Belarus in the Czech Republic (Prague)"
        },
        "category": "culture",
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
        "coordinates": [
            50.1171,
            14.4259
        ],
        "image": "",
        "description": {
            "by": "Дыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Чэшскай Рэспубліцы (Sádky 626, 171 00 Praha-Troja).",
            "ru": "Посольство Республики Беларусь в Чехии (Sádky 626, Прага-Троя).",
            "en": "Embassy of Belarus in the Czech Republic (Sádky 626, Praha-Troja)."
        },
        "links": [
            {
                "title": "Афіцыйны сайт пасольства ў Чэхіі",
                "url": "https://czech.mfa.gov.by"
            }
        ],
        "tags": [
            "Чэхія",
            "Прага",
            "пасольства",
            "дыпламатыя"
        ],
        "mustSee": False
    },
    {
        "id": "italy-embassy-rome",
        "title": {
            "by": "Пасольства Беларусі ў Італіі (Рым)",
            "ru": "Посольство Беларуси в Италии (Рим)",
            "en": "Embassy of Belarus in Italy (Rome)"
        },
        "category": "culture",
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
        "coordinates": [
            41.8344,
            12.4936
        ],
        "image": "",
        "description": {
            "by": "Дыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Італьянскай Рэспубліцы (Via Luigi Girolamo Gattoni 8, 00142 Roma). Таксама пастаяннае прадстаўніцтва пры ФАО (FAO).",
            "ru": "Посольство Республики Беларусь в Италии (Via Luigi Girolamo Gattoni 8, Рим).",
            "en": "Embassy of Belarus in Italy and Permanent Representation to FAO (Via Luigi Girolamo Gattoni 8, Rome)."
        },
        "links": [
            {
                "title": "Афіцыйны сайт пасольства ў Італіі",
                "url": "https://italy.mfa.gov.by"
            }
        ],
        "tags": [
            "Італія",
            "Рым",
            "пасольства",
            "дыпламатыя"
        ],
        "mustSee": False
    },
    {
        "id": "china-embassy-beijing",
        "title": {
            "by": "Пасольства Беларусі ў Кітаі (Пекін)",
            "ru": "Посольство Беларуси в Китае (Пекин)",
            "en": "Embassy of Belarus in China (Beijing)"
        },
        "category": "culture",
        "country": {
            "by": "Кітай",
            "ru": "Китай",
            "en": "China"
        },
        "city": {
            "by": "Пекін",
            "ru": "Пекин",
            "en": "Beijing"
        },
        "coordinates": [
            39.9388,
            116.4522
        ],
        "image": "",
        "description": {
            "by": "Дыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Кітайскай Народнай Рэспубліцы (No. 1, Dong Yi Jie, San Li Tun, Chaoyang District, Beijing).",
            "ru": "Посольство Республики Беларусь в КНР (район Чаоян, Пекин).",
            "en": "Embassy of Belarus in the People's Republic of China, Chaoyang District, Beijing."
        },
        "links": [
            {
                "title": "Афіцыйны сайт пасольства ў Кітаі",
                "url": "https://china.mfa.gov.by"
            }
        ],
        "tags": [
            "Кітай",
            "Пекін",
            "пасольства",
            "дыпламатыя"
        ],
        "mustSee": False
    },
    {
        "id": "israel-embassy-tel-aviv",
        "title": {
            "by": "Пасольства Беларусі ў Ізраілі (Тэль-Авіў)",
            "ru": "Посольство Беларуси в Израиле (Тель-Авив)",
            "en": "Embassy of Belarus in Israel (Tel Aviv)"
        },
        "category": "culture",
        "country": {
            "by": "Ізраіль",
            "ru": "Израиль",
            "en": "Israel"
        },
        "city": {
            "by": "Тэль-Авіў",
            "ru": "Тель-Авив",
            "en": "Tel Aviv"
        },
        "coordinates": [
            32.0838,
            34.7735
        ],
        "image": "",
        "description": {
            "by": "Дыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Дзяржаве Ізраіль (Rehov Beilinson 3, Tel Aviv 6435103). Звязвае Беларусь са шматтысячнай супольнасцю выхадцаў з Беларусі ў Ізраілі.",
            "ru": "Посольство Республики Беларусь в Государстве Израиль (ул. Бейлинсон 3, Тель-Авив).",
            "en": "Embassy of Belarus in the State of Israel (Rehov Beilinson 3, Tel Aviv)."
        },
        "links": [
            {
                "title": "Афіцыйны сайт пасольства ў Ізраілі",
                "url": "https://israel.mfa.gov.by"
            }
        ],
        "tags": [
            "Ізраіль",
            "Тэль-Авіў",
            "пасольства",
            "дыпламатыя"
        ],
        "mustSee": False
    }
]

def run():
    with open('data/places.json', 'r', encoding='utf-8') as f:
        places = json.load(f)
    
    existing_ids = {p['id'] for p in places}
    added_count = 0
    for ep in embassy_places:
        if ep['id'] not in existing_ids:
            places.append(ep)
            existing_ids.add(ep['id'])
            added_count += 1
            
    print(f"Added {added_count} new places (Netherlands & Embassies). Total places: {len(places)}")
    
    with open('data/places.json', 'w', encoding='utf-8') as f:
        json.dump(places, f, ensure_ascii=False, indent=2)
        
    with open('data/places.js', 'w', encoding='utf-8') as f:
        f.write('window.INITIAL_PLACES = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

if __name__ == '__main__':
    run()
