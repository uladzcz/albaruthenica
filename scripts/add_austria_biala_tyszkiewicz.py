# -*- coding: utf-8 -*-
"""
Add new objects from user requests:
1. Biala Podlaska Radziwill Palace (Бяла Радзівілаўская)
2. Vienna Hofburg KHM - Imperial Armoury: Parade Armour of Mikolaj Radziwill "the Black" by Kunz Lochner
3. Nieborow Palace - Hall of the Nesvizh Armoury
4. Uzutrakis (Zatrachcha) Tyszkiewicz Palace on Lake Galve near Trakai
5. Lentvaris (Landtvarava) Tyszkiewicz Palace
6. Vilnius - St. Johns Church & Basilian Gate (Johann Christoph Glaubitz masterpieces)
7. Mark key iconic heritage locations with `mustSee: true`
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

# 1. PERSON: Johann Christoph Glaubitz
upsert_person({
    "id": "johann-christoph-glaubitz",
    "name": {
        "by": "Ян Крыштаф Глаўбіц",
        "ru": "Иоганн Кристоф Глаубиц",
        "en": "Johann Christoph Glaubitz"
    },
    "dates": "~1700 — 1767",
    "role": {
        "by": "Архітэктар, стваральнік непаўторнага стылю «віленскага барока» ў Беларусі і Літве",
        "ru": "Архитектор, создатель уникального стиля «виленского барокко» в Беларуси и Литве",
        "en": "Architect, founding master of the 'Vilnius Baroque' style in Belarus and Lithuania"
    },
    "bio": {
        "by": "Найвыдатнейшы архітэктар позняга барока і ракако ў Вялікім Княстве Літоўскім. Стваральнік знакамітай школы «віленскага барока», якая вызначаецца ажурнай вертыкальнасцю вежаў і пластычнасцю ліній. У Беларусі аднавіў і перабудаваў у барочным стылі Сафійскі сабор у Полацку, стварыў касцёл і базыльянскі кляштар у Беразвеччы (пад Глыбокім). У Вільні стварыў грандыёзны галоўны фасад касцёла Святых Янаў, касцёл Святой Кацярыны і знакамітую барочную Базыльянскую браму кляштара Святой Тройцы.",
        "ru": "Крупнейший зодчий эпохи барокко в ВКЛ, создатель школы «виленского барокко». В Беларуси перестроил Софийский собор в Полоцке, костёл в Березвечье под Глубоким. В Вильнюсе создал фасад костёла Святых Иоаннов, костёл Святой Екатерины и триумфальные Базилианские ворота монастыря Святой Троицы.",
        "en": "Preeminent Late Baroque architect in the Grand Duchy of Lithuania, father of the 'Vilnius Baroque' school. In Belarus, rebuilt Saint Sophia Cathedral in Polotsk and Berezvechye Monastery. In Vilnius, designed the soaring facade and altar of the Church of St. Johns, St. Catherine's Church, and the ornate Basilian Gate."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Vilnius_St_Johns_Church_facade.jpg/960px-Vilnius_St_Johns_Church_facade.jpg",
    "wiki": "https://be.wikipedia.org/wiki/Ян_Крыштаф_Глаўбіц",
    "placeIds": ["vilnia-glaubitz-st-johns"]
})

# 2. PLACE: Biala Podlaska Radziwill Palace Complex
upsert_place({
    "id": "biala-podlaska-radziwill-palace",
    "title": {
        "by": "Палацава-паркавы комплекс Радзівілаў у Бялай Падляскай (Бяла Радзівілаўская)",
        "ru": "Дворцово-парковый комплекс Радзивиллов в Бяла-Подляске (Бяла Радзивилловская)",
        "en": "Radziwill Palace & Castle Complex in Biała Podlaska"
    },
    "category": "historical",
    "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
    "city": {"by": "Бяла-Падляска", "ru": "Бяла-Подляска", "en": "Biała Podlaska"},
    "coordinates": [52.0336, 23.1256],
    "description": {
        "by": "Адна з трох галоўных і найбагацейшых рэзідэнцый князёў Радзівілаў нясвіжска-алыцкай лініі (разам з Нясвіжам і Олыкай). Горад належаў Радзівілам з 1569 па 1831 год і насіў афіцыйную назву Бяла Радзівілаўская (Biała Radziwiłłowska). Грандыёзны барочны замак і палац будавалі Аляксандр Людвік Радзівіл, Міхал Казімір Радзівіл «Рыбанька», Кацярына з Сабескіх і Ганна з Сангушкаў. Тут дзейнічалі Бяльская акадэмія, друкарня, мануфактуры і збройныя майстэрні. Захаваліся ўязная вежа-брама, бастыёны, замкавая капліца і флігелі (цяпер Музей Паўднёвага Падляшша).",
        "ru": "Одна из главных резиденций несвижских Радзивиллов (наряду с Несвижем и Олыкой), принадлежавшая роду с 1569 по 1831 год. Город назывался «Бяла Радзивилловская». Монументальный барочный замок строили Александр Людвик, Михаил Казимир «Рыбонька», Екатерина Собеская. Сохранились замковая башня-ворота, валы, часовня и павильоны, где работает Музей Южного Подляшья.",
        "en": "One of the three principal residences of the Nesvizh Radziwill dynasty (alongside Nesvizh and Olyka), owned from 1569 to 1831 when the town was officially called Biała Radziwiłłowska. Built and expanded by Aleksander Ludwik, Michał Kazimierz 'Rybeńko', and Katarzyna Radziwiłłowa née Sobieska. The preserved gate tower, bastion fortifications, chapel, and pavilions now house the Museum of Southern Podlasie."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Biala_Podlaska_Brama_wjazdowa_Radziwillow.jpg/960px-Biala_Podlaska_Brama_wjazdowa_Radziwillow.jpg",
    "links": [
        {"title": "Zespół pałacowo-parkowy Radziwiłłów w Białej Podlaskiej — Wikipedia", "url": "https://pl.wikipedia.org/wiki/Zesp%C3%B3%C5%82_pa%C5%82acowo-parkowy_Radziwi%C5%82%C5%82%C3%B3w_w_Bia%C5%82ej_Podlaskiej"},
        {"title": "Музей Паўднёвага Падляшша", "url": "https://muzeumbiala.pl/"}
    ],
    "tags": ["Польшча", "Падляшша", "Бяла Радзівілаўская", "Радзівілы", "замак", "палац", "historical"],
    "personId": "radziwills",
    "personIds": ["radziwills"],
    "mustSee": True,
    "unverifiedCoordinates": False
})

# 3. PLACE: Vienna Hofburg - KHM Imperial Armoury (Radziwill Parade Armour)
upsert_place({
    "id": "vienna-hofburg-radziwill-armour",
    "title": {
        "by": "Парадны даспех Мікалая Радзівіла Чорнага ў Імператарскай збраёўні Вены (Хофбург)",
        "ru": "Парадный доспех Николая Радзивилла Чёрного в Императорской оружейной палате Вены (Хофбург)",
        "en": "Parade Armour of Mikołaj Radziwiłł \"the Black\" in the Imperial Armoury of Vienna (Hofburg)"
    },
    "category": "culture",
    "country": {"by": "Аўстрыя", "ru": "Австрия", "en": "Austria"},
    "city": {"by": "Вена", "ru": "Вена", "en": "Vienna"},
    "coordinates": [48.2054, 16.3656],
    "description": {
        "by": "У палацы Нойе-Бург імператарскага ансамбля Хофбург (Hofjagd- und Rüstkammer, філіял Музея гісторыі мастацтваў KHM) экспануецца сусветна вядомы шэдэўр рэнесанснага збройнага мастацтва — парадны рыцарскі даспех вялікага канцлера літоўскага і віленскага ваяводы князя Мікалая Радзівіла «Чорнага» (1515–1565). Створаны каля 1555 г. славутым нюрнбергскім майстрам Кунцам Лохнерам (Kunz Lochner), упрыгожаны вытанчанай залатой гравіроўкай, чорнай эмаллю і радзівілаўскімі сімваламі. Быў выкуплены імператарамі Габсбургамі і лічыцца адным з найпрыгажэйшых рыцарскіх даспехаў у свеце.",
        "ru": "В венском Хофбурге (Hofjagd- und Rüstkammer Музея истории искусств Вены) хранится признанный шедевр мирового оружейного искусства — парадный рыцарский доспех великого канцлера литовского князя Николая Радзивилла «Чёрного» (1515–1565). Создан около 1555 г. знаменитым мастером Кунцем Лохнером в Нюрнберге, украшен позолотой и черной эмалью.",
        "en": "Exhibited in the Neue Burg at the Hofburg Palace (Imperial Armoury / KHM Vienna), this is one of the most famous Renaissance garnitures in the world: the parade armour of Grand Chancellor of Lithuania Prince Mikołaj Radziwiłł 'the Black' (1515–1565). Crafted around 1555 by master Kunz Lochner in Nuremberg with lavish gilding, black enamel, and heraldic eagles."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Hofjagd-_und_R%C3%BCstkammer_Wien_Radziwill_armour.jpg/960px-Hofjagd-_und_R%C3%BCstkammer_Wien_Radziwill_armour.jpg",
    "links": [
        {"title": "KHM Hofjagd- und Rüstkammer Wien", "url": "https://www.khm.at/besuchen/sammlungen/hofjagd-und-ruestkammer/"},
        {"title": "Беларусы ў Аўстрыі — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Беларусы_ў_Аўстрыі"}
    ],
    "tags": ["Аўстрыя", "Вена", "Хофбург", "KHM", "Радзівіл Чорны", "даспехі", "скарбы", "culture"],
    "personId": "radziwills",
    "personIds": ["radziwills"],
    "mustSee": True,
    "unverifiedCoordinates": False
})

# 4. PLACE: Nieborow Palace - Hall of the Nesvizh Armoury
upsert_place({
    "id": "nieborow-nesvizh-armoury",
    "title": {
        "by": "Зала Нясвіжскай збраёўні ў палацы Радзівілаў у Нябораве",
        "ru": "Зал Несвижской оружейной палаты во дворце Радзивиллов в Неборове",
        "en": "The Nesvizh Armoury Hall in the Radziwiłł Palace at Nieborów"
    },
    "category": "culture",
    "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
    "city": {"by": "Нябораў", "ru": "Неборов", "en": "Nieborów"},
    "coordinates": [52.0664, 20.0694],
    "description": {
        "by": "На другім паверсе знакамітага палаца Радзівілаў у Нябораве (філіял Нацыянальнага музея ў Варшаве) знаходзіцца гістарычны пакой «Нясвіжская збраёўня» (Zbrojownia Nieświeska). Тут захоўваецца ўнікальная калекцыя вайсковых рэліквій і рыцарскіх даспехаў, вывезеных з арсенала Нясвіжскага замка: польскія і вялікалітоўскія гусарскія латы XVII ст., шлемы-шышакі, кальчугі, шаблі і штандары з гербамі «Трубы».",
        "ru": "На втором этаже дворца Радзивиллов в Неборове размещается исторический зал «Несвижская оружейная палата» (Zbrojownia Nieświeska). Здесь экспонируются рыцарские доспехи, гусарские латы XVII века, шлемы, сабли и штандарты, спасенные и вывезенные из арсенала Несвижского замка.",
        "en": "On the second floor of the Radziwiłł Palace in Nieborów (branch of the National Museum in Warsaw) is 'The Nesvizh Armoury' room. Houses rare historical armor, 17th-century winged hussar breastplates, helmets, and weaponry preserved from the legendary arsenal of Nesvizh Castle."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Palac_w_Nieborowie_2011.jpg/960px-Palac_w_Nieborowie_2011.jpg",
    "links": [
        {"title": "The Nesvizh Armoury in Nieborów Palace", "url": "https://www.nieborow.art.pl/en/visit/palace-tour/second-floor/the-nesvizh-armoury/"}
    ],
    "tags": ["Польшча", "Нябораў", "Радзівілы", "Нясвіжская збраёўня", "гусары", "culture"],
    "personId": "radziwills",
    "personIds": ["radziwills"],
    "mustSee": True,
    "unverifiedCoordinates": False
})

# 5. PLACE: Uzutrakis (Zatrachcha) Tyszkiewicz Palace
upsert_place({
    "id": "trakai-uzutrakis-tyszkiewicz-palace",
    "title": {
        "by": "Палац графаў Тышкевічаў ва Ужутракісе (Затраччы) на возеры Гальвэ",
        "ru": "Дворец графов Тышкевичей в Ужутракисе (Затрачье) на озере Гальве",
        "en": "Tyszkiewicz Palace in Užutrakis on Lake Galvė (Trakai)"
    },
    "category": "historical",
    "country": {"by": "Літва", "ru": "Литва", "en": "Lithuania"},
    "city": {"by": "Трокі", "ru": "Тракай", "en": "Trakai"},
    "coordinates": [54.6606, 24.9431],
    "description": {
        "by": "Пышны неакласічны палац роду графаў Тышкевічаў («з Лагойска і Бярдычава»), пабудаваны ў 1898–1901 гг. графам Юзафам Тышкевічам і архітэктарам Юзафам Гусам на мысе паміж азёрамі Гальвэ і Скайсціс, насупраць Трокскага астраўнога замка. Палац акружаны рамантычным паркам французскага ландшафтнага архітэктара Эдуара Андрэ з сістэмай сажалак і скульптур.",
        "ru": "Великолепный неоклассический дворец графов Тышкевичей на полуострове озера Гальве, прямо напротив Тракайского замка. Построен в 1898–1901 гг. графом Юзефом Тышкевичем по проекту Юзефа Гуса. Окружен роскошным парком Эдуарда Андре.",
        "en": "Magnificent neoclassical manor of the Counts Tyszkiewicz built in 1898–1901 by Count Józef Tyszkiewicz directly across from the medieval Trakai Island Castle on Lake Galvė. Surrounded by an exquisite park designed by French landscape master Édouard André."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Uzutrakis_Manor_2012.jpg/960px-Uzutrakis_Manor_2012.jpg",
    "links": [
        {"title": "Палац Тышкевічаў ва Ужутракісе — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Сядзіба_Тышкевічаў_(Ужутракіс)"}
    ],
    "tags": ["Літва", "Трокі", "Ужутракіс", "Тышкевічы", "палац", "Гальвэ", "historical"],
    "mustSee": True,
    "unverifiedCoordinates": False
})

# 6. PLACE: Lentvaris Tyszkiewicz Palace
upsert_place({
    "id": "lentvaris-tyszkiewicz-palace",
    "title": {
        "by": "Неагатычны палац графаў Тышкевічаў у Ландвараве (Лентварыс)",
        "ru": "Неоготический дворец графов Тышкевичей в Ландворово (Лентварис)",
        "en": "Tyszkiewicz Neo-Gothic Palace in Lentvaris"
    },
    "category": "historical",
    "country": {"by": "Літва", "ru": "Литва", "en": "Lithuania"},
    "city": {"by": "Лентварыс", "ru": "Лентварис", "en": "Lentvaris"},
    "coordinates": [54.6536, 25.0489],
    "description": {
        "by": "Манументальны неагатычны англійскі замак-палац на беразе возера, рэзідэнцыя графа Уладзіслава Тышкевіча. Пабудаваны ў XIX ст. і перабудаваны ў 1899 г. архітэктарам Тадэвушам Раствароўскім у стылі цюдараўскай готыкі з высокай вежай. Вакол палаца знаходзіцца вялікі пейзажны парк Эдуара Андрэ са штучнымі скаламі і вадаспадамі.",
        "ru": "Монументальный неоготический замок-дворец графа Владислава Тышкевича на берегу озера в Лентварисе. Перестроен в 1899 году в стиле тюдоровской неоготики. Окружен живописным парком Эдуарда Андре.",
        "en": "Monumental Neo-Gothic Tudor-style palace of Count Władysław Tyszkiewicz set beside Lake Lentvaris. Redesigned in 1899 by architect Tadeusz Rostworowski, featuring an imposing tower and a park by Édouard André."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Lentvaris_Manor_House.jpg/960px-Lentvaris_Manor_House.jpg",
    "links": [
        {"title": "Палац Тышкевічаў у Ландвараве — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Сядзіба_Тышкевічаў_(Лентварыс)"}
    ],
    "tags": ["Літва", "Ландвараў", "Лентварыс", "Тышкевічы", "неаготыка", "historical"],
    "unverifiedCoordinates": False
})

# 7. PLACE: Vilnius - St. Johns Church & Basilian Gate (Glaubitz masterpieces)
upsert_place({
    "id": "vilnia-glaubitz-st-johns",
    "title": {
        "by": "Касцёл Святых Янаў і Базыльянская брама ў Вільні (Ян Крыштаф Глаўбіц)",
        "ru": "Костёл Святых Иоаннов и Базилианские ворота в Вильнюсе (Иоганн Кристоф Глаубиц)",
        "en": "Church of St. Johns & Basilian Gate in Vilnius (Johann Christoph Glaubitz)"
    },
    "category": "church",
    "country": {"by": "Літва", "ru": "Литва", "en": "Lithuania"},
    "city": {"by": "Вільня", "ru": "Вильнюс", "en": "Vilnius"},
    "coordinates": [54.6826, 25.2886],
    "description": {
        "by": "Кульмінацыя стылю «віленскага барока», створаная славутым дойлідам Янам Крыштафам Глаўбіцам (які таксама перабудаваў Полацкі Сафійскі сабор). Галоўны хвалісты фасад касцёла Святых Янаў ва ўніверсітэце, яго арган і грандыёзны алтар з 10 калон — вяршыня сакральнага дойлідства ВКЛ. Непадалёк месціцца яшчэ адзін шэдэўр Глаўбіца — унікальная трох'ярусная барочная Брама манастыра Святой Тройцы (Базыльянскія муры), цесна звязаная з беларускім адраджэннем, друкарняй Скарыны і беларускай гімназіяй.",
        "ru": "Триумф школы «виленского барокко», созданный архитектором Иоганном Кристофом Глаубицем (автором перестройки полоцкого Софийского собора). Волнообразный фасад костёла Святых Иоаннов в университете и триумфальные Базилианские ворота монастыря Святой Троицы являются жемчужинами европейского барокко.",
        "en": "The crowning achievement of 'Vilnius Baroque' created by master architect Johann Christoph Glaubitz (who also rebuilt Saint Sophia Cathedral in Polotsk). Features the undulating facade and high altar of the University Church of St. Johns, alongside Glaubitz's magnificent Basilian Gate at Holy Trinity Monastery."
    },
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Vilnius_St_Johns_Church_facade.jpg/960px-Vilnius_St_Johns_Church_facade.jpg",
    "links": [
        {"title": "Касцёл Святых Янаў (Вільнюс) — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Касцёл_Святых_Янаў_(Вільнюс)"},
        {"title": "Ян Крыштаф Глаўбіц — Вікіпедыя", "url": "https://be.wikipedia.org/wiki/Ян_Крыштаф_Глаўбіц"}
    ],
    "tags": ["Вільня", "Літва", "Глаўбіц", "віленскае барока", "Святы Ян", "Базыльяне", "church"],
    "personId": "johann-christoph-glaubitz",
    "personIds": ["johann-christoph-glaubitz"],
    "mustSee": True,
    "unverifiedCoordinates": False
})

# ==========================================
# 8. MARK ICONIC WORLD SITES AS MUST-SEE
# ==========================================

must_see_ids = {
    # Lithuania
    "vilnia-vostraya-brama", "vilnia-rosy-cemetery", "vilnia-dom-pad-balvanami",
    "vilnia-glaubitz-st-johns", "trakai-uzutrakis-tyszkiewicz-palace", "palanga-tiskevicius-palace",
    # Italy
    "bari-basilica-san-nicola-bona-sforza-tomb", "bari-castello-svevo-bona-sforza",
    "florence-city-hub", "skaryna-padua-university", "rome-sergius-bacchus-zyrovici",
    # Poland
    "biala-podlaska-radziwill-palace", "nieborow-nesvizh-armoury",
    "krakow-muzeum-emeryka-hutten-czapskiego", "krakow-wawel-cathedral-kosciuszko",
    "krakow-sukiennice-siemiradzki", "warszawa-royal-castle-rejtan",
    "warszawa-belarus-center", "nazi-camp-auschwitz-birkenau", "nazi-camp-sobibor-revolt",
    # Czechia
    "skaryna-prague-monument", "olsany-cemetery-prague",
    # USA
    "un-hq-chernobyl-tapestry", "kosciuszko-national-memorial-philadelphia",
    "chicago-kosciuszko-monument", "south-river-belarusian-cemetery",
    # UK
    "london-belarusian-memorial-church", "london-skaryna-library",
    # France
    "paris-mickiewicz-monument", "maisons-laffitte-kultura-czapski",
    # Denmark
    "ringsted-st-bendts-church-sophia-minsk",
    # Austria
    "vienna-hofburg-radziwill-armour", "nazi-camp-mauthausen-memorial",
    # Sweden
    "visby-baltic-centre-writers-bcwt", "uppsala-carolina-rediviva-belarustreasures",
    # Ukraine
    "kyiv-pechersk-lavra-hleb-minskirad", "kyiv-karatkevich-monument", "kyiv-memorial-fallen-belarusians",
    # Chile
    "santiago-domeyko-monument",
    # GULAG & Camps
    "gulag-solovki-slon", "gulag-sandarmokh-memorial", "gulag-kolyma-maska-smutku",
    "moscow-kremlin-lazkovichy-cross"
}

for p in places:
    if p['id'] in must_see_ids:
        p['mustSee'] = True
    elif 'mustSee' not in p:
        p['mustSee'] = False

# Save files
with open('data/places.json', 'w', encoding='utf-8') as f:
    json.dump(places, f, ensure_ascii=False, indent=2)
with open('data/places.js', 'w', encoding='utf-8') as f:
    f.write('// Albaruthenica Places Dataset\nwindow.INITIAL_PLACES = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

with open('data/persons.json', 'w', encoding='utf-8') as f:
    json.dump(persons, f, ensure_ascii=False, indent=2)
with open('data/persons.js', 'w', encoding='utf-8') as f:
    f.write('// Albaruthenica Persons Dataset\nwindow.INITIAL_PERSONS = ' + json.dumps(persons, ensure_ascii=False, indent=2) + ';\n')

print(f"Dataset successfully updated! Total places: {len(places)}, Total persons: {len(persons)}")
must_see_count = sum(1 for p in places if p.get('mustSee'))
print(f"Total Must-See places flagged: {must_see_count}")
