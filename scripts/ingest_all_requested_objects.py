# -*- coding: utf-8 -*-
"""
Ingestion script for all requested locations:
- GULAG camps (Solovki, Sandarmokh, Inta, Vorkuta, Kolyma, Karlag/ALZHIR, Kengir, Norilsk)
- Nazi concentration camps (Auschwitz, Sobibor, Mauthausen, Buchenwald, Ravensbruck, Sachsenhausen, Dachau, Stutthof)
- Kyiv & Lviv (Pechersk Lavra, University, Karatkevich monument, Bessarabsky market, Beloruska memorial, Zhyzneuski, Mohyla Academy, Dom Volnay Belarusi, vul. Biloruska)
- Berlin & Potsdam (BNR Mission, Press Bureau, Der Sturm Chagall, Tacheles / Rodzin, Das Minsk)
- Moscow Kremlin (Lazkovichy Cross)
- Sweden (BCWT Visby with Bykau & Arlou, Stockholm Sveriges Belarusier, Uppsala Carolina Rediviva)
- Slovakia (Ján Nálepka monument in Spišská Nová Ves)
- Czapski heritage (Muzeum Emeryka Hutten-Czapskiego, Pawilon Józefa Czapskiego, Maisons-Laffitte Kultura)
"""
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

with open('data/places.json', 'r', encoding='utf-8') as f:
    places = json.load(f)
with open('data/persons.json', 'r', encoding='utf-8') as f:
    persons = json.load(f)

def upsert_person(p_dict):
    global persons
    existing = next((p for p in persons if p['id'] == p_dict['id']), None)
    if existing:
        all_pids = list(dict.fromkeys(existing.get('placeIds', []) + p_dict.get('placeIds', [])))
        existing.update(p_dict)
        existing['placeIds'] = all_pids
    else:
        persons.append(p_dict)

def upsert_place(p_dict):
    global places
    existing = next((p for p in places if p['id'] == p_dict['id']), None)
    if existing:
        existing.update(p_dict)
    else:
        places.append(p_dict)

# ==========================================
# 1. NEW PERSONS
# ==========================================

upsert_person({
    "id": "francisak-alyakhnovich",
    "name": {
        "by": "Францішак Аляхновіч",
        "ru": "Франтишек Олехнович",
        "en": "Frantsishak Alyakhnovich"
    },
    "dates": "1883 — 1944",
    "role": {
        "by": "Беларускі драматург, тэатральны дзеяч, вязень Салаўкоў, аўтар «У капцюрох ГПУ»",
        "ru": "Белорусский драматург, театральный деятель, узник Соловков, автор «В когтях ГПУ»",
        "en": "Belarusian playwright, theater director, Solovki GULAG survivor, author of 'In the Claws of the GPU'"
    },
    "bio": {
        "by": "Патрыярх беларускай драматургіі, рэжысёр і публіцыст. У 1926 г. пераехаў з Вільні ў БССР, дзе быў арыштаваны ДПУ і асуджаны да 10 гадоў Салавецкага лагера (СЛАОН). У 1933 г. абменены на Браніслава Тарашкевіча. Напісаў сусветна вядомую кнігу ўспамінаў «У капцюрох ГПУ» — першы ў сусветнай літаратуры дакументальны твор пра савецкія канцлагеры.",
        "ru": "Основоположник белорусской драматургии. В 1926 году приехал из Вильнюса в БССР, был арестован и отправлен на Соловки (СЛОН). В 1933 году обменян на Бронислава Тарашкевича. Автор знаменитых мемуаров «В когтях ГПУ» — первого в мировой литературе документального свидетельства о лагерях ГУЛАГа.",
        "en": "Pioneering Belarusian dramatist and director. Arrested by the Soviet OGPU in 1926 and sentenced to 10 years in the Solovki labor camp (SLON). Exchanged for Branislaw Tarashkyevich in 1933. Wrote 'In the Claws of the GPU' (1935), the very first published personal documentary account of the Soviet GULAG system."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Franci%C5%A1ak_Alachnovi%C4%8D._%D0%A4%D1%80%D0%B0%D0%BD%D1%86%D1%96%D1%88%D0%B0%D0%BA_%D0%90%D0%BB%D1%8F%D1%85%D0%BD%D0%BE%D0%B2%D1%96%D1%87_%281920-39%29.jpg/330px-Franci%C5%A1ak_Alachnovi%C4%8D._%D0%A4%D1%80%D0%B0%D0%BD%D1%86%D1%96%D1%88%D0%B0%D0%BA_%D0%90%D0%BB%D1%8F%D1%85%D0%BD%D0%BE%D0%B2%D1%96%D1%87_%281920-39%29.jpg",
    "wiki": "https://be.wikipedia.org/wiki/Францішак_Каралевіч_Аляхновіч",
    "placeIds": ["gulag-solovki-slon"]
})

upsert_person({
    "id": "siarhiej-hrahouski",
    "name": {
        "by": "Сяргей Грахоўскі",
        "ru": "Сергей Граховский",
        "en": "Siarhiej Hrahouski"
    },
    "dates": "1913 — 2002",
    "role": {
        "by": "Беларускі паэт, празаік, вязень ГУЛАГа (Калыма, Сібір), аўтар лагернай трылогіі",
        "ru": "Белорусский поэт, прозаик, узник ГУЛАГа (Колыма, Сибирь), автор лагерной трилогии",
        "en": "Belarusian poet, writer, survivor of Kolyma and Siberian GULAG camps, author of the Gulag memoir trilogy"
    },
    "bio": {
        "by": "Выбітны беларускі пісьменнік і перакладчык. Двойчы рэпрэсаваны савецкім рэжымам (арышты ў 1936 і 1949 гг.), правёў у лагерах і высылцы на Калыме і ў Сібіры амаль два дзесяцігоддзі. Аўтар аўтабіяграфічнай лагернай трылогіі «Такія сінія снягі», «Зона маўчання», «З воўчым білетам» — фундаментальнага летапісу трагедыі беларускай інтэлігенцыі ў ГУЛАГу.",
        "ru": "Белорусский писатель и поэт. Дважды репрессирован советской властью (аресты 1936 и 1949 гг.), провел в лагерях и ссылках на Колыме и в Сибири почти двадцать лет. Автор документальной трилогии «Такі сінія снягі», «Зона маўчання», «З воўчым білетам».",
        "en": "Renowned Belarusian poet and prose writer. Twice arrested by Soviet authorities (1936 and 1949), spending nearly two decades in the brutal gold mines of Kolyma and in Siberian exile. Chronicled the genocide of the Belarusian intelligentsia in his monumental GULAG autobiographical trilogy."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Siarhiej_Hrachouski_1930s.jpg/330px-Siarhiej_Hrachouski_1930s.jpg",
    "wiki": "https://be.wikipedia.org/wiki/Сяргей_Іванавіч_Грахоўскі",
    "placeIds": ["gulag-kolyma-maska-smutku"]
})

upsert_person({
    "id": "uladzimir-karatkevich",
    "name": {
        "by": "Уладзімір Караткевіч",
        "ru": "Владимир Короткевич",
        "en": "Uladzimir Karatkevich"
    },
    "dates": "1930 — 1984",
    "role": {
        "by": "Класік беларускай літаратуры, стваральнік беларускага гістарычнага рамана",
        "ru": "Классик белорусской литературы, основоположник белорусского исторического романа",
        "en": "Classic of Belarusian literature, creator of the Belarusian historical novel"
    },
    "bio": {
        "by": "Ураджэнец Оршы. Стваральнік сучаснага беларускага гістарычнага рамана і дэтэктыва, аўтар шэдэўраў «Дзікае паляванне караля Стаха», «Каласы пад сярпом тваім», «Хрыстос прызямліўся ў Гародні», «Чорны замак Альшанскі». Скончыў філалагічны факультэт і аспірантуру Кіеўскага дзяржаўнага ўніверсітэта (1954). У Кіеве напісаў першы варыянт «Дзікага палявання» і задумаў эпапею пра паўстанне 1863 года.",
        "ru": "Уроженец Орши. Создатель жанра белорусского исторического романа, автор бессмертных произведений «Дикая охота короля Стаха», «Колосья под серпом твоим», «Черный замок Ольшанский». Окончил филологический факультет Киевского университета (1954), где зародились замыслы его главных исторических шедевров.",
        "en": "Born in Orsha. Celebrated titan of Belarusian literature and founder of the national historical novel genre. Author of 'King Stakh's Wild Hunt', 'Ears of Rye Under Thy Sickle', and 'The Black Castle of Alshanka'. Graduated from the University of Kyiv (1954), where he drafted his earliest masterworks."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/U%C5%82adzimir_Karatkievi%C4%8D.jpg/330px-U%C5%82adzimir_Karatkievi%C4%8D.jpg",
    "wiki": "https://be.wikipedia.org/wiki/Уладзімір_Сямёнавіч_Караткевіч",
    "placeIds": ["kyiv-university-philology-karatkevich", "kyiv-karatkevich-monument"]
})

upsert_person({
    "id": "mitrafan-dounar-zapolski",
    "name": {
        "by": "Мітрафан Доўнар-Запольскі",
        "ru": "Митрофан Довнар-Запольский",
        "en": "Mitrafan Dounar-Zapolski"
    },
    "dates": "1861 — 1934",
    "role": {
        "by": "Выбітны беларускі гісторык, этнограф, прафесар Кіеўскага ўніверсітэта, дыпламат БНР",
        "ru": "Выдающийся белорусский историк, этнограф, профессор Киевского университета, дипломат БНР",
        "en": "Prominent Belarusian historian, ethnographer, professor at Kyiv University, BNR diplomat"
    },
    "bio": {
        "by": "Ураджэнец Рэчыцы. Адзін з пачынальнікаў беларускай нацыянальнай гістарыяграфіі і эканомікі. Шматгадовы прафесар Кіеўскага ўніверсітэта Святога Уладзіміра, арганізатар Кіеўскага камерцыйнага інстытута. У 1918 г. узначальваў дыпламатычную місію БНР у Кіеве, аўтар працы «Асновы дзяржаўнасці Беларусі» (1919) і манументальнай «Гісторыі Беларусі».",
        "ru": "Уроженец Речицы. Один из отцов белорусской исторической науки. Профессор Киевского университета Св. Владимира, создатель Киевского коммерческого института. Возглавлял дипломатическую миссию БНР в Киеве, обосновал историческое и этнографическое право Беларуси на независимость.",
        "en": "Born in Rechytsa. Founding father of Belarusian national historiography. Longtime professor at St. Vladimir University in Kyiv. Led the BNR diplomatic mission in Kyiv in 1918, authoring 'Historical Foundations of Belarusian Statehood' (1919)."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/M_Dounar-Zapolski.jpg/330px-M_Dounar-Zapolski.jpg",
    "wiki": "https://be.wikipedia.org/wiki/Мітрафан_Віктаравіч_Доўнар-Запольскі",
    "placeIds": ["kyiv-university-philology-karatkevich"]
})

upsert_person({
    "id": "mikhail-zhyzneuski",
    "name": {
        "by": "Міхаіл Жызнеўскі",
        "ru": "Михаил Жизневский",
        "en": "Mikhail Zhyzneuski"
    },
    "dates": "1988 — 2014",
    "role": {
        "by": "Беларускі грамадскі актывіст, Герой Украіны, рыцар Нябеснай Сотні",
        "ru": "Белорусский активист, Герой Украины, рыцарь Небесной Сотни",
        "en": "Belarusian activist, Hero of Ukraine, knight of the Heavenly Hundred"
    },
    "bio": {
        "by": "Ураджэнец Гомеля. Удзельнік Рэвалюцыі Годнасці ва Украіне. Загінуў 22 студзеня 2014 г. на вуліцы Грушэўскага ў Кіеве ад стрэлу ў сэрца, стаўшы адной з першых ахвяр супрацьстаяння і першым замежнікам сярод герояў Нябеснай Сотні. Першы іншаземец, якому пасмяротна прысвоена найвышэйшае званне Героя Украіны (2017).",
        "ru": "Уроженец Гомеля. Участник Евромайдана и Революции Достоинства. Погиб 22 января 2014 года в Киеве, став одной из первых жертв Небесной Сотни. Первый иностранец, посмертно удостоенный звания Героя Украины.",
        "en": "Born in Gomel. Prominent participant in Ukraine's Revolution of Dignity (Euromaidan). Shot dead on Hrushevsky Street in Kyiv on January 22, 2014, becoming one of the first martyrs of the Heavenly Hundred. Posthumously awarded the highest title of Hero of Ukraine."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Mikhail_Zhyzneuski.jpg/330px-Mikhail_Zhyzneuski.jpg",
    "wiki": "https://be.wikipedia.org/wiki/Міхаіл_Міхайлавіч_Жызнеўскі",
    "placeIds": ["kyiv-memorial-zhyzneuski", "kyiv-memorial-fallen-belarusians"]
})

upsert_person({
    "id": "ales-rodzin",
    "name": {
        "by": "Алесь Родзін",
        "ru": "Алесь Родин",
        "en": "Ales Rodzin"
    },
    "dates": "1947 — 2022",
    "role": {
        "by": "Беларускі мастак-авангардыст, легенда берлінскага арт-цэнтра «Тахелес»",
        "ru": "Белорусский художник-авангардист, легенда берлинского арт-центра «Тахелес»",
        "en": "Belarusian avant-garde painter, legend of Berlin's Kunsthaus Tacheles"
    },
    "bio": {
        "by": "Ураджэнец Баранавічаў. Стваральнік унікальных касмічна-філасофскіх манументальных палотнаў і перформансаў. З 2001 па 2014 год яго майстэрня і перманентная выстава займалі цэлы паверх у сусветна вядомым сквоце і арт-цэнтры «Тахелес» (Tacheles) у цэнтры Берліна. Арганізатар міжнароднага фестывалю эксперыментальнага мастацтва «Дах».",
        "ru": "Уроженец Барановичей. Один из ярчайших представителей белорусского авангарда. С 2001 года жил и творил в Берлине, где его мастерская в арт-центре «Тахелес» (Kunsthaus Tacheles) стала культовым местом европейской богемы. Основатель фестиваля «Дах».",
        "en": "Born in Baranavichy. Iconic figure of Belarusian contemporary and avant-garde art. From 2001 to 2014, his monumental canvases and studio occupied an entire floor of Berlin's legendary Kunsthaus Tacheles on Oranienburger Straße, becoming a focal point of European underground culture."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Ales_Rodzin_2011.jpg/330px-Ales_Rodzin_2011.jpg",
    "wiki": "https://be.wikipedia.org/wiki/Алесь_Радзін",
    "placeIds": ["berlin-tacheles-ales-rodzin"]
})

upsert_person({
    "id": "jan-nalepka",
    "name": {
        "by": "Ян Налепка («Рэпкін»)",
        "ru": "Ян Налепка («Репкин»)",
        "en": "Ján Nálepka (\"Repkin\")"
    },
    "dates": "1912 — 1943",
    "role": {
        "by": "Славацкі антыфашыст, камандзір чэхаславацкага партызанскага атрада ў Беларусі, Герой Савецкага Саюза",
        "ru": "Словацкий антифашист, командир чехословацкого партизанского отряда в Беларуси, Герой Советского Союза",
        "en": "Slovak anti-fascist officer, commander of the Czechoslovak partisan unit in Belarus, Hero of the Soviet Union"
    },
    "bio": {
        "by": "Славацкі афіцэр, начальнік штаба 101-га славацкага палка, раскватараванага ў 1942–1943 гг. у Беларусі (Ельск). Таемна перайшоў на бок савецкіх партызан, стварыў 1-ы чэхаславацкі партызанскі атрад у беларускіх лясах, які вызначыўся ў баях на Палессі. Загінуў пры вызваленні Оўруча ў лістападзе 1943 г. Адзіны славак — Герой Савецкага Саюза.",
        "ru": "Словацкий офицер, перешедший на сторону партизан в белорусском Ельске. Создал и возглавил 1-й чехословацкий партизанский отряд в белорусском Полесье. Погиб в ноябре 1943 года при освобождении Овруча. Единственный словак — Герой Советского Союза.",
        "en": "Slovak officer stationed in Yelsk (Belarus) in 1942–1943 who joined the anti-Nazi resistance. Formed and commanded the 1st Czechoslovak partisan detachment in the Belarusian forests. Died in action in November 1943. The only Slovak honored as Hero of the Soviet Union."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/J%C3%A1n_N%C3%A1lepka.jpg/330px-J%C3%A1n_N%C3%A1lepka.jpg",
    "wiki": "https://be-tarask.wikipedia.org/wiki/Ян_Налепка",
    "placeIds": ["spisska-nova-ves-jan-nalepka-monument"]
})

upsert_person({
    "id": "emeryk-hutten-czapski",
    "name": {
        "by": "Эмерык Гутэн-Чапскі",
        "ru": "Эмерик Гуттен-Чапский",
        "en": "Emeryk Hutten-Czapski"
    },
    "dates": "1828 — 1896",
    "role": {
        "by": "Дзяржаўны дзеяч, калекцыянер, нумізмат, стваральнік музея Чапскіх у Кракаве, уладальнік Станькава",
        "ru": "Государственный деятель, коллекционер, нумизмат, создатель музея Чапских в Кракове, владелец Станьково",
        "en": "Statesman, numismatist, bibliophile, founder of the Czapski Museum in Kraków, lord of Stankava"
    },
    "bio": {
        "by": "Ураджэнец Станькава (пад Койданавам). Стварыў найбуйнейшую ў свеце калекцыю манет і медалёў ВКЛ і Польшчы, а таксама бібліятэку рэдкіх рукапісаў. У 1894 г. перавёз свае багацці з Беларусі ў Кракаў, дзе пабудаваў музей («Monumentis Patriae naufragio ereptis»). Бацька легендарнага мэра Мінска Караля Чапскага.",
        "ru": "Уроженец имения Станьково под Минском. Собрал колоссальную коллекцию монет, медалей и древностей ВКЛ. В 1894 году перевёз коллекцию в Краков и основал знаменитый музей Чапских. Отец легендарного минского городского головы Кароля Чапского.",
        "en": "Born at the family estate in Stankava near Minsk. Amassed an unmatched collection of GDL coins, medals, and ancient manuscripts. In 1894 transferred the collection to Kraków and built the Czapski Palace Museum. Father of renowned Minsk Mayor Karol Hutten-Czapski."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Emeryk_Hutten-Czapski.PNG/330px-Emeryk_Hutten-Czapski.PNG",
    "wiki": "https://be.wikipedia.org/wiki/Эмерык_Гутэн-Чапскі",
    "placeIds": ["krakow-muzeum-emeryka-hutten-czapskiego"]
})

upsert_person({
    "id": "jozef-czapski",
    "name": {
        "by": "Юзаф Чапскі",
        "ru": "Юзеф Чапский",
        "en": "Józef Czapski"
    },
    "dates": "1896 — 1993",
    "role": {
        "by": "Мастак, эсэіст, вязень Старабельскага лагера, аўтар «На бесчалавечнай зямлі», дзеяч парыжскай «Культуры»",
        "ru": "Художник, писатель, узник Старобельского лагеря, автор книги «На бесчеловечной земле», соратник «Культуры»",
        "en": "Painter, writer, GULAG survivor, author of 'The Inhuman Land', co-founder of 'Kultura' in Paris"
    },
    "bio": {
        "by": "Унук Эмерыка Чапскага. Правёў дзяцінства і юнацтва ў родавым маёнтку Прылукі пад Мінскам. Выпускнік Пецярбургскага ўніверсітэта і Кракаўскай акадэміі мастацтваў. Афіцэр Войска Польскага, вязень Старабельскага лагера (цудам пазбег Катынскага расстрэлу). Шукаў зніклых польскіх афіцэраў у СССР, пра што напісаў сусветна вядомую кнігу «На бесчалавечнай зямлі». Сузаснавальнік парыжскай «Культуры» і Інстытута літаратурнага ў Мэзон-Лафіт.",
        "ru": "Внук Эмерика Чапского. Детство и юность провел в родовом имении Прилуки под Минском. Выдающийся художник и эссеист. Офицер, выживший узник Старобельского лагеря, искал пропавших офицеров в СССР, описав это в книге «На бесчеловечной земле». Сооснователь парижского журнала «Kultura» в Мезон-Лаффит.",
        "en": "Grandson of Emeryk Hutten-Czapski. Spent his youth at the family estate in Pryluki near Minsk. Survived the Starobelsk camp and documented the Katyn massacres in 'The Inhuman Land'. After WWII, co-founded the influential dissident publishing house 'Kultura' in Maisons-Laffitte near Paris."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/J%C3%B3zef_Czapski_1932.jpg/330px-J%C3%B3zef_Czapski_1932.jpg",
    "wiki": "https://be.wikipedia.org/wiki/Юзаф_Чапскі",
    "placeIds": ["krakow-pawilon-jozefa-czapskiego", "maisons-laffitte-kultura-czapski"]
})

upsert_person({
    "id": "uladzimir-arlou",
    "name": {
        "by": "Уладзімір Арлоў",
        "ru": "Владимир Орлов",
        "en": "Uladzimir Arlou"
    },
    "dates": "нар. 1953",
    "role": {
        "by": "Беларускі гісторык, празаік, паэт, аўтар культавых гістарычных кніг пра Беларусь і ВКЛ",
        "ru": "Белорусский историк, прозаик, эссеист, автор знаковых исторических книг о Беларуси и ВКЛ",
        "en": "Prominent Belarusian historian, novelist, essayist, chronicler of the Grand Duchy of Lithuania"
    },
    "bio": {
        "by": "Ураджэнец Полацка. Адзін з найпапулярнейшых сучасных беларускіх пісьменнікаў і гісторыкаў, аўтар кніг «Краіна Беларусь», «Адкуль наш род», «Таямніцы полацкай гісторыі». Рэгулярны стыпендыят і госць Балтыйскага цэнтра пісьменнікаў і перакладчыкаў у Вісбю (Швецыя).",
        "ru": "Уроженец Полоцка. Один из ведущих современных белорусских писателей и исторических публицистов. Автор бестселлеров «Краіна Беларусь», «Адкуль наш род». Постоянный участник творческих резиденций Балтийского центра писателей в Висбю (Швеция).",
        "en": "Born in Polotsk. Celebrated contemporary Belarusian novelist and historian, author of the bestselling historical panoramas 'The Land of Belarus' and 'Secrets of Polotsk History'. Regular resident author at the Baltic Centre for Writers and Translators in Visby, Sweden."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Uladzimir_Arlou_2011.jpg/330px-Uladzimir_Arlou_2011.jpg",
    "wiki": "https://be.wikipedia.org/wiki/Уладзімір_Аляксеевіч_Арлоў",
    "placeIds": ["visby-baltic-centre-writers-bcwt"]
})

upsert_person({
    "id": "hleb-usyaslavich",
    "name": {
        "by": "Глеб Усяславіч (Глеб Менскі)",
        "ru": "Глеб Всеславич (Глеб Минский)",
        "en": "Hleb Usyaslavich of Minsk"
    },
    "dates": "~1050-я — 1119",
    "role": {
        "by": "Першы летапісны князь Менскі, сын полацкага князя Усяслава Чарадзея",
        "ru": "Первый летописный князь Минский, сын полоцкого князя Всеслава Чародея",
        "en": "First recorded Prince of Minsk, son of Prince Usiaslaw Charadzei of Polotsk"
    },
    "bio": {
        "by": "Сын полацкага князя Усяслава Чарадзея. Заснавальнік Мінскай княжацкай дынастыі, пры якім Менск стаў буйным цэнтрам удзельнага княства. Далучыў Оршу, Друцк, Копысь. У 1119 г. у час вайны з кіеўскім князем Уладзімірам Манамахам быў узяты ў палон і вывезены ў Кіеў, дзе памёр у зняволенні. Пахаваны ў Кіева-Пячэрскай лаўры.",
        "ru": "Сын полоцкого князя Всеслава Чародея, первый правитель Минского княжества. Превратил Минск в мощный оплот. В 1119 году пленен Владимиром Мономахом и увезен в Киев, где скончался в темнице. Погребен в Киево-Печерской лавре.",
        "en": "Son of the legendary Polotsk Prince Usiaslaw the Sorcerer. Founder of the Principality of Minsk. Captured in 1119 by Vladimir Monomakh and brought to Kyiv, where he died in captivity. Entombed in the Kyiv-Pechersk Lavra."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Hleb_Usiaslavich.jpg/330px-Hleb_Usiaslavich.jpg",
    "wiki": "https://be.wikipedia.org/wiki/Глеб_Усяславіч",
    "placeIds": ["kyiv-pechersk-lavra-hleb-minskirad"]
})

upsert_person({
    "id": "simeon-polotsky",
    "name": {
        "by": "Сімяон Полацкі",
        "ru": "Симеон Полоцкий",
        "en": "Simeon of Polotsk"
    },
    "dates": "1629 — 1680",
    "role": {
        "by": "Беларускі асветнік, паэт, мысліляр, выпускнік Кіева-Магілянскай акадэміі",
        "ru": "Белорусский просветитель, поэт, философ, выпускник Киево-Могилянской академии",
        "en": "Belarusian enlightener, poet, theologian, alumnus of Kyiv-Mohyla Academy"
    },
    "bio": {
        "by": "Ураджэнец Полацка. Выбітны дзеяч усходнеславянскага барока, пісьменнік і мысліцель. Скончыў Кіева-Магілянскую акадэмію ў 1650-я гг., дзе вывучыў рыторыку, філасофію і еўрапейскія мовы, пасля чаго выкладаў у Полацкай брацкай школе і стаў настаўнікам царскіх дзяцей у Маскве.",
        "ru": "Уроженец Полоцка. Выдающийся деятель эпохи барокко. Окончил Киево-Могилянскую академию в Киеве, преподавал в Полоцке, затем стал придворным поэтом и наставником царских детей в Москве.",
        "en": "Born in Polotsk. Prominent Baroque polymath, poet, and dramatist. Graduated from the Kyiv-Mohyla Academy in the 1650s, taught in Polotsk, and later laid the foundations of Russian higher education in Moscow."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Simeon_Polotsky.jpg/330px-Simeon_Polotsky.jpg",
    "wiki": "https://be.wikipedia.org/wiki/Сімяон_Полацкі",
    "placeIds": ["kyiv-mohyla-academy-polotsky-konissky"]
})

# Update Vasil Bykau placeIds to include visby
bykau = next((p for p in persons if p['id'] == 'vasil-bykau'), None)
if bykau:
    if 'visby-baltic-centre-writers-bcwt' not in bykau.get('placeIds', []):
        bykau.setdefault('placeIds', []).append('visby-baltic-centre-writers-bcwt')

# Update Larysa Heniyush placeIds to include inta
geniyush = next((p for p in persons if p['id'] == 'larysa-heniyush'), None)
if geniyush:
    if 'gulag-inta-geniyush' not in geniyush.get('placeIds', []):
        geniyush.setdefault('placeIds', []).append('gulag-inta-geniyush')

print("All persons prepared!")

# ==========================================
# 2. GULAG CAMPS
# ==========================================

upsert_place({
    "id": "gulag-solovki-slon",
    "title": {
        "by": "Салавецкі лагер асаблівага прызначэння (СЛАОН) — пакуты беларускай эліты",
        "ru": "Соловецкий лагерь особого назначения (СЛОН) — Голгофа белорусской элиты",
        "en": "Solovki Special Purpose Camp (SLON) — Cradle of the GULAG"
    },
    "category": "historical",
    "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
    "city": {"by": "Салаўкі", "ru": "Соловки", "en": "Solovetsky Islands"},
    "coordinates": [65.0250, 35.7100],
    "description": {
        "by": "Галоўны першы канцлагер савецкай сістэмы ГУЛАГ, створаны на Салавецкіх астравах. Тут адбывалі зняволенне і гінулі лідары БНР (прэм'ер Вацлаў Ластоўскі), каталіцкія святары (экзарх Фабіян Абрантовіч), паэты і пісьменнікі. Тут сядзеў Францішак Аляхновіч, які пасля вызвалення напісаў першую ў свеце кнігу пра савецкія канцлагеры «У капцюрох ГПУ».",
        "ru": "Первый и самый известный концлагерь системы ГУЛАГ на Соловецких островах. Место страданий белорусской национальной элиты: премьера БНР Вацлава Ластовского, драматурга Франтишка Олехновича, священников и поэтов. Олехнович после освобождения описал лагерь в знаменитой книге «В когтях ГПУ».",
        "en": "The pioneering concentration camp of the Soviet GULAG system on the Solovetsky Islands. Scene of suffering for the Belarusian intellectual and political elite, including BNR Prime Minister Vatslau Lastouski, Catholic Exarch Fabian Abrantovich, and playwright Frantsishak Alyakhnovich, whose memoir 'In the Claws of the GPU' exposed the camps to the world."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Solovetsky_Monastery_2011.jpg/960px-Solovetsky_Monastery_2011.jpg",
    "links": [
        {"title": "Салавецкі лагер — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Салавецкі_лагер_асаблівага_прызначэння"},
        {"title": "Францішак Аляхновіч — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Францішак_Каралевіч_Аляхновіч"}
    ],
    "tags": ["ГУЛАГ", "Салаўкі", "СЛАОН", "Аляхновіч", "Ластоўскі", "рэпрэсіі", "historical"],
    "personId": "francisak-alyakhnovich",
    "personIds": ["francisak-alyakhnovich"],
    "unverifiedCoordinates": False
})

upsert_place({
    "id": "gulag-sandarmokh-memorial",
    "title": {
        "by": "Урочышча Сандармох — Беларускі крыж і месца расстрэлу салавецкіх этапаў",
        "ru": "Урочище Сандармох — Белорусский крест и расстрелы соловецких узников",
        "en": "Sandarmokh Memorial & Belarusian Cross in Karelia"
    },
    "category": "monument",
    "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
    "city": {"by": "Мядзведжагорск", "ru": "Медвежьегорск", "en": "Medvezhyegorsk"},
    "coordinates": [62.8808, 34.4072],
    "description": {
        "by": "Лясное ўрочышча ў Карэліі, дзе ў 1937–1938 гг. органамі НКУС было таемна расстраляна і пахавана больш за 9500 чалавек 58 нацыянальнасцей. Сярод іх — салавецкі этап са славутымі дзеячамі беларускага адраджэння (Уладзіслаў Галубок, Сымон Баранавых і інш.). У 2004 г. беларуская дыяспара і таварыства «Мемарыял» паставілі тут дубовы Беларускі мемарыяльны крыж «Беларусам — ахвярам таталітарызму».",
        "ru": "Лесное урочище в Карелии — место массовых тайных расстрелов НКВД (более 9500 человек), включая соловецкие этапы. Здесь погибли цвет белорусской культуры (Владислав Голубок, Симон Барановых и др.). В 2004 году установлен памятный Белорусский крест жертвам репрессий.",
        "en": "Mass execution site and cemetery of the Great Terror in Karelia where over 9,500 victims were executed by the NKVD in 1937–1938, including hundreds from the Solovki transports and Belarusian intellectuals like Uladzislaw Halubok. A memorial Belarusian Cross was erected here in 2004."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Sandarmokh_cross.jpg/960px-Sandarmokh_cross.jpg",
    "links": [
        {"title": "Сандармох — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Сандармох"}
    ],
    "tags": ["Сандармох", "ГУЛАГ", "Карэлія", "Крыж", "расстрэлы", "Галубок", "monument"],
    "unverifiedCoordinates": False
})

upsert_place({
    "id": "gulag-inta-geniyush",
    "title": {
        "by": "Мінлаг / Інталаг у Інце — пакуты і лагерная паэзія Ларысы Геніюш",
        "ru": "Минлаг / Инталаг в Инте — лагерная ссылка Ларисы Гениюш",
        "en": "Intalag / Minlag Camp in Inta — Larysa Heniyush's GULAG Poems"
    },
    "category": "historical",
    "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
    "city": {"by": "Інта", "ru": "Инта", "en": "Inta"},
    "coordinates": [65.9995, 60.1317],
    "description": {
        "by": "Асаблівы лагер № 1 (Мінлаг) і Інталаг у Комі АССР, дзе на шахтах здабычы вугалю адбывалі тэрміны тысячы палітвязняў. Сюды пасля выкрадання савецкім СМЕРШам з Прагі ў 1949–1956 гг. былі кінуты паэтка і сакратар Рады БНР Ларыса Геніюш разам з мужам Янкам. Менавіта ў інцінскіх бараках Геніюш стварыла свае знакамітыя вершы духоўнага супраціву, якія сукамерніцы завучвалі на памяць.",
        "ru": "Особый лагерь № 1 (Минлаг) и Инталаг в Коми, где на угольных шахтах трудились политзаключенные. В 1949–1956 годах здесь отбывала заключение выдающаяся белорусская поэтесса Лариса Гениюш и ее супруг Иван Гениюш, похищенные советскими спецслужбами из Праги.",
        "en": "Special Camp No. 1 (Minlag) in the Komi Republic where thousands of political prisoners worked the coal mines. Belarusian national poet and BNR Secretary Larysa Heniyush and her husband Yanka were imprisoned here from 1949 to 1956 following their kidnapping from Prague. Here she penned heroic clandestine verses of spiritual defiance."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Inta_mining_tower.jpg/960px-Inta_mining_tower.jpg",
    "links": [
        {"title": "Ларыса Геніюш — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Ларыса_Антонаўна_Геніюш"},
        {"title": "Мінлаг — Вікіпедыя", "url": "https://ru.wikipedia.org/wiki/Минлаг"}
    ],
    "tags": ["ГУЛАГ", "Інта", "Мінлаг", "Геніюш", "Комі", "вершы", "historical"],
    "personId": "larysa-heniyush",
    "personIds": ["larysa-heniyush"],
    "unverifiedCoordinates": False
})

upsert_place({
    "id": "gulag-vorkuta-repost",
    "title": {
        "by": "Варкутлаг і мемарыял Юр-Шор — Варкуцінскае паўстанне 1953 года",
        "ru": "Воркутлаг и мемориал Юр-Шор — Воркутинское восстание 1953 года",
        "en": "Vorkutlag & Yur-Shor Memorial — Vorkuta Uprising of 1953"
    },
    "category": "monument",
    "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
    "city": {"by": "Варкута", "ru": "Воркута", "en": "Vorkuta"},
    "coordinates": [67.5950, 64.1200],
    "description": {
        "by": "Адзін з найбуйнейшых запалярных лагерных комплексаў ГУЛАГа. У ліпені–жніўні 1953 г. тут адбылося легендарнае Варкуцінскае паўстанне вязняў Рэчлага (шахта № 29, Юр-Шор), у якім актыўны ўдзел бралі беларускія палітвязні. На мемарыяльных могілках Юр-Шор усталяваны памятныя знакі і крыжы загінулым паўстанцам і ахвярам лагера, у тым ліку беларусам.",
        "ru": "Крупнейший арктический лагерный комплекс. В 1953 году здесь вспыхнуло легендарное Воркутинское восстание узников Речлага (шахта № 29 Юр-Шор), где белорусские политзаключенные составляли значительную часть сопротивления. На мемориале в Юр-Шоре установлены кресты погибшим узникам.",
        "en": "One of the largest polar camp complexes of the GULAG. In July–August 1953, the historic Vorkuta Uprising of Rechlag prisoners erupted here at Mine No. 29 (Yur-Shor), involving hundreds of Belarusian political prisoners. The Yur-Shor memorial cemetery preserves memorials and crosses to the victims."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Vorkuta_Yurshor_memorial.jpg/960px-Vorkuta_Yurshor_memorial.jpg",
    "links": [
        {"title": "Варкуцінскае паўстанне — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Варкуцінскае_паўстанне"},
        {"title": "Варкутлаг — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Варкутлаг"}
    ],
    "tags": ["ГУЛАГ", "Варкута", "Юр-Шор", "паўстанне", "Рэчлаг", "monument"],
    "unverifiedCoordinates": False
})

upsert_place({
    "id": "gulag-kolyma-maska-smutku",
    "title": {
        "by": "Калыма і манумент «Маска смутку» ў Магадане — золата на касцях",
        "ru": "Колыма и монумент «Маска скорби» в Магадане — золото на костях",
        "en": "Kolyma & 'Mask of Sorrow' in Magadan — The Coldest Hell of the GULAG"
    },
    "category": "monument",
    "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
    "city": {"by": "Магадан", "ru": "Магадан", "en": "Magadan"},
    "coordinates": [59.5925, 150.8122],
    "description": {
        "by": "Сталіца Дальбуда і калымскіх залатых руднікоў, дзе загінулі дзесяткі тысяч ураджэнцаў Беларусі. Праз пекла Калымы прайшлі беларускія пісьменнікі Сяргей Грахоўскі, Алесь Звонак, Станіслаў Шушкевіч-старэйшы, Алесь Дудар (расстраляны ў 1937 г.). У памяць пра сотні тысяч закатаваных на сопцы Крутая ў 1996 г. пастаўлены грандыёзны манумент Эрнста Невядомага «Маска смутку».",
        "ru": "Столица Дальстроя и колымских золотых приисков. Через колымские лагеря прошли белорусские литераторы Сергей Граховский, Алесь Звонак, Станислав Шушкевич-старший и тысячи белорусов. На сопке Крутая воздвигнут монумент Эрнста Неизвестного «Маска скорби».",
        "en": "Center of Dalstroy and Kolyma gold mining camps where tens of thousands of Belarusians perished. Belarusian writers Siarhiej Hrahouski, Ales Zvonak, and Stanislaw Shushkevich Sr. survived years of hard labor here. Ernst Neizvestny's colossal 'Mask of Sorrow' monument sits atop Krutaya Hill overlooking Magadan."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Mask_of_Sorrow_in_Magadan.jpg/960px-Mask_of_Sorrow_in_Magadan.jpg",
    "links": [
        {"title": "Маска смутку — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Маска_смутку"},
        {"title": "Сяргей Грахоўскі — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Сяргей_Іванавіч_Грахоўскі"}
    ],
    "tags": ["ГУЛАГ", "Калыма", "Магадан", "Маска смутку", "Грахоўскі", "monument"],
    "personId": "siarhiej-hrahouski",
    "personIds": ["siarhiej-hrahouski"],
    "unverifiedCoordinates": False
})

upsert_place({
    "id": "gulag-karlag-dolinka",
    "title": {
        "by": "Карлаг і музей памяці ахвяр рэпрэсій у Далінцы (Казахстан)",
        "ru": "Карлаг и Музей памяти жертв политических репрессий в Долинке (Казахстан)",
        "en": "Karlag Memorial Museum in Dolinka (Kazakhstan)"
    },
    "category": "culture",
    "country": {"by": "Казахстан", "ru": "Казахстан", "en": "Kazakhstan"},
    "city": {"by": "Далінка", "ru": "Долинка", "en": "Dolinka"},
    "coordinates": [49.6800, 72.6900],
    "description": {
        "by": "Карагандзінскі папраўча-працоўны лагер — адзін з найвялікшых лагераў у свеце, чыя тэрыторыя перавышала плошчу Францыі. Тут і ў яго аддзяленні АЛЖЫР (Акмолінскі лагер жонак здраднікаў Радзімы) сядзелі тысячы беларусаў, у тым ліку жонкі расстраляных беларускіх паэтаў (Міхася Чарота, Платона Галавача, Алеся Дудара). У будынку кіраўніцтва Карлага ў пасёлку Далінка дзейнічае Музей памяці ахвяр палітычных рэпрэсій.",
        "ru": "Карагандинский лагерь (Карлаг) — гигантский лагерный архипелаг в степях Казахстана. В Карлаге и лагере АЛЖИР отбывали сроки тысячи белорусов, включая жен расстрелянных белорусских писателей. В историческом здании Управления Карлага в Долинке открыт Музей памяти жертв политических репрессий.",
        "en": "The Karaganda labor camp (Karlag), one of the largest in the GULAG spanning territory greater than France. Held thousands of Belarusians, while its ALZHIR branch held wives of executed Belarusian poets (Mikhas Charot, Platon Halavach, Ales Dudar). The former Karlag Administration building in Dolinka now houses the Memorial Museum of Victims of Political Repression."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Karlag_Museum_Dolinka.jpg/960px-Karlag_Museum_Dolinka.jpg",
    "links": [
        {"title": "Карлаг — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Карлаг"}
    ],
    "tags": ["ГУЛАГ", "Карлаг", "Далінка", "Казахстан", "АЛЖЫР", "музей", "culture"],
    "unverifiedCoordinates": False
})

upsert_place({
    "id": "gulag-kengir-steplag",
    "title": {
        "by": "Сцяплаг і Кенгірскае паўстанне 1954 года (Жэзказган)",
        "ru": "Степлаг и Кенгирское восстание 1954 года (Жезказган)",
        "en": "Steplag & The 40 Days of Kengir Uprising in Zhezkazgan"
    },
    "category": "historical",
    "country": {"by": "Казахстан", "ru": "Казахстан", "en": "Kazakhstan"},
    "city": {"by": "Жэзказган", "ru": "Жезказган", "en": "Zhezkazgan"},
    "coordinates": [47.7833, 67.7667],
    "description": {
        "by": "Сцяпны лагер (Сцяплаг) МУС СССР каля пасёлка Кенгір. У траўні–чэрвені 1954 года тут успыхнула самае маштабнае паўстанне ў гісторыі ГУЛАГа: больш за 5000 вязняў (сярод якіх была вялікая колькасць беларусаў і ўкраінцаў) 40 дзён трымалі лагер пад сваім кантролем, патрабуючы свабоды. Паўстанне было бязлітасна задушана танкамі Т-34.",
        "ru": "Степной лагерь (Степлаг) около Кенгира. В мае-июне 1954 года здесь произошло самое знаменитое восстание в истории ГУЛАГа: более 5000 узников (среди которых было множество белорусов) 40 дней удерживали лагерь под своим контролем. Восстание было раздавлено танками Т-34.",
        "en": "Steplag near Kengir was the stage for the historic Kengir Uprising of May–June 1954. Over 5,000 prisoners, including many Belarusians and Ukrainians, revolted against the MVD and established a self-governing camp republic for 40 days until crushed by Soviet T-34 tanks."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Zhezkazgan_monument.jpg/960px-Zhezkazgan_monument.jpg",
    "links": [
        {"title": "Кенгірскае паўстанне — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Кенгірскае_паўстанне"}
    ],
    "tags": ["ГУЛАГ", "Кенгір", "Сцяплаг", "паўстанне", "Казахстан", "historical"],
    "unverifiedCoordinates": False
})

upsert_place({
    "id": "gulag-norillag-memorial",
    "title": {
        "by": "Нарыльлаг і мемарыял «Нарыльская Галгофа» — паўстанне 1953 года",
        "ru": "Норильлаг и мемориал «Норильская Голгофа» — восстание 1953 года",
        "en": "Norillag & 'Norilsk Golgotha' Memorial at Mount Schmidt"
    },
    "category": "monument",
    "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
    "city": {"by": "Нарыльск", "ru": "Норильск", "en": "Norilsk"},
    "coordinates": [69.3190, 88.1780],
    "description": {
        "by": "Нарыльскі лагер за палярным кругам, дзе на нікелевых і медных рудніках пакутавалі сотні тысяч нявольнікаў. У траўні–жніўні 1953 г. тут адбылося Нарыльскае паўстанне. Ля падножжа гары Шміта на месцы масавых пахаванняў створаны мемарыяльны комплекс «Нарыльская Галгофа» са званіцай і памятнымі крыжамі ахвярам рэпрэсій з Беларусі, Польшчы, Літвы і Украіны.",
        "ru": "Норильский лагерь за полярным кругом. В 1953 году здесь вспыхнуло Норильское восстание. У подножия горы Шмидта на месте массовых захоронений создан мемориальный комплекс «Норильская Голгофа» с крестами жертвам репрессий из Беларуси, Польши, стран Балтии.",
        "en": "Norillag labor camp above the Arctic Circle. Site of the major Norilsk Uprising in the summer of 1953. At the foot of Mount Schmidt, on the mass graves of prisoners, stands the 'Norilsk Golgotha' memorial complex honoring victims from Belarus, Poland, Lithuania, and Ukraine."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Norilsk_Golgotha_Memorial.jpg/960px-Norilsk_Golgotha_Memorial.jpg",
    "links": [
        {"title": "Нарыльскае паўстанне — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Нарыльскае_паўстанне"},
        {"title": "Нарыльлаг — Вікіпедыя", "url": "https://ru.wikipedia.org/wiki/Норильлаг"}
    ],
    "tags": ["ГУЛАГ", "Нарыльск", "Нарыльлаг", "Галгофа", "паўстанне", "monument"],
    "unverifiedCoordinates": False
})

# ==========================================
# 3. NAZI CONCENTRATION CAMPS
# ==========================================

upsert_place({
    "id": "nazi-camp-auschwitz-birkenau",
    "title": {
        "by": "Аўшвіц-Біркенаў — фабрыка смерці і памяць ахвяр з Беларусі",
        "ru": "Аушвиц-Биркенау — лагерь уничтожения и память жертв из Беларуси",
        "en": "Auschwitz-Birkenau Memorial and Museum"
    },
    "category": "monument",
    "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
    "city": {"by": "Асвенцім", "ru": "Освенцим", "en": "Oświęcim"},
    "coordinates": [50.0264, 19.2040],
    "description": {
        "by": "Найбуйнейшы нацысцкі канцэнтрацыйны лагер і лагер смерці. Сюды былі дэпартаваны і знішчаны сотні тысяч грамадзян з беларускіх земляў — у першую чаргу габрэі з гета Заходняй і Усходняй Беларусі (Гродна, Брэст, Беласток, Навагрудак), а таксама беларускія падпольшчыкі, партызаны і ваеннапалонныя. Дзяржаўны музей Аўшвіц-Біркенаў з'яўляецца сусветным мемарыялам Халакосту.",
        "ru": "Крупнейший нацистский лагерь смерти. Сюда были депортированы и уничтожены сотни тысяч узников из Беларуси — евреи из гетто Гродно, Бреста, Белостока, а также белорусские подпольщики, партизаны и военнопленные.",
        "en": "The largest Nazi concentration and extermination camp. Hundreds of thousands from Belarusian lands were murdered here, predominantly Jews deported from the ghettos of Grodno, Brest, Bialystok, and Novogrudok, alongside Belarusian resistance fighters and Soviet POWs."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Auschwitz_Birkenau_Gate.jpg/960px-Auschwitz_Birkenau_Gate.jpg",
    "links": [
        {"title": "Асвенцім — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Асвенцім_(канцэнтрацыйны_лагер)"}
    ],
    "tags": ["Аўшвіц", "Асвенцім", "Халакост", "нацызм", "лагер смерці", "Польшча", "monument"],
    "unverifiedCoordinates": False
})

upsert_place({
    "id": "nazi-camp-sobibor-revolt",
    "title": {
        "by": "Сабібор — лагер знішчэння і легендарнае паўстанне менскіх вязняў 1943 года",
        "ru": "Собибор — лагерь уничтожения и восстание узников Минского гетто 1943 года",
        "en": "Sobibor Extermination Camp & Partisan Revolt of 1943"
    },
    "category": "monument",
    "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
    "city": {"by": "Сабібур", "ru": "Собибур", "en": "Sobibór"},
    "coordinates": [51.4486, 23.5936],
    "description": {
        "by": "Лагер знішчэння ў Люблінскім ваяводстве, дзе было забіта каля 250 тысяч чалавек, у тым ліку тысячы вязняў з Менскага гета. 14 кастрычніка 1943 года тут адбылося адзінае цалкам паспяховае масавае паўстанне ў гісторыі нацысцкіх лагераў смерці, якое ўзначалілі савецкі афіцэр Аляксандр Пячэрскі і байцы Менскага падполля.",
        "ru": "Лагерь смерти в Польше. 14 октября 1943 года здесь произошло единственное успешное восстание в нацистских лагерях уничтожения, организованное советским офицером Александром Печерским и узниками Минского гетто, вырвавшимися на свободу.",
        "en": "Nazi extermination camp where roughly 250,000 Jews were murdered, including thousands transported from the Minsk Ghetto. On October 14, 1943, it witnessed the only successful mass uprising in any Nazi death camp, spearheaded by POW Alexander Pechersky and Minsk ghetto underground fighters."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Sobibor_memorial_mound.jpg/960px-Sobibor_memorial_mound.jpg",
    "links": [
        {"title": "Сабібор — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Сабібор_(лагер_смерці)"},
        {"title": "Паўстанне ў лагеры Сабібор — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Паўстанне_ў_Сабіборы"}
    ],
    "tags": ["Сабібор", "Менскае гета", "паўстанне", "Пячэрскі", "Халакост", "monument"],
    "unverifiedCoordinates": False
})

upsert_place({
    "id": "nazi-camp-mauthausen-memorial",
    "title": {
        "by": "Маўтхаўзен — каменны кар'ер, пакуты беларусаў і паўстанне Блока № 20",
        "ru": "Маутхаузен — каменоломни смерти и восстание Блока № 20",
        "en": "Mauthausen Memorial & The Heroic Block 20 Revolt"
    },
    "category": "monument",
    "country": {"by": "Аўстрыя", "ru": "Австрия", "en": "Austria"},
    "city": {"by": "Маўтхаўзен", "ru": "Маутхаузен", "en": "Mauthausen"},
    "coordinates": [48.2575, 14.5005],
    "description": {
        "by": "Адзін з самых жорсткіх нацысцкіх канцлагераў (катэгорыя III) са «Сходамі смерці» на гранітным кар'еры. Тут загінулі тысячы беларускіх вязняў і ваеннапалонных. 2 лютага 1945 г. смяротнікі Блока № 20 (савецкія і беларускія афіцэры) здзейснілі бяспрыкладны гераічны ўцёк-паўстанне, пайшоўшы голымі рукамі на кулямёты эсэсаўцаў.",
        "ru": "Концлагерь высшей категории жестокости в Австрии с печально известной «Лестницей смерти». Здесь погибли тысячи белорусов. В ночь на 2 февраля 1945 года советские военнопленные Блока смертников № 20 совершили беспримерное вооруженное восстание и массовый побег.",
        "en": "Brutal Category III Nazi concentration camp in Upper Austria known for its granite quarry and 'Stairs of Death'. Held thousands of Belarusian POWs and partisans. On February 2, 1945, condemned officers in Death Block 20 mounted a legendary bare-handed assault against SS machine guns to break out."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Mauthausen_monuments.jpg/960px-Mauthausen_monuments.jpg",
    "links": [
        {"title": "Маўтхаўзен — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Маўтхаўзен_(канцэнтрацыйны_лагер)"}
    ],
    "tags": ["Маўтхаўзен", "Аўстрыя", "Блок 20", "паўстанне", "нацызм", "monument"],
    "unverifiedCoordinates": False
})

upsert_place({
    "id": "nazi-camp-buchenwald-memorial",
    "title": {
        "by": "Канцлагер Бухенвальд — мемарыял і памяць беларускіх ахвяр",
        "ru": "Концлагерь Бухенвальд — мемориал и память белорусских узников",
        "en": "Buchenwald Memorial & Resistance"
    },
    "category": "monument",
    "country": {"by": "Германія", "ru": "Германия", "en": "Germany"},
    "city": {"by": "Ваймар", "ru": "Веймар", "en": "Weimar"},
    "coordinates": [51.0222, 11.2492],
    "description": {
        "by": "Адзін з найбуйнейшых нацысцкіх канцлагераў на тэрыторыі Германіі каля Ваймара. Праз яго прайшлі больш за 250 000 чалавек, у тым ліку тысячы вывезеных з Беларусі остарбайтараў, падпольшчыкаў і ваеннапалонных. 11 красавіка 1945 года інтэрнацыянальнае падполле Бухенвальда падняло ўзброенае паўстанне і вызваліла лагер да прыходу саюзнікаў.",
        "ru": "Один из крупнейших концлагерей нацистской Германии близ Веймара. Здесь содержались тысячи белорусских подпольщиков, остарбайтеров и военнопленных. 11 апреля 1945 года интернациональное подполье лагеря подняло победоносное вооруженное восстание.",
        "en": "Major Nazi concentration camp established near Weimar. Imprisoned more than 250,000 victims, including thousands of captured Belarusian underground fighters and forced laborers. On April 11, 1945, the underground resistance staged an armed uprising and liberated the camp."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Buchenwald_Bell_Tower.jpg/960px-Buchenwald_Bell_Tower.jpg",
    "links": [
        {"title": "Бухенвальд — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Бухенвальд"}
    ],
    "tags": ["Бухенвальд", "Германія", "Ваймар", "паўстанне", "нацызм", "monument"],
    "unverifiedCoordinates": False
})

upsert_place({
    "id": "nazi-camp-ravensbruck-women",
    "title": {
        "by": "Равенсбрук — галоўны жаночы канцлагер і подзвіг беларускіх жанчын",
        "ru": "Равенсбрюк — главный женский концлагерь и подвиг белорусских женщин",
        "en": "Ravensbrück Memorial — Nazi Women's Concentration Camp"
    },
    "category": "monument",
    "country": {"by": "Германія", "ru": "Германия", "en": "Germany"},
    "city": {"by": "Фюрстэнберг", "ru": "Фюрстенберг", "en": "Fürstenberg/Havel"},
    "coordinates": [53.1906, 13.1672],
    "description": {
        "by": "Галоўны нацысцкі канцэнтрацыйны лагер для жанчын у Германіі (за 90 км на поўнач ад Берліна). Сюды масава этапавалі беларускіх жанчын-падпольшчыц, партызанак, медсясцёр і закладніц з карных аперацый у Беларусі. Вязніцы падвяргаліся катаванням і псеўдамедыцынскім эксперыментам.",
        "ru": "Главный женский концентрационный лагерь нацистов в Германии. Сюда отправляли белорусских подпольщиц, партизанок, медсестер и женщин, захваченных в ходе карательных операций в Беларуси. Место мученичества десятков тысяч женщин.",
        "en": "The primary Nazi concentration camp for women in Germany, 90 km north of Berlin. Thousands of Belarusian female underground fighters, partisans, medical workers, and civilian hostages were imprisoned here and subjected to brutal forced labor and medical experiments."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Ravensbrueck_memorial.jpg/960px-Ravensbrueck_memorial.jpg",
    "links": [
        {"title": "Равенсбрук — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Равенсбрук"}
    ],
    "tags": ["Равенсбрук", "Германія", "жанчыны", "партызанкі", "нацызм", "monument"],
    "unverifiedCoordinates": False
})

upsert_place({
    "id": "nazi-camp-sachsenhausen",
    "title": {
        "by": "Заксенхаўзен — лагер пад Берлінам і знішчэнне антыфашыстаў",
        "ru": "Заксенхаузен — лагерь под Берлином и уничтожение антифашистов",
        "en": "Sachsenhausen Concentration Camp Memorial in Oranienburg"
    },
    "category": "monument",
    "country": {"by": "Германія", "ru": "Германия", "en": "Germany"},
    "city": {"by": "Араніенбург", "ru": "Ораниенбург", "en": "Oranienburg"},
    "coordinates": [52.7661, 13.2642],
    "description": {
        "by": "Узорны нацысцкі канцлагер пад Берлінам, адміністрацыйны цэнтр усёй сістэмы лагераў. Тут у «Станцыі Z» масава расстрэльвалі савецкіх ваеннапалонных і беларускіх дзеячаў Супраціву. У лагеры дзейнічала інтэрнацыянальнае антыфашысцкае падполле.",
        "ru": "Концентрационный лагерь близ Берлина, служивший административным центром лагерной системы СС. Здесь на «Станции Z» уничтожались советские военнопленные и участники антифашистского Сопротивления из Беларуси.",
        "en": "Model Nazi concentration camp in Oranienburg near Berlin, headquarters for the Inspectorate of Concentration Camps. Thousands of Soviet POWs and Belarusian resistance members were methodically exterminated at 'Station Z'."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Sachsenhausen_Memorial_2011.jpg/960px-Sachsenhausen_Memorial_2011.jpg",
    "links": [
        {"title": "Заксенхаўзен — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Заксенхаўзен"}
    ],
    "tags": ["Заксенхаўзен", "Германія", "Берлін", "Араніенбург", "нацызм", "monument"],
    "unverifiedCoordinates": False
})

upsert_place({
    "id": "nazi-camp-dachau-memorial",
    "title": {
        "by": "Дахаў — першы нацысцкі канцлагер у Баварыі і беларускія вязні",
        "ru": "Дахау — первый нацистский концлагерь в Баварии и белорусские узники",
        "en": "Dachau Concentration Camp Memorial Site"
    },
    "category": "monument",
    "country": {"by": "Германія", "ru": "Германия", "en": "Germany"},
    "city": {"by": "Дахаў", "ru": "Дахау", "en": "Dachau"},
    "coordinates": [48.2700, 11.4683],
    "description": {
        "by": "Першы канцэнтрацыйны лагер нацысцкай Германіі, адкрыты ў 1933 годзе пад Мюнхенам. Праз Дахаў прайшлі дзесяткі святароў з Беларусі і Польшчы («барак святароў»), антыфашысты, палітычныя дзеячы і прымусовыя рабочыя. Дзейнічае мемарыяльны комплекс.",
        "ru": "Первый нацистский концлагерь, открытый в 1933 году около Мюнхена. Через него прошли католические священники из Беларуси и Польши, политические противники нацизма и тысячи советских граждан.",
        "en": "The first Nazi concentration camp opened in 1933 near Munich. Imprisoned Catholic clergy from Belarus and Poland in the infamous 'Priest Barracks', alongside political dissidents and anti-fascist fighters."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Dachau_Jourhaus_Gate.jpg/960px-Dachau_Jourhaus_Gate.jpg",
    "links": [
        {"title": "Дахаў — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Дахаў_(канцэнтрацыйны_лагер)"}
    ],
    "tags": ["Дахаў", "Германія", "Баварыя", "Мюнхен", "нацызм", "monument"],
    "unverifiedCoordinates": False
})

upsert_place({
    "id": "nazi-camp-stutthof-memorial",
    "title": {
        "by": "Штутгоф — канцлагер пад Гданьскам і ахвяры з Заходняй Беларусі",
        "ru": "Штуттгоф — концлагерь под Гданьском и жертвы из Западной Беларуси",
        "en": "Stutthof Concentration Camp Memorial in Sztutowo"
    },
    "category": "monument",
    "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
    "city": {"by": "Штутава", "ru": "Штутово", "en": "Sztutowo"},
    "coordinates": [54.3314, 19.1625],
    "description": {
        "by": "Нацысцкі канцлагер на ўзбярэжжы Балтыкі каля Гданьска. Сюды масава дэпартавалі і знішчалі жыхароў Заходняй Беларусі, Віленшчыны і Беласточчыны: інтэлігенцыю, каталіцкіх ксяндзоў, удзельнікаў руху Супраціву і габрэяў з гета.",
        "ru": "Концлагерь на побережье Балтийского моря возле Гданьска. Место массового уничтожения узников из Западной Беларуси, Вильнюсского края и Белосточчины: интеллигенции, священников, антифашистов.",
        "en": "Nazi concentration camp on the Baltic coast near Gdańsk. A major site of imprisonment and murder for victims from Western Belarus, the Vilnius region, and Bialystok, including intelligentsia, clergy, and partisans."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Stutthof_Gate_of_Death.jpg/960px-Stutthof_Gate_of_Death.jpg",
    "links": [
        {"title": "Штутгоф — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Штутгоф"}
    ],
    "tags": ["Штутгоф", "Польшча", "Гданьск", "Заходняя Беларусь", "нацызм", "monument"],
    "unverifiedCoordinates": False
})

# ==========================================
# 4. KYIV & LVIV
# ==========================================

upsert_place({
    "id": "kyiv-pechersk-lavra-hleb-minskirad",
    "title": {
        "by": "Кіева-Пячэрская лаўра — пахаванне Глеба Менскага і мошчы Еўфрасінні",
        "ru": "Киево-Печерская лавра — гробница Глеба Минского и мощи Евфросинии Полоцкой",
        "en": "Kyiv-Pechersk Lavra — Tomb of Prince Hleb of Minsk & St. Euphrosyne"
    },
    "category": "church",
    "country": {"by": "Украіна", "ru": "Украина", "en": "Ukraine"},
    "city": {"by": "Кіеў", "ru": "Киев", "en": "Kyiv"},
    "coordinates": [50.4345, 30.5574],
    "description": {
        "by": "Старажытная праваслаўная святыня, цесна звязаная з беларускай гісторыяй. Тут стваралася «Аповесць мінулых гадоў» з першымі згадкамі Полацка, Менска, Турава і Віцебска. У Дальніх пячорах з 1187 па 1910 год спачывалі святыя мошчы прападобнай Еўфрасінні Полацкай перад іх урачыстым вяртаннем у Полацк. У Лаўры пахаваны сын Усяслава Чарадзея — першы летапісны менскі князь Глеб Менскі (памёр у 1119 г.).",
        "ru": "Древняя святыня, тесно связанная с историей Беларуси. Здесь в Дальних пещерах более семи веков (1187–1910) покоились мощи преподобной Евфросинии Полоцкой. В лавре погребен сын Всеслава Чародея, основатель Минского княжества князь Глеб Минский (умер в 1119 г.).",
        "en": "Historic cradle of Eastern Slavic Orthodoxy. For over seven centuries (1187–1910), the holy relics of Saint Euphrosyne of Polotsk rested in its Far Caves before returning to Polotsk. The Lavra is also the final resting place of Prince Hleb of Minsk (son of Prince Usiaslaw the Sorcerer, died in captivity in 1119)."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Kyiv_Pechersk_Lavra_Great_Belfry_2011.jpg/960px-Kyiv_Pechersk_Lavra_Great_Belfry_2011.jpg",
    "links": [
        {"title": "Кіева-Пячэрская лаўра — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Кіева-Пячэрская_лаўра"},
        {"title": "Глеб Усяславіч — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Глеб_Усяславіч"}
    ],
    "tags": ["Кіеў", "Украіна", "Лаўра", "Еўфрасіння Полацкая", "Глеб Менскі", "church"],
    "personId": "hleb-usyaslavich",
    "personIds": ["hleb-usyaslavich", "euphrosyne-polotsk"],
    "unverifiedCoordinates": False
})

upsert_place({
    "id": "kyiv-university-philology-karatkevich",
    "title": {
        "by": "Інстытут філалогіі Кіеўскага ўніверсітэта (Караткевіч і Доўнар-Запольскі)",
        "ru": "Институт филологии Киевского университета (Короткевич и Довнар-Запольский)",
        "en": "Institute of Philology at Taras Shevchenko University in Kyiv"
    },
    "category": "culture",
    "country": {"by": "Украіна", "ru": "Украина", "en": "Ukraine"},
    "city": {"by": "Кіеў", "ru": "Киев", "en": "Kyiv"},
    "coordinates": [50.4431, 30.5106],
    "description": {
        "by": "Гістарычны корпус універсітэта на бульвары Тараса Шаўчэнкі, 14. Тут вучыўся і скончыў аспірантуру класік беларускай літаратуры Уладзімір Караткевіч (выпуск 1954 г.), дзе стварыў першы варыянт «Дзікага палявання караля Стаха» і задумаў раман «Каласы пад сярпом тваім». Таксама ва ўніверсітэце працаваў выбітны беларускі гісторык прафесар Мітрафан Доўнар-Запольскі.",
        "ru": "Историческое здание Института филологии КНУ им. Тараса Шевченко (бульвар Шевченко, 14). В 1954 г. его окончил будущий классик белорусской литературы Владимир Короткевич, написавший здесь первый вариант «Дикой охоты короля Стаха». В университете также преподавал выдающийся историк Митрофан Довнар-Запольский.",
        "en": "Historic building of the Institute of Philology at Shevchenko National University of Kyiv (Taras Shevchenko Blvd 14). Alumnus Vladimir Karatkevich graduated here in 1954, conceptualizing 'King Stakh's Wild Hunt' and 'Ears of Rye Under Thy Sickle'. Historic home of pioneer Belarusian historian Professor Mitrafan Dounar-Zapolski."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Kyiv_Shevchenko_University_yellow_building.jpg/960px-Kyiv_Shevchenko_University_yellow_building.jpg",
    "links": [
        {"title": "Кіеўскі нацыянальны ўніверсітэт — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Кіеўскі_нацыянальны_ўніверсітэт_імя_Тараса_Шаўчэнкі"},
        {"title": "Уладзімір Караткевіч — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Уладзімір_Сямёнавіч_Караткевіч"}
    ],
    "tags": ["Кіеў", "Украіна", "Караткевіч", "Доўнар-Запольскі", "універсітэт", "culture"],
    "personId": "uladzimir-karatkevich",
    "personIds": ["uladzimir-karatkevich", "mitrafan-dounar-zapolski"],
    "unverifiedCoordinates": False
})

upsert_place({
    "id": "kyiv-karatkevich-monument",
    "title": {
        "by": "Помнік Уладзіміру Караткевічу ў Кіеве",
        "ru": "Памятник Владимиру Короткевичу в Киеве",
        "en": "Monument to Uladzimir Karatkevich in Kyiv"
    },
    "category": "monument",
    "country": {"by": "Украіна", "ru": "Украина", "en": "Ukraine"},
    "city": {"by": "Кіеў", "ru": "Киев", "en": "Kyiv"},
    "coordinates": [50.4486, 30.5015],
    "description": {
        "by": "Бронзавы помнік выбітнаму беларускаму пісьменніку Уладзіміру Караткевічу на вуліцы Міхаіла Кацюбінскага, 3. Адкрыты ў кастрычніку 2011 года. Постаць пісьменніка вышынёй 2,5 метра стаіць на фоне разгорнутай кнігі, на якой выбіты радкі з яго верша на беларускай і ўкраінскай мовах.",
        "ru": "Бронзовый памятник классику белорусской литературы Владимиру Короткевичу на ул. Михаила Коцюбинского, 3. Открыт в 2011 году. Скульптура высотой 2,5 метра изображает писателя на фоне раскрытой книги с его стихами на белорусском и украинском языках.",
        "en": "Bronze monument to classic Belarusian writer Uladzimir Karatkevich on Mykhaila Kotsyubynskoho St 3. Unveiled in October 2011. Depicts the 2.5-meter figure of the writer against an open book inscribed with verses in Belarusian and Ukrainian."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/U%C5%82adzimir_Karatkievi%C4%8D.jpg/330px-U%C5%82adzimir_Karatkievi%C4%8D.jpg",
    "links": [
        {"title": "Помнік Уладзіміру Караткевічу (Кіеў) — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Помнік_Уладзіміру_Караткевічу_(Кіеў)"}
    ],
    "tags": ["Кіеў", "Украіна", "Караткевіч", "помнік", "літаратура", "monument"],
    "personId": "uladzimir-karatkevich",
    "personIds": ["uladzimir-karatkevich"],
    "unverifiedCoordinates": False
})

upsert_place({
    "id": "kyiv-bessarabsky-market",
    "title": {
        "by": "Бесарабскі рынак у Кіеве (архітэктар Генрых Гай)",
        "ru": "Бессарабский рынок в Киеве (архитектор Генрих Гай)",
        "en": "Bessarabsky Market in Kyiv (Architect Henryk Gay)"
    },
    "category": "culture",
    "country": {"by": "Украіна", "ru": "Украина", "en": "Ukraine"},
    "city": {"by": "Кіеў", "ru": "Киев", "en": "Kyiv"},
    "coordinates": [50.4422, 30.5217],
    "description": {
        "by": "Знакаміты крыты рынак у пачатку Хрэшчаціка (Басейная вул., 2), пабудаваны ў 1910–1912 гг. у стылі мадэрн. Аўтарам праекта быў знакаміты польска-беларускі архітэктар Генрых Гай (Henryk Gay), які таксама спраектаваў цэлы шэраг знакавых будынкаў у цэнтры Мінска (даходныя дамы на Савецкай, 19 і Карла Маркса, 30, будынак МУС на пр. Незалежнасці, 15).",
        "ru": "Знаменитый крытый рынок Киева в стиле модерн на Бессарабской площади. Построен по проекту архитектора Генриха Гая, спроектировавшего также ключевые здания в Минске (ул. Советская, 19, ул. Карла Маркса, 30, здание МВД на пр. Независимости, 15).",
        "en": "Iconic Art Nouveau covered market hall on Bessarabska Square. Designed in 1910–1912 by architect Henryk Gay, who also designed landmark monumental buildings in central Minsk (Savetskaya St 19, Karl Marx St 30, and the MVD headquarters on Independence Ave 15)."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Bessarabsky_Market_Kyiv_2013.jpg/960px-Bessarabsky_Market_Kyiv_2013.jpg",
    "links": [
        {"title": "Бесарабскі рынак — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Бесарабскі_рынак"},
        {"title": "Генрых Гай — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Генрых_Юльян_Гай"}
    ],
    "tags": ["Кіеў", "Украіна", "Бесарабка", "Генрых Гай", "архітэктура", "culture"],
    "unverifiedCoordinates": False
})

upsert_place({
    "id": "kyiv-memorial-fallen-belarusians",
    "title": {
        "by": "Мемарыял беларусам, якія загінулі за Украіну (вул. Беларуская, 22)",
        "ru": "Мемориал белорусам, погибшим за Украину (ул. Белорусская, 22)",
        "en": "Memorial to Belarusians Fallen for Ukraine (Beloruska St 22, Kyiv)"
    },
    "category": "monument",
    "country": {"by": "Украіна", "ru": "Украина", "en": "Ukraine"},
    "city": {"by": "Кіеў", "ru": "Киев", "en": "Kyiv"},
    "coordinates": [50.4633, 30.4764],
    "description": {
        "by": "Памятны знак на будынку па вуліцы Беларускай, 22 у Кіеве. Прысвечаны беларускім добраахвотнікам і героям (сярод якіх Міхаіл Жызнеўскі, Алесь Чаркашын, Віталь Ціліжэнка, воіны Палка Каліноўскага і іншыя байцы), якія аддалі свае жыцці ў барацьбе за незалежнасць Украіны і свабоду Беларусі. На помніку выбіты беларускі нацыянальны герб «Пагоня» і словы «Жыве Беларусь! Слава Украіне!».",
        "ru": "Памятный знак на ул. Белорусской, 22 в Киеве, открытый в честь белорусских добровольцев (Михаил Жизневский, Алесь Черкашин, воины Полка Калиновского и др.), погибших за независимость Украины. На памятнике изображен герб «Погоня».",
        "en": "Memorial on Beloruska Street 22 in Kyiv honoring Belarusian volunteers (including Mikhail Zhyzneuski, Ales Charkashyn, Kastus Kalinouski Regiment soldiers, and others) who fell fighting for the independence of Ukraine and a free Belarus. Features the Pahonia coat of arms."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Mikhail_Zhyzneuski.jpg/330px-Mikhail_Zhyzneuski.jpg",
    "links": [
        {"title": "Рэформ: Ціханоўская ў Кіеве ўшанавала памяць загінулых беларусаў", "url": "https://reform.news/be/cihano-skaja-kieve-shanavala-pamjac-zaginulyh-belarusa/"}
    ],
    "tags": ["Кіеў", "Украіна", "Беларуская вул", "Пагоня", "добраахвотнікі", "Жызнеўскі", "monument"],
    "personId": "mikhail-zhyzneuski",
    "personIds": ["mikhail-zhyzneuski"],
    "unverifiedCoordinates": False
})

upsert_place({
    "id": "kyiv-memorial-zhyzneuski",
    "title": {
        "by": "Помнік Герою Украіны Міхаілу Жызнеўскаму на вуліцы Інстытуцкай",
        "ru": "Мемориал Герою Украины Михаилу Жизневскому на улице Институтской",
        "en": "Memorial to Hero of Ukraine Mikhail Zhyzneuski on Instytutska St"
    },
    "category": "monument",
    "country": {"by": "Украіна", "ru": "Украина", "en": "Ukraine"},
    "city": {"by": "Кіеў", "ru": "Киев", "en": "Kyiv"},
    "coordinates": [50.4490, 30.5280],
    "description": {
        "by": "Мемарыяльны знак на Алеі Герояў Нябеснай Сотні (вул. Інстытуцкая) у самым сэрцы Кіева. Прысвечаны беларускаму актывісту з Гомеля Міхаілу Жызнеўскаму (1988–2014), які загінуў тут 22 студзеня 2014 года і пасмяротна стаў першым іншаземцам — Героем Украіны. Месца ўшанавання беларускай дыяспарай і ўкраінцамі.",
        "ru": "Памятный знак на Аллее Героев Небесной Сотни (ул. Институтская) в Киеве белорусскому активисту из Гомеля Михаилу Жизневскому (1988–2014), погибшему на Евромайдане 22 января 2014 года и посмертно удостоенному звания Героя Украины.",
        "en": "Memorial on the Alley of the Heavenly Hundred Heroes (Instytutska St) in Kyiv dedicated to Belarusian activist from Gomel Mikhail Zhyzneuski (1988–2014), who was fatally shot on January 22, 2014 during Euromaidan and became the first foreigner awarded the title Hero of Ukraine."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Mikhail_Zhyzneuski.jpg/330px-Mikhail_Zhyzneuski.jpg",
    "links": [
        {"title": "Міхаіл Жызнеўскі — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Міхаіл_Міхайлавіч_Жызнеўскі"}
    ],
    "tags": ["Кіеў", "Украіна", "Майдан", "Жызнеўскі", "Нябесная Сотня", "Інстытуцкая", "monument"],
    "personId": "mikhail-zhyzneuski",
    "personIds": ["mikhail-zhyzneuski"],
    "unverifiedCoordinates": False
})

upsert_place({
    "id": "kyiv-mohyla-academy-polotsky-konissky",
    "title": {
        "by": "Кіева-Магілянская акадэмія (Сімяон Полацкі і Георгій Каніскі)",
        "ru": "Киево-Могилянская академия (Симеон Полоцкий и Георгий Конисский)",
        "en": "Kyiv-Mohyla Academy — Simeon of Polotsk & Georgij Konisskij"
    },
    "category": "culture",
    "country": {"by": "Украіна", "ru": "Украина", "en": "Ukraine"},
    "city": {"by": "Кіеў", "ru": "Киев", "en": "Kyiv"},
    "coordinates": [50.4661, 30.5208],
    "description": {
        "by": "Стараакадэмічны (Мазепін) корпус акадэміі на Контрактавай плошчы Подола (вул. Скаварады, 2). Славутая вышэйшая навучальная ўстанова, якую скончылі выбітны полацкі асветнік Сімяон Полацкі, а таксама архіепіскап Магілёўскі Георгій Каніскі. Акадэмія адыграла ключавую ролю ў адукацыі беларускай эліты XVII–XVIII стст.",
        "ru": "Староакадемический корпус Киево-Могилянской академии на Подоле (ул. Сковороды, 2). Колыбель просвещения, выпускниками которой были просветитель Симеон Полоцкий и архиепископ Могилевский Георгий Конисский.",
        "en": "Old Academic Building of the Kyiv-Mohyla Academy on Kontraktova Square (Podil). Historic alma mater of prominent Belarusian Baroque enlightener Simeon of Polotsk and Archbishop of Mogilev Georgij Konisskij."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Old_Academic_Building_Kyiv-Mohyla_Academy.jpg/960px-Old_Academic_Building_Kyiv-Mohyla_Academy.jpg",
    "links": [
        {"title": "Кіева-Магілянская акадэмія — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Кіева-Магілянская_акадэмія"},
        {"title": "Сімяон Полацкі — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Сімяон_Полацкі"}
    ],
    "tags": ["Кіеў", "Украіна", "Падол", "Магілянка", "Сімяон Полацкі", "Каніскі", "culture"],
    "personId": "simeon-polotsky",
    "personIds": ["simeon-polotsky"],
    "unverifiedCoordinates": False
})

upsert_place({
    "id": "lviv-dom-volnay-belarusi",
    "title": {
        "by": "Дом Вольнай Беларусі і Беларускі крызісны цэнтр у Львове",
        "ru": "Дом Свободной Беларуси и Белорусский кризисный центр во Львове",
        "en": "Free Belarus Hub & Belarusian Crisis Center in Lviv"
    },
    "category": "culture",
    "country": {"by": "Украіна", "ru": "Украина", "en": "Ukraine"},
    "city": {"by": "Львоў", "ru": "Львов", "en": "Lviv"},
    "coordinates": [49.8398, 24.0205],
    "description": {
        "by": "Грамадска-культурная прастора беларускай дыяспары ў Львове (вул. Касцюшкі / Мацейка). Цэнтр дапамогі беларускім рэлакантам і добраахвотнікам, дзе ладзяцца курсы беларускай мовы, культурныя імпрэзы, сустрэчы і выставы.",
        "ru": "Общественно-культурное пространство белорусской диаспоры во Львове. Центр помощи белорусам и добровольцам, площадка проведения курсов белорусского языка, выставок и культурных встреч.",
        "en": "Civic and cultural community space of the Belarusian diaspora in Lviv. Center assisting Belarusian relocants and volunteers, hosting Belarusian language courses, cultural events, and art exhibitions."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Lviv_Matejka_street.jpg/960px-Lviv_Matejka_street.jpg",
    "links": [
        {"title": "Будзьма: Курсы беларускай мовы ў Львове", "url": "https://budzma.org/news/kursy-belaruskay-movy.html"},
        {"title": "Беларусы ў Львове — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Беларусы_ў_Львове"}
    ],
    "tags": ["Львоў", "Украіна", "дыяспара", "Дом Вольнай Беларусі", "курсы", "culture"],
    "unverifiedCoordinates": True
})

upsert_place({
    "id": "lviv-beloruska-street",
    "title": {
        "by": "Вуліца Беларуская ў Львове",
        "ru": "Улица Белорусская во Львове",
        "en": "Biloruska Street in Lviv"
    },
    "category": "culture",
    "country": {"by": "Украіна", "ru": "Украина", "en": "Ukraine"},
    "city": {"by": "Львоў", "ru": "Львов", "en": "Lviv"},
    "coordinates": [49.8667, 24.0167],
    "description": {
        "by": "Вуліца ў Шаўчэнкаўскім раёне Львова (мясцовасць Галаско). Названая ў гонар Беларусі, адлюстроўвае гістарычныя і культурныя сувязі паміж Львовам і Беларуссю.",
        "ru": "Улица в Шевченковском районе Львова (микрорайон Голоско). Названа в честь Беларуси.",
        "en": "Street in the Shevchenkivskyi district of Lviv named in honor of Belarus, testifying to historic ties between Lviv and Belarus."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Lviv_panorama.jpg/960px-Lviv_panorama.jpg",
    "links": [
        {"title": "Вулиця Білоруська (Львів) — Вікіпедыя", "url": "https://uk.wikipedia.org/wiki/Вулиця_Білоруська_(Львів)"}
    ],
    "tags": ["Львоў", "Украіна", "вуліца", "Беларуская", "culture"],
    "unverifiedCoordinates": False
})

# ==========================================
# 5. BERLIN & POTSDAM
# ==========================================

upsert_place({
    "id": "berlin-bnr-diplomatic-mission",
    "title": {
        "by": "Дыпламатычная місія БНР у Берліне (Motzstraße 21)",
        "ru": "Дипломатическая миссия БНР в Берлине (Motzstraße 21)",
        "en": "BNR Diplomatic Mission in Berlin (Motzstraße 21)"
    },
    "category": "historical",
    "country": {"by": "Германія", "ru": "Германия", "en": "Germany"},
    "city": {"by": "Берлін", "ru": "Берлин", "en": "Berlin"},
    "coordinates": [52.4988, 13.3486],
    "description": {
        "by": "Будынак на Motzstraße 21 у раёне Шонэберг, дзе ў 1919–1925 гг. размяшчалася Надзвычайная дыпламатычная місія Беларускай Народнай Рэспублікі ў Германіі. Кіраўнікамі місіі былі Аркадзь Смоліч, Лявон Заяц, Андрэй Бароўскі. Тут выдаваліся беларускія пашпарты, рэгістраваліся грамадзяне БНР і друкаваліся інфармацыйныя матэрыялы пра Беларусь для нямецкага і еўрапейскага друку.",
        "ru": "Здание на Мотцштрассе 21 в Берлине, где в 1919–1925 годах действовала Чрезвычайная дипломатическая миссия Белорусской Народной Республики. Здесь выдавались паспорта БНР и велась работа по международному признанию Беларуси.",
        "en": "Building on Motzstraße 21 in Berlin-Schöneberg that housed the Extraordinary Diplomatic Mission of the Belarusian Democratic Republic (BNR) from 1919 to 1925, led by Arkadz Smalich and Andrei Barouski. Issued BNR passports and lobbied for international recognition of Belarus."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Motzstra%C3%9Fe_21_Berlin.jpg/960px-Motzstra%C3%9Fe_21_Berlin.jpg",
    "links": [
        {"title": "Новы Час: Беларускі Берлін", "url": "https://novychas.online/kultura/belaruski-berlin-mescy-jakija-dyhajuc-naszaj-hi"},
        {"title": "Дыпламатычныя прадстаўніцтвы БНР — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Дыпламатычныя_прадстаўніцтвы_БНР"}
    ],
    "tags": ["Берлін", "Германія", "БНР", "дыпламатыя", "пашпарт БНР", "historical"],
    "unverifiedCoordinates": False
})

upsert_place({
    "id": "berlin-bnr-press-bureau",
    "title": {
        "by": "Беларускае прэс-бюро ў Берліне (Bundesallee 209)",
        "ru": "Белорусское пресс-бюро в Берлине (Bundesallee 209)",
        "en": "Belarusian Press Bureau in Berlin (Bundesallee 209)"
    },
    "category": "historical",
    "country": {"by": "Германія", "ru": "Германия", "en": "Germany"},
    "city": {"by": "Берлін", "ru": "Берлин", "en": "Berlin"},
    "coordinates": [52.4975, 13.3308],
    "description": {
        "by": "Будынак на Bundesallee 209 (колішняя Kaiserallee), дзе ў 1920-я гг. працавала Беларускае прэс-бюро, заснаванае дзеячамі БНР. Бюро выдавала інфармацыйныя бюлетэні на нямецкай мове, інфармуючы грамадскасць краін Заходняй Еўропы аб барацьбе Беларусі за самавызначэнне і супрацьстаяла савецкай і польскай прапагандзе.",
        "ru": "Здание на Бундесаллее 209 (бывшая Кайзераллее), где в 1920-е годы действовало Белорусское пресс-бюро БНР, выпускавшее бюллетени на немецком языке.",
        "en": "Building on Bundesallee 209 (formerly Kaiserallee) which housed the Belarusian Press Bureau in the 1920s, publishing German-language bulletins to inform the Western European public about Belarus's fight for statehood."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Bundesallee_209_Berlin.jpg/960px-Bundesallee_209_Berlin.jpg",
    "links": [
        {"title": "Новы Час: Беларускі Берлін", "url": "https://novychas.online/kultura/belaruski-berlin-mescy-jakija-dyhajuc-naszaj-hi"}
    ],
    "tags": ["Берлін", "Германія", "прэс-бюро", "БНР", "historical"],
    "unverifiedCoordinates": False
})

upsert_place({
    "id": "berlin-der-sturm-chagall",
    "title": {
        "by": "Галерэя «Der Sturm» — першая нямецкая выстава Марка Шагала (1914)",
        "ru": "Галерея «Der Sturm» — первая немецкая выставка Марка Шагала (1914)",
        "en": "Der Sturm Gallery in Berlin — Marc Chagall's Historic 1914 Exhibition"
    },
    "category": "culture",
    "country": {"by": "Германія", "ru": "Германия", "en": "Germany"},
    "city": {"by": "Берлін", "ru": "Берлин", "en": "Berlin"},
    "coordinates": [52.5028, 13.3644],
    "description": {
        "by": "Гістарычнае месца на Potsdamer Straße 134, дзе размяшчалася славутая галерэя і часопіс «Der Sturm» Херварта Вальдэна. У чэрвені 1914 года тут адкрылася першая вялікая персанальная выстава ўраджэнца Віцебска Марка Шагала, на якой экспанавалася больш за 200 карцін і малюнкаў. Выстава стала сусветным трыумфам Шагала і зацвердзіла яго статус лідара еўрапейскага авангарду.",
        "ru": "Историческое место на Потсдамер-штрассе 134, где располагалась легендарная авангардная галерея «Der Sturm». В июне 1914 года здесь прошла первая персональная выставка Марка Шагала (более 200 работ), принесшая уроженцу Витебска европейскую славу.",
        "en": "Historic location of Herwarth Walden's seminal avant-garde gallery 'Der Sturm' on Potsdamer Straße 134. In June 1914, Vitebsk-born master Marc Chagall held his breakthrough solo exhibition here featuring over 200 works, propelling him to international renown."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Potsdamer_Strasse_134_Berlin.jpg/960px-Potsdamer_Strasse_134_Berlin.jpg",
    "links": [
        {"title": "Марк Шагал — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Марк_Шагал"},
        {"title": "Новы Час: Беларускі Берлін", "url": "https://novychas.online/kultura/belaruski-berlin-mescy-jakija-dyhajuc-naszaj-hi"}
    ],
    "tags": ["Берлін", "Германія", "Шагал", "Der Sturm", "авангард", "culture"],
    "personId": "marc-chagall",
    "personIds": ["marc-chagall"],
    "unverifiedCoordinates": False
})

upsert_place({
    "id": "berlin-tacheles-ales-rodzin",
    "title": {
        "by": "Арт-цэнтр «Тахелес» і студыя Алеся Родзіна ў Берліне",
        "ru": "Арт-центр «Тахелес» и мастерская Алеся Родина в Берлине",
        "en": "Kunsthaus Tacheles & Ales Rodzin Studio in Berlin"
    },
    "category": "culture",
    "country": {"by": "Германія", "ru": "Германия", "en": "Germany"},
    "city": {"by": "Берлін", "ru": "Берлин", "en": "Berlin"},
    "coordinates": [52.5256, 13.3892],
    "description": {
        "by": "Культавы берлінскі дом мастацтваў і сквот на Oranienburger Straße 54–56. З 2001 па 2014 год тут дзейнічала легендарная майстэрня і галерэя выбітнага беларускага авангардыста Алеся Родзіна. Родзін ствараў тут манументальныя палотны цыкла «Глабальнае пацяпленне» і арганізоўваў фестываль «Дах», зрабіўшы «Тахелес» важным мастом паміж беларускім і еўрапейскім сучасным мастацтвам.",
        "ru": "Культовый сквот и арт-центр Kunsthaus Tacheles в центре Берлина. С 2001 года здесь находилась постоянная мастерская и экспозиция белорусского художника Алеся Родина, проводившего фестивали белорусского экспериментального искусства «Дах».",
        "en": "Iconic cultural squatted art center Kunsthaus Tacheles on Oranienburger Straße 54–56. For over a decade from 2001, Belarusian master Ales Rodzin maintained his permanent studio and monumental exhibition here, founding the avant-garde 'Dakh' festival and creating cultural ties between Belarus and Berlin."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Kunsthaus_Tacheles_2008.jpg/960px-Kunsthaus_Tacheles_2008.jpg",
    "links": [
        {"title": "Кунстхаўс Тахелес — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Кунстхаўс_Тахелес"},
        {"title": "Алесь Родзін — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Алесь_Радзін"}
    ],
    "tags": ["Берлін", "Германія", "Тахелес", "Родзін", "авангард", "Дах", "culture"],
    "personId": "ales-rodzin",
    "personIds": ["ales-rodzin"],
    "unverifiedCoordinates": False
})

upsert_place({
    "id": "potsdam-das-minsk-kunsthaus",
    "title": {
        "by": "Музей сучаснага мастацтва «Das Minsk» у Патсдаме",
        "ru": "Музей современного искусства «Das Minsk» в Потсдаме",
        "en": "DAS MINSK Kunsthaus in Potsdam (Former Restaurant Minsk)"
    },
    "category": "culture",
    "country": {"by": "Германія", "ru": "Германия", "en": "Germany"},
    "city": {"by": "Патсдам", "ru": "Потсдам", "en": "Potsdam"},
    "coordinates": [52.3888, 13.0645],
    "description": {
        "by": "Будынак на Max-Planck-Straße 1 у Патсдаме, пабудаваны ў 1970-я гг. у стылі мадэрнізму як рэстаран «Мінск» у знак пабрацімства паміж Патсдамам і Мінскам (у Мінску адначасова быў адкрыты рэстаран «Патсдам»). Пасля рэканструкцыі мецэнатам Хаса Платнерам у 2022 г. адкрыты як музей сучаснага мастацтва «DAS MINSK Kunsthaus», захаваўшы гістарычную назву і спадчыну мадэрнізму.",
        "ru": "Здание на Макс-Планк-штрассе 1 в Потсдаме, построенное в 1970-х как ресторан «Минск» в знак побратимства Потсдама и Минска. В 2022 году бережно отреставрировано и открыто как музей современного искусства DAS MINSK Kunsthaus.",
        "en": "Striking modernist pavilion on Max-Planck-Straße 1 in Potsdam, built in the 1970s as Restaurant 'Minsk' celebrating the partnership between twin cities Potsdam and Minsk. Lovingly revitalized in 2022 as 'DAS MINSK Kunsthaus' contemporary art museum, preserving its historic Belarusian name and architectural heritage."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Restaurant_Minsk_Potsdam_2022.jpg/960px-Restaurant_Minsk_Potsdam_2022.jpg",
    "links": [
        {"title": "DAS MINSK Kunsthaus", "url": "https://dasminsk.de/"},
        {"title": "Новы Час: Беларускі Берлін", "url": "https://novychas.online/kultura/belaruski-berlin-mescy-jakija-dyhajuc-naszaj-hi"}
    ],
    "tags": ["Патсдам", "Германія", "Дас Мінск", "рэстаран Мінск", "мастацтва", "culture"],
    "unverifiedCoordinates": False
})

# ==========================================
# 6. MOSCOW KREMLIN (LAZKOVICHY CROSS)
# ==========================================

upsert_place({
    "id": "moscow-kremlin-lazkovichy-cross",
    "title": {
        "by": "Лазковіцкі крыж князя Алехны Глазыны (1494–1495) у Маскоўскім Крамлі",
        "ru": "Лазковичский крест князя Алехны Глазыны (1494–1495) в Московском Кремле",
        "en": "Lazkovichy Cross of Prince Alekhna Hlazyna in Moscow Kremlin Museums"
    },
    "category": "culture",
    "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
    "city": {"by": "Масква", "ru": "Москва", "en": "Moscow"},
    "coordinates": [55.7496, 37.6167],
    "description": {
        "by": "Унікальная нацыянальная святыня беларускага сакральнага мастацтва канца XV ст., створаная паводле ўзору крыжа Еўфрасінні Полацкай (памеры 50 × 21 см) на замову смаленскага акольнічага князя Алехны Глазыны для царквы ў маёнтку Лазковічы. Змяшчае мошчы 25 хрысціянскіх святых і часцінку Жыватворнага Крыжа. Быў сямейнай рэліквіяй родаў Сапегаў, Хадкевічаў, Пацаў, захоўваўся ў Жыровіцкім і Віленскім Свята-Духавым манастырах. У 1915 г. эвакуяваны ў Маскву, адкуль не вернуты; з 1926 г. знаходзіцца ў сховішчах Музеяў Маскоўскага Крамля (інв. № ДК-1025).",
        "ru": "Уникальный напрестольный крест-реликварий конца XV века, созданный по образцу креста Евфросинии Полоцкой по заказу смоленского окольничего князя Алехны Глазыны (1494–1495 гг.). Хранил мощи 25 святых и частицу Древа Животворящего Креста. Святыня Жировичского и Виленского монастырей, вывезенная в 1915 году в Москву и хранящаяся в фондах Музеев Московского Кремля.",
        "en": "Exquisite 15th-century masterpiece of Belarusian sacral art (50 × 21 cm), crafted as a twin to St. Euphrosyne's Cross for Smolensk Prince Alekhna Hlazyna. Reliquary holding relics of 25 saints and a fragment of the True Cross. Long preserved at Zhirovichi and Vilna Holy Spirit Monasteries, evacuated to Moscow during WWI in 1915 and now held in the Moscow Kremlin Museums."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Lazkovichy_cross_Trutnev.jpg/960px-Lazkovichy_cross_Trutnev.jpg",
    "links": [
        {"title": "Наша Ніва: У Маскоўскім Крамлі знойдзены Лазковіцкі крыж", "url": "https://nashaniva.com/400340"}
    ],
    "tags": ["Масква", "Крэмль", "Лазковіцкі крыж", "Глазына", "Сапегі", "Жыровічы", "скарбы", "culture"],
    "unverifiedCoordinates": False
})

# ==========================================
# 7. SWEDEN (VISBY, STOCKHOLM, UPPSALA)
# ==========================================

upsert_place({
    "id": "visby-baltic-centre-writers-bcwt",
    "title": {
        "by": "Балтыйскі цэнтр пісьменнікаў і перакладчыкаў (BCWT) у Вісбю",
        "ru": "Балтийский центр писателей и переводчиков (BCWT) в Висбю",
        "en": "Baltic Centre for Writers and Translators (BCWT) in Visby"
    },
    "category": "culture",
    "country": {"by": "Швецыя", "ru": "Швеция", "en": "Sweden"},
    "city": {"by": "Вісбю", "ru": "Висбю", "en": "Visby"},
    "coordinates": [57.6413, 18.2928],
    "description": {
        "by": "Міжнародны пісьменніцкі дом на востраве Готланд (Uddens gränd 3, Вісбю), заснаваны ў 1993 годзе. Стаў адным з галоўных еўрапейскіх прыстанкаў і творчых рэзідэнцый для беларускіх літаратараў. Тут працавалі і стваралі новыя кнігі класік беларускай літаратуры Васіль Быкаў, Уладзімір Арлоў, Алесь Разанаў, Андрэй Хадановіч, Марына Шода і іншыя выбітныя аўтары.",
        "ru": "Международный дом писателей на шведском острове Готланд (Uddens gränd 3, Висбю). Стал важнейшим европейским центром творческих резиденций для белорусских литераторов. Здесь жили и работали Василь Быков, Владимир Орлов, Алесь Рязанов, Андрей Хаданович и другие авторы.",
        "en": "International residential center for writers and translators on Gotland (Uddens gränd 3, Visby). Celebrated sanctuary and residency hub for Belarusian literature, where Vasil Bykau, Uladzimir Arlou, Ales Razanau, and Andrei Khadanovich lived and created significant works."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Visby_Uddens_gr%C3%A4nd_3.jpg/800px-Visby_Uddens_gr%C3%A4nd_3.jpg",
    "links": [
        {"title": "Baltic Centre for Writers and Translators", "url": "https://www.bcwt.org/"},
        {"title": "Беларусы Швецыі — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Беларусы_Швецыі"}
    ],
    "tags": ["Швецыя", "Вісбю", "Готланд", "Быкаў", "Арлоў", "рэзідэнцыя", "літаратура", "culture"],
    "personId": "vasil-bykau",
    "personIds": ["vasil-bykau", "uladzimir-arlou"],
    "unverifiedCoordinates": False
})

upsert_place({
    "id": "stockholm-sveriges-belarusier-razam",
    "title": {
        "by": "Згуртаванне беларусаў у Швецыі «Разам» і плошча Сергельсторг",
        "ru": "Объединение белорусов в Швеции «Разам» и площадь Сергельсторг",
        "en": "Sveriges Belarusier \"Razam\" & Sergels Torg in Stockholm"
    },
    "category": "culture",
    "country": {"by": "Швецыя", "ru": "Швеция", "en": "Sweden"},
    "city": {"by": "Стакгольм", "ru": "Стокгольм", "en": "Stockholm"},
    "coordinates": [59.3326, 18.0649],
    "description": {
        "by": "Цэнтр грамадскага і культурнага жыцця беларусаў Швецыі. Згуртаванне «Разам» (Sveriges Belarusier), створанае прадстаўнікамі дыяспары, ладзіць культурныя праекты, курсы беларускай мовы і Дні беларускай культуры. Цэнтральная плошча Стакгольма — Сергельсторг (Sergels torg) — стала традыцыйным месцам акцый салідарнасці беларускай супольнасці.",
        "ru": "Центр общественной и культурной жизни белорусов Швеции. Объединение «Разам» организует культурные события, курсы языка и дни культуры. Площадь Сергельсторг в центре Стокгольма — традиционное место акций солидарности диаспоры.",
        "en": "Hub of civic and cultural life of the Belarusian diaspora in Sweden. The Sveriges Belarusier 'Razam' organization hosts cultural festivals, educational initiatives, and language courses, with central Sergels Torg square serving as a landmark site of community solidarity."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Sergels_torg_Stockholm_2011.jpg/960px-Sergels_torg_Stockholm_2011.jpg",
    "links": [
        {"title": "Sveriges Belarusier «Разам»", "url": "https://www.sverigesbelarusier.eu/"},
        {"title": "Беларусы Швецыі — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Беларусы_Швецыі"}
    ],
    "tags": ["Швецыя", "Стакгольм", "дыяспара", "Разам", "Сергельсторг", "culture"],
    "unverifiedCoordinates": False
})

upsert_place({
    "id": "uppsala-carolina-rediviva-belarustreasures",
    "title": {
        "by": "Бібліятэка Carolina Rediviva Упсальскага ўніверсітэта (беларускія зборы)",
        "ru": "Библиотека Carolina Rediviva Уппсальского университета (белорусские коллекции)",
        "en": "Carolina Rediviva Library at Uppsala University (GDL & Belarusian Collections)"
    },
    "category": "culture",
    "country": {"by": "Швецыя", "ru": "Швеция", "en": "Sweden"},
    "city": {"by": "Упсала", "ru": "Уппсала", "en": "Uppsala"},
    "coordinates": [59.8550, 17.6310],
    "description": {
        "by": "Галоўная бібліятэка найстарэйшага ўніверсітэта Скандынавіі. Тут захоўваюцца бясцэнныя помнікі кніжнай і картаграфічнай спадчыны ВКЛ, вывезеныя ў Швецыю ў час Паўночных войнаў: выданні полацкіх і віленскіх друкарняў, арыгінальная насценная карта ВКЛ Мікалая Радзівіла Сіроткі 1613 г., архіўныя матэрыялы Сапегаў і Радзівілаў. Універсітэт з'яўляецца цэнтрам шведскай беларусістыкі.",
        "ru": "Библиотека Уппсальского университета, хранящая богатейшую коллекцию раритетов ВКЛ и Беларуси: книги виленских и полоцких типографий, карту ВКЛ Радзивилла 1613 года, архивы магнатов. Центр шведской белорусистики.",
        "en": "Main library of Scandinavia's oldest university. Houses priceless historic treasures of the Grand Duchy of Lithuania taken to Sweden during 17th–18th-century wars, including rare editions from Polotsk and Vilna, Tomasz Makowski's 1613 Radziwill Map of the GDL, and documents of the Sapieha and Radziwill families."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Carolina_Rediviva_Uppsala.jpg/960px-Carolina_Rediviva_Uppsala.jpg",
    "links": [
        {"title": "Carolina Rediviva — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Караліна_Рэдывіва"},
        {"title": "Шведская беларусістыка", "url": "https://belhistory.com/shvedskaja-belarusistyka.html"}
    ],
    "tags": ["Швецыя", "Упсала", "ВКЛ", "кнігі", "Радзівілаўская карта", "беларусістыка", "culture"],
    "unverifiedCoordinates": False
})

# ==========================================
# 8. SLOVAKIA (JÁN NÁLEPKA)
# ==========================================

upsert_place({
    "id": "spisska-nova-ves-jan-nalepka-monument",
    "title": {
        "by": "Помнік капітану Яну Налепку («Рэпкіну») у Спішска-Нова-Вес",
        "ru": "Памятник капитану Яну Налепке («Репкину») в Спишска-Нова-Вес",
        "en": "Monument to Captain Ján Nálepka (\"Repkin\") in Spišská Nová Ves"
    },
    "category": "monument",
    "country": {"by": "Славакія", "ru": "Словакия", "en": "Slovakia"},
    "city": {"by": "Спішска-Нова-Вес", "ru": "Спишска-Нова-Вес", "en": "Spišská Nová Ves"},
    "coordinates": [48.9439, 20.5678],
    "description": {
        "by": "Манументальны помнік славацкаму герою-антыфашысту капітану Яну Налепку на Ратушнай плошчы. У 1942–1943 гг. Налепка служыў начальнікам штаба 101-га славацкага палка ў беларускім Ельску, перайшоў на бок партызан, стварыў чэхаславацкі партызанскі атрад у беларускіх лясах і разам з беларускімі байцамі граміў фашыстаў на Палессі. Адзіны славак — Герой Савецкага Саюза.",
        "ru": "Монументальный памятник словацкому герою Яну Налепке на Ратушной площади. В 1942–1943 гг. Налепка служил в белорусском Ельске, перешел на сторону партизан и создал чехословацкий партизанский отряд, сражавшийся в лесах Беларуси. Единственный словак — Герой Советского Союза.",
        "en": "Monument to Slovak anti-fascist commander Captain Ján Nálepka on Town Hall Square. While stationed in Yelsk (Belarus) in 1942–1943, he defected to the partisans and founded the Czechoslovak partisan detachment fighting alongside Belarusian resistance forces in Polesia."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/J%C3%A1n_N%C3%A1lepka.jpg/330px-J%C3%A1n_N%C3%A1lepka.jpg",
    "links": [
        {"title": "Ян Налепка — Вікіпедыя", "url": "https://be-tarask.wikipedia.org/wiki/Ян_Налепка"}
    ],
    "tags": ["Славакія", "Налепка", "Ельск", "партызаны", "помнік", "monument"],
    "personId": "jan-nalepka",
    "personIds": ["jan-nalepka"],
    "unverifiedCoordinates": False
})

# ==========================================
# 9. CZAPSKI HERITAGE (KRAKÓW & MAISONS-LAFFITTE)
# ==========================================

upsert_place({
    "id": "krakow-muzeum-emeryka-hutten-czapskiego",
    "title": {
        "by": "Музей імя Эмерыка Гутэн-Чапскага ў Кракаве (скарбы Станькава)",
        "ru": "Музей имени Эмерика Гуттен-Чапского в Кракове (сокровища Станьково)",
        "en": "Emeryk Hutten-Czapski Museum & Palace in Kraków"
    },
    "category": "culture",
    "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
    "city": {"by": "Кракаў", "ru": "Краков", "en": "Kraków"},
    "coordinates": [50.0594, 19.9308],
    "description": {
        "by": "Палац і музей на вуліцы Пілсудскага, 12 (філіял Нацыянальнага музея ў Кракаве). Пабудаваны Эмерыкам Гутэн-Чапскім (1828–1896) спецыяльна для размяшчэння грандыёзных збораў манет, медалёў і рарытэтаў ВКЛ і Беларусі, перавезеных з радавога маёнтка Станькава пад Мінскам. На франтоне высечаны дэвіз «Monumentis Patriae naufragio ereptis» («Святыням Айчыны, уратаваным ад караблекрушэння»).",
        "ru": "Дворец и музей на ул. Пилсудского, 12 (филиал Национального музея в Кракове). Основан графом Эмериком Гуттен-Чапским для демонстрации колоссальной коллекции нумизматики и редкостей ВКЛ, перевезенных из белорусского имения Станьково. Девиз на фасаде: «Памятникам Отечества, спасенным от кораблекрушения».",
        "en": "Palace and museum on Piłsudskiego St 12 (branch of the National Museum in Kraków). Founded by Count Emeryk Hutten-Czapski to house his immense numismatic collections and rare manuscripts of the GDL and Belarus brought from his Stankava estate near Minsk. The facade bears the famous Latin motto 'Monumentis Patriae naufragio ereptis'."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Krakow_Palac_Czapskich.jpg/960px-Krakow_Palac_Czapskich.jpg",
    "links": [
        {"title": "Muzeum im. Emeryka Hutten-Czapskiego", "url": "https://mnk.pl/oddzial/muzeum-im-emeryka-hutten-czapskiego"},
        {"title": "Эмерык Гутэн-Чапскі — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Эмерык_Гутэн-Чапскі"}
    ],
    "tags": ["Кракаў", "Польшча", "Чапскія", "Станькава", "нумізматыка", "ВКЛ", "палац", "culture"],
    "personId": "emeryk-hutten-czapski",
    "personIds": ["emeryk-hutten-czapski"],
    "unverifiedCoordinates": False
})

upsert_place({
    "id": "krakow-pawilon-jozefa-czapskiego",
    "title": {
        "by": "Павільён Юзафа Чапскага ў Кракаве (маладосць у Прылуках)",
        "ru": "Павильон Юзефа Чапского в Кракове (молодость в Прилуках)",
        "en": "Józef Czapski Pavilion in Kraków"
    },
    "category": "culture",
    "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
    "city": {"by": "Кракаў", "ru": "Краков", "en": "Kraków"},
    "coordinates": [50.0592, 19.9305],
    "description": {
        "by": "Сучасны музейны павільён у садзе палаца Чапскіх (вул. Пілсудскага, 12), адкрыты ў 2016 г. Прысвечаны ўнуку Эмерыка — выбітнаму мастаку і пісьменніку Юзафу Чапскаму (1896–1993), які правёў дзяцінства і юнацтва ў маёнтку Прылукі пад Мінскам. У павільёне прадстаўлены карціны Чапскага, яго мастацкія дзённікі і дакладная рэканструкцыя яго пакоя ў Мэзон-Лафіт пад Парыжам.",
        "ru": "Музейный павильон в саду дворца Чапских в Кракове, открытый в 2016 году. Посвящен внуку Эмерика — художнику и писателю Юзефу Чапскому, чьи детство и юность прошли в Прилуках под Минском. Включает его картины, дневники и реконструкцию его комнаты в Мезон-Лаффит.",
        "en": "Contemporary museum pavilion in the gardens of the Czapski Palace (Piłsudskiego St 12), opened in 2016. Dedicated to painter and writer Józef Czapski (1896–1993), who grew up at the family estate in Pryluki near Minsk. Houses his paintings, notebooks, and an exact replica of his Paris room in Maisons-Laffitte."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Pawilon_Jozefa_Czapskiego_Krakow.jpg/960px-Pawilon_Jozefa_Czapskiego_Krakow.jpg",
    "links": [
        {"title": "Павільён Юзафа Чапскага — MNK", "url": "https://mnk.pl/oddzial/pawilon-jozefa-czapskiego"},
        {"title": "Юзаф Чапскі — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Юзаф_Чапскі"}
    ],
    "tags": ["Кракаў", "Польшча", "Юзаф Чапскі", "Прылукі", "жывапіс", "culture"],
    "personId": "jozef-czapski",
    "personIds": ["jozef-czapski"],
    "unverifiedCoordinates": False
})

upsert_place({
    "id": "maisons-laffitte-kultura-czapski",
    "title": {
        "by": "Сядзіба парыжскай «Культуры» і пакой Юзафа Чапскага ў Мэзон-Лафіт",
        "ru": "Дом парижской «Культуры» и комната Юзефа Чапского в Мезон-Лаффит",
        "en": "Maisons-Laffitte \"Kultura\" Headquarters & Józef Czapski Studio"
    },
    "category": "culture",
    "country": {"by": "Францыя", "ru": "Франция", "en": "France"},
    "city": {"by": "Мэзон-Лафіт", "ru": "Мезон-Лаффит", "en": "Maisons-Laffitte"},
    "coordinates": [48.9467, 2.1408],
    "description": {
        "by": "Гістарычны дом на 91 Avenue de Poissy пад Парыжам, дзе з 1954 г. размяшчалася штаб-кватэра Літаратурнага інстытута і легендарнага часопіса «Kultura» Ежы Гедройца. Тут амаль 40 гадоў жыў, пісаў карціны і ствараў свае кнігі Юзаф Чапскі (выхадзец з беларускіх Прылук), які фармаваў еўрапейскі дыялог пра лёс усходнееўрапейскіх нацый.",
        "ru": "Исторический особняк на 91 Avenue de Poissy близ Парижа — штаб-квартира Литературного института и журнала «Kultura» Ежи Гедройца. Здесь почти 40 лет жил и творил Юзеф Чапский, уроженец белорусских Прилук.",
        "en": "Historic residence at 91 Avenue de Poissy near Paris, headquarters of the Literary Institute and dissident journal 'Kultura' led by Jerzy Giedroyc. Belarusian-raised intellectual Józef Czapski lived and painted here from 1954 until his death in 1993, shaping Eastern European cultural dialogue."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/J%C3%B3zef_Czapski_1932.jpg/330px-J%C3%B3zef_Czapski_1932.jpg",
    "links": [
        {"title": "Юзаф Чапскі — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Юзаф_Чапскі"},
        {"title": "Szlak Nadziei: Józef Czapski", "url": "https://szlakinadziei.ipn.gov.pl/sne/exposures/people/9942,Jozef-Czapski-18961993.html"}
    ],
    "tags": ["Францыя", "Парыж", "Мэзон-Лафіт", "Культура", "Юзаф Чапскі", "culture"],
    "personId": "jozef-czapski",
    "personIds": ["jozef-czapski"],
    "unverifiedCoordinates": False
})

# ==========================================
# 10. SAVE FILES
# ==========================================

with open('data/places.json', 'w', encoding='utf-8') as f:
    json.dump(places, f, ensure_ascii=False, indent=2)
with open('data/places.js', 'w', encoding='utf-8') as f:
    f.write('// Albaruthenica Places Dataset\nwindow.INITIAL_PLACES = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

with open('data/persons.json', 'w', encoding='utf-8') as f:
    json.dump(persons, f, ensure_ascii=False, indent=2)
with open('data/persons.js', 'w', encoding='utf-8') as f:
    f.write('// Albaruthenica Persons Dataset\nwindow.INITIAL_PERSONS = ' + json.dumps(persons, ensure_ascii=False, indent=2) + ';\n')

print(f"Dataset successfully updated! Total places: {len(places)}, Total persons: {len(persons)}")
