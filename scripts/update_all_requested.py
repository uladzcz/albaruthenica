# -*- coding: utf-8 -*-
"""
Update dataset with:
1. Fix vilnia-kvatera-samoyly (remove yanka-kupala, link uladzimir-samoila, fix typos).
2. Fix vilnia-bibliyateka-akademii-navuk-litvy-imya-urublew (remove kastus-kalinouski, link tadevush-urubleuski and valery-urubleuski).
3. Fix vilnia-dom-urublewskaha (remove adam-mickiewicz, link tadevush-urubleuski).
4. Add Walery Wróblewski's grave at Père Lachaise in Paris.
5. Add Belarusian-Lithuanian monarchs (persons and places: Wawel, Vilnius crypt, Ringsted, Warsaw cathedral, Paris Saint-Germain-des-Prés, Dresden Hofkirche, Central Park NY, Aglona, Veliuona, Kahlenberg Vienna).
6. Add Harbin / China & repressed clergy (persons and places: Harbin Marian mission & St. Nicholas lyceum, Butyrka Moscow, Ozerlag Tayshet, Solovki).
"""

import json
import os

with open('data/places.json', 'r', encoding='utf-8') as f:
    places = json.load(f)

with open('data/persons.json', 'r', encoding='utf-8') as f:
    persons = json.load(f)

places_map = {p['id']: p for p in places}
persons_map = {p['id']: p for p in persons}

# -------------------------------------------------------------
# 1. NEW PERSONS
# -------------------------------------------------------------

new_persons = [
    {
        "id": "uladzimir-samoila",
        "name": {
            "by": "Уладзімір Самойла",
            "ru": "Владимир Самойло",
            "en": "Uladzimir Samoila"
        },
        "years": "1878–1941",
        "role": {
            "by": "Публіцыст, літаратурны крытык, філосаф, грамадскі дзеяч",
            "ru": "Публицист, литературный критик, философ, общественный деятель",
            "en": "Publicist, literary critic, philosopher, public figure"
        },
        "bio": {
            "by": "Адзін з пачынальнікаў беларускага нацыянальна-адраджэнскага руху. Першым даў гісторыка-літаратурную ацэнку творчасці Янкі Купалы (артыкулы «Вячоркі», водгук на «Жалейку»). Выкладаў у Віленскай беларускай гімназіі, працаваў у Віленскім беларускім музеі імя І. Луцкевіча. Арыштаваны органамі НКУС у Вільні ў 1939 г., загінуў у зняволенні.",
            "ru": "Один из зачинателей белорусского национального возрождения. Первым дал историко-литературную оценку творчеству Янки Купалы. Преподавал в Виленской белорусской гимназии, работал в Виленском белорусском музее. Арестован НКВД в 1939 г., погиб в заключении.",
            "en": "One of the initiators of the Belarusian national revival. First to evaluate the poetry of Yanka Kupala in print. Taught at the Vilnius Belarusian Gymnasium, worked at the Lutskievich Museum. Arrested by NKVD in 1939, died in Soviet Gulag."
        },
        "photo": "https://upload.wikimedia.org/wikipedia/commons/8/8e/Samojla.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%A3%D0%BB%D0%B0%D0%B4%D0%B7%D1%96%D0%BC%D1%96%D1%80_%D0%86%D0%B2%D0%B0%D0%BD%D0%B0%D0%B2%D1%96%D1%87_%D0%A1%D0%B0%D0%BC%D0%BE%D0%B9%D0%BB%D0%B0"
    },
    {
        "id": "tadevush-urubleuski",
        "name": {
            "by": "Тадэвуш Урублеўскі",
            "ru": "Тадеуш Врублевский",
            "en": "Tadeusz Wróblewski"
        },
        "years": "1858–1925",
        "role": {
            "by": "Юрыст, адвакат, грамадскі дзеяч, бібліяфіл, заснавальнік Бібліятэкі Урублеўскіх",
            "ru": "Юрист, адвокат, общественный деятель, библиофил, основатель Библиотеки Врублевских",
            "en": "Lawyer, attorney, public figure, bibliophile, founder of Wróblewski Library"
        },
        "bio": {
            "by": "Беларускі і польскі грамадскі дзеяч, знакаміты віленскі адвакат і бібліяфіл. Абараняў у судах дзеячаў беларускага нацыянальнага руху (Цётку, Аляксандра Уласава, братоў Луцкевічаў). Сабраў унікальную калекцыю рэдкіх кніг і рукапісаў, якая склала аснову Бібліятэкі Урублеўскіх (цяпер Бібліятэка Акадэміі навук Літвы).",
            "ru": "Белорусский и польский общественный деятель, виленский адвокат и библиофил. Защищал деятелей белорусского национального движения (Тётку, А. Власова). Собрал уникальную коллекцию рукописей и книг, ставшую основой Библиотеки Врублевских (ныне Библиотека АН Литвы).",
            "en": "Public figure, prominent Vilnius attorney and bibliophile. Defended Belarusian national revival activists in court. Assembled a massive collection of rare books and manuscripts, founding the Wróblewski Library in Vilnius."
        },
        "photo": "https://upload.wikimedia.org/wikipedia/commons/5/56/Tadeusz_Wr%C3%B3blewski.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%A2%D0%B0%D0%B4%D1%8D%D0%B2%D1%83%D1%88_%D0%A3%D1%80%D1%83%D0%B1%D0%BB%D0%B5%D1%9E%D1%81%D0%BA%D1%96"
    },
    {
        "id": "valery-urubleuski",
        "name": {
            "by": "Валеры Антоній Урублеўскі",
            "ru": "Валерий Антоний Врублевский",
            "en": "Walery Antoni Wróblewski"
        },
        "years": "1836–1908",
        "role": {
            "by": "Рэвалюцыянер, адзін з кіраўнікоў паўстання 1863—1864 гадоў, генерал Парыжскай Камуны",
            "ru": "Революционер, один из руководителей восстания 1863—1864 гг., генерал Парижской Коммуны",
            "en": "Revolutionary, military commander of the 1863–1864 Uprising, General of the Paris Commune"
        },
        "bio": {
            "by": "Ураджэнец мястэчка Жалудок на Гарадзеншчыне. Адзін з найбліжэйшых паплечнікаў Кастуся Каліноўскага, камандуючы паўстанцкімі сіламі Гарадзенскага і Люблінскага ваяводстваў. Пасля паражэння паўстання эміграваў у Францыю, стаў выбітным вайсковым кіраўніком і генералам Парыжскай Камуны, камандаваў левабярэжнай арміяй абароны Парыжа. Пахаваны на знакамітых парыжскіх могілках Пер-Лашэз.",
            "ru": "Уроженец местечка Желудок на Гродненщине. Ближайший соратник Кастуся Калиновского, командующий повстанческими отрядами Гродненского и Люблинского воеводств. Генерал Парижской Коммуны, командовал левобережной армией Парижа. Похоронен на кладбище Пер-Лашез в Париже.",
            "en": "Born in Žaludok, Hrodna region. Close associate of Kastuś Kalinoŭski, military commander during the 1863–1864 Uprising. Later General of the Paris Commune in France, commanding the left bank army. Buried at Père Lachaise Cemetery in Paris."
        },
        "photo": "https://upload.wikimedia.org/wikipedia/commons/d/d9/Valery_Antoni_%C5%ACruble%C5%ADski._%D0%92%D0%B0%D0%BB%D0%B5%D1%80%D1%8B_%D0%90%D0%BD%D1%82%D0%BE%D0%BD%D1%96_%D0%8E%D1%80%D1%83%D0%B1%D0%BB%D0%B5%D1%9E%D1%81%D0%BA%D1%96_%281860-69%29.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%92%D0%B0%D0%BB%D0%B5%D1%80%D1%8B%D0%B9_%D0%90%D0%BD%D1%82%D0%BE%D0%BD%D1%96%D0%B9_%D0%A3%D1%80%D1%83%D0%B1%D0%BB%D0%B5%D1%9E%D1%81%D0%BA%D1%96"
    },
    {
        "id": "yagaila",
        "name": {
            "by": "Уладзіслаў II Ягайла",
            "ru": "Владислав II Ягайло",
            "en": "Władysław II Jagiełło (Jogaila)"
        },
        "years": "каля 1352/1362–1434",
        "role": {
            "by": "Вялікі князь літоўскі (1377–1434), кароль польскі (1386–1434), заснавальнік дынастыі Ягелонаў",
            "ru": "Великий князь литовский (1377–1434), король польский (1386–1434), основатель династии Ягеллонов",
            "en": "Grand Duke of Lithuania (1377–1434), King of Poland (1386–1434), founder of the Jagiellonian dynasty"
        },
        "bio": {
            "by": "Сын вялікага князя Альгерда і цвярской князёўны Ульяны. Вялікі князь літоўскі і кароль польскі, пераможца Тэўтонскага ордэна ў Грунвальдскай бітве 1410 г. разам з стрыечным братам Вітаўтам. Родапачынальнік каралеўскай дынастыі Ягелонаў, якая кіравала землямі ВКЛ, Польшчы, Чэхіі і Венгрыі.",
            "ru": "Сын Ольгерда и Ульяны Тверской. Великий князь литовский и король польский, победитель Тевтонского ордена в Грюнвальдской битве 1410 года. Основатель династии Ягеллонов.",
            "en": "Son of Algirdas and Uliana of Tver. Grand Duke of Lithuania and King of Poland. Victor over the Teutonic Order at Grunwald (1410) alongside Vytautas. Founder of the Jagiellonian dynasty."
        },
        "photo": "https://upload.wikimedia.org/wikipedia/commons/4/4b/W%C5%82adys%C5%82aw_II_Jagie%C5%82%C5%82o.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%AF%D0%B3%D0%B0%D0%B9%D0%BB%D0%B0"
    },
    {
        "id": "kazimir-iv-yagelonchyk",
        "name": {
            "by": "Казімір IV Ягелончык",
            "ru": "Казимир IV Ягеллончик",
            "en": "Casimir IV Jagiellon"
        },
        "years": "1427–1492",
        "role": {
            "by": "Вялікі князь літоўскі (1440–1492), кароль польскі (1447–1492)",
            "ru": "Великий князь литовский (1440–1492), король польский (1447–1492)",
            "en": "Grand Duke of Lithuania (1440–1492), King of Poland (1447–1492)"
        },
        "bio": {
            "by": "Малодшы сын Ягайлы і Соф'і Гальшанскай. Аўтар знакамітага Судзебніка 1468 г. — першага збору законаў ВКЛ на старабеларускай мове. Умацаваў аўтаномію і моц Вялікага Княства Літоўскага. Пахаваны ў капліцы Святога Крыжа Вавельскага сабора ў Кракаве пад шэдэўральным саркафагам работы Файта Штоса.",
            "ru": "Младший сын Ягайло и Софьи Гольшанской. Издал Судебник 1468 г. — первый свод законов ВКЛ на старобелорусском языке. Укрепил Великое Княжество Литовское. Похоронен на Вавеле в Кракове.",
            "en": "Younger son of Jogaila and Sophia of Holszany. Issued the Code of 1468 (Sudiebnik), the first codification of GDL law in Ruthenian/Old Belarusian. Buried at Wawel Cathedral under Veit Stoss's tomb."
        },
        "photo": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Kazimierz_IV_Jagiello%C5%84czyk.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%9A%D0%B0%D0%B7%D1%96%D0%BC%D1%96%D1%80_%D0%AF%D0%B3%D0%B5%D0%BB%D0%BE%D0%BD%D1%87%D1%8B%D0%BA"
    },
    {
        "id": "aleksandr-yagelonchyk",
        "name": {
            "by": "Аляксандр Ягелончык",
            "ru": "Александр Ягеллончик",
            "en": "Alexander Jagiellon"
        },
        "years": "1461–1506",
        "role": {
            "by": "Вялікі князь літоўскі (1492–1506), кароль польскі (1501–1506)",
            "ru": "Великий князь литовский (1492–1506), король польский (1501–1506)",
            "en": "Grand Duke of Lithuania (1492–1506), King of Poland (1501–1506)"
        },
        "bio": {
            "by": "Чацвёрты сын Казіміра IV Ягелончыка. Пастаянна жыў у Вільні, пашырыў прывілеі шляхты ВКЛ, апекаваў мастацтва і дойлідства (у т.л. касцёл Святой Ганны). Адзіны з польскіх каралёў і вялікіх князёў літоўскіх эпохі Рэнесансу, які пахаваны ў Каралеўскай крыпце Віленскага кафедральнага сабора.",
            "ru": "Сын Казимира IV. Жил в Вильнюсе, расширил привилегии шляхты ВКЛ, поддерживал культуру. Единственный монарх, похороненный в королевской крипте Вильнюсского собора.",
            "en": "Son of Casimir IV. Resided in Vilnius, expanded rights of GDL nobility. The only Polish king and Grand Duke buried in the Royal Crypt of Vilnius Cathedral."
        },
        "photo": "https://upload.wikimedia.org/wikipedia/commons/5/54/Aleksander_Jagiellonczyk_%2876851933%29_%28cropped%29.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%90%D0%BB%D1%8F%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%AF%D0%B3%D0%B5%D0%BB%D0%BE%D0%BD%D1%87%D1%8B%D0%BA"
    },
    {
        "id": "stefan-batory",
        "name": {
            "by": "Стэфан Баторый",
            "ru": "Стефан Баторий",
            "en": "Stephen Báthory"
        },
        "years": "1533–1586",
        "role": {
            "by": "Кароль польскі і вялікі князь літоўскі (1576–1586), князь трансільванскі",
            "ru": "Король польский и великий князь литовский (1576–1586), князь трансильванский",
            "en": "King of Poland and Grand Duke of Lithuania (1576–1586), Prince of Transylvania"
        },
        "bio": {
            "by": "Адзін з найбольш значных манархаў у гісторыі Беларусі і Рэчы Паспалітай. Зрабіў Гродна сваёй фактычнай каралеўскай рэзідэнцыяй, перабудаваўшы Стары замак. Вызваліў Полацк ад войскаў Івана Жахлівага (1579). Заснаваў Віленскі ўніверсітэт (Акадэмію). Пахаваны ў Вавельскім саборы ў Кракаве.",
            "ru": "Король польский и великий князь литовский. Сделал Гродно своей фактической резиденцией. Освободил Полоцк в 1579 г., основал Виленский университет. Похоронен на Вавеле в Кракове.",
            "en": "King of Poland and Grand Duke of Lithuania. Made Hrodna his de facto royal residence. Liberated Polatsk (1579) and founded Vilnius University. Buried at Wawel Cathedral."
        },
        "photo": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Stefan_Batory_portrait.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%A1%D1%82%D1%8D%D1%84%D0%B0%D0%BD_%D0%91%D0%B0%D1%82%D0%BE%D1%80%D1%8B%D0%B9"
    },
    {
        "id": "yan-iii-sabeski",
        "name": {
            "by": "Ян III Сабескі",
            "ru": "Ян III Собеский",
            "en": "John III Sobieski"
        },
        "years": "1629–1696",
        "role": {
            "by": "Кароль польскі і вялікі князь літоўскі (1674–1696), палкаводзец",
            "ru": "Король польский и великий князь литовский (1674–1696), полководец",
            "en": "King of Poland and Grand Duke of Lithuania (1674–1696), military commander"
        },
        "bio": {
            "by": "Выдатны палкаводзец, пераможца бітвы пад Хоцінам (1673) і знакамітай бітвы пад Венай (1683), дзе аб'яднаныя сілы Рэчы Паспалітай і саюзнікаў спынілі асманскую экспансію ў Еўропу. Рэгулярна склікаў соймы ў Гродне. Пахаваны ў Вавельскім саборы ў Кракаве.",
            "ru": "Выдающийся полководец, победитель при Хотине и Венской битве 1683 года. Регулярно проводил сеймы в Гродно. Похоронен на Вавеле.",
            "en": "King of Poland and Grand Duke of Lithuania, commander who routed the Ottoman army at the Battle of Vienna (1683). Buried at Wawel Cathedral."
        },
        "photo": "https://upload.wikimedia.org/wikipedia/commons/6/67/Jan_III_Sobieski_in_karacena.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%AF%D0%BD_III_%D0%A1%D0%B0%D0%B1%D0%B5%D1%81%D0%BA%D1%96"
    },
    {
        "id": "stanislaw-august-poniatowski",
        "name": {
            "by": "Станіслаў Аўгуст Панятоўскі",
            "ru": "Станислав Август Понятовский",
            "en": "Stanisław August Poniatowski"
        },
        "years": "1732–1798",
        "role": {
            "by": "Апошні кароль польскі і вялікі князь літоўскі (1764–1795)",
            "ru": "Последний король польский и великий князь литовский (1764–1795)",
            "en": "Last King of Poland and Grand Duke of Lithuania (1764–1795)"
        },
        "bio": {
            "by": "Ураджэнец мястэчка Воўчын (цяпер Камянецкі раён Брэсцкай вобласці). Апошні манарх Рэчы Паспалітай і Вялікага Княства Літоўскага. Мецэнат Асветніцтва, ініцыятар прыняцця Канстытуцыі 3 мая 1791 г. і стварэння Камісіі нацыянальнай адукацыі. Саркафаг манарха спачывае ў крыпце архікатэдры Святога Яна ў Варшаве.",
            "ru": "Уроженец местечка Волчин (Брестская область). Последний монарх Речи Посполитой и ВКЛ. Меценат Просвещения, инициатор Конституции 3 мая 1791 года. Саркофаг покоится в соборе Св. Яна в Варшаве.",
            "en": "Born in Voŭčyn (Brest region, Belarus). Last monarch of the Polish-Lithuanian Commonwealth and GDL. Patron of Enlightenment and initiator of the Constitution of May 3, 1791. Buried in St. John's Archcathedral in Warsaw."
        },
        "photo": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Stanislaw_poniatowski_bacciarelli.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%A1%D1%82%D0%B0%D0%BD%D1%96%D1%81%D0%BB%D0%B0%D1%9E_%D0%90%D1%9E%D0%B3%D1%83%D1%81%D1%82_%D0%9F%D0%B0%D0%BD%D1%8F%D1%82%D0%BE%D1%9E%D1%81%D0%BA%D1%96"
    },
    {
        "id": "sofia-menskaya",
        "name": {
            "by": "Сафія Валадараўна (Сафія Менская)",
            "ru": "София Володаревна (София Минская)",
            "en": "Sophia of Minsk (Queen of Denmark)"
        },
        "years": "каля 1140–1198",
        "role": {
            "by": "Князёўна менская, каралева Даніі (1157–1182)",
            "ru": "Княжна минская, королева Дании (1157–1182)",
            "en": "Princess of Minsk, Queen of Denmark (1157–1182)"
        },
        "bio": {
            "by": "Дачка менскага князя Валадара Глебавіча і польскай княгіні Рыксы. Каралева Даніі, жонка дацкага караля Вальдэмара I Вялікага. Маці каралёў Кнуда VI і Вальдэмара II Пераможцы, а таксама каралевы Францыі Інгеборгі. Пахаваная побач з мужам у каралеўскім пантэоне — царкве Святога Бендта ў Рынгстэдзе, Данія.",
            "ru": "Дочь минского князя Володаря Глебовича. Королева Дании, супруга короля Вальдемара I Великого. Мать королей Кнуда VI и Вальдемара II. Похоронена в церкви Св. Бендта в Рингстеде.",
            "en": "Daughter of Prince Valadar of Minsk and Rikissa of Poland. Queen consort of Denmark as wife of Valdemar I the Great. Mother of Danish kings Canute VI and Valdemar II. Buried at St. Bendt's Church in Ringsted, Denmark."
        },
        "photo": "https://upload.wikimedia.org/wikipedia/commons/5/59/Sankt_Bendts_Kirke_-_Sophia.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%A1%D0%B0%D1%84%D1%96%D1%8F_%D0%92%D0%B0%D0%BB%D0%B0%D0%B4%D0%B0%D1%80%D0%B0%D1%9E%D0%BD%D0%B0"
    },
    {
        "id": "zhygimont-ii-august",
        "name": {
            "by": "Жыгімонт II Аўгуст",
            "ru": "Сигизмунд II Август",
            "en": "Sigismund II Augustus"
        },
        "years": "1520–1572",
        "role": {
            "by": "Вялікі князь літоўскі і кароль польскі (1548–1572)",
            "ru": "Великий князь литовский и король польский (1548–1572)",
            "en": "Grand Duke of Lithuania and King of Poland (1548–1572)"
        },
        "bio": {
            "by": "Апошні манарх з дынастыі Ягелонаў па мужчынскай лініі. Правёў Аграрную рэформу (Валочная памера). Ажаніўся па каханні з Барбарай Радзівіл насуперак волі маці Боны Сфорцы і шляхты. Падпісаў Люблінскую унію 1569 г. Пахаваны ў Жыгімонтаўскай капліцы Вавельскага сабора ў Кракаве.",
            "ru": "Последний монарх из династии Ягеллонов. Провёл волочную померу. Женился по любви на Барбаре Радзивилл. Подписал Люблинскую унию. Похоронен на Вавеле.",
            "en": "Last monarch of the Jagiellonian dynasty in male line. Conducted the Volok Reform. Married Barbara Radziwiłł for love. Signed the Union of Lublin (1569). Buried in Sigismund Chapel at Wawel."
        },
        "photo": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Cranach_the_Younger_Sigismund_II_Augustus.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%96%D1%8B%D0%B3%D1%96%D0%BC%D0%BE%D0%BD%D1%82_II_%D0%90%D1%9E%D0%B3%D1%83%D1%81%D1%82"
    },
    {
        "id": "fabian-abrantovich",
        "name": {
            "by": "Архімандрыт Фабіян Абрантовіч",
            "ru": "Архимандрит Фабиан Абрантович",
            "en": "Archimandrite Fabian Abrantovich"
        },
        "years": "1884–1946",
        "role": {
            "by": "Беларускі рэлігійны і грамадскі дзеяч, філосаф, першаіерарх місіі ў Харбіне",
            "ru": "Белорусский религиозный и общественный деятель, философ, глава миссии в Харбине",
            "en": "Belarusian Catholic religious leader, philosopher, head of Harbin Byzantine Mission"
        },
        "bio": {
            "by": "Ураджэнец Навагрудчыны. Доктар філасофіі, святар кангрэгацыі марыянаў (MIC). Адзін з заснавальнікаў Хрысціянска-дэмакратычнай злучнасці ў Петраградзе (1917). У 1928–1939 гг. — апостальскі адміністратар і кіраўнік Беларускай каталіцкай місіі візантыйска-славянскага абраду ў Харбіне (Кітай), заснавальнік ліцэя Святога Мікалая. У 1939 г. падчас візіту ў Беларусь арыштаваны НКУС. Загінуў пасля катаванняў у Бутырскай турме ў Маскве ў 1946 г.",
            "ru": "Уроженец Новогрудчины. Доктор философии, марианин. Руководитель Белорусской католической миссии восточного обряда в Харбине (Китай, 1928–1939). Арестован НКВД в 1939 г., погиб в Бутырской тюрьме в Москве.",
            "en": "Born in Novogrudok district. Marian priest, Doctor of Philosophy. Head of the Byzantine Catholic Mission in Harbin, Manchuria (1928–1939). Arrested by Soviets in 1939, died in Butyrka prison in Moscow in 1946."
        },
        "photo": "https://upload.wikimedia.org/wikipedia/commons/4/46/Fabian_Abrantowicz.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%A4%D0%B0%D0%B1%D1%96%D1%8F%D0%BD_%D0%90%D0%B1%D1%80%D0%B0%D0%BD%D1%82%D0%BE%D0%B2%D1%96%D1%87"
    },
    {
        "id": "andrei-tsikota",
        "name": {
            "by": "Архімандрыт Андрэй Цікота",
            "ru": "Архимандрит Андрей Цикото",
            "en": "Archimandrite Andrei Tsikota"
        },
        "years": "1891–1952",
        "role": {
            "by": "Генеральны настаяцель айцоў марыянаў (Рым), экзарх Харбіна, мучанік ГУЛАГу",
            "ru": "Генеральный настоятель мариан (Рим), экзарх Харбина, мученик ГУЛАГа",
            "en": "Superior General of the Marian Fathers (Rome), Apostolic Administrator in Harbin, Gulag martyr"
        },
        "bio": {
            "by": "Ураджэнец Смаргоншчыны. Член Рады БНР, дзеяч беларускага хрысціянскага адраджэння. Генеральны суперыёр ордэна марыянаў у Рыме (1933–1939), затым апостальскі адміністратар у Харбіне (Кітай, 1939–1948). У снежні 1948 г. арыштаваны кітайскімі камуністамі, перададзены савецкаму МДБ, асуджаны на 25 гадоў ГУЛАГу. Загінуў у лагерным шпіталі Азярлагу (Новачунка каля Тайшэта). Працягваецца працэс беатыфікацыі.",
            "ru": "Уроженец Сморгонщины. Член Рады БНР. Генеральный супериор мариан в Риме, экзарх Харбина (1939–1948). Арестован в Китае, передан СССР, погиб в Озерлаге (Тайшет).",
            "en": "Born in Smorgon region. Member of BNR Council. Superior General of Marian Fathers in Rome (1933–1939), Apostolic Administrator in Harbin (1939–1948). Arrested in 1948, died in Ozerlag Gulag hospital near Tayshet in 1952."
        },
        "photo": "https://upload.wikimedia.org/wikipedia/commons/c/c7/%D0%90%D0%B9%D1%86%D0%B5%D1%86_%D0%90%D0%BD%D0%B4%D1%8D%D0%B9_%D0%A6%D1%96%D0%BA%D0%BE%D1%82%D0%B0.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%90%D0%BD%D0%B4%D1%80%D1%8D%D0%B9_%D0%A6%D1%96%D0%BA%D0%BE%D1%82%D0%B0"
    },
    {
        "id": "yazep-hermanovich",
        "name": {
            "by": "Язэп Германовіч (Вінцук Адважны)",
            "ru": "Иосиф Германович (Винцук Адважный)",
            "en": "Yazep Hermanovich (Vintsyuk Advazhny)"
        },
        "years": "1890–1978",
        "role": {
            "by": "Грэка-каталіцкі святар (марыянін), паэт, пісьменнік, аўтар успамінаў пра ГУЛАГ",
            "ru": "Греко-католический священник, поэт, писатель, узник ГУЛАГа",
            "en": "Greek Catholic priest (Marian father), poet, writer, author of Gulag memoirs"
        },
        "bio": {
            "by": "Ураджэнец Гальшанаў. Беларускі паэт і публіцыст (псеўданім Вінцук Адважны). Працаваў у Друйскай гімназіі, затым у місіі ў Харбіне (Кітай) і дырэктарам Ліцэя Св. Мікалая. У 1948 г. арыштаваны савецкімі органамі ў Харбіне, адбыў катаргу ў лагерах Тайшэта (1948–1955). Аўтар знакамітай кнігі «Кітай – Сібір – Масква (Успаміны спаведніка і мучаніка)». Пазней жыў і служыў у Беларускім доме марыянаў у Лондане.",
            "ru": "Уроженец Гольшан. Белорусский поэт и священник-марианин. Работал в Харбине (директор лицея Св. Николая). Прошёл лагеря Тайшета. Автор книги «Китай – Сибирь – Москва». Позже жил в Лондоне.",
            "en": "Born in Halshany. Belarusian poet and Marian priest. Directed St. Nicholas Lyceum in Harbin. Spent 1948–1955 in Siberian Gulag camps. Author of 'China – Siberia – Moscow'. Later served at the Marian House in London."
        },
        "photo": "https://upload.wikimedia.org/wikipedia/commons/3/3d/Jazep_Hiermanovi%C4%8D._%D0%AF%D0%B7%D1%8D%D0%BF_%D0%93%D0%B5%D1%80%D0%BC%D0%B0%D0%BD%D0%BE%D0%B2%D1%96%D1%87_%281932%29.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%AF%D0%B7%D1%8D%D0%BF_%D0%A1%D1%82%D0%B0%D0%BD%D1%96%D1%81%D0%BB%D0%B0%D0%B2%D0%B0%D0%B2%D1%96%D1%87_%D0%93%D0%B5%D1%80%D0%BC%D0%B0%D0%BD%D0%BE%D0%B2%D1%96%D1%87"
    }
]

for p in new_persons:
    persons_map[p['id']] = p

# -------------------------------------------------------------
# 2. FIX EXISTING PLACES
# -------------------------------------------------------------

# Fix vilnia-kvatera-samoyly
if 'vilnia-kvatera-samoyly' in places_map:
    p = places_map['vilnia-kvatera-samoyly']
    p['personId'] = 'uladzimir-samoila'
    p['personIds'] = ['uladzimir-samoila']
    p['description']['by'] = (
        "Адрас: Liejyklos, 10/13.\n\n"
        "Тут у 1920-х – пачатку 1930-х у «маленечкай аднапакаёвай кватэры амаль на падстрэшшы» "
        "разам з жонкай і сынам жыў адзін з пачынальнікаў адраджэнскага руху Уладзімір Самойла. "
        "Літаратуразнаўца і публіцыст, Самойла першым ацаніў у друку творчасць Янкі Купалы. "
        "Ён выкладаў у Беларускай віленскай гімназіі, працаваў бібліятэкарам Віленскага беларускага "
        "музея імя І. Луцкевіча, актыўна выступаў у друку. За шматгадовую ахвярную дзейнасць на ніве "
        "беларушчыны быў арыштаваны органамі НКУС пасля прыходу ў Вільню Чырвонай арміі ў 1939 г. "
        "ды згінуў у савецкіх засценках."
    )
    p['description']['ru'] = (
        "Адрес: Liejyklos, 10/13.\n\n"
        "Здесь в 1920-х – начале 1930-х жил публицист, философ и литературовед Владимир Самойло. "
        "Самойло первым в печати высоко оценил поэзию Янки Купалы. Преподавал в Виленской белорусской "
        "гимназии, работал в Белорусском музее им. И. Луцкевича. Арестован НКВД в 1939 году и погиб в заключении."
    )
    p['description']['en'] = (
        "Address: Liejyklos, 10/13.\n\n"
        "Here in the 1920s and early 1930s lived Uladzimir Samoila, a publicist, literary critic, and philosopher. "
        "Samoila was the first to recognize and review the poetry of Yanka Kupala in print. He taught at the Vilnius "
        "Belarusian Gymnasium and worked at the Ivan Lutskievich Museum. Arrested by the Soviet NKVD in 1939, he died in custody."
    )

# Fix vilnia-bibliyateka-akademii-navuk-litvy-imya-urublew
if 'vilnia-bibliyateka-akademii-navuk-litvy-imya-urublew' in places_map:
    p = places_map['vilnia-bibliyateka-akademii-navuk-litvy-imya-urublew']
    p['personId'] = 'tadevush-urubleuski'
    p['personIds'] = ['tadevush-urubleuski', 'valery-urubleuski']
    p['description']['by'] = (
        "Адрас: Žygimantų, 1/8.\n\n"
        "Бібліятэка Акадэміі навук Літвы імя Урублеўскіх паўстала на аснове ўнікальнага сямейнага збору "
        "кніг і рукапісаў, які налічваў дзясяткі тысяч рэдкіх выданняў, старадрукаў і дакументаў.\n\n"
        "Заснавальнік бібліятэкі — знакаміты віленскі юрыст і адвакат Тадэвуш Урублеўскі, які ў царскіх судах "
        "бясплатна абараняў дзеячаў беларускага нацыянальнага руху (Цётку, Аляксандра Уласава, актывістаў БСГ). "
        "Ягоны родны дзядзька Валеры Урублеўскі быў паплечнікам Кастуся Каліноўскага, камандуючым паўстаннем 1863 г. "
        "і генералам Парыжскай Камуны."
    )
    p['description']['ru'] = (
        "Адрес: Žygimantų, 1/8.\n\n"
        "Библиотека Академии наук Литвы им. Врублевских возникла на основе частного собрания Тадеуша Врублевского. "
        "Врублевский был выдающимся адвокатом, защищавшим деятелей белорусского движения. Его дядя Валерий Врублевский "
        "был соратником Калиновского в восстании 1863 года и генералом Парижской Коммуны."
    )
    p['description']['en'] = (
        "Address: Žygimantų, 1/8.\n\n"
        "The Wroblewski Library of the Lithuanian Academy of Sciences was established from the private collection "
        "of Tadeusz Wróblewski, a distinguished Vilnius attorney who defended Belarusian national revival figures in court. "
        "His uncle Walery Antoni Wróblewski was a prominent leader of the 1863 Uprising and General of the Paris Commune."
    )

# Fix vilnia-dom-urublewskaha
if 'vilnia-dom-urublewskaha' in places_map:
    p = places_map['vilnia-dom-urublewskaha']
    p['personId'] = 'tadevush-urubleuski'
    p['personIds'] = ['tadevush-urubleuski']

# -------------------------------------------------------------
# 3. NEW PLACES (Père Lachaise, Monarchs, Harbin & Clergy)
# -------------------------------------------------------------

new_places = [
    {
        "id": "paris-pere-lachaise-valery-wroblewski-grave",
        "title": {
            "by": "Магіла генерала Валерыя Урублеўскага на могілках Пер-Лашэз",
            "ru": "Могила генерала Валерия Врублевского на кладбище Пер-Лашез",
            "en": "Grave of General Walery Wróblewski at Père Lachaise Cemetery"
        },
        "category": "grave",
        "country": {"by": "Францыя", "ru": "Франция", "en": "France"},
        "city": {"by": "Парыж", "ru": "Париж", "en": "Paris"},
        "coordinates": [48.86016, 2.39801],
        "description": {
            "by": "Адрас: Cimetière du Père-Lachaise, Division 76.\n\nТут спачывае генерал Валеры Антоній Урублеўскі (1836–1908) — ураджэнец мястэчка Жалудок на Гарадзеншчыне, найбліжэйшы паплечнік Кастуся Каліноўскага і начальнік паўстанцкіх сілаў Гарадзенскага ваяводства ў паўстанні 1863–1864 гадоў. Пасля эміграцыі ў Францыю стаў адным з галоўных военачальнікаў і генералам Парыжскай Камуны 1871 г., камандуючы абаронай левага берага Сены. Помнік усталяваны недалёка ад Сцяны Камунараў.",
            "ru": "Адрес: Cimetière du Père-Lachaise, Division 76.\n\nЗдесь похоронен генерал Валерий Антоний Врублевский (1836–1908) — уроженец местечка Желудок на Гродненщине, соратник Кастуся Калиновского и командующий повстанцами Гродненского воеводства в 1863–1864 гг. Позже генерал Парижской Коммуны, командовавший обороной левого берега Сены.",
            "en": "Address: Père Lachaise Cemetery, Division 76.\n\nGrave and monument of General Walery Antoni Wróblewski (1836–1908), born in Žaludok near Hrodna. Close associate of Kastuś Kalinoŭski and military commander of Hrodna voivodeship during the 1863–1864 Uprising. In France, he became a renowned military leader and General of the Paris Commune (1871). Located near the Mur des Fédérés."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/d/d1/P%C3%A8re-Lachaise_-_Division_76_-_Wroblewski_03.jpg",
        "links": [
            {
                "title": "Вікіпедыя: Валерый Антоній Урублеўскі",
                "url": "https://be.wikipedia.org/wiki/%D0%92%D0%B0%D0%BB%D0%B5%D1%80%D1%8B%D0%B9_%D0%90%D0%BD%D1%82%D0%BE%D0%BD%D1%96%D0%B9_%D0%A3%D1%80%D1%83%D0%B1%D0%BB%D0%B5%D1%9E%D1%81%D0%BA%D1%96"
            }
        ],
        "tags": ["Францыя", "Парыж", "Паўстанне 1863", "Пер-Лашэз", "grave"],
        "personId": "valery-urubleuski",
        "personIds": ["valery-urubleuski"],
        "mustSee": True
    },
    {
        "id": "krakow-wawel-cathedral-royal-pantheon",
        "title": {
            "by": "Кафедральны сабор на Вавелі — Каралеўскі пантэон манархаў ВКЛ",
            "ru": "Кафедральный собор на Вавеле — Королевский пантеон монархов ВКЛ",
            "en": "Wawel Cathedral Royal Pantheon — Monarchs of GDL"
        },
        "category": "grave",
        "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
        "city": {"by": "Кракаў", "ru": "Краков", "en": "Kraków"},
        "coordinates": [50.0545, 19.9354],
        "description": {
            "by": "Адрас: Wawel 3, Kraków.\n\nКафедральны сабор Святых Станіслава і Вацлава на Вавелі — галоўны каралеўскі некропаль манархаў Вялікага Княства Літоўскага і Рэчы Паспалітай. Тут знаходзяцца саркафагі і капліцы:\n• Уладзіслава II Ягайлы ( Jogaila ) — цудоўны гатычны саркафаг з чырвонага мармуру;\n• Казіміра IV Ягелончыка — шэдэўр сусветнага мастацтва работы Файта Штоса (1492 г.);\n• Каралевы Соф'і Гальшанскай (маці Ягелонаў, Капліца Святой Тройцы);\n• Жыгімонта I Старога і Жыгімонта II Аўгуста (знакамітая Рэнесансная Жыгімонтаўская капліца);\n• Стэфана Баторыя (надмагілле Санці Гучы ў Капліцы Маці Божай);\n• Каралёў з дынастыі Вазаў і Яна III Сабескага.",
            "ru": "Адрес: Wawel 3, Kraków.\n\nВавельский собор — главный королевский некрополь монархов Великого Княжества Литовского и Речи Посполитой. Здесь находятся надгробия Ягайло, Казимира IV Ягеллончика (шедевр Фейта Штосса 1492 г.), королевы Софьи Гольшанской, Сигизмунда II Августа, Стефана Батория и Яна III Собеского.",
            "en": "Address: Wawel 3, Kraków.\n\nThe Royal Archcathedral Basilica at Wawel is the principal royal necropolis of the monarchs of the Grand Duchy of Lithuania and the Polish-Lithuanian Commonwealth. Houses the tombs of Władysław II Jagiełło, Casimir IV Jagiellon (masterpiece by Veit Stoss, 1492), Queen Sophia of Holszany, Sigismund II Augustus, Stephen Báthory, and John III Sobieski."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/7/76/Wawel_Cathedral_Front.jpg",
        "links": [
            {
                "title": "Wawel Royal Cathedral",
                "url": "https://www.katedra-wawelska.pl/"
            }
        ],
        "tags": ["Польшча", "Кракаў", "Вавель", "Манархі ВКЛ", "Ягелоны", "grave"],
        "personId": "yagaila",
        "personIds": ["yagaila", "kazimir-iv-yagelonchyk", "zhygimont-ii-august", "stefan-batory", "yan-iii-sabeski"],
        "mustSee": True
    },
    {
        "id": "vilnius-cathedral-royal-crypt",
        "title": {
            "by": "Каралеўская крыпта Віленскага кафедральнага сабора",
            "ru": "Королевская крипта Вильнюсского кафедрального собора",
            "en": "Royal Crypt of Vilnius Cathedral"
        },
        "category": "grave",
        "country": {"by": "Літва", "ru": "Литва", "en": "Lithuania"},
        "city": {"by": "Вільня", "ru": "Вильнюс", "en": "Vilnius"},
        "coordinates": [54.6858, 25.2877],
        "description": {
            "by": "Адрас: Katedros a. 2, Vilnius.\n\nПад барочнай капліцай Святога Казіміра знаходзіцца Каралеўская крыпта (Karališkoji kripta). Тут спачывае вялікі князь літоўскі і кароль польскі Аляксандр Ягелончык (1461–1506) — адзіны манарх, пахаваны ў Вільні. Таксама тут захоўваецца сэрца караля і вялікага князя Уладзіслава IV Вазы, саркафагі Барбары Радзівіл і Лізаветы Габсбург (жонкі Жыгімонта Аўгуста), а таксама мемарыял вялікага князя Вітаўта Вялікага.",
            "ru": "Адрес: Katedros a. 2, Vilnius.\n\nПод капеллой Святого Казимира расположена Королевская крипта, где покоится великий князь литовский и король Александр Ягеллончик — единственный монарх, похороненный в Вильнюсе. Также здесь хранится урна с сердцем Владислава IV Вазы, саркофаги Барбары Радзивилл и Елизаветы Габсбург.",
            "en": "Address: Katedros a. 2, Vilnius.\n\nBeneath the Chapel of Saint Casimir lies the Royal Crypt of Vilnius Cathedral. It contains the sarcophagus of Alexander Jagiellon (1461–1506), the only monarch buried in Vilnius, the urn with the heart of King Władysław IV Vasa, and the sarcophagus of Barbara Radziwiłł."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/54/Aleksander_Jagiellonczyk_%2876851933%29_%28cropped%29.jpg",
        "links": [
            {
                "title": "Віленскі кафедральны сабор",
                "url": "https://katedra.lt/en/crypts/"
            }
        ],
        "tags": ["Літва", "Вільня", "Кафедра", "Манархі ВКЛ", "grave"],
        "personId": "aleksandr-yagelonchyk",
        "personIds": ["aleksandr-yagelonchyk", "barbara-radziwill"],
        "mustSee": True
    },
    {
        "id": "ringsted-st-bendts-church-sophia-of-minsk",
        "title": {
            "by": "Царква Святога Бендта ў Рынгстэдзе — Магіла каралевы Сафіі Менскай",
            "ru": "Церковь Святого Бендта в Рингстеде — Могила королевы Софии Минской",
            "en": "St. Bendt's Church in Ringsted — Grave of Queen Sophia of Minsk"
        },
        "category": "grave",
        "country": {"by": "Данія", "ru": "Дания", "en": "Denmark"},
        "city": {"by": "Рынгстэд", "ru": "Рингстед", "en": "Ringsted"},
        "coordinates": [55.44194, 11.79056],
        "description": {
            "by": "Адрас: Sct Bendts Kirke, Sct Bendtsgade 9, 4100 Ringsted.\n\nЦарква Святога Бендта ў Рынгстэдзе — найстарэйшая цагляная царква Паўночнай Еўропы і першы каралеўскі пантэон дацкіх манархаў. Тут у каралеўскім пахаванні спачывае Сафія Валадараўна (каля 1140–1198) — князёўна Менская, каралева Даніі, жонка караля Вальдэмара I Вялікага і маці каралёў Кнуда VI і Вальдэмара II. На магільнай пліце і мемарыяльнай дошцы пазначана яе імя (Dronning Sofia).",
            "ru": "Адрес: Sct Bendts Kirke, Ringsted, Denmark.\n\nЦерковь Святого Бендта в Рингстеде — королевская усыпальница датских монархов. Здесь погребена минская княжна София Володаревна (ок. 1140–1198), королева Дании, супруга Вальдемара I Великого и мать королей Кнуда VI и Вальдемара II.",
            "en": "Address: Sct Bendtsgade 9, Ringsted, Denmark.\n\nSt. Bendt's Church is the royal burial site of early Danish monarchs. Here lies Sophia of Minsk (c. 1140–1198), Princess of Minsk, Queen consort of Denmark alongside her husband King Valdemar I the Great. Mother of Danish kings Canute VI and Valdemar II."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/59/Sankt_Bendts_Kirke_-_Sophia.jpg",
        "links": [
            {
                "title": "Вікіпедыя: Сафія Валадараўна",
                "url": "https://be.wikipedia.org/wiki/%D0%A1%D0%B0%D1%84%D1%96%D1%8F_%D0%92%D0%B0%D0%BB%D0%B0%D0%B4%D0%B0%D1%80%D0%B0%D1%9E%D0%BD%D0%B0"
            }
        ],
        "tags": ["Данія", "Рынгстэд", "Полацкае княства", "Менск", "Каралева Даніі", "grave"],
        "personId": "sofia-menskaya",
        "personIds": ["sofia-menskaya"],
        "mustSee": True
    },
    {
        "id": "warsaw-st-john-archcathedral-stanislaw-august-tomb",
        "title": {
            "by": "Архікатэдра Святога Яна ў Варшаве — Саркафаг Станіслава Аўгуста Панятоўскага",
            "ru": "Архикафедральный собор Святого Иоанна в Варшаве — Саркофаг Станислава Августа Понятовского",
            "en": "St. John's Archcathedral in Warsaw — Tomb of King Stanisław August Poniatowski"
        },
        "category": "grave",
        "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
        "city": {"by": "Варшава", "ru": "Варшава", "en": "Warsaw"},
        "coordinates": [52.2492, 21.0136],
        "description": {
            "by": "Адрас: Świętojańska 8, Warszawa.\n\nУ крыпце архікатэдры Святога Яна ў Старым горадзе Варшавы знаходзіцца саркафаг апошняга вялікага князя літоўскага і караля польскага Станіслава Аўгуста Панятоўскага (1732–1798), ураджэнца Воўчына на Берасцейшчыне. Пасля складанага гістарычнага шляху (пахаванне ў Пецярбургу, перапахаванне ў родным Воўчыне) у 1995 г. парэшткі манарха былі ўрачыста перанесены ў крыпту варшаўскай архікатэдры.",
            "ru": "Адрес: Świętojańska 8, Warszawa.\n\nВ крипте собора Св. Иоанна покоится саркофаг последнего великого князя литовского и короля Станислава Августа Понятовского (1732–1798), уроженца Волчина под Брестом.",
            "en": "Address: Świętojańska 8, Warsaw.\n\nThe crypt of St. John's Archcathedral holds the sarcophagus of the last Grand Duke of Lithuania and King of Poland, Stanisław August Poniatowski (1732–1798), born in Voŭčyn, Belarus."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/7/70/Bazylika_archikatedralna_%C5%9Bw._Jana_Chrzciciela_w_Warszawie_2020.jpg",
        "links": [
            {
                "title": "Вікіпедыя: Станіслаў Аўгуст Панятоўскі",
                "url": "https://be.wikipedia.org/wiki/%D0%A1%D1%82%D0%B0%D0%BD%D1%96%D1%81%D0%BB%D0%B0%D1%9E_%D0%90%D1%9E%D0%B3%D1%83%D1%81%D1%82_%D0%9F%D0%B0%D0%BD%D1%8F%D1%82%D0%BE%D1%9E%D1%81%D0%BA%D1%96"
            }
        ],
        "tags": ["Польшча", "Варшава", "Панятоўскі", "Манархі ВКЛ", "Воўчын", "grave"],
        "personId": "stanislaw-august-poniatowski",
        "personIds": ["stanislaw-august-poniatowski"],
        "mustSee": True
    },
    {
        "id": "paris-saint-germain-des-pres-jan-casimir-tomb",
        "title": {
            "by": "Абацтва Сен-Жэрмэн-дэ-Прэ — Надмагілле і сэрца караля Яна II Казіміра",
            "ru": "Аббатство Сен-Жермен-де-Пре — Надгробие и сердце короля Яна II Казимира",
            "en": "Saint-Germain-des-Prés Abbey — Tomb and Heart of King John II Casimir"
        },
        "category": "grave",
        "country": {"by": "Францыя", "ru": "Франция", "en": "Paris"},
        "city": {"by": "Парыж", "ru": "Париж", "en": "Paris"},
        "coordinates": [48.8540, 2.3338],
        "description": {
            "by": "Адрас: 3 Place Saint-Germain des Prés, Paris.\n\nУ знакамітай старажытнай царкве абацтва Сен-Жэрмэн-дэ-Прэ знаходзіцца пышнае барочнае надмагілле Яна II Казіміра Вазы (1609–1672) — караля і вялікага князя літоўскага, які пасля адрачэння ад пасаду ў 1668 г. з'ехаў у Францыю і стаў абатам гэтага манастыра. Тут у металічнай урне захоўваецца сэрца манарха, а манументальная скульптура паказвае яго на каленях у малітве.",
            "ru": "Адрес: 3 Place Saint-Germain des Prés, Paris.\n\nВ церкви аббатства Сен-Жермен-де-Пре находится монументальное надгробие короля и великого князя литовского Яна II Казимира Вазы (1609–1672), ставшего после отречения абатом монастыря. Здесь хранится сердце монарха.",
            "en": "Address: 3 Place Saint-Germain des Prés, Paris.\n\nThe famous Abbey church of Saint-Germain-des-Prés houses the monumental Baroque tomb and heart of King and Grand Duke John II Casimir Vasa (1609–1672), who became abbot of the monastery after abdicating the throne."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/9/90/Schultz_-_Portrait_de_Jean-Casimir_Vasa_%281609-1672%29%2C_roi_de_Pologne%2C_puis_abb%C3%A9_de_Saint-Germain-des-Pr%C3%A9s.jpg",
        "links": [
            {
                "title": "Église de Saint-Germain-des-Prés",
                "url": "https://en.wikipedia.org/wiki/Saint-Germain-des-Pr%C3%A9s_(abbey)"
            }
        ],
        "tags": ["Францыя", "Парыж", "Ваза", "Манархі ВКЛ", "grave"],
        "mustSee": False
    },
    {
        "id": "dresden-hofkirche-august-iii-tomb",
        "title": {
            "by": "Кафедральны сабор Найсвяцейшай Тройцы (Хофкірхе) — Пахаванне Аўгуста III",
            "ru": "Собор Хофкирхе в Дрездене — Усыпальница Августа III",
            "en": "Katholische Hofkirche in Dresden — Tomb of King Augustus III"
        },
        "category": "grave",
        "country": {"by": "Германія", "ru": "Германия", "en": "Germany"},
        "city": {"by": "Дрэздэн", "ru": "Дрезден", "en": "Dresden"},
        "coordinates": [51.0535, 13.7374],
        "description": {
            "by": "Адрас: Schloßplatz, Dresden.\n\nУ каралеўскай крыпце Ветынаў кафедральнага сабора Хофкірхе ў Дрэздэне спачывае вялікі князь літоўскі і кароль польскі Аўгуст III (1696–1763) і яго жонка Марыя Жазэфа. Таксама ў крыпце ў адмысловай капсуле захоўваецца сэрца караля і вялікага князя Аўгуста II Моцнага.",
            "ru": "Адрес: Schloßplatz, Dresden.\n\nВ королевской крипте собора Хофкирхе в Дрездене покоится великий князь литовский и король Август III (1696–1763). Также здесь хранится капсула с сердцем Августа II Сильного.",
            "en": "Address: Schloßplatz, Dresden.\n\nThe Wettin Royal Crypt at Dresden Cathedral (Hofkirche) houses the tomb of Grand Duke of Lithuania and King Augustus III (1696–1763) and the capsule containing the heart of Augustus II the Strong."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/2b/Dresden%2C_Katholische_Hofkirche_--_2023_--_9410.jpg",
        "links": [
            {
                "title": "Dresden Hofkirche",
                "url": "https://en.wikipedia.org/wiki/Dresden_Cathedral"
            }
        ],
        "tags": ["Германія", "Дрэздэн", "Ветыны", "Манархі ВКЛ", "grave"],
        "mustSee": False
    },
    {
        "id": "new-york-central-park-king-jagiello",
        "title": {
            "by": "Помнік вялікаму князю і каралю Ягайлу ў Цэнтральным парку Нью-Ёрка",
            "ru": "Памятник великому князю и королю Ягайло в Центральном парке Нью-Йорка",
            "en": "King Jagiello Monument in Central Park, New York"
        },
        "category": "monument",
        "country": {"by": "ЗША", "ru": "США", "en": "USA"},
        "city": {"by": "Нью-Ёрк", "ru": "Нью-Йорк", "en": "New York"},
        "coordinates": [40.7797, -73.9687],
        "description": {
            "by": "Адрас: 79th Street Transverse / Turtle Pond, Central Park, New York.\n\nМанументальны бронзавы конны помнік вялікаму князю літоўскаму і каралю польскаму Уладзіславу II Ягайлу (Jogaila), які трымае над галавой два скрыжаваныя Грунвальдскія мячы. Створаны скульптарам Станіславам Казімірам Астроўскім для польскага павільёна Сусветнай выставы ў Нью-Ёрку 1939 г. У 1945 г. усталяваны ў Цэнтральным парку на беразе сажалкі Цёртл-Понд каля замка Бельведэр.",
            "ru": "Адрес: Central Park, New York.\n\nКонный бронзовый монумент Ягайло, держащему над головой два грюнвальдских меча. Создан скульптором Станиславом Островским для Всемирной выставки 1939 года. Установлен в Центральном парке в 1945 г.",
            "en": "Address: Central Park, near Turtle Pond, New York, NY.\n\nMonumental equestrian bronze statue of Grand Duke of Lithuania and King of Poland Władysław II Jagiełło, brandishing two crossed Grunwald swords over his head. Created by sculptor Stanisław Kazimierz Ostrowski for the 1939 New York World's Fair, erected in Central Park in 1945."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/1/14/Monument_a_King_Jagiello_al_Central_Park.jpg",
        "links": [
            {
                "title": "Central Park: King Jagiello Monument",
                "url": "https://www.centralparknyc.org/monuments/king-jagiello"
            }
        ],
        "tags": ["ЗША", "Нью-Ёрк", "Цэнтральны парк", "Ягайла", "Грунвальд", "monument"],
        "personId": "yagaila",
        "personIds": ["yagaila"],
        "mustSee": True
    },
    {
        "id": "aglona-basilica-mindaugas-memorial",
        "title": {
            "by": "Базіліка ў Аглоне — Помнік каралю Міндоўгу і каралеве Марце",
            "ru": "Базилика в Аглоне — Памятник королю Миндовгу и королеве Марте",
            "en": "Aglona Basilica — Monument to King Mindaugas and Queen Marta"
        },
        "category": "monument",
        "country": {"by": "Латвія", "ru": "Латвия", "en": "Latvia"},
        "city": {"by": "Аглона", "ru": "Аглона", "en": "Aglona"},
        "coordinates": [56.1264, 27.0161],
        "description": {
            "by": "Адрас: Cirīšu iela 8, Aglona, Preiļu novads.\n\nКаля знакамітай Аглонскай базілікі ўсталяваны велічны бронзавы помнік першаму каралю Літвы і стваральніку ВКЛ Міндоўгу і ягонай жонцы каралеве Марце (скульптар Вітаўтас Рукас, 2015 г.). Паводле летапісных звестак і латгальскіх паданняў, каралева Марта паходзіла з гэтых зямель, а пасля забойства ў 1263 г. Міндоўг разам з сынамі быў пахаваны на тэрыторыі сучаснай Аглоны.",
            "ru": "Адрес: Cirīšu iela 8, Aglona.\n\nПамятник основателю ВКЛ королю Миндовгу и его супруге королеве Марте у знаменитой Аглонской базилики (скульптор В. Рукас, 2015). По местным преданиям, Марта происходила из Латгалии, а Миндовг был похоронен в Аглоне.",
            "en": "Address: Cirīšu iela 8, Aglona, Latvia.\n\nBronze monument dedicated to the founder of the Grand Duchy of Lithuania, King Mindaugas, and Queen Marta, unveiled in 2015 near the renowned Aglona Basilica. According to local traditions, Queen Marta was from Latgale and Mindaugas was buried here in 1263."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Veliuona005.JPG",
        "links": [
            {
                "title": "Вікіпедыя: Міндоўг",
                "url": "https://be.wikipedia.org/wiki/%D0%9C%D1%96%D0%BD%D0%B4%D0%BE%D1%9E%D0%B3"
            }
        ],
        "tags": ["Латвія", "Аглона", "Міндоўг", "Манархі ВКЛ", "monument"],
        "mustSee": False
    },
    {
        "id": "veliuona-gediminas-grave-mound",
        "title": {
            "by": "Курган Гедзіміна ў Вялёне (Veliuona)",
            "ru": "Курган Гедимина в Велюоне (Veliuona)",
            "en": "Gediminas Mound in Veliuona"
        },
        "category": "historical",
        "country": {"by": "Літва", "ru": "Литва", "en": "Lithuania"},
        "city": {"by": "Вялёна", "ru": "Велюона", "en": "Veliuona"},
        "coordinates": [55.0747, 23.2753],
        "description": {
            "by": "Адрас: Veliuona, Jurbarko raj.\n\nКурган на маляўнічым высокім беразе Нёмана, дзе паводле Хронікі Быхаўца і старажытных паданняў у 1341 г. гераічна загінуў пры аблозе крыжацкай крэпасці Баербург вялікі князь літоўскі Гедзімін — заснавальнік дынастыі Гедзімінавічаў і новай сталіцы Вільні. На вяршыні кургана ўсталяваны мемарыяльны знак з Калюмнамі Гедзіміна.",
            "ru": "Адрес: Veliuona, Jurbarko raj.\n\nКурган на высоком берегу Немана, где согласно Хронике Быховца в 1341 году погиб в битве с крестоносцами великий князь литовский Гедимин — основатель династии Гедиминовичей.",
            "en": "Address: Veliuona, Jurbarkas district, Lithuania.\n\nA castle mound overlooking the Nemunas river where, according to the Bychowiec Chronicle, Grand Duke Gediminas perished in battle against Teutonic Knights in 1341. Marked by a memorial stone."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Veliuona005.JPG",
        "links": [
            {
                "title": "Вікіпедыя: Гедзімін",
                "url": "https://be.wikipedia.org/wiki/%D0%93%D0%B5%D0%B4%D0%B7%D1%96%D0%BC%D1%96%D0%BD"
            }
        ],
        "tags": ["Літва", "Вялёна", "Гедзімін", "Манархі ВКЛ", "Нёман", "historical"],
        "mustSee": False
    },
    {
        "id": "vienna-kahlenberg-st-joseph-sobieski",
        "title": {
            "by": "Касцёл Святога Юзафа на гары Каленберг — Мемарыял Яна III Сабескага",
            "ru": "Костёл Святого Иосифа на горе Каленберг — Мемориал Яна III Собеского",
            "en": "St. Joseph's Church on Kahlenberg — John III Sobieski Memorial"
        },
        "category": "monument",
        "country": {"by": "Аўстрыя", "ru": "Австрия", "en": "Austria"},
        "city": {"by": "Вена", "ru": "Вена", "en": "Vienna"},
        "coordinates": [48.2758, 16.3347],
        "description": {
            "by": "Адрас: Josefsdorf 38, 1190 Wien.\n\nКасцёл Святога Юзафа на гары Каленберг пад Венай. Менавіта адсюль 12 верасня 1683 г. кароль і вялікі князь Ян III Сабескі камандаваў аб'яднаным войскам Рэчы Паспалітай і саюзнікаў у вырашальнай Венскай бітве, якая спыніла турэцкае нашэсце на Цэнтральную Еўропу. У касцёле створана памятная капліца Сабескага (Sobieski-Kapelle) з карцінамі і мемарыяльнымі дошкамі.",
            "ru": "Адрес: Josefsdorf 38, Wien.\n\nКостёл Святого Иосифа на горе Каленберг, откуда 12 сентября 1683 года Ян III Собеский руководил союзными войсками в победной Венской битве. Внутри действует капелла Собеского.",
            "en": "Address: Josefsdorf 38, Vienna, Austria.\n\nSt. Joseph's Church on Mount Kahlenberg overlooking Vienna, where King and Grand Duke John III Sobieski commanded the allied forces during the Battle of Vienna (1683). Features the Sobieski Memorial Chapel."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/a/a3/Kahlenberg_%28Wien%29_-_Kirche_%281%29.JPG",
        "links": [
            {
                "title": "Kahlenberg Kirche",
                "url": "https://en.wikipedia.org/wiki/Kahlenberg"
            }
        ],
        "tags": ["Аўстрыя", "Вена", "Каленберг", "Сабескі", "monument"],
        "personId": "yan-iii-sabeski",
        "personIds": ["yan-iii-sabeski"],
        "mustSee": True
    },
    {
        "id": "harbin-marian-mission-st-nicholas-lyceum",
        "title": {
            "by": "Беларуская каталіцкая місія і Ліцэй Святога Мікалая ў Харбіне",
            "ru": "Белорусская католическая миссия и Лицей Святого Николая в Харбине",
            "en": "Belarusian Marian Mission and St. Nicholas Lyceum in Harbin"
        },
        "category": "culture",
        "country": {"by": "Кітай", "ru": "Китай", "en": "China"},
        "city": {"by": "Харбін", "ru": "Харбин", "en": "Harbin"},
        "coordinates": [45.7562, 126.6341],
        "description": {
            "by": "Адрас: вуліца Ашыхэ (цяпер Ashihe St), Харбін, Маньчжурыя.\n\nАсяродак Беларускай каталіцкай місіі ўсходняга (візантыйска-славянскага) абраду, заснаванай у 1928 г. архімандрытам Фабіянам Абрантовічам. У 1929 г. тут быў адкрыты знакаміты мужчынскі Ліцэй імя Святога Мікалая, канвікт (інтэрнат), прытулак для сірот і манастыр сясцёр-уршулянак. У 1930–1940-х гг. місіяй кіравалі архімандрыт Андрэй Цікота і святар-паэт Язэп Германовіч (Вінцук Адважны). Місія стала цэнтрам адукацыі, культуры і беларускай прысутнасці на Далёкім Усходзе да захопу Маньчжурыі савецкімі войскамі.",
            "ru": "Адрес: Ashihe St, Харбин, Китай.\n\nЦентр Белорусской католической миссии восточного обряда и Лицей Святого Николая, основанные архимандритом Фабианом Абрантовичем в 1928 году. Миссией руководили Андрей Цикото и поэт Язеп Германович.",
            "en": "Address: Ashihe St, Harbin, China.\n\nCenter of the Belarusian Byzantine-Slavic Catholic Mission and St. Nicholas Lyceum, established in Harbin in 1928 by Archimandrite Fabian Abrantovich. Later led by Archimandrite Andrei Tsikota and poet Yazep Hermanovich, serving as a beacon of education and Belarusian culture in the Far East."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/3d/Jazep_Hiermanovi%C4%8D._%D0%AF%D0%B7%D1%8D%D0%BF_%D0%93%D0%B5%D1%80%D0%BC%D0%B0%D0%BD%D0%BE%D0%B2%D1%96%D1%87_%281932%29.jpg",
        "links": [
            {
                "title": "Вікіпедыя: Беларусы Кітая",
                "url": "https://be.wikipedia.org/wiki/%D0%91%D0%B5%D0%BB%D0%B0%D1%80%D1%83%D1%81%D1%8B_%D0%9A%D1%96%D1%82%D0%B0%D1%8F"
            }
        ],
        "tags": ["Кітай", "Харбін", "Марыяне", "Беларусы Кітая", "culture"],
        "personId": "fabian-abrantovich",
        "personIds": ["fabian-abrantovich", "andrei-tsikota", "yazep-hermanovich"],
        "mustSee": True
    },
    {
        "id": "moscow-butyrka-fabian-abrantovich-martyrdom",
        "title": {
            "by": "Бутырская турма — Месца гібелі архімандрыта Фабіяна Абрантовіча",
            "ru": "Бутырская тюрьма — Место гибели архимандрита Фабиана Абрантовича",
            "en": "Butyrka Prison — Martyrdom Site of Archimandrite Fabian Abrantovich"
        },
        "category": "historical",
        "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
        "city": {"by": "Масква", "ru": "Москва", "en": "Moscow"},
        "coordinates": [55.7897, 37.5947],
        "description": {
            "by": "Адрас: вул. Новаслабодская 45, Масква.\n\nБутырская турма — месца зняволення, катаванняў і мучаніцкай смерці выбітнага дзеяча беларускага каталіцкага адраджэння архімандрыта Фабіяна Абрантовіча (1884–1946). Абрантовіч, які ўзначальваў Беларускую місію ў Харбіне, быў схоплены савецкімі спецслужбамі ўвосень 1939 г. на тэрыторыі Заходняй Беларусі і пасля сямі гадоў допытаў і здзекаў загінуў у Бутырцы 2 студзеня 1946 г.",
            "ru": "Адрес: Новослободская ул., 45, Москва.\n\nБутырская тюрьма — место заключения и гибели главы Белорусской католической миссии в Харбине архимандрита Фабиана Абрантовича, умершего в застенках 2 января 1946 г.",
            "en": "Address: Novoslobodskaya St 45, Moscow.\n\nButyrka prison was the site of the imprisonment and martyrdom of Archimandrite Fabian Abrantovich, head of the Belarusian mission in Harbin, who perished in Soviet custody on January 2, 1946."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/7/76/Butyrka_prison_ed.jpg",
        "links": [
            {
                "title": "Вікіпедыя: Фабіян Абрантовіч",
                "url": "https://be.wikipedia.org/wiki/%D0%A4%D0%B0%D0%B1%D1%96%D1%8F%D0%BD_%D0%90%D0%B1%D1%80%D0%B0%D0%BD%D1%82%D0%BE%D0%B2%D1%96%D1%87"
            }
        ],
        "tags": ["Расія", "Масква", "Бутырка", "Рэпрэсіі", "Марыяне", "historical"],
        "personId": "fabian-abrantovich",
        "personIds": ["fabian-abrantovich"],
        "mustSee": False
    },
    {
        "id": "ozerlag-tayshet-novochunka-andrei-tsikota-grave",
        "title": {
            "by": "Лагпункт Азярлагу ў Новачунцы — Магіла архімандрыта Андрэя Цікоты",
            "ru": "Лагпункт Озерлага в Новочунке — Могила архимандрита Андрея Цикото",
            "en": "Ozerlag Camp in Novochunka — Grave of Archimandrite Andrei Tsikota"
        },
        "category": "grave",
        "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
        "city": {"by": "Новачунка", "ru": "Новочунка", "en": "Novochunka"},
        "coordinates": [56.1283, 99.6467],
        "description": {
            "by": "Адрас: станцыя Новачунка, Чунскі раён, Іркуцкая вобласць.\n\nУ савецкім канцлагеры «Азярлаг» (лагерны шпіталь № 038) 13 лютага 1952 г. загінуў архімандрыт Андрэй Цікота — Генеральны настаяцель ордэна марыянаў у Рыме і кіраўнік місіі ў Харбіне. Святара пахавалі на лагерных могілках каля чыгуначнага палатна. У 2003 г. на месцы пахавання каталіцкімі святарамі быў усталяваны мемарыяльны крыж з надпісам «Айцец Андрэй Цікота».",
            "ru": "Адрес: станция Новочунка, Чунский район, Иркутская область.\n\nЗдесь в лагерном госпитале Озерлага 13 февраля 1952 г. погиб архимандрит Андрей Цикото, генеральный настоятель мариан. На лагерном кладбище установлен памятный крест.",
            "en": "Address: Novochunka station, Chunsky district, Irkutsk oblast, Russia.\n\nHere in the Ozerlag Gulag hospital, Archimandrite Andrei Tsikota, Superior General of the Marian Fathers in Rome and head of the Harbin mission, died on February 13, 1952. A memorial cross was erected on the camp burial ground in 2003."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/c/c7/%D0%90%D0%B9%D1%86%D0%B5%D1%86_%D0%90%D0%BD%D0%B4%D1%8D%D0%B9_%D0%A6%D1%96%D0%BA%D0%BE%D1%82%D0%B0.jpg",
        "links": [
            {
                "title": "Вікіпедыя: Андрэй Цікота",
                "url": "https://be.wikipedia.org/wiki/%D0%90%D0%BD%D0%B4%D1%80%D1%8D%D0%B9_%D0%A6%D1%96%D0%BA%D0%BE%D1%82%D0%B0"
            }
        ],
        "tags": ["Расія", "Сібір", "Азярлаг", "Тайшэт", "Марыяне", "ГУЛАГ", "grave"],
        "personId": "andrei-tsikota",
        "personIds": ["andrei-tsikota"],
        "mustSee": False
    },
    {
        "id": "solovki-monastery-gulag-clergy-memorial",
        "title": {
            "by": "Салавецкі лагер асаблівага прызначэння (СЛОН) — Мемарыял рэпрэсаваным святарам",
            "ru": "Соловецкий лагерь особого назначения (СЛОН) — Мемориал репрессированным священникам",
            "en": "Solovki Camp (SLON) — Memorial to Repressed Belarusian Clergy"
        },
        "category": "historical",
        "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
        "city": {"by": "Салаўкі", "ru": "Соловки", "en": "Solovki"},
        "coordinates": [65.0253, 35.7089],
        "description": {
            "by": "Адрас: Салавецкія астравы, Архангельская вобласць.\n\nСалавецкі лагер асаблівага прызначэння (СЛОН), Савацеўскі скіт і Секірная гара — адно з галоўных месцаў зняволення і катаванняў беларускіх каталіцкіх і праваслаўных святароў і вернікаў (даследаваных Леанідам Мараковым). Тут пакутавалі і былі расстраляныя дзесяткі беларускіх святароў (кс. Адам Лісоўскі, кс. Ян Траецкі, кс. Станіслаў Шылько і інш.). На Серафімаўскіх могілках і каля скітоў усталяваны паклонныя крыжы і памятныя знакі.",
            "ru": "Адрес: Соловецкие острова, Архангельская область.\n\nСоловецкий лагерь особого назначения (СЛОН) — место заключения и гибели десятков белорусских священников, задокументированных исследователем Леонидом Моряковым. Установлены поклонные кресты и мемориальные знаки.",
            "en": "Address: Solovetsky Islands, Arkhangelsk oblast, Russia.\n\nThe Solovki Special Purpose Camp (SLON) was a notorious site of imprisonment and martyrdom for dozens of Belarusian Catholic and Orthodox clergy and laity documented by researcher Leanid Marakou. Memorial crosses and markers commemorate the victims."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/2b/Ensemble_of_the_Solovetsky_monastery_in_the_fog.jpg",
        "links": [
            {
                "title": "Рэпрэсаваныя каталіцкія духоўныя асобы Беларусі (Л. Маракоў)",
                "url": "https://knihi-online.com/represavanyja-katalickija-duchounyja-kansekravanyja-i-svieckija-asoby-bielarusi-marakou.html"
            }
        ],
        "tags": ["Расія", "Салаўкі", "СЛОН", "Рэпрэсіі", "Леанід Маракоў", "historical"],
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

# Also sync places.js and persons.js
with open('data/places.js', 'w', encoding='utf-8') as f:
    f.write('window.INITIAL_PLACES = ' + json.dumps(final_places, ensure_ascii=False, indent=2) + ';\n')

with open('data/persons.js', 'w', encoding='utf-8') as f:
    f.write('window.INITIAL_PERSONS = ' + json.dumps(final_persons, ensure_ascii=False, indent=2) + ';\n')

print(f"Updated places: {len(final_places)}")
print(f"Updated persons: {len(final_persons)}")
