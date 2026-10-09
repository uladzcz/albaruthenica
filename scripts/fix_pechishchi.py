import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/places.json', 'r', encoding='utf-8') as f:
    places = json.load(f)

for p in places:
    if p['id'] == 'pechishchi-kupala-museum':
        p['coordinates'] = [55.782080, 48.954623]
        p['image'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/%D0%92%D0%B8%D0%B4_%D0%BD%D0%B0_%D1%81%D0%B5%D0%BB%D0%BE_%D0%9F%D0%B5%D1%87%D0%B8%D1%89%D0%B8_%D1%81%D0%BE_%D1%81%D1%82%D0%BE%D1%80%D0%BE%D0%BD%D1%8B_%D0%9A%D0%B0%D0%B7%D0%B0%D0%BD%D0%B8.JPG/960px-%D0%92%D0%B8%D0%B4_%D0%BD%D0%B0_%D1%81%D0%B5%D0%BB%D0%BE_%D0%9F%D0%B5%D1%87%D0%B8%D1%89%D0%B8_%D1%81%D0%BE_%D1%81%D1%82%D0%BE%D1%80%D0%BE%D0%BD%D1%8B_%D0%9A%D0%B0%D0%B7%D0%B0%D0%BD%D0%B8.JPG'
        p['wiki'] = 'https://be.wikipedia.org/wiki/Пячышчы'
        p['description'] = {
            'by': 'Адрас: вул. Калініна, 5 (тэрыторыя млына Аканішнікава), с. Пячышчы, Верхняўслонскі раён, Татарстан.\n\nАдзіны музей Янкі Купалы ў Расіі (філіял Нацыянальнага музея Рэспублікі Татарстан). Адкрыты ў 1975 годзе ў гістарычным будынку паравога млына купцоў Аканішнікавых на беразе Волгі, дзе класік беларускай літаратуры жыў у эвакуацыі з 13 лістапада 1941 г. па 18 чэрвеня 1942 г. Адсюль ён выехаў у Маскву, дзе трагічна загінуў 28 чэрвеня 1942 года. У Пячышчах Купала напісаў славутыя вершы «Беларускім партызанам», «Зноў будзем шчасце мець і волю». У музеі адноўлены мемарыяльны пакой паэта, прадстаўлены яго асабістыя рэчы, кнігі і рукапісы.',
            'ru': 'Адрес: ул. Калинина, 5 (территория мельницы Оконишникова), с. Печищи, Верхнеуслонский район, Татарстан.\n\nЕдинственный музей Янки Купалы в России (филиал Национального музея Республики Татарстан). Открыт в 1975 году в здании паровой мельницы торгового дома «Иван Оконишников и сыновья» на берегу Волги, где народный поэт Беларуси жил в эвакуации с ноября 1941 г. по 18 июня 1942 г. до своего последнего отъезда в Москву. Здесь написаны стихотворения «Белорусским партизанам», «Снова будем счастье иметь и волю». Сохранилась мемориальная комната поэта.',
            'en': 'Address: 5 Kalinina St (Okonishnikov Mill complex), Pechishchi, Tatarstan, Russia.\n\nThe only Yanka Kupala museum in Russia (branch of the National Museum of Tatarstan). Opened in 1975 in a historic 19th-century steam flour mill on the bank of the Volga, where the Belarusian national poet lived in wartime evacuation from November 1941 until June 18, 1942, shortly before his tragic death in Moscow. The memorial room displays his personal belongings, books, and manuscripts.'
        }
        p['links'] = [
            {
                'title': 'Афіцыйны сайт: Музей Янкі Купалы ў с. Пячышчы',
                'url': 'https://kupala.tatmuseum.ru/'
            },
            {
                'title': 'Яндекс Карты: Музей Янки Купалы в Печищах',
                'url': 'https://yandex.ru/maps/org/muzey_yanki_kupaly/1271109961/'
            },
            {
                'title': 'Вікіпедыя: Пячышчы (раздзел пра Янку Купалу)',
                'url': 'https://be.wikipedia.org/wiki/Пячышчы'
            },
            {
                'title': 'Музеи России: Музей Янки Купалы в с. Печищи',
                'url': 'http://www.museum.ru/M1302'
            }
        ]
        p.pop('unverifiedCoordinates', None)

with open('data/places.json', 'w', encoding='utf-8') as f:
    json.dump(places, f, ensure_ascii=False, indent=2)

with open('data/places.js', 'w', encoding='utf-8') as f:
    f.write('window.INITIAL_PLACES = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

print("Updated pechishchi-kupala-museum successfully!")
