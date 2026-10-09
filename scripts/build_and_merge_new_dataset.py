import json
import re
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

# Load existing
with open('data/places.json', 'r', encoding='utf-8') as f:
    places = json.load(f)
with open('data/persons.json', 'r', encoding='utf-8') as f:
    persons = json.load(f)

with open('scripts/new_persons_images.json', 'r', encoding='utf-8') as f:
    portraits = json.load(f)

# 1. ADD NEW PERSONS
new_persons_data = [
    {
        "id": "magdalena-radziwill",
        "name": {
            "by": "Марыя Магдалена Радзівіл",
            "ru": "Мария Магдалена Радзивилл",
            "en": "Maria Magdalena Radziwiłł"
        },
        "dates": "1861 — 1945",
        "role": {
            "by": "Мецэнатка беларускага адраджэння, асветніца, графіня і княгіня",
            "ru": "Меценатка беларусского возрождения, просветительница, графиня и княгиня",
            "en": "Patroness of Belarusian national revival, philanthropist and noblewoman"
        },
        "bio": {
            "by": "Выбітная дзяячка беларускага нацыянальна-культурнага адраджэння, дачка графа Яна Завішы. Фінансавала выданне першай кнігі Максіма Багдановіча «Вянок», твораў Якуба Коласа, Максіма Гарэцкага, газету «Наша Ніва», беларускія школы, шпіталі і таварыствы. У 1918 г. падтрымала Беларускую Народную Рэспубліку, адкрыла ў сваім варшаўскім палацы на вуліцы Фоксаль палітычны салон для дзеячаў БНР. Апошнія гады правяла ў Швейцарыі (Фрыбур).",
            "ru": "Выдающаяся деятельница беларусского национально-культурного возрождения, дочь графа Яна Завиши. Финансировала издание первого сборника Максима Богдановича «Вянок», произведений Якуба Коласа, Максима Горецкого, газету «Наша Ніва», беларусские школы и больницы. В 1918 г. поддержала Белорусскую Народную Республику, открыла в своём варшавском дворце на улице Фоксаль политический салон деятелей БНР. Последние годы провела в Швейцарии (Фрибур).",
            "en": "Prominent figure of the Belarusian national-cultural revival, daughter of Count Jan Zawisza. She funded the publication of Maksim Bahdanovich's landmark poetry book 'Vianok', works by Yakub Kolas, Maksim Haretski, the 'Nasha Niva' newspaper, and schools. In 1918 she actively backed the Belarusian Democratic Republic, hosting a political salon in her Warsaw palace on Foksal street. Spent her final years in Fribourg, Switzerland."
        },
        "wiki": portraits.get("magdalena-radziwill", {}).get("wiki", "https://be.wikipedia.org/wiki/Марыя_Магдалена_Радзівіл"),
        "image": portraits.get("magdalena-radziwill", {}).get("thumb", "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Maryja_Magdalena_Radzivi%C5%82_%28Zavi%C5%A1a%29.jpg/330px-Maryja_Magdalena_Radzivi%C5%82_%28Zavi%C5%A1a%29.jpg"),
        "placeIds": []
    },
    {
        "id": "jan-zawisza",
        "name": {
            "by": "Ян Тадэвуш Завіша",
            "ru": "Ян Тадеушевич Завиша",
            "en": "Jan Tadeusz Zawisza"
        },
        "dates": "1822 — 1887",
        "role": {
            "by": "Беларускі археолаг, этнограф, фалькларыст і мецэнат",
            "ru": "Беларусский археолог, этнограф, фольклорист и меценат",
            "en": "Belarusian archaeologist, folklorist and philanthropist"
        },
        "bio": {
            "by": "Беларускі арыстакрат, ураджэнец Кухцічаў Ігуменскага павета (Міншчына). Піянер даследавання першабытнай археалогіі каменнага веку на тэрыторыі Беларусі, даследчык беларускага фальклору і звычаяў. У Варшаве заснаваў і выдаваў часопіс «Wiadomości archeologiczne». Прафінансаваў грандыёзную рэстаўрацыю Калоны караля Жыгімонта III у Варшаве з вырабам ствала з італьянскага ружовага граніту. Бацька Магдалены Радзівіл.",
            "ru": "Беларусский аристократ, уроженец Кухтичей Минской губернии. Пионер исследования первобытной археологии каменного века на территории Беларуси, собиратель фольклора. Основал журнал «Wiadomości archeologiczne». Профинансировал масштабную реставрацию Колонны Сигизмунда III в Варшаве из итальянского гранита. Отец Магдалены Радзивилл.",
            "en": "Belarusian aristocrat, born in Kukhtzichy (Minsk region). Pioneer in Stone Age archaeological research on the territory of Belarus, folklorist and patron of science. Funded the major restoration of the Sigismund Column in Warsaw using Italian pink granite. Father of Magdalena Radziwill."
        },
        "wiki": portraits.get("jan-zawisza", {}).get("wiki", "https://ru.wikipedia.org/wiki/Завиша,_Ян_Тадеушевич"),
        "image": portraits.get("jan-zawisza", {}).get("thumb", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/%D0%AF%D0%BD_%D0%A2%D0%B0%D0%B4%D1%8D%D1%83%D1%88_%D0%97%D0%B0%D0%B2%D1%96%D1%88%D0%B0.jpg/330px-%D0%AF%D0%BD_%D0%A2%D0%B0%D0%B4%D1%8D%D1%83%D1%88_%D0%97%D0%B0%D0%B2%D1%96%D1%88%D0%B0.jpg"),
        "placeIds": []
    },
    {
        "id": "yazep-khodzko",
        "name": {
            "by": "Язэп Ходзька",
            "ru": "Иосиф (Юзеф) Ходзько",
            "en": "Józef Chodźko"
        },
        "dates": "1800 — 1881",
        "role": {
            "by": "Геадэзіст, географ, тапограф, удзельнік паўстання 1830—1831 гг.",
            "ru": "Геодезист, географ, топограф, участник восстания 1830—1831 гг.",
            "en": "Geodesist, geographer, topographer, 1830 insurgent"
        },
        "bio": {
            "by": "Выбітны беларускі геадэзіст і географ, ураджэнец мястэчка Крывічы (Мядзельшчына). Выпускнік Віленскага ўніверсітэта. Падчас паўстання 1830–1831 гг. планаваўся камендантам Вільні, пасля чаго высланы царызмам на Каўказ. Ажыццявіў манументальную Закаўказскую трыянгуляцыю, упершыню вымераў вяршыні Арарата і Эльбруса, уганараваны Залатым Канстанцінаўскім медалём. Пахаваны ў Тбілісі на Кукійскіх могілках.",
            "ru": "Выдающийся беларусский геодезист и географ, уроженец Мядельщины. Выпускник Виленского университета. Участник восстания 1830–1831 гг., сослан царскими властями на Кавказ. Осуществил фундаментальную Закавказскую триангуляцию, измерил высоты Арарата и Эльбруса. Похоронен в Тбилиси на Кукийском кладбище.",
            "en": "Prominent Belarusian geodesist and geographer, born near Myadzel. Graduate of Vilnius University. Participant in the 1830–1831 uprising, exiled by the tsarist regime to the Caucasus where he executed the comprehensive Transcaucasian triangulation. Buried in Tbilisi at the Kukiya cemetery."
        },
        "wiki": portraits.get("yazep-khodzko", {}).get("wiki", "https://be.wikipedia.org/wiki/Язэп_Ходзька"),
        "image": portraits.get("yazep-khodzko", {}).get("thumb", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Chodzko%2C_General_Geodesist.jpg/330px-Chodzko%2C_General_Geodesist.jpg"),
        "placeIds": []
    },
    {
        "id": "yanka-luchyna",
        "name": {
            "by": "Янка Лучына (Іван Неслухоўскі)",
            "ru": "Янка Лучина (Иван Неслуховский)",
            "en": "Yanka Luchyna (Ivan Niesluchowski)"
        },
        "dates": "1851 — 1897",
        "role": {
            "by": "Беларускі паэт, драматург і перакладчык",
            "ru": "Беларусский поэт, драматург и переводчик",
            "en": "Belarusian poet, playwright and translator"
        },
        "bio": {
            "by": "Беларускі паэт шляхецкага роду Лучыўка-Неслухоўскіх, ураджэнец Мінска. Аўтар класічных паэтычных шэдэўраў «Роднай старонцы», «Вясновай песенькі», зборніка «Вязанка», вершаў пра палескі край. Пасля навучання ў Пецярбургу працаваў начальнікам чыгуначных складоў у Тыфлісе (Тбілісі) у 1877–1880 гг., дзе ў яго зарадзілася шмат вобразаў.",
            "ru": "Беларусский поэт шляхетского рода Лучивка-Неслуховских, уроженец Минска. Автор классических стихотворений «Роднай старонцы», «Вязанка», шедевров о Полесье. После учёбы в Петербурге работал начальником железнодорожных складов в Тифлисе (Тбилиси) в 1877–1880 гг.",
            "en": "Belarusian poet of the noble Luchyuka-Neslukhouski family, born in Minsk. Author of classic Belarusian lyrical poems 'Rodnay starontsy' and 'Viazanka'. Worked in Tiflis (Tbilisi) heading railway depots in 1877–1880."
        },
        "wiki": portraits.get("yanka-luchyna", {}).get("wiki", "https://be.wikipedia.org/wiki/Янка_Лучына"),
        "image": portraits.get("yanka-luchyna", {}).get("thumb", "https://upload.wikimedia.org/wikipedia/commons/6/6d/Janka_%C5%81u%C4%8Dyna.jpg"),
        "placeIds": []
    },
    {
        "id": "pyotra-krecheuski",
        "name": {
            "by": "Пётр (Пётра) Крэчэўскі",
            "ru": "Пётр Антонович Кречевский",
            "en": "Pyotra Krechewski"
        },
        "dates": "1879 — 1928",
        "role": {
            "by": "Трэці Старшыня Рады БНР, гісторык, паэт, драматург",
            "ru": "Третий Председатель Рады БНР, историк, поэт, драматург",
            "en": "Third President of the Rada of BNR, historian, poet"
        },
        "bio": {
            "by": "Выбітны дзяржаўны дзеяч Беларускай Народнай Рэспублікі, Старшыня Рады БНР у 1919–1928 гг., аўтар Трэцяй Устаўной граматы аб незалежнасці Беларусі. Перанёс кіраўніцтва БНР у Прагу, дабіўся чэшскіх дзяржаўных стыпендый для соцень беларускіх студэнтаў, заснаваў Беларускі замежны архіў. Пахаваны на Альшанскіх могілках у Празе.",
            "ru": "Выдающийся государственный деятель Белорусской Народной Республики, Председатель Рады БНР в 1919–1928 гг. Перенёс центр БНР в Прагу, добился стипендий для беларусских студентов, основал Беларусский заграничный архив. Похоронен на Ольшанском кладбище в Праге.",
            "en": "Prominent statesman of the Belarusian Democratic Republic, President of the Rada of the BNR in 1919–1928. Relocated the BNR council to Prague, secured Czechoslovak government scholarships for Belarusian students, and founded the Belarusian Foreign Archive. Buried at Olsany Cemetery in Prague."
        },
        "wiki": portraits.get("pyotra-krecheuski", {}).get("wiki", "https://be.wikipedia.org/wiki/Пётр_Антонавіч_Крэчэўскі"),
        "image": portraits.get("pyotra-krecheuski", {}).get("thumb", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Piotr_Kre%C4%8De%C5%ADski.jpg/330px-Piotr_Kre%C4%8De%C5%ADski.jpg"),
        "placeIds": []
    },
    {
        "id": "larysa-heniyush",
        "name": {
            "by": "Ларыса Геніюш",
            "ru": "Лариса Антоновна Гениюш",
            "en": "Larysa Hienijuš"
        },
        "dates": "1910 — 1983",
        "role": {
            "by": "Класік беларускай літаратуры, паэтка, Генеральны сакратар Рады БНР",
            "ru": "Классик беларусской литературы, поэтесса, Генеральный секретарь Рады БНР",
            "en": "Classic Belarusian poet, General Secretary of the Rada of BNR"
        },
        "bio": {
            "by": "Вялікая беларуская паэтка, сімвал нязломнасці духу, ураджэнка Ваўкавышчыны. Жыла ў Празе з 1937 г., сакратар Рады БНР, захавальніца дзяржаўнага архіва БНР і пячаткі з Пагоняй. Аўтар зборніка «Ад родных ніў» і аўтабіяграфічнай аповесці «Споведзь». Пасля выкрадання савецкімі органамі ў 1948 г. прайшла праз ГУЛАГ, адмовіўшыся прыняць савецкае грамадзянства.",
            "ru": "Великая беларусская поэтесса, символ несокрушимости национального духа, уроженка Волковыщины. Жила в Праге с 1937 г., Генеральный секретарь Рады БНР, хранительница архива и печати БНР с Погоней. Автор книги «Споведзь». Прошла сталинские лагеря, наотрез отказавшись принять советское гражданство.",
            "en": "Legendary Belarusian poet and symbol of unwavering national spirit. Lived in Prague from 1937, serving as General Secretary of the Rada of BNR and guardian of its state archives and seal. Author of the classic memoir 'Spovedz'. Endured years in the Soviet Gulag, firmly refusing Soviet citizenship."
        },
        "wiki": portraits.get("larysa-heniyush", {}).get("wiki", "https://be.wikipedia.org/wiki/Ларыса_Антонаўна_Геніюш"),
        "image": portraits.get("larysa-heniyush", {}).get("thumb", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/%C5%81arysa_Hieniju%C5%A1._%D0%9B%D0%B0%D1%80%D1%8B%D1%81%D0%B0_%D0%93%D0%B5%D0%BD%D1%96%D1%8E%D1%88_%281937%29.jpg/330px-%C5%81arysa_Hieniju%C5%A1._%D0%9B%D0%B0%D1%80%D1%8B%D1%81%D0%B0_%D0%93%D0%B5%D0%BD%D1%96%D1%8E%D1%88_%281937%29.jpg"),
        "placeIds": []
    },
    {
        "id": "vasil-bykau",
        "name": {
            "by": "Васіль Быкаў",
            "ru": "Василь Владимирович Быков",
            "en": "Vasil Bykaŭ"
        },
        "dates": "1924 — 2003",
        "role": {
            "by": "Народны пісьменнік Беларусі, сусветна вядомы празаік і сумленне нацыі",
            "ru": "Народный писатель Беларуси, всемирно известный прозаик и совесть нации",
            "en": "People's Writer of Belarus, world-renowned author and moral conscience of Belarus"
        },
        "bio": {
            "by": "Сусветна вядомы беларускі празаік, ураджэнец вёскі Бычкі на Вушаччыне. Аўтар шэдэўраў псіхалагічнай ваеннай прозы «Сотнікаў», «Знак бяды», «Жураўліны крык», «Альпійская балада», «Доўгі шлях дадому». У 1990–2000-я гады — маральны аўтарытэт і лідар беларускага дэмакратычнага руху. Апошні замежны перыяд жыцця (2002–2003) правёў у Празе на запрашэнне прэзідэнта Вацлава Гавела.",
            "ru": "Всемирно известный беларусский прозаик, уроженец Ушаччины. Автор шедевров военной прозы «Сотников», «Знак беды», «Обелиск», «Долгая дорога домой». Моральный авторитет беларусского движения за свободу. Последний период эмиграции (2002–2003) провёл в Праге по личному приглашению Вацлава Гавела.",
            "en": "World-renowned Belarusian novelist and moral compass of the nation, born in Bychki (Ushachy district). Master of psychological wartime prose ('Sotnikov', 'Sign of Misfortune', 'Alpine Ballad', 'Long Road Home'). Spent his final exile period in Prague (2002–2003) upon the personal invitation of President Václav Havel."
        },
        "wiki": portraits.get("vasil-bykau", {}).get("wiki", "https://be.wikipedia.org/wiki/Васіль_Уладзіміравіч_Быкаў"),
        "image": portraits.get("vasil-bykau", {}).get("thumb", "https://upload.wikimedia.org/wikipedia/commons/1/1a/Vasil_Bykov_%28cropped%29.jpg"),
        "placeIds": []
    },
    {
        "id": "hanna-tumarkina",
        "name": {
            "by": "Ганна Тумаркіна",
            "ru": "Анна Павловна Тумаркина",
            "en": "Anna Tumarkin"
        },
        "dates": "1875 — 1951",
        "role": {
            "by": "Першая ў Еўропе жанчына-прафесар філасофіі, навукоўца і выкладчыца",
            "ru": "Первая в Европе женщина-профессор философии, учёная",
            "en": "First female professor of philosophy in Europe, academic"
        },
        "bio": {
            "by": "Выдатная філосафка і навукоўца, ураджэнка Дуброўна (Віцебшчына). У 1898 годзе ў Бернскім універсітэце (Швейцарыя) стала першай жанчынай-выкладчыцай філасофіі, а ў 1909 г. — першай ва ўсёй Еўропе жанчынай-экстраардынарным прафесарам. Аўтарка фундаментальных прац па эстэтыцы, гісторыі філасофіі і швейцарскай культуры. У Берне ў яе гонар названая вуліца Tumarkinweg.",
            "ru": "Выдающийся философ и учёная, уроженка Дубровно (Витебская губ.). В Бернском университете стала первой женщиной-преподавателем философии в Швейцарии (1898) и первой в Европе женщиной — профессором философии (1909). В Берне в её честь названа улица Tumarkinweg.",
            "en": "Pioneering philosopher, born in Dubrovno (Vitebsk region, Belarus). At the University of Bern in Switzerland, she became the first female philosophy lecturer (1898) and in 1909 the first female professor of philosophy in all of Europe. A street adjacent to the university in Bern is named Tumarkinweg in her honour."
        },
        "wiki": "https://en.wikipedia.org/wiki/Anna_Tumarkin",
        "image": "https://upload.wikimedia.org/wikipedia/en/e/e2/Anna_Tumarkin.jpg",
        "placeIds": []
    },
    {
        "id": "emeryk-hutten-czapski",
        "name": {
            "by": "Эмерык Гутэн-Чапскі",
            "ru": "Эмерик фон Гуттен-Чапский",
            "en": "Emeryk Hutten-Czapski"
        },
        "dates": "1828 — 1896",
        "role": {
            "by": "Дзяржаўны дзеяч, калекцыянер, нумізмат і бібліяфіл са Станькава",
            "ru": "Государственный деятель, коллекционер, нумизмат и библиофил из Станьково",
            "en": "Statesman, numismatist, collector from Stankava"
        },
        "bio": {
            "by": "Беларускі магнат, граф са Станькава (пад Койданавам/Дзяржынскам). Сабраў у сваім станькаўскім маёнтку грандыёзную калекцыю старажытнасцей беларускай зямлі і ВКЛ: 30 тысяч манет і медалёў, 20 тысяч тамоў рэдкіх кніг, 16 слуцкіх паясоў, зброю і гравюры. У 1894 г. перавёз калекцыю ў Кракаў і стварыў знакаміты Музей Гутэн-Чапскага.",
            "ru": "Беларусский магнат, граф из Станьково (Минщина). Собрал в имении колоссальную коллекцию древностей Беларуси и ВКЛ: 30 тысяч монет, 20 тысяч томов редких книг, 16 слуцких поясов, оружие и гравюры. В 1894 г. перевёз собрание в Краков, создав известный Музей Гуттен-Чапского.",
            "en": "Belarusian magnate and count from Stankava (Minsk region). Assembled an immense private museum collection of Belarusian and GDL antiquities: 30,000 coins and medals, 20,000 rare books, 16 Slutsk sashes, arms, and engravings. In 1894 relocated it to Krakow, establishing the Hutten-Czapski Museum."
        },
        "wiki": portraits.get("emeryk-hutten-czapski", {}).get("wiki", "https://be.wikipedia.org/wiki/Эмерык_Гутэн-Чапскі"),
        "image": portraits.get("emeryk-hutten-czapski", {}).get("thumb", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Emeryk_Hutten-Czapski._%D0%AD%D0%BC%D0%B5%D1%80%D1%8B%D0%BA_%D0%93%D1%83%D1%82%D1%8D%D0%BD-%D0%A7%D0%B0%D0%BF%D1%81%D0%BA%D1%96_%281896%29.jpg/330px-Emeryk_Hutten-Czapski._%D0%AD%D0%BC%D0%B5%D1%80%D1%8B%D0%BA_%D0%93%D1%83%D1%82%D1%8D%D0%BD-%D0%A7%D0%B0%D0%BF%D1%81%D0%BA%D1%96_%281896%29.jpg"),
        "placeIds": []
    },
    {
        "id": "jazafat-kuncevic",
        "name": {
            "by": "Святы Язафат Кунцэвіч",
            "ru": "Святой Иосафат Кунцевич",
            "en": "Saint Josaphat Kuntsevych"
        },
        "dates": "1580 — 1623",
        "role": {
            "by": "Полацкі архіепіскап, святы і пакутнік Уніяцкай царквы",
            "ru": "Полоцкий архиепископ, святой и мученик Униатской церкви",
            "en": "Archbishop of Polotsk, saint and martyr of the Uniate Church"
        },
        "bio": {
            "by": "Рэлігійны і грамадскі дзеяч Рэчы Паспалітай, полацкі архіепіскап, ігумен Жыровіцкага манастыра. Бараніў Берасцейскую унію і самабытнасць усходняга абраду ў адзінстве з Апостальскім Пасадам. Трагічна загінуў у Віцебску ў 1623 г. Кананізаваны папам Піем IX у 1867 г. Яго святыя мошчы захоўваюцца ў галоўнай святыні каталіцтва — саборы Святога Пятра ў Ватыкане.",
            "ru": "Религиозный деятель Речи Посполитой, полоцкий архиепископ, игумен Жировичского монастыря. Поборник Брестской унии. Погиб в Витебске в 1623 г., канонизирован в 1867 г. Его мощи покоятся в соборе Святого Петра в Ватикане.",
            "en": "Archbishop of Polotsk, prior of the Zyrovichy monastery, martyr of the Eastern Catholic (Uniate) Church in the Grand Duchy of Lithuania. Canonized in 1867. His holy relics rest in St. Peter's Basilica in the Vatican."
        },
        "wiki": portraits.get("jazafat-kuncevic", {}).get("wiki", "https://be.wikipedia.org/wiki/Язафат_Кунцэвіч"),
        "image": portraits.get("jazafat-kuncevic", {}).get("thumb", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/JKuncewicz.jpg/330px-JKuncewicz.jpg"),
        "placeIds": []
    },
    {
        "id": "celina-borzencka",
        "name": {
            "by": "Блаславёная Цэліна Бажэнцкая",
            "ru": "Блаженная Целина Боженцкая",
            "en": "Blessed Celina Borzęcka"
        },
        "dates": "1833 — 1913",
        "role": {
            "by": "Заснавальніца Кангрэгацыі сясцёр-змартыхпаўстанак, блаславёная",
            "ru": "Основательница Конгрегации сестёр-воскресенок, блаженная",
            "en": "Foundress of the Sisters of the Resurrection, blessed"
        },
        "bio": {
            "by": "Рэлігійная і грамадская дзяячка з роду Хлюдзінскіх, ураджэнка Антовіля каля Оршы. У маёнтку Абрэмбшчына пад Гроднам дапамагала сялянам, падчас паўстання 1863 г. хавала паўстанцаў Каліноўскага, сядзела ў гродзенскай турме з немаўлём. Пасля смерці мужа выехала ў Рым, дзе разам з дачкой Ядвігай заснавала Кангрэгацыю сясцёр Змёртвыхпаўстання (Casa Madre). Абвешчаная блаславёнай у 2007 г.",
            "ru": "Религиозная деятельница из рода Хлюдзинских, уроженка Оршанщины. Под Гродно помогала крестьянам, скрывала повстанцев Калиновского в 1863 г., сидела в тюрьме. В Риме вместе с дочерью Ядвигой основала Конгрегацию сестёр Воскресения Господня (Casa Madre). Беатифицирована в 2007 г.",
            "en": "Religious figure, born near Orsha. In her estate near Hrodna she aided peasants and sheltered Kastus Kalinouski's insurgents in 1863, enduring tsarist imprisonment. In Rome she co-founded the Congregation of the Sisters of the Resurrection (Casa Madre). Beatified in 2007."
        },
        "wiki": portraits.get("celina-borzencka", {}).get("wiki", "https://be.wikipedia.org/wiki/Цэліна_Бажэнцкая"),
        "image": portraits.get("celina-borzencka", {}).get("thumb", "https://upload.wikimedia.org/wikipedia/commons/a/a5/Celina_Chludzi%C5%84ska_Borz%C4%99cka.jpg"),
        "placeIds": []
    },
    {
        "id": "aleksandr-valkovich",
        "name": {
            "by": "Аляксандр Вальковіч",
            "ru": "Александр Иванович Валькович",
            "en": "Alyaksandr Valkovich"
        },
        "dates": "1892 — 1937",
        "role": {
            "by": "Міністр фінансаў БНР, дыпламатычны прадстаўнік БНР у Грузіі",
            "ru": "Министр финансов БНР, дипломатический представитель БНР в Грузии",
            "en": "Finance Minister of BNR, diplomatic representative of BNR in Georgia"
        },
        "bio": {
            "by": "Беларускі грамадска-палітычны дзеяч, ураджэнец Мінска. Удзельнік Першага Усебеларускага з'езда 1917 г., міністр фінансаў у Народным Сакратарыяце Беларускай Народнай Рэспублікі, дыпламатычны прадстаўнік урада БНР пры ўрадзе Грузінскай Дэмакратычнай Рэспублікі ў Тыфлісе (1918–1920 гг., Моладзевы палац). Рэпрэсаваны і расстраляны ў 1937 г.",
            "ru": "Беларусский общественно-политический деятель, уроженец Минска. Министр финансов БНР, дипломатический представитель БНР при правительстве Грузии в Тифлисе (1918–1920 гг.). Репрессирован и расстрелян в 1937 г.",
            "en": "Belarusian statesman, born in Minsk. Finance Minister of the Belarusian Democratic Republic (BNR) and diplomatic envoy to the Democratic Republic of Georgia in Tiflis (1918–1920). Executed in Soviet repressions in 1937."
        },
        "wiki": portraits.get("aleksandr-valkovich", {}).get("wiki", "https://be.wikipedia.org/wiki/Аляксандр_Іванавіч_Вальковіч"),
        "image": portraits.get("aleksandr-valkovich", {}).get("thumb", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Aleksander_Valkovich.jpg/330px-Aleksander_Valkovich.jpg"),
        "placeIds": []
    }
]

existing_person_ids = {p['id'] for p in persons}
for np in new_persons_data:
    if np['id'] not in existing_person_ids:
        persons.append(np)
        print(f"Added new person: {np['id']}")

# 2. PREPARE ALL NEW PLACES
new_places_data = [
    # WARSAW
    {
        "id": "warsaw-sigismund-column",
        "title": {
            "by": "Калона караля Жыгімонта III Вазы (рэстаўрацыя Яна Завішы)",
            "ru": "Колонна короля Сигизмунда III Вазы (реставрация Яна Завиши)",
            "en": "Sigismund's Column (Restoration by Jan Zawisza)"
        },
        "category": "monument",
        "city": {"by": "Варшава", "ru": "Варшава", "en": "Warsaw"},
        "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
        "coordinates": [52.2472, 21.0143],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Славуты сімвал Варшавы на Замкавай плошчы. Кароль Жыгімонт III Ваза зацвердзіў Трэці Статут ВКЛ 1588 года на старабеларускай мове. У 1885–1887 гг. найбуйнейшую рэстаўрацыю калоны прафінансаваў беларускі археолаг і мецэнат граф Ян Завіша разам з Людовікам Красінскім: быў створаны новы ствол з ружовага італьянскага граніту. Разбураны ў 1944 г. гістарычны ствол Завішы экспануецца побач з плошчай.",
            "ru": "Знаменитый символ Варшавы на Замковой площади. Сигизмунд III утвердил Третий Статут ВКЛ 1588 г. на старобеларусском языке. В 1885–1887 гг. крупнейшую реставрацию монумента профинансировал беларусский археолог Ян Завиша: ствол колонны изготовили из итальянского розового гранита. Его фрагменты экспонируются рядом.",
            "en": "Iconic landmark on Castle Square in Warsaw. King Sigismund III confirmed the Third Statute of the GDL in 1588 in the Old Belarusian language. In 1885–1887, the major restoration was funded by Belarusian archaeologist and patron Jan Zawisza, who commissioned the pink Italian granite column."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Kolumna_Zygmunta_III_Wazy_w_Warszawie.jpg/500px-Kolumna_Zygmunta_III_Wazy_w_Warszawie.jpg",
        "personId": "jan-zawisza",
        "personIds": ["jan-zawisza", "magdalena-radziwill"],
        "tags": ["warsaw", "monument", "zawisza", "statut1588", "sigismund"],
        "links": [
            {"title": "Maldzis.world: Беларусская Варшава ч.1", "url": "https://maldzis.world/belarusskaja-varshava-chast-i-kolonna-sigizmunda-tretego/"},
            {"title": "Wikipedia: Kolumna Zygmunta", "url": "https://pl.wikipedia.org/wiki/Kolumna_Zygmunta_III_Wazy_w_Warszawie"}
        ]
    },
    {
        "id": "warsaw-przebendowski-palace",
        "title": {
            "by": "Палац Пшэбэндоўскіх / Завішаў / Радзівілаў (Музей незалежнасці)",
            "ru": "Дворец Пшебендовских / Завишей / Радзивиллов (Музей независимости)",
            "en": "Przebendowski-Zawisza-Radziwiłł Palace (Museum of Independence)"
        },
        "category": "historical",
        "city": {"by": "Варшава", "ru": "Варшава", "en": "Warsaw"},
        "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
        "coordinates": [52.2452, 21.0028],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Барочны палац XVIII ст. на алеі «Салідарнасці», 62. У студзені 1863 г. палац набыў граф Ян Завіша з Кухцічаў. Тут жыла і расла яго дачка, будучая выдатная мецэнатка беларускага адраджэння Магдалена Радзівіл (Завіша). На фасадзе ўсталявана мемарыяльная дошка з імёнамі Завішаў і Радзівілаў. Цяпер тут месціцца Музей незалежнасці.",
            "ru": "Барочный дворец на аллее «Солидарности», 62. В 1863 г. дворец приобрёл граф Ян Завиша из Кухтичей. Здесь росла его дочь, будущая главная меценатка беларусского возрождения Магдалена Радзивилл. На фасаде установлена мемориальная доска Завишей и Радзивиллов. Ныне Музей независимости.",
            "en": "Baroque palace on Aleja Solidarności 62. In 1863 acquired by Count Jan Zawisza from Kukhtzichy. Here grew up his daughter, prominent Belarusian patroness Magdalena Radziwill. Today houses the Museum of Independence."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Pa%C5%82ac_Przebendowskich_Radziwi%C5%82%C5%82%C3%B3w_w_Warszawie.jpg/500px-Pa%C5%82ac_Przebendowskich_Radziwi%C5%82%C5%82%C3%B3w_w_Warszawie.jpg",
        "personId": "magdalena-radziwill",
        "personIds": ["magdalena-radziwill", "jan-zawisza"],
        "tags": ["warsaw", "palace", "magdalena-radziwill", "zawisza", "museum"],
        "links": [
            {"title": "Maldzis.world: Беларуская Варшава ч.3", "url": "https://maldzis.world/belaruskaja-varshava-chastka-3-palac-zavisha/"},
            {"title": "Wikipedia: Pałac Przebendowskich w Warszawie", "url": "https://pl.wikipedia.org/wiki/Pa%C5%82ac_Przebendowskich_w_Warszawie"}
        ]
    },
    {
        "id": "warsaw-foksal-palace-bourbon",
        "title": {
            "by": "Палац Валоўскага / Бурбона — рэзідэнцыя Магдалены Радзівіл",
            "ru": "Дворец Воловского / Бурбона — резиденция Магдалены Радзивилл",
            "en": "Wołowski / Bourbon Palace — Residence of Magdalena Radziwiłł"
        },
        "category": "historical",
        "city": {"by": "Варшава", "ru": "Варшава", "en": "Warsaw"},
        "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
        "coordinates": [52.2338, 21.0205],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Палац на вул. Фоксаль 3/5, набыты Магдаленай Радзівіл у 1900 г. У 1918–1919 гг. палац стаў галоўным беларускім палітычным салонам у Варшаве: тут збіраліся Эдвард Вайніловіч, Раман Скірмунт, Лявон Вітан-Дубейкаўскі (консул БНР) для вырашэння лёсу беларускай дзяржаўнасці. Пазней перададзены праўнуку прынцу Антонію дэ Бурбону Сіцылійскаму.",
            "ru": "Дворец на ул. Фоксаль 3/5, приобретённый Магдаленой Радзивилл в 1900 г. В 1918–1919 гг. служил главным беларусским политическим салоном в Варшаве: здесь собирались Эдвард Войнилович, Роман Скирмунт, Леон Витан-Дубейковский для решения судьбы беларусской государственности.",
            "en": "Palace on Foksal Street 3/5, owned by Magdalena Radziwill from 1900. In 1918–1919 it hosted the main Belarusian political salon in Warsaw, gathering Edward Woynillowicz, Raman Skirmunt, and Leon Vitan-Dubeikauski to discuss Belarusian statehood."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Foksal_3-5_Warszawa.jpg/500px-Foksal_3-5_Warszawa.jpg",
        "personId": "magdalena-radziwill",
        "personIds": ["magdalena-radziwill"],
        "tags": ["warsaw", "palace", "magdalena-radziwill", "bnr", "foksal"],
        "links": [
            {"title": "Maldzis.world: Беларуская Варшава ч.4", "url": "https://maldzis.world/belaruskaja-varshava-chastka-4-palac-burbona/"},
            {"title": "Wikipedia: Pałac Wołowskiego w Warszawie", "url": "https://pl.wikipedia.org/wiki/Pa%C5%82ac_Wo%C5%82owskiego_w_Warszawie"}
        ]
    },
    {
        "id": "warsaw-poniatowski-monument",
        "title": {
            "by": "Помнік Юзафу Панятоўскаму (гамельскі след)",
            "ru": "Памятник Юзефу Понятовскому (гомельский след)",
            "en": "Monument to Prince Józef Poniatowski (Gomel Heritage)"
        },
        "category": "monument",
        "city": {"by": "Варшава", "ru": "Варшава", "en": "Warsaw"},
        "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
        "coordinates": [52.2431, 21.0163],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Конны помнік перад Прэзідэнцкім палацам на Кракаўскім прадмесці. Арыгінальная скульптура працы Бертэля Торвальдсена на працягу 82 гадоў (1840–1922) упрыгожвала парк палаца Паскевічаў у Гомелі, з'яўляючыся адзінай коннай статуяй у Беларусі, і была вернутая ў Варшаву паводле Рыжскага міру 1921 года.",
            "ru": "Конный монумент перед Президентским дворцом в Варшаве. Оригинальная скульптура Торвальдсена на протяжении 82 лет (1840–1922) стояла на террасе парка Паскевичей в Гомеле — единственная конная статуя в Беларуси, возвращённая в Варшаву по Рижскому миру 1921 г.",
            "en": "Equestrian monument in front of the Presidential Palace on Krakowskie Przedmieście. The original sculpture by Bertel Thorvaldsen stood for 82 years (1840–1922) in the park of the Paskevich Palace in Gomel as the only equestrian monument in Belarus before being returned under the Peace of Riga."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Pomnik_ksi%C4%99cia_J%C3%B3zefa_Poniatowskiego_w_Warszawie_2020.jpg/500px-Pomnik_ksi%C4%99cia_J%C3%B3zefa_Poniatowskiego_w_Warszawie_2020.jpg",
        "tags": ["warsaw", "monument", "gomel", "poniatowski", "thorvaldsen"],
        "links": [
            {"title": "Maldzis.world: Беларусская Варшава ч.2", "url": "https://maldzis.world/belarusskaja-varshava-chast-2-bronzovyj-vsadnik-bez-shtanov/"},
            {"title": "Wikipedia: Pomnik Józefa Poniatowskiego w Warszawie", "url": "https://pl.wikipedia.org/wiki/Pomnik_J%C3%B3zefa_Poniatowskiego_w_Warszawie"}
        ]
    },
    {
        "id": "warsaw-belarusian-youth-hub",
        "title": {
            "by": "Беларускі моладзевы хаб у Варшаве",
            "ru": "Белорусский молодёжный хаб в Варшаве",
            "en": "Belarusian Youth Hub in Warsaw"
        },
        "category": "culture",
        "city": {"by": "Варшава", "ru": "Варшава", "en": "Warsaw"},
        "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
        "coordinates": [52.2223, 21.0167],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Культурная і грамадская прастора на плошчы Канстытуцыі, 6. Размешчаны ў гістарычным будынку, дзе ў 1989 г. працаваў камітэт польскага руху «Салідарнасць». Арганізуе выставы, канцэрты, прэзентацыі кніг, тэатральныя і моўныя курсы.",
            "ru": "Культурное и общественное пространство на площади Конституции, 6. Расположено в историческом здании штаба движения «Солидарность» 1989 года. Проводит выставки, концерты, презентации книг и курсы.",
            "en": "Cultural and social community hub on Plac Konstytucji 6, situated in the historic building of the Polish 'Solidarność' committee from 1989. Hosts concerts, exhibitions, and lectures."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Plac_Konstytucji_w_Warszawie_2021.jpg/500px-Plac_Konstytucji_w_Warszawie_2021.jpg",
        "tags": ["warsaw", "culture", "diaspora", "hub"],
        "links": [
            {"title": "Budzma.org: Гайд па беларускай Варшаве", "url": "https://budzma.org/news/gayd-pa-belaruskay-varshave.html"}
        ]
    },
    {
        "id": "warsaw-belarusian-house",
        "title": {
            "by": "Беларускі дом у Варшаве",
            "ru": "Белорусский дом в Варшаве",
            "en": "Belarusian House in Warsaw"
        },
        "category": "culture",
        "city": {"by": "Варшава", "ru": "Варшава", "en": "Warsaw"},
        "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
        "coordinates": [52.2268, 21.0267],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Грамадскі і культурны цэнтр беларускай дыяспары ў Польшчы на вул. Вейскай, 13/3 (ul. Wiejska 13/3). Дзейнічае з 2012 года як інфармацыйны і адукацыйны хаб, ладзіць выставы, трэнінгі і дабрачынныя імпрэзы.",
            "ru": "Общественный и культурный центр беларусской диаспоры на ул. Вейской, 13/3. Действует с 2012 года как координационный центр, проводит выставки, встречи и культурные мероприятия.",
            "en": "Public and cultural hub of the Belarusian diaspora in Poland located on Wiejska 13/3. Operating since 2012, hosting cultural events, meetings, and exhibitions."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Ulica_Wiejska_w_Warszawie_2019.jpg/500px-Ulica_Wiejska_w_Warszawie_2019.jpg",
        "tags": ["warsaw", "culture", "diaspora", "house"],
        "links": [
            {"title": "Budzma.org: Гайд па беларускай Варшаве", "url": "https://budzma.org/news/gayd-pa-belaruskay-varshave.html"}
        ]
    },

    # GEORGIA / SAKARTVELO
    {
        "id": "tbilisi-railway-station-luchyna",
        "title": {
            "by": "Таварная чыгуначная станцыя — месца працы Янкі Лучыны",
            "ru": "Товарная железнодорожная станция — место работы Янки Лучины",
            "en": "Tiflis Goods Railway Station — Workplace of Yanka Luchyna"
        },
        "category": "historical",
        "city": {"by": "Тбілісі", "ru": "Тбилиси", "en": "Tbilisi"},
        "country": {"by": "Грузія", "ru": "Грузия", "en": "Georgia"},
        "coordinates": [41.7214, 44.7981],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Чыгуначны вузел Тбілісі, дзе ў 1877–1880 гг. пасля заканчэння Пецярбургскага тэхналагічнага інстытута служыў начальнікам складоў беларускі паэт Іван Неслухоўскі (Янка Лучына). Тут малады інжынер натхняўся каўказскімі краявідамі перад вяртаннем у Мінск.",
            "ru": "Железнодорожный узел Тбилиси, где в 1877–1880 гг. работал начальником складов классик беларусской литературы Иван Неслуховский (Янка Лучина).",
            "en": "Railway depot area in Tbilisi where classic Belarusian poet Ivan Niesluchowski (Yanka Luchyna) served as chief of warehouses from 1877 to 1880 after engineering studies."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Janka_%C5%81u%C4%8Dyna.jpg/330px-Janka_%C5%81u%C4%8Dyna.jpg",
        "personId": "yanka-luchyna",
        "personIds": ["yanka-luchyna"],
        "tags": ["georgia", "tbilisi", "luchyna", "railway", "literature"],
        "links": [
            {"title": "Maldzis.world: Гайд па беларускіх мясцінах Сакартвэла", "url": "https://maldzis.world/gajd-pa-belaruskih-mjascinah-sakartvjela/"}
        ]
    },
    {
        "id": "tbilisi-youth-palace-valkovich",
        "title": {
            "by": "Моладзевы (Варанцоўскі) палац — Аляксандр Вальковіч",
            "ru": "Молодёжный (Воронцовский) дворец — Александр Валькович",
            "en": "Youth (Vorontsov) Palace — Alyaksandr Valkovich"
        },
        "category": "historical",
        "city": {"by": "Тбілісі", "ru": "Тбилиси", "en": "Tbilisi"},
        "country": {"by": "Грузія", "ru": "Грузия", "en": "Georgia"},
        "coordinates": [41.6961, 44.7997],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Гістарычны палац намесніка на праспекце Руставелі, 6, дзе зараджалася Грузінская Дэмакратычная Рэспубліка. Тут працаваў міністр фінансаў БНР Аляксандр Вальковіч — афіцыйны дыпламатычны прадстаўнік Беларускай Народнай Рэспублікі пры ўрадзе Грузіі ў 1918–1920 гг.",
            "ru": "Исторический дворец на проспекте Руставели, 6. Здесь работал министр финансов БНР Александр Валькович — дипломатический представитель Белорусской Народной Республики при правительстве Грузии в 1918–1920 гг.",
            "en": "Historic palace on Rustaveli Avenue 6. Seat where the diplomatic mission of the Belarusian Democratic Republic (BNR) operated under Finance Minister and envoy Alyaksandr Valkovich in 1918–1920."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Youth_Palace%2C_Tbilisi.jpg/500px-Youth_Palace%2C_Tbilisi.jpg",
        "personId": "aleksandr-valkovich",
        "personIds": ["aleksandr-valkovich"],
        "tags": ["georgia", "tbilisi", "bnr", "valkovich", "diplomacy"],
        "links": [
            {"title": "Maldzis.world: Гайд па беларускіх мясцінах Сакартвэла", "url": "https://maldzis.world/gajd-pa-belaruskih-mjascinah-sakartvjela/"}
        ]
    },
    {
        "id": "tbilisi-unr-bnr-mission",
        "title": {
            "by": "Дыпламатычная місія на праспекце Руставелі — Іван Краскоўскі",
            "ru": "Дипломатическая миссия на проспекте Руставели — Иван Красковский",
            "en": "Diplomatic Mission on Rustaveli Avenue — Ivan Kraskouski"
        },
        "category": "plaque",
        "city": {"by": "Тбілісі", "ru": "Тбилиси", "en": "Tbilisi"},
        "country": {"by": "Грузія", "ru": "Грузия", "en": "Georgia"},
        "coordinates": [41.7012, 44.7925],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Будынак на праспекце Руставелі, 37, дзе працаваў дзеяч БНР і УНР Іван Краскоўскі (ураджэнец Гродзеншчыны). Краскоўскі ўзначальваў дыпламатычную місію на Каўказе і выступаў дарадцам дэлегацыі БНР. На будынку адкрыта мемарыяльная дошка.",
            "ru": "Здание на проспекте Руставели, 37, где работал деятель БНР и УНР Иван Красковский (уроженец Гродненщины), возглавлявший дипломатическую миссию на Кавказе. Установлена памятная доска.",
            "en": "Building at Rustaveli Avenue 37 where Belarusian-Ukrainian diplomat and BNR figure Ivan Kraskouski led the diplomatic mission to the Caucasus. Marked with a commemorative plaque."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Jan_Kraskouski.jpg/330px-Jan_Kraskouski.jpg",
        "tags": ["georgia", "tbilisi", "plaque", "bnr", "kraskouski"],
        "links": [
            {"title": "Maldzis.world: Гайд па беларускіх мясцінах Сакартвэла", "url": "https://maldzis.world/gajd-pa-belaruskih-mjascinah-sakartvjela/"}
        ]
    },
    {
        "id": "tbilisi-philharmonic-staver",
        "title": {
            "by": "Тбіліская філармонія — «Жураўлі на Палессе ляцяць»",
            "ru": "Тбилисская филармония — «Жураўлі на Палессе ляцяць»",
            "en": "Tbilisi Philharmonic — 'Cranes Fly to Polesia'"
        },
        "category": "culture",
        "city": {"by": "Тбілісі", "ru": "Тбилиси", "en": "Tbilisi"},
        "country": {"by": "Грузія", "ru": "Грузия", "en": "Georgia"},
        "coordinates": [41.7089, 44.7836],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Канцэртная зала Тбіліскай філармоніі на вул. Мелікішвілі. Тут у 1970-х і 2001 гг. з аншлагамі выступалі «Песняры». Знаходзячыся ў Тбілісі, беларускі паэт Алесь Ставер на карабку запалак запісаў першыя радкі легендарнай песні «Жураўлі на Палессе ляцяць».",
            "ru": "Концертный зал Тбилисской филармонии. Здесь с триумфом выступали «Песняры». Находясь в Тбилиси, беларусский поэт Алесь Ставер написал на коробке спичек строки легендарной песни «Жураўлі на Палессе ляцяць».",
            "en": "Tbilisi State Concert Hall where the famous Belarusian band 'Pesnyary' performed. While in Tbilisi, Belarusian poet Ales Staver jotted down the lyrics to the beloved national song 'Cranes Fly to Polesia' on a matchbox."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Tbilisi_Concert_Hall_2011.jpg/500px-Tbilisi_Concert_Hall_2011.jpg",
        "tags": ["georgia", "tbilisi", "culture", "pesnyary", "music"],
        "links": [
            {"title": "Maldzis.world: Гайд па беларускіх мясцінах Сакартвэла", "url": "https://maldzis.world/gajd-pa-belaruskih-mjascinah-sakartvjela/"}
        ]
    },
    {
        "id": "tbilisi-art-academy-azgur",
        "title": {
            "by": "Тбіліская акадэмія мастацтваў — Заір Азгур і генерал Кандратовіч",
            "ru": "Тбилисская академия художеств — Заир Азгур и генерал Кондратович",
            "en": "Tbilisi State Academy of Arts — Zair Azgur & Gen. Kandratovich"
        },
        "category": "culture",
        "city": {"by": "Тбілісі", "ru": "Тбилиси", "en": "Tbilisi"},
        "country": {"by": "Грузія", "ru": "Грузия", "en": "Georgia"},
        "coordinates": [41.7011, 44.7961],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Акадэмія мастацтваў на вул. Грыбаедава, 22. Тут у 1929 г. вучыўся і працаваў народны мастак Беларусі Заір Азгур у майстэрні Якава Нікаладзэ. Раней у гэтым жа будынку размяшчаўся штаб 1-га Каўказскага армейскага корпуса генерала Кіпрыяна Кандратовіча — ураджэнца Лідчыны, галоўнакамандуючага войскаў БНР.",
            "ru": "Академия художеств на ул. Грибоедова, 22. Здесь в 1929 г. учился классик беларусской скульптуры Заир Азгур. Ранее в здании находился штаб 1-го Кавказского корпуса генерала Киприана Кондратовича — главнокомандующего войсками БНР.",
            "en": "Academy of Arts on Griboedov Street 22. Here renowned Belarusian sculptor Zair Azgur refined his craft in 1929. Previously housed the military headquarters of Gen. Kipryan Kandratovich, commander-in-chief of the BNR forces."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Tbilisi_State_Academy_of_Arts.jpg/500px-Tbilisi_State_Academy_of_Arts.jpg",
        "tags": ["georgia", "tbilisi", "azgur", "art", "kandratovich"],
        "links": [
            {"title": "Maldzis.world: Гайд па беларускіх мясцінах Сакартвэла", "url": "https://maldzis.world/gajd-pa-belaruskih-mjascinah-sakartvjela/"}
        ]
    },
    {
        "id": "tbilisi-kukiya-grave-chodzko",
        "title": {
            "by": "Кукійскія могілкі — магіла Язэпа Ходзькі",
            "ru": "Кукийское кладбище — могила Иосифа (Юзефа) Ходзько",
            "en": "Kukiya Cemetery — Grave of Józef Chodźko"
        },
        "category": "grave",
        "city": {"by": "Тбілісі", "ru": "Тбилиси", "en": "Tbilisi"},
        "country": {"by": "Грузія", "ru": "Грузия", "en": "Georgia"},
        "coordinates": [41.7161, 44.8131],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Гістарычныя могілкі Кукія ў Тбілісі ля царквы Св. Ніно. Тут у каталіцкай частцы спачывае выбітны беларускі географ, геадэзіст, генерал і паўстанец 1830 г. Язэп Ходзька (1800–1881), кіраўнік Закаўказскай трыянгуляцыі.",
            "ru": "Историческое кладбище Кукия в Тбилиси. В католической части похоронен выдающийся беларусский географ, геодезист и повстанец 1830 г. Иосиф (Юзеф) Ходзько (1800–1881).",
            "en": "Historic Kukiya Cemetery in Tbilisi near St. Nino's Church, where prominent Belarusian geographer, geodesist, and 1830 insurgent Józef Chodźko (1800–1881) is buried."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Chodzko%2C_General_Geodesist.jpg/330px-Chodzko%2C_General_Geodesist.jpg",
        "personId": "yazep-khodzko",
        "personIds": ["yazep-khodzko"],
        "tags": ["georgia", "tbilisi", "grave", "chodzko", "science"],
        "links": [
            {"title": "Maldzis.world: Гайд па беларускіх мясцінах Сакартвэла", "url": "https://maldzis.world/gajd-pa-belaruskih-mjascinah-sakartvjela/"}
        ]
    },
    {
        "id": "tskaltubo-kupala-kutateli",
        "title": {
            "by": "Курорт Цхалтуба — экспазіцыя Янкі Купалы ў Art House Kutateli",
            "ru": "Курорт Цхалтубо — экспозиция Янки Купалы в Art House Kutateli",
            "en": "Tskaltubo Resort — Yanka Kupala Memorial in Art House Kutateli"
        },
        "category": "culture",
        "city": {"by": "Цхалтуба", "ru": "Цхалтубо", "en": "Tskaltubo"},
        "country": {"by": "Грузія", "ru": "Грузия", "en": "Georgia"},
        "coordinates": [42.3275, 42.5978],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Любімы курорт Янкі Купалы ў Сакартвела, дзе пясняр рэгулярна адпачываў у 1938–1941 гг. Тут ён пазнаёміўся са сваёй музай Эліко Метэхелі і напісаў славуты верш «Генацвале». У гасцявым доме Art House Kutateli дзейнічае экспазіцыя, прысвечаная песняру.",
            "ru": "Любимый курорт Янки Купалы в Грузии, где классик отдыхал в 1938–1941 гг. Здесь он создал стихотворение «Генацвале». В гостевом доме Art House Kutateli открыта экспозиция памяти поэта.",
            "en": "Beloved Georgian resort of Yanka Kupala, where he vacationed between 1938 and 1941, writing the famous lyric 'Genatsvale'. A permanent Kupala memorial exhibit is open in Art House Kutateli."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Janka_Kupa%C5%82a._%D0%AF%D0%BD%D0%BA%D0%B0_%D0%9A%D1%83%D0%BF%D0%B0%D0%BB%D0%B0_%281930%29.jpg/330px-Janka_Kupa%C5%82a._%D0%AF%D0%BD%D0%BA%D0%B0_%D0%9A%D1%83%D0%BF%D0%B0%D0%BB%D0%B0_%281930%29.jpg",
        "personId": "yanka-kupala",
        "personIds": ["yanka-kupala"],
        "tags": ["georgia", "tskaltubo", "kupala", "literature"],
        "links": [
            {"title": "Maldzis.world: Гайд па беларускіх мясцінах Сакартвэла", "url": "https://maldzis.world/gajd-pa-belaruskih-mjascinah-sakartvjela/"}
        ]
    },

    # ROME & VATICAN
    {
        "id": "rome-st-peter-kuncevic",
        "title": {
            "by": "Сабор Святога Пятра — рэліквіі святога Язафата Кунцэвіча",
            "ru": "Собор Святого Петра — реликвии святого Иосафата Кунцевича",
            "en": "St. Peter's Basilica — Relics of Saint Josaphat Kuntsevych"
        },
        "category": "grave",
        "city": {"by": "Ватыкан / Рым", "ru": "Ватикан / Рим", "en": "Vatican / Rome"},
        "country": {"by": "Ватыкан", "ru": "Ватикан", "en": "Vatican"},
        "coordinates": [41.9022, 12.4539],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Галоўная святыня Каталіцкага касцёла. Каля алтара святога Васіля Вялікага спачываюць нятленныя мошчы беларускага святога і мучаніка Язафата Кунцэвіча (1580–1623), полацкага архіепіскапа і ігумена Жыровіцкага манастыра.",
            "ru": "Главный собор христианского мира. Возле алтаря святого Василия Великого покоятся нетленные мощи беларусского святого и мученика Иосафата Кунцевича (1580–1623), полоцкого архиепископа.",
            "en": "The central sanctuary of Catholicism. Near the altar of St. Basil the Great rest the sacred relics of Belarusian saint and martyr Josaphat Kuntsevych (1580–1623), Archbishop of Polotsk."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/JKuncewicz.jpg/330px-JKuncewicz.jpg",
        "personId": "jazafat-kuncevic",
        "personIds": ["jazafat-kuncevic"],
        "tags": ["vatican", "rome", "church", "kuncevic", "relics"],
        "links": [
            {"title": "Maldzis.world: Беларускія мясціны ў Вечным горадзе", "url": "https://maldzis.world/belaruskija-mjasciny-vechnym-goradze/"},
            {"title": "Wikipedia: Базіліка Святога Пятра", "url": "https://be.wikipedia.org/wiki/Базіліка_Святога_Пятра"}
        ]
    },
    {
        "id": "rome-sergius-bacchus-zyrovici",
        "title": {
            "by": "Царква святых Сяргея і Вакха — цудатворны Жыровіцкі абраз",
            "ru": "Церковь святых Сергия и Вакха — чудотворная Жировичская икона",
            "en": "Church of Sts. Sergius & Bacchus — Zyrovichy Madonna"
        },
        "category": "church",
        "city": {"by": "Рым", "ru": "Рим", "en": "Rome"},
        "country": {"by": "Італія", "ru": "Италия", "en": "Italy"},
        "coordinates": [41.8942, 12.4908],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Старадаўні храм на Piazza della Madonna dei Monti, 3. Ад 1641 г. — галоўны рымскі асяродак манахаў-базыльянаў з Жыровічаў. У 1718 г. тут адшукалі цудатворную фрэску Маці Божай Жыровіцкай («Madonna del Pascolo / Багародзіца з пашы»), якая праславілася шматлікімі вылячэннямі. Купал увянчаны крыжам, падобным да Пагоні.",
            "ru": "Древний храм на Piazza della Madonna dei Monti, 3. С 1641 г. — римская резиденция монахов-базилиан из Жировичей. В 1718 г. здесь обнаружили чудотворную фреску Матери Божьей Жировичской («Madonna del Pascolo»), прославившуюся исцелениями.",
            "en": "Historic church on Piazza della Madonna dei Monti 3. From 1641, the main Roman seat of Basilian monks from Zyrovichy. In 1718, a miraculous fresco of the Mother of God of Zyrovichy ('Madonna del Pascolo') was rediscovered beneath the plaster."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Santi_Sergio_e_Bacco_a_Roma.jpg/500px-Santi_Sergio_e_Bacco_a_Roma.jpg",
        "tags": ["rome", "church", "zyrovici", "basilian", "icon"],
        "links": [
            {"title": "Maldzis.world: Беларускія мясціны ў Вечным горадзе", "url": "https://maldzis.world/belaruskija-mjasciny-vechnym-goradze/"},
            {"title": "Wikipedia: Santi Sergio e Bacco degli Armeni", "url": "https://en.wikipedia.org/wiki/Santi_Sergio_e_Bacco_degli_Armeni"}
        ]
    },
    {
        "id": "rome-il-gesu-radziwill",
        "title": {
            "by": "Касцёл Іль-Джэзу — кардынал Юры Радзівіл і Андрэй Баболя",
            "ru": "Костёл Иль-Джезу — кардинал Юрий Радзивилл и Андрей Боболя",
            "en": "Church of the Gesù — Cardinal Jerzy Radziwiłł"
        },
        "category": "church",
        "city": {"by": "Рым", "ru": "Рим", "en": "Rome"},
        "country": {"by": "Італія", "ru": "Италия", "en": "Italy"},
        "coordinates": [41.8959, 12.4798],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Галоўны храм ордэна езуітаў у Рыме на Via degli Astalli, 16. Паслужыў прамым архітэктурным правобразам для касцёла Божага Цела ў Нясвіжы. Тут пахаваны першы кардынал у гісторыі ВКЛ Юры Радзівіл (1556–1600) з мармуровым надмагіллем і гербам «Трубы», а ў капліцы захоўваюцца мошчы святога Андрэя Баболі.",
            "ru": "Главный храм ордена иезуитов в Риме, архитектурный прообраз костёла Божьего Тела в Несвиже. Здесь погребён первый кардинал в истории ВКЛ Юрий Радзивилл (1556–1600) с мраморной плитой с гербом «Трубы», а также хранятся мощи св. Андрея Боболи.",
            "en": "Mother church of the Jesuit Order in Rome, architectural prototype for the Corpus Christi Church in Nesvizh. Tomb of the first cardinal of the GDL, Jerzy Radziwiłł (1556–1600), adorned with the 'Trąby' coat of arms, and relics of St. Andrew Bobola."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Gesu_Church_Rome.jpg/500px-Gesu_Church_Rome.jpg",
        "personId": "radziwills",
        "personIds": ["radziwills"],
        "tags": ["rome", "church", "radziwill", "nesvizh", "bobola"],
        "links": [
            {"title": "Maldzis.world: Беларускія мясціны ў Вечным горадзе", "url": "https://maldzis.world/belaruskija-mjasciny-vechnym-goradze/"},
            {"title": "Wikipedia: Church of the Gesù", "url": "https://en.wikipedia.org/wiki/Church_of_the_Ges%C3%B9"}
        ]
    },
    {
        "id": "rome-radziwill-palace-boncompagni",
        "title": {
            "by": "Палац Марыі Ружы Радзівіл на Via Boncompagni 22",
            "ru": "Дворец Марии Розы Радзивилл на Via Boncompagni 22",
            "en": "Maria Roza Radziwiłł Palace on Via Boncompagni 22"
        },
        "category": "historical",
        "city": {"by": "Рым", "ru": "Рим", "en": "Rome"},
        "country": {"by": "Італія", "ru": "Италия", "en": "Italy"},
        "coordinates": [41.9079, 12.4947],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Неакласічны палац Радзівілаў на вуліцы Бонкампаньі, 22. Належаў княгіні Марыі Ружы Радзівіл (з Браніцкіх, 1863–1941) — гаспадыні Нясвіжскага замка. У гэтым палацы княгіня прымала каралеву Італіі Алену Савойскую і еўрапейскіх манархаў.",
            "ru": "Неоклассический дворец Радзивиллов на ул. Бонкомпаньи, 22. Принадлежал хозяйке Несвижского замка княгине Марии Розе Радзивилл. Здесь княгиня принимала королеву Италии Елену Савойскую и европейскую аристократию.",
            "en": "Neoclassical Radziwill palace on Via Boncompagni 22, owned by Princess Maria Roza Radziwiłł of Nesvizh Castle, where she hosted Queen Elena of Italy and European dignitaries."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Palazzo_Boncompagni_Corcos_Roma.jpg/500px-Palazzo_Boncompagni_Corcos_Roma.jpg",
        "personId": "radziwills",
        "personIds": ["radziwills"],
        "tags": ["rome", "palace", "radziwill", "nesvizh"],
        "links": [
            {"title": "Maldzis.world: Беларускія мясціны ў Вечным горадзе", "url": "https://maldzis.world/belaruskija-mjasciny-vechnym-goradze/"}
        ]
    },
    {
        "id": "rome-resurrectionists-casa-madre",
        "title": {
            "by": "Генеральны дом сясцёр-змартыхпаўстанак (Casa Madre) — Цэліна Бажэнцкая",
            "ru": "Генеральный дом сестёр-воскресенок (Casa Madre) — Целина Боженцкая",
            "en": "Resurrectionist Sisters Motherhouse (Casa Madre) — Celina Borzęcka"
        },
        "category": "church",
        "city": {"by": "Рым", "ru": "Рим", "en": "Rome"},
        "country": {"by": "Італія", "ru": "Италия", "en": "Italy"},
        "coordinates": [41.9114, 12.4667],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Галоўны манастырскі дом Кангрэгацыі сясцёр Змёртвыхпаўстання (Casa Madre) на Via Marcantonio Colonna, 52. Заснаваны ўраджэнкай Аршаншчыны, блаславёнай Цэлінай Бажэнцкай і яе дачкой Ядвігай (з-пад Гродна). Дзейнічае да сёння.",
            "ru": "Главный дом Конгрегации сестёр Воскресения Господня (Casa Madre) на Via Marcantonio Colonna, 52, основанный блаженной Целиной Боженцкой (уроженкой Оршанщины) и её дочерью Ядвигой.",
            "en": "The Motherhouse (Casa Madre) of the Sisters of the Resurrection on Via Marcantonio Colonna 52, established by Blessed Celina Borzęcka (born near Orsha) and her daughter Jadwiga."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Celina_Chludzi%C5%84ska_Borz%C4%99cka.jpg",
        "personId": "celina-borzencka",
        "personIds": ["celina-borzencka"],
        "tags": ["rome", "church", "borzencka", "monastery"],
        "links": [
            {"title": "Maldzis.world: Беларускія мясціны ў Вечным горадзе", "url": "https://maldzis.world/belaruskija-mjasciny-vechnym-goradze/"}
        ]
    },
    {
        "id": "rome-palazzo-pio-vatican-radio",
        "title": {
            "by": "Палацца Пія — Беларуская рэдакцыя Ватыканскага радыё",
            "ru": "Палаццо Пиа — Белорусская редакция Ватиканского радио",
            "en": "Palazzo Pio — Belarusian Editorial Office of Vatican Radio"
        },
        "category": "culture",
        "city": {"by": "Рым", "ru": "Рим", "en": "Rome"},
        "country": {"by": "Італія", "ru": "Италия", "en": "Italy"},
        "coordinates": [41.9028, 12.4631],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Гістарычны палац на Piazza Pia, 3 каля замка Святога Анёла. Ад 1950 г. тут працуе Беларуская рэдакцыя Ватыканскага радыё, якую ўзначальвалі ксёндз Пётр Татарыновіч, айцец Леў Гарошка, архімандрыт Роберт Тамушанскі і біскуп Часлаў Сіповіч.",
            "ru": "Исторический дворец на Piazza Pia, 3. С 1950 г. здесь работает Белорусская редакция Ватиканского радио, которую возглавляли священники Пётр Татаринович, Лев Горошко и епископ Чеслав Сипович.",
            "en": "Historic palace on Piazza Pia 3 near Castel Sant'Angelo. Since 1950, home to the Belarusian editorial desk of Vatican Radio, led by notable émigré cultural leaders."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Palazzo_Pio%2C_Rome.jpg/500px-Palazzo_Pio%2C_Rome.jpg",
        "tags": ["rome", "culture", "vatican", "radio", "media"],
        "links": [
            {"title": "Maldzis.world: Беларускія мясціны ў Вечным горадзе", "url": "https://maldzis.world/belaruskija-mjasciny-vechnym-goradze/"}
        ]
    },

    # KRAKOW
    {
        "id": "krakow-hutten-czapski-museum",
        "title": {
            "by": "Музей і палац Эмерыка Гутэн-Чапскага ў Кракаве",
            "ru": "Музей и дворец Эмерика Гуттен-Чапского в Кракове",
            "en": "Emeryk Hutten-Czapski Museum and Palace in Krakow"
        },
        "category": "culture",
        "city": {"by": "Кракаў", "ru": "Краков", "en": "Krakow"},
        "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
        "coordinates": [50.0597, 19.9322],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Філіял Нацыянальнага музея на вул. Пілсудскага, 12 (ul. Piłsudskiego 12). Палац набыў і абсталяваў у 1894 г. граф Эмерык Гутэн-Чапскі са Станькава для сваёй неацэннай калекцыі: 30 тысяч манет, 20 тысяч тамоў станькаўскай бібліятэкі, слуцкія паясы, граматы і экслібрысы.",
            "ru": "Филиал Национального музея на ул. Пилсудского, 12. Дворец приобрёл в 1894 г. граф Эмерик Гуттен-Чапский из Станьково для сокровищницы: 30 тысяч монет, 20 тысяч томов станьковской библиотеки, слуцкие пояса, медали и грамоты.",
            "en": "Branch of the National Museum on Piłsudskiego 12. Palace acquired in 1894 by Count Emeryk Hutten-Czapski of Stankava to preserve his immense collection: 30,000 coins, 20,000 rare books, Slutsk sashes, and manuscripts."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Emeryk_Hutten-Czapski._%D0%AD%D0%BC%D0%B5%D1%80%D1%8B%D0%BA_%D0%93%D1%83%D1%82%D1%8D%D0%BD-%D0%A7%D0%B0%D0%BF%D1%81%D0%BA%D1%96_%281896%29.jpg/330px-Emeryk_Hutten-Czapski._%D0%AD%D0%BC%D0%B5%D1%80%D1%8B%D0%BA_%D0%93%D1%83%D1%82%D1%8D%D0%BD-%D0%A7%D0%B0%D0%BF%D1%81%D0%BA%D1%96_%281896%29.jpg",
        "personId": "emeryk-hutten-czapski",
        "personIds": ["emeryk-hutten-czapski"],
        "tags": ["krakow", "museum", "czapski", "stankava", "numismatics"],
        "links": [
            {"title": "Maldzis.world: Дзе на карце Кракава знайсці Беларусь", "url": "https://maldzis.world/dze-na-karce-polskaga-krakava-znajsci-belarus/"},
            {"title": "Wikipedia: Muzeum im. Emeryka Hutten-Czapskiego", "url": "https://pl.wikipedia.org/wiki/Muzeum_im._Emeryka_Hutten-Czapskiego_w_Krakowie"}
        ]
    },
    {
        "id": "krakow-peter-paul-church-bernardoni",
        "title": {
            "by": "Касцёл святых Пятра і Паўла — архітэктар Бернардоні (копія Нясвіжа)",
            "ru": "Костёл святых Петра и Павла — архитектор Бернардони (копия Несвижа)",
            "en": "Church of Sts. Peter & Paul — Bernardoni (Nesvizh Model)"
        },
        "category": "church",
        "city": {"by": "Кракаў", "ru": "Краков", "en": "Krakow"},
        "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
        "coordinates": [50.0569, 19.9389],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Першы барочны касцёл Кракава на вул. Гродскай, 52A (ul. Grodzka 52A). Узведзены па праекце Джавані Бернардоні — слыннага «беларускага італьянца», які 13 гадоў жыў у Нясвіжы на запрашэнне Радзівіла Сіроткі і стварыў касцёл як прамую копію нясвіжскага касцёла Божага Цела.",
            "ru": "Первый барочный храм Кракова на ул. Гродзкой, 52A. Построен Джованни Бернардони — «беларусским итальянцем», прожившим 13 лет в Несвиже по приглашению Радзивилла Сиротки; собор возведён как близкая копия несвижского костёла Божьего Тела.",
            "en": "The first Baroque church in Krakow on Grodzka 52A, designed by Giovanni Maria Bernardoni who lived 13 years in Nesvizh and modeled this church directly after the Corpus Christi Church in Nesvizh."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Krak%C3%B3w_-_Ko%C5%9Bci%C3%B3%C5%82_%C5%9Awi%C4%99tych_Aposto%C5%82%C3%B3w_Piotra_i_Paw%C5%82a.JPG/500px-Krak%C3%B3w_-_Ko%C5%9Bci%C3%B3%C5%82_%C5%9Awi%C4%99tych_Aposto%C5%82%C3%B3w_Piotra_i_Paw%C5%82a.JPG",
        "personId": "radziwills",
        "personIds": ["radziwills"],
        "tags": ["krakow", "church", "bernardoni", "nesvizh", "baroque"],
        "links": [
            {"title": "Maldzis.world: Дзе на карце Кракава знайсці Беларусь", "url": "https://maldzis.world/dze-na-karce-polskaga-krakava-znajsci-belarus/"},
            {"title": "Wikipedia: Kościół Świętych Apostołów Piotra i Pawła w Krakowie", "url": "https://pl.wikipedia.org/wiki/Ko%C5%9Bci%C3%B3%C5%82_%C5%9Awi%C4%99tych_Aposto%C5%82%C3%B3w_Piotra_i_Paw%C5%82a_w_Krakowie"}
        ]
    },
    {
        "id": "krakow-anczyc-printing-bahusevic",
        "title": {
            "by": "Друкарня Анчыца — першае выданне «Дудкі беларускай» Багушэвіча",
            "ru": "Типография Анчица — первое издание «Дудкі беларускай» Богушевича",
            "en": "Anczyc Printing House — 1st Edition of Bahusevic's 'Dudka Bielaruskaja'"
        },
        "category": "historical",
        "city": {"by": "Кракаў", "ru": "Краков", "en": "Krakow"},
        "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
        "coordinates": [50.0558, 19.9378],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Будынак на вул. Кананічай, 9 (ul. Kanonicza 9). Тут у друкарні Уладзіслава Анчыца ў 1891 г. упершыню пабачыла свет «Дудка беларуская» Францішка Багушэвіча (пад псеўданімам Мацей Бурачок) з гістарычным маніфестам: «Не пакідайце ж мовы нашай беларускай, каб не ўмёрлі!»",
            "ru": "Здание на ул. Каноничей, 9. Здесь в типографии Владислава Анчица в 1891 г. впервые вышла в свет книга «Дудка беларуская» Францишка Богушевича со знаменитым заветом: «Не пакідайце ж мовы нашай беларускай, каб не ўмёрлі!»",
            "en": "Building on Kanonicza 9 in Krakow. In 1891, the printing house of Władysław Anczyc published the first edition of Francišak Bahuševič's seminal poetry book 'Dudka Bielaruskaja' with the famous manifesto on preserving the Belarusian language."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Dudka_bie%C5%82aruskaja.jpg/330px-Dudka_bie%C5%82aruskaja.jpg",
        "personId": "francisak-bahusevic",
        "personIds": ["francisak-bahusevic"],
        "tags": ["krakow", "printing", "bahusevic", "literature", "history"],
        "links": [
            {"title": "Maldzis.world: Дзе на карце Кракава знайсці Беларусь", "url": "https://maldzis.world/dze-na-karce-polskaga-krakava-znajsci-belarus/"}
        ]
    },
    {
        "id": "krakow-st-barbara-yuravichy-icon",
        "title": {
            "by": "Касцёл святой Барбары — цудатворны абраз Маці Божай Юравіцкай",
            "ru": "Костёл святой Барбары — чудотворная икона Матери Божьей Юровичской",
            "en": "St. Barbara's Church — Miraculous Icon of Our Lady of Yuravichy"
        },
        "category": "church",
        "city": {"by": "Кракаў", "ru": "Краков", "en": "Krakow"},
        "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
        "coordinates": [50.0617, 19.9403],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Касцёл на Малым Рынку, 9 (ul. Mały Rynek 9). Тут захоўваецца арыгінал славутага цудатворнага абраза Маці Божай Юравіцкай (з вёскі Юравічы Калінкавіцкага р-на Гомельшчыны), які ў 1885 г. перавезла сюды Габрыэля Горват з пісьмовым запаветам вярнуць у Юравічы пасля адраджэння святыні. Адшуканы Адамам Мальдзісам.",
            "ru": "Костёл на Малом Рынке, 9. Здесь хранится оригинал чудотворной иконы Матери Божьей Юровичской (из деревни Юровичи Калинковичского р-на), перевезённый в 1885 г. Габриэлой Горватт. Местонахождение иконы разыскал Адам Мальдис.",
            "en": "Church on Mały Rynek 9 housing the original miraculous icon of Our Lady of Yuravichy (from Yuravichy, Gomel region), secretly relocated to Krakow in 1885 by Gabriela Horwatt to save it from tsarist persecution. Identified by Adam Maldis."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Ko%C5%9Bci%C3%B3%C5%82_%C5%9Bw._Barbary_w_Krakowie.jpg/500px-Ko%C5%9Bci%C3%B3%C5%82_%C5%9Bw._Barbary_w_Krakowie.jpg",
        "personId": "adam-maldis",
        "personIds": ["adam-maldis"],
        "tags": ["krakow", "church", "yuravichy", "icon", "maldis"],
        "links": [
            {"title": "Maldzis.world: Дзе на карце Кракава знайсці Беларусь", "url": "https://maldzis.world/dze-na-karce-polskaga-krakava-znajsci-belarus/"}
        ]
    },

    # PRAGUE
    {
        "id": "prague-krecheuski-house",
        "title": {
            "by": "Дом Пётры Крэчэўскага на Брусэльскай, 1",
            "ru": "Дом Петра Кречевского на Брюссельской, 1",
            "en": "Pyotra Krechewski's Residence on Bruselská 1"
        },
        "category": "historical",
        "city": {"by": "Прага", "ru": "Прага", "en": "Prague"},
        "country": {"by": "Чэхія", "ru": "Чехия", "en": "Czech Republic"},
        "coordinates": [50.0722, 14.4358],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Дом у раёне Вінаграды (Bruselská 1), дзе ў 1923–1928 гг. жыў Старшыня Рады БНР Пётра Крэчэўскі. Тут месцілася прадстаўніцтва Рады БНР, ствараўся Беларускі замежны архіў і выдаваўся альманах «Замежная Беларусь».",
            "ru": "Дом в районе Винограды (Bruselská 1), где в 1923–1928 гг. жил Председатель Рады БНР Пётр Кречевский. Здесь находилось представительство Рады БНР, создавался архив БНР и издавался альманах «Замежная Беларусь».",
            "en": "Residence on Bruselská 1 in Prague-Vinohrady where the 3rd President of the Rada of BNR Pyotra Krechewski lived from 1923 until his death in 1928, creating the Belarusian Foreign Archive."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Piotr_Kre%C4%8De%C5%ADski.jpg/330px-Piotr_Kre%C4%8De%C5%ADski.jpg",
        "personId": "pyotra-krecheuski",
        "personIds": ["pyotra-krecheuski"],
        "tags": ["prague", "bnr", "krecheuski", "history"],
        "links": [
            {"title": "Maldzis.world: Беларуская Прага", "url": "https://maldzis.world/belaruskaja-praga-sabrali-gistoryi-pra-ajchynnyh-litaratara-i-zvjazanyja-z-imi-mescy-stalicy-chjehii/"}
        ]
    },
    {
        "id": "prague-heniyush-hermanova",
        "title": {
            "by": "Дом Ларысы і Янкі Геніюшаў на Германавай, 7",
            "ru": "Дом Ларисы и Янки Гениюш на Гержмановой, 7",
            "en": "Larysa & Yanka Hienijuš Residence on Heřmanova 7"
        },
        "category": "historical",
        "city": {"by": "Прага", "ru": "Прага", "en": "Prague"},
        "country": {"by": "Чэхія", "ru": "Чехия", "en": "Czech Republic"},
        "coordinates": [50.1006, 14.4372],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Галоўны пражскі адрас выдатнай паэткі Ларысы Геніюш і доктара Янкі Геніюша ў раёне Галяшовіцы (Heřmanova 7). Тут літаратарка напісала кнігу «Ад родных ніў», даглядала хворага прэзідэнта БНР Васіля Захарку і захоўвала дзяржаўны архіў БНР разам з пячаткай з Пагоняй.",
            "ru": "Главный пражский адрес Ларисы Гениюш и доктора Янки Гениюша на улице Heřmanova 7. Здесь поэтесса создавала свои книги, ухаживала за президентом БНР Василием Захарко и хранила государственный архив и печать БНР.",
            "en": "The main Prague home of Belarusian poet Larysa Hienijuš and Dr. Yanka Hienijuš on Heřmanova 7 in Holešovice. Here she safeguarded the archives and seal of the Belarusian Democratic Republic."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/%C5%81arysa_Hieniju%C5%A1._%D0%9B%D0%B0%D1%80%D1%8B%D1%81%D0%B0_%D0%93%D0%B5%D0%BD%D1%96%D1%8E%D1%88_%281937%29.jpg/330px-%C5%81arysa_Hieniju%C5%A1._%D0%9B%D0%B0%D1%80%D1%8B%D1%81%D0%B0_%D0%93%D0%B5%D0%BD%D1%96%D1%8E%D1%88_%281937%29.jpg",
        "personId": "larysa-heniyush",
        "personIds": ["larysa-heniyush"],
        "tags": ["prague", "heniyush", "bnr", "literature"],
        "links": [
            {"title": "Maldzis.world: Беларуская Прага", "url": "https://maldzis.world/belaruskaja-praga-sabrali-gistoryi-pra-ajchynnyh-litaratara-i-zvjazanyja-z-imi-mescy-stalicy-chjehii/"}
        ]
    },
    {
        "id": "prague-bykau-last-flat",
        "title": {
            "by": "Апошняя кватэра Васіля Быкава і Гаўлічкавы сады",
            "ru": "Последняя квартира Василя Быкова и Гавличковы сады",
            "en": "Vasil Bykaŭ's Last Residence & Havlíčkovy Sady"
        },
        "category": "historical",
        "city": {"by": "Прага", "ru": "Прага", "en": "Prague"},
        "country": {"by": "Чэхія", "ru": "Чехия", "en": "Czech Republic"},
        "coordinates": [50.0678, 14.4489],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Кватэра на вуліцы U Vršovického nádraží, дзе народны пісьменнік Васіль Быкаў з жонкай Ірынай жыў у пачатку 2003 г. падчас свайго апошняга замежнага перыяду. Побач — рамантычныя Гаўлічкавы сады (Havlíčkovy sady), дзе любіў гуляць пісьменнік.",
            "ru": "Квартира на улице U Vršovického nádraží, где Василь Быков жил в начале 2003 г. во время последнего периода эмиграции. Рядом — Гавличковы сады, где любил гулять писатель.",
            "en": "Apartment on U Vršovického nádraží where People's Writer of Belarus Vasil Bykaŭ spent his final months in early 2003, walking in the nearby Havlíčkovy Sady park before returning home."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Vasil_Bykov_%28cropped%29.jpg",
        "personId": "vasil-bykau",
        "personIds": ["vasil-bykau"],
        "tags": ["prague", "bykau", "literature", "memory"],
        "links": [
            {"title": "Maldzis.world: Беларуская Прага", "url": "https://maldzis.world/belaruskaja-praga-sabrali-gistoryi-pra-ajchynnyh-litaratara-i-zvjazanyja-z-imi-mescy-stalicy-chjehii/"}
        ]
    },

    # SWITZERLAND
    {
        "id": "zurich-fraumunster-chagall",
        "title": {
            "by": "Царква Фраўмюнстэр — вітражы Марка Шагала",
            "ru": "Церковь Фраумюнстер — витражи Марка Шагала",
            "en": "Fraumünster Church — Chagall's Stained Glass Windows"
        },
        "category": "culture",
        "city": {"by": "Цюрых", "ru": "Цюрих", "en": "Zurich"},
        "country": {"by": "Швейцарыя", "ru": "Швейцария", "en": "Switzerland"},
        "coordinates": [47.3697, 8.5414],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Славутая бажніца на Münsterhof 2 у Цюрыху. Сусветную славу царкве прынеслі 5 унікальных вітражных вокнаў хору і рузе-вітражы дыяметрам 2,7 м, створаныя ўраджэнцам Віцебска Маркам Шагалам у 1970 і 1978 гадах. Шагал уласнаручна апрацоўваў паверхню шкла ва ўзросце 83 і 90 гадоў.",
            "ru": "Знаменитая церковь на Münsterhof 2. Мировую известность ей принесли 5 уникальных витражных окон хора и окно-роза, созданные уроженцем Витебска Марком Шагалом в 1970 и 1978 гг.",
            "en": "Historic abbey church on Münsterhof 2 in Zurich. Famous worldwide for the five stunning stained glass choir windows and the rose window created by Vitebsk-born artist Marc Chagall in 1970 and 1978."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Fraum%C3%BCnster_Z%C3%BCrich_Chagall-Fenster.jpg/500px-Fraum%C3%BCnster_Z%C3%BCrich_Chagall-Fenster.jpg",
        "personId": "marc-chagall",
        "personIds": ["marc-chagall"],
        "items": [
            {
                "title": "Вітражныя вокны хору Фраўмюнстэр (Прарокі, Закон, Якаў, Сіён, Хрыстос)",
                "author": "Марк Шагал",
                "personId": "marc-chagall",
                "year": "1970",
                "description": "Пяць манументальных вітражных вокнаў вышынёй амаль 10 метраў, уласнаручна створаных Шагалам.",
                "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Fraum%C3%BCnster_Z%C3%BCrich_Chagall-Fenster.jpg/500px-Fraum%C3%BCnster_Z%C3%BCrich_Chagall-Fenster.jpg"
            },
            {
                "title": "Ружа-вітраж на паўднёвай сцяне нефа",
                "author": "Марк Шагал",
                "personId": "marc-chagall",
                "year": "1978",
                "description": "Круглае вітражнае акно дыяметрам 2,7 метра, выкананае майстрам у 90-гадовым узросце.",
                "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Fraum%C3%BCnster_Z%C3%BCrich_Chagall-Fenster.jpg/500px-Fraum%C3%BCnster_Z%C3%BCrich_Chagall-Fenster.jpg"
            }
        ],
        "tags": ["zurich", "chagall", "church", "art", "stained-glass"],
        "links": [
            {"title": "Maldzis.world: Шагал па Цюрыху", "url": "https://maldzis.world/shagal-po-cjurihu-ne-tolko-mark-ili-belarusskie-mesta-v-shvejcarii/"},
            {"title": "Wikipedia: Fraumünster", "url": "https://en.wikipedia.org/wiki/Fraum%C3%BCnster"}
        ]
    },
    {
        "id": "bern-university-tumarkinweg",
        "title": {
            "by": "Бернскі ўніверсітэт і вуліца Тумаркінвег — Ганна Тумаркіна",
            "ru": "Бернский университет и улица Тумаркинвег — Анна Тумаркина",
            "en": "University of Bern & Tumarkinweg — Anna Tumarkin"
        },
        "category": "historical",
        "city": {"by": "Берн", "ru": "Берн", "en": "Bern"},
        "country": {"by": "Швейцарыя", "ru": "Швейцария", "en": "Switzerland"},
        "coordinates": [46.9506, 7.4378],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Галоўны корпус Бернскага ўніверсітэта на Hochschulstrasse 4 і прылеглая вуліца Tumarkinweg. Прысвечаны выбітнай ураджэнцы Дуброўна (Беларусь) Ганне Тумаркінай (1875–1951) — першай у Швейцарыі і ва ўсёй Еўропе жанчыне-прафесару філасофіі.",
            "ru": "Главный корпус Бернского университета на Hochschulstrasse 4 и прилегающая улица Tumarkinweg в честь Анны Тумаркиной — уроженки Дубровно, первой в Европе женщины-профессора философии.",
            "en": "Main building of the University of Bern on Hochschulstrasse 4 and adjacent Tumarkinweg street, honoring Dubrovno-born Anna Tumarkin, Europe's first female philosophy professor."
        },
        "image": "https://upload.wikimedia.org/wikipedia/en/e/e2/Anna_Tumarkin.jpg",
        "personId": "hanna-tumarkina",
        "personIds": ["hanna-tumarkina"],
        "tags": ["bern", "university", "tumarkin", "philosophy", "science"],
        "links": [
            {"title": "Maldzis.world: Шагал па Цюрыху", "url": "https://maldzis.world/shagal-po-cjurihu-ne-tolko-mark-ili-belarusskie-mesta-v-shvejcarii/"},
            {"title": "Wikipedia: Anna Tumarkin", "url": "https://en.wikipedia.org/wiki/Anna_Tumarkin"}
        ]
    },
    {
        "id": "bourguillon-magdalena-radziwill",
        "title": {
            "by": "Царква Нотр-Дам-дэ-Бургійон — мемарыял Магдалены Радзівіл",
            "ru": "Церковь Нотр-Дам-де-Бургийон — мемориал Магдалены Радзивилл",
            "en": "Church of Notre-Dame de Bourguillon — Magdalena Radziwiłł Memorial"
        },
        "category": "plaque",
        "city": {"by": "Фрыбур", "ru": "Фрибур", "en": "Fribourg"},
        "country": {"by": "Швейцарыя", "ru": "Швейцария", "en": "Switzerland"},
        "coordinates": [46.8042, 7.1758],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Гістарычная царква ў прадмесці Фрыбура (Route de Bourguillon 21). Тут на прысядзібных могілках з 1945 па 2017 гг. спачываў прах выбітнай беларускай мецэнаткі княгіні Магдалены Радзівіл (перапахавана ў Мінску). На муры царквы ўсталявана мемарыяльная дошка аўтарства беларускага скульптара Максіма Петруля.",
            "ru": "Церковь в предместье Фрибура, где с 1945 по 2017 гг. покоился прах меценатки Магдалены Радзивилл (ныне перезахоронена в Минске). На стене установлена памятная доска работы Максима Петруля.",
            "en": "Church in the suburbs of Fribourg where Princess Magdalena Radziwill was buried from 1945 until her reburial in Minsk in 2017. A bronze commemorative plaque by Belarusian sculptor Maksim Petrul is placed on the wall."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Maryja_Magdalena_Radzivi%C5%82_%28Zavi%C5%A1a%29.jpg/330px-Maryja_Magdalena_Radzivi%C5%82_%28Zavi%C5%A1a%29.jpg",
        "personId": "magdalena-radziwill",
        "personIds": ["magdalena-radziwill"],
        "tags": ["fribourg", "switzerland", "radziwill", "plaque", "memory"],
        "links": [
            {"title": "Maldzis.world: Шагал па Цюрыху", "url": "https://maldzis.world/shagal-po-cjurihu-ne-tolko-mark-ili-belarusskie-mesta-v-shvejcarii/"}
        ]
    },
    {
        "id": "rapperswil-polish-museum-sluck",
        "title": {
            "by": "Замак Раперсвіль — слуцкія паясы і гербы ВКЛ",
            "ru": "Замок Рапперсвиль — слуцкие пояса и гербы ВКЛ",
            "en": "Rapperswil Castle — Slutsk Sashes and GDL Heraldry"
        },
        "category": "culture",
        "city": {"by": "Раперсвіль", "ru": "Рапперсвиль", "en": "Rapperswil"},
        "country": {"by": "Швейцарыя", "ru": "Швейцария", "en": "Switzerland"},
        "coordinates": [47.2269, 8.8156],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Сярэднявечны замак на Цюрыхскім возеры. У зборах музея захоўваюцца аўтэнтычныя слуцкія паясы з шаўкова-залатымі ніткамі, старадаўнія гербы гарадоў Вялікага Княства Літоўскага, а таксама доўгі час захоўвалася сэрца Тадэвуша Касцюшкі перад вяртаннем у Варшаву.",
            "ru": "Средневековый замок на Цюрихском озере. В собрании музея хранятся подлинные слуцкие пояса, старинные гербы городов ВКЛ; здесь же хранилось сердце Тадеуша Костюшко до отправки в Варшаву.",
            "en": "Medieval castle on Lake Zurich housing genuine Slutsk sashes, Grand Duchy of Lithuania heraldry, and previously the urn with Tadeusz Kosciuszko's heart before it was transferred to Warsaw."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Schloss_Rapperswil_2011.jpg/500px-Schloss_Rapperswil_2011.jpg",
        "tags": ["rapperswil", "switzerland", "castle", "slutsk-sash", "vkl"],
        "links": [
            {"title": "Maldzis.world: Шагал па Цюрыху", "url": "https://maldzis.world/shagal-po-cjurihu-ne-tolko-mark-ili-belarusskie-mesta-v-shvejcarii/"},
            {"title": "Wikipedia: Rapperswil Castle", "url": "https://en.wikipedia.org/wiki/Rapperswil_Castle"}
        ]
    },
    {
        "id": "zuchwil-kosciuszko-grave",
        "title": {
            "by": "Помнік на месцы пахавання вантробаў Тадэвуша Касцюшкі ў Цухвілі",
            "ru": "Памятник на месте захоронения внутренностей Тадеуша Костюшко в Цухвиле",
            "en": "Monument at the Entrails Burial Site of Tadeusz Kosciuszko in Zuchwil"
        },
        "category": "grave",
        "city": {"by": "Цухвіль (Залатурн)", "ru": "Цухвиль (Золотурн)", "en": "Zuchwil (Solothurn)"},
        "country": {"by": "Швейцарыя", "ru": "Швейцария", "en": "Switzerland"},
        "coordinates": [47.1997, 7.5583],
        "unverifiedCoordinates": True,
        "description": {
            "by": "Мемарыяльны помнік на могілках у мястэчку Цухвіль (прыгарад Залатурна). Пасля бальзамавання цела Касцюшкі ў 1817 г. яго вантробы былі асобна пахаваныя тут, дзе помнік стаіць і дагэтуль.",
            "ru": "Памятник на кладбище в городке Цухвиль (пригород Золотурна), где в 1817 г. после бальзамирования были захоронены внутренности Тадеуша Костюшко.",
            "en": "Memorial marker at the cemetery in Zuchwil near Solothurn where Tadeusz Kosciuszko's internal organs were interred following his embalming in 1817."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Tadeusz_Kosciuszko_portrait.jpg/330px-Tadeusz_Kosciuszko_portrait.jpg",
        "personId": "tadeusz-kosciuszko",
        "personIds": ["tadeusz-kosciuszko"],
        "tags": ["switzerland", "solothurn", "zuchwil", "kosciuszko", "grave"],
        "links": [
            {"title": "Maldzis.world: Шагал па Цюрыху", "url": "https://maldzis.world/shagal-po-cjurihu-ne-tolko-mark-ili-belarusskie-mesta-v-shvejcarii/"}
        ]
    }
]

existing_place_ids = {p['id'] for p in places}
added_count = 0
for np in new_places_data:
    if np['id'] not in existing_place_ids:
        places.append(np)
        added_count += 1
        print(f"Added new place: {np['id']} ({np['title']['by']})")
    else:
        print(f"Place already exists: {np['id']}")

print(f"\nTotal new places added: {added_count}")
print(f"Total places now: {len(places)}")
print(f"Total persons now: {len(persons)}")

# 3. RECALCULATE BIDIRECTIONAL LINKS
place_ids_set = {p['id'] for p in places}
for pers in persons:
    p_id = pers['id']
    linked = set(pers.get('placeIds', []))
    for pl in places:
        if pl.get('personId') == p_id or p_id in pl.get('personIds', []):
            linked.add(pl['id'])
        if any(item.get('personId') == p_id for item in pl.get('items', [])):
            linked.add(pl['id'])
    # filter valid
    pers['placeIds'] = sorted([pid for pid in linked if pid in place_ids_set])

# Also ensure place personIds is populated
for pl in places:
    pids = set(pl.get('personIds', []))
    if pl.get('personId'):
        pids.add(pl['personId'])
    for item in pl.get('items', []):
        if item.get('personId'):
            pids.add(item['personId'])
    pl['personIds'] = sorted(list(pids))

# 4. WRITE OUT JSON AND JS
with open('data/places.json', 'w', encoding='utf-8') as f:
    json.dump(places, f, ensure_ascii=False, indent=2)

with open('data/places.js', 'w', encoding='utf-8') as f:
    f.write('// Albaruthenica Places Dataset\nwindow.INITIAL_PLACES = ')
    json.dump(places, f, ensure_ascii=False, indent=2)
    f.write(';\n')

with open('data/persons.json', 'w', encoding='utf-8') as f:
    json.dump(persons, f, ensure_ascii=False, indent=2)

with open('data/persons.js', 'w', encoding='utf-8') as f:
    f.write('// Albaruthenica Persons Dataset\nwindow.INITIAL_PERSONS = ')
    json.dump(persons, f, ensure_ascii=False, indent=2)
    f.write(';\n')

print("Saved all dataset files successfully!")
