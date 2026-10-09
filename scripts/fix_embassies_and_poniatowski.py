import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def run():
    with open('data/places.json', 'r', encoding='utf-8') as f:
        places = json.load(f)

    print(f"Initial places count: {len(places)}")

    # 1. Official Embassies to remove duplicates and normalize
    # We will remove old duplicate IDs:
    to_remove = {
        'poland-embassy-warsaw',
        'lithuania-embassy-vilnius',
        'latvia-embassy-riga',
        'germany-embassy-berlin',
        'france-embassy-paris',
        'london-embassy-belarus',      # keep uk-embassy-london
        'usa-embassy-washington',        # keep washington-embassy-belarus
        'austria-embassy-vienna',        # keep vienna-embassy-belarus
        'switzerland-embassy-bern',      # keep bern-embassy-belarus
        'italy-embassy-rome',            # keep rome-embassy-belarus
    }

    places = [p for p in places if p['id'] not in to_remove]
    print(f"Places count after removing 10 duplicate embassy entries: {len(places)}")

    # Update canonical embassy entries with 100% verified addresses and OSM building coords
    embassy_updates = {
        'rome-embassy-belarus': {
            'coordinates': [41.936622, 12.536815],
            'category': 'embassy',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Ambasciata_di_Bielorussia_Roma.jpg/960px-Ambasciata_di_Bielorussia_Roma.jpg' if False else 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Roma_Via_Nomentana_01.jpg/960px-Roma_Via_Nomentana_01.jpg',
            'wiki': 'https://be.wikipedia.org/wiki/Пасольства_Беларусі_ў_Італіі',
            'description': {
                'by': 'Афіцыйнае дыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Італьянскай Рэспубліцы.\n\nАдрас: Via delle Alpi Apuane, 16, 00141 Roma, Італія (Консульскі аддзел: Via Gazza, 10).',
                'ru': 'Официальное дипломатическое представительство Республики Беларусь в Итальянской Республике.\n\nАдрес: Via delle Alpi Apuane, 16, 00141 Roma, Италия (Консульский отдел: Via Gazza, 10).',
                'en': 'Embassy of the Republic of Belarus in the Italian Republic.\n\nAddress: Via delle Alpi Apuane, 16, 00141 Rome, Italy (Consular section: Via Gazza, 10).'
            },
            'links': [
                {'title': 'Афіцыйны сайт: Пасольства Беларусі ў Італіі', 'url': 'https://italy.mfa.gov.by'},
                {'title': 'Вікіпедыя: Пасольства Беларусі ў Італіі', 'url': 'https://be.wikipedia.org/wiki/Пасольства_Беларусі_ў_Італіі'}
            ]
        },
        'uk-embassy-london': {
            'id': 'uk-embassy-london',
            'title': {
                'by': 'Пасольства Беларусі ў Вялікабрытаніі (Лондан)',
                'ru': 'Посольство Беларуси в Великобритании (Лондон)',
                'en': 'Embassy of Belarus in the United Kingdom (London)'
            },
            'category': 'embassy',
            'country': {'by': 'Вялікабрытанія', 'ru': 'Великобритания', 'en': 'United Kingdom'},
            'city': {'by': 'Лондан', 'ru': 'Лондон', 'en': 'London'},
            'coordinates': [51.501599, -0.186803],
            'description': {
                'by': 'Афіцыйнае дыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Злучаным Каралеўстве Вялікабрытаніі і Паўночнай Ірландыі.\n\nАдрас: 6 Kensington Court, London W8 5DL, Вялікабрытанія.',
                'ru': 'Официальное дипломатическое представительство Республики Беларусь в Соединённом Королевстве Великобритании и Северной Ирландии.\n\nАдрес: 6 Kensington Court, London W8 5DL, Великобритания.',
                'en': 'Embassy of the Republic of Belarus in the United Kingdom of Great Britain and Northern Ireland.\n\nAddress: 6 Kensington Court, London W8 5DL, United Kingdom.'
            },
            'links': [
                {'title': 'Афіцыйны сайт: Пасольства Беларусі ў Вялікабрытаніі', 'url': 'https://uk.mfa.gov.by'},
                {'title': 'Вікіпедыя: Пасольства Беларусі ў Вялікабрытаніі', 'url': 'https://be.wikipedia.org/wiki/Пасольства_Беларусі_ў_Вялікабрытаніі'}
            ]
        },
        'warsaw-embassy-belarus': {
            'coordinates': [52.171814, 21.081903],
            'category': 'embassy',
            'description': {
                'by': 'Афіцыйнае дыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Рэспубліцы Польшча.\n\nАдрас: ul. Wiertnicza 58, 02-952 Warszawa, Польшча.',
                'ru': 'Официальное дипломатическое представительство Республики Беларусь в Республике Польша.\n\nАдрес: ul. Wiertnicza 58, 02-952 Warszawa, Польша.',
                'en': 'Embassy of the Republic of Belarus in the Republic of Poland.\n\nAddress: ul. Wiertnicza 58, 02-952 Warsaw, Poland.'
            },
            'links': [
                {'title': 'Афіцыйны сайт: Пасольства Беларусі ў Польшчы', 'url': 'https://poland.mfa.gov.by'},
                {'title': 'Вікіпедыя: Пасольства Беларусі ў Польшчы', 'url': 'https://be.wikipedia.org/wiki/Пасольства_Беларусі_ў_Польшчы'}
            ]
        },
        'vilnius-embassy-belarus': {
            'coordinates': [54.677235, 25.273211],
            'category': 'embassy',
            'description': {
                'by': 'Афіцыйнае дыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Літоўскай Рэспубліцы.\n\nАдрас: Mindaugo g. 13, LT-03225 Vilnius, Літва.',
                'ru': 'Официальное дипломатическое представительство Республики Беларусь в Литовской Республике.\n\nАдрес: Mindaugo g. 13, LT-03225 Vilnius, Литва.',
                'en': 'Embassy of the Republic of Belarus in the Republic of Lithuania.\n\nAddress: Mindaugo g. 13, LT-03225 Vilnius, Lithuania.'
            },
            'links': [
                {'title': 'Афіцыйны сайт: Пасольства Беларусі ў Літве', 'url': 'https://lithuania.mfa.gov.by'},
                {'title': 'Вікіпедыя: Пасольства Беларусі ў Літве', 'url': 'https://be.wikipedia.org/wiki/Пасольства_Беларусі_ў_Літве'}
            ]
        },
        'riga-embassy-belarus': {
            'coordinates': [56.941857, 24.124804],
            'category': 'embassy',
            'description': {
                'by': 'Афіцыйнае дыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Латвійскай Рэспубліцы.\n\nАдрас: Jēzusbaznīcas iela 12, Rīga, LV-1050, Латвія.',
                'ru': 'Официальное дипломатическое представительство Республики Беларусь в Латвийской Республике.\n\nАдрес: Jēzusbaznīcas iela 12, Rīga, LV-1050, Латвия.',
                'en': 'Embassy of the Republic of Belarus in the Republic of Latvia.\n\nAddress: Jēzusbaznīcas iela 12, Rīga, LV-1050, Latvia.'
            },
            'links': [
                {'title': 'Афіцыйны сайт: Пасольства Беларусі ў Латвіі', 'url': 'https://latvia.mfa.gov.by'},
                {'title': 'Вікіпедыя: Пасольства Беларусі ў Латвіі', 'url': 'https://be.wikipedia.org/wiki/Пасольства_Беларусі_ў_Латвіі'}
            ]
        },
        'berlin-embassy-belarus': {
            'coordinates': [52.487039, 13.463744],
            'category': 'embassy',
            'description': {
                'by': 'Афіцыйнае дыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Федэратыўнай Рэспубліцы Германія.\n\nАдрас: Am Treptower Park 32, 12435 Berlin, Германія.',
                'ru': 'Официальное дипломатическое представительство Республики Беларусь в Федеративной Республике Германия.\n\nАдрес: Am Treptower Park 32, 12435 Berlin, Германия.',
                'en': 'Embassy of the Republic of Belarus in the Federal Republic of Germany.\n\nAddress: Am Treptower Park 32, 12435 Berlin, Germany.'
            },
            'links': [
                {'title': 'Афіцыйны сайт: Пасольства Беларусі ў Германіі', 'url': 'https://germany.mfa.gov.by'},
                {'title': 'Вікіпедыя: Пасольства Беларусі ў Германіі', 'url': 'https://be.wikipedia.org/wiki/Пасольства_Беларусі_ў_Германіі'}
            ]
        },
        'paris-embassy-belarus': {
            'coordinates': [48.858080, 2.264716],
            'category': 'embassy',
            'description': {
                'by': 'Афіцыйнае дыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Французскай Рэспубліцы.\n\nАдрас: 38 Boulevard Suchet, 75016 Paris, Францыя.',
                'ru': 'Официальное дипломатическое представительство Республики Беларусь во Французской Республике.\n\nАдрес: 38 Boulevard Suchet, 75016 Paris, Франция.',
                'en': 'Embassy of the Republic of Belarus in the French Republic.\n\nAddress: 38 Boulevard Suchet, 75016 Paris, France.'
            },
            'links': [
                {'title': 'Афіцыйны сайт: Пасольства Беларусі ў Францыі', 'url': 'https://france.mfa.gov.by'},
                {'title': 'Вікіпедыя: Пасольства Беларусі ў Францыі', 'url': 'https://be.wikipedia.org/wiki/Пасольства_Беларусі_ў_Францыі'}
            ]
        },
        'washington-embassy-belarus': {
            'coordinates': [38.912135, -77.040722],
            'category': 'embassy',
            'description': {
                'by': 'Афіцыйнае дыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Злучаных Штатах Амерыкі.\n\nАдрас: 1619 New Hampshire Ave NW, Washington, DC 20009, ЗША.',
                'ru': 'Официальное дипломатическое представительство Республики Беларусь в Соединённых Штатах Америки.\n\nАдрес: 1619 New Hampshire Ave NW, Washington, DC 20009, США.',
                'en': 'Embassy of the Republic of Belarus in the United States of America.\n\nAddress: 1619 New Hampshire Ave NW, Washington, DC 20009, USA.'
            },
            'links': [
                {'title': 'Афіцыйны сайт: Пасольства Беларусі ў ЗША', 'url': 'https://usa.mfa.gov.by'},
                {'title': 'Вікіпедыя: Пасольства Беларусі ў ЗША', 'url': 'https://be.wikipedia.org/wiki/Пасольства_Беларусі_ў_ЗША'}
            ]
        },
        'vienna-embassy-belarus': {
            'coordinates': [48.203076, 16.257568],
            'category': 'embassy',
            'description': {
                'by': 'Афіцыйнае дыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Аўстрыйскай Рэспубліцы і пры міжнародных арганізацыях у Вене (АБСЕ).\n\nАдрас: Hüttelbergstraße 6, 1140 Wien, Аўстрыя.',
                'ru': 'Официальное дипломатическое представительство Республики Беларусь в Австрийской Республике и при ОБСЕ.\n\nАдрес: Hüttelbergstraße 6, 1140 Wien, Австрия.',
                'en': 'Embassy of the Republic of Belarus in the Republic of Austria and Permanent Mission to the OSCE.\n\nAddress: Hüttelbergstraße 6, 1140 Vienna, Austria.'
            },
            'links': [
                {'title': 'Афіцыйны сайт: Пасольства Беларусі ў Аўстрыі', 'url': 'https://austria.mfa.gov.by'},
                {'title': 'Вікіпедыя: Пасольства Беларусі ў Аўстрыі', 'url': 'https://be.wikipedia.org/wiki/Пасольства_Беларусі_ў_Аўстрыі'}
            ]
        },
        'bern-embassy-belarus': {
            'coordinates': [46.933818, 7.488585],
            'category': 'embassy',
            'description': {
                'by': 'Афіцыйнае дыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Швейцарскай Канфедэрацыі.\n\nАдрас: Quartierweg 6, 3074 Muri bei Bern, Швейцарыя.',
                'ru': 'Официальное дипломатическое представительство Республики Беларусь в Швейцарской Конфедерации.\n\nАдрес: Quartierweg 6, 3074 Muri bei Bern, Швейцария.',
                'en': 'Embassy of the Republic of Belarus in the Swiss Confederation.\n\nAddress: Quartierweg 6, 3074 Muri bei Bern, Switzerland.'
            },
            'links': [
                {'title': 'Афіцыйны сайт: Пасольства Беларусі ў Швейцарыі', 'url': 'https://switzerland.mfa.gov.by'},
                {'title': 'Вікіпедыя: Пасольства Беларусі ў Швейцарыі', 'url': 'https://be.wikipedia.org/wiki/Пасольства_Беларусі_ў_Швейцарыі'}
            ]
        },
        'ankara-embassy-belarus': {
            'coordinates': [39.882758, 32.854778],
            'category': 'embassy',
            'description': {
                'by': 'Афіцыйнае дыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Турэцкай Рэспубліцы.\n\nАдрас: Abidin Daver Sk. No: 17, 06550 Çankaya, Ankara, Турцыя.',
                'ru': 'Официальное дипломатическое представительство Республики Беларусь в Турецкой Республике.\n\nАдрес: Abidin Daver Sk. No: 17, 06550 Çankaya, Ankara, Турция.',
                'en': 'Embassy of the Republic of Belarus in the Republic of Turkey.\n\nAddress: Abidin Daver Sk. No: 17, 06550 Çankaya, Ankara, Turkey.'
            },
            'links': [
                {'title': 'Афіцыйны сайт: Пасольства Беларусі ў Турцыі', 'url': 'https://turkey.mfa.gov.by'},
                {'title': 'Вікіпедыя: Пасольства Беларусі ў Турцыі', 'url': 'https://be.wikipedia.org/wiki/Пасольства_Беларусі_ў_Турцыі'}
            ]
        },
        'istanbul-consulate-belarus': {
            'coordinates': [40.975858, 28.797842],
            'category': 'embassy',
            'description': {
                'by': 'Генеральнае консульства Рэспублікі Беларусь у Стамбуле.\n\nАдрас: Germeyan Sk. No: 1, Florya, Şenlikköy Mah., Bakırköy, İstanbul, Турцыя.',
                'ru': 'Генеральное консульство Республики Беларусь в Стамбуле.\n\nАдрес: Germeyan Sk. No: 1, Florya, Şenlikköy Mah., Bakırköy, İstanbul, Турция.',
                'en': 'Consulate General of the Republic of Belarus in Istanbul.\n\nAddress: Germeyan Sk. No: 1, Florya, Şenlikköy Mah., Bakırköy, Istanbul, Turkey.'
            },
            'links': [
                {'title': 'Афіцыйны сайт: Генконсульства Беларусі ў Стамбуле', 'url': 'https://istanbul.mfa.gov.by'}
            ]
        },
        'un-mission-new-york': {
            'coordinates': [40.766678, -73.963590],
            'category': 'embassy',
            'description': {
                'by': 'Пастаяннае прадстаўніцтва Рэспублікі Беларусь пры Арганізацыі Аб’яднаных Нацый у Нью-Ёрку.\n\nАдрас: 136 E 67th St, New York, NY 10065, ЗША.',
                'ru': 'Постоянное представительство Республики Беларусь при Организации Объединенных Наций в Нью-Йорке.\n\nАдрес: 136 E 67th St, New York, NY 10065, США.',
                'en': 'Permanent Mission of the Republic of Belarus to the United Nations in New York.\n\nAddress: 136 E 67th St, New York, NY 10065, USA.'
            },
            'links': [
                {'title': 'Афіцыйны сайт: Прадстаўніцтва Беларусі пры ААН', 'url': 'https://un.mfa.gov.by'}
            ]
        },
        'netherlands-embassy-hague': {
            'coordinates': [52.085014, 4.288465],
            'category': 'embassy',
            'description': {
                'by': 'Афіцыйнае дыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Каралеўстве Нідэрланды.\n\nАдрас: Groot Hertoginnelaan 26, 2517 EG Den Haag, Нідэрланды.',
                'ru': 'Официальное дипломатическое представительство Республики Беларусь в Королевстве Нидерландов.\n\nАдрес: Groot Hertoginnelaan 26, 2517 EG Den Haag, Нидерланды.',
                'en': 'Embassy of the Republic of Belarus in the Kingdom of the Netherlands.\n\nAddress: Groot Hertoginnelaan 26, 2517 EG The Hague, Netherlands.'
            },
            'links': [
                {'title': 'Афіцыйны сайт: Пасольства Беларусі ў Нідэрландах', 'url': 'https://netherlands.mfa.gov.by'}
            ]
        },
        'belgium-embassy-brussels': {
            'coordinates': [50.815661, 4.354170],
            'category': 'embassy',
            'description': {
                'by': 'Афіцыйнае дыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Каралеўстве Бельгія і Пастаяннае прадстаўніцтва пры ЕС.\n\nАдрас: Avenue Molière 192, 1050 Ixelles, Брусель, Бельгія.',
                'ru': 'Официальное дипломатическое представительство Республики Беларусь в Королевстве Бельгия и представительство при ЕС.\n\nАдрес: Avenue Molière 192, 1050 Ixelles, Брюссель, Бельгия.',
                'en': 'Embassy of the Republic of Belarus in the Kingdom of Belgium and Mission to the EU.\n\nAddress: Avenue Molière 192, 1050 Ixelles, Brussels, Belgium.'
            },
            'links': [
                {'title': 'Афіцыйны сайт: Пасольства Беларусі ў Бельгіі', 'url': 'https://belgium.mfa.gov.by'}
            ]
        },
        'czech-embassy-prague': {
            'coordinates': [50.116431, 14.420674],
            'category': 'embassy',
            'description': {
                'by': 'Афіцыйнае дыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Чэшскай Рэспубліцы.\n\nАдрас: Sádky 326/2, Troja, 171 00 Praha 7, Чэхія.',
                'ru': 'Официальное дипломатическое представительство Республики Беларусь в Чешской Республике.\n\nАдрес: Sádky 326/2, Troja, 171 00 Praha 7, Чехия.',
                'en': 'Embassy of the Republic of Belarus in the Czech Republic.\n\nAddress: Sádky 326/2, Troja, 171 00 Prague 7, Czech Republic.'
            },
            'links': [
                {'title': 'Афіцыйны сайт: Пасольства Беларусі ў Чэхіі', 'url': 'https://czech.mfa.gov.by'}
            ]
        },
        'china-embassy-beijing': {
            'coordinates': [39.913181, 116.441042],
            'category': 'embassy',
            'description': {
                'by': 'Афіцыйнае дыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Кітайскай Народнай Рэспубліцы.\n\nАдрас: No. 1, Dong Yi Jie, Ri Tan Lu, Chaoyang District, Beijing, 100600, Кітай (朝阳区日坛东二街1号).',
                'ru': 'Официальное дипломатическое представительство Республики Беларусь в Китайской Народной Республике.\n\nАдрес: No. 1, Dong Yi Jie, Ri Tan Lu, Chaoyang District, Beijing, 100600, Китай.',
                'en': 'Embassy of the Republic of Belarus in the People’s Republic of China.\n\nAddress: No. 1, Dong Yi Jie, Ri Tan Lu, Chaoyang District, Beijing, 100600, China.'
            },
            'links': [
                {'title': 'Афіцыйны сайт: Пасольства Беларусі ў Кітаі', 'url': 'https://china.mfa.gov.by'}
            ]
        },
        'israel-embassy-tel-aviv': {
            'coordinates': [32.074586, 34.783265],
            'category': 'embassy',
            'description': {
                'by': 'Афіцыйнае дыпламатычнае прадстаўніцтва Рэспублікі Беларусь у Дзяржаве Ізраіль.\n\nАдрас: Rehov Daniel Frisch 3, Tel Aviv-Yafo, 6473104, Ізраіль.',
                'ru': 'Официальное дипломатическое представительство Республики Беларусь в Государстве Израиль.\n\nАдрес: Rehov Daniel Frisch 3, Tel Aviv-Yafo, 6473104, Израиль.',
                'en': 'Embassy of the Republic of Belarus in the State of Israel.\n\nAddress: Rehov Daniel Frisch 3, Tel Aviv-Yafo, 6473104, Israel.'
            },
            'links': [
                {'title': 'Афіцыйны сайт: Пасольства Беларусі ў Ізраілі', 'url': 'https://israel.mfa.gov.by'}
            ]
        }
    }

    for p in places:
        pid = p['id']
        if pid in embassy_updates:
            u = embassy_updates[pid]
            for k, v in u.items():
                p[k] = v

    # 2. Update Lytham Hall and Chagall with explicit sources in links
    for p in places:
        if p['id'] == 'lytham-hall-belarusian-timber':
            p['links'] = [
                {
                    'title': 'Наша Ніва: У ангельскім палацы знайшлі беларускі лес',
                    'url': 'https://nashaniva.com/378830'
                },
                {
                    'title': 'Вікіпедыя: Lytham Hall (Grade I listed country house)',
                    'url': 'https://en.wikipedia.org/wiki/Lytham_Hall'
                }
            ]
        elif p['id'] == 'reims-cathedral-chagall-stained-glass':
            p['links'] = [
                {
                    'title': 'Наша Ніва: У Рэймскім саборы пра Марка Шагала пішуць нісянеціцу',
                    'url': 'https://nashaniva.com/399979'
                },
                {
                    'title': 'Marc Chagall: Catalogue raisonné des vitraux',
                    'url': 'https://www.marcchagall.com/fr/catalogue-raisonne'
                },
                {
                    'title': 'Вікіпедыя: Рэймскі сабор (Cathedrale Notre-Dame de Reims)',
                    'url': 'https://be.wikipedia.org/wiki/Рэймскі_сабор'
                }
            ]
        elif p['id'] == 'warsaw-bulak-balachowicz-plaque':
            p['links'] = [
                {
                    'title': 'Хартыя\'97: У Варшаве адкрылі дошку генералу Булак-Балаховічу',
                    'url': 'https://charter97.org/ru/news/2009/5/11/18042/'
                },
                {
                    'title': 'Радыё Рацыя: У Варшаве ўшанавалі памяць Станіслава Булак-Балаховіча',
                    'url': 'https://racyja.com/by/sumezza/u-varsav-usanavali-pamjac-stanislava-bulak-bulachovica/'
                },
                {
                    'title': 'Polskie Radio: Tablica gen. Stanisława Bułak-Bałachowicza',
                    'url': 'https://www2.polskieradio.pl/eo/print.aspx?iid=107917'
                }
            ]

    # 3. Add Volchyn Holy Trinity Church and St. Petersburg St. Catherine Basilica
    existing_ids = {p['id'] for p in places}

    volchyn_id = 'volchyn-holy-trinity-church-poniatowski'
    if volchyn_id not in existing_ids:
        places.append({
            'id': volchyn_id,
            'title': {
                'by': 'Касцёл Найсвяцейшай Тройцы ў Воўчыне — Месца нараджэння і перапахавання Станіслава Аўгуста Панятоўскага',
                'ru': 'Костёл Святой Троицы в Волчине — Место рождения и перезахоронения Станислава Августа Понятовского',
                'en': 'Holy Trinity Church in Voŭčyn — Birthplace and Reburial of King Stanisław August Poniatowski'
            },
            'category': 'church',
            'country': {
                'by': 'Беларусь',
                'ru': 'Беларусь',
                'en': 'Belarus'
            },
            'city': {
                'by': 'Воўчын',
                'ru': 'Волчин',
                'en': 'Voŭčyn'
            },
            'coordinates': [52.285808, 23.310356],
            'image': 'https://upload.wikimedia.org/wikipedia/commons/d/d9/%D0%92%D0%BE%D1%9E%D1%87%D1%8B%D0%BD_Vo%C5%AD%C4%8Dyn_%282021%29_01.jpg',
            'description': {
                'by': 'Адрас: вул. Леніна, 45А, в. Воўчын, Камянецкі раён, Брэсцкая вобласць.\n\nШэдэўр барока і ракако XVIII ст., збудаваны пад кіраўніцтвам архітэктара Яна Баптыста Цупіні і фундаваны падканцлерам ВКЛ Станіславам Панятоўскім. Тут у 1732 г. нарадзіўся і быў ахрышчаны апошні вялікі князь літоўскі і кароль польскі Станіслаў Аўгуст Панятоўскі.\n\nУ ліпені 1938 года ўрад СССР таемна перадаў Польшчы труну з парэшткамі Панятоўскага з Пецярбурга, і манарх быў урачыста перапахаваны ў крыпце Воўчынскага касцёла. Пасля Другой сусветнай вайны касцёл быў разрабаваны, а ў 1988–1995 гг. парэшткі караля былі перанесены ў Варшаву ў архікатэдру Святога Яна. Сёння касцёл адноўлены.',
                'ru': 'Адрес: ул. Ленина, 45А, д. Волчин, Каменецкий район, Брестская область.\n\nШедевр позднего барокко и рококо XVIII в. Здесь в 1732 г. родился и крестился последний король польский и великий князь литовский Станислав Август Понятовский. В июле 1938 г. советские власти тайно передали гроб с останками короля Польше, и он был торжественно перезахоронен в крипте Волчинского костёла. В 1988–1995 гг. прах перевезён в Варшаву в собор Св. Иоанна.',
                'en': 'Address: 45A Lenina St, Voŭčyn, Kamyanyets District, Brest Region.\n\n18th-century Baroque church where the last Grand Duke of Lithuania and King of Poland, Stanisław August Poniatowski, was born in 1732. In July 1938, his remains were secretly transferred here from Leningrad by Soviet authorities and reburied in the crypt. In 1988–1995 his ashes were moved to St. John\'s Cathedral in Warsaw.'
            },
            'links': [
                {
                    'title': 'Вікіпедыя: Касцёл Найсвяцейшай Тройцы (Воўчын)',
                    'url': 'https://be.wikipedia.org/wiki/Касцёл_Найсвяцейшай_Тройцы_(Воўчын)'
                },
                {
                    'title': 'Радзіма мая — Беларусь: Касцёл Святой Тройцы ў Воўчыне',
                    'url': 'https://radzima.org/be/object/665.html'
                }
            ],
            'tags': [
                'панятоўскі',
                'воўчын',
                'вкл',
                'перапахаванне',
                'сабор',
                'барока',
                'спадчына'
            ],
            'personId': 'stanislaw-august-poniatowski',
            'personIds': ['stanislaw-august-poniatowski'],
            'mustSee': True
        })

    spb_catherine_id = 'spb-st-catherine-basilica-poniatowski'
    if spb_catherine_id not in existing_ids:
        places.append({
            'id': spb_catherine_id,
            'title': {
                'by': 'Базіліка Святой Кацярыны на Неўскім — Першапачатковае пахаванне Панятоўскага',
                'ru': 'Базилика Святой Екатерины на Невском — Первоначальное захоронение Понятовского',
                'en': 'Basilica of St. Catherine on Nevsky — Original Tomb of King Stanisław August Poniatowski'
            },
            'category': 'church',
            'country': {
                'by': 'Расія',
                'ru': 'Россия',
                'en': 'Russia'
            },
            'city': {
                'by': 'Санкт-Пецярбург',
                'ru': 'Санкт-Петербург',
                'en': 'Saint Petersburg'
            },
            'coordinates': [59.935609, 30.329101],
            'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Saint_Petersburg_Nevsky_Prospekt_Catholic_Church_of_St_Catherine.jpg/960px-Saint_Petersburg_Nevsky_Prospekt_Catholic_Church_of_St_Catherine.jpg',
            'description': {
                'by': 'Адрас: Неўскі праспект, 32-34, Санкт-Пецярбург.\n\nНайстарэйшы каталіцкі храм Пецярбурга, цесна звязаны з беларускай гісторыяй. Тут пасля смерці ў 1798 г. быў пахаваны апошні кароль і вялікі князь літоўскі Станіслаў Аўгуст Панятоўскі (яго цела спачывала ў крыпце 140 гадоў да перапахавання ў Воўчыне ў 1938 г.). Таксама ў гэтым храме быў пахаваны Чэслаў Манюшка (бацька кампазітара Станіслава Манюшкі), тут маліліся тысячы беларусаў Паўночнай сталіцы.',
                'ru': 'Адрес: Невский проспект, 32-34, Санкт-Петербург.\n\nСтарейший католический храм Санкт-Петербурга. Здесь после смерти в 1798 г. был погребён Станислав Август Понятовский (его прах покоился в крипте 140 лет до перезахоронения в Волчине в 1938 г.). Также здесь был похоронен Чеслав Монюшко — отец композитора Станислава Монюшко.',
                'en': 'Address: 32-34 Nevsky Prospekt, Saint Petersburg.\n\nThe oldest Roman Catholic church in St. Petersburg. Following his death in 1798, King Stanisław August Poniatowski was interred here for 140 years before his secret reburial in Voŭčyn in 1938. Czesław Moniuszko (father of composer Stanisław Moniuszko) was also buried here.'
            },
            'links': [
                {
                    'title': 'Вікіпедыя: Базіліка Святой Кацярыны Александрыйскай',
                    'url': 'https://be.wikipedia.org/wiki/Базіліка_Святой_Кацярыны_Александрыйскай'
                }
            ],
            'tags': [
                'панятоўскі',
                'пецярбург',
                'манюшка',
                'вкл',
                'касцёл',
                'неўскі'
            ],
            'personId': 'stanislaw-august-poniatowski',
            'personIds': ['stanislaw-august-poniatowski']
        })

    # Link both places to stanislaw-august-poniatowski in persons.json
    with open('data/persons.json', 'r', encoding='utf-8') as f:
        persons = json.load(f)

    for per in persons:
        if per['id'] == 'stanislaw-august-poniatowski':
            pids = set(per.get('placeIds', []))
            pids.add(volchyn_id)
            pids.add(spb_catherine_id)
            pids.add('warsaw-st-john-archcathedral-stanislaw-august-tomb')
            per['placeIds'] = list(pids)

    with open('data/persons.json', 'w', encoding='utf-8') as f:
        json.dump(persons, f, ensure_ascii=False, indent=2)

    with open('data/persons.js', 'w', encoding='utf-8') as f:
        f.write('window.INITIAL_PERSONS = ' + json.dumps(persons, ensure_ascii=False, indent=2) + ';\n')

    with open('data/places.json', 'w', encoding='utf-8') as f:
        json.dump(places, f, ensure_ascii=False, indent=2)

    with open('data/places.js', 'w', encoding='utf-8') as f:
        f.write('window.INITIAL_PLACES = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

    print(f"Final places count: {len(places)}")
    print("Updated places.json, places.js, persons.json, persons.js successfully!")

if __name__ == '__main__':
    run()
