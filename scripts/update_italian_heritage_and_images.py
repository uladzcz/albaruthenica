import json
import urllib.parse

def run():
    with open('data/places.json', 'r', encoding='utf-8') as f:
        places = json.load(f)
    with open('data/persons.json', 'r', encoding='utf-8') as f:
        persons = json.load(f)

    # 1. Update verified images for places
    verified_place_images = {
        "trakai-uzutrakis-tyszkiewicz-palace": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/U%C5%BEutrakio_dvaras_31.JPG/960px-U%C5%BEutrakio_dvaras_31.JPG",
        "lentvaris-tyszkiewicz-palace": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Lentvario_dvaras%2C_2024_vasaris_%282%29.jpg/960px-Lentvario_dvaras%2C_2024_vasaris_%282%29.jpg",
        "vilnia-glaubitz-st-johns": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Vilnius%2C_gate_of_the_Basilian_monastery_of_the_Holy_Trinity.jpg/960px-Vilnius%2C_gate_of_the_Basilian_monastery_of_the_Holy_Trinity.jpg",
        "braniewo-jesuit-college-sirotka-peregrinatio": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Braniewo_Gda%C5%84ska_17_19_Liceum_Hosianum.JPG/960px-Braniewo_Gda%C5%84ska_17_19_Liceum_Hosianum.JPG",
        "bologna-archiginnasio-university": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Archiginnasio_di_Bologna_dal_cortile.jpg/960px-Archiginnasio_di_Bologna_dal_cortile.jpg"
    }

    for pl in places:
        if pl['id'] in verified_place_images:
            pl['image'] = verified_place_images[pl['id']]

        # Verified nested items in Stare Powązki
        if pl['id'] == 'warsaw-cmentarz-powazkowski-stare-powazki':
            for it in pl.get('items', []):
                t = it.get('title', '')
                if 'Булгак' in t:
                    it['image'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Jan_Bu%C5%82hak_-_gr%C3%B3b.jpg/500px-Jan_Bu%C5%82hak_-_gr%C3%B3b.jpg'
                elif 'Немен' in t:
                    it['image'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/PL_Warsaw_Stare_Pow%C4%85zki_czeslaw_niemen_2.jpg/500px-PL_Warsaw_Stare_Pow%C4%85zki_czeslaw_niemen_2.jpg'
                elif 'Мастовіч' in t:
                    it['image'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Tadeusz_Do%C5%82%C4%99ga-Mostowicz_Polish_writer.jpg/500px-Tadeusz_Do%C5%82%C4%99ga-Mostowicz_Polish_writer.jpg'
                elif 'Карловіч' in t:
                    it['image'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Mieczys%C5%82aw_Kar%C5%82owicz_-_gr%C3%B3b.jpg/500px-Mieczys%C5%82aw_Kar%C5%82owicz_-_gr%C3%B3b.jpg'
                elif 'Адынец' in t:
                    it['image'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Antoni_Edward_Odyniec_-_gr%C3%B3b.jpg/500px-Antoni_Edward_Odyniec_-_gr%C3%B3b.jpg'
                elif 'Хамянтоўск' in t:
                    it['image'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Zofia_Chom%C4%99towska_%28lata_1930%29.jpg/500px-Zofia_Chom%C4%99towska_%28lata_1930%29.jpg'
                elif 'Корзан' in t:
                    it['image'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Tadeusz_Korzon.png/500px-Tadeusz_Korzon.png'

        # Link Zabejda-Sumitski to Olšany cemetery in Prague
        if pl['id'] == 'olsany-cemetery-prague':
            pids = pl.setdefault('personIds', [])
            if 'mikhas-zabejda-sumitski' not in pids:
                pids.append('mikhas-zabejda-sumitski')

    # 2. Update verified images for persons
    verified_person_images = {
        "jan-bulhak": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Jan_Bu%C5%82hak._%D0%AF%D0%BD_%D0%91%D1%83%D0%BB%D0%B3%D0%B0%D0%BA_%281935%29.jpg/500px-Jan_Bu%C5%82hak._%D0%AF%D0%BD_%D0%91%D1%83%D0%BB%D0%B3%D0%B0%D0%BA_%281935%29.jpg",
        "czeslaw-niemen": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Czes%C5%82aw_Niemen.png/500px-Czes%C5%82aw_Niemen.png",
        "tadeusz-dolega-mostowicz": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Tadeusz_Do%C5%82%C4%99ga-Mostowicz_Polish_writer.jpg/500px-Tadeusz_Do%C5%82%C4%99ga-Mostowicz_Polish_writer.jpg",
        "mieczyslaw-karlowicz": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Mieczys%C5%82aw_Kar%C5%82owicz_-_gr%C3%B3b.jpg/500px-Mieczys%C5%82aw_Kar%C5%82owicz_-_gr%C3%B3b.jpg",
        "antoni-edward-odyniec": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Antoni_Edward_Odyniec_-_gr%C3%B3b.jpg/500px-Antoni_Edward_Odyniec_-_gr%C3%B3b.jpg",
        "zofia-chometowska": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Zofia_Chom%C4%99towska_%28lata_1930%29.jpg/500px-Zofia_Chom%C4%99towska_%28lata_1930%29.jpg",
        "tadeusz-korzon": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Tadeusz_Korzon.png/500px-Tadeusz_Korzon.png"
    }

    for per in persons:
        if per['id'] in verified_person_images:
            per['image'] = verified_person_images[per['id']]

    # 3. Add new Italian places
    existing_place_ids = {p['id'] for p in places}

    # a) Milan: Teatro alla Scala
    if 'milan-teatro-alla-scala' not in existing_place_ids:
        places.append({
            "id": "milan-teatro-alla-scala",
            "title": {
                "by": "Тэатр Ла Скала ў Мілане",
                "ru": "Театр Ла Скала в Милане",
                "en": "Teatro alla Scala in Milan"
            },
            "category": "culture",
            "country": {
                "by": "Італія",
                "ru": "Италия",
                "en": "Italy"
            },
            "city": {
                "by": "Мілан",
                "ru": "Милан",
                "en": "Milan"
            },
            "coordinates": [
                45.4674,
                9.1897
            ],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Milano_-_Teatro_alla_Scala_0187.jpg/960px-Milano_-_Teatro_alla_Scala_0187.jpg",
            "description": {
                "by": "Сусветна вядомы оперны тэатр у Мілане, з якім шчыльна звязаныя выбітныя старонкі беларускай музычнай культуры. У 1930-я гады тут выступаў знакаміты беларускі тэнар Міхась Забэйда-Суміцкі, які вучыўся ў Мілане ў маэстра Фернанда Карпі і бліскуча выконваў вядучыя партыі ў «Травіяце», «Рыгалета» і «Севільскім цырульніку», адначасна папулярызуючы беларускую песню на еўрапейскіх сцэнах. Раней, у канцы XVIII стагоддзя, пры двары Міхала Казіміра Агінскага ў Слоніме («Слонімскіх Афінах») працаваў італьянскі дойлід і сцэнограф Іначэнца Мараіна, які кіраваў будаўніцтвам «Новага дому опэр» на вадзе, а пасля ствараў дэкарацыі для «Ла Скала». Таксама ў 1905 годзе на міланскай сцэне была з поспехам пастаўлена класічная опера «Галька» нашага земляка Станіслава Манюшкі.",
                "ru": "Всемирно известный оперный театр в Милане, с которым связаны яркие страницы беларусской музыкальной истории. В 1930-е годы на сцене «Ла Скала» пел выдающийся беларусский тенор Михаил Забейдо-Сумицкий («Травиата», «Риголетто», «Севильский цирюльник»). В конце XVIII века придворный архитектор и декоратор слонимского театра Михала Казимира Огинского Иноченцо Мараино создавал декорации для «Ла Скала». В 1905 году в Милане была с триумфом поставлена опера «Галька» Станислава Монюшко.",
                "en": "World-famous opera house in Milan, intimately connected with Belarusian musical heritage. In the 1930s, celebrated Belarusian tenor Mikhas Zabejda-Sumitski performed here ('La Traviata', 'Rigoletto', 'The Barber of Seville'). In the late 18th century, Innocenzo Maraino, chief architect and set designer of Prince Michał Kazimierz Ogiński's theatre in Slonim, designed scenery for La Scala. In 1905, Stanisław Moniuszko's masterpiece opera 'Halka' was staged in Milan."
            },
            "links": [
                {
                    "title": "Вікіпедыя: Ла Скала",
                    "url": "https://be.wikipedia.org/wiki/Ла_Скала"
                },
                {
                    "title": "Вікіпедыя: Міхаіл Забэйда-Суміцкі",
                    "url": "https://be.wikipedia.org/wiki/Міхаіл_Забэйда-Суміцкі"
                },
                {
                    "title": "Вікіпедыя: Слонімскі тэатр Агінскага",
                    "url": "https://be.wikipedia.org/wiki/Слонімскі_тэатр_Агінскага"
                }
            ],
            "tags": [
                "Італія",
                "Мілан",
                "Ла Скала",
                "тэатр",
                "опера",
                "Забэйда-Суміцкі",
                "Агінскі",
                "Манюшка"
            ],
            "personIds": [
                "mikhas-zabejda-sumitski",
                "stanislaw-moniuszko"
            ],
            "mustSee": True
        })

    # b) Milan: Piazza del Duomo (Mindaugas & Radziwiłł)
    if 'milan-piazza-duomo-mindaugas-radziwill' not in existing_place_ids:
        places.append({
            "id": "milan-piazza-duomo-mindaugas-radziwill",
            "title": {
                "by": "Саборная плошча Мілана (пасольства Міндоўга і Радзівіл Сіротка)",
                "ru": "Соборная площадь Милана (посольство Миндовга и Радзивилл Сиротка)",
                "en": "Piazza del Duomo in Milan (Mindaugas Embassy & Radziwiłł Sirotka)"
            },
            "category": "historical",
            "country": {
                "by": "Італія",
                "ru": "Италия",
                "en": "Italy"
            },
            "city": {
                "by": "Мілан",
                "ru": "Милан",
                "en": "Milan"
            },
            "coordinates": [
                45.4641,
                9.1919
            ],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Milan_Cathedral_from_Piazza_del_Duomo.jpg/960px-Milan_Cathedral_from_Piazza_del_Duomo.jpg",
            "description": {
                "by": "Гістарычнае сэрца Мілана, непасрэдна звязанае з вытокамі дыпламатыі і культуры ВКЛ. Менавіта ў Мілан у ліпені 1251 года прыбыло пасольства вялікага князя Міндоўга да папы рымскага Інакенція IV: пантыфік прыняў ліцвінскіх паслоў, абвясціў прыняцце Літвы пад апеку Святога Пасаду і падпісаў папскія булы пра каранацыю Міндоўга каралём (булы ад 17 ліпеня 1251 г.). У 1560-я гады падчас гранд-тура Мілан наведаў Мікалай Крыштаф Радзівіл «Сіротка», знаёмства якога з ламбардскім рэнесансам паўплывала на перабудову Нясвіжа. Таксама ад лацінскай назвы Мілана (Mediolanum) паходзіць славутая парода вартаўнічых і паляўнічых сабак шляхты ВКЛ — «медзяляны», увезеныя з Ламбардыі і згаданыя ў Статуце ВКЛ.",
                "ru": "Историческое сердце Милана. В июле 1251 года сюда прибыло посольство великого князя Миндовга к папе Иннокентию IV, издавшему буллы о коронации Миндовга королём Литвы. В 1560-е годы Милан посетил Николай Криштоф Радзивилл Сиротка. От латинского названия Милана (Mediolanum) происходит порода охотничьих мастифов знати ВКЛ — «меделяне».",
                "en": "Historic heart of Milan. In July 1251, Grand Duke Mindaugas sent an embassy here to Pope Innocent IV, who issued papal bulls declaring Lithuania under the protection of the Holy See and authorizing Mindaugas' royal coronation. In the 1560s, Mikołaj Krzysztof Radziwiłł 'Sirotka' visited Milan during his grand tour. The Latin name Mediolanum also gave rise to the historic GDL mastiff breed 'medelyany' (Mediolan dogs) kept by the nobility."
            },
            "links": [
                {
                    "title": "Вікіпедыя: Міндоўг",
                    "url": "https://be.wikipedia.org/wiki/Міндоўг"
                },
                {
                    "title": "Вікіпедыя: Мікалай Крыштаф Радзівіл Сіротка",
                    "url": "https://be.wikipedia.org/wiki/Мікалай_Крыштаф_Радзівіл_Сіротка"
                }
            ],
            "tags": [
                "Італія",
                "Мілан",
                "Міндоўг",
                "дыпламатыя",
                "ВКЛ",
                "Радзівіл Сіротка",
                "медзяляны",
                "пасольства"
            ],
            "personIds": [
                "radziwill-sirotka"
            ],
            "mustSee": True
        })

    # c) Naples: Castel Capuano (Bona Sforza)
    if 'naples-castel-capuano-bona-sforza' not in existing_place_ids:
        places.append({
            "id": "naples-castel-capuano-bona-sforza",
            "title": {
                "by": "Замак Кастэль-Капуана ў Неапалі (вянчанне Боны Сфорца і «неапалітанскія сумы»)",
                "ru": "Замок Кастель-Капуано в Неаполе (венчание Боны Сфорца и «неаполитанские суммы»)",
                "en": "Castel Capuano in Naples (Wedding of Bona Sforza & Neapolitan Sums)"
            },
            "category": "historical",
            "country": {
                "by": "Італія",
                "ru": "Италия",
                "en": "Italy"
            },
            "city": {
                "by": "Неапаль",
                "ru": "Неаполь",
                "en": "Naples"
            },
            "coordinates": [
                40.8533,
                14.2655
            ],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Napoli_-_Castel_Capuano.jpg/960px-Napoli_-_Castel_Capuano.jpg",
            "description": {
                "by": "Знакаміты нармандска-арагонскі замак у Неапалі, цесна звязаны з лёсам вялікай княгіні літоўскай і каралевы польскай Боны Сфорца. 6 снежня 1517 года тут адбылося пышнае вянчанне Боны з каралём польскім і вялікім князем літоўскім Жыгімонтам I Старым (па даверанасці). Бона Сфорца аказала каласальны ўплыў на беларускія землі: праводзіла аграрную рэформу («Валочная памера»), будавала каналы ў Кобрыне і Пінску, заснавала горад Моталь, прывезла міжземнаморскую культуру і кухню. З гэтым жа неапалітанскім кантэкстам звязаны сусветна вядомы фінансава-дыпламатычны дэтэктыў — «неапалітанскія сумы»: у 1557 г. Бона пазычыла каралю Філіпу II Неапалітанскаму 430 000 залатых дукатаў, пасля чаго была атручаная ў Бары; спробы вярнуць гэты доўг ВКЛ доўжыліся больш за два стагоддзі.",
                "ru": "Нормандско-арагонский замок в Неаполе. 6 декабря 1517 года здесь состоялось венчание Боны Сфорца с королём и великим князем Сигизмундом I Старым. Бона провела в ВКЛ грандиозную аграрную реформу («Волочная помера»), строила каналы в Кобрине и Пинске, основала Мотоль. С Неаполем связан исторический детектив — «неаполитанские суммы» (долг короля Филиппа II в 430 000 дукатов, который дипломаты ВКЛ пытались взыскать более двух столетий).",
                "en": "Historic castle in Naples where, on 6 December 1517, Duchess Bona Sforza was married by proxy to Sigismund I the Old, King of Poland and Grand Duke of Lithuania. Bona went on to revolutionize Belarusian lands with sweeping land reforms ('Valochnaya Pamera'), canals in Kobryn and Pinsk, and Italian Renaissance horticulture. Naples is also home to the famous saga of the 'Neapolitan Sums' — 430,000 gold ducats lent by Bona to King Philip II, leading to her poisoning in Bari and over two centuries of diplomatic recovery efforts."
            },
            "links": [
                {
                    "title": "Вікіпедыя: Бона Сфорца",
                    "url": "https://be.wikipedia.org/wiki/Бона_Сфорца"
                },
                {
                    "title": "Вікіпедыя: Неапалітанскія сумы",
                    "url": "https://be.wikipedia.org/wiki/Неапалітанскія_сумы"
                },
                {
                    "title": "Вікіпедыя: Кастэль-Капуана",
                    "url": "https://be.wikipedia.org/wiki/Кастэль-Капуана"
                }
            ],
            "tags": [
                "Італія",
                "Неапаль",
                "Бона Сфорца",
                "Кастэль-Капуана",
                "неапалітанскія сумы",
                "ВКЛ",
                "замак"
            ],
            "personIds": [
                "bona-sforza"
            ],
            "mustSee": True
        })

    # 4. Add new persons
    existing_person_ids = {p['id'] for p in persons}

    if 'mikhas-zabejda-sumitski' not in existing_person_ids:
        persons.append({
            "id": "mikhas-zabejda-sumitski",
            "name": {
                "by": "Міхась Забэйда-Суміцкі",
                "ru": "Михаил Забейдо-Сумицкий",
                "en": "Mikhas Zabejda-Sumitski"
            },
            "dates": "1900–1981",
            "role": {
                "by": "Выбітны беларускі спявак (тэнар), саліст міланскай «Ла Скала» і Пражскай оперы",
                "ru": "Выдающийся беларусский певец (тенор), солист миланской «Ла Скала» и Пражской оперы",
                "en": "Renowned Belarusian tenor, soloist at Milan's Teatro alla Scala and Prague National Theatre"
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Micha%C5%9B_Zabejda-Sumicki._%D0%9C%D1%96%D1%85%D0%B0%D1%81%D1%8C_%D0%97%D0%B0%D0%B1%D1%8D%D0%B9%D0%B4%D0%B0-%D0%A1%D1%83%D0%BC%D1%96%D1%86%D0%BA%D1%96_%281930-37%29.jpg/500px-Micha%C5%9B_Zabejda-Sumicki._%D0%9C%D1%96%D1%85%D0%B0%D1%81%D1%8C_%D0%97%D0%B0%D0%B1%D1%8D%D0%B9%D0%B4%D0%B0-%D0%A1%D1%83%D0%BC%D1%96%D1%86%D0%BA%D1%96_%281930-37%29.jpg",
            "bio": {
                "by": "Нарадзіўся ў вёсцы Шэйпічы на Пружаншчыне. Вучыўся ў Мілане ў маэстра Фернанда Карпі, у 1930-я выступаў у тэатры «Ла Скала». У гады эміграцыі жыў у Празе, быў салістам Нацыянальнага тэатра, папулярызаваў беларускія песні і класіку па ўсім свеце. Пахаваны на Альшанскіх могілках у Празе.",
                "ru": "Родился в деревне Шейпичи Пружанского уезда. Совершенствовал вокальное мастерство в Милане, выступал на сцене «Ла Скала». С 1940 г. жил в Праге, солист Пражской оперы. Похоронен на Ольшанском кладбище в Праге.",
                "en": "Born in Shejpichy, Pruzhany region. Studied under maestro Fernando Carpi in Milan, performing at Teatro alla Scala. Later principal soloist of the Prague National Theatre. Buried at Olšany Cemetery in Prague."
            },
            "wiki": "https://be.wikipedia.org/wiki/Міхаіл_Забэйда-Суміцкі",
            "placeIds": [
                "milan-teatro-alla-scala",
                "olsany-cemetery-prague"
            ]
        })

    # Connect Bona Sforza and Radziwiłł Sirotka
    for per in persons:
        if per['id'] == 'bona-sforza':
            pids = per.setdefault('placeIds', [])
            if 'naples-castel-capuano-bona-sforza' not in pids:
                pids.append('naples-castel-capuano-bona-sforza')
        if per['id'] == 'radziwill-sirotka':
            pids = per.setdefault('placeIds', [])
            if 'milan-piazza-duomo-mindaugas-radziwill' not in pids:
                pids.append('milan-piazza-duomo-mindaugas-radziwill')

    # Save places
    with open('data/places.json', 'w', encoding='utf-8') as f:
        json.dump(places, f, ensure_ascii=False, indent=2)

    with open('data/places.js', 'w', encoding='utf-8') as f:
        f.write('window.INITIAL_PLACES = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

    # Save persons
    with open('data/persons.json', 'w', encoding='utf-8') as f:
        json.dump(persons, f, ensure_ascii=False, indent=2)

    with open('data/persons.js', 'w', encoding='utf-8') as f:
        f.write('window.INITIAL_PERSONS = ' + json.dumps(persons, ensure_ascii=False, indent=2) + ';\n')

    print(f"Done! Places: {len(places)}, Persons: {len(persons)}")

if __name__ == '__main__':
    run()
