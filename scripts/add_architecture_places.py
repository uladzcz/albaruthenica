import json

def main():
    with open('data/places.json', 'r', encoding='utf-8') as f:
        places = json.load(f)

    with open('data/persons.json', 'r', encoding='utf-8') as f:
        persons = json.load(f)

    existing_place_ids = {p['id'] for p in places}
    existing_person_ids = {p['id'] for p in persons}

    arch_places = [
        {
            "id": "spb-saint-petersburg-mosque-krichinsky",
            "title": {
                "by": "Санкт-Пецярбургская саборная мячэць (архітэктар Сцяпан Крычынскі)",
                "ru": "Санкт-Петербургская соборная мечеть (архитектор Степан Кричинский)",
                "en": "Saint Petersburg Mosque (Architect Stepan Krichinsky)"
            },
            "category": "culture",
            "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
            "city": {"by": "Санкт-Пецярбург", "ru": "Санкт-Петербург", "en": "Saint Petersburg"},
            "coordinates": [59.955300, 30.323900],
            "description": {
                "by": "Адрас: Кронверкскі праспект, 7, Санкт-Пецярбург.\n\nНайбуйнейшая мячэць у еўрапейскай частцы Расійскай імперыі (1910–1913), пабудаваная па праекце беларускага шляхціца-татара Сцяпана Крычынскага (ураджэнца маёнтка Каскевічы Ашмянскага павета). Крычынскі спалучыў традыцыі ўсходняга дойлідства Самарканда з паўночным мадэрнам. Ён таксама пабудаваў у Пецярбургу дом Эміра Бухарскага (Каменнаастроўскі пр-т, 44б) і Фёдараўскі сабор.",
                "ru": "Кронверкский проспект 7, Санкт-Петербург. Соборная мечеть, построенная по проекту белорусско-татарского архитектора Степана Кричинского (уроженца Ошмянского уезда).",
                "en": "Saint Petersburg Mosque on Kronverksky Prospekt, designed by Belarusian-Tatar architect Stepan Krichinsky from Ashmyany district. Built in 1910–1913 blending Samarkand motifs with Northern Art Nouveau."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Saint_Petersburg_Mosque_2016.jpg/800px-Saint_Petersburg_Mosque_2016.jpg",
            "links": [
                {"title": "Наша Ніва: Чым расійская архітэктура абавязана Беларусі", "url": "https://nashaniva.com/339527"},
                {"title": "Санкт-Пецярбургская саборная мячэць (be.wikipedia)", "url": "https://be.wikipedia.org/wiki/Санкт-Пецярбургская_саборная_мячэць"}
            ],
            "tags": ["Расія", "Пецярбург", "Крычынскі", "архітэктура", "culture"],
            "personIds": ["stepan-krichinsky"]
        },
        {
            "id": "moscow-cathedral-immaculate-conception-dvorzhetsky",
            "title": {
                "by": "Кафедральны сабор Беззаганнага Зачацця ў Маскве (архітэктар Тамаш Багдановіч-Дваржэцкі)",
                "ru": "Собор Непорочного Зачатия в Москве (архитектор Фома Богданович-Дворжецкий)",
                "en": "Cathedral of the Immaculate Conception in Moscow (Tomasz Bohdanowicz-Dworzecki)"
            },
            "category": "church",
            "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
            "city": {"by": "Масква", "ru": "Москва", "en": "Moscow"},
            "coordinates": [55.768100, 37.571400],
            "description": {
                "by": "Адрас: Малая Грузінская вул., 27/13, Масква.\n\nГалоўны каталіцкі кафедральны сабор Расіі, шэдэўр неаготыкі (1901–1911), спраектаваны ўраджэнцам Віцебска Тамашам Багдановічам-Дваржэцкім (з роду мсціслаўскіх баяр). Агароджу выканаў віленскі дойлід Лявон Даўкша. Пасля савецкага заняпаду сабор быў адроджаны ў 1990-я гады мітрапалітам Тадэвушам Кандрусевічам.",
                "ru": "Малая Грузинская ул., 27/13, Москва. Кафедральный собор Непорочного Зачатия Девы Марии, шедевр неоготики, спроектированный уроженцем Витебска Фомой Богдановичем-Дворжецким.",
                "en": "Cathedral of the Immaculate Conception in Moscow, a grand Neo-Gothic cathedral built in 1901–1911 to the design of Vitebsk-born architect Tomasz Bohdanowicz-Dworzecki."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Cathedral_of_the_Immaculate_Conception_Moscow_01.jpg/800px-Cathedral_of_the_Immaculate_Conception_Moscow_01.jpg",
            "links": [
                {"title": "Наша Ніва: Чым расійская архітэктура абавязана Беларусі", "url": "https://nashaniva.com/339527"},
                {"title": "Сабор Беззаганнага Зачацця (be.wikipedia)", "url": "https://be.wikipedia.org/wiki/Сабор_Беззаганнага_Зачацця_Найсвяцейшай_Дзевы_Марыі_(Масква)"}
            ],
            "tags": ["Расія", "Масква", "Багдановіч-Дваржэцкі", "касцёл", "неаготыка", "church"],
            "personIds": ["tomasz-dvorzhetsky"],
            "mustSee": True
        },
        {
            "id": "samara-sacred-heart-church-dvorzhetsky",
            "title": {
                "by": "Касцёл Найсвяцейшага Сэрца Ісуса ў Самары (архітэктар Тамаш Багдановіч-Дваржэцкі)",
                "ru": "Храм Пресвятого Сердца Иисуса в Самаре (архитектор Фома Богданович-Дворжецкий)",
                "en": "Church of the Sacred Heart in Samara (Tomasz Bohdanowicz-Dworzecki)"
            },
            "category": "church",
            "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
            "city": {"by": "Самара", "ru": "Самара", "en": "Samara"},
            "coordinates": [53.195800, 50.098300],
            "description": {
                "by": "Адрас: вул. Фрунзэ, 157, Самара.\n\nЗнакаміты «Польскі касцёл» у Самары (1906), выдатны ўзор псеўдаготыкі, збудаваны па праекце ўраджэнца Віцебска Тамаша Багдановіча-Дваржэцкага. У вытанчаных спічастых вежах і арачным дэкоры аўтар працытаваў матывы славутага касцёла Святой Ганны ў Вільні.",
                "ru": "Ул. Фрунзе, 157, Самара. Храм Пресвятого Сердца Иисуса («Польский костёл», 1906 г.), построенный витеблянином Фомой Богдановичем-Дворжецким с мотивами костёла св. Анны в Вильне.",
                "en": "Church of the Sacred Heart of Jesus in Samara (1906), Neo-Gothic Catholic church designed by Vitebsk-born Tomasz Bohdanowicz-Dworzecki, echoing the facade of St. Anne's Church in Vilnius."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Samara_Catholic_Church_2011.jpg/800px-Samara_Catholic_Church_2011.jpg",
            "links": [
                {"title": "Наша Ніва: Чым расійская архітэктура абавязана Беларусі", "url": "https://nashaniva.com/339527"}
            ],
            "tags": ["Расія", "Самара", "Багдановіч-Дваржэцкі", "касцёл", "church"],
            "personIds": ["tomasz-dvorzhetsky"]
        },
        {
            "id": "moscow-pigit-house-yuditsky-bulgakov",
            "title": {
                "by": "Дом Пігіта і «Нядобрая кватэра» ў Маскве (архітэктар Эдмунд Юдзіцкі)",
                "ru": "Дом Пигита и «Нехорошая квартира» в Москве (архитектор Эдмунд Юдицкий)",
                "en": "Pigit House in Moscow (Architect Edmund Yuditsky)"
            },
            "category": "culture",
            "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
            "city": {"by": "Масква", "ru": "Москва", "en": "Moscow"},
            "coordinates": [55.766900, 37.593600],
            "description": {
                "by": "Адрас: Вялікая Садовая вул., 10, Масква.\n\nДаходны дом у стылі мадэрн, пабудаваны ў 1902–1903 гадах архітэктарам Эдмундам Юдзіцкім (выхадцам з мястэчка Глуск Бабруйскага павета). У гэтым доме ў пакоі камуналкі жыў Міхаіл Булгакаў; менавіта гэтая кватэра стала правобразам знакамітай «нядобрай кватэры № 50» у рамане «Майстар і Маргарыта». Сёння тут дзейнічае Музей Булгакава.",
                "ru": "Большая Садовая ул., 10, Москва. Доходный дом Ильи Пигита в стиле модерн, построенный уроженцем Глуска Эдмундом Юдицким. Прообраз «нехорошей квартиры» из романа «Мастер и Маргарита».",
                "en": "Art Nouveau apartment building at 10 Bolshaya Sadovaya St, Moscow, designed in 1902–1903 by Belarusian architect Edmund Yuditsky from Hlusk. Inspiration for the 'Odd Flat' in Bulgakov's The Master and Margarita."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Bolshaya_Sadovaya_10_Moscow.jpg/800px-Bolshaya_Sadovaya_10_Moscow.jpg",
            "links": [
                {"title": "Наша Ніва: Чым расійская архітэктура абавязана Беларусі", "url": "https://nashaniva.com/339527"},
                {"title": "Дом Пигита (ru.wikipedia)", "url": "https://ru.wikipedia.org/wiki/Дом_Пигита"}
            ],
            "tags": ["Расія", "Масква", "Юдзіцкі", "Булгакаў", "culture"],
            "personIds": ["edmund-yuditsky"]
        },
        {
            "id": "moscow-narkomfin-building-ginzburg",
            "title": {
                "by": "Дом Наркамфіна ў Маскве (архітэктар Майсей Гінзбург)",
                "ru": "Дом Наркомфина в Москве (архитектор Моисей Гинзбург)",
                "en": "Narkomfin Building in Moscow (Architect Moisei Ginzburg)"
            },
            "category": "culture",
            "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
            "city": {"by": "Масква", "ru": "Москва", "en": "Moscow"},
            "coordinates": [55.753300, 37.581900],
            "description": {
                "by": "Адрас: Новінскі бульвар, 25, Масква.\n\nСусветна вядомы помнік савецкага канструктывізму (1928–1930), створаны ўраджэнцам Менска Майсеем Гінзбургам — лідарам і галоўным тэарэтыкам канструктывізму ў архітэктуры. Дом вылучаецца эксперыментальнай стужкавай шкляной забудовай, двухузроўневымі ячэйкамі і эрганамічнымі грамадскімі прасторамі.",
                "ru": "Новинский бульвар, 25, Москва. Шедевр конструктивизма, созданный уроженцем Минска Моисеем Гинзбургом в 1928–1930 гг.",
                "en": "Landmark constructivist building in Moscow (1928–1930) by Minsk-born architect Moisei Ginzburg, pioneering functionalist housing concepts."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Narkomfin_Building_2020.jpg/800px-Narkomfin_Building_2020.jpg",
            "links": [
                {"title": "Наша Ніва: Чым расійская архітэктура абавязана Беларусі", "url": "https://nashaniva.com/339527"},
                {"title": "Дом Наркамфіна (be.wikipedia)", "url": "https://be.wikipedia.org/wiki/Дом_Наркамфіна"}
            ],
            "tags": ["Расія", "Масква", "Гінзбург", "канструктывізм", "culture"],
            "personIds": ["moisei-ginzburg"],
            "mustSee": True
        },
        {
            "id": "saint-remy-glanum-mausoleum-naroulia",
            "title": {
                "by": "Маўзалей Юліяў у Сен-Рэмі-дэ-Праванс (прататып Нараўлянскай альтанкі)",
                "ru": "Мавзолей Юлиев в Сен-Реми-де-Прованс (прототип Наровлянской альтанки)",
                "en": "Mausoleum of Glanum in Saint-Rémy-de-Provence"
            },
            "category": "historical",
            "country": {"by": "Францыя", "ru": "Франция", "en": "France"},
            "city": {"by": "Сен-Рэмі-дэ-Праванс", "ru": "Сен-Реми-де-Прованс", "en": "Saint-Rémy-de-Provence"},
            "coordinates": [43.774400, 4.832200],
            "description": {
                "by": "Адрас: Les Antiques, Saint-Rémy-de-Provence, France.\n\nСтаражытнарымскі маўзалей 30–20 гг. да н.э., адзін з найлепш захаваных антычных манументаў Галіі. Менавіта ім натхніліся ўладальнікі маёнтка Нароўля Артур і Эдвард Горваты, якія пасля падарожжа ў Праванс у сярэдзіне XIX стагоддзя пабудавалі па яго дакладных формах знакамітую трох'ярусную альтанку-маяк над ракой Прыпяць у Нароўлі.",
                "ru": "Древнеримский мавзолей Юлия в Глануме (Сен-Реми-де-Прованс, Франция). Послужил прототипом для знаменитой трехъярусной усадебной альтанки-маяка Горваттов на Припяти в Наровле.",
                "en": "Ancient Roman Mausoleum of Glanum (Les Antiques) in Provence, France (c. 30–20 BC). Inspired the Horwatt family to construct their iconic three-tiered gazebo-lighthouse overlooking the Pripyat River in Naroulia, Belarus."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Saint-R%C3%A9my-de-Provence_-_Mausol%C3%A9e_de_Glanum.jpg/800px-Saint-R%C3%A9my-de-Provence_-_Mausol%C3%A9e_de_Glanum.jpg",
            "links": [
                {"title": "Наша Ніва: У альтанкі ў Нароўлі адшукаўся старажытны прататып", "url": "https://nashaniva.com/341784"},
                {"title": "Маўзалей у Глануме (fr.wikipedia)", "url": "https://fr.wikipedia.org/wiki/Mausolée_de_Glanum"}
            ],
            "tags": ["Францыя", "Горваты", "Нароўля", "антычнасць", "historical"]
        }
    ]

    for p in arch_places:
        if p['id'] not in existing_place_ids:
            places.append(p)
            existing_place_ids.add(p['id'])

    arch_persons = [
        {
            "id": "stepan-krichinsky",
            "name": {
                "by": "Сцяпан Крычынскі",
                "ru": "Степан Кричинский",
                "en": "Stepan Krichinsky"
            },
            "role": {
                "by": "Архітэктар, майстар мадэрну і неакласіцызму",
                "ru": "Архитектор, мастер модерна и неоклассицизма",
                "en": "Architect, master of Art Nouveau and Neoclassicism"
            },
            "years": "1874–1923",
            "birthPlace": "маёнтак Каскевічы (Ашмянскі павет)",
            "description": {
                "by": "Беларуска-татарскі архітэктар са шляхецкага роду князёў Крычынскіх герба «Радван». Аўтар праекта Санкт-Пецярбургскай саборнай мячэці, дома Эміра Бухарскага і Фёдараўскага сабора.",
                "ru": "Архитектор из белорусско-татарского дворянского рода. Автор Санкт-Петербургской соборной мечети и дома Эмира Бухарского.",
                "en": "Belarusian-Tatar architect from Ashmyany district. Designer of the Saint Petersburg Mosque and Emir of Bukhara House."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Saint_Petersburg_Mosque_2016.jpg/800px-Saint_Petersburg_Mosque_2016.jpg",
            "wiki": "https://ru.wikipedia.org/wiki/Кричинский,_Степан_Самойлович",
            "placeIds": ["spb-saint-petersburg-mosque-krichinsky"]
        },
        {
            "id": "tomasz-dvorzhetsky",
            "name": {
                "by": "Тамаш Багдановіч-Дваржэцкі",
                "ru": "Фома Богданович-Дворжецкий",
                "en": "Tomasz Bohdanowicz-Dworzecki"
            },
            "role": {
                "by": "Архітэктар, майстар неаготыкі, акадэмік архітэктуры",
                "ru": "Архитектор, мастер неоготики, академик архитектуры",
                "en": "Architect, master of Neo-Gothic architecture"
            },
            "years": "1859–1920",
            "birthPlace": "Віцебск (з мсціслаўскіх баяр)",
            "description": {
                "by": "Выбітны архітэктар з беларускай шляхты Віцебшчыны. Аўтар Кафедральнага сабора Беззаганнага Зачацця ў Маскве і касцёла Сэрца Ісуса ў Самары.",
                "ru": "Архитектор родом из Витебска. Автор собора Непорочного Зачатия в Москве и храма Пресвятого Сердца Иисуса в Самаре.",
                "en": "Architect born in Vitebsk. Designer of the Cathedral of the Immaculate Conception in Moscow and Catholic Church in Samara."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Cathedral_of_the_Immaculate_Conception_Moscow_01.jpg/800px-Cathedral_of_the_Immaculate_Conception_Moscow_01.jpg",
            "wiki": "https://ru.wikipedia.org/wiki/Богданович-Дворжецкий,_Фома_Осипович",
            "placeIds": [
                "moscow-cathedral-immaculate-conception-dvorzhetsky",
                "samara-sacred-heart-church-dvorzhetsky"
            ]
        },
        {
            "id": "edmund-yuditsky",
            "name": {
                "by": "Эдмунд Юдзіцкі",
                "ru": "Эдмунд Юдицкий",
                "en": "Edmund Yuditsky"
            },
            "role": {
                "by": "Архітэктар маскоўскага мадэрну",
                "ru": "Архитектор московского модерна",
                "en": "Moscow Art Nouveau architect"
            },
            "years": "1838–1908",
            "birthPlace": "Глуск (Бабруйскі павет, Мінская губерня)",
            "description": {
                "by": "Архітэктар, ураджэнец Глуска. Аўтар знакамітага даходнага дома Пігіта на Вялікай Садовай, 10 у Маскве («нядобрая кватэра» Булгакава).",
                "ru": "Архитектор, уроженец Глуска. Автор знаменитого дома Пигита в Москве (прообраз «нехорошей квартиры» Булгакова).",
                "en": "Architect born in Hlusk, Belarus. Designer of the Pigit House on Bolshaya Sadovaya in Moscow (Bulgakov's 'Odd Flat')."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Bolshaya_Sadovaya_10_Moscow.jpg/800px-Bolshaya_Sadovaya_10_Moscow.jpg",
            "wiki": "https://ru.wikipedia.org/wiki/Юдицкий,_Эдмунд_Станиславович",
            "placeIds": ["moscow-pigit-house-yuditsky-bulgakov"]
        },
        {
            "id": "moisei-ginzburg",
            "name": {
                "by": "Майсей Гінзбург",
                "ru": "Моисей Гинзбург",
                "en": "Moisei Ginzburg"
            },
            "role": {
                "by": "Архітэктар-авангардыст, галоўны тэарэтык канструктывізму",
                "ru": "Архитектор-авангардист, главный теоретик конструктивизма",
                "en": "Constructivist architect and architectural theorist"
            },
            "years": "1892–1946",
            "birthPlace": "Мінск",
            "description": {
                "by": "Ураджэнец Мінска, лідар савецкага канструктывізму, заснавальнік АСА (Аб'яднанне сучасных архітэктараў). Аўтар шэдэўра канструктывізму — дома Наркамфіна ў Маскве.",
                "ru": "Уроженец Минска, лидер советского конструктивизма. Создатель дома Наркомфина в Москве.",
                "en": "Minsk-born leading theorist of Soviet constructivism. Architect of the landmark Narkomfin Building in Moscow."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Narkomfin_Building_2020.jpg/800px-Narkomfin_Building_2020.jpg",
            "wiki": "https://be.wikipedia.org/wiki/Майсей_Якаўлевіч_Гінзбург",
            "placeIds": ["moscow-narkomfin-building-ginzburg"]
        }
    ]

    for p in arch_persons:
        if p['id'] not in existing_person_ids:
            persons.append(p)
            existing_person_ids.add(p['id'])

    with open('data/places.json', 'w', encoding='utf-8') as f:
        json.dump(places, f, ensure_ascii=False, indent=2)

    with open('data/persons.json', 'w', encoding='utf-8') as f:
        json.dump(persons, f, ensure_ascii=False, indent=2)

    with open('data/places.js', 'w', encoding='utf-8') as f:
        f.write('window.INITIAL_PLACES = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

    with open('data/persons.js', 'w', encoding='utf-8') as f:
        f.write('window.INITIAL_PERSONS = ' + json.dumps(persons, ensure_ascii=False, indent=2) + ';\n')

    print(f"Total places: {len(places)}, Total persons: {len(persons)}")

if __name__ == '__main__':
    main()
