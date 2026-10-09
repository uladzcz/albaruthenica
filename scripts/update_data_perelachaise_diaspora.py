import json
import os

def update_dataset():
    with open('data/places.json', 'r', encoding='utf-8') as f:
        places = json.load(f)
    with open('data/persons.json', 'r', encoding='utf-8') as f:
        persons = json.load(f)

    # 1. Fix school and Podlasie images
    for p in places:
        if p['id'] == 'bielsk-podlaski-szkola-3-hajduk':
            p['image'] = ''
        elif p['id'] == 'bialystok-skver-tamary-salanevich':
            p['image'] = ''
        elif p['id'] == 'studziwody-muzej-maloj-backauszcyny':
            p['image'] = ''
        elif p['id'] == 'grabarka-sviataya-hara':
            p['image'] = 'https://upload.wikimedia.org/wikipedia/commons/2/2a/Transfiguration_of_Jesus_Christ_church_in_Grabarka_-_exterior_%281%29.jpg'

    # 2. Add new persons
    new_persons = [
        {
            "id": "mikola-abramchyk",
            "name": {
                "by": "Мікола Абрамчык",
                "ru": "Николай Абрамчик",
                "en": "Mikoła Abramčyk"
            },
            "dates": "1903–1970",
            "role": {
                "by": "Старшыня (Прэзідэнт) Рады БНР (1943–1970), грамадска-палітычны дзеяч эміграцыі",
                "ru": "Председатель (Президент) Рады БНР (1943–1970), деятель эмиграции",
                "en": "President of the Rada of the Belarusian Democratic Republic (1943–1970)"
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/%D0%9C%D1%96%D0%BA%D0%BE%D0%BB%D0%B0_%D0%90%D0%B1%D1%80%D0%B0%D0%BC%D1%87%D1%8B%D0%BA.png/330px-%D0%9C%D1%96%D0%BA%D0%BE%D0%BB%D0%B0_%D0%90%D0%B1%D1%80%D0%B0%D0%BC%D1%87%D1%8B%D0%BA.png",
            "bio": {
                "by": "Нарадзіўся ў Сычавічах пад Радашковічамі. Вучыўся ў Празе, дзяяч БНР, выдавец і арганізатар беларускага жыцця ў Францыі і Еўропе, аўтар працы «Гісторыя Беларусі ў картах і малюнках». З 1943 па 1970 гг. — Старшыня Рады Беларускай Народнай Рэспублікі.",
                "ru": "Родился под Радошковичами. Учился в Праге, председатель Рады БНР (1943–1970), издатель и организатор белорусской диаспоры во Франции.",
                "en": "Born near Radaszkowiczy. Belarusian statesman and journalist, President of the Rada of the Belarusian Democratic Republic in exile from 1943 until his death in 1970."
            },
            "placeIds": ["paris-cmentarz-pere-lachaise"]
        },
        {
            "id": "nina-abramchyk",
            "name": {
                "by": "Ніна Абрамчык",
                "ru": "Нина Абрамчик",
                "en": "Nina Abramčyk"
            },
            "dates": "1916–2004",
            "role": {
                "by": "Грамадска-палітычная дзяячка, пісьменніца, сакратарка Рады БНР",
                "ru": "Общественный деятель диаспоры, писательница, секретарь Рады БНР",
                "en": "Belarusian diaspora activist, writer, secretary of Rada BNR"
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Portrait_Placeholder.png/440px-Portrait_Placeholder.png",
            "bio": {
                "by": "Нарадзілася ў Шацку (цяпер Пухавіцкі р-н). Беларуская грамадская дзяячка ў Францыі, рэдактарка часопіса «Раніца», адна з кіраўніц Беларускага хаўруса ў Францыі, аўтарка літаратурных і публіцыстычных твораў пад псеўданімам Ніна Раса.",
                "ru": "Белорусская общественная деятельница во Франции, писательница (псевдоним Нина Роса), супруга президента Рады БНР Николая Абрамчика.",
                "en": "Belarusian activist in Paris, writer (pen name Nina Rasa), secretary of Rada BNR and wife of Mikoła Abramčyk."
            },
            "placeIds": ["paris-cmentarz-pere-lachaise"]
        },
        {
            "id": "tadeusz-tyszkiewicz",
            "name": {
                "by": "Тадэвуш Тышкевіч",
                "ru": "Тадеуш Тышкевич",
                "en": "Tadeusz Tyszkiewicz"
            },
            "dates": "1774–1852",
            "role": {
                "by": "Брыгадны генерал войскаў ВКЛ, сенатар, паўстанец 1794 і 1830–1831 гг.",
                "ru": "Бригадный генерал войск ВКЛ, сенатор, участник восстаний 1794 и 1830–1831 гг.",
                "en": "Brigadier General of the Grand Duchy of Lithuania, Senator, 1830 Insurgent"
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Tadevu%C5%A1_Ty%C5%A1kievi%C4%8D._%D0%A2%D0%B0%D0%B4%D1%8D%D0%B2%D1%83%D1%88_%D0%A2%D1%8B%D1%88%D0%BA%D0%B5%D0%B2%D1%96%D1%87_%281910%29.jpg/330px-Tadevu%C5%A1_Ty%C5%A1kievi%C4%8D._%D0%A2%D0%B0%D0%B4%D1%8D%D0%B2%D1%83%D1%88_%D0%A2%D1%8B%D1%88%D0%BA%D0%B5%D0%B2%D1%96%D1%87_%281910%29.jpg",
            "bio": {
                "by": "Нарадзіўся ў Белавежы (Камянецкі р-н). Генерал-маёр, удзельнік паўстання Касцюшкі, кампаній Напалеона і паўстання 1830–1831 гадоў, старшыня Часовага цэнтральнага камітэта на Літве і ў Беларусі.",
                "ru": "Родился в Беловеже. Бригадный генерал, участник восстания Костюшко, наполеоновских войн и восстания 1830–1831 гг. Возглавлял Временный комитет в Литве и Беларуси.",
                "en": "Born in Belavezha. General of the Grand Duchy of Lithuania, veteran of Kościuszko Uprising, Napoleonic campaigns, and 1830 November Uprising."
            },
            "placeIds": ["paris-cmentarz-pere-lachaise"]
        },
        {
            "id": "tytus-puslowski",
            "name": {
                "by": "Адам Цітус Пуслоўскі",
                "ru": "Адам Тит Пусловский",
                "en": "Adam Tytus Pusłowski"
            },
            "dates": "1803–1854",
            "role": {
                "by": "Паўстанец 1830–1831 гг. на Палессі і ў Белавежы, мецэнат",
                "ru": "Повстанец 1830–1831 гг. на Полесье и в Беловеже",
                "en": "1830 Insurgent in Polesia, nobleman of Pusłowski house"
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Portrait_Placeholder.png/440px-Portrait_Placeholder.png",
            "bio": {
                "by": "Сын Войцеха Пуслоўскага, нарадзіўся ў маёнтку Пяскі (Бярозаўскі р-н). Камандзір паўстанцкага атрада на Палессі і ў Белавежскай пушчы ў 1831 годзе. Пасля паражэння паўстання эміграваў у Францыю.",
                "ru": "Сын Войцеха Пусловского, родился в Песках. Командир повстанческого отряда на Полесье и в Беловежской пуще (1831 г.). Жил в эмиграции в Париже.",
                "en": "Son of Wojciech Pusłowski, commander of insurgent unit in Polesia and Belovezha Forest in 1831. Exiled to France."
            },
            "placeIds": ["paris-cmentarz-pere-lachaise"]
        },
        {
            "id": "jacob-balgley",
            "name": {
                "by": "Якаў Балглей",
                "ru": "Яков Балглей",
                "en": "Jacob Balgley"
            },
            "dates": "1891–1934",
            "role": {
                "by": "Мастак-жывапісец і гравёр Парыжскай школы (родам з Брэста)",
                "ru": "Художник и гравер Парижской школы (уроженец Бреста)",
                "en": "Painter and engraver of School of Paris, native of Brest"
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Jacob_Balgley_self-portrait.jpg/330px-Jacob_Balgley_self-portrait.jpg",
            "bio": {
                "by": "Нарадзіўся ў Брэст-Літоўску ў сям'і рабіна. Выбітны прадстаўнік знакамітай Парыжскай школы (École de Paris), майстар афорта і жывапісу. Творы захоўваюцца ў музеях Парыжа, Іерусаліма і па ўсім свеце.",
                "ru": "Родился в Брест-Литовске. Видный представитель Парижской школы, мастер офорта и живописи.",
                "en": "Born in Brest-Litovsk. Notable painter and printmaker of the School of Paris."
            },
            "placeIds": ["paris-cmentarz-pere-lachaise"]
        },
        {
            "id": "mikalaj-minski",
            "name": {
                "by": "Мікалай Мінскі (Віленкін)",
                "ru": "Николай Минский (Виленкин)",
                "en": "Nikolai Minsky"
            },
            "dates": "1855–1937",
            "role": {
                "by": "Паэт Срэбнага веку, філосаф, перакладчык «Іліяды» (родам з Глыбокага)",
                "ru": "Поэт Серебряного века, философ, переводчик (уроженец Глубокого)",
                "en": "Silver Age poet, philosopher, translator of Iliad (native of Hlybokaye)"
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Nikolay_Minsky.jpg/330px-Nikolay_Minsky.jpg",
            "bio": {
                "by": "Нарадзіўся ў Глыбокім Дзісненскага павета Віленскай губерні (цяпер Віцебская вобласць). Выдатны паэт-сімваліст, мысліцель, перакладчык Гамера, Персі Бішы Шэлі і Верлена. Памёр у Парыжы.",
                "ru": "Родился в Глубоком. Поэт Серебряного века, один из зачинателей русского символизма, философ, переводчик Гомера.",
                "en": "Born in Hlybokaye (Vitebsk Region). Prominent Silver Age symbolist poet, philosopher, and translator of Homer's Iliad."
            },
            "placeIds": ["paris-cmentarz-pere-lachaise"]
        },
        {
            "id": "ewelina-hanska",
            "name": {
                "by": "Эвеліна Ганская (Жавуская)",
                "ru": "Эвелина Ганская (Ржевуская)",
                "en": "Ewelina Hańska (Rzewuska)"
            },
            "dates": "1805–1882",
            "role": {
                "by": "Графіня з роду Жавускіх, муза і жонка Анарэ дэ Бальзака",
                "ru": "Графиня из рода Ржевуских, муза и супруга Оноре де Бальзака",
                "en": "Countess of Rzewuski house, wife and muse of Honoré de Balzac"
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Ewelina_Hanska_circa_1825.jpg/330px-Ewelina_Hanska_circa_1825.jpg",
            "bio": {
                "by": "Графіня з магнацкага роду Жавускіх. Шматгадовая карэспандэнтка, каханая і законная жонка Анарэ дэ Бальзака, якая адыграла ключавую ролю ў яго творчасці. Пахаваная разам з Бальзакам на могілках Пер-Лашэз.",
                "ru": "Графиня из рода Ржевуских, муза и супруга Оноре де Бальзака. Похоронена вместе с Бальзаком на кладбище Пер-Лашез.",
                "en": "Noblewoman of Rzewuski family, longtime correspondent and wife of French novelist Honoré de Balzac. Interred with Balzac in division 48 of Père Lachaise."
            },
            "placeIds": ["paris-cmentarz-pere-lachaise"]
        }
    ]

    existing_person_ids = {p['id'] for p in persons}
    for np in new_persons:
        if np['id'] not in existing_person_ids:
            persons.append(np)
            existing_person_ids.add(np['id'])

    # Ensure valery-urubleuski links to paris-cmentarz-pere-lachaise
    for per in persons:
        if per['id'] == 'valery-urubleuski':
            if 'paris-cmentarz-pere-lachaise' not in per.get('placeIds', []):
                per.setdefault('placeIds', []).append('paris-cmentarz-pere-lachaise')

    # 3. Restructure / replace paris-pere-lachaise-valery-wroblewski-grave with composite hub paris-cmentarz-pere-lachaise
    pere_lachaise_hub = {
        "id": "paris-cmentarz-pere-lachaise",
        "title": {
            "by": "Могілкі Пер-Лашэз: беларускі пантэон у Парыжы",
            "ru": "Кладбище Пер-Лашез: белорусский пантеон в Париже",
            "en": "Père Lachaise Cemetery: Belarusian Pantheon in Paris"
        },
        "category": "grave",
        "country": {
            "by": "Францыя",
            "ru": "Франция",
            "en": "France"
        },
        "city": {
            "by": "Парыж",
            "ru": "Париж",
            "en": "Paris"
        },
        "coordinates": [
            48.8614,
            2.3965
        ],
        "image": "https://upload.wikimedia.org/wikipedia/commons/d/d1/P%C3%A8re-Lachaise_-_Division_76_-_Wroblewski_03.jpg",
        "description": {
            "by": "Сусветна вядомыя могілкі Пер-Лашэз (Cimetière du Père-Lachaise, 20-я акруга Парыжа) з'яўляюцца найважнейшым мемарыяльным месцам беларускай гісторыі ў Францыі. Тут спачываюць выбітныя дзеячы розных эпох: кіраўнік паўстання 1863 года і генерал Парыжскай камуны Валерый Урублеўскі (сект. 76), Прэзідэнт Рады Беларускай Народнай Рэспублікі Мікола Абрамчык і яго жонка пісьменніца Ніна Абрамчык (сект. 59), паўстанцы генералы Тадэвуш Тышкевіч (сект. 54) і Адам Цітус Пуслоўскі (сект. 26), мастак Парыжскай школы родам з Брэста Якаў Балглей, паэт з Глыбокага Мікалай Мінскі, а таксама жонка Бальзака графіня Эвеліна Ганская з роду Жавускіх (сект. 48).",
            "ru": "Знаменитое кладбище Пер-Лашез в Париже хранит память о выдающихся уроженцах Беларуси: генерале восстания 1863 года и Парижской коммуны Валерии Врублевском (сект. 76), Президенте Рады БНР Николае Абрамчике и его супруге Нине Абрамчик (сект. 59), генерале Тадеуше Тышкевиче (сект. 54), повстанце Адаме Тите Пусловском (сект. 26), художнике Парижской школы Якове Балглее, поэте Николае Минском и супруге Бальзака Эвелине Ганской (Ржевуской) (сект. 48).",
            "en": "The renowned Père Lachaise Cemetery in Paris holds the graves of prominent Belarusian leaders, insurgents, and cultural figures: General Walery Antoni Wróblewski of the 1863 Uprising and Paris Commune (div. 76), Rada BNR President Mikoła Abramčyk and writer Nina Abramčyk (div. 59), General Count Tadeusz Tyszkiewicz (div. 54), 1830 insurgent Adam Tytus Pusłowski (div. 26), School of Paris artist Jacob Balgley, poet Nikolai Minsky, and Balzac's wife Countess Ewelina Hańska (div. 48)."
        },
        "links": [
            {
                "title": "Вікіпедыя: Могілкі Пер-Лашэз",
                "url": "https://be.wikipedia.org/wiki/Могілкі_Пер-Лашэз"
            },
            {
                "title": "Вікіпедыя: Валерый Урублеўскі",
                "url": "https://be.wikipedia.org/wiki/Валерый_Антонавіч_Урублеўскі"
            },
            {
                "title": "Вікіпедыя: Мікола Абрамчык",
                "url": "https://be.wikipedia.org/wiki/Мікола_Абрамчык"
            }
        ],
        "tags": [
            "магіла",
            "пантэон",
            "Францыя",
            "Парыж",
            "Пер-Лашэз",
            "паўстанне1863",
            "БНР",
            "эміграцыя",
            "мастацтва"
        ],
        "personIds": [
            "valery-urubleuski",
            "mikola-abramchyk",
            "nina-abramchyk",
            "tadeusz-tyszkiewicz",
            "tytus-puslowski",
            "jacob-balgley",
            "mikalaj-minski",
            "ewelina-hanska"
        ],
        "mustSee": True,
        "items": [
            {
                "title": "Магіла генерала Валерыя Урублеўскага (Сцяна камунараў)",
                "person": "Валерый Урублеўскі (1836–1908)",
                "personId": "valery-urubleuski",
                "year": "1908",
                "description": "Сектар 76 (Division 76), каля Сцяны камунараў (Mur des Fédérés). Манументальны бюст герою вызваленчага паўстання 1863 года на Гродзеншчыне і Падляшшы і генералу паўсталай Парыжскай камуны.",
                "image": "https://upload.wikimedia.org/wikipedia/commons/d/d1/P%C3%A8re-Lachaise_-_Division_76_-_Wroblewski_03.jpg"
            },
            {
                "title": "Магіла Міколы і Ніны Абрамчыкаў",
                "person": "Мікола Абрамчык (1903–1970), Ніна Абрамчык (1916–2004)",
                "personId": "mikola-abramchyk",
                "year": "1970",
                "description": "Сектар 59 (Division 59). Месца спачыну Старшыні (Прэзідэнта) Рады Беларускай Народнай Рэспублікі ў 1943–1970 гг. і яго жонкі, пісьменніцы і сакратаркі Рады БНР Ніны Абрамчык (Ляўковіч). На надмагіллі высечана: «Président du Conseil de la République Populaire Biélorussienne».",
                "image": "https://upload.wikimedia.org/wikipedia/commons/a/a7/P%C3%A8re-Lachaise_-_Division_59_-_Abramtchik_01.jpg"
            },
            {
                "title": "Магіла генерала графа Тадэвуша Тышкевіча",
                "person": "Тадэвуш Тышкевіч (1774–1852)",
                "personId": "tadeusz-tyszkiewicz",
                "year": "1852",
                "description": "Сектар 54 (Division 54). Брыгадны генерал войскаў ВКЛ, сенатар, удзельнік паўстання Касцюшкі і паўстання 1830–1831 гг. Нарадзіўся ў Белавежы на Камянеччыне.",
                "image": "https://upload.wikimedia.org/wikipedia/commons/2/23/P%C3%A8re-Lachaise_-_Division_54_-_Thad%C3%A9e_Tuszkiewicz_01.jpg"
            },
            {
                "title": "Магіла Адама Цітуса Пуслоўскага",
                "person": "Адам Цітус Пуслоўскі (1803–1854)",
                "personId": "tytus-puslowski",
                "year": "1854",
                "description": "Сектар 26 (Division 26). Паўстанец 1830–1831 гг., арганізатар баявых атрадаў у Белавежскай пушчы і на Палессі, прадстаўнік роду Пуслоўскіх (Пяскі / Косава).",
                "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Entree_Pere_Lachaise.jpg/960px-Entree_Pere_Lachaise.jpg"
            },
            {
                "title": "Месца спачыну Якава Балглея",
                "person": "Якаў Балглей (1891–1934)",
                "personId": "jacob-balgley",
                "year": "1934",
                "description": "Выбітны мастак-жывапісец і майстар гравюры славутай Парыжскай школы (École de Paris), ураджэнец Брэста.",
                "image": "https://upload.wikimedia.org/wikipedia/commons/a/ab/Jacob_Balgley_self-portrait.jpg"
            },
            {
                "title": "Месца спачыну Мікалая Мінскага (Віленкіна)",
                "person": "Мікалай Мінскі (1855–1937)",
                "personId": "mikalaj-minski",
                "year": "1937",
                "description": "Калумбарый могілак Пер-Лашэз. Паэт Срэбнага веку, філосаф і перакладчык «Іліяды», ураджэнец мястэчка Глыбокае.",
                "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Nikolay_Minsky.jpg/330px-Nikolay_Minsky.jpg"
            },
            {
                "title": "Сумесная грабніца Анарэ дэ Бальзака і графіні Эвеліны Ганскай",
                "person": "Эвеліна Ганская (1805–1882)",
                "personId": "ewelina-hanska",
                "year": "1882",
                "description": "Сектар 48 (Division 48). Знакамітая грабніца выдатнага французскага класіка Анарэ дэ Бальзака і яго каханай жонкі і музы графіні Эвеліны Ганскай з магнацкага роду Жавускіх.",
                "image": "https://upload.wikimedia.org/wikipedia/commons/9/9e/P%C3%A8re-Lachaise_-_Division_48_-_Balzac_02.jpg"
            }
        ]
    }

    # Replace old Wroblewski solitary entry with the composite Père Lachaise hub
    replaced = False
    for i, p in enumerate(places):
        if p['id'] in ['paris-pere-lachaise-valery-wroblewski-grave', 'paris-cmentarz-pere-lachaise']:
            places[i] = pere_lachaise_hub
            replaced = True
            break
    if not replaced:
        places.append(pere_lachaise_hub)

    # 4. Add key diaspora organizations from Wikipedia category
    diaspora_places = [
        {
            "id": "bialystok-bgkt",
            "title": {
                "by": "Беларускае грамадска-культурнае таварыства (БГКТ)",
                "ru": "Белорусское общественно-культурное общество (БОКО)",
                "en": "Belarusian Social and Cultural Association (BTSK in Białystok)"
            },
            "category": "culture",
            "country": {
                "by": "Польшча",
                "ru": "Польша",
                "en": "Poland"
            },
            "city": {
                "by": "Беласток",
                "ru": "Белосток",
                "en": "Białystok"
            },
            "coordinates": [
                53.1332,
                23.1678
            ],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Warszawska_11_Bialystok.jpg/960px-Warszawska_11_Bialystok.jpg",
            "description": {
                "by": "Гістарычная штаб-кватэра Беларускага грамадска-культурнага таварыства ў Польшчы (вул. Варшаўская 11, Беласток). БГКТ было заснаванае ў 1956 годзе і стала найстарэйшай і найбуйнейшай арганізацыяй беларускай меншасці ў паваеннай Польшчы. Тут дзейнічалі выдавецтвы, ладзіліся фестывалі песні, выставы беларускіх мастакоў і грамадскія імпрэзы.",
                "ru": "Историческая штаб-квартира Белорусского общественно-культурного общества в Польше (ул. Варшавская 11, Белосток). Старейшая организация белорусского меньшинства в Польше, основана в 1956 г.",
                "en": "Headquarters of the Belarusian Social and Cultural Association in Poland (BTSK) at Warszawska 11, Białystok. Founded in 1956, it is the oldest postwar organization of the Belarusian minority in Poland."
            },
            "links": [
                {
                    "title": "Вікіпедыя: Беларускае грамадска-культурнае таварыства",
                    "url": "https://be.wikipedia.org/wiki/Беларускае_грамадска-культурнае_таварыства"
                }
            ],
            "tags": [
                "БГКТ",
                "Беласток",
                "Польшча",
                "Падляшша",
                "дыяспара",
                "культура"
            ],
            "mustSee": True
        },
        {
            "id": "hajnowka-museum-belarusian",
            "title": {
                "by": "Музей і асяродак беларускай культуры ў Гайнаўцы",
                "ru": "Музей белорусской культуры в Гайновке",
                "en": "Museum and Center of Belarusian Culture in Hajnówka"
            },
            "category": "culture",
            "country": {
                "by": "Польшча",
                "ru": "Польша",
                "en": "Poland"
            },
            "city": {
                "by": "Гайнаўка",
                "ru": "Гайновка",
                "en": "Hajnówka"
            },
            "coordinates": [
                52.7423,
                23.5781
            ],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Hajnowka_-_Muzeum_i_Osrodek_Kultury_Bialoruskiej_01.jpg/960px-Hajnowka_-_Muzeum_i_Osrodek_Kultury_Bialoruskiej_01.jpg",
            "description": {
                "by": "Музей і асяродак беларускай культуры (вул. 3 Мая 42, Гайнаўка) — унікальная музейная ўстанова, прысвечаная гісторыі, традыцыйнаму побыту, рамёствам і мастацтву беларусаў Падляшша. У музеі дзейнічаюць экспазіцыі традыцыйнага ткацтва, ганчарства, кавальства, а таксама сучасная мастацкая галерэя і бібліятэка.",
                "ru": "Музей белорусской культуры в Гайновке (ул. 3 Мая 42) — уникальный музей традиционного быта, ремесел и искусства белорусов Подляшья.",
                "en": "Museum and Center of Belarusian Culture in Hajnówka (ul. 3 Maja 42), showcasing the heritage, crafts, folklore, and art of Podlasie Belarusians."
            },
            "links": [
                {
                    "title": "Вікіпедыя: Музей беларускай культуры ў Гайнаўцы",
                    "url": "https://be.wikipedia.org/wiki/Музей_і_асяродак_беларускай_культуры_ў_Гайнаўцы"
                }
            ],
            "tags": [
                "Гайнаўка",
                "музей",
                "Падляшша",
                "Польшча",
                "этнаграфія",
                "культура"
            ],
            "mustSee": True
        },
        {
            "id": "london-belarusian-house-zbvb",
            "title": {
                "by": "Беларускі дом і Згуртаванне беларусаў у Вялікай Брытаніі (ЗБВБ)",
                "ru": "Белорусский дом и Объединение белорусов Великобритании",
                "en": "Belarusian House & Association of Belarusians in Great Britain"
            },
            "category": "culture",
            "country": {
                "by": "Вялікабрытанія",
                "ru": "Великобритания",
                "en": "United Kingdom"
            },
            "city": {
                "by": "Лондан",
                "ru": "Лондон",
                "en": "London"
            },
            "coordinates": [
                51.5542,
                -0.1195
            ],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/52_Penn_Road_London.jpg/960px-52_Penn_Road_London.jpg",
            "description": {
                "by": "Беларускі дом у Лондане (52 Penn Road, London N7 9RE) — галоўны асяродак беларускага грамадскага і культурнага жыцця ў Вялікабрытаніі з 1960 года. Тут месціцца Згуртаванне беларусаў у Вялікай Брытаніі (ЗБВБ, заснаванае ў 1946 г.), Англа-беларускае таварыства, праходзяць урачыстасці да Дня Волі і сустрэчы беларусаў брытанскай сталіцы.",
                "ru": "Белорусский дом в Лондоне (52 Penn Road) — центр общественной жизни диаспоры с 1960 г. Штаб-квартира Объединения белорусов Великобритании (ЗБВБ, осн. 1946).",
                "en": "Belarusian House in London (52 Penn Road), headquarters of the Association of Belarusians in Great Britain (founded 1946) and premier community hub since 1960."
            },
            "links": [
                {
                    "title": "Вікіпедыя: Згуртаванне беларусаў у Вялікай Брытаніі",
                    "url": "https://be.wikipedia.org/wiki/Згуртаванне_беларусаў_у_Вялікай_Брытаніі"
                }
            ],
            "tags": [
                "Лондан",
                "Вялікабрытанія",
                "ЗБВБ",
                "дыяспара",
                "культура"
            ],
            "mustSee": True
        },
        {
            "id": "london-church-st-cyril-turau",
            "title": {
                "by": "Царква Святога Кірылы Тураўскага ў Лондане",
                "ru": "Церковь Святого Кирилла Туровского в Лондоне",
                "en": "Church of St Cyril of Turau in London"
            },
            "category": "church",
            "country": {
                "by": "Вялікабрытанія",
                "ru": "Великобритания",
                "en": "United Kingdom"
            },
            "city": {
                "by": "Лондан",
                "ru": "Лондон",
                "en": "London"
            },
            "coordinates": [
                51.6192,
                -0.1852
            ],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Church_of_St_Cyril_of_Turau_and_All_the_Patron_Saints_of_the_Belarusian_People.jpg/960px-Church_of_St_Cyril_of_Turau_and_All_the_Patron_Saints_of_the_Belarusian_People.jpg",
            "description": {
                "by": "Беларуская царква Святога Кірылы Тураўскага і ўсіх святых заступнікаў беларускага народа (Holden Road, London N12 8HS, каля Бібліятэкі імя Скарыны). Пабудаваная ў 2016 годзе ў традыцыях беларускага драўлянага барока (архітэктар Цзыўай Со) як мемарыял ахвярам Чарнобыльскай катастрофы. Першы драўляны храм у Лондане пасля 1666 года, лаўрэат прэстыжных міжнародных архітэктурных прэмій.",
                "ru": "Белорусская церковь Св. Кирилла Туровского в Лондоне (2016 г., арх. Цзывай Со). Построена в традициях белорусского деревянного барокко как мемориал Чернобыля.",
                "en": "Church of St Cyril of Turau and All the Patron Saints of the Belarusian People in London (built 2016, architect Tszwai So). Award-winning wooden church built in Belarusian baroque vernacular as a Chernobyl memorial."
            },
            "links": [
                {
                    "title": "Вікіпедыя: Царква Святога Кірылы Тураўскага (Лондан)",
                    "url": "https://be.wikipedia.org/wiki/Царква_Святога_Кірылы_Тураўскага_і_ўсіх_святых_заступнікаў_беларускага_народа"
                }
            ],
            "tags": [
                "Лондан",
                "Вялікабрытанія",
                "храм",
                "царква",
                "Кірыла Тураўскі",
                "архітэктура",
                "Чарнобыль"
            ],
            "mustSee": True
        },
        {
            "id": "toronto-belarusian-center",
            "title": {
                "by": "Беларускі грамадска-рэлігійны цэнтр і Згуртаванне беларусаў Канады (Таронта)",
                "ru": "Белорусский центр и Объединение белорусов Канады (Торонто)",
                "en": "Belarusian Community Center & Canadian Alliance (Toronto)"
            },
            "category": "culture",
            "country": {
                "by": "Канада",
                "ru": "Канада",
                "en": "Canada"
            },
            "city": {
                "by": "Таронта",
                "ru": "Торонто",
                "en": "Toronto"
            },
            "coordinates": [
                43.6596,
                -79.4422
            ],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Toronto_St_Clarens_Belarusian_Church.jpg/960px-Toronto_St_Clarens_Belarusian_Church.jpg",
            "description": {
                "by": "Беларускі цэнтр і царква Жыровіцкай Божай Маці ў Таронта (524 Saint Clarens Ave, Toronto, ON M6H 3W7). Галоўная сядзіба Згуртавання беларусаў Канады (ЗБК, засн. 1948). Тут дзесяцігоддзямі дзейнічалі школа беларусаведы, моладзевыя суполкі, музейныя і выдавецкія праекты беларусаў Канады.",
                "ru": "Белорусский центр и церковь Жировичской Богоматери в Торонто (524 St Clarens Ave). Главный центр Объединения белорусов Канады (осн. 1948).",
                "en": "Belarusian Center and Church of St. Mary of Žyrovičy in Toronto (524 St Clarens Ave). Headquarters of the Belarusian Canadian Alliance (founded 1948)."
            },
            "links": [
                {
                    "title": "Вікіпедыя: Згуртаванне беларусаў Канады",
                    "url": "https://be.wikipedia.org/wiki/Згуртаванне_беларусаў_Канады"
                }
            ],
            "tags": [
                "Канада",
                "Таронта",
                "ЗБК",
                "дыяспара",
                "культура"
            ],
            "mustSee": True
        },
        {
            "id": "prague-belarusian-archive-bnr",
            "title": {
                "by": "Беларускі загранічны архіў і прадстаўніцтва БНР у Празе",
                "ru": "Белорусский заграничный архив и представительство БНР в Праге",
                "en": "Belarusian Foreign Archive & BNR Center in Prague"
            },
            "category": "historical",
            "country": {
                "by": "Чэхія",
                "ru": "Чехия",
                "en": "Czech Republic"
            },
            "city": {
                "by": "Прага",
                "ru": "Прага",
                "en": "Prague"
            },
            "coordinates": [
                50.0865,
                14.4162
            ],
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Klementinum_2011.jpg/960px-Klementinum_2011.jpg",
            "description": {
                "by": "Прага ў міжваенны час (1920–1940-я гг.) была сталіцай урада Беларускай Народнай Рэспублікі ў эміграцыі і цэнтрам беларускага студэнцтва. У гістарычным комплексе Клеменцінум (Klementinum) і архіўных установах Прагі размяшчаўся Беларускі загранічны архіў, дзе захоўваліся ўнікальныя дзяржаўныя дакументы БНР, зборы Пятра Крэчэўскага, Васіля Захаркі, грамадскіх і студэнцкіх суполак.",
                "ru": "В межвоенный период Прага была центром правительства БНР в эмиграции и белорусского студенчества. В комплексе Клементинум и архивах Праги размещался Белорусский заграничный архив с государственными документами БНР.",
                "en": "Between the world wars, Prague was the seat of the Rada of the Belarusian Democratic Republic (BNR) in exile and student organizations. The Belarusian Foreign Archive in Prague preserved vital national historical records."
            },
            "links": [
                {
                    "title": "Вікіпедыя: Беларускі загранічны архіў",
                    "url": "https://be.wikipedia.org/wiki/Беларускі_загранічны_архіў"
                }
            ],
            "tags": [
                "Прага",
                "Чэхія",
                "БНР",
                "архіў",
                "гісторыя",
                "Клеменцінум"
            ],
            "mustSee": True
        }
    ]

    existing_place_ids = {p['id'] for p in places}
    for dp in diaspora_places:
        if dp['id'] not in existing_place_ids:
            places.append(dp)
            existing_place_ids.add(dp['id'])

    # Write back data/places.json and data/places.js
    with open('data/places.json', 'w', encoding='utf-8') as f:
        json.dump(places, f, ensure_ascii=False, indent=2)

    with open('data/places.js', 'w', encoding='utf-8') as f:
        f.write('window.INITIAL_PLACES = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

    # Write back data/persons.json and data/persons.js
    with open('data/persons.json', 'w', encoding='utf-8') as f:
        json.dump(persons, f, ensure_ascii=False, indent=2)

    with open('data/persons.js', 'w', encoding='utf-8') as f:
        f.write('window.INITIAL_PERSONS = ' + json.dumps(persons, ensure_ascii=False, indent=2) + ';\n')

    print("Updated places and persons successfully!")

if __name__ == '__main__':
    update_dataset()
