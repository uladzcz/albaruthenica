import json
import urllib.request
import urllib.parse
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Function to fetch thumbnail from Wikipedia REST API
def fetch_wiki_image(wiki_url):
    m = re.search(r'https?://([a-z]+)\.wikipedia\.org/wiki/(.+)', wiki_url)
    if not m:
        return None
    lang = m.group(1)
    raw_title = m.group(2)
    clean_title = urllib.parse.unquote(raw_title)
    quoted_title = urllib.parse.quote(clean_title)
    api_url = f"https://{lang}.wikipedia.org/api/rest_v1/page/summary/{quoted_title}"
    try:
        req = urllib.request.Request(api_url, headers={'User-Agent': 'AlbaruthenicaBot/1.0 (https://github.com/uladzcz/albaruthenica)'})
        with urllib.request.urlopen(req, timeout=6) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if 'thumbnail' in data and 'source' in data['thumbnail']:
                # Clean query params if any
                src = data['thumbnail']['source']
                return src.split('?')[0]
            elif 'originalimage' in data and 'source' in data['originalimage']:
                src = data['originalimage']['source']
                return src.split('?')[0]
    except Exception as e:
        print(f"Failed wiki img for {clean_title} ({lang}): {e}")
    return None

def main():
    print("Loading data...")
    with open('data/places.json', 'r', encoding='utf-8') as f:
        places = json.load(f)
    with open('data/persons.json', 'r', encoding='utf-8') as f:
        persons = json.load(f)
        
    places_map = {p['id']: p for p in places}
    persons_map = {p['id']: p for p in persons}
    
    # 1. FIX SOLOTHURN: Replace duplicate kosciuszko-museum-solothurn with solothurn-kosciuszko-monument
    if 'kosciuszko-museum-solothurn' in places_map:
        del places_map['kosciuszko-museum-solothurn']
        
    places_map['solothurn-kosciuszko-monument'] = {
        "id": "solothurn-kosciuszko-monument",
        "title": {
            "by": "Помнік Тадэвушу Касцюшку ў Залатурне (Stadtpark)",
            "ru": "Памятник Тадеушу Костюшко в Золотурне (Stadtpark)",
            "en": "Tadeusz Kosciuszko Monument in Solothurn (Stadtpark)"
        },
        "category": "monument",
        "country": {
            "by": "Швейцарыя",
            "ru": "Швейцария",
            "en": "Switzerland"
        },
        "city": {
            "by": "Залатурн",
            "ru": "Золотурн",
            "en": "Solothurn"
        },
        "coordinates": [47.2064, 7.5412],
        "description": {
            "by": "Помнік нацыянальнаму герою Беларусі, Польшчы і ЗША Тадэвушу Касцюшку ў гарадскім парку (Stadtpark) Залатурна — горада, дзе герой правёў апошнія гады жыцця і спачыў у 1817 годзе. Усталяваны 21 кастрычніка 2017 года да 200-годдзя з дня смерці Касцюшкі па ініцыятыве Беларускага аб'яднання ў Швейцарыі (Алесь Сапега) пры шырокай падтрымцы беларускай дыяспары. Бронзавая постаць вышынёй 181 см усталяваная на пастаменце з вялікага беларускага палявога валуна. На шыльдзе змешчаны надпіс на беларускай і нямецкай мовах: «Тадэвуш Касцюшка / Thaddäus Kosciuszko (1746–1817). Выбітны сын Беларусі».",
            "ru": "Памятник национальному герою Беларуси, Польши и США Тадеушу Костюшко в городском парке Золотурна — города, где он провёл последние годы жизни. Установлен в 2017 году к 200-летию со дня смерти героя по инициативе Ассоциации белорусов в Швейцарии (Алесь Сапега). Бронзовая фигура на постаменте из белорусского полевого валуна с надписью «Выбітны сын Беларусі».",
            "en": "Monument to national hero Tadeusz Kosciuszko in the Stadtpark of Solothurn, where he spent his final years and died in 1817. Erected in October 2017 on the initiative of the Association of Belarusians in Switzerland (Ales Sapeha). The 1.8-meter bronze statue stands on a boulder brought from Belarus with the inscription: 'Outstanding son of Belarus'."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Kosciuszko_monument_Solothurn.jpg/640px-Kosciuszko_monument_Solothurn.jpg",
        "links": [
            {
                "title": "Вікіпедыя: Помнік Тадэвушу Касцюшку ў Залатурне",
                "url": "https://be.wikipedia.org/wiki/Помнік_Тадэвушу_Касцюшку_(Залатурн)"
            }
        ],
        "tags": ["Залатурн", "Касцюшка", "Помнік", "Дыяспара", "Швейцарыя"],
        "personId": "tadeusz-kosciuszko",
        "personIds": ["tadeusz-kosciuszko"],
        "unverifiedCoordinates": False,
        "isUnverifiedCoordinates": False
    }
    print("Fixed Solothurn: museum deduplicated, monument added.")

    # 2. ADD SCHLOSS HÖCHSTÄDT (НАЦЫСЦКАЕ СХОВІШЧА ВЫВЕЗЕНЫХ БЕЛАРУСКІХ КАШТОЎНАСЦЕЙ)
    places_map['germany-schloss-hoechstaedt'] = {
        "id": "germany-schloss-hoechstaedt",
        "title": {
            "by": "Замак Хёхштэд — сховішча нарабаваных нацыстамі беларускіх каштоўнасцей",
            "ru": "Замок Хёхштедт — хранилище вывезенных нацистами белорусских ценностей",
            "en": "Höchstädt Castle — Nazi Repository of Looted Belarusian Treasures"
        },
        "category": "historical",
        "country": {
            "by": "Германія",
            "ru": "Германия",
            "en": "Germany"
        },
        "city": {
            "by": "Хёхштэд-на-Дунаі",
            "ru": "Хёхштедт-на-Дунае",
            "en": "Höchstädt an der Donau"
        },
        "coordinates": [48.611111, 10.578056],
        "description": {
            "by": "Рэнесансны замак у Баварыі, які падчас Другой сусветнай вайны стаў адным з найбуйнейшых сховішчаў нарабаваных нацыстамі культурных каштоўнасцей Аператыўнага штаба рэйхсляйтара Розенберга (ERR). Сюды эшалонамі вывозілі шэдэўры са спаленай і акупаванай Беларусі: калекцыі Дзяржаўнай карціннай галерэі ў Мінску, экспанаты Беларускага дзяржаўнага музея, царкоўныя рэліквіі, старадрукі і гістарычныя архівы. У 1945 годзе амерыканскія эксперты па ахове помнікаў («Monuments Men») выявілі тут велізарны масіў беларускай спадчыны. Даследаваннем гэтага сховішча і вяртаннем скарбаў дзесяцігоддзямі займаўся выбітны вучоны Адам Мальдзіс.",
            "ru": "Ренессансный замок в Баварии, служивший в годы Второй мировой войны одним из главных хранилищ награбленных нацистами культурных ценностей (штаб Розенберга - ERR). Сюда эшелонами вывозились шедевры из Беларуси: фонды Минской картинной галереи, Белорусского государственного музея, церковные реликвии, редкие старопечатные книги. В 1945 году американские «Monuments Men» обнаружили здесь колоссальный массив вывезенного наследия.",
            "en": "Renaissance castle in Bavaria used during WWII by the Nazi Einsatzstab Reichsleiter Rosenberg (ERR) as a principal repository for cultural treasures plundered from occupied Belarus. Hundreds of crates containing masterpieces from the Minsk Picture Gallery, the Belarusian State Museum, church relics, and historic archives were hidden here before being discovered in 1945 by the Allied 'Monuments Men'."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Schloss_H%C3%B6chst%C3%A4dt_01.jpg/960px-Schloss_H%C3%B6chst%C3%A4dt_01.jpg",
        "links": [
            {
                "title": "Вікіпедыя: Höchstädt Castle",
                "url": "https://en.wikipedia.org/wiki/Höchstädt_Castle"
            },
            {
                "title": "Афіцыйны сайт замка Хёхштэд",
                "url": "https://www.schloss-hoechstaedt.de/"
            }
        ],
        "tags": ["Германія", "Баварыя", "Хёхштэд", "Каштоўнасці", "Мальдзіс", "Другая сусветная вайна"],
        "personId": "adam-maldis",
        "personIds": ["adam-maldis"],
        "unverifiedCoordinates": False,
        "isUnverifiedCoordinates": False
    }
    print("Added Schloss Höchstädt.")

    # 3. UPDATE SOUTH RIVER ITEMS with personIds
    if 'south-river-st-euphrosyne' in places_map:
        sr = places_map['south-river-st-euphrosyne']
        sr['personIds'] = ["radaslau-astrouski", "jurka-vicbic", "yauhim-kipel"]
        sr['items'] = [
            {
                "title": "Магіла Радаслава Астроўскага",
                "author": "",
                "person": "Радаслаў Астроўскі (1887–1976)",
                "personId": "radaslau-astrouski",
                "year": "1976",
                "description": "Прэзідэнт Беларускай Цэнтральнай Рады, дзеяч БНР і беларускага школьніцтва, заснавальнік паваеннай суполкі ў Саўт-Рыверы.",
                "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Radasla%C5%AD_Astro%C5%ADski._%D0%A0%D0%B0%D0%B4%D0%B0%D1%81%D0%BB%D0%B0%D1%9E_%D0%90%D1%81%D1%82%D1%80%D0%BE%D1%9E%D1%81%D0%BA%D1%96_%281917%29.jpg/330px-Radasla%C5%AD_Astro%C5%ADski._%D0%A0%D0%B0%D0%B4%D0%B0%D1%81%D0%BB%D0%B0%D1%9E_%D0%90%D1%81%D1%82%D1%80%D0%BE%D1%9E%D1%81%D0%BA%D1%96_%281917%29.jpg"
            },
            {
                "title": "Магіла Юркі Віцьбіча",
                "author": "",
                "person": "Юрка Віцьбіч (1905–1975)",
                "personId": "jurka-vicbic",
                "year": "1975",
                "description": "Выбітны пісьменнік, эсэіст, публіцыст і краязнаўца, даследчык беларускай гісторыі і рэпрэсій савецкага часу.",
                "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Jurka_Vi%C4%87bi%C4%8D.jpg/330px-Jurka_Vi%C4%87bi%C4%8D.jpg"
            },
            {
                "title": "Магіла Яўхіма Кіпеля",
                "author": "",
                "person": "Яўхім Кіпель (1896–1969)",
                "personId": "yauhim-kipel",
                "year": "1969",
                "description": "Беларускі педагог, грамадскі і культурны дзеяч, пачынальнік арганізацыі беларускага школьніцтва ў ЗША.",
                "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Jauchim_Kipel.jpg/330px-Jauchim_Kipel.jpg"
            }
        ]
        print("Updated South River items with explicit personIds and images.")

    # 4. ADD NEW PERSONS: Radaslau Astrouski, Jurka Vicbic, Yauhim Kipel, Adam Maldis
    new_persons_defs = [
        {
            "id": "radaslau-astrouski",
            "name": {
                "by": "Радаслаў Астроўскі",
                "ru": "Радослав Островский",
                "en": "Radaslau Astrouski"
            },
            "dates": "1887–1976",
            "role": {
                "by": "Грамадска-палітычны дзеяч, прэзідэнт Беларускай Цэнтральнай Рады, міністр асветы БНР",
                "ru": "Общественно-политический деятель, президент БЦР, министр просвещения БНР",
                "en": "Statesman, President of the Belarusian Central Council, educator"
            },
            "bio": {
                "by": "Ураджэнец Ігуменскага павета (Пухавіччына). Адзін з арганізатараў беларускага школьніцтва, дырэктар Віленскай беларускай гімназіі, дзеяч Беларускай Народнай Рэспублікі. У гады эміграцыі жыў у ЗША, дзе стаў ключавой фігурай грамадскага жыцця беларускай дыяспары ў Саўт-Рыверы і стварыў знакаміты беларускі некропаль.",
                "ru": "Уроженец Пуховичского района. Директор Виленской белорусской гимназии, деятель БНР. В эмиграции в США стал основателем белорусского общественного центра и некрополя в Саут-Ривере.",
                "en": "Born in the Pukhavichy district. Educator, director of the Vilnius Belarusian Gymnasium, and activist of the Belarusian Democratic Republic. In US exile, became the foundational leader of the South River Belarusian community and its historic cemetery."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Radasla%C5%AD_Astro%C5%ADski._%D0%A0%D0%B0%D0%B4%D0%B0%D1%81%D0%BB%D0%B0%D1%9E_%D0%90%D1%81%D1%82%D1%80%D0%BE%D1%9E%D1%81%D0%BA%D1%96_%281917%29.jpg/330px-Radasla%C5%AD_Astro%C5%ADski._%D0%A0%D0%B0%D0%B4%D0%B0%D1%81%D0%BB%D0%B0%D1%9E_%D0%90%D1%81%D1%82%D1%80%D0%BE%D1%9E%D1%81%D0%BA%D1%96_%281917%29.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Радаслаў_Казіміравіч_Астроўскі",
            "placeIds": ["south-river-st-euphrosyne"]
        },
        {
            "id": "jurka-vicbic",
            "name": {
                "by": "Юрка Віцьбіч (Серафімовіч)",
                "ru": "Юрка Витьбич (Серафимович)",
                "en": "Jurka Vićbič"
            },
            "dates": "1905–1975",
            "role": {
                "by": "Выдатны беларускі пісьменнік, эсэіст, гісторык-краязнаўца, даследчык спадчыны",
                "ru": "Белорусский писатель, эссеист, историк-краевед, исследователь наследия",
                "en": "Belarusian writer, essayist, historian, chronicler of cultural heritage"
            },
            "bio": {
                "by": "Ураджэнец Вяліжа (Віцебская губерня). Прыхільнік адраджэння беларускай нацыянальнай памяці, аўтар глыбокіх гістарычных аповесцей і даследаванняў пра лёсы беларускіх дзеячаў і ахвяр савецкіх рэпрэсій («Мы дойдзем!», «Плыве з-пад Святога гор Дзвіна»). У эміграцыі ў ЗША — актыўны дзеяч беларускай грамады ў Саўт-Рыверы.",
                "ru": "Уроженец Велижа (Витебская губерния). Выдающийся прозаик и краевед, исследовавший судьбы белорусских деятелей и жертв репрессий. В эмиграции в США — видный деятель белорусской общины Саут-Ривера.",
                "en": "Born in Vyalizh (Vitebsk Governorate). Prominent novelist, essayist, and historian dedicated to documenting Belarusian national heritage and the victims of Soviet repressions. Active member of the South River Belarusian diaspora."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Jurka_Vi%C4%87bi%C4%8D.jpg/330px-Jurka_Vi%C4%87bi%C4%8D.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Юрка_Віцьбіч",
            "placeIds": ["south-river-st-euphrosyne"]
        },
        {
            "id": "yauhim-kipel",
            "name": {
                "by": "Яўхім Кіпель",
                "ru": "Евфимий Кипель",
                "en": "Yauhim Kipel"
            },
            "dates": "1896–1969",
            "role": {
                "by": "Педагог, грамадскі дзеяч, арганізатар беларускага школьніцтва ў ЗША",
                "ru": "Педагог, общественный деятель, организатор белорусских школ в США",
                "en": "Educator, public figure, organizer of Belarusian schools in the US"
            },
            "bio": {
                "by": "Ураджэнец Бабруйскага павета. Удзельнік беларускага нацыянальнага адраджэння 1920-х гадоў, выкладчык беларускай мовы і літаратуры. Пасля Другой сусветнай вайны эміграваў у ЗША, дзе заклаў асновы беларускага школьніцтва і выхавання моладзі ў Саўт-Рыверы, сузаснавальнік Беларускага інстытута навукі і мастацтва (БІНіМ).",
                "ru": "Уроженец Бобруйского уезда. Педагог и просветитель, участник национального движения 1920-х годов. В США заложил основы белорусского школьного образования в Саут-Ривере, сооснователь БИНИМ.",
                "en": "Born in the Babruysk district. Pioneer educator who advanced Belarusian schooling and youth education in post-war America. Co-founder of the Belarusian Institute of Arts and Sciences (BINiM) in New York."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Jauchim_Kipel.jpg/330px-Jauchim_Kipel.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Яўхім_Яўсеевіч_Кіпель",
            "placeIds": ["south-river-st-euphrosyne"]
        },
        {
            "id": "adam-maldis",
            "name": {
                "by": "Адам Мальдзіс",
                "ru": "Адам Мальдис",
                "en": "Adam Maldis"
            },
            "dates": "1932–2022",
            "role": {
                "by": "Літаратуразнаўца, гісторык, культуролаг, старшыня камісіі «Вяртанне»",
                "ru": "Литературовед, историк, культуролог, председатель комиссии «Вяртанне»",
                "en": "Literary scholar, historian, cultural researcher, head of the 'Return' commission"
            },
            "bio": {
                "by": "Нарадзіўся ў вёсцы Расолы Астравецкага раёна Гродзенскай вобласці. Выдатны даследчык беларускай літаратуры і культуры, доктар філалагічных навук, прафесар. Заснавальнік і кіраўнік Нацыянальнага навукова-асветнага цэнтра імя Францыска Скарыны. Прысвяціў жыццё адшуканню і вяртанню ў Беларусь нацыянальных гісторыка-культурных каштоўнасцей, вывезеных за межы краіны (у тым ліку даследаваў нямецкія сховішчы ў Баварыі і замку Хёхштэд).",
                "ru": "Родился в Островецком районе Гродненской области. Выдающийся исследователь белорусской литературы и культуры, доктор филологических наук. Основатель Центра имени Франциска Скорины. Возглавлял государственную комиссию по поиску и возвращению национальных культурных ценностей, утраченных в годы войн.",
                "en": "Born in the Astravec district of Hrodna region. Renowned historian, scholar of Belarusian literature and culture, and leader of the National Center named after Francysk Skaryna. Spearheaded missions across Europe to trace, document, and return looted Belarusian treasures, including ERR war repositories such as Höchstädt Castle."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Adam_Maldis.jpg/330px-Adam_Maldis.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Адам_Іосіфавіч_Мальдзіс",
            "placeIds": ["germany-schloss-hoechstaedt"]
        }
    ]

    for p in new_persons_defs:
        persons_map[p['id']] = p

    # 5. ENHANCE EVERY PERSON'S BIO to clearly reveal their connection to Belarus, Belarusian culture and history
    # And fetch verified Wikipedia thumbnail
    print(f"Enhancing {len(persons_map)} person biographies and Wikipedia images...")
    
    # Specific curated Belarusian connection additions:
    BELARUS_CONNECTIONS = {
        "henryk-sienkiewicz": {
            "by": "Паходзіў са шляхецкага роду герба «Осык» з татарскімі каранямі з Вялікага Княства Літоўскага. Яго сям'я мела глыбокія карані на Навагрудчыне і Гарадзеншчыне. У знакамітай гістарычнай «Трылогіі» («Патоп», «Агнём і мячом») ключавыя падзеі адбываюцца на землях ВКЛ, а галоўнымі героямі выступаюць аршанскі шляхціц Анджэй Кміціц і магнаты Радзівілы. Лаўрэат Нобелеўскай прэміі па літаратуры (1905).",
            "ru": "Происходил из шляхетского рода с корнями в Великом Княжестве Литовском (липковские татары Новогрудчины). В знаменитой трилогии («Потоп») ключевые события разворачиваются в ВКЛ, а главными героями являются оршанский шляхтич Анджей Кмитиц и магнаты Радзивиллы. Лауреат Нобелевской премии по литературе 1905 года.",
            "en": "Descended from Lipka Tatar nobility rooted in the Grand Duchy of Lithuania (Navahrudak and Hrodna lands). The pivotal historical scenes of his epic 'Trilogy' take place across Belarusian and Lithuanian lands, featuring characters like the Orsha nobleman Andrzej Kmicic and the Radziwiłł magnates. Nobel Prize laureate in Literature (1905)."
        },
        "tadeusz-kosciuszko": {
            "by": "Нарадзіўся ва ўрочышчы Мерачоўшчына каля Косава (цяпер Івацэвіцкі раён Брэсцкай вобласці). Выбітны ваенны інжынер, нацыянальны герой Беларусі, Польшчы і ЗША. Кіраўнік вызваленчага паўстання 1794 года ў абарону незалежнасці Рэчы Паспалітай і ВКЛ. Ганаровы грамадзянін Францыі і генерал арміі Джорджа Вашынгтона.",
            "ru": "Родился в урочище Меречёвщина близ Коссово (Брестская область). Выдающийся военный инженер, национальный герой Беларуси, Польши и США. Предводитель освободительного восстания 1794 года, бригадный генерал армии США.",
            "en": "Born in Merachowshchyna near Kosava (Brest region). National hero of Belarus, Poland, and the United States, military engineer and supreme commander of the 1794 Uprising defending the freedom of the Grand Duchy and Poland."
        },
        "francysk-skaryna": {
            "by": "Ураджэнец Полацка. Беларускі і ўсходнеславянскі першадрукар, мысліцель-гуманіст, доктар лекарскіх навук Падуанскага ўніверсітэта. У 1517–1519 гг. у Празе выдаў першыя друкаваныя кнігі на старабеларускай мове (Біблію Руску). У 1522 г. у Вільні заснаваў першую друкарню на землях ВКЛ.",
            "ru": "Уроженец Полоцка. Белорусский и восточнославянский первопечатник, мыслитель-гуманист, доктор медицины Падуанского университета. Издал в Праге первую Библию на старобелорусском языке (1517–1519), открыл первую типографию в Вильне (1522).",
            "en": "Born in Polatsk. Belarusian and East Slavic pioneer printer, Renaissance humanist, and Doctor of Medicine (Padua, 1512). Published the first printed Bible in Old Belarusian in Prague (1517–1519) and established the Grand Duchy's first printing shop in Vilnius (1522)."
        },
        "adam-mickiewicz": {
            "by": "Нарадзіўся на Навагрудчыне (фальварак Завоссе). Геніяльны паэт-рамантык, пачынальнік новай беларускай літаратурнай традыцыі («Літва! Мая айчына...»). Выкарыстоўваў беларускія паданні, моўныя элементы і фальклор Навагрудчыны і Свіцязі ў сусветна вядомых паэмах «Гражына», «Дзяды», «Пан Тадэвуш».",
            "ru": "Родился на Новогрудчине (фольварк Заосье). Классик романтизма, воспевший родные новогрудские земли, озеро Свитязь и шляхетские традиции ВКЛ в бессмертных поэмах «Гражина», «Дзяды» и «Пан Тадеуш».",
            "en": "Born in the Navahrudak region (Zavosse estate). Foremost Romantic poet whose immortal masterpieces ('Pan Tadeusz', 'Dziady', 'Grażyna') are deeply rooted in the folklore, landscapes, and heritage of Belarusian lands."
        },
        "ignacy-domeyko": {
            "by": "Нарадзіўся ў маёнтку Мядзвядка Навагрудскага павета (цяпер Карэліцкі раён Гродзенскай вобласці). Сябра таварыства філаматаў і блізкі сябар Адама Міцкевіча, удзельнік вызваленчага паўстання 1830–1831 гг. У эміграцыі стаў выдатным геолагам, рэктарам Чылійскага ўніверсітэта і нацыянальным героем Чылі.",
            "ru": "Родился в имении Медвядка Новогрудского уезда (Гродненская область). Член общества филоматов, сподвижник Мицкевича, участник восстания 1830–1831 гг. Национальный герой Чили, ректор Чилийского университета.",
            "en": "Born in Myadzvyadka near Karelichy (Hrodna region). Member of the Philomaths, comrade of Mickiewicz, and veteran of the 1831 Uprising. Became the founding father of Chilean science, mineralogy, and rector of the University of Chile."
        },
        "nikolai-sudzilovsky": {
            "by": "Ураджэнец Магілёва, выпускнік Магілёўскай гімназіі. Выдатны навуковец, этнограф, доктар медыцыны і рэвалюцыянер. Заўсёды падкрэсліваў сваё беларускае паходжанне. У 1895 г. пасяліўся на Гаваі (пад імем Нікалас Расэль), змагаўся за правы карэнных жыхароў канакаў і ў 1901 г. быў абраны першым прэзідэнтам Сената тэрыторыі Гаваі.",
            "ru": "Уроженец Могилёва. Ученый, этнограф, доктор медицины. Неизменно подчеркивал своё белорусское происхождение. В 1895 г. поселился на Гавайях (Николас Рассель), где защищал права коренного населения и был избран первым президентом Сената территории Гавайи.",
            "en": "Born in Mogilev. Renowned physician, ethnographer, and natural scientist who proudly maintained his Belarusian heritage. Settling in Hawaii as Nicholas Russel, he advocated for native rights and was elected the first President of the Senate of Hawaii in 1901."
        },
        "eliza-orzeszkowa": {
            "by": "Нарадзілася ў маёнтку Мількаўшчына пад Гроднам, амаль усё жыццё пражыла і тварыла ў Гродне. Удзельніца падтрымкі вызваленчага паўстання 1863 года. Выдатная пісьменніца, чые творы («Над Нёманам», «Хам», «Нізіны») прысвечаны лёсам, мове, фальклору і душы беларускага сялянства і шляхты Панямоння.",
            "ru": "Родилась в имении Мильковщина близ Гродно, всю жизнь жила и творила в Гродно. Поддерживала восстание 1863 года. Автор классических романов («Над Неманом», «Хам»), увековечивших жизнь, язык и культуру белорусского Понеманья.",
            "en": "Born near Hrodna, where she spent her life writing. Supported the 1863 January Uprising. Her realist epics ('Nad Niemnem', 'Cham') are dedicated entirely to the culture, language, and pastoral spirit of the people along the Neman River."
        },
        "yafim-karski": {
            "by": "Ураджэнец вёскі Лаша Гродзенскага павета. Пачынальнік навуковага беларусазнаўства, акадэмік Пецярбургскай акадэміі навук. Аўтар фундаментальнай трохтамовай энцыклапедыі «Беларусы» (1903–1922), якая навукова вызначыла моўныя межы беларускага этнасу і даказала самастойнасць беларускай мовы і нацыі.",
            "ru": "Родился в деревне Лаша Гродненского уезда. Основоположник научного белорусоведения, академик. Автор монументального труда «Белорусы» (1903–1922), научно обосновавшего самобытность белорусского языка и границы этноса.",
            "en": "Born near Hrodna. The founding father of academic Belarusian linguistics and ethnography. Author of the landmark three-volume encyclopedia 'The Belarusians' (1903–1922), which defined the linguistic borders and autonomy of the nation."
        },
        "jan-matejko": {
            "by": "Выдатны мастак гістарычнага жанру, чые найгалоўнейшыя творы прысвечаны гісторыі беларускіх зямель і ВКЛ. Аўтар палотнаў «Бітва пад Грунвальдам» (з вялікім князем Вітаўтам у цэнтры і віленскімі і полацкімі харугвамі), «Рэйтан — заняпад Польшчы» (пра беларускага шляхціца з Грушаўкі Тадэвуша Рэйтана), «Стэфан Баторый пад Псковам» і «Люблінская унія».",
            "ru": "Выдающийся живописец, посвятивший главные полотна истории ВКЛ и белорусских земель: «Грюнвальдская битва» (с князем Витовтом и полоцкими хоругвями), «Рейтан — упадок Польши» (о шляхтиче из Грушевки Тадеуше Рейтане), «Стефан Баторий под Псковом» и «Люблинская уния».",
            "en": "Master historical painter whose defining epics depict the heritage of the Grand Duchy of Lithuania: the 'Battle of Grunwald' (centering Grand Duke Vytautas and Polatsk banners), 'Rejtan' (honoring the Navahrudak envoy Tadeusz Rejtan), and the 'Union of Lublin'."
        },
        "henryk-siemiradzki": {
            "by": "Паходзіў са старадаўняга шляхецкага роду Семірадскіх герба «Лебедзь» з Навагрудчыны. Выбітны прадстаўнік еўрапейскага акадэмізму. У 1879 годзе падарыў Кракаву сваё грандыёзнае палатно «Светачы хрысціянства» («Pochodnie Nerona»), што стала пачаткам Нацыянальнага музея ў Сукенніцах.",
            "ru": "Происходил из шляхетского рода Семирадских герба «Лебедь» из-под Новогрудка. Мастер европейского академизма. В 1879 г. подарил Кракову грандиозное полотно «Светочи христианства» («Факелы Нерона»), положив начало Национальному музею в Суконных рядах.",
            "en": "Descended from the noble Siemiradzki family rooted in Navahrudak. Eminent master of European academic classicism whose donation of 'Nero's Torches' in 1879 founded the National Museum at the Sukiennice in Kraków."
        },
        "stanislaw-zukowski": {
            "by": "Нарадзіўся ў маёнтку Ендрыхаўцы Гродзенскай губерні (цяпер Ваўкавыскі раён). Выбітны мастак-пейзажыст, вучань Ісака Левітана. У сваіх карцінах узнёсла апяваў беларускую прыроду, лясы і непаўторны свет старадаўніх шляхецкіх сядзіб Панямоння.",
            "ru": "Родился в имении Ендриховцы Гродненской губернии (Волковысский район). Художник-пейзажист, ученик Левитана. Воспел природу Беларуси, леса и поэтику старинных дворянских усадеб Понеманья.",
            "en": "Born in Yendrykhaŭtsy (Vawkavysk district, Hrodna region). Impressionist landscape painter who immortalized the twilight forests, seasons, and noble country estates of Western Belarus."
        },
        "louis-b-mayer": {
            "by": "Нарадзіўся ў Мінску ў яўрэйскай сям'і. Кінематаграфічны магнат, сузаснавальнік і кіраўнік найбуйнейшай галівудскай кінастудыі залатога веку Metro-Goldwyn-Mayer (MGM). У 1927 годзе выступіў галоўным ініцыятарам стварэння Амерыканскай кінаакадэміі і прэміі «Оскар».",
            "ru": "Родился в Минске. Кинопродюсер, создатель студии Metro-Goldwyn-Mayer (MGM) и главный инициатор основания Американской киноакадемии и премии «Оскар» (1927).",
            "en": "Born in Minsk. Legendary titan of the Golden Age of Hollywood, head of Metro-Goldwyn-Mayer (MGM), and visionary creator of the Academy of Motion Picture Arts and Sciences and the Oscar awards."
        },
        "irving-berlin": {
            "by": "Нарадзіўся ў мястэчку Талачын (цяпер Віцебская вобласць). Выдатны амерыканскі кампазітар, класік сусветнай музыкі, аўтар больш за 1500 песень, у тым ліку неафіцыйнага гімна ЗША «God Bless America» і культавай «White Christmas» — найбольш прадаванай песні ў гісторыі гуказапісу.",
            "ru": "Родился в местечке Толочин (Витебская область). Выдающийся композитор, автор более 1500 песен, включая неофициальный гимн США «God Bless America» и рекордный сингл «White Christmas».",
            "en": "Born in Talachyn (Vitebsk region). Foremost American songwriter of the 20th century, creator of over 1,500 classic melodies including 'God Bless America' and 'White Christmas'."
        },
        "david-sarnoff": {
            "by": "Нарадзіўся ў мястэчку Узляны Ігуменскага павета (цяпер Пухавіцкі раён Мінскай вобласці). Піянер сусветнага радыё- і тэлевяшчання, прэзідэнт медыягіганта RCA, заснавальнік тэлесеткі NBC, кіраўнік будаўніцтва знакамітага хмарачоса 30 Rockefeller Plaza у Нью-Ёрку.",
            "ru": "Родился в местечке Узляны под Минском. Пионер коммерческого радиовещания и телевидения, президент корпорации RCA, основатель сети NBC.",
            "en": "Born in Uzlyany near Minsk. Telecommunications visionary, longtime president of RCA, and founder of the NBC broadcasting network based at 30 Rockefeller Plaza."
        },
        "chaim-weizmann": {
            "by": "Нарадзіўся ў мястэчку Моталь Кобрынскага павета (цяпер Іванаўскі раён Брэсцкай вобласці). Выбітны навуковец-біяхімік, вынаходнік, шматгадовы лідар сусветнага сіянісцкага руху. Першы прэзідэнт Дзяржавы Ізраіль (1949–1952), заснавальнік знакамітага навукова-даследчага Інстытута Вайцмана ў Рэхавоце.",
            "ru": "Родился в местечке Мотоль (Брестская область). Учёный-биохимик, первый президент Государства Израиль (1949–1952), основатель Института Вейцмана в Реховоте.",
            "en": "Born in Motal (Brest region). Distinguished biochemist, leader of the Zionist movement, and the first President of the State of Israel (1949–1952). Founder of the Weizmann Institute of Science."
        },
        "shimon-peres": {
            "by": "Нарадзіўся ў вёсцы Вішнева Валожынскага раёна Мінскай вобласці. Выбітны дзяржаўны дзеяч, патрыярх ізраільскай палітыкі, двойчы прэм'ер-міністр і 9-ы прэзідэнт Ізраіля (2007–2014). Лаўрэат Нобелеўскай прэміі міру (1994), заснавальнік Цэнтра міру і інавацый у Яфе.",
            "ru": "Родился в деревне Вишнево Воложинского района Минской области. Патриарх израильской политики, дважды премьер-министр и 9-й президент Израиля, лауреат Нобелевской премии мира (1994).",
            "en": "Born in Vishneva (Valozhyn district, Minsk region). Founding father of Israeli statehood, two-time Prime Minister, and 9th President of Israel (2007–2014). Nobel Peace Prize laureate (1994)."
        },
        "isaac-asimov": {
            "by": "Нарадзіўся ў мястэчку Пятровічы Клімавіцкага павета (тады Гомельская губерня / БССР). Сусветна вядомы амерыканскі пісьменнік-фантаст, папулярызатар навукі, прафесар біяхіміі Бостанскага ўніверсітэта. Аўтар Трох законаў робататэхнікі і легендарных цыклаў «Фундацыя» і «Я, робат».",
            "ru": "Родился в местечке Петровичи (тогда Гомельская губерния / БССР). Всемирно известный писатель-фантаст, биохимик, создатель Трёх законов робототехники и эпопеи «Основание».",
            "en": "Born in Petrovichi (then Gomel Governorate). Master science fiction writer, biochemist, and author of over 500 books, creator of the Three Laws of Robotics and the 'Foundation' saga."
        }
    }
    
    for pid, conn in BELARUS_CONNECTIONS.items():
        if pid in persons_map:
            persons_map[pid]['bio']['by'] = conn['by']
            persons_map[pid]['bio']['ru'] = conn['ru']
            persons_map[pid]['bio']['en'] = conn['en']

    # Update images via Wikipedia API
    for pid, p in persons_map.items():
        wiki = p.get('wiki', '')
        if wiki:
            img = fetch_wiki_image(wiki)
            if img:
                p['image'] = img
                print(f"Verified image for {pid}: {img}")
            else:
                print(f"Retained existing image for {pid}: {p.get('image')}")
                
    # Recalculate placeIds for all persons
    final_places = list(places_map.values())
    for pid, p in persons_map.items():
        connected_place_ids = set(p.get('placeIds', []))
        for place in final_places:
            if place.get('personId') == pid:
                connected_place_ids.add(place['id'])
            if pid in place.get('personIds', []):
                connected_place_ids.add(place['id'])
            if 'items' in place and isinstance(place['items'], list):
                for item in place['items']:
                    if item.get('personId') == pid:
                        connected_place_ids.add(place['id'])
        p['placeIds'] = sorted(list(connected_place_ids))

    final_persons = list(persons_map.values())
    print(f"\nFinal Places count: {len(final_places)}")
    print(f"Final Persons count: {len(final_persons)}")

    # Save data/places.json
    with open('data/places.json', 'w', encoding='utf-8') as f:
        json.dump(final_places, f, ensure_ascii=False, indent=2)
    with open('data/places.js', 'w', encoding='utf-8') as f:
        f.write("window.PLACES_DATA = ")
        json.dump(final_places, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print("Saved places files.")

    # Save data/persons.json
    with open('data/persons.json', 'w', encoding='utf-8') as f:
        json.dump(final_persons, f, ensure_ascii=False, indent=2)
    with open('data/persons.js', 'w', encoding='utf-8') as f:
        f.write("window.PERSONS_DATA = ")
        json.dump(final_persons, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print("Saved persons files.")

if __name__ == '__main__':
    main()
