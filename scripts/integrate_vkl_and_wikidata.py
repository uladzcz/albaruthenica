import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Load existing files
with open('data/persons.json', 'r', encoding='utf-8') as f:
    persons = json.load(f)

with open('data/places.json', 'r', encoding='utf-8') as f:
    places = json.load(f)

print(f"Initial: {len(persons)} persons, {len(places)} places")

# 1. Update radziwills and Radziwill clan members
radz_ids = ["barbara-radziwill", "radziwill-sirotka", "mikolaj-radziwill-black", "antoni-radziwill", "magdalena-radziwill", "anna-radziwill"]

for p in persons:
    if p['id'] == 'radziwills':
        p['name'] = {
            "by": "Радзівілы",
            "ru": "Радзивиллы",
            "en": "Radziwills"
        }
        p['relatedPersonIds'] = radz_ids
    elif p['id'] in radz_ids:
        p['relatedPersonIds'] = ["radziwills"]
    elif p['id'] == 'lew-sapieha':
        p['name'] = {
            "by": "Леў Сапега",
            "ru": "Лев Сапега",
            "en": "Lew Sapieha"
        }

# 2. Add new persons
new_persons = [
    {
        "id": "mikolaj-radziwill-black",
        "name": {
            "by": "Мікалай Радзівіл «Чорны»",
            "ru": "Николай Радзивилл «Чёрный»",
            "en": "Mikołaj \"the Black\" Radziwiłł"
        },
        "role": {
            "by": "Канцлер і гетман вялікі літоўскі, лідар Рэфармацыі ў ВКЛ",
            "ru": "Канцлер и великий гетман литовский, лидер Реформации в ВКЛ",
            "en": "Grand Chancellor and Hetman of Lithuania, Reformation leader"
        },
        "dates": "1515–1565",
        "bio": {
            "by": "Адзін з наймагутнейшых дзяржаўных дзеячаў у гісторыі Вялікага Княства Літоўскага, канцлер вялікі літоўскі і ваявода віленскі. Заснавальнік Брэсцкай друкарні, фундатар Брэсцкай Бібліі (1563). Ягоны рэнесансны парадны даспех работы Кунца Лохнера (~1555) зберагаецца ў Імператарскай зброевай палаце Музея гісторыі мастацтваў у Вене (Хофбург).",
            "ru": "Один из могущественнейших государственных деятелей ВКЛ, канцлер великий литовский и виленский воевода. Основатель Брестской типографии, меценат Брестской Библии (1563). Его парадный ренессансный доспех работы Кунца Лохнера (~1555) хранится в Императорской оружейной палате в Вене (Хофбург).",
            "en": "One of the most powerful statesmen of the Grand Duchy of Lithuania, Grand Chancellor and Voivode of Vilnius. Founded the Brest printing house and sponsored the Brest Bible (1563). His gilded parade armor by Kunz Lochner (~1555) is exhibited at the Imperial Armoury in the Vienna Hofburg."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Mika%C5%82aj_Radzivi%C5%82_%C4%8Corny._%D0%9C%D1%96%D0%BA%D0%B0%D0%BB%D0%B0%D0%B9_%D0%A0%D0%B0%D0%B4%D0%B7%D1%96%D0%B2%D1%96%D0%BB_%D0%A7%D0%BE%D1%80%D0%BD%D1%8B_%28XVI%29.jpg/440px-Mika%C5%82aj_Radzivi%C5%82_%C4%8Corny._%D0%9C%D1%96%D0%BA%D0%B0%D0%BB%D0%B0%D0%B9_%D0%A0%D0%B0%D0%B4%D0%B7%D1%96%D0%B2%D1%96%D0%BB_%D0%A7%D0%BE%D1%80%D0%BD%D1%8B_%28XVI%29.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%9C%D1%96%D0%BA%D0%B0%D0%BB%D0%B0%D0%B9_%D0%A0%D0%B0%D0%B4%D0%B7%D1%96%D0%B2%D1%96%D0%BB_%D0%A7%D0%BE%D1%80%D0%BD%D1%8B",
        "relatedPersonIds": ["radziwills", "radziwill-sirotka", "barbara-radziwill"]
    },
    {
        "id": "vilna-gaon",
        "name": {
            "by": "Віленскі Гаон (Эліяху бен Шлома Залман)",
            "ru": "Виленский Гаон (Элияху бен Шломо Залман)",
            "en": "Vilna Gaon (Elijah ben Solomon Zalman)"
        },
        "role": {
            "by": "Найвялікшы духоўны аўтарытэт літвацкага юдаізму, мысляр і матэматык",
            "ru": "Величайший духовный авторитет литвакского иудаизма, мыслитель и математик",
            "en": "Supreme spiritual authority of Litvak Judaism, philosopher and scholar"
        },
        "dates": "1720–1797",
        "bio": {
            "by": "Нарадзіўся ў мястэчку Сялец на Берасцейшчыне. Адзін з найвыдатнейшых духоўных аўтарытэтаў у гісторыі яўрэйскага народа, духоўны бацька руху міснагдым (літвакоў). Аўтар дзясяткаў каментароў да Торы і Талмуда, прац па геаметрыі, астраноміі і граматыцы іўрыту. Пахаваны ў Вільні на могілках Судэрве.",
            "ru": "Родился в местечке Селец на Брестчине. Один из выдающихся духовных авторитетов в еврейской истории, отец движения миснагдим (литваков). Автор фундаментальных трудов по Талмуду, математике и астрономии. Похоронен в Вильнюсе на кладбище Судерве.",
            "en": "Born in Sielec near Brest (Belarus). The leading spiritual authority of Litvak Judaism, known as the Genius of Vilna. Authored seminal commentaries on the Torah and Talmud as well as treatises on geometry and astronomy. Buried at the Sudervė Cemetery in Vilnius."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Vilna_Gaon.jpg/440px-Vilna_Gaon.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%92%D1%96%D0%BB%D0%B5%D0%BD%D1%81%D0%BA%D1%96_%D0%B3%D0%B0%D0%BE%D0%BD"
    },
    {
        "id": "eliezer-ben-yehuda",
        "name": {
            "by": "Эліэзер Бэн-Егуда",
            "ru": "Элиэзер Бен-Йехуда",
            "en": "Eliezer Ben-Yehuda"
        },
        "role": {
            "by": "«Бацька сучаснага іўрыту», мовазнавец і рэфарматар",
            "ru": "«Отец современного иврита», языковед и лексикограф",
            "en": "Father of Modern Hebrew, lexicographer and revitalizer of the language"
        },
        "dates": "1858–1922",
        "bio": {
            "by": "Нарадзіўся ў мястэчку Лужкі Дзісненскага павета (цяпер Шаркаўшчынскі раён). Чалавек, які здзейсніў адно з найвялікшых лінгвістычных цудаў у гісторыі: адрадзіў іўрыт як жывую паўсядзённую гутарковую мову і склаў першы поўны слоўнік старажытнага і сучаснага іўрыту. Заснаваў Камітэт мовы іўрыт у Іерусаліме.",
            "ru": "Родился в местечке Лужки Дисненского уезда (ныне Шарковщинский район). Возродил иврит как разговорный язык повседневного общения и создал фундаментальный 16-томный словарь современного иврита. Похоронен на Масличной горе в Иерусалиме.",
            "en": "Born in Luzhki, Vitebsk region (Belarus). Known as the Father of Modern Hebrew; he accomplished the historic revival of Hebrew as a spoken everyday language and authored the first comprehensive modern Hebrew dictionary. Buried on the Mount of Olives in Jerusalem."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Eliezer_Ben-Yehuda.jpg/440px-Eliezer_Ben-Yehuda.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%AD%D0%BB%D1%96%D1%8D%D0%B7%D0%B5%D1%80_%D0%91%D1%8D%D0%BD-%D0%95%D0%B3%D1%83%D0%B4%D0%B0"
    },
    {
        "id": "simon-kuznets",
        "name": {
            "by": "Сайман Кузнец (Сямён Кузнец)",
            "ru": "Саймон Кузнец (Семён Кузнец)",
            "en": "Simon Kuznets"
        },
        "role": {
            "by": "Лаўрэат Нобелеўскай прэміі па эканоміцы (1971), стваральнік паняцця ВУП",
            "ru": "Лауреат Нобелевской премии по экономике (1971), создатель концепции ВВП",
            "en": "Nobel Memorial Prize laureate in Economic Sciences (1971), creator of GDP"
        },
        "dates": "1901–1985",
        "bio": {
            "by": "Нарадзіўся ў Пінску. Выбітны эканаміст XX стагоддзя, прафесар Гарвардскага ўніверсітэта. Стварыў стандартызаваную сістэму нацыянальных рахункаў і ўвёў у сусветную эканоміку фундаментальнае паняцце валавога ўнутранага прадукту (ВУП/GDP), а таксама выявіў эканамічныя цыклы Кузнеца. У 1971 г. уганараваны Нобелеўскай прэміяй па эканоміцы.",
            "ru": "Родился в Пинске. Профессор Гарвардского университета, лауреат Нобелевской премии по экономике 1971 года. Создатель концепции валового внутреннего продукта (ВВП) и современных национальных счетов, первооткрыватель циклов Кузнеца.",
            "en": "Born in Pinsk (Belarus). Harvard University economist awarded the Nobel Prize in Economic Sciences in 1971. Pioneered national income accounting and developed the concept of Gross Domestic Product (GDP), transforming macroeconomic measurement globally."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Simon_Kuznets.jpg/440px-Simon_Kuznets.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%A1%D0%B0%D0%B9%D0%BC%D0%B0%D0%BD_%D0%9A%D1%83%D0%B7%D0%BD%D0%B5%D1%86"
    },
    {
        "id": "ryszard-kapuscinski",
        "name": {
            "by": "Рышард Капусцінскі",
            "ru": "Рышард Капущинский",
            "en": "Ryszard Kapuściński"
        },
        "role": {
            "by": "Сусветны класік літаратурнага рэпартажу, пісьменнік і публіцыст",
            "ru": "Классик мирового литературного репортажа, писатель и публицист",
            "en": "World-renowned literary reporter, author, and essayist"
        },
        "dates": "1932–2007",
        "bio": {
            "by": "Нарадзіўся ў Пінску і заўсёды падкрэсліваў, што ягоны светапогляд сфарміравала дзяцінства на Палессі сярод беларусаў: «Я чалавек Палесся, туды вяртаюцца ўсе мае ўспаміны». Сусветна вядомы рэпарцёр, які працаваў у Афрыцы, Лацінскай Амерыцы і Азіі, аўтар кніг «Імперыя», «Шахіншах», «Імператар», «Падарожжы з Герадотам».",
            "ru": "Родился в Пинске, неоднократно подчеркивал значение своего полесского детства для своего взгляда на мир. Всемирно известный репортёр и автор книг «Империя», «Шахиншах», «Император», переведённых на десятки языков.",
            "en": "Born in Pinsk (Polesia, Belarus). Internationally acclaimed Polish-Belarusian journalist and writer, author of 'The Emperor', 'Shah of Shahs', and 'Imperium'. He consistently traced his worldview to his childhood among the people of Polesia."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Ryszard_Kapu%C5%9Bci%C5%84ski_2003_%28cropped%29.jpg/440px-Ryszard_Kapu%C5%9Bci%C5%84ski_2003_%28cropped%29.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%A0%D1%8B%D1%88%D0%B0%D1%80%D0%B4_%D0%9A%D0%B0%D0%BF%D1%83%D1%81%D1%86%D1%96%D0%BD%D1%81%D0%BA%D1%96"
    },
    {
        "id": "boris-kit",
        "name": {
            "by": "Барыс Кіт",
            "ru": "Борис Кит",
            "en": "Boris Kit"
        },
        "role": {
            "by": "Беларускі і амерыканскі вучоны ў галіне астранаўтыкі, распрацоўшчык паліва «Апалона»",
            "ru": "Белорусский и американский учёный в области астронавтики, разработчик ракетного топлива программы «Аполлон»",
            "en": "Belarusian-American astronautics scientist, liquid hydrogen fuel pioneer for Apollo"
        },
        "dates": "1910–2018",
        "bio": {
            "by": "Нарадзіўся ў беларускай сям'і, вырас у вёсцы Агароднікі на Карэліччыне, скончыў Навагрудскую беларускую гімназію і Віленскі ўніверсітэт. Выбітны дзеяч беларускай эміграцыі. У ЗША стаў піянерам ракетнага паліва: даследаваў вадкі вадарод і стварыў сістэмы паліва для праграмы «Апалон» і шатлаў. Пражыў 107 гадоў і пахаваны ў Вісбадэне пад бел-чырвона-белым сцягам.",
            "ru": "Выпускник Виленского университета и директор Новогрудской белорусской гимназии. В США стоял у истоков космической программы NASA, исследовал жидкий водород и разработал топливные смеси для лунной программы «Аполлон». Похоронен в Висбадене под бело-красно-белым флагом.",
            "en": "Born to a Belarusian family, directed the Novogrudok Belarusian Gymnasium. In the US, he became a key rocket propulsion expert for NASA, pioneering liquid hydrogen fuel systems for the Apollo lunar missions and space shuttles. Lived to 107 and is buried in Wiesbaden under the Belarusian white-red-white flag."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Barys_Kit_%28Boris_Kit%29.jpg/440px-Barys_Kit_%28Boris_Kit%29.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%91%D0%B0%D1%80%D1%8B%D1%81_%D0%9A%D1%96%D1%82"
    },
    {
        "id": "michal-kleofas-oginski",
        "name": {
            "by": "Міхал Клеафас Агінскі",
            "ru": "Михаил Клеофас Огинский",
            "en": "Michał Kleofas Ogiński"
        },
        "role": {
            "by": "Кампазітар, аўтар паланэза «Развітанне з Радзімай», дзяржаўны дзеяч ВКЛ",
            "ru": "Композитор, автор полонеза «Прощание с Родиной», государственный деятель ВКЛ",
            "en": "Composer of the Polonaise 'Farewell to the Homeland', statesman of the GDL"
        },
        "dates": "1765–1833",
        "bio": {
            "by": "Дзяржаўны дзеяч Вялікага Княства Літоўскага, падскарбі вялікі літоўскі, дыпламат, паплечнік Тадэвуша Касцюшкі. Аўтар легендарнага паланэза ля мінор «Развітанне з Радзімай» («Паланэз Агінскага»), напісанага пры ад'ездзе за мяжу пасля паразы паўстання 1794 года. Жыў у Залессі пад Смаргонню. Пахаваны ў базіліцы Санта-Крочэ ў Фларэнцыі побач з Мікеланджэла і Галілеем.",
            "ru": "Подскарбий великий литовский, дипломат, участник восстания Костюшко. Автор всемирно известного полонеза ля минор «Прощание с Родиной». Жил в усадьбе Залесье. Похоронен в пантеоне базилики Санта-Кроче во Флоренции.",
            "en": "Grand Treasurer of Lithuania, diplomat, and composer. Authored the immortal Polonaise in A minor 'Farewell to the Homeland'. Lived at his Zalesye estate near Smorgon. Buried in the Basilica of Santa Croce in Florence alongside Michelangelo and Galileo."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Micha%C5%82_Kleofas_Ogi%C5%84ski.jpg/440px-Micha%C5%82_Kleofas_Ogi%C5%84ski.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%9C%D1%96%D1%85%D0%B0%D0%BB_%D0%9A%D0%BB%D0%B5%D0%B0%D1%84%D0%B0%D1%81_%D0%90%D0%B3%D1%96%D0%BD%D1%81%D0%BA%D1%96",
        "relatedPersonIds": ["michal-kazimir-oginski"]
    },
    {
        "id": "alhierd",
        "name": {
            "by": "Вялікі князь Альгерд",
            "ru": "Великий князь Ольгерд",
            "en": "Grand Duke Algirdas (Alhierd)"
        },
        "role": {
            "by": "Вялікі князь літоўскі (1345–1377), палкаводзец, пераможца бітвы на Сініх Водах",
            "ru": "Великий князь литовский (1345–1377), полководец, победитель битвы на Синих Водах",
            "en": "Grand Duke of Lithuania (1345–1377), victor of the Battle of Blue Waters"
        },
        "dates": "каля 1296–1377",
        "bio": {
            "by": "Сын Гедзіміна, вялікі князь літоўскі, які аб'яднаў усе беларускія землі вакол ВКЛ і пашырыў межы дзяржавы ад Балтыйскага да Чорнага мора. У 1362 г. разграміў трох татарскіх князёў у бітве на Сініх Водах, вызваліўшы Кіеўшчыну і Падолле ад ардынскай залежнасці. Здзейсніў тры пераможныя паходы на Маскву (1368, 1370, 1372).",
            "ru": "Великий князь литовский, объединивший все белорусские земли в составе ВКЛ. В 1362 году разгромил ордынских беев в битве на Синих Водах, освободив Киев и Подолье. Совершил три победоносных похода на Москву.",
            "en": "Grand Duke of Lithuania who unified all Belarusian principalities under the GDL and expanded borders to the Black Sea. Defeated the Golden Horde at the Battle of Blue Waters (1362), liberating Kyiv and Podolia."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Alhierd._%D0%90%D0%BB%D1%8C%D0%B3%D0%B5%D1%80%D0%B4_%28A._Guagnini%2C_1578%29.jpg/440px-Alhierd._%D0%90%D0%BB%D1%8C%D0%B3%D0%B5%D1%80%D0%B4_%28A._Guagnini%2C_1578%29.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%90%D0%BB%D1%8C%D0%B3%D0%B5%D1%80%D0%B4"
    },
    {
        "id": "jan-karol-chodkiewicz",
        "name": {
            "by": "Ян Караль Хадкевіч",
            "ru": "Ян Кароль Ходкевич",
            "en": "Jan Karol Chodkiewicz"
        },
        "role": {
            "by": "Вялікі гетман літоўскі, палкаводзец, пераможца бітвы пад Кірхгольмам",
            "ru": "Великий гетман литовский, полководец, победитель битвы при Кирхгольме",
            "en": "Grand Hetman of Lithuania, celebrated military commander, victor of Kirchholm"
        },
        "dates": "1560–1621",
        "bio": {
            "by": "Адзін з найвыдатнейшых военачальнікаў Еўропы XVII стагоддзя, вялікі гетман літоўскі і ваявода віленскі. У 1605 г. у бітве пад Кірхгольмам (цяпер Саласпілс, Латвія) на чале 4-тысячнага войска ВКЛ разграміў 14-тысячную шведскую каралеўскую армію Карла IX дзякуючы легендарнай атацы гусарыі. У 1621 г. кіраваў гераічнай абаронай Хоціна ад асманскага войска.",
            "ru": "Один из выдающихся полководцев Европы XVII века, великий гетман литовский. В битве при Кирхгольме (1605) разгромил шведскую армию короля Карла IX благодаря тактике крылатых гусар ВКЛ. Руководил обороной Хотина в 1621 году.",
            "en": "Grand Hetman of Lithuania and one of the finest military commanders of 17th-century Europe. At the Battle of Kirchholm (1605, Salaspils, Latvia), his Lithuanian winged hussars crushed a Swedish royal army more than three times its size. Led the victorious defense of Khotyn in 1621."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Jan_Karol_Chodkiewicz.PNG/440px-Jan_Karol_Chodkiewicz.PNG",
        "wiki": "https://be.wikipedia.org/wiki/%D0%AF%D0%BD_%D0%9A%D0%B0%D1%80%D0%B0%D0%BB%D1%8C_%D0%A5%D0%B0%D0%B4%D0%BA%D0%B5%D0%B2%D1%96%D1%87"
    },
    {
        "id": "sciapan-palubes",
        "name": {
            "by": "Сцяпан Палубес",
            "ru": "Степан Полубес",
            "en": "Sciapan Palubes (Stepan Polubes)"
        },
        "role": {
            "by": "Выбітны беларускі майстар-цаканік і кафляр з Мсціслава",
            "ru": "Белорусский мастер изразцового дела и керамики из Мстиславля",
            "en": "Master tilemaker and ceramist from Mstsislaw, creator of polychrome tiles"
        },
        "dates": "XVII ст.",
        "bio": {
            "by": "Ураджэнец Мсціслава, адзін з найвыдатнейшых майстроў шматколернай паліванай кафлі («цаніннай справы») эпохі барока. Пасля вайны 1654–1667 гг. працаваў у Маскве, дзе жыў у Мяшчанскай слабадзе. Аздабляў царкву Пакрова Багародзіцы ў Ізмайлаве, Новаіерусалімскі манастыр, сабор Пакрова на Раве і храмы Масквы, увёўшы беларускія раслінныя матывы «паўлінава вока» ў манументальнае мастацтва.",
            "ru": "Уроженец Мстиславля, крупнейший мастер многоцветного изразцового искусства XVII века. Жил в Мещанской слободе Москвы. Создал уникальные изразцовые пояса «павлинье око» Новоиерусалимского монастыря, храма Покрова в Измайлове и московских соборов.",
            "en": "Master ceramist born in Mstsislaw (Belarus), pioneer of Belarusian polychrome relief tiles in Moscow. Lived in the Meshchanskaya Sloboda and decorated the New Jerusalem Monastery and Izmaylovo Church with his famous 'peacock eye' ceramic friezes."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Church_of_the_Intercession_%28Izmaylovo%29_-_Frieze_02.jpg/440px-Church_of_the_Intercession_%28Izmaylovo%29_-_Frieze_02.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%A1%D1%86%D1%8F%D0%BF%D0%B0%D0%BD_%D0%86%D0%B2%D0%B0%D0%BD%D0%B0%D0%B2%D1%96%D1%87_%D0%9F%D0%B0%D0%BB%D1%83%D0%B1%D0%B5%D1%81"
    },
    {
        "id": "branislaw-epimakh-shypila",
        "name": {
            "by": "Браніслаў Эпімах-Шыпіла",
            "ru": "Бронислав Эпимах-Шипило",
            "en": "Branislaŭ Epimakh-Shypila"
        },
        "role": {
            "by": "Дзеяч беларускага адраджэння, бібліятэкар, заснавальнік суполкі «Загляне сонца»",
            "ru": "Деятель белорусского возрождения, библиограф, основатель «Загляне сонца»",
            "en": "Belarusian cultural revival pioneer, bibliographer, publisher"
        },
        "dates": "1859–1934",
        "bio": {
            "by": "Ураджэнец Полаччыны, прафесар і бібліятэкар Санкт-Пецярбургскага ўніверсітэта. Заснавальнік і кіраўнік першага беларускага выдавецтва «Загляне сонца і ў наша аконца» (1906). У ягонай пецярбургскай кватэры на Васільеўскім востраве (4-я лінія, 45) у 1909–1913 гг. жыў Янка Купала, збіралася студэнцкая беларуская моладзь і рыхтаваліся класічныя выданні нацыянальнай літаратуры.",
            "ru": "Профессор и хранитель библиотеки Петербургского университета. Основатель белорусского издательства «Загляне сонца і ў наша аконца». В его квартире на 4-й линии В.О., 45 жил Янка Купала и собиралась белорусская интеллигенция.",
            "en": "Bibliographer and professor at Saint Petersburg University. Co-founded the pioneering Belarusian publishing society 'Zahliane sontsa i ŭ nasha akontsa' (1906). In his apartment at 4th Line V.O. 45, poet Yanka Kupala lived from 1909 to 1913."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Branisla%C5%AD_Epimach-%C5%A0ypila._%D0%91%D1%80%D0%B0%D0%BD%D1%96%D1%81%D0%BB%D0%B0%D1%9E_%D0%AD%D0%BF%D1%96%D0%BC%D0%B0%D1%85-%D0%A8%D1%8B%D0%BF%D1%96%D0%BB%D0%B0_%281900%29.jpg/440px-Branisla%C5%AD_Epimach-%C5%A0ypila._%D0%91%D1%80%D0%B0%D0%BD%D1%96%D1%81%D0%BB%D0%B0%D1%9E_%D0%AD%D0%BF%D1%96%D0%BC%D0%B0%D1%85-%D0%A8%D1%8B%D0%BF%D1%96%D0%BB%D0%B0_%281900%29.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%91%D1%80%D0%B0%D0%BD%D1%96%D1%81%D0%BB%D0%B0%D1%9E_%D0%86%D0%B3%D0%BD%D0%B0%D1%82%D0%B0%D0%B2%D1%96%D1%87_%D0%AD%D0%BF%D1%96%D0%BC%D0%B0%D1%85-%D0%A8%D1%8B%D0%BF%D1%96%D0%BB%D0%B0"
    },
    {
        "id": "ivan-hryharovich",
        "name": {
            "by": "Іван Грыгаровіч",
            "ru": "Иван Григорович",
            "en": "Ivan Hryharovich"
        },
        "role": {
            "by": "Заснавальнік беларускай археаграфіі, гісторык, святар",
            "ru": "Основатель белорусской археографии, историк, протоиерей",
            "en": "Founder of Belarusian archeography, historian, publisher"
        },
        "dates": "1792–1852",
        "bio": {
            "by": "Нарадзіўся ў Прапойску (цяпер Слаўгарад). Піянер беларускай навуковай археаграфіі і гістарыяграфіі. Выдаў манументальны першы збор дакументаў па гісторыі Беларусі «Беларускі архіў старажытных граматаў» (1824) і зборнік «Акты Заходняй Расіі». Аўтар неапублікаванай працы «Беларуская іерархія». Пахаваны на Волкаўскіх праваслаўных могілках у Санкт-Пецярбургу.",
            "ru": "Родился в Пропойске (Славгород). Основоположник белорусской археографии, издатель первого фундаментального сборника документов «Белорусский архив древних грамот» (1824). Похоронен на Волковском православном кладбище в Петербурге.",
            "en": "Born in Propoysk (now Slawharad, Belarus). Founder of Belarusian archeography, editor of the first comprehensive source collection 'Belarusian Archive of Ancient Deeds' (1824). Buried at the Volkovo Orthodox Cemetery in Saint Petersburg."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Ivan_Hryharovi%C4%8D._%D0%86%D0%B2%D0%B0%D0%BD_%D0%93%D1%80%D1%8B%D0%B3%D0%B0%D1%80%D0%BE%D0%B2%D1%96%D1%87.jpg/440px-Ivan_Hryharovi%C4%8D._%D0%86%D0%B2%D0%B0%D0%BD_%D0%93%D1%80%D1%8B%D0%B3%D0%B0%D1%80%D0%BE%D0%B2%D1%96%D1%87.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%86%D0%B2%D0%B0%D0%BD_%D0%86%D0%B2%D0%B0%D0%BD%D0%B0%D0%B2%D1%96%D1%87_%D0%93%D1%80%D1%8B%D0%B3%D0%B0%D1%80%D0%BE%D0%B2%D1%96%D1%87"
    },
    {
        "id": "mikhail-mikeshin",
        "name": {
            "by": "Міхаіл Мікешын",
            "ru": "Михаил Микешин",
            "en": "Mikhail Mikeshin"
        },
        "role": {
            "by": "Скульптар і жывапісец беларускага паходжання, аўтар манументаў",
            "ru": "Скульптор и живописец белорусского происхождения, создатель монументов",
            "en": "Sculptor and artist of Belarusian descent, monument creator"
        },
        "dates": "1835–1896",
        "bio": {
            "by": "Нарадзіўся ў вёсцы Платонава Рослаўскага павета (Смаленшчына) у сям'і выхадцаў з Беларусі. Скончыў Пецярбургскую Акадэмію мастацтваў. Стваральнік грандыёзных манументаў эпохі: помніка Кацярыне II на плошчы Астроўскага ў Пецярбургу, помніка 1000-годдзю Расіі ў Ноўгарадзе і помніка Багдану Хмяльніцкаму ў Кіеве. Сябраваў з Тарасам Шаўчэнкам і ілюстраваў творы славянскіх паэтаў.",
            "ru": "Родился на Смоленщине. Академик Императорской Академии художеств. Автор памятника «Тысячелетие России» в Новгороде, памятника Екатерине II в Санкт-Петербурге и памятника Богдану Хмельницкому в Киеве.",
            "en": "Sculptor of Belarusian descent, graduated from the Saint Petersburg Academy of Arts. Created iconic monuments including Catherine the Great in Saint Petersburg, the Millennium of Russia in Novgorod, and Bohdan Khmelnytsky in Kyiv."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Mikhail_Mikeshin_1880.jpg/440px-Mikhail_Mikeshin_1880.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%9C%D1%96%D1%85%D0%B0%D1%96%D0%BB_%D0%92%D1%81%D0%B5%D0%B2%D0%B0%D0%BB%D0%B0%D0%B4%D0%B0%D0%B2%D1%96%D1%87_%D0%9C%D1%96%D0%BA%D0%B5%D1%88%D1%8B%D0%BD"
    },
    {
        "id": "mendele-mocher-sforim",
        "name": {
            "by": "Мендэле Мойхер-Сфорым (Шолем-Якаў Абрамовіч)",
            "ru": "Менделе Мойхер-Сфорим (Шолом-Яков Абрамович)",
            "en": "Mendele Mocher Sforim"
        },
        "role": {
            "by": "«Дзядуля яўрэйскай літаратуры», пісьменнік і асветнік",
            "ru": "«Дедушка еврейской литературы», писатель и просветитель",
            "en": "Grandfather of modern Yiddish and Hebrew literature"
        },
        "dates": "1836–1917",
        "bio": {
            "by": "Нарадзіўся ў мястэчку Капыль на Міншчыне. Прызнаны заснавальнік сучаснай свецкай мастацкай літаратуры на ідышы і іўрыце. У сваіх аповесцях ярка адлюстраваў побыт і характары беларускага мястэчка. Большую частку сталага жыцця правёў у Адэсе, дзе кіраваў талмуд-торай і быў лідарам культурнага жыцця. Пахаваны на Другіх хрысціянскіх могілках у Адэсе.",
            "ru": "Родился в местечке Копыль под Минском. Признанный основоположник классической еврейской литературы на идише и иврите. Похоронен на Втором христианском кладбище в Одессе.",
            "en": "Born in Kapyl (Belarus). Celebrated as the Grandfather of modern Yiddish and Hebrew literature. Masterfully depicted the life of the Belarusian shtetl. Buried at the Second Christian Cemetery in Odesa (Ukraine)."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Mendele_Mocher_Sforim_1910.jpg/440px-Mendele_Mocher_Sforim_1910.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%9C%D0%B5%D0%BD%D0%B4%D1%8D%D0%BB%D0%B5_%D0%9C%D0%BE%D0%B9%D1%85%D0%B5%D1%80-%D0%A1%D1%84%D0%BE%D1%80%D1%8B%D0%BC"
    },
    {
        "id": "stefaniya-stanyuta",
        "name": {
            "by": "Стэфанія Станюта",
            "ru": "Стефания Станюта",
            "en": "Stefaniya Stanyuta"
        },
        "role": {
            "by": "Легенда беларускага тэатра і кіно, народная артыстка Беларусі",
            "ru": "Легенда белорусского театра и кино, народная артистка Беларуси",
            "en": "Legendary Belarusian theatre and film actress, People's Artist"
        },
        "dates": "1905–2000",
        "bio": {
            "by": "Нарадзілася ў Мінску ў сям'і мастака Міхаіла Станюты. У 1926 г. скончыла Беларускую драматычную студыю ў Маскве, выпуснікі якой склалі аснову БДТ-2 (Коласаўскага тэатра ў Віцебску). З 1932 г. — прыма Купалаўскага тэатра ў Мінску, знялася ў дзясятках класічных фільмаў («Белыя росы», «Людзі на балоце», «Развітанне з Мацёрай»).",
            "ru": "Родилась в Минске. В 1926 году окончила Белорусскую драматическую студию в Москве. Звезда Купаловского театра, выдающаяся актриса кино («Белые росы», «Прощание»).",
            "en": "Born in Minsk to painter Mikhail Stanyuta. Graduated from the Belarusian Dramatic Studio in Moscow in 1926. Became a premier star of the Kupala National Theatre and classical cinema ('White Dew', 'Farewell')."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Stefaniya_Stanyuta.jpg/440px-Stefaniya_Stanyuta.jpg",
        "wiki": "https://be.wikipedia.org/wiki/%D0%A1%D1%82%D1%8D%D1%84%D0%B0%D0%BD%D1%96%D1%8F_%D0%9C%D1%96%D1%85%D0%B0%D0%B9%D0%BB%D0%B0%D1%9E%D0%BD%D0%B0_%D0%A1%D1%82%D0%B0%D0%BD%D1%8E%D1%82%D0%B0"
    }
]

# Check existing persons
existing_person_ids = {p['id'] for p in persons}
added_persons = 0
for np in new_persons:
    if np['id'] not in existing_person_ids:
        persons.append(np)
        existing_person_ids.add(np['id'])
        added_persons += 1

print(f"Added {added_persons} new persons. Total persons now: {len(persons)}")

# 3. New places to add
new_places = [
    # Moscow Sites
    {
        "id": "moscow-meshchanskaya-sloboda",
        "title": {
            "by": "Мяшчанская слабада (гістарычнае пасяленне выхадцаў з Беларусі ў Маскве)",
            "ru": "Мещанская слобода (историческое поселение выходцев из Беларуси в Москве)",
            "en": "Meshchanskaya Sloboda (Historic Belarusian Settlement in Moscow)"
        },
        "category": "historical",
        "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
        "city": {"by": "Масква", "ru": "Москва", "en": "Moscow"},
        "coordinates": [55.7766, 37.6322],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Meshchanskaya_Street_1910s.jpg/640px-Meshchanskaya_Street_1910s.jpg",
        "description": {
            "by": "Заснаваная ў 1671 годзе царом Аляксеем Міхайлавічам адмыслова для перасяленцаў і палонных з Вялікага Княства Літоўскага і Беларусі пасля вайны 1654–1667 гг. Менавіта ад беларускага слова «мяшчане» (гараджане, жыхары места) у расійскую мову ўвайшло само паняцце «мещане»! Тут жылі беларускія рамеснікі, пераплётчыкі, збройнікі і славуты мсціслаўскі кафляр Сцяпан Палубес, які стварыў унікальную паліхромную маскоўскую кафлю. Раён сучасных Мяшчанскіх вуліц і праспекта Міру.",
            "ru": "Основана в 1671 году для выходцев из Великого Княжества Литовского и Беларуси. Именно от белорусского слова «мяшчане» (горожане) в русский язык вошло сословие «мещане». Здесь жили ремесленники, переплётчики и знаменитый керамист из Мстиславля Степан Полубес.",
            "en": "Established in 1671 specifically for craftsmen and settlers from the Grand Duchy of Lithuania and Belarus. The Russian word 'meshchane' (townspeople) originated directly from the Belarusian 'miashchane'. Home to artisans and master tilemaker Sciapan Palubes."
        },
        "personIds": ["sciapan-palubes"],
        "mustSee": True,
        "links": [
            {"title": "Мещанская слобода (Вікіпедыя)", "url": "https://be.wikipedia.org/wiki/%D0%9C%D1%8F%D1%88%D1%87%D0%B0%D0%BD%D1%81%D0%BA%D0%B0%D1%8F_%D1%81%D0%BB%D0%B0%D0%B1%D0%B0%D0%B4%D0%B0"}
        ]
    },
    {
        "id": "moscow-belarusian-drama-studio",
        "title": {
            "by": "Беларуская драматычная студыя ў Маскве (калыска тэатра імя Коласа)",
            "ru": "Белорусская драматическая студия в Москве (колыбель театра имени Коласа)",
            "en": "Belarusian Dramatic Studio in Moscow (Cradle of Kolas Theatre)"
        },
        "category": "culture",
        "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
        "city": {"by": "Масква", "ru": "Москва", "en": "Moscow"},
        "coordinates": [55.7588, 37.6045],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Stefaniya_Stanyuta.jpg/440px-Stefaniya_Stanyuta.jpg",
        "description": {
            "by": "Дзяржаўная тэатральная навучальная ўстанова, якая працавала ў Маскве ў 1921–1926 гг. пры Наркамасвеце БССР. Тут пад кіраўніцтвам дзеячаў МХАТ рыхтавалі прафесійных акцёраў для першага беларускага дзяржаўнага тэатра. Выпускнікі студыі (Стэфанія Станюта, Аляксандр Ільінскі, Павел Малчанаў) у 1926 г. заснавалі Другі беларускі дзяржаўны тэатр (БДТ-2, цяпер Нацыянальны драматычны тэатр імя Якуба Коласа ў Віцебску).",
            "ru": "Действовала в Москве в 1921–1926 годах при Наркомпросе. Выпускники студии (Стефания Станюта, Александр Ильинский, Павел Молчанов) основали в 1926 году Второй белорусский государственный театр (БДТ-2, ныне театр имени Якуба Коласа в Витебске).",
            "en": "Operating in Moscow from 1921 to 1926, this studio trained the pioneer generation of professional Belarusian actors. Its graduates, including Stefaniya Stanyuta, went on to establish the second state theatre (now the Yakub Kolas National Academic Theatre in Vitebsk)."
        },
        "personIds": ["stefaniya-stanyuta"],
        "links": [
            {"title": "Беларуская драматычная студыя (Вікіпедыя)", "url": "https://be.wikipedia.org/wiki/%D0%91%D0%B5%D0%BB%D0%B0%D1%80%D1%83%D1%81%D0%BA%D0%B0%D1%8F_%D0%B4%D1%80%D0%B0%D0%BC%D0%B0%D1%82%D1%8B%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%83%D0%B4%D1%8B%D1%8F"}
        ]
    },
    # Saint Petersburg Sites
    {
        "id": "petersburg-epimakh-shypila-flat",
        "title": {
            "by": "Кватэра Браніслава Эпімах-Шыпілы і суполка «Загляне сонца» (4-я лінія В.В., 45)",
            "ru": "Квартира Бронислава Эпимах-Шипило и общество «Загляне сонца» (4-я линия В.О., 45)",
            "en": "Apartment of Branislaŭ Epimakh-Shypila & 'Zahliane Sontsa' (4th Line V.O. 45)"
        },
        "category": "historical",
        "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
        "city": {"by": "Санкт-Пецярбург", "ru": "Санкт-Петербург", "en": "Saint Petersburg"},
        "coordinates": [59.9431, 30.2825],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Branisla%C5%AD_Epimach-%C5%A0ypila._%D0%91%D1%80%D0%B0%D0%BD%D1%96%D1%81%D0%BB%D0%B0%D1%9E_%D0%AD%D0%BF%D1%96%D0%BC%D0%B0%D1%85-%D0%A8%D1%8B%D0%BF%D1%96%D0%BB%D0%B0_%281900%29.jpg/440px-Branisla%C5%AD_Epimach-%C5%A0ypila._%D0%91%D1%80%D0%B0%D0%BD%D1%96%D1%81%D0%BB%D0%B0%D1%9E_%D0%AD%D0%BF%D1%96%D0%BC%D0%B0%D1%85-%D0%A8%D1%8B%D0%BF%D1%96%D0%BB%D0%B0_%281900%29.jpg",
        "description": {
            "by": "Легендарны цэнтр беларускага нацыянальнага адраджэння пачатку XX стагоддзя на Васільеўскім востраве. Тут жыў прафесар Браніслаў Эпімах-Шыпіла, і менавіта ў ягонай кватэры ў 1909–1913 гг. жыў Янка Купала падчас вучобы на курсах Чарняева. Тут збіраліся Цётка, Браніслаў Тарашкевіч, Вацлаў Іваноўскі, і дзейнічала першая беларуская выдавецкая суполка «Загляне сонца і ў наша аконца», якая надрукавала зборнікі «Гусляр», «Адвечная песня» і «Паўлінку».",
            "ru": "Исторический центр белорусского национального возрождения начала XX века. В квартире профессора Эпимах-Шипило в 1909–1913 гг. жил Янка Купала. Здесь собирались Тётка, Тарашкевич, Ивановский и действовало первое белорусское издательство «Загляне сонца і ў наша аконца».",
            "en": "Historic focal point of the early 20th-century Belarusian cultural revival. Poet Yanka Kupala resided here from 1909 to 1913 while studying in Saint Petersburg. The apartment served as headquarters for the publishing society 'Zahliane sontsa i ŭ nasha akontsa'."
        },
        "personIds": ["branislaw-epimakh-shypila", "yanka-kupala"],
        "mustSee": True,
        "links": [
            {"title": "Беларускі Пецярбург (Радыё Свабода)", "url": "https://www.svaboda.org/a/24876672.html"},
            {"title": "Загляне сонца і ў наша аконца (Вікіпедыя)", "url": "https://be.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D1%8F%D0%BD%D0%B5_%D1%81%D0%BE%D0%BD%D1%86%D0%B0_%D1%96_%D1%9E_%D0%BD%D0%B0%D1%88%D0%B0_%D0%B0%D0%BA%D0%BE%D0%BD%D1%86%D0%B0"}
        ]
    },
    {
        "id": "petersburg-national-library-kalinouski",
        "title": {
            "by": "Расійская нацыянальная бібліятэка (Публічная бібліятэка, праца Віктара Каліноўскага і архіў беларусікі)",
            "ru": "Российская национальная библиотека (Публичная библиотека, труды Виктора Калиновского и архив белорусики)",
            "en": "National Library of Russia (Work of Viktar Kalinouski & Archive of Belarussica)"
        },
        "category": "culture",
        "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
        "city": {"by": "Санкт-Пецярбург", "ru": "Санкт-Петербург", "en": "Saint Petersburg"},
        "coordinates": [59.9336, 30.3355],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/National_Library_of_Russia%2C_St._Petersburg.jpg/640px-National_Library_of_Russia%2C_St._Petersburg.jpg",
        "description": {
            "by": "Галоўны корпус Імператарскай публічнай бібліятэкі на рагу Неўскага і Садовай. Тут у 1850-я гг. працаваў гісторык і археограф Віктар Каліноўскі (старэйшы брат Кастуся Каліноўскага), які адшукваў і перапісваў старадаўнія рукапісы і летапісы ВКЛ. Тут захоўваецца велізарны архіў беларусікі: выданні Францыска Скарыны, дыяруш Паўла Сапегі, рукапісы Івана Грыгаровіча, першыя беларускія газеты «Дзянніца» і «Гоман». Тут праводзіліся навуковыя канферэнцыі «Санкт-Пецярбург і беларуская культура» (Мікола Нікалаеў).",
            "ru": "В Императорской публичной библиотеке работал Виктор Калиновский (старший брат Кастуся Калиновского), собиратель летописей ВКЛ. Здесь хранится богатейший архив белорусики: издания Скорины, диариуш Павла Сапеги, рукописи Григоровича.",
            "en": "The Imperial Public Library where historian Viktar Kalinouski (elder brother of Kastus Kalinouski) researched ancient GDL manuscripts. Houses unique Belarusian treasures including Skaryna prints, Sapieha diaries, and the manuscripts of Ivan Hryharovich."
        },
        "personIds": ["kastus-kalinouski", "francysk-skaryna", "ivan-hryharovich"],
        "mustSee": True,
        "links": [
            {"title": "Беларускі Пецярбург (Радыё Свабода)", "url": "https://www.svaboda.org/a/24876672.html"}
        ]
    },
    {
        "id": "petersburg-volkovo-hryharovich",
        "title": {
            "by": "Волкаўскія могілкі — Магіла Івана Грыгаровіча (заснавальніка беларускай археаграфіі)",
            "ru": "Волковское кладбище — Могила Ивана Григоровича (основателя белорусской археографии)",
            "en": "Volkovo Cemetery — Grave of Ivan Hryharovich (Founder of Belarusian Archeography)"
        },
        "category": "grave",
        "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
        "city": {"by": "Санкт-Пецярбург", "ru": "Санкт-Петербург", "en": "Saint Petersburg"},
        "coordinates": [59.9042, 30.3601],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Ivan_Hryharovi%C4%8D._%D0%86%D0%B2%D0%B0%D0%BD_%D0%93%D1%80%D1%8B%D0%B3%D0%B0%D1%80%D0%BE%D0%B2%D1%96%D1%87.jpg/440px-Ivan_Hryharovi%C4%8D._%D0%86%D0%B2%D0%B0%D0%BD_%D0%93%D1%80%D1%8B%D0%B3%D0%B0%D1%80%D0%BE%D0%B2%D1%96%D1%87.jpg",
        "description": {
            "by": "На Волкаўскіх праваслаўных могілках пахаваны Іван Грыгаровіч (1792–1852) — заснавальнік беларускай археаграфіі, ураджэнец Прапойска. Укладальнік першага навуковага збору першакрыніц па гісторыі Беларусі «Беларускі архіў старажытных граматаў» (1824). Побач спачываюць і іншыя выхадцы з Беларусі.",
            "ru": "На Волковском православном кладбище похоронен Иван Григорович (1792–1852) — основоположник белорусской археографии, издатель первого свода источников «Белорусский архив древних грамот» (1824).",
            "en": "Grave of Ivan Hryharovich (1792–1852) at the Volkovo Orthodox Cemetery. Pioneer of Belarusian documentary history and editor of the foundational 'Belarusian Archive of Ancient Deeds' (1824)."
        },
        "personIds": ["ivan-hryharovich"],
        "links": [
            {"title": "Іван Грыгаровіч (Вікіпедыя)", "url": "https://be.wikipedia.org/wiki/%D0%86%D0%B2%D0%B0%D0%BD_%D0%86%D0%B2%D0%B0%D0%BD%D0%B0%D0%B2%D1%96%D1%87_%D0%93%D1%80%D1%8B%D0%B3%D0%B0%D1%80%D0%BE%D0%B2%D1%96%D1%87"}
        ]
    },
    {
        "id": "petersburg-kinofabryka-belarusfilm",
        "title": {
            "by": "Кінастудыя «Савецкая Беларусь» (Ленінградская студыя «Беларусьфільм» 1928–1939)",
            "ru": "Киностудия «Советская Беларусь» (Ленинградская база «Беларусьфильм» 1928–1939)",
            "en": "'Savieckaja Bielaruś' Film Studio (Leningrad Base of Belarusfilm 1928–1939)"
        },
        "category": "culture",
        "country": {"by": "Расія", "ru": "Россия", "en": "Russia"},
        "city": {"by": "Санкт-Пецярбург", "ru": "Санкт-Петербург", "en": "Saint Petersburg"},
        "coordinates": [59.9592, 30.3204],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Kastus_Kalinowski_film_poster_1928.jpg/440px-Kastus_Kalinowski_film_poster_1928.jpg",
        "description": {
            "by": "Першая нацыянальная кінастудыя Савецкай Беларусі была створана і працавала ў Ленінградзе (вул. Малая Пасадская і наб. Мойкі) з 1928 па 1939 год з прычыны адсутнасці ўласнай матэрыяльнай базы ў Менску. Тут рэжысёр Юрый Тарыч і першапраходцы беларускага кінематографа знялі класічныя нямыя і гукавыя фільмы: «Кастусь Каліноўскі» (1928), «Да заўтра» (1929), «Адзінаццаты ліпеня» (1938), якія заклалі асновы нацыянальнага кіно.",
            "ru": "Первая белорусская государственная киностудия «Советская Беларусь» (будущий «Беларусьфильм») работала в Ленинграде с 1928 по 1939 год. Здесь были сняты классические фильмы «Кастусь Калиновский» (1928), «До завтра» и «Одиннадцатое июля».",
            "en": "The pioneering Belarusian film studio operated in Leningrad from 1928 until 1939 before moving fully to Minsk. Groundbreaking national films were shot here, including 'Kastus Kalinouski' (1928) and 'Until Tomorrow' (1929)."
        },
        "personIds": ["kastus-kalinouski"],
        "links": [
            {"title": "Беларусьфільм (Вікіпедыя)", "url": "https://be.wikipedia.org/wiki/%D0%91%D0%B5%D0%BB%D0%B0%D1%80%D1%83%D1%81%D1%8C%D1%84%D1%96%D0%BB%D1%8C%D0%BC"}
        ]
    },
    # GDL Heritage Sites (from vkl.by)
    {
        "id": "basel-munster-vkl-embassy",
        "title": {
            "by": "Базельскі кафедральны сабор (Пасольства ВКЛ на Базельскім саборы 1433–1434 гг.)",
            "ru": "Базельский собор (Посольство ВКЛ на Базельском соборе 1433–1434 гг.)",
            "en": "Basel Minster (Embassy of the GDL to the Council of Basel 1433–1434)"
        },
        "category": "historical",
        "country": {"by": "Швейцарыя", "ru": "Швейцария", "en": "Switzerland"},
        "city": {"by": "Базель", "ru": "Базель", "en": "Basel"},
        "coordinates": [47.5564, 7.5925],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Basler_M%C3%BCnster_2021.jpg/640px-Basler_M%C3%BCnster_2021.jpg",
        "description": {
            "by": "У велічным гатычным Базельскім кафедральным саборы ў 1431–1449 гг. праходзіў сусветны Базельскі сабор. У 1433–1434 гг. сюды прыбыло ўрачыстае дыпламатычнае пасольства Вялікага Княства Літоўскага, накіраванае вялікім князем літоўскім Свідрыгайлам і мітрапалітам Кіеўскім і ўсяе Русі Герасімам. Пасольства дамаглося міжнароднага прызнання самастойнасці ВКЛ і вяло перамовы аб царкоўнай уніі, замацаваўшы высокі еўрапейскі статус беларуска-літоўскай дзяржавы.",
            "ru": "В Базельском соборе заседал Вселенский собор. В 1433–1434 гг. сюда прибыло официальное посольство Великого Княжества Литовского от великого князя Свидригайло и митрополита Герасима, добившееся признания суверенитета ВКЛ в европейской политике.",
            "en": "Site of the Council of Basel. In 1433–1434, an official embassy from the Grand Duchy of Lithuania, sent by Grand Duke Švitrigaila and Metropolitan Gerasim, presented credentials to the Council, asserting the sovereign status of the GDL in European diplomacy."
        },
        "mustSee": True,
        "links": [
            {"title": "Базельскі сабор (vkl.by)", "url": "http://web.archive.org/web/20210512140534/http://vkl.by/articles/203"}
        ]
    },
    {
        "id": "padua-palazzo-bo-vkl-students",
        "title": {
            "by": "Палацца Бо ў Падуанскім універсітэце («Natio Ruthena et Lithuana», гербы студэнтаў ВКЛ)",
            "ru": "Палаццо Бо в Падуанском университете («Natio Ruthena et Lithuana», гербы студентов ВКЛ)",
            "en": "Palazzo Bo at University of Padua ('Natio Ruthena et Lithuana', GDL Student Crests)"
        },
        "category": "culture",
        "country": {"by": "Італія", "ru": "Италия", "en": "Italy"},
        "city": {"by": "Падуя", "ru": "Падуя", "en": "Padua"},
        "coordinates": [45.4069, 11.8778],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Palazzo_del_Bo_Padova_cortile.jpg/640px-Palazzo_del_Bo_Padova_cortile.jpg",
        "description": {
            "by": "Гістарычны галоўны корпус Падуанскага ўніверсітэта (заснаванага ў 1222 г.). Тут у 1512 годзе Францыск Скарына бліскуча абараніў ступень доктара лекарскіх навук (яго партрэт упрыгожвае Залу Сарака). У двары і галерэях Палацца Бо высечаны сотні студэнцкіх гербаў, у тым ліку прадстаўнікоў ВКЛ карпарацыі «Natio Ruthena et Lithuana»: Радзівілаў, Валовічаў, Сапегаў, Агрыпаў, якія атрымлівалі тут перадавую еўрапейскую адукацыю.",
            "ru": "Исторический центр Падуанского университета. Здесь в 1512 году Франциск Скорина защитил степень доктора медицинских наук. Во дворе Палаццо Бо сохранились гербы студентов из ВКЛ (корпорация Natio Ruthena et Lithuana) — Радзивиллов, Воловичей, Сапег.",
            "en": "The historic core of the University of Padua. Francysk Skaryna defended his doctorate in medicine here in 1512 (his portrait hangs in the 'Sala dei Quaranta'). The Renaissance courtyard features carved crests of students from the Grand Duchy of Lithuania."
        },
        "personIds": ["francysk-skaryna", "radziwills", "radziwill-sirotka"],
        "mustSee": True,
        "links": [
            {"title": "Падуанскі ўніверсітэт (Вікіпедыя)", "url": "https://be.wikipedia.org/wiki/%D0%9F%D0%B0%D0%B4%D1%83%D0%B0%D0%BD%D1%81%D0%BA%D1%96_%D1%9E%D0%BD%D1%96%D0%B2%D0%B5%D1%80%D1%81%D1%96%D1%82%D1%8D%D1%82"}
        ]
    },
    {
        "id": "krakow-bursa-litwanorum",
        "title": {
            "by": "Бурса Ліцвінаў і Русінаў (Bursa Litwanorum, Ягелонскі ўніверсітэт у Кракаве)",
            "ru": "Бурса Литвинов и Русинов (Bursa Litwanorum, Ягеллонский университет в Кракове)",
            "en": "Lithuanian-Ruthenian Hall (Bursa Litwanorum, Jagiellonian University in Kraków)"
        },
        "category": "historical",
        "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
        "city": {"by": "Кракаў", "ru": "Краков", "en": "Krakow"},
        "coordinates": [50.0617, 19.9339],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Krak%C3%B3w_Collegium_Maius_dziedziniec.jpg/640px-Krak%C3%B3w_Collegium_Maius_dziedziniec.jpg",
        "description": {
            "by": "Студэнцкая рэзідэнцыя (бурса), заснаваная ў 1397 годзе каралевай Ядвігай пры Кракаўскім універсітэце адмыслова для выхадцаў з Вялікага Княства Літоўскага і Русі (Bursa Litwanorum / Bursa Pauperum на вул. Вісьльнай). Тут жылі і рыхтаваліся да заняткаў першыя беларускія студэнты, у тым ліку Францыск Скарына падчас свайго навучання ў Кракаве (1504–1506).",
            "ru": "Студенческое общежитие, основанное в 1397 году королевой Ядвигой при Краковском университете специально для студентов из ВКЛ и Руси. Здесь жили первые белорусские студенты, включая Франциска Скорину в 1504–1506 годах.",
            "en": "Student hall founded in 1397 by Queen Jadwiga at Kraków University specifically for students hailing from the Grand Duchy of Lithuania and Ruthenia. Provided accommodation to pioneering Belarusian scholars, including Francysk Skaryna (1504–1506)."
        },
        "personIds": ["francysk-skaryna"],
        "mustSee": True,
        "links": [
            {"title": "Ягелонскі ўніверсітэт (Вікіпедыя)", "url": "https://be.wikipedia.org/wiki/%D0%AF%D0%B3%D0%B5%D0%BB%D0%BE%D0%BD%D1%81%D0%BA%D1%96_%D1%9E%D0%BD%D1%96%D0%B2%D0%B5%D1%80%D1%81%D1%96%D1%82%D1%8D%D1%82"}
        ]
    },
    {
        "id": "sinia-vody-battlefield-memorial",
        "title": {
            "by": "Мемарыял бітвы на Сініх Водах 1362 года (перамога князя Альгерда над татарамі)",
            "ru": "Мемориал битвы на Синих Водах 1362 года (победа князя Ольгерда над татарами)",
            "en": "Battle of Blue Waters Memorial 1362 (Algirdas Victory over the Golden Horde)"
        },
        "category": "historical",
        "country": {"by": "Украіна", "ru": "Украина", "en": "Ukraine"},
        "city": {"by": "Тарговіца", "ru": "Торговица", "en": "Torhovytsya"},
        "coordinates": [48.6583, 30.7783],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Pamyatnyk_Syni_Vody.jpg/640px-Pamyatnyk_Syni_Vody.jpg",
        "description": {
            "by": "Поле славутай бітвы восені 1362 года каля ракі Сінюха (Сінія Воды). Аб'яднанае беларуска-літоўскае войска Вялікага Княства Літоўскага пад кіраўніцтвам вялікага князя Альгерда ўшчэнт разграміла войскі трох татарскіх кіраўнікоў (Хачыбея, Кутлубугі і Дзмітрыя). Гэтая эпахальная перамога вызваліла Кіеўшчыну, Падолле і Пераяслаўшчыну ад татарскага ярма і замацавала межы ВКЛ да Чорнага мора. На месцы бітвы ўсталяваны мемарыяльны памятны знак і крыж.",
            "ru": "Место битвы осени 1362 года на реке Синюхе. Войско ВКЛ под командованием великого князя Ольгерда разгромило войска трёх ордынских ханов, освободив Киевщину и Подолье от власти Золотой Орды. На месте битвы установлен мемориал.",
            "en": "Historic site of the pivotal Battle of Blue Waters in autumn 1362. The army of the Grand Duchy of Lithuania led by Grand Duke Algirdas decisively defeated three Golden Horde khans, liberating Kyiv and Podolia. Commemorated by a memorial cross and monument."
        },
        "personIds": ["alhierd"],
        "mustSee": True,
        "links": [
            {"title": "Бітва на Сініх Водах (Вікіпедыя)", "url": "https://be.wikipedia.org/wiki/%D0%91%D1%96%D1%82%D0%B2%D0%B0_%D0%BD%D0%B0_%D0%A1%D1%96%D0%BD%D1%96%D1%85_%D0%92%D0%BE%D0%B4%D0%B0%D1%85"}
        ]
    },
    {
        "id": "salaspils-kirchholm-battle-memorial",
        "title": {
            "by": "Поле бітвы пад Кірхгольмам 1605 года (трыумф гетмана Яна Караля Хадкевіча)",
            "ru": "Поле битвы при Кирхгольме 1605 года (триумф гетмана Яна Кароля Ходкевича)",
            "en": "Battle of Kirchholm Memorial 1605 (Jan Karol Chodkiewicz Triumph)"
        },
        "category": "monument",
        "country": {"by": "Латвія", "ru": "Латвия", "en": "Latvia"},
        "city": {"by": "Саласпілс", "ru": "Саласпилс", "en": "Salaspils"},
        "coordinates": [56.8586, 24.3486],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Jan_Karol_Chodkiewicz.PNG/440px-Jan_Karol_Chodkiewicz.PNG",
        "description": {
            "by": "27 верасня 1605 года каля Кірхгольма (цяпер Саласпілс пад Рыгай) 4-тысячнае войска Вялікага Княства Літоўскага пад кіраўніцтвам вялікага гетмана Яна Караля Хадкевіча ўшчэнт разграміла 14-тысячную армію шведскага караля Карла IX. Дзякуючы бліскучай тактыцы гетмана і імклівай атацы крылатай гусарыі ВКЛ бітва ўвайшла ва ўсе сусветныя ваенныя падручнікі. У Саласпілсе ўсталяваны памятны знак перамогі войска ВКЛ.",
            "ru": "27 сентября 1605 года 4-тысячное войско ВКЛ под предводительством Яна Кароля Ходкевича наголову разбило 14-тысячную армию шведского короля Карла IX. Блистательный триумф тактики крылатых гусар ВКЛ. В Саласпилсе установлен памятный камень.",
            "en": "Site of the legendary Battle of Kirchholm on 27 September 1605. Grand Hetman Jan Karol Chodkiewicz led 4,000 GDL troops, spearheaded by winged hussars, to annihilate a Swedish royal army of 14,000. Marked by a memorial stone in Salaspils."
        },
        "personIds": ["jan-karol-chodkiewicz"],
        "mustSee": True,
        "links": [
            {"title": "Бітва пад Кірхгольмам (Вікіпедыя)", "url": "https://be.wikipedia.org/wiki/%D0%91%D1%96%D1%82%D0%B2%D0%B0_%D0%BF%D0%B0%D0%B4_%D0%9A%D1%96%D1%80%D1%85%D0%B3%D0%BE%D0%BB%D1%8C%D0%BC%D0%B0%D0%BC"}
        ]
    },
    {
        "id": "suprasl-annunciation-monastery",
        "title": {
            "by": "Супрасльскі Дабравешчанскі манастыр (абарончы гатычны сабор ВКЛ і асяродак летапісання)",
            "ru": "Супрасльский Благовещенский монастырь (оборонный готический собор ВКЛ и центр летописания)",
            "en": "Supraśl Annunciation Monastery (Fortified Gothic Cathedral of the GDL)"
        },
        "category": "church",
        "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
        "city": {"by": "Супрасль", "ru": "Супрасль", "en": "Suprasl"},
        "coordinates": [53.2097, 23.3369],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Monaster_w_Supra%C5%9Blu_2020.jpg/640px-Monaster_w_Supra%C5%9Blu_2020.jpg",
        "description": {
            "by": "Заснаваны ў 1498 г. маршалкам ВКЛ Аляксандрам Хадкевічам і праваслаўным архіепіскапам Іосіфам Солтанам. Галоўны храм — унікальны ўзор беларускай абарончай готыкі ВКЛ XVI стагоддзя з чатырма кутнімі байнічнымі вежамі і фрэскамі. Адзін з найважнейшых асяродкаў летапісання і кніжнасці ВКЛ (тут створаны Супрасльскі летапіс і доўгі час зберагаўся знакаміты Супрасльскі рукапіс XI ст. — помнік сусветнай спадчыны ЮНЕСКА).",
            "ru": "Основан в 1498 году маршалком ВКЛ Александром Ходкевичем. Уникальный шедевр оборонной готики Великого Княжества Литовского с четырьмя угловыми башнями. Крупнейший центр летописания ВКЛ, хранитель Супрасльской рукописи XI века (ЮНЕСКО).",
            "en": "Founded in 1498 by GDL Marshal Aleksander Chodkiewicz. Features a rare fortified Gothic cathedral of the Grand Duchy of Lithuania with four defensive towers. A paramount center of Belarusian chronicle writing and home to the 11th-century Codex Suprasliensis (UNESCO Memory of the World)."
        },
        "personIds": ["jan-karol-chodkiewicz"],
        "mustSee": True,
        "links": [
            {"title": "Супрасльскі Дабравешчанскі манастыр (Вікіпедыя)", "url": "https://be.wikipedia.org/wiki/%D0%A1%D1%83%D0%BF%D1%80%D0%B0%D1%81%D0%BB%D1%8C%D1%81%D0%BA%D1%96_%D0%94%D0%B0%D0%B1%D1%80%D0%B0%D0%B2%D0%B5%D1%88%D1%87%D0%B0%D0%BD%D1%81%D0%BA%D1%96_%D0%BC%D0%B0%D0%BD%D0%B0%D1%81%D1%82%D1%8B%D1%80"}
        ]
    },
    {
        "id": "koden-sanctuary-sapieha-castle",
        "title": {
            "by": "Кодэнь — Санктуарый Маці Божай Кодэньскай і замак Сапегаў",
            "ru": "Кодень — Санктуарий Матери Божьей Коденьской и замок Сапег",
            "en": "Kodeń Sanctuary of Our Lady of Kodeń & Sapieha Castle"
        },
        "category": "church",
        "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
        "city": {"by": "Кодэнь", "ru": "Кодень", "en": "Koden"},
        "coordinates": [51.9142, 23.6067],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Ko%C5%9Bci%C3%B3%C5%82_%C5%9Bw._Anny_w_Kodniu.JPG/640px-Ko%C5%9Bci%C3%B3%C5%82_%C5%9Bw._Anny_w_Kodniu.JPG",
        "description": {
            "by": "Галоўная радавая рэзідэнцыя Сапегаў на Падляшшы на беразе Буга ля самай мяжы з Брэстам. У барочнай базіліцы Святой Ганны (1629–1635) зберагаецца цудатворны абраз Маці Божай Кодэньскай, вывезены Мікалаем Сапегам «Піем» з Рыма. У парку захаваліся валы замка Сапегаў і гатычная капліца Святога Духа (1530–1540) — выдатны помнік абарончага дойлідства ВКЛ.",
            "ru": "Родовая резиденция Сапег на Подляшье близ Бреста. Базилика Святой Анны хранит чудотворную икону Матери Божьей Коденьской, вывезенную Николаем Сапегой из Рима. Сохранилась замковая готическая каплица Святого Духа (1530-е гг.).",
            "en": "Ancestral seat of the Sapieha magnate family on the Bug River facing Brest. The Baroque Basilica of St. Anne houses the miraculous icon of Our Lady of Kodeń, brought from Rome by Mikołaj Sapieha. The site preserves castle ramparts and the Gothic Holy Spirit Chapel."
        },
        "personIds": ["lew-sapieha"],
        "mustSee": True,
        "links": [
            {"title": "Кодэнь (Вікіпедыя)", "url": "https://be.wikipedia.org/wiki/%D0%9A%D0%BE%D0%B4%D1%8D%D0%BD%D1%8C"}
        ]
    },
    {
        "id": "szydlowiec-radziwill-castle",
        "title": {
            "by": "Шыдловецкі замак Радзівілаў (сталіца Шыдлавецкага графства)",
            "ru": "Шидловецкий замок Радзивиллов (столица Шидловецкого графства)",
            "en": "Szydłowiec Radziwiłł Castle (Capital of the County of Szydłowiec)"
        },
        "category": "historical",
        "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
        "city": {"by": "Шыдловец", "ru": "Шидловец", "en": "Szydlowiec"},
        "coordinates": [51.2231, 20.9317],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Szydlowiec_zamek.jpg/640px-Szydlowiec_zamek.jpg",
        "description": {
            "by": "Рэнесансны замак на выспе сярод става, набыты Мікалаем Радзівілам «Чорным» у 1548 г. На працягу 250 гадоў (да 1802 г.) замак з'яўляўся галоўнай рэзідэнцыяй Шыдлавецкага графства Радзівілаў. Замак быў перабудаваны Мікалаем Крыштафам Радзівілам «Сіроткам» і Альбрэхтам Радзівілам. Цяпер тут месціцца Музей народных музычных інструментаў.",
            "ru": "Ренессансный замок на острове, приобретённый Николаем Радзивиллом «Чёрным» в 1548 году. На протяжении 250 лет — главная резиденция Шидловецкого графства Радзивиллов, перестроен замковыми зодчими Сиротки.",
            "en": "A Renaissance water castle acquired by Mikołaj 'the Black' Radziwiłł in 1548. Served as the principal seat of the Radziwiłł County of Szydłowiec for 250 years. Substantially remodeled under Mikołaj 'the Orphan' Radziwiłł."
        },
        "personIds": ["radziwills", "mikolaj-radziwill-black", "radziwill-sirotka"],
        "mustSee": True,
        "links": [
            {"title": "Шыдловецкі замак (Вікіпедыя)", "url": "https://be.wikipedia.org/wiki/%D0%A8%D1%8B%D0%B4%D0%BB%D0%BE%D0%B2%D0%B5%D1%86%D0%BA%D1%96_%D0%B7%D0%B0%D0%BC%D0%B0%D0%BA"}
        ]
    },
    {
        "id": "medininkai-castle",
        "title": {
            "by": "Замак Меднікі (магутны каменны кастэль ВКЛ XIV ст. ля беларускай мяжы)",
            "ru": "Замок Медники (мощный каменный кастель ВКЛ XIV в. у белорусской границы)",
            "en": "Medininkai Castle (Grand 14th-Century GDL Enclosure Castle)"
        },
        "category": "historical",
        "country": {"by": "Літва", "ru": "Литва", "en": "Lithuania"},
        "city": {"by": "Мядзінінкай", "ru": "Мядининкай", "en": "Medininkai"},
        "coordinates": [54.5397, 25.6500],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Medininkai_castle_2013.JPG/640px-Medininkai_castle_2013.JPG",
        "description": {
            "by": "Адзін з найбуйнейшых мураваных замкаў-кастэляў Вялікага Княства Літоўскага, пабудаваны ў першай палове XIV ст. вялікімі князямі Гедзімінам і Альгердам усяго за некалькі кіламетраў ад сучаснай мяжы з Ашмянскім раёнам. Меў велічныя сцены вышынёй да 15 метраў і чатыры вежы з галоўным данжонам. Цэнтр абароны Віленскай зямлі ад крыжакоў і рэзідэнцыя каралевіча Казіміра.",
            "ru": "Один из крупнейших каменных замков-кастелей ВКЛ XIV века, возведённый князьями Гедимином и Ольгердом у самой границы с современной Беларусью. Мощные стены высотой до 15 метров защищали Виленскую землю от крестоносцев.",
            "en": "One of the largest stone enclosure castles of the Grand Duchy of Lithuania, built in the early 14th century by Grand Dukes Gediminas and Algirdas near the present-day Belarusian border. Boasted 15-meter-high defensive walls."
        },
        "personIds": ["alhierd"],
        "mustSee": True,
        "links": [
            {"title": "Медніцкі замак (Вікіпедыя)", "url": "https://be.wikipedia.org/wiki/%D0%9C%D0%B5%D0%B4%D0%BD%D1%96%D1%86%D0%BA%D1%96_%D0%B7%D0%B0%D0%BC%D0%B0%D0%BA"}
        ]
    },
    {
        "id": "florence-santa-croce-oginski-tomb",
        "title": {
            "by": "Базіліка Санта-Крочэ ў Фларэнцыі — Магіла Міхала Клеафаса Агінскага",
            "ru": "Базилика Санта-Кроче во Флоренции — Могила Михаила Клеофаса Огинского",
            "en": "Basilica of Santa Croce, Florence — Tomb of Michał Kleofas Ogiński"
        },
        "category": "grave",
        "country": {"by": "Італія", "ru": "Италия", "en": "Italy"},
        "city": {"by": "Фларэнцыя", "ru": "Флоренция", "en": "Florence"},
        "coordinates": [43.7686, 11.2622],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Santa_Croce_-_Monumento_Oginski.jpg/440px-Santa_Croce_-_Monumento_Oginski.jpg",
        "description": {
            "by": "У славутай базіліцы Санта-Крочэ ў Фларэнцыі — Пантэоне Італіі, дзе спачываюць Мікеланджэла, Галілей і Макіявелі — пахаваны выдатны дзяржаўны дзеяч ВКЛ і кампазітар Міхал Клеафас Агінскі (1765–1833), аўтар знакамітага паланэза «Развітанне з Радзімай». Мармуровы помнік Агінскаму з партрэтным барэльефам усталяваны ў капліцы Кастэлані.",
            "ru": "В знаменитой базилике Санта-Кроче во Флоренции (итальянском Пантеоне рядом с Микеланджело и Галилеем) покоится автор бессмертного полонеза «Прощание с Родиной» Михаил Клеофас Огинский. Мраморный памятник расположен в капелле Кастеллани.",
            "en": "Located inside Florence's Basilica of Santa Croce (the Italian Pantheon, alongside Michelangelo and Galileo). Tomb and marble memorial monument to composer and GDL statesman Michał Kleofas Ogiński, creator of the 'Farewell to the Homeland' Polonaise."
        },
        "personIds": ["michal-kleofas-oginski"],
        "mustSee": True,
        "links": [
            {"title": "Міхал Клеафас Агінскі (Вікіпедыя)", "url": "https://be.wikipedia.org/wiki/%D0%9C%D1%96%D1%85%D0%B0%D0%BB_%D0%9A%D0%BB%D0%B5%D0%B0%D1%84%D0%B0%D1%81_%D0%90%D0%B3%D1%96%D0%BD%D1%81%D0%BA%D1%96"}
        ]
    },
    {
        "id": "warsaw-teatr-wielki-moniuszko",
        "title": {
            "by": "Помнік Станіславу Манюшку перад Тэатрам Вялікім у Варшаве",
            "ru": "Памятник Станиславу Монюшко перед Большим театром в Варшаве",
            "en": "Stanisław Moniuszko Monument at Teatr Wielki in Warsaw"
        },
        "category": "monument",
        "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
        "city": {"by": "Варшава", "ru": "Варшава", "en": "Warsaw"},
        "coordinates": [52.2439, 21.0108],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Pomnik_Stanis%C5%82awa_Moniuszki_w_Warszawie.JPG/640px-Pomnik_Stanis%C5%82awa_Moniuszki_w_Warszawie.JPG",
        "description": {
            "by": "Манументальны помнік стваральніку нацыянальнай класічнай оперы Станіславу Манюшку (1819–1872), ураджэнцу фальварка Убель пад Ігуменам (Чэрвенем). Усталяваны на Тэатральнай плошчы перад галоўным фасадам Нацыянальнай оперы Польшчы (Тэатра Вялікага), дзе Манюшка працаваў дырэктарам оперы і дзе адбыліся трыумфальныя пастаноўкі опер «Галька» і «Страшны двор».",
            "ru": "Памятник создателю национальной классической оперы Станиславу Монюшко, уроженцу имения Убель под Минском. Расположен на Театральной площади перед Большим театром, где композитор руководил оперной труппой.",
            "en": "Monument to the founder of Polish and Belarusian national opera, Stanisław Moniuszko (born in Ubel near Chervyen, Belarus). Stands on Theatre Square in front of Teatr Wielki, where Moniuszko served as opera director."
        },
        "personIds": ["stanislaw-moniuszko"],
        "mustSee": True,
        "links": [
            {"title": "Станіслаў Манюшка (Вікіпедыя)", "url": "https://be.wikipedia.org/wiki/%D0%A1%D1%82%D0%B0%D0%BD%D1%96%D1%81%D0%BB%D0%B0%D1%9E_%D0%9C%D0%B0%D0%BD%D1%8E%D1%88%D0%BA%D0%B0"}
        ]
    },
    {
        "id": "warsaw-powazki-kapuscinski-grave",
        "title": {
            "by": "Вайсковыя могілкі Павонзкі — Магіла Рышарда Капусцінскага (Варшава)",
            "ru": "Воинское кладбище Повонзки — Могила Рышарда Капущинского (Варшава)",
            "en": "Powązki Military Cemetery — Grave of Ryszard Kapuściński (Warsaw)"
        },
        "category": "grave",
        "country": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
        "city": {"by": "Варшава", "ru": "Варшава", "en": "Warsaw"},
        "coordinates": [52.2583, 20.9531],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Ryszard_Kapu%C5%9Bci%C5%84ski_2003_%28cropped%29.jpg/440px-Ryszard_Kapu%C5%9Bci%C5%84ski_2003_%28cropped%29.jpg",
        "description": {
            "by": "На Алеі заслужаных знакамітых Вайсковых могілак Павонзкі ў Варшаве пахаваны сусветна вядомы рэпарцёр і пісьменнік Рышард Капусцінскі (1932–2007), ураджэнец Пінска. Надмагільны помнік з чорнага граніту з лаканічным аўтографам пісьменніка стаў месцам ушанавання літаратараў з усяго свету.",
            "ru": "На Аллее заслуженных Воинского кладбища Повонзки в Варшаве похоронен уроженец Пинска, всемирно признанный классик репортажа Рышард Капущинский (1932–2007).",
            "en": "Located in the Avenue of the Merited at Warsaw's Powązki Military Cemetery. Grave of Pinsk-born literary reporter and author Ryszard Kapuściński (1932–2007)."
        },
        "personIds": ["ryszard-kapuscinski"],
        "links": [
            {"title": "Рышард Капусцінскі (Вікіпедыя)", "url": "https://be.wikipedia.org/wiki/%D0%A1%D1%82%D0%B0%D0%BD%D1%96%D1%81%D0%BB%D0%B0%D1%9E_%D0%9C%D0%B0%D0%BD%D1%8E%D1%88%D0%BA%D0%B0"}
        ]
    },
    {
        "id": "paris-la-ruche-montparnasse",
        "title": {
            "by": "Фаланстэр мастакоў «Вулей» (La Ruche, Парыж — асяродак Суціна, Шагала і Цадкіна)",
            "ru": "Фаланстер художников «Улей» (La Ruche, Париж — обитель Сутина, Шагала и Цадкина)",
            "en": "'La Ruche' Artists' Colony (Paris — Haven of Soutine, Chagall & Zadkine)"
        },
        "category": "culture",
        "country": {"by": "Францыя", "ru": "Франция", "en": "France"},
        "city": {"by": "Парыж", "ru": "Париж", "en": "Paris"},
        "coordinates": [48.8317, 2.2989],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/La_Ruche%2C_passage_de_Dantzig%2C_Paris_15e.jpg/640px-La_Ruche%2C_passage_de_Dantzig%2C_Paris_15e.jpg",
        "description": {
            "by": "Знакаміты фаланстэр мастакоў Манпарнаса ў 15-й акрузе Парыжа (Passage de Dantzig, 2). Менавіта тут, у круглым трохпавярховым ратондавым будынку, знаходзіліся майстэрні выхадцаў з Беларусі — зорных майстроў Парыжскай школы: Марка Шагала, Хаіма Суціна, Восіпа Цадкіна, Пінхуса Крэменя і Міхаіла Кікоіна. Тут нараджаліся шэдэўры сусветнага экспрэсіянізму і авангарда.",
            "ru": "Знаменитый фаланстер художников на Монпарнасе в Париже. В «Улье» жили и работали уроженцы Беларуси, ставшие лидерами Парижской школы: Марк Шагал, Хаим Сутин, Осип Цадкин, Пинхус Кремень и Михаил Кикоин.",
            "en": "Historic artists' settlement in the 15th arrondissement of Paris. Served as home and studio for Belarusian-born giants of the School of Paris: Marc Chagall, Chaïm Soutine, Ossip Zadkine, Pinchus Kremegne, and Michel Kikoine."
        },
        "personIds": ["marc-chagall", "chaim-soutine", "ossip-zadkine"],
        "mustSee": True,
        "links": [
            {"title": "La Ruche (Вікіпедыя)", "url": "https://be.wikipedia.org/wiki/%D0%92%D1%83%D0%BB%D0%B5%D0%B9_(%D1%84%D0%B0%D0%BB%D0%B0%D0%BD%D1%81%D1%82%D1%8D%D1%80)"}
        ]
    },
    {
        "id": "paris-montparnasse-soutine-grave",
        "title": {
            "by": "Могілкі Манпарнас — Магіла Хаіма Суціна (Парыж)",
            "ru": "Кладбище Монпарнас — Могила Хаима Сутина (Париж)",
            "en": "Montparnasse Cemetery — Grave of Chaïm Soutine (Paris)"
        },
        "category": "grave",
        "country": {"by": "Францыя", "ru": "Франция", "en": "France"},
        "city": {"by": "Парыж", "ru": "Париж", "en": "Paris"},
        "coordinates": [48.8394, 2.3275],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Tombe_Chaim_Soutine.JPG/640px-Tombe_Chaim_Soutine.JPG",
        "description": {
            "by": "На знакамітых могілках Манпарнас у Парыжы пахаваны адзін з найвялікшых жывапісцаў-экспрэсіяністаў XX стагоддзя Хаім Суцін (1893–1943), ураджэнец мястэчка Смілавічы пад Мінскам. Помнік мастаку з'яўляецца месцам паломніцтва аматараў мастацтва з усяго свету.",
            "ru": "На знаменитом кладбище Монпарнас в Париже похоронен гений экспрессионизма Хаим Сутин (1893–1943), уроженец Смиловичей под Минском.",
            "en": "Located at the Cimetière du Montparnasse in Paris. Grave of master expressionist painter Chaïm Soutine (1893–1943), who was born in Smilavichy near Minsk (Belarus)."
        },
        "personIds": ["chaim-soutine"],
        "links": [
            {"title": "Хаім Суцін (Вікіпедыя)", "url": "https://be.wikipedia.org/wiki/%D0%A5%D0%B0%D1%96%D0%BC_%D0%A1%D1%83%D1%86%D1%96%D0%BD"}
        ]
    },
    {
        "id": "paris-batignolles-bakst-grave",
        "title": {
            "by": "Баціньёльскія могілкі — Магіла Леона Бакста (Парыж)",
            "ru": "Батиньольское кладбище — Могила Леона Бакста (Париж)",
            "en": "Batignolles Cemetery — Grave of Léon Bakst (Paris)"
        },
        "category": "grave",
        "country": {"by": "Францыя", "ru": "Франция", "en": "France"},
        "city": {"by": "Парыж", "ru": "Париж", "en": "Paris"},
        "coordinates": [48.8953, 2.3150],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Leon_Bakst_grave_Batignolles.jpg/640px-Leon_Bakst_grave_Batignolles.jpg",
        "description": {
            "by": "На Баціньёльскіх могілках у Парыжы спачывае геніяльны сцэнограф, мадэльер і мастак Леон Бакст (Лейб-Хаім Розенберг, 1866–1924), які нарадзіўся ў Гродне. Ягоныя касцюмы і дэкарацыі для «Рускіх сезонаў» Дзягілева ў Парыжы зрабілі рэвалюцыю ў сусветным тэатральным і дэкаратыўным мастацтве і дызайне.",
            "ru": "На Батиньольском кладбище в Париже похоронен гениальный театральный художник и модельер Леон Бакст (1866–1924), родившийся в Гродно. Декорации Бакста для «Русских сезонов» Дягилева произвели мировую революцию в сценографии.",
            "en": "Grave of Grodno-born painter and stage designer Léon Bakst (1866–1924) at the Cimetière des Batignolles in Paris. Bakst's revolutionary set and costume designs for Diaghilev's Ballets Russes transformed modern stage aesthetics and haute couture."
        },
        "personIds": ["leon-bakst"],
        "links": [
            {"title": "Леон Бакст (Вікіпедыя)", "url": "https://be.wikipedia.org/wiki/%D0%9B%D0%B5%D0%BE%D0%BD_%D0%91%D0%B0%D0%BA%D1%81%D1%82"}
        ]
    },
    {
        "id": "rotterdam-zadkine-destroyed-city",
        "title": {
            "by": "Манумент «Разбураны горад» Восіпа Цадкіна (Ратэрдам, Нідэрланды)",
            "ru": "Монумент «Разрушенный город» Осипа Цадкина (Роттердам, Нидерланды)",
            "en": "'The Destroyed City' Monument by Ossip Zadkine (Rotterdam, Netherlands)"
        },
        "category": "monument",
        "country": {"by": "Нідэрланды", "ru": "Нидерланды", "en": "Netherlands"},
        "city": {"by": "Ратэрдам", "ru": "Роттердам", "en": "Rotterdam"},
        "coordinates": [51.9189, 4.4828],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/De_Verwoeste_Stad_Rotterdam.jpg/640px-De_Verwoeste_Stad_Rotterdam.jpg",
        "description": {
            "by": "Сусветна знакаміты бронзавы манумент «De Verwoeste Stad» (вышынёй 6 метраў), створаны ўраджэнцам Віцебска скульптарам Восіпам Цадкінам і адкрыты ў 1953 г. на плошчы Плейн 1940. Экспрэсіўная постаць з вырваным сэрцам увасабляе трагедыю Ратэрдама, знішчанага нацысцкімі бамбардзіроўкамі 1940 года. Адзін з найвялікшых антываенных помнікаў сусветнага мастацтва XX стагоддзя.",
            "ru": "Всемирно известный монумент уроженца Витебска скульптора Осипа Цадкина «Разрушенный город» (1953) в Роттердаме. Экспрессивная шестиметровая фигура с вырванным сердцем признана одним из величайших антивоенных памятников XX века.",
            "en": "Iconic 6-meter bronze monument 'De Verwoeste Stad' (The Destroyed City, 1953) created by Vitebsk-born sculptor Ossip Zadkine. Depicting a human figure with a hollow chest where the heart was torn out, it stands as a world-renowned anti-war masterpiece in central Rotterdam."
        },
        "personIds": ["ossip-zadkine"],
        "mustSee": True,
        "links": [
            {"title": "Разбураны горад (Вікіпедыя)", "url": "https://be.wikipedia.org/wiki/%D0%A0%D0%B0%D0%B7%D0%B1%D1%83%D1%80%D0%B0%D0%BD%D1%8B_%D0%B3%D0%BE%D1%80%D0%B0%D0%B4"}
        ]
    },
    {
        "id": "paris-musee-zadkine",
        "title": {
            "by": "Музей Восіпа Цадкіна (дом-майстэрня на Rue d'Assas 100bis, Парыж)",
            "ru": "Музей Осипа Цадкина (дом-мастерская на Rue d'Assas 100bis, Париж)",
            "en": "Musée Zadkine (Home-Studio on Rue d'Assas 100bis, Paris)"
        },
        "category": "culture",
        "country": {"by": "Францыя", "ru": "Франция", "en": "France"},
        "city": {"by": "Парыж", "ru": "Париж", "en": "Paris"},
        "coordinates": [48.8431, 2.3339],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Mus%C3%A9e_Zadkine_Paris_garden.jpg/640px-Mus%C3%A9e_Zadkine_Paris_garden.jpg",
        "description": {
            "by": "Мемарыяльны дом і сад скульптур на Манпарнасе, дзе віцебскі майстар Восіп Цадкін жыў і тварыў з 1928 года да сваёй смерці ў 1967 г. Экспануюцца арыгінальныя скульптуры з дрэва, мармуру і бронзы, гуашы і фатаграфіі скульптара, які захаваў памяць пра Віцебск і Дзвіну на ўсё жыццё.",
            "ru": "Дом-мастерская и сад скульптур Осипа Цадкина на Монпарнасе в Париже, где скульптор работал с 1928 по 1967 год. В коллекции музея — более 300 скульптур, гуашей и рисунков уроженца Витебска.",
            "en": "Memorial studio museum and sculpture garden where Vitebsk-born cubist sculptor Ossip Zadkine lived and created from 1928 until his death in 1967. Houses over 300 works in wood, bronze, and stone near the Jardin du Luxembourg in Paris."
        },
        "personIds": ["ossip-zadkine"],
        "mustSee": True,
        "links": [
            {"title": "Музей Цадкіна (Вікіпедыя)", "url": "https://be.wikipedia.org/wiki/%D0%9C%D1%83%D0%B7%D0%B5%D0%B9_%D0%A6%D0%B0%D0%B4%D0%BA%D1%96%D0%BD%D0%B0"}
        ]
    },
    {
        "id": "wiesbaden-neroberg-boris-kit-grave",
        "title": {
            "by": "Могілкі Нераберг у Вісбадэне — Магіла Барыса Кіта пад БЧБ-сцягам (Германія)",
            "ru": "Кладбище Нероберг в Висбадене — Могила Бориса Кита под БЧБ-флагом (Германия)",
            "en": "Neroberg Cemetery in Wiesbaden — Grave of Boris Kit (Germany)"
        },
        "category": "grave",
        "country": {"by": "Германія", "ru": "Германия", "en": "Germany"},
        "city": {"by": "Вісбадэн", "ru": "Висбаден", "en": "Wiesbaden"},
        "coordinates": [50.0983, 8.2325],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Barys_Kit_%28Boris_Kit%29.jpg/440px-Barys_Kit_%28Boris_Kit%29.jpg",
        "description": {
            "by": "На гістарычных могілках на гары Нераберг у нямецкім Вісбадэне спачывае выдатны беларускі і амерыканскі вучоны-астранаўт Барыс Кіт (1910–2018). На ягоным надмагіллі высечаны словы «Я жыў і працаваў для Беларусі» і выяўлены бел-чырвона-белы сцяг.",
            "ru": "На кладбище на горе Нероберг в Висбадене похоронен выдающийся белорусско-американский учёный в области астронавтики Борис Кит (1910–2018). На памятнике высечен бело-красно-белый флаг.",
            "en": "Located at the historic Russian Cemetery on Neroberg hill in Wiesbaden (Germany). Resting place of astronautics pioneer Boris Kit (1910–2018). The monument bears the Belarusian white-red-white flag and the inscription 'I lived and worked for Belarus'."
        },
        "personIds": ["boris-kit"],
        "links": [
            {"title": "Барыс Кіт (Вікіпедыя)", "url": "https://be.wikipedia.org/wiki/%D0%91%D0%B0%D1%80%D1%8B%D1%81_%D0%9A%D1%96%D1%82"}
        ]
    },
    {
        "id": "vilnius-suderve-vilna-gaon-mausoleum",
        "title": {
            "by": "Маўзалей (Огель) Віленскага Гаона на могілках Судэрве (Вільня, Літва)",
            "ru": "Мавзолей (Огель) Виленского Гаона на кладбище Судерве (Вильнюс, Литва)",
            "en": "Ohel / Mausoleum of the Vilna Gaon at Sudervė Cemetery (Vilnius, Lithuania)"
        },
        "category": "grave",
        "country": {"by": "Літва", "ru": "Литва", "en": "Lithuania"},
        "city": {"by": "Вільня", "ru": "Вильнюс", "en": "Vilnius"},
        "coordinates": [54.7214, 25.2131],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Vilna_Gaon_grave_Vilnius.jpg/640px-Vilna_Gaon_grave_Vilnius.jpg",
        "description": {
            "by": "Маўзалей (огель) найвялікшага духоўнага аўтарытэта літвакоў — Віленскага Гаона (Эліяху бен Шлома Залмана, 1720–1797), ураджэнца вёскі Сялец на Берасцейшчыне. Месца міжнароднага духоўнага паломніцтва вернікаў і навукоўцаў з усяго свету. Таксама ў Вільні на вул. Жыду ўсталяваны помнік і мемарыяльная дошка Гаону.",
            "ru": "Огель (мавзолей) духовного лидера литваков Виленского Гаона, родившегося в местечке Селец на Брестчине. Место паломничества верующих со всего мира.",
            "en": "The mausoleum (Ohel) of the renowned sage Vilna Gaon (Elijah ben Solomon Zalman, 1720–1797), born in Sielec near Brest (Belarus). Located at the Jewish Cemetery in Sudervė (Vilnius), attracting visitors worldwide."
        },
        "personIds": ["vilna-gaon"],
        "mustSee": True,
        "links": [
            {"title": "Віленскі гаон (Вікіпедыя)", "url": "https://be.wikipedia.org/wiki/%D0%92%D1%96%D0%BB%D0%B5%D0%BD%D1%81%D0%BA%D1%96_%D0%B3%D0%B0%D0%BE%D0%BD"}
        ]
    },
    {
        "id": "jerusalem-beit-ben-yehuda",
        "title": {
            "by": "Дом-музей Эліэзера Бэн-Егуды і магіла на Алейнай гары (Іерусалім)",
            "ru": "Дом-музей Элиэзера Бен-Йехуды и могила на Масличной горе (Иерусалим)",
            "en": "Beit Ben-Yehuda Memorial Museum & Mount of Olives Tomb (Jerusalem)"
        },
        "category": "culture",
        "country": {"by": "Ізраіль", "ru": "Израиль", "en": "Israel"},
        "city": {"by": "Іерусалім", "ru": "Иерусалим", "en": "Jerusalem"},
        "coordinates": [31.7511, 35.2158],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Eliezer_Ben-Yehuda.jpg/440px-Eliezer_Ben-Yehuda.jpg",
        "description": {
            "by": "Дом-музей «Бейт Бэн-Егуда» ў Іерусаліме (раён Тальпіёт) прысвечаны жыццю і подзвігу ўраджэнца вёскі Лужкі на Віцебшчыне Эліэзера Бэн-Егуды (1858–1922). Тут прадстаўлены ягоны працоўны кабінет, рукапісы 16-томнага слоўніка і дакументы адраджэння іўрыту. Сам Бэн-Егуда пахаваны на Алейнай (Маслічнай) гары ў Іерусаліме.",
            "ru": "Дом-музей «Бейт Бен-Йехуда» в Иерусалиме посвящён подвигу уроженца Витебщины Элиэзера Бен-Йехуды, возродившего современный иврит. Похоронен на Масличной горе.",
            "en": "Memorial museum 'Beit Ben-Yehuda' in Jerusalem celebrating the life of Vitebsk-born lexicographer Eliezer Ben-Yehuda, who revived spoken Hebrew. He is buried in the historic cemetery on the Mount of Olives."
        },
        "personIds": ["eliezer-ben-yehuda"],
        "mustSee": True,
        "links": [
            {"title": "Эліэзер Бэн-Егуда (Вікіпедыя)", "url": "https://be.wikipedia.org/wiki/%D0%AD%D0%BB%D1%96%D1%8D%D0%B7%D0%B5%D1%80_%D0%91%D1%8D%D0%BD-%D0%95%D0%B3%D1%83%D0%B4%D0%B0"}
        ]
    },
    {
        "id": "harvard-littauer-center-kuznets",
        "title": {
            "by": "Гарвардскі ўніверсітэт — Дэпартамент эканомікі і кабінет Саймана Кузнеца (Кембрыдж, ЗША)",
            "ru": "Гарвардский университет — Департамент экономики и кабинет Саймона Кузнеца (Кембридж, США)",
            "en": "Harvard University — Department of Economics & Simon Kuznets Center (Cambridge, USA)"
        },
        "category": "culture",
        "country": {"by": "ЗША", "ru": "США", "en": "USA"},
        "city": {"by": "Кембрыдж", "ru": "Кембридж", "en": "Cambridge"},
        "coordinates": [42.3761, -71.1189],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Simon_Kuznets.jpg/440px-Simon_Kuznets.jpg",
        "description": {
            "by": "У будынку Littauer Center у Гарвардскім універсітэце (Кембрыдж, Масачусетс) выкладаў і праводзіў фундаментальныя даследаванні Нобелеўскі лаўрэат па эканоміцы Сайман Кузнец (1901–1985), ураджэнец Пінска. Тут ён распрацоўваў тэорыю эканамічнага росту і метрыкі нацыянальнага даходу, якія вызначылі сучасную сусветную макраэканоміку.",
            "ru": "В здании Littauer Center Гарвардского университета преподавал нобелевский лауреат по экономике Саймон Кузнец, родившийся в Пинске. Здесь он создал основы современных национальных счетов и концепцию ВВП.",
            "en": "At the Littauer Center of Harvard University (Cambridge, Massachusetts), Pinsk-born Nobel laureate Simon Kuznets taught and conducted the foundational research on national income, economic growth, and Gross Domestic Product (GDP)."
        },
        "personIds": ["simon-kuznets"],
        "links": [
            {"title": "Сайман Кузнец (Вікіпедыя)", "url": "https://be.wikipedia.org/wiki/%D0%A1%D0%B0%D0%B9%D0%BC%D0%B0%D0%BD_%D0%9A%D1%83%D0%B7%D0%BD%D0%B5%D1%86"}
        ]
    },
    {
        "id": "odesa-second-cemetery-mendele",
        "title": {
            "by": "Другія хрысціянскія могілкі ў Адэсе — Магіла Мендэле Мойхер-Сфорыма",
            "ru": "Второе христианское кладбище в Одессе — Могила Менделе Мойхер-Сфорима",
            "en": "Second Christian Cemetery in Odesa — Grave of Mendele Mocher Sforim"
        },
        "category": "grave",
        "country": {"by": "Украіна", "ru": "Украина", "en": "Ukraine"},
        "city": {"by": "Адэса", "ru": "Одесса", "en": "Odesa"},
        "coordinates": [46.4444, 30.7289],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Mendele_Mocher_Sforim_1910.jpg/440px-Mendele_Mocher_Sforim_1910.jpg",
        "description": {
            "by": "У Адэсе пахаваны «дзядуля яўрэйскай літаратуры» Мендэле Мойхер-Сфорым (Шолем-Якаў Абрамовіч, 1836–1917), які нарадзіўся ў мястэчку Капыль на Міншчыне. Заснавальнік сучаснай класічнай прозы на ідышы і іўрыце, які ўславіў у сваіх творах духоўны свет і побыт беларускага мястэчка.",
            "ru": "В Одессе похоронен уроженец Копыля Менделе Мойхер-Сфорим (1836–1917) — классик и основоположник литературы на идише и иврите.",
            "en": "Grave of Kapyl-born author Mendele Mocher Sforim (1836–1917) in Odesa (Ukraine). Venerated as the founding father of modern Yiddish and Hebrew literature."
        },
        "personIds": ["mendele-mocher-sforim"],
        "links": [
            {"title": "Мендэле Мойхер-Сфорым (Вікіпедыя)", "url": "https://be.wikipedia.org/wiki/%D0%9C%D0%B5%D0%BD%D0%B4%D1%8D%D0%BB%D0%B5_%D0%9C%D0%BE%D0%B9%D1%85%D0%B5%D1%80-%D0%A1%D1%84%D0%BE%D1%80%D1%8B%D0%BC"}
        ]
    }
]

# Check existing places
existing_place_ids = {p['id'] for p in places}
added_places = 0
for np in new_places:
    if np['id'] not in existing_place_ids:
        places.append(np)
        existing_place_ids.add(np['id'])
        added_places += 1

print(f"Added {added_places} new places. Total places now: {len(places)}")

# Save JSON files
with open('data/persons.json', 'w', encoding='utf-8') as f:
    json.dump(persons, f, ensure_ascii=False, indent=2)

with open('data/places.json', 'w', encoding='utf-8') as f:
    json.dump(places, f, ensure_ascii=False, indent=2)

# Save JS files
with open('data/persons.js', 'w', encoding='utf-8') as f:
    f.write('window.personsData = ' + json.dumps(persons, ensure_ascii=False, indent=2) + ';\n')

with open('data/places.js', 'w', encoding='utf-8') as f:
    f.write('window.placesData = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

print("Successfully written places and persons JSON and JS files!")
