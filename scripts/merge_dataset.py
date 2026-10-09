import json
import re
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

# Import helper functions from normalize_helper
from normalize_helper import process_item, COUNTRY_MAP, CITY_MAP, PERSON_ID_NORMALIZE

# Person metadata definitions for all new historical figures
NEW_PERSONS = [
    {
        "id": "nikolai-sudzilovsky",
        "name": {
            "by": "Мікалай Судзілоўскі (Нікалас Расэль)",
            "ru": "Николай Судзиловский (Николас Рассель)",
            "en": "Nikolai Sudzilovsky (Nicholas Russel)"
        },
        "dates": "1850–1930",
        "role": {
            "by": "Навуковец, этнограф, доктар медыцыны, рэвалюцыянер, першы прэзідэнт Сената Гаваяў",
            "ru": "Ученый, этнограф, доктор медицины, революционер, первый президент Сената Гавайев",
            "en": "Scientist, ethnographer, medical doctor, revolutionary, first President of the Senate of Hawaii"
        },
        "bio": {
            "by": "Ураджэнец Магілёва. Вучыўся ў Пецярбургу і Кіеве, у Бухарэсце абараніў ступень доктара медыцыны. Жыў і працаваў у Францыі, Балгарыі, ЗША, Японіі і Кітаі. У 1895 годзе перасяліўся на Гаваі (пад імем Нікалас Расэль), змагаўся за правы карэнных канакаў, а ў 1901 годзе быў абраны першым прэзідэнтам Сената тэрыторыі Гаваі.",
            "ru": "Уроженец Могилёва. Окончил Бухарестский университет со степенью доктора медицины. В 1895 году поселился на Гавайях (под именем Николас Рассель), где защищал права коренного населения и в 1901 году был избран первым президентом Сената территории Гавайи.",
            "en": "Born in Mogilev. Studied medicine in Bucharest and worked across Europe and America before settling in Hawaii in 1895 as Nicholas Russel. A champion of native rights, he was elected the first President of the Senate of the Territory of Hawaii in 1901."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Nikolay_Sudzilovsky.jpg/480px-Nikolay_Sudzilovsky.jpg",
        "wiki": "https://be.wikipedia.org/wiki/Мікалай_Канстанцінавіч_Судзілоўскі",
        "placeIds": []
    },
    {
        "id": "henryk-sienkiewicz",
        "name": {
            "by": "Генрык Сянкевіч",
            "ru": "Генрик Сенкевич",
            "en": "Henryk Sienkiewicz"
        },
        "dates": "1846–1916",
        "role": {
            "by": "Польскі пісьменнік, публіцыст, лаўрэат Нобелеўскай прэміі па літаратуры (1905)",
            "ru": "Польский писатель, публицист, лауреат Нобелевской премии по литературе (1905)",
            "en": "Polish novelist, journalist, Nobel Prize laureate in Literature (1905)"
        },
        "bio": {
            "by": "Паходзіў са шляхецкага роду герба «Осык», які меў татарскія карані з Вялікага Княства Літоўскага. Аўтар знакамітай гістарычнай трылогіі («Агнём і мячом», «Патоп», «Пан Валадыёўскі»), рамана «Кама градашы» (Quo Vadis) і «Крыжакі». Памёр у Веве (Швейцарыя) у 1916 годзе.",
            "ru": "Происходил из шляхетского рода с корнями в Великом Княжестве Литовском. Автор всемирно известной трилогии, романов «Камо грядеши» (Quo Vadis) и «Крестоносцы». Лауреат Нобелевской премии 1905 года.",
            "en": "Descended from noble GDL Lipka Tatar heritage. Author of the classic Trilogy, 'Quo Vadis' and 'The Teutonic Knights'. Awarded the Nobel Prize in Literature in 1905 for his outstanding merits as an epic writer."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Henryk_Sienkiewicz_Kazimierz_Mordasewicz.jpg/480px-Henryk_Sienkiewicz_Kazimierz_Mordasewicz.jpg",
        "wiki": "https://be.wikipedia.org/wiki/Генрык_Сянкевіч",
        "placeIds": []
    },
    {
        "id": "eliza-orzeszkowa",
        "name": {
            "by": "Эліза Ажэшка",
            "ru": "Элиза Ожешко",
            "en": "Eliza Orzeszkowa"
        },
        "dates": "1841–1910",
        "role": {
            "by": "Пісьменніца, эсэістка, грамадская дзяячка, намінантка на Нобелеўскую прэмію",
            "ru": "Писательница, эссеистка, общественный деятель, номинантка на Нобелевскую премию",
            "en": "Writer, essayist, social activist, Nobel Prize nominee"
        },
        "bio": {
            "by": "Нарадзілася ў маёнтку Мількаўшчына пад Гроднам. Удзельніца падтрымкі паўстання 1863 года. Аўтар раманаў «Над Нёманам», «Хам», «Нізіны», аповесцей пра лёсы беларускіх сялян і шляхты Панямоння. Жыла і тварыла ў Гродне, дзе яе дом стаў цэнтрам грамадскага жыцця.",
            "ru": "Родилась в имении Мильковщина близ Гродно. Участница поддержки восстания 1863 года. Автор романов «Над Неманом», «Хам», повестей о белорусской жизни. Её дом в Гродно был средоточием культурной мысли.",
            "en": "Born near Hrodna. Supported the January Uprising of 1863. Author of 'Nad Niemnem' and moving realist chronicles depicting local life along the Neman River. Nominated for the Nobel Prize in Literature."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Eliza_Orzeszkowa.jpg/480px-Eliza_Orzeszkowa.jpg",
        "wiki": "https://be.wikipedia.org/wiki/Эліза_Ажэшка",
        "placeIds": []
    },
    {
        "id": "yafim-karski",
        "name": {
            "by": "Яўхім Карскі",
            "ru": "Евфимий Карский",
            "en": "Yafim Karski"
        },
        "dates": "1860–1931",
        "role": {
            "by": "Мовазнавец, славіст, палеограф, фалькларыст, рэктар Варшаўскага ўніверсітэта, акадэмік",
            "ru": "Языковед, славист, палеограф, фольклорист, ректор Варшавского университета, академик",
            "en": "Linguist, Slavist, paleographer, ethnographer, rector of Warsaw University, academician"
        },
        "bio": {
            "by": "Ураджэнец вёскі Лаша пад Гроднам. Заснавальнік навуковага беларусазнаўства. Аўтар фундаментальнага трохтамовага даследавання «Беларусы» (1903–1922) — энцыклапедыі беларускай мовы, культуры і фальклору, якая навукова абгрунтавала самабытнасць беларускай нацыі. Працаваў у Варшаве і Санкт-Пецярбургу.",
            "ru": "Родился в деревне Лаша Гродненского уезда. Основоположник научного белорусоведения. Создатель фундаментального трёхтомного труда «Белорусы» (1903–1922). Академик Петербургской академии наук.",
            "en": "Born near Hrodna. The foundational scholar of Belarusian philology and linguistics. Author of the monumental three-volume encyclopedia 'The Belarusians' (1903–1922), which defined the linguistic borders of the nation."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Yefim_Karsky.jpg/480px-Yefim_Karsky.jpg",
        "wiki": "https://be.wikipedia.org/wiki/Яўхім_Фёдаравіч_Карскі",
        "placeIds": []
    },
    {
        "id": "sophia-of-minsk",
        "name": {
            "by": "Сафія Менская (Валадараўна)",
            "ru": "София Минская (Володаревна)",
            "en": "Sophia of Minsk"
        },
        "dates": "каля 1140–1198",
        "role": {
            "by": "Князёўна Менская, каралева Даніі (1157–1182), жонка караля Вальдэмара I Вялікага",
            "ru": "Княжна Минская, королева Дании (1157–1182), супруга короля Вальдемара I Великого",
            "en": "Princess of Minsk, Queen consort of Denmark (1157–1182), wife of Valdemar I the Great"
        },
        "bio": {
            "by": "Дачка менскага і полацкага князя Валадара Глебавіча і польскай князёўны Рыкісы Баляславаўны. Выйшла замуж за караля Даніі Вальдэмара I Вялікага. Маці дацкіх каралёў Кнуда VI і Вальдэмара II Пераможцы, а таксама французскай каралевы Інгеборгі. Пахаваная ў каралеўскім пантэоне ў царкве Святога Бендта ў Рынгстэдзе.",
            "ru": "Дочь минского князя Володаря Глебовича. Супруга короля Дании Вальдемара I Великого. Мать датских королей Кнуда VI и Вальдемара II Победителя, а также королевы Франции Ингеборги. Похоронена в церкви Св. Бендта в Рингстеде.",
            "en": "Daughter of Prince Volodar of Minsk. Queen consort of Denmark through her marriage to Valdemar I the Great. Mother of Kings Canute VI and Valdemar II, and Queen Ingeborg of France. Buried in St. Bendt's Church in Ringsted."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Sophia_of_Minsk.jpg/480px-Sophia_of_Minsk.jpg",
        "wiki": "https://be.wikipedia.org/wiki/Сафія_Валадараўна",
        "placeIds": []
    },
    {
        "id": "barbara-radziwill",
        "name": {
            "by": "Барбара Радзівіл",
            "ru": "Барбара Радзивилл",
            "en": "Barbara Radziwiłł"
        },
        "dates": "1520–1551",
        "role": {
            "by": "Вялікая княгіня літоўская і каралева польская, знакамітая постаць эпохі Адраджэння",
            "ru": "Великая княгиня литовская и королева польская, знаменитая фигура Ренессанса",
            "en": "Grand Duchess of Lithuania and Queen of Poland, iconic Renaissance figure"
        },
        "bio": {
            "by": "Дачка кашталяна віленскага Юрыя Радзівіла «Геркулеса». Славутая сваёй незвычайнай прыгажосцю і адукаванасцю. Таемна пабралася шлюбам з вялікім князем Жыгімонтам II Аўгустам у 1547 годзе. Нягледзячы на шалёны супраціў сойма, была ўрачыста каранавана ў Кракаве. Пахаваная ў крыпце Віленскага кафедральнага сабора.",
            "ru": "Дочь Юрия Радзивилла. Знаменита своей красотой и романтической историей тайного брака с великим князем Сигизмундом II Августом. Коронована в Кракове. Похоронена в крипте Виленского кафедрального собора.",
            "en": "Daughter of Jerzy Radziwiłł 'Hercules'. Celebrated for her extraordinary beauty and romantic marriage to Sigismund II Augustus. Crowned Queen in Kraków. Buried in the Royal Crypt of Vilnius Cathedral."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Lucas_Cranach_d.J._-_K%C3%B6nigin_Barbara_Radziwill_%28KHM_Wien%29.jpg/480px-Lucas_Cranach_d.J._-_K%C3%B6nigin_Barbara_Radziwill_%28KHM_Wien%29.jpg",
        "wiki": "https://be.wikipedia.org/wiki/Барбара_Радзівіл",
        "placeIds": []
    },
    {
        "id": "anna-radziwill",
        "name": {
            "by": "Ганна Радзівіл",
            "ru": "Анна Радзивилл",
            "en": "Anna Radziwiłł"
        },
        "dates": "1476–1522",
        "role": {
            "by": "Княгіня мазавецкая, рэгентка Варшавы і Мазовіі, дзяржаўная дзяячка і рэфарматарка",
            "ru": "Княгиня мазовецкая, регентша Варшавы и Мазовии, государственная деятельница",
            "en": "Duchess of Masovia, Regent of Warsaw and Masovia, stateswoman and reformer"
        },
        "bio": {
            "by": "Дачка вялікалітоўскага канцлера Мікалая Радзівіла «Старога». Жонка князя Конрада III Рудога. Пасля яго смерці больш за 15 гадоў мудра кіравала Мазавецкім княствам і Варшавай як рэгентка пры сынах. Заснавала касцёл і шпіталь Святой Ганны ў Варшаве, адстаяла аўтаномію Мазовіі. Пахаваная ў касцёле Святой Ганны.",
            "ru": "Дочь великолитовского канцлера Николая Радзивилла Старого. Более 15 лет мудро правила Мазовией и Варшавой в качестве регентши. Основательница костёла Св. Анны в Варшаве.",
            "en": "Daughter of GDL Chancellor Mikołaj Radziwiłł 'the Old'. Ruled the Duchy of Masovia and Warsaw as regent for over 15 years, defending Masovian autonomy. Founded the Church of St. Anne in Warsaw."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Anna_Radziwi%C5%82%C5%82%C3%B3wna.jpg/480px-Anna_Radziwi%C5%82%C5%82%C3%B3wna.jpg",
        "wiki": "https://be.wikipedia.org/wiki/Ганна_Радзівіл",
        "placeIds": []
    },
    {
        "id": "antoni-radziwill",
        "name": {
            "by": "Антон Генрых Радзівіл",
            "ru": "Антон Генрих Радзивилл",
            "en": "Antoni Henryk Radziwiłł"
        },
        "dates": "1775–1833",
        "role": {
            "by": "Князь, дзяржаўны дзеяч, кампазітар, мецэнат Шапэна і Бетховена, намеснік Пазнані",
            "ru": "Князь, государственный деятель, композитор, меценат Шопена и Бетховена",
            "en": "Prince, statesman, composer, patron of Chopin and Beethoven"
        },
        "bio": {
            "by": "Паходзіў з нясвіжска-нябораўскай лініі Радзівілаў. Быў уладальнікам палаца Радзівілаў у Берліне (Wilhelmstraße 77), дзе трымаў знакаміты музычны салон. Аўтар першай оперы на тэму трагедыі Гётэ «Фаўст». Мецэнат Людвіга ван Бетховена і Фрыдэрыка Шапэна.",
            "ru": "Представитель несвижской линии Радзивиллов. Владелец дворца Радзивиллов в Берлине, где собирался цвет европейской культуры. Автор первой оперы на сюжет «Фауста» Гёте. Покровитель Шопена и Бетховена.",
            "en": "Prince of the Nieśwież-Nieborów line. Resided at Palais Radziwiłł in Berlin, hosting a premier cultural salon. Composed the first musical score for Goethe's 'Faust'. Patron to Frédéric Chopin and Beethoven."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Antoni_Henryk_Radziwi%C5%82%C5%82.jpg/480px-Antoni_Henryk_Radziwi%C5%82%C5%82.jpg",
        "wiki": "https://be.wikipedia.org/wiki/Антон_Генрых_Радзівіл",
        "placeIds": []
    },
    {
        "id": "radziwills",
        "name": {
            "by": "Магнацкі род Радзівілаў",
            "ru": "Магнатский род Радзивиллов",
            "en": "The Radziwiłł Family"
        },
        "dates": "XV–XX ст.",
        "role": {
            "by": "Найбуйнейшы магнацкі род ВКЛ і Рэчы Паспалітай, «некаранаваныя каралі»",
            "ru": "Крупнейший магнатский род ВКЛ и Речи Посполитой, «некоронованные короли»",
            "en": "Foremost magnate family of the GDL and Poland-Lithuania, 'uncrowned kings'"
        },
        "bio": {
            "by": "Адзін з наймагутнейшых родаў у гісторыі Еўропы герба «Трубы». Трымалі вышэйшыя дзяржаўныя пасады канцлераў, гетманаў і ваяводаў. Заснавальнікі Нясвіжскага, Мірскага, Алыцкага, Біржанскага і Шыдлавецкага замкаў, уладальнікі рэзідэнцый у Вільні, Варшаве, Берліне і Парыжы.",
            "ru": "Могущественный род герба «Трубы», давший Великому Княжеству Литовскому десятки гетманов, канцлеров и епископов. Владельцы сотен городов и замков в Несвиже, Мире, Олыке, Варшаве и Берлине.",
            "en": "One of the wealthiest and most influential aristocratic dynasties in European history. Held supreme state and military posts in the Grand Duchy of Lithuania, building iconic palaces and castles across Belarus, Lithuania, Poland, and Ukraine."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Herb_Radziwill.svg/480px-Herb_Radziwill.svg.png",
        "wiki": "https://be.wikipedia.org/wiki/Радзівілы",
        "placeIds": []
    },
    {
        "id": "tyszkiewicz",
        "name": {
            "by": "Графы Тышкевічы",
            "ru": "Графы Тышкевичи",
            "en": "The Tyszkiewicz Family"
        },
        "dates": "XVI–XX ст.",
        "role": {
            "by": "Магнацкі род ВКЛ герба «Ляліва», выбітныя мецэнаты, навукоўцы і калекцыянеры",
            "ru": "Магнатский род ВКЛ герба «Лелива», выдающиеся меценаты и исследователи",
            "en": "Magnate dynasty of the GDL, distinguished patrons of art, archaeologists, collectors"
        },
        "bio": {
            "by": "Выбітны род з Лагойска і Свіслачы. Браты Канстанцін і Яўстах Тышкевічы заснавалі беларускую навуковую археалогію і Віленскі музей старажытнасцей. Уладальнікі раскошных палацаў у Паланзе, Крэтынзе, Варшаве і Лагойску, руплівыя збіральнікі гістарычнай спадчыны.",
            "ru": "Известный род из Логойска. Братья Константин и Евстафий Тышкевичи стали основателями белорусской археологии и Виленского музея древностей. Владельцы дворцов в Паланге, Кретинге, Варшаве и Логойске.",
            "en": "Noble dynasty originating from Lahoysk. Brothers Eustachy and Konstanty Tyszkiewicz founded modern Belarusian archaeology and the Vilnius Museum of Antiquities. Built majestic palaces in Palanga, Kretinga, Warsaw, and Lahoysk."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Herb_Leliwa.svg/480px-Herb_Leliwa.svg.png",
        "wiki": "https://be.wikipedia.org/wiki/Тышкевічы",
        "placeIds": []
    },
    {
        "id": "jan-karol-chodkiewicz",
        "name": {
            "by": "Ян Караль Хадкевіч",
            "ru": "Ян Кароль Ходкевич",
            "en": "Jan Karol Chodkiewicz"
        },
        "dates": "1560–1621",
        "role": {
            "by": "Вялікі гетман літоўскі, палкаводзец, пераможца бітваў пад Кірхгольмам і Хоцінам",
            "ru": "Великий гетман литовский, полководец, победитель битв при Кирхгольме и Хотине",
            "en": "Grand Hetman of Lithuania, brilliant military commander, victor of Kircholm and Khotyn"
        },
        "bio": {
            "by": "Нарадзіўся ў Вільні. Адзін з найвыдатнейшых военачальнікаў Еўропы XVII стагоддзя. У 1605 г. у бітве пад Кірхгольмам з утрая меншым войскам разграміў шведскую армію караля Карла IX. У 1621 г. узначаліў абарону Хоціна ад 150-тысячнага асманскага войска і памёр у крэпасці як герой напярэдадні перамогі.",
            "ru": "Один из величайших полководцев XVII века. В 1605 г. при Кирхгольме разгромил шведскую армию, будучи в меньшинстве. В 1621 г. возглавлял оборону Хотина от османской армии и пал смертью героя в крепости.",
            "en": "One of the greatest military strategists of 17th-century Europe. Famous for his stunning cavalry triumph over Swedish forces at Kircholm (1605) and for heroically commanding the fortress of Khotyn against massive Ottoman siege forces in 1621."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Jan_Karol_Chodkiewicz.PNG/480px-Jan_Karol_Chodkiewicz.PNG",
        "wiki": "https://be.wikipedia.org/wiki/Ян_Караль_Хадкевіч",
        "placeIds": []
    },
    {
        "id": "lew-sapieha",
        "name": {
            "by": "Леў Сапега і род Сапегаў",
            "ru": "Лев Сапега и род Сапег",
            "en": "Lew Sapieha & Sapieha Family"
        },
        "dates": "1557–1633",
        "role": {
            "by": "Вялікі канцлер і гетман літоўскі, галоўны стваральнік Трэцяга Статута ВКЛ (1588)",
            "ru": "Великий канцлер и гетман литовский, создатель Третьего Статута ВКЛ (1588)",
            "en": "Grand Chancellor and Hetman of Lithuania, chief architect of the Third Statute of the GDL (1588)"
        },
        "bio": {
            "by": "Ураджэнец Астроўна (цяпер Бешанковіцкі раён). Выбітны дзяржаўны дзеяч, дыпламат і юрыст. Аўтар і выдавец Трэцяга Статута ВКЛ 1588 года — перадавога збору законаў на старабеларускай мове. Заснавальнік касцёла Святога Міхала ў Вільні (родавы пантэон Сапегаў), рэзідэнцый у Ружанах, Кодэні і Красічыне.",
            "ru": "Родился в Островно. Выдающийся государственный деятель, мыслитель и правовед. Создатель и издатель Третьего Статута ВКЛ 1588 года на старобелорусском языке. Основатель родового пантеона в костёле Св. Михаила в Вильне и резиденций в Ружанах и Кодене.",
            "en": "Born in Astroŭna. Renowned jurist, diplomat, and statesman who formulated and financed the Third Statute of the GDL (1588) in Old Belarusian. Established grand residences in Ruzhany, Kodeń, Krasiczyn, and the Sapieha pantheon at St. Michael's Church in Vilnius."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Lew_Sapieha.PNG/480px-Lew_Sapieha.PNG",
        "wiki": "https://be.wikipedia.org/wiki/Леў_Іванавіч_Сапега",
        "placeIds": []
    },
    {
        "id": "gediminas",
        "name": {
            "by": "Вялікі князь Гедзімін",
            "ru": "Великий князь Гедимин",
            "en": "Grand Duke Gediminas"
        },
        "dates": "каля 1275–1341",
        "role": {
            "by": "Вялікі князь літоўскі (1316–1341), заснавальнік дынастыі Гедзімінавічаў і Вільні",
            "ru": "Великий князь литовский (1316–1341), основатель династии Гедиминовичей и Вильнюса",
            "en": "Grand Duke of Lithuania (1316–1341), founder of the Gediminid dynasty and Vilnius"
        },
        "bio": {
            "by": "Выбітны манарх і дыпламат, які аб'яднаў вакол Навагрудка і Полацка беларускія і балцкія землі ў адзіную магутную дзяржаву. Перанёс сталіцу ў Вільню, запрашаў еўрапейскіх майстроў і гандляроў, пашырыў межы дзяржавы да Дняпра і Палесся.",
            "ru": "Выдающийся государь и дипломат, объединивший белорусские и балтские земли. Перенёс столицу государства в Вильну, привлекал ремесленников со всей Европы и заложил основы могущества ВКЛ.",
            "en": "Architect of the Grand Duchy's rise as a European superpower. Consolidated Belarusian and Baltic lands, transferred the capital to Vilnius, invited Western European merchants and craftsmen, and established a dynastic line ruling for centuries."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Gediminas_statue_Vilnius.jpg/480px-Gediminas_statue_Vilnius.jpg",
        "wiki": "https://be.wikipedia.org/wiki/Гедзімін",
        "placeIds": []
    },
    {
        "id": "vytautas",
        "name": {
            "by": "Вялікі князь Вітаўт Вялікі",
            "ru": "Великий князь Витовт Великий",
            "en": "Grand Duke Vytautas the Great"
        },
        "dates": "1350–1430",
        "role": {
            "by": "Вялікі князь літоўскі (1392–1430), пераможца бітвы пад Грунвальдам",
            "ru": "Великий князь литовский (1392–1430), победитель битвы при Грюнвальде",
            "en": "Grand Duke of Lithuania (1392–1430), victor of the Battle of Grunwald"
        },
        "bio": {
            "by": "Сын Кейстута. Пры яго кіраванні Вялікае Княства Літоўскае дасягнула вяршыні магутнасці і найбольшай тэрыторыі — ад Балтыйскага да Чорнага мора. Разам з каралём Ягайлам у 1410 г. камандаваў саюзным войскам, якое разграміла Тэўтонскі ордэн пад Грунвальдам. Абаронца беларускіх гарадоў і пашыральнік Магдэбургскага права.",
            "ru": "Сын Кейстута. При его правлении Великое Княжество Литовское достигло апогея территориального и политического могущества — от Балтики до Чёрного моря. Вместе с Ягайло разгромил Тевтонский орден в Грюнвальдской битве 1410 года.",
            "en": "Son of Kęstutis. Under his reign, the Grand Duchy expanded to its greatest territorial extent, spanning from the Baltic to the Black Sea. Co-commanded the victorious allied army at the pivotal Battle of Grunwald in 1410."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Vytautas_the_Great_monument_in_Kaunas.jpg/480px-Vytautas_the_Great_monument_in_Kaunas.jpg",
        "wiki": "https://be.wikipedia.org/wiki/Вітаўт",
        "placeIds": []
    },
    {
        "id": "henryk-siemiradzki",
        "name": {
            "by": "Генрых Семірадскі",
            "ru": "Генрих Семирадский",
            "en": "Henryk Siemiradzki"
        },
        "dates": "1843–1902",
        "role": {
            "by": "Мастак-акадэміст, майстар манументальнага гістарычнага жывапісу, сузаснавальнік Нацыянальнага музея ў Кракаве",
            "ru": "Художник-академист, мастер монументальной исторической живописи, сооснователь Национального музея в Кракове",
            "en": "Academic painter, master of monumental classical scenes, co-founder of the National Museum in Krakow"
        },
        "bio": {
            "by": "Нарадзіўся ў сям'і афіцэра шляхецкага роду з Навагрудка герба «Лебедзь». Вучыўся ў Пецярбургу, дзесяцігоддзямі жыў і тварыў у Рыме. У 1879 годзе падарыў гораду Кракаву сваё грандыёзнае палатно «Светачы хрысціянства» («Pochodnie Nerona»), што стала пачаткам Нацыянальнага музея ў Сукенніцах. Яго палотны ўпрыгожваюць лепшыя галерэі Кракава, Львова і Варшавы.",
            "ru": "Родился в семье офицера шляхетского рода из Новогрудка. Жил и творил в Риме. В 1879 г. подарил Кракову грандиозное полотно «Светочи христианства» («Факелы Нерона»), что положило начало Национальному музею в Сукенницах.",
            "en": "Born to a noble family with roots in Navahrudak. Celebrated for his grandiose classical antiquity canvases painted in Rome. In 1879, gifted 'Nero's Torches' to Kraków, inaugurating the collection of the National Museum at the Sukiennice."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Henryk_Siemiradzki_1880s.jpg/480px-Henryk_Siemiradzki_1880s.jpg",
        "wiki": "https://be.wikipedia.org/wiki/Генрых_Іпалітавіч_Семірадскі",
        "placeIds": []
    },
    {
        "id": "jan-matejko",
        "name": {
            "by": "Ян Матэйка",
            "ru": "Ян Матейко",
            "en": "Jan Matejko"
        },
        "dates": "1838–1893",
        "role": {
            "by": "Выдатны мастак гістарычнага жанру, аўтар манументальных карцін па гісторыі ВКЛ",
            "ru": "Выдающийся художник исторического жанра, автор монументальных полотен по истории ВКЛ",
            "en": "Master painter of monumental historical scenes from GDL and Polish history"
        },
        "bio": {
            "by": "Найбуйнейшы прадстаўнік гістарычнага жывапісу Цэнтральнай Еўропы. Стварыў неўміручыя шэдэўры, прысвечаныя ключавым падзеям беларускай і супольнай гісторыі: «Бітва пад Грунвальдам» (з вялікім князем Вітаўтам у цэнтры), «Рэйтан — заняпад Польшчы» (пра беларускага шляхціца Тадэвуша Рэйтана), «Стэфан Баторый пад Псковам» і «Люблінская унія».",
            "ru": "Классик европейской исторической живописи. Создал монументальные полотна о ключевых вехах истории ВКЛ: «Грюнвальдская битва» (с князем Витовтом в центре), «Рейтан — упадок Польши», «Стефан Баторий под Псковом» и «Люблинская уния».",
            "en": "Celebrated master of historical painting. Created epic works illustrating critical events of GDL history, including the 'Battle of Grunwald' (featuring Grand Duke Vytautas), 'Rejtan', and the 'Union of Lublin'."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Jan_Matejko_Self-portrait.jpg/480px-Jan_Matejko_Self-portrait.jpg",
        "wiki": "https://be.wikipedia.org/wiki/Ян_Матэйка",
        "placeIds": []
    },
    {
        "id": "stanislaw-zukowski",
        "name": {
            "by": "Станіслаў Жукоўскі",
            "ru": "Станислав Жуковский",
            "en": "Stanisław Żukowski"
        },
        "dates": "1873–1944",
        "role": {
            "by": "Мастак-пейзажыст, пясняр шляхецкіх сядзіб і прыроды Палесся і Панямоння",
            "ru": "Художник-пейзажист, певец старинных усадеб и природы Понеманья",
            "en": "Landscape painter, master of country manor interiors and twilight landscapes"
        },
        "bio": {
            "by": "Нарадзіўся ў маёнтку Ендрыхаўцы каля Росі (цяпер Ваўкавыскі раён). Вучыўся ў Маскве ў Ісака Левітана. У сваіх карцінах апяваў непаўторную паэтыку старадаўніх шляхецкіх сядзіб, пакояў з адкрытымі вокнамі ў сад, восеньскіх паркаў і лясоў Беларусі. Загінуў падчас Варшаўскага паўстання ў 1944 г.",
            "ru": "Родился в имении Ендриховцы (Волковысский район). Ученик Левитана. Прославился тончайшими пейзажами и интерьерами дворянских усадеб с открытыми окнами в сад. Погиб во время Варшавского восстания 1944 года.",
            "en": "Born in Yendrykhaŭtsy near Vaŭkavysk. Disciple of Isaac Levitan. World-renowned for his atmospheric depictions of old aristocratic estates, sunlit open windows, and serene forests. Died during the Warsaw Uprising in 1944."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Stanislav_Zhukovsky_selfportrait.jpg/480px-Stanislav_Zhukovsky_selfportrait.jpg",
        "wiki": "https://be.wikipedia.org/wiki/Станіслаў_Юльянавіч_Жукоўскі",
        "placeIds": []
    },
    {
        "id": "louis-b-mayer",
        "name": {
            "by": "Луіс Б. Маер (Лазар Маер)",
            "ru": "Луис Б. Майер (Лазарь Мейер)",
            "en": "Louis B. Mayer"
        },
        "dates": "1884–1957",
        "role": {
            "by": "Кінапрадзюсар, сузаснавальнік і кіраўнік Metro-Goldwyn-Mayer (MGM), стваральнік прэміі «Оскар»",
            "ru": "Кинопродюсер, сооснователь и руководитель киностудии Metro-Goldwyn-Mayer, создатель премии «Оскар»",
            "en": "Film mogul, head of Metro-Goldwyn-Mayer (MGM), founder of the Academy Awards (Oscars)"
        },
        "bio": {
            "by": "Нарадзіўся ў Мінску ў яўрэйскай сям'і. Стварыў наймагутнейшую кінастудыю залатога веку Галівуда — Metro-Goldwyn-Mayer (MGM). У 1927 годзе выступіў галоўным ініцыятарам заснавання Амерыканскай акадэміі кінамастацтваў і прэміі «Оскар». Адкрыў такіх зорак, як Грэта Гарба, Джудзі Гарленд і Кларк Гейбл.",
            "ru": "Родился в Минске. Основатель легендарной студии Metro-Goldwyn-Mayer (MGM). Главный инициатор создания Американской киноакадемии и премии «Оскар» (1927). Открыл Грету Гарбо, Джуди Гарленд и Кларка Гейбла.",
            "en": "Born in Minsk. Legendary studio titan who built Metro-Goldwyn-Mayer (MGM) into Hollywood's dominant force. Spearheaded the creation of the Academy of Motion Picture Arts and Sciences and the Oscar statuette in 1927."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Louis_B_Mayer_1953.jpg/480px-Louis_B_Mayer_1953.jpg",
        "wiki": "https://be.wikipedia.org/wiki/Луіс_Барт_Маер",
        "placeIds": []
    },
    {
        "id": "irving-berlin",
        "name": {
            "by": "Ірвінг Берлін (Ізраіль Бейлін)",
            "ru": "Ирвинг Берлин (Израиль Бейлин)",
            "en": "Irving Berlin"
        },
        "dates": "1888–1989",
        "role": {
            "by": "Кампазітар, класік амерыканскай песні, аўтар «God Bless America» і «White Christmas»",
            "ru": "Композитор, классик американской песни, автор «God Bless America» и «White Christmas»",
            "en": "Legendary composer and lyricist, author of 'God Bless America' and 'White Christmas'"
        },
        "bio": {
            "by": "Нарадзіўся ў мястэчку Талачын (цяпер Віцебская вобласць). Напісаў больш за 1500 песень і музыку да дзясяткаў брадвейскіх мюзіклаў і фільмаў. Яго твор «God Bless America» стаў неафіцыйным гімнам ЗША, а «White Christmas» — самай папулярнай песняй усіх часоў. Пабудаваў тэатр Music Box на Брадвеі.",
            "ru": "Родился в Толочине (Витебская область). Автор более 1500 песен, включая неофициальный гимн США «God Bless America» и легендарный сингл «White Christmas». Построил бродвейский театр Music Box Theatre.",
            "en": "Born in Talachyn (Vitebsk region). One of America's greatest songwriters, author of over 1,500 tunes including 'God Bless America' and 'White Christmas' (the best-selling single of all time). Built Broadway's Music Box Theatre."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Irving_Berlin_in_1948.jpg/480px-Irving_Berlin_in_1948.jpg",
        "wiki": "https://be.wikipedia.org/wiki/Ірвінг_Берлін",
        "placeIds": []
    },
    {
        "id": "david-sarnoff",
        "name": {
            "by": "Давід Сарнаў",
            "ru": "Давид Сарнов",
            "en": "David Sarnoff"
        },
        "dates": "1891–1971",
        "role": {
            "by": "Піянер электронных камунікацый, прэзідэнт RCA, заснавальнік сеткі NBC",
            "ru": "Пионер радио- и телевещания, президент корпорации RCA, основатель сети NBC",
            "en": "Pioneer of radio and television broadcasting, head of RCA, founder of NBC"
        },
        "bio": {
            "by": "Нарадзіўся ў мястэчку Узляны Ігуменскага павета (цяпер Пухавіцкі раён Мінскай вобласці). У 1912 г. трое сутак бесперапынна прымаў радыёсігналы пра гібель «Тытаніка». Прадказаў і стварыў масавае камерцыйнае радыёвяшчанне, заснаваў сетку NBC і кіраваў медыягігантам RCA з 30 Rockefeller Plaza.",
            "ru": "Родился в местечке Узляны под Минском. Пионер коммерческого радиовещания и телевидения. В 1912 г. принимал сигналы бедствия «Титаника». Основал телерадиосеть NBC и возглавлял корпорацию RCA.",
            "en": "Born in Uzlyany near Minsk. Telecommunications visionary who predicted mass home radio and television. Founded the NBC network and led RCA from its headquarters at 30 Rockefeller Plaza."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/David_Sarnoff_1922.jpg/480px-David_Sarnoff_1922.jpg",
        "wiki": "https://be.wikipedia.org/wiki/Давід_Сарнаў",
        "placeIds": []
    },
    {
        "id": "mark-rothko",
        "name": {
            "by": "Марк Ротка (Маркус Роткавіч)",
            "ru": "Марк Ротко (Маркус Роткович)",
            "en": "Mark Rothko"
        },
        "dates": "1903–1970",
        "role": {
            "by": "Мастак-авангардыст, лідар абстрактнага экспрэсіянізму і жывапісу каляровага поля",
            "ru": "Художник-авангардист, лидер абстрактного экспрессионизма и живописи цветового поля",
            "en": "Abstract expressionist painter, pioneer of Color Field painting"
        },
        "bio": {
            "by": "Нарадзіўся ў Дзвінску (Віцебская губерня). Адзін з найвялікшых мастакоў другой паловы XX стагоддзя. Распрацаваў свой знакаміты стыль палотнаў з палямі насычанага колеру, якія выклікаюць глыбокі эмацыйны рэзананс. Стваральнік сусветна вядомай Rothko Chapel у Х'юстане.",
            "ru": "Родился в Двинске (Витебская губерния). Один из величайших живописцев XX века, пионер живописи цветового поля. Создатель знаменитой Капеллы Ротко в Хьюстоне.",
            "en": "Born in Dvinsk (Vitebsk Governorate). Renowned master of Color Field painting whose luminous rectangles of color evoke profound spiritual resonance. Creator of the Rothko Chapel in Houston, Texas."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Mark_Rothko_by_Consuelo_Kanaga_1940s.jpg/480px-Mark_Rothko_by_Consuelo_Kanaga_1940s.jpg",
        "wiki": "https://be.wikipedia.org/wiki/Марк_Ротка",
        "placeIds": []
    },
    {
        "id": "chaim-weizmann",
        "name": {
            "by": "Хаім Вайцман",
            "ru": "Хаим Вейцман",
            "en": "Chaim Weizmann"
        },
        "dates": "1874–1952",
        "role": {
            "by": "Вучоны-хімік, сіянісцкі лідар, першы прэзідэнт Дзяржавы Ізраіль (1949–1952)",
            "ru": "Учёный-химик, сионистский лидер, первый президент Государства Израиль (1949–1952)",
            "en": "Chemist, statesman, first President of the State of Israel (1949–1952)"
        },
        "bio": {
            "by": "Нарадзіўся ў вёсцы Моталь Кобрынскага павета (цяпер Іванаўскі раён Брэсцкай вобласці). Бліскучы вучоны-біяхімік, вынаходнік, прафесар Манчэстэрскага ўніверсітэта. Шматгадовы кіраўнік Сусветнай сіянісцкай арганізацыі. У 1934 г. заснаваў у Рэхавоце даследчы інстытут (цяпер Інстытут Вайцмана), а ў 1949 г. стаў першым прэзідэнтам Ізраіля.",
            "ru": "Родился в деревне Мотоль Брестской области. Выдающийся биохимик, профессор. Многолетний лидер Всемирной сионистской организации. Основатель Института Вейцмана в Реховоте и первый президент Израиля (1949–1952).",
            "en": "Born in Motal (Brest region). Distinguished biochemist who developed synthetic acetone fermentation at Manchester. Longtime president of the World Zionist Organization and founding President of the State of Israel (1949–1952)."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Chaim_Weizmann_1948.jpg/480px-Chaim_Weizmann_1948.jpg",
        "wiki": "https://be.wikipedia.org/wiki/Хаім_Вайцман",
        "placeIds": []
    },
    {
        "id": "shimon-peres",
        "name": {
            "by": "Шымон Перэс (Перскі)",
            "ru": "Шимон Перес (Перский)",
            "en": "Shimon Peres"
        },
        "dates": "1923–2016",
        "role": {
            "by": "Прэзідэнт і прэм'ер-міністр Ізраіля, лаўрэат Нобелеўскай прэміі міру (1994)",
            "ru": "Президент и премьер-министр Израиля, лауреат Нобелевской премии мира (1994)",
            "en": "President and Prime Minister of Israel, Nobel Peace Prize laureate (1994)"
        },
        "bio": {
            "by": "Нарадзіўся ў вёсцы Вішнева Валожынскага раёна Мінскай вобласці. Адзін з айцоў-заснавальнікаў ізраільскай дзяржаўнасці, двойчы прэм'ер-міністр і 9-ы прэзідэнт Ізраіля (2007–2014). За падпісанне мірных пагадненняў у Осла ўдастоены Нобелеўскай прэміі міру. Заснавальнік Цэнтра міру і інавацый у Яфе.",
            "ru": "Родился в деревне Вишнево Воложинского района. Патриарх израильской политики, дважды премьер-министр и 9-й президент Израиля. Лауреат Нобелевской премии мира 1994 года. Создатель Центра мира и инноваций Переса в Яффе.",
            "en": "Born in Vishneva (Valozhyn district). Founding father of Israeli statehood, defense strategist, two-time Prime Minister, and 9th President of Israel. Awarded the Nobel Peace Prize in 1994. Founded the Peres Center for Peace and Innovation in Jaffa."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Shimon_Peres_2009.jpg/480px-Shimon_Peres_2009.jpg",
        "wiki": "https://be.wikipedia.org/wiki/Шымон_Перэс",
        "placeIds": []
    },
    {
        "id": "isaac-asimov",
        "name": {
            "by": "Ісак Азімаў (Ісаак Азімаў)",
            "ru": "Айзек Азимов (Исаак Юдович Азимов)",
            "en": "Isaac Asimov"
        },
        "dates": "1920–1992",
        "role": {
            "by": "Сусветна вядомы пісьменнік-фантаст, папулярызатар навукі, прафесар біяхіміі",
            "ru": "Всемирно известный писатель-фантаст, популяризатор науки, профессор биохимии",
            "en": "World-renowned science fiction author, science popularizer, professor of biochemistry"
        },
        "bio": {
            "by": "Нарадзіўся ў мястэчку Пятровічы Клімавіцкага павета (тады Гомельская губерня / БССР). Прафесар біяхіміі Бостанскага ўніверсітэта. Напісаў і адрэдагаваў больш за 500 кніг. Аўтар Трох законаў робататэхнікі, цыклаў «Фундацыя», «Галактычная імперыя» і «Я, робат». Шматразовы лаўрэат прэмій «Х'юга» і «Неб'юла».",
            "ru": "Родился в местечке Петровичи Климовичского уезда. Профессор биохимии Бостонского университета. Автор более 500 книг, создатель Трёх законов робототехники и эпопей «Основание» и «Я, робот». Обладатель премий «Хьюго» и «Небьюла».",
            "en": "Born in Petrovichi (then Gomel Governorate). Professor of biochemistry at Boston University. Author of over 500 books, pioneer of the Three Laws of Robotics, and master of the legendary 'Foundation' and 'Robot' series. Recipient of numerous Hugo and Nebula awards."
        },
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Isaac.Asimov01.jpg/480px-Isaac.Asimov01.jpg",
        "wiki": "https://be.wikipedia.org/wiki/Айзэк_Азімаў",
        "placeIds": []
    }
]

# Dataset 2 person mappings
DATA2_PERSON_MAP = {
    "berlin-palais-radziwill": {"personId": "antoni-radziwill", "personIds": ["antoni-radziwill", "radziwills"]},
    "warszawa-palac-radziwillow": {"personId": "radziwills", "personIds": ["radziwills"]},
    "nieborow-palac-radziwillow": {"personId": "radziwills", "personIds": ["radziwills"]},
    "olyka-radziwill-castle": {"personId": "radziwills", "personIds": ["radziwills"]},
    "olyka-holy-trinity-collegiate": {"personId": "radziwills", "personIds": ["radziwills"]},
    "szydlowiec-radziwill-castle": {"personId": "radziwills", "personIds": ["radziwills"]},
    "palanga-tiskevicius-palace": {"personId": "tyszkiewicz", "personIds": ["tyszkiewicz"]},
    "kretinga-tiskevicius-palace": {"personId": "tyszkiewicz", "personIds": ["tyszkiewicz"]},
    "warszawa-palac-tyszkiewiczow": {"personId": "tyszkiewicz", "personIds": ["tyszkiewicz"]},
    "vilnius-chodkiewicz-palace": {"personId": "jan-karol-chodkiewicz", "personIds": ["jan-karol-chodkiewicz"]},
    "krakow-chodkiewicz-residence": {"personId": "jan-karol-chodkiewicz", "personIds": ["jan-karol-chodkiewicz"]},
    "khotyn-fortress-chodkiewicz": {"personId": "jan-karol-chodkiewicz", "personIds": ["jan-karol-chodkiewicz"]},
    "vilnius-st-michael-church-sapieha": {"personId": "lew-sapieha", "personIds": ["lew-sapieha"]},
    "vilnius-antakalnis-sapieha-palace": {"personId": "lew-sapieha", "personIds": ["lew-sapieha"]},
    "koden-sapieha-complex": {"personId": "lew-sapieha", "personIds": ["lew-sapieha"]},
    "krasiczyn-castle-sapieha": {"personId": "lew-sapieha", "personIds": ["lew-sapieha"]},
    "ringsted-queen-sophia-of-minsk-tomb": {"personId": "sophia-of-minsk", "personIds": ["sophia-of-minsk"]},
    "vilnius-cathedral-barbara-radziwill-crypt": {"personId": "barbara-radziwill", "personIds": ["barbara-radziwill", "radziwills"]},
    "warsaw-duchess-anna-radziwill-st-anne": {"personId": "anna-radziwill", "personIds": ["anna-radziwill", "radziwills"]},
    "vilnius-gediminas-monument": {"personId": "gediminas", "personIds": ["gediminas"]},
    "kaunas-vytautas-the-great-monument": {"personId": "vytautas", "personIds": ["vytautas"]},
    "senieji-trakai-vytautas-monument": {"personId": "vytautas", "personIds": ["vytautas"]},
    "grunwald-battle-memorial-stebark": {"personId": "vytautas", "personIds": ["vytautas"]},
}

# Dataset 3 person mappings
DATA3_PERSON_MAP = {
    "krakow-sukiennice-siemiradzki": {"personId": "henryk-siemiradzki", "personIds": ["henryk-siemiradzki"]},
    "lviv-art-gallery-siemiradzki": {"personId": "henryk-siemiradzki", "personIds": ["henryk-siemiradzki"]},
    "warsaw-mnw-matejko-grunwald": {"personId": "jan-matejko", "personIds": ["jan-matejko", "vytautas"]},
    "warsaw-royal-castle-matejko": {"personId": "jan-matejko", "personIds": ["jan-matejko"]},
    "lublin-castle-museum-unia-lubelska": {"personId": "jan-matejko", "personIds": ["jan-matejko"]},
    "vilnia-ndg-ruszczyc": {"personId": "ferdynand-ruszczyc", "personIds": ["ferdynand-ruszczyc"]},
    "warsaw-mnw-wankowicz-ruszczyc": {"personId": "ferdynand-ruszczyc", "personIds": ["ferdynand-ruszczyc", "walenty-wankowicz"]},
    "krakow-mnk-napoleon-orda": {"personId": "napoleon-orda", "personIds": ["napoleon-orda"]},
    "moscow-tretyakov-gallery-zhukovsky": {"personId": "stanislaw-zukowski", "personIds": ["stanislaw-zukowski"]},
    "los-angeles-walk-of-fame-louis-b-mayer": {"personId": "louis-b-mayer", "personIds": ["louis-b-mayer"]},
    "new-york-music-box-theatre-irving-berlin": {"personId": "irving-berlin", "personIds": ["irving-berlin"]},
    "new-york-rockefeller-center-david-sarnoff": {"personId": "david-sarnoff", "personIds": ["david-sarnoff"]},
    "houston-rothko-chapel": {"personId": "mark-rothko", "personIds": ["mark-rothko"]},
    "rehovot-weizmann-house": {"personId": "chaim-weizmann", "personIds": ["chaim-weizmann"]},
    "jaffa-peres-center-for-peace": {"personId": "shimon-peres", "personIds": ["shimon-peres"]},
    "boston-university-asimov-archive": {"personId": "isaac-asimov", "personIds": ["isaac-asimov"]},
}

def main():
    print("Starting dataset merge...")
    
    # 1. Load existing places
    with open('data/places.json', 'r', encoding='utf-8') as f:
        existing_places = json.load(f)
    print(f"Loaded existing places: {len(existing_places)}")
    places_map = {p['id']: p for p in existing_places}
    
    # 2. Parse raw message files
    with open('scratch/msg1.txt', 'r', encoding='utf-8') as f:
        t1 = f.read()
    m1 = re.search(r'```(?:json)?\s*(\[\s*\{.*\}\s*\])\s*```', t1, re.DOTALL)
    data1 = json.loads(m1.group(1)) if m1 else json.loads(t1.strip())
    print(f"Data 1 items: {len(data1)}")
    
    with open('scratch/msg2.txt', 'r', encoding='utf-8') as f:
        t2 = f.read()
    data2 = json.loads(t2.strip()).get('historicalSites', [])
    print(f"Data 2 items: {len(data2)}")
    
    with open('scratch/msg3.txt', 'r', encoding='utf-8') as f:
        t3 = f.read()
    m3 = re.search(r'```json\s*(\[\s*\{.*\}\s*\])\s*```', t3, re.DOTALL)
    data3 = json.loads(m3.group(1))
    print(f"Data 3 items: {len(data3)}")
    
    added_places = []
    updated_places = []
    
    # 3. Process Data 1
    for it in data1:
        processed = process_item(it)
        processed["unverifiedCoordinates"] = True
        processed["isUnverifiedCoordinates"] = True
        # Ensure personIds array exists
        if "personId" in processed:
            pid = processed["personId"]
            processed["personIds"] = [pid]
        
        if processed['id'] in places_map:
            print(f"Updating existing place with D1: {processed['id']}")
            places_map[processed['id']].update(processed)
            updated_places.append(processed['id'])
        else:
            places_map[processed['id']] = processed
            added_places.append(processed['id'])
            
    # 4. Process Data 2
    for it in data2:
        processed = process_item(it)
        processed["unverifiedCoordinates"] = True
        processed["isUnverifiedCoordinates"] = True
        
        # Apply person mappings
        if processed['id'] in DATA2_PERSON_MAP:
            pmap = DATA2_PERSON_MAP[processed['id']]
            processed['personId'] = pmap['personId']
            processed['personIds'] = pmap['personIds']
            
        if processed['id'] in places_map:
            print(f"Updating existing place with D2: {processed['id']}")
            places_map[processed['id']].update(processed)
            updated_places.append(processed['id'])
        else:
            places_map[processed['id']] = processed
            added_places.append(processed['id'])
            
    # 5. Process Data 3
    for it in data3:
        processed = process_item(it)
        processed["unverifiedCoordinates"] = True
        processed["isUnverifiedCoordinates"] = True
        
        # Apply person mappings
        if processed['id'] in DATA3_PERSON_MAP:
            pmap = DATA3_PERSON_MAP[processed['id']]
            processed['personId'] = pmap['personId']
            processed['personIds'] = pmap['personIds']
            
        if processed['id'] in places_map:
            print(f"Enriching existing place with D3 (items/images): {processed['id']}")
            # Enrich items if present
            if "items" in processed and processed["items"]:
                places_map[processed['id']]["items"] = processed["items"]
            if "image" in processed and processed["image"]:
                places_map[processed['id']]["image"] = processed["image"]
            if "personId" in processed and not places_map[processed['id']].get("personId"):
                places_map[processed['id']]["personId"] = processed["personId"]
            if "personIds" in processed:
                pids = set(places_map[processed['id']].get("personIds", []))
                for pid in processed["personIds"]:
                    pids.add(pid)
                places_map[processed['id']]["personIds"] = list(pids)
            updated_places.append(processed['id'])
        else:
            places_map[processed['id']] = processed
            added_places.append(processed['id'])
            
    final_places = list(places_map.values())
    print(f"Merged total places: {len(final_places)} (Added: {len(added_places)}, Updated: {len(updated_places)})")
    
    # 6. Save data/places.json
    with open('data/places.json', 'w', encoding='utf-8') as f:
        json.dump(final_places, f, ensure_ascii=False, indent=2)
    print("Saved data/places.json")
    
    # 7. Save data/places.js
    with open('data/places.js', 'w', encoding='utf-8') as f:
        f.write("window.PLACES_DATA = ")
        json.dump(final_places, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print("Saved data/places.js")
    
    # 8. Process Persons
    with open('data/persons.json', 'r', encoding='utf-8') as f:
        existing_persons = json.load(f)
    print(f"Loaded existing persons: {len(existing_persons)}")
    persons_map = {p['id']: p for p in existing_persons}
    
    # Add new persons
    for p in NEW_PERSONS:
        if p['id'] not in persons_map:
            persons_map[p['id']] = p
            print(f"Added new person: {p['id']} - {p['name']['by']}")
        else:
            print(f"Person already exists: {p['id']}")
            
    # Calculate bidirectional placeIds for each person
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
    print(f"Total persons: {len(final_persons)}")
    
    # 9. Save data/persons.json
    with open('data/persons.json', 'w', encoding='utf-8') as f:
        json.dump(final_persons, f, ensure_ascii=False, indent=2)
    print("Saved data/persons.json")
    
    # 10. Save data/persons.js
    with open('data/persons.js', 'w', encoding='utf-8') as f:
        f.write("window.PERSONS_DATA = ")
        json.dump(final_persons, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print("Saved data/persons.js")
    
    print("\nDataset merge complete successfully!")

if __name__ == '__main__':
    main()
