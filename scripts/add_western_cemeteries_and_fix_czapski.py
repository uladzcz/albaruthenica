# -*- coding: utf-8 -*-
"""
1. Merge duplicate Czapski museums and fix Polish Wikipedia link.
2. Add new Western European cemetery sites & figures:
   - Montmorency Cemetery (Julian Ursyn Niemcewicz, Aleksander Chodzko, Leonard Chodzko)
   - Montmartre Cemetery (Walenty Wańkowicz)
   - Montparnasse Cemetery (Ossip Zadkine grave)
   - London St. Pancras & Islington Cemetery (Belarusian Pantheon: Bishop Ceslaus Sipovich, Fr. Alexander Nadson)
   - Rapperswil Castle (Count Władysław Plater, Polish-Lithuanian Museum & Kościuszko mausoleum)
   - Sayn Palace Crypt (Princess Leonilla Sayn-Wittgenstein-Sayn / Mir Castle)
   - Warsaw Powązki (Stanisław Moniuszko)
   - Wilanów Radziwiłł Crypt (Janusz Radziwiłł)
"""

import json

with open('data/places.json', 'r', encoding='utf-8') as f:
    places = json.load(f)

with open('data/persons.json', 'r', encoding='utf-8') as f:
    persons = json.load(f)

places_map = {p['id']: p for p in places}
persons_map = {p['id']: p for p in persons}

# -------------------------------------------------------------
# 1. FIX CZAPSKI DUPLICATE & WIKIPEDIA LINK
# -------------------------------------------------------------

# Remove duplicate unverified krakow-hutten-czapski-museum
if 'krakow-hutten-czapski-museum' in places_map:
    del places_map['krakow-hutten-czapski-museum']

# Ensure krakow-muzeum-emeryka-hutten-czapskiego has both working Wikipedia links
if 'krakow-muzeum-emeryka-hutten-czapskiego' in places_map:
    p = places_map['krakow-muzeum-emeryka-hutten-czapskiego']
    p['links'] = [
        {
            "title": "Muzeum im. Emeryka Hutten-Czapskiego (MNK)",
            "url": "https://mnk.pl/oddzial/muzeum-im-emeryka-hutten-czapskiego"
        },
        {
            "title": "Вікіпедыя: Музей імя Эмерыка Гутэн-Чапскага",
            "url": "https://be.wikipedia.org/wiki/Музей_імя_Эмерыка_Гутэн-Чапскага"
        },
        {
            "title": "Wikipedia: Muzeum im. Emeryka Hutten-Czapskiego",
            "url": "https://pl.wikipedia.org/wiki/Muzeum_im._Emeryka_Hutten-Czapskiego"
        },
        {
            "title": "Maldzis.world: Дзе на карце Кракава знайсці Беларусь",
            "url": "https://maldzis.world/dze-na-karce-polskaga-krakava-znajsci-belarus/"
        }
    ]

# -------------------------------------------------------------
# 2. NEW PERSONS (Western Europe)
# -------------------------------------------------------------

new_persons = [
    {
        "id": "yulian-ursyn-nyamtsevich",
        "name": {
            "by": "Юльян Урсын Нямцэвіч",
            "ru": "Юлиан Урсын Немцевич",
            "en": "Julian Ursyn Niemcewicz"
        },
        "years": "1758–1841",
        "role": {
            "by": "Пісьменнік, драматург, гісторык, паплечнік Тадэвуша Касцюшкі",
            "ru": "Писатель, драматург, историк, соратник Тадеуша Костюшко",
            "en": "Writer, playwright, historian, aide-de-camp to Tadeusz Kościuszko"
        },
        "bio": {
            "by": "Ураджэнец маёнтка Скокі пад Брэстам (сядзіба Нямцэвічаў). Адзін з найвыбітнейшых дзеячаў Чатырохгадовага Сойма і аўтараў Канстытуцыі 3 мая 1791 г. Ад'ютант і бліжэйшы паплечнік Тадэвуша Касцюшкі ў паўстанні 1794 г. Аўтар знакамітых «Гістарычных спеваў» і ўспамінаў. Пахаваны ў беларуска-польскім пантэоне эміграцыі на могілках Шампо ў Манмарансі пад Парыжам.",
            "ru": "Уроженец имения Скоки под Брестом. Деятель Четырёхлетнего Сейма, соавтор Конституции 3 мая 1791 года. Адъютант и соратник Тадеуша Костюшко. Похоронен на кладбище Монморанси под Парижем.",
            "en": "Born in Skoki near Brest. Statesman of the Great Sejm and co-author of the Constitution of May 3, 1791. Close aide-de-camp to Tadeusz Kościuszko during the 1794 Uprising. Buried in the Polish-Lithuanian Pantheon at Montmorency near Paris."
        },
        "photo": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Julian_Ursyn_Niemcewicz_11.PNG",
        "wiki": "https://be.wikipedia.org/wiki/%D0%AE%D0%BB%D1%8C%D1%8F%D0%BD_%D0%A3%D1%80%D1%81%D1%8B%D0%BD_%D0%9D%D1%8F%D0%BC%D1%86%D1%8D%D0%B2%D1%96%D1%87"
    },
    {
        "id": "aleksandr-chodzko",
        "name": {
            "by": "Аляксандр Ходзька",
            "ru": "Александр Ходзько",
            "en": "Aleksander Chodźko"
        },
        "years": "1804–1891",
        "role": {
            "by": "Паэт, усходазнавец, дыпламат, прафесар Калеж дэ Франс",
            "ru": "Поэт, востоковед, дипломат, профессор Коллеж де Франс",
            "en": "Poet, orientalist, diplomat, professor at the Collège de France"
        },
        "bio": {
            "by": "Ураджэнец мястэчка Крывічы (цяпер Мядзельскі раён). Сябра таварыства філаматаў, блізкі сябар Адама Міцкевіча. Выдатны паліглот, дыпламат і ўсходазнавец, даследчык персідскай літаратуры і фальклору. Пераемнік Адама Міцкевіча на пасадзе загадчыка кафедры славянскіх літаратур у прэстыжным Калеж дэ Франс у Парыжы (1857–1883). Пахаваны на могілках у Манмарансі.",
            "ru": "Уроженец Кривичей. Филомат, друг Адама Мицкевича. Востоковед и дипломат. Преемник Мицкевича на кафедре славянских литератур в Коллеж де Франс в Париже. Похоронен в Монморанси.",
            "en": "Born in Kryvichy. Philomath, close friend of Adam Mickiewicz. Renowned orientalist and diplomat. Succeeded Mickiewicz as professor of Slavic literatures at the Collège de France in Paris. Buried at Montmorency."
        },
        "photo": "https://upload.wikimedia.org/wikipedia/commons/7/77/Aleksander_Chod%C5%BAko.JPG",
        "wiki": "https://be.wikipedia.org/wiki/%D0%90%D0%BB%D1%8F%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%A5%D0%BE%D0%B4%D1%8C%D0%BA%D0%B0"
    },
    {
        "id": "leonard-chodzko",
        "name": {
            "by": "Леанард Ходзька",
            "ru": "Леонард Ходзько",
            "en": "Leonard Chodźko"
        },
        "years": "1800–1871",
        "role": {
            "by": "Гісторык, публіцыст, картограф, выдавец гісторыі ВКЛ і Беларусі",
            "ru": "Историк, публицист, картограф, издатель истории ВКЛ",
            "en": "Historian, publicist, cartographer, publisher of GDL history"
        },
        "bio": {
            "by": "Ураджэнец вёскі Аборак (цяпер Маладзечанскі раён). Вучыўся ў Віленскім універсітэце, быў філарэтам. Працаваў сакратаром кампазітара Міхала Клеафаса Агінскага. У Парыжы стаў адным з найбольш плённых гісторыкаў і прапагандыстаў гісторыі Беларусі, ВКЛ і Рэчы Паспалітай у Заходняй Еўропе, стварыў багатыя архівы і карты. Пахаваны ў Манмарансі.",
            "ru": "Уроженец деревни Оборок (Молодечненский район). Филарет, секретарь М. К. Огиньского. В Париже издавал фундаментальные труды и карты по истории ВКЛ и Речи Посполитой. Похоронен в Монморанси.",
            "en": "Born in Aborak near Maladzyechna. Philareth at Vilnius University, secretary to Michał Kleofas Ogiński. In Paris, published monumental works and historical maps on the Grand Duchy of Lithuania and Poland. Buried at Montmorency."
        },
        "photo": "https://upload.wikimedia.org/wikipedia/commons/7/77/Aleksander_Chod%C5%BAko.JPG",
        "wiki": "https://be.wikipedia.org/wiki/%D0%9B%D0%B5%D0%B0%D0%BD%D0%B0%D1%80%D0%B4_%D0%A5%D0%BE%D0%B4%D1%8C%D0%BA%D0%B0"
    },
    {
        "id": "valentsin-vankovich",
        "name": {
            "by": "Валянцін Ваньковіч",
            "ru": "Валентий Ванькович",
            "en": "Walenty Wańkowicz"
        },
        "years": "1800–1842",
        "role": {
            "by": "Класік беларускага і еўрапейскага жывапісу рамантызму",
            "ru": "Классик живописи эпохи романтизма",
            "en": "Classic Romantic portrait painter"
        },
        "bio": {
            "by": "Ураджэнец маёнтка Калюжыца Ігуменскага павета (цяпер Чэрвеньскі раён). Стваральнік знакамітых партрэтаў: «Міцкевіч на скале Аю-Даг», Марыі Шыманоўскай, Аляксандра Пушкіна, карціны «Напалеон каля вогнішча». Блізкі сябар Адама Міцкевіча. Памёр у Парыжы на руках у Міцкевіча. Пахаваны на знакамітых парыжскіх могілках Манмартр.",
            "ru": "Уроженец имения Калюжица (Червенский район). Автор знаменитого портрета «Мицкевич на скале Аю-Даг», портретов Пушкина, Шимановской. Близкий друг Мицкевича. Умер в Париже на руках поэта. Похоронен на кладбище Монмартр.",
            "en": "Born in Kałużyca near Cherven (Minsk region). Master of Romantic portraiture, painted the iconic 'Mickiewicz on the Ay-Dagh Cliff'. Close friend of Adam Mickiewicz, died in Paris in Mickiewicz's home. Buried at Montmartre Cemetery in Paris."
        },
        "photo": "https://upload.wikimedia.org/wikipedia/commons/9/90/Walenty_wankowicz.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%92%D0%B0%D0%BB%D1%8F%D0%BD%D1%86%D1%96%D0%BD_%D0%92%D0%B0%D0%BD%D1%8C%D0%BA%D0%BE%D0%B2%D1%96%D1%87"
    },
    {
        "id": "chaslau-sipovich",
        "name": {
            "by": "Біскуп Часлаў Сіповіч",
            "ru": "Епископ Чеслав Сипович",
            "en": "Bishop Ceslaus Sipovich"
        },
        "years": "1914–1981",
        "role": {
            "by": "Беларускі грэка-каталіцкі біскуп, заснавальнік Бібліятэкі і музея імя Скарыны ў Лондане",
            "ru": "Белорусский греко-католический епископ, основатель Библиотеки Скорины в Лондоне",
            "en": "Belarusian Greek Catholic Bishop, founder of the Francis Skaryna Library in London"
        },
        "bio": {
            "by": "Ураджэнец Дзісненшчыны (вёска Дзедзінка). Апостальскі візітатар для беларусаў-каталікоў у эміграцыі, тытулярны біскуп Марыямэтанскі. Генеральны суперыёр Кангрэгацыі айцоў марыянаў (Рым, 1963–1969). Заснавальнік і натхняльнік Беларускай бібліятэкі і музея імя Францыска Скарыны ў Лондане. Пахаваны на могілках Сэнт-Панкрас у Лондане.",
            "ru": "Уроженец Дисненщины. Апостольский визитатор для белорусов-католиков зарубежья. Генеральный супериор мариан в Риме. Основатель Белорусской библиотеки и музея им. Скорины в Лондоне. Похоронен в Лондоне.",
            "en": "Born in Dzyadzinka (Dzisna district). Apostolic Visitor for Belarusian Greek Catholics abroad. Superior General of the Marian Fathers in Rome (1963–1969). Founder of the Francis Skaryna Belarusian Library and Museum in London. Buried at St Pancras and Islington Cemetery, London."
        },
        "photo": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Biskup_Sipovich_u_biblijatecy.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%A7%D1%8D%D1%81%D0%BB%D0%B0%D1%9E_%D0%A1%D1%96%D0%BF%D0%BE%D0%B2%D1%96%D1%87"
    },
    {
        "id": "alyaksandr-nadsan",
        "name": {
            "by": "Айцец Аляксандр Надсан",
            "ru": "Отец Александр Надсон",
            "en": "Father Alexander Nadson"
        },
        "years": "1926–2015",
        "role": {
            "by": "Апостальскі візітатар, шматгадовы кіраўнік Бібліятэкі Скарыны ў Лондане, навуковец",
            "ru": "Апостольский визитатор, руководитель Библиотеки Скорины в Лондоне, учёный",
            "en": "Apostolic Visitor, director of the Skaryna Library in London, scholar"
        },
        "bio": {
            "by": "Ураджэнец мястэчка Гарадзея (Нясвіжскі раён). Духоўны лідар беларускага замежжа, апостальскі візітатар для беларусаў-каталікоў замежжа. Больш за 30 гадоў узначальваў Беларускую бібліятэку і музей імя Францыска Скарыны ў Лондане. Аўтар навуковых прац па скарыназнаўстве і гісторыі Уніі, перакладчык літургічных тэкстаў на беларускую мову. Пахаваны ў Лондане на могілках Сэнт-Панкрас.",
            "ru": "Уроженец Городеи (Несвижский район). Апостольский визитатор белорусов зарубежья, многолетний глава Белорусской библиотеки им. Скорины в Лондоне. Исследователь наследия Скорины. Похоронен в Лондоне.",
            "en": "Born in Haradzeya (Nyasvizh district). Spiritual leader of the Belarusian diaspora, Apostolic Visitor for Belarusian Catholics abroad. Directed the Skaryna Library in London for decades. Scholar of Skaryna studies. Buried at St Pancras Cemetery in London."
        },
        "photo": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Biskup_Sipovich_u_biblijatecy.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%90%D0%BB%D1%8F%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%9D%D0%B0%D0%B4%D1%81%D0%B0%D0%BD"
    },
    {
        "id": "uladzislaw-plyater",
        "name": {
            "by": "Граф Уладзіслаў Плятэр",
            "ru": "Граф Владислав Платер",
            "en": "Count Władysław Plater"
        },
        "years": "1808–1889",
        "role": {
            "by": "Магнат з роду Плятэраў, удзельнік паўстання 1831 г., заснавальнік музея ў Раперсвілі",
            "ru": "Магнат из рода Плятеров, участник восстания 1831 г., основатель музея в Рапперсвиле",
            "en": "Magnate of the Plater family, 1831 insurgent, founder of Rapperswil Museum"
        },
        "bio": {
            "by": "Прадстаўнік знакамітага магнацкага роду Плятэраў (Браслаўшчына, Віленшчына, Інфлянты), стрыечны брат гераіні паўстання Эміліі Плятэр. Удзельнік вызваленчага паўстання 1830–1831 гг. У эміграцыі ў Швейцарыі ў 1870 г. выкупіў і аднавіў сярэднявечны замак Раперсвіль на Цюрыхскім возеры, дзе заснаваў Польска-Літоўскі нацыянальны музей і маўзалей Тадэвуша Касцюшкі. Пахаваны ў Раперсвілі.",
            "ru": "Представитель магнатского рода Плятеров, двоюродный брат Эмилии Плятер. Участник восстания 1831 г. Выкупил и восстановил замок Рапперсвиль в Швейцарии, основав там Польско-Литовский национальный музей и мавзолей сердца Костюшко.",
            "en": "Magnate of the Plater family, cousin of heroine Emilia Plater. Insurgent of 1831. Restored Rapperswil Castle in Switzerland, creating the Polish-Lithuanian National Museum and the mausoleum for Tadeusz Kościuszko's heart."
        },
        "photo": "https://upload.wikimedia.org/wikipedia/commons/f/f6/Rapperswil_Schloss_Nacht.jpeg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%A3%D0%BB%D0%B0%D0%B4%D0%B7%D1%96%D1%81%D0%BB%D0%B0%D1%9E_%D0%9F%D0%BB%D1%8F%D1%82%D1%8D%D1%80"
    },
    {
        "id": "leonilla-sayn-wittgenstein",
        "name": {
            "by": "Княгіня Леаніла Барацінская (Вітгенштэйн)",
            "ru": "Княгиня Леонилла Барятинская (Витгенштейн)",
            "en": "Princess Leonilla of Sayn-Wittgenstein-Sayn"
        },
        "years": "1816–1918",
        "role": {
            "by": "Княгіня, уладальніца Мірскага замка і радзівілаўскіх латыфундый, мецэнатка",
            "ru": "Княгиня, владелица Мирского замка и латифундий Радзивиллов",
            "en": "Princess, mistress of Mir Castle and Radziwiłł estates, patron of arts"
        },
        "bio": {
            "by": "Адна з найпрыгажэйшых жанчын Еўропы XIX стагоддзя (вядомы партрэт Франца Ксавера Вінтэрхальтэра ў музеі Геці). Жонка князя Льва Вітгенштэйна. Пасля смерці Стэфаніі Радзівіл успадкавала каласальныя радзівілаўскія маёнткі, у тым ліку Мірскі замак. Пражыла 102 гады. Пахавана ў неагатычнай капліцы замка Зайн у Германіі.",
            "ru": "Супруга князя Льва Витгенштейна, владелица Мирского замка и владений Радзивиллов в Беларуси. Прожила 102 года. Похоронена в дворцовой капелле Зайн в Германии.",
            "en": "Wife of Prince Ludwig zu Sayn-Wittgenstein. Inherited vast Radziwiłł estates including Mir Castle. Renowned beauty portrayed by Winterhalter. Lived to 102. Buried in Sayn Palace Chapel, Germany."
        },
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Schloss_Sayn_2011.jpg/1280px-Schloss_Sayn_2011.jpg",
        "wiki": "https://en.wikipedia.org/wiki/Leonilla_Bariatinskaya"
    }
]

for p in new_persons:
    persons_map[p['id']] = p

# -------------------------------------------------------------
# 3. NEW PLACES (Western European Cemeteries & Heritage)
# -------------------------------------------------------------

new_places = [
    {
        "id": "montmorency-champeaux-cemetery-pantheon",
        "title": {
            "by": "Могілкі Шампо ў Манмарансі — Пантэон беларуска-польскай эміграцыі",
            "ru": "Кладбище Шампо в Монморанси — Пантеон эмиграции",
            "en": "Champeaux Cemetery in Montmorency — Emigration Pantheon"
        },
        "category": "grave",
        "country": {"by": "Францыя", "ru": "Франция", "en": "France"},
        "city": {"by": "Манмарансі", "ru": "Монморанси", "en": "Montmorency"},
        "coordinates": [48.9897, 2.3256],
        "description": {
            "by": "Адрас: Rue des Champeaux, 95160 Montmorency (15 км ад Парыжа).\n\nГалоўны гістарычны пантэон дзеячаў Вялікага Княства Літоўскага і Рэчы Паспалітай XIX ст. Тут спачываюць выбітныя ўраджэнцы Беларусі:\n• Юльян Урсын Нямцэвіч (1758–1841, з маёнтка Скокі пад Брэстам) — паплечнік Касцюшкі і аўтар Канстытуцыі 3 мая;\n• Аляксандр Ходзька (1804–1891, з Крывічоў) — філамат, усходазнавец, прафесар Калеж дэ Франс;\n• Леанард Ходзька (1800–1871, з Аборка) — гісторык, публіцыст і картограф ВКЛ;\n• Генерал Караль Князевіч (1762–1842);\n• Радавы склеп сям'і Адама Міцкевіча (сам паэт спачываў тут у 1855–1890 гг. да пераносу на Вавель; тут пахаваны яго сын Уладзіслаў Міцкевіч і дачка Марыя Гурэцкая);\n• Вацлаў Пелікан (1790–1873) — рэктар Віленскага ўніверсітэта.",
            "ru": "Адрес: Rue des Champeaux, Montmorency (Франция).\n\nГлавный исторический пантеон эмиграции. Здесь похоронены Юлиан Урсын Немцевич (уроженец Скоков под Брестом), востоковед Александр Ходзько (из Кривичей), историк Леонард Ходзько, семья Адама Мицкевича (сам поэт покоился здесь до 1890 г.).",
            "en": "Address: Rue des Champeaux, Montmorency, France.\n\nThe foremost historic necropolis of the 19th-century Great Emigration. Holds the tombs of Julian Ursyn Niemcewicz (born in Skoki near Brest), orientalist Aleksander Chodźko, historian Leonard Chodźko, and the Mickiewicz family crypt (where Adam Mickiewicz was buried until 1890)."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Cimeti%C3%A8re_Champeaux_-_Montmorency_%28FR95%29_-_2024-10-13_-_1.jpg",
        "links": [
            {
                "title": "Cimetière des Champeaux de Montmorency",
                "url": "https://fr.wikipedia.org/wiki/Cimeti%C3%A8re_des_Champeaux_de_Montmorency"
            }
        ],
        "tags": ["Францыя", "Манмарансі", "Пантэон", "Нямцэвіч", "Ходзька", "Міцкевіч", "grave"],
        "personId": "yulian-ursyn-nyamtsevich",
        "personIds": ["yulian-ursyn-nyamtsevich", "aleksandr-chodzko", "leonard-chodzko", "adam-mickiewicz"],
        "mustSee": True
    },
    {
        "id": "paris-montmartre-valentsin-vankovich-grave",
        "title": {
            "by": "Магіла мастака Валянціна Ваньковіча на могілках Манмартр",
            "ru": "Могила художника Валентия Ваньковича на кладбище Монмартр",
            "en": "Grave of Painter Walenty Wańkowicz at Montmartre Cemetery"
        },
        "category": "grave",
        "country": {"by": "Францыя", "ru": "Франция", "en": "France"},
        "city": {"by": "Парыж", "ru": "Париж", "en": "Paris"},
        "coordinates": [48.8876, 2.3303],
        "description": {
            "by": "Адрас: Cimetière de Montmartre, 20 Avenue Rachel, 75018 Paris.\n\nТут спачывае класік рамантычнага жывапісу Валянцін Ваньковіч (1800–1842), ураджэнец маёнтка Калюжыца Ігуменскага павета (Чэрвеньскі раён). Аўтар знакамітага кананічнага партрэта Адама Міцкевіча на скале Аю-Даг, партрэтаў Марыі Шыманоўскай, Аляксандра Пушкіна, карціны «Апафеоз Напалеона». Блізкі сябар Міцкевіча, які памёр у Парыжы ў яго кватэры на руках у паэта.",
            "ru": "Адрес: Cimetière de Montmartre, 20 Avenue Rachel, Paris.\n\nЗдесь похоронен выдающийся художник-романтик Валентий Ванькович (1800–1842), уроженец Калюжицы (Червенский район). Автор хрестоматийного портрета Адама Мицкевича на скале Аю-Даг. Умер в Париже на руках у Мицкевича.",
            "en": "Address: Montmartre Cemetery, 20 Avenue Rachel, Paris.\n\nTomb of classic Romantic portrait painter Walenty Wańkowicz (1800–1842), born in Kałużyca near Cherven (Minsk region). Creator of the iconic portrait of Adam Mickiewicz on the Ay-Dagh Cliff. Died in Paris in Mickiewicz's home."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/9/90/Walenty_wankowicz.jpg",
        "links": [
            {
                "title": "Вікіпедыя: Валянцін Ваньковіч",
                "url": "https://be.wikipedia.org/wiki/%D0%92%D0%B0%D0%BB%D1%8F%D0%BD%D1%86%D1%96%D0%BD_%D0%92%D0%B0%D0%BD%D1%8C%D0%BA%D0%BE%D0%B2%D1%96%D1%87"
            }
        ],
        "tags": ["Францыя", "Парыж", "Манмартр", "Ваньковіч", "жывапіс", "grave"],
        "personId": "valentsin-vankovich",
        "personIds": ["valentsin-vankovich", "adam-mickiewicz"],
        "mustSee": True
    },
    {
        "id": "paris-montparnasse-ossip-zadkine-grave",
        "title": {
            "by": "Магіла скульптара Восіпа Цадкіна на могілках Манпарнас",
            "ru": "Могила скульптора Осипа Цадкина на кладбище Монпарнас",
            "en": "Grave of Sculptor Ossip Zadkine at Montparnasse Cemetery"
        },
        "category": "grave",
        "country": {"by": "Францыя", "ru": "Франция", "en": "France"},
        "city": {"by": "Парыж", "ru": "Париж", "en": "Paris"},
        "coordinates": [48.8412, 2.3275],
        "description": {
            "by": "Адрас: Cimetière du Montparnasse, Division 8, 3 Boulevard Edgar Quinet, 75014 Paris.\n\nТут спачывае адзін з найвыдатнейшых скульптараў сусветнага авангарду XX стагоддзя Восіп Цадкін (1890–1967), ураджэнец Віцебска. Цадкін вучыўся ў Віцебску разам з Маркам Шагалам у школе Юдэля Пэна. У Парыжы стаў піянерам кубізму ў скульптуры (аўтар славутага манумента «Разбураны горад» у Ратэрдаме). Пахаваны разам з жонкай, мастачкай Валянцінай Пракс; на магіле ўсталявана яго ўласная бронзавая скульптура.",
            "ru": "Адрес: Cimetière du Montparnasse, Division 8, Paris.\n\nЗдесь похоронен один из величайших скульпторов XX века Осип Цадкин (1890–1967), уроженец Витебска, ученик Юделя Пэна. Пионер кубизма в скульптуре.",
            "en": "Address: Montparnasse Cemetery, Division 8, Paris.\n\nTomb of world-renowned avant-garde sculptor Ossip Zadkine (1890–1967), born in Vitebsk and student of Yehuda Pen. A pioneer of Cubist sculpture."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/52/Tombe_Ossip_Zadkine.jpg",
        "links": [
            {
                "title": "Вікіпедыя: Восіп Цадкін",
                "url": "https://be.wikipedia.org/wiki/%D0%92%D0%BE%D1%81%D1%96%D0%BF_%D0%A6%D0%B0%D0%B4%D0%BA%D1%96%D0%BD"
            }
        ],
        "tags": ["Францыя", "Парыж", "Манпарнас", "Цадкін", "скульптура", "Віцебск", "grave"],
        "personId": "ossip-zadkine",
        "personIds": ["ossip-zadkine"],
        "mustSee": False
    },
    {
        "id": "london-st-pancras-belarusian-pantheon",
        "title": {
            "by": "Беларускі пантэон на могілках Сэнт-Панкрас у Лондане",
            "ru": "Белорусский пантеон на кладбище Сент-Панкрас в Лондоне",
            "en": "Belarusian Pantheon at St Pancras Cemetery in London"
        },
        "category": "grave",
        "country": {"by": "Вялікабрытанія", "ru": "Великобритания", "en": "United Kingdom"},
        "city": {"by": "Лондан", "ru": "Лондон", "en": "London"},
        "coordinates": [51.5976, -0.1698],
        "description": {
            "by": "Адрас: St Pancras and Islington Cemetery, 278 High Rd, East Finchley, London N2 9AG.\n\nГалоўны нацыянальны некропаль беларускай паваеннай эміграцыі ў Вялікабрытаніі. Тут у беларускай секцыі спачываюць выбітныя духоўныя і грамадскія дзеячы:\n• Біскуп Часлаў Сіповіч (1914–1981) — апостальскі візітатар, заснавальнік Бібліятэкі і музея імя Скарыны ў Лондане;\n• Айцец Аляксандр Надсан (1926–2015) — апостальскі візітатар, шматгадовы кіраўнік Бібліятэкі Скарыны;\n• Айцец Леў Гарошка (1897–1977) — святар, рэдактар часопіса «Божым шляхам»;\n• Гай дэ Пікарда (1931–2007) — брытанскі даследчык беларускай музыкі і культуры;\n• Павел Навара, Ян Садоўскі, Вінцук Жук-Грышкевіч і дзесяткі іншых дзеячаў Згуртавання беларусаў у Вялікабрытаніі.",
            "ru": "Адрес: St Pancras and Islington Cemetery, East Finchley, London.\n\nГлавный некрополь белорусской диаспоры в Великобритании. Здесь похоронены епископ Чеслав Сипович, отец Александр Надсон, священник Лев Горошко, исследователь Гай де Пикарда и деятели белорусского движения.",
            "en": "Address: St Pancras and Islington Cemetery, 278 High Rd, East Finchley, London.\n\nThe principal national necropolis of the Belarusian diaspora in the UK. Houses the graves of Bishop Ceslaus Sipovich, Fr. Alexander Nadson, Fr. Leo Haroshka, Guy Picarda, and prominent members of the Association of Belarusians in Great Britain."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Biskup_Sipovich_u_biblijatecy.jpg",
        "links": [
            {
                "title": "Згуртаванне беларусаў у Вялікабрытаніі",
                "url": "https://zbvb.org.uk/"
            }
        ],
        "tags": ["Вялікабрытанія", "Лондан", "Пантэон", "Сіповіч", "Надсан", "Скарынаўка", "grave"],
        "personId": "chaslau-sipovich",
        "personIds": ["chaslau-sipovich", "alyaksandr-nadsan"],
        "mustSee": True
    },
    {
        "id": "rapperswil-castle-plater-museum",
        "title": {
            "by": "Замак Раперсвіль і музей графа Уладзіслава Плятэра",
            "ru": "Замок Рапперсвиль и музей графа Владислава Плятера",
            "en": "Rapperswil Castle & Museum of Count Władysław Plater"
        },
        "category": "culture",
        "country": {"by": "Швейцарыя", "ru": "Швейцария", "en": "Switzerland"},
        "city": {"by": "Раперсвіль", "ru": "Рапперсвиль", "en": "Rapperswil"},
        "coordinates": [47.2269, 8.8156],
        "description": {
            "by": "Адрас: Lindenhof, 8640 Rapperswil-Jona, Switzerland.\n\nЗамак на Цюрыхскім возеры, выкуплены і адноўлены ў 1870 г. графам Уладзіславам Плятэрам (з магнацкага роду Плятэраў, стрыечным братам Эміліі Плятэр). Плятэр стварыў тут Польска-Літоўскі нацыянальны музей і маўзалей, дзе дзесяцігоддзямі захоўвалася урна з сэрцам Тадэвуша Касцюшкі (перавезена ў Варшаву ў 1927 г.). Сам граф Уладзіслаў Плятэр пахаваны тут жа ў замкавай капліцы.",
            "ru": "Адрес: Lindenhof, Rapperswil-Jona, Швейцария.\n\nЗамок на Цюрихском озере, восстановленный графом Владиславом Плятером в 1870 г. Здесь был основан Польско-Литовский национальный музей, где хранилось сердце Тадеуша Костюшко. Сам граф Плятер похоронен в замке.",
            "en": "Address: Rapperswil Castle, Switzerland.\n\nMedieval castle restored in 1870 by Count Władysław Plater (of the Plater magnate family). Plater established the Polish-Lithuanian Museum and the mausoleum where the heart of Tadeusz Kościuszko was enshrined for decades. Count Plater is buried at the castle."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/f/f6/Rapperswil_Schloss_Nacht.jpeg",
        "links": [
            {
                "title": "Schloss Rapperswil",
                "url": "https://en.wikipedia.org/wiki/Rapperswil_Castle"
            }
        ],
        "tags": ["Швейцарыя", "Раперсвіль", "Плятэры", "Касцюшка", "замак", "музей", "culture"],
        "personId": "uladzislaw-plyater",
        "personIds": ["uladzislaw-plyater", "tadevush-kastsyushka"],
        "mustSee": True
    },
    {
        "id": "sayn-palace-crypt-leonilla-wittgenstein",
        "title": {
            "by": "Капліца палаца Зайн — Пахаванне княгіні Леанілы Барацінскай (уладальніцы Міра)",
            "ru": "Капелла дворца Зайн — Усыпальница княгини Леониллы Барятинской (владелицы Мира)",
            "en": "Sayn Palace Chapel — Tomb of Princess Leonilla of Sayn-Wittgenstein"
        },
        "category": "grave",
        "country": {"by": "Германія", "ru": "Германия", "en": "Germany"},
        "city": {"by": "Бендорф-Зайн", "ru": "Бендорф-Зайн", "en": "Bendorf-Sayn"},
        "coordinates": [50.4389, 7.5778],
        "description": {
            "by": "Адрас: Schloßstraße 100, 56170 Bendorf-Sayn, Rheinland-Pfalz, Germany.\n\nУ неагатычнай палацавай капліцы роду Зайн-Вітгенштэйн знаходзіцца мармуровы саркафаг княгіні Леанілы Барацінскай-Вітгенштэйн (1816–1918), якая пражыла 102 гады. Леаніла была жонкай князя Льва Вітгенштэйна і праз шлюб валодала велізарнымі зямлямі Радзівілаў на Беларусі, уключаючы Мірскі замак, які яна ў канцы XIX ст. прадала князю Мікалаю Святаполк-Мірскаму.",
            "ru": "Адрес: Schloßstraße 100, Bendorf-Sayn, Германия.\n\nВ неоготической капелле дворца Зайн находится саркофаг княгини Леониллы Барятинской (Витгенштейн, 1816–1918), владелицы Мирского замка и владений Радзивиллов в Беларуси.",
            "en": "Address: Schloßstraße 100, Bendorf-Sayn, Germany.\n\nThe Neo-Gothic chapel of Sayn Palace contains the marble tomb of Princess Leonilla of Sayn-Wittgenstein-Sayn (1816–1918), mistress of Mir Castle and vast Radziwiłł estates in Belarus."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Schloss_Sayn_2011.jpg/1280px-Schloss_Sayn_2011.jpg",
        "links": [
            {
                "title": "Schloss Sayn",
                "url": "https://en.wikipedia.org/wiki/Sayn_Castle"
            }
        ],
        "tags": ["Германія", "Зайн", "Мірскі замак", "Радзівілы", "Вітгенштэйны", "grave"],
        "personId": "leonilla-sayn-wittgenstein",
        "personIds": ["leonilla-sayn-wittgenstein"],
        "mustSee": False
    },
    {
        "id": "warsaw-powazki-stanislaw-moniuszko-grave",
        "title": {
            "by": "Магіла кампазітара Станіслава Манюшкі на Паванзках у Варшаве",
            "ru": "Могила композитора Станислава Монюшко на Повонзках в Варшаве",
            "en": "Grave of Composer Stanisław Moniuszko at Powązki Cemetery in Warsaw"
        },
        "category": "grave",
        "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
        "city": {"by": "Варшава", "ru": "Варшава", "en": "Warsaw"},
        "coordinates": [52.2536, 20.9786],
        "description": {
            "by": "Адрас: Cmentarz Powązkowski, Powązkowska 14, Warszawa (Aleja Katakumbowa, каля філаматаў).\n\nТут спачывае Станіслаў Манюшка (1819–1872) — вялікі кампазітар, ураджэнец фальварка Убель Ігуменскага павета (Чэрвеньскі раён). Стваральнік першай нацыянальнай беларускамоўнай оперы «Сялянка» («Ідылія») разам з Вінцэнтам Дуніным-Марцінкевічам, а таксама знакамітых опер «Галька», «Страшны двор» і зборнікаў песень «Хатні спеўнік».",
            "ru": "Адрес: Cmentarz Powązkowski, Варшава.\n\nЗдесь похоронен Станислав Монюшко (1819–1872) — великий композитор, уроженец фольварка Убель (Червенский район). Создатель белорусской оперы «Селянка» (вместе с Дуниным-Марцинкевичем) и польской классической оперы.",
            "en": "Address: Powązki Cemetery, Warsaw.\n\nTomb of composer Stanisław Moniuszko (1819–1872), born in Ubiel near Minsk. Creator of the first Belarusian-language opera 'Sielanka' with Vincent Dunin-Marcinkievič, and classic operas 'Halka' and 'The Haunted Manor'."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Gr%C3%B3b_Stanis%C5%82awa_Moniuszki.jpg/800px-Gr%C3%B3b_Stanis%C5%82awa_Moniuszki.jpg",
        "links": [
            {
                "title": "Вікіпедыя: Станіслаў Манюшка",
                "url": "https://be.wikipedia.org/wiki/%D0%A1%D1%82%D0%B0%D0%BD%D1%96%D1%81%D0%BB%D0%B0%D1%9E_%D0%9C%D0%B0%D0%BD%D1%8E%D1%88%D0%BA%D0%B0"
            }
        ],
        "tags": ["Польшча", "Варшава", "Паванзкі", "Манюшка", "опера", "Убель", "grave"],
        "personId": "stanislaw-monyushka",
        "personIds": ["stanislaw-monyushka"],
        "mustSee": True
    },
    {
        "id": "warsaw-wilanow-radziwill-crypt",
        "title": {
            "by": "Капліца і крыпта князёў Радзівілаў у Вілянаве",
            "ru": "Часовня и крипта князей Радзивиллов в Вилянуве",
            "en": "Radziwiłł Crypt and Chapel in Wilanów, Warsaw"
        },
        "category": "grave",
        "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
        "city": {"by": "Варшава", "ru": "Варшава", "en": "Warsaw"},
        "coordinates": [52.1656, 21.0903],
        "description": {
            "by": "Адрас: Stanisława Kostki Potockiego 1, Warszawa (касцёл Святой Ганны каля Вілянаўскага палаца).\n\nСямейная магільная капліца і крыпта князёў Радзівілаў (Krypta Radziwiłłów). Тут спачываюць выбітныя прадстаўнікі роду Радзівілаў канца XIX — XX стагоддзяў, у тым ліку князь Януш Францішак Радзівіл (1880–1967, ардынат на Алыцы, палітычны і дзяржаўны дзеяч) і яго сваякі.",
            "ru": "Адрес: Stanisława Kostki Potockiego 1, Warszawa.\n\nФамильная усыпальница князей Радзивиллов в костёле Святой Анны в Вилянуве. Здесь похоронен князь Януш Радзивилл (1880–1967) и члены его семьи.",
            "en": "Address: St. Anne's Church, Wilanów, Warsaw.\n\nThe family crypt and burial chapel of the Radziwiłł princes at Wilanów. Holds the tombs of Prince Janusz Franciszek Radziwiłł (1880–1967) and his relatives."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Kosciol_sw_Anny_w_Wilanowie.jpg/800px-Kosciol_sw_Anny_w_Wilanowie.jpg",
        "links": [
            {
                "title": "Вікіпедыя: Радзівілы",
                "url": "https://be.wikipedia.org/wiki/%D0%A0%D0%B0%D0%B4%D0%B7%D1%96%D0%B2%D1%96%D0%BB%D1%8B"
            }
        ],
        "tags": ["Польшча", "Варшава", "Вілянаў", "Радзівілы", "магнаты", "grave"],
        "personId": "radziwills",
        "personIds": ["radziwills"],
        "mustSee": False
    }
]

for p in new_places:
    places_map[p['id']] = p

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

print(f"Total places after cemetery addition: {len(final_places)}")
print(f"Total persons after cemetery addition: {len(final_persons)}")
