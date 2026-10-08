import xml.etree.ElementTree as ET
import json
import re
import os

def clean_html(raw_html):
    if not raw_html:
        return ""
    # Replace <br> tags with newlines
    text = re.sub(r'<br\s*/?>', '\n', raw_html, flags=re.IGNORECASE)
    # Remove all other HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Collapse multiple newlines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def detect_category(name, desc):
    combined = (name + " " + desc).lower()
    if any(w in combined for w in ["могілкі", "пахаван", "магіл", "некропаль"]):
        return "grave"
    if any(w in combined for w in ["царква", "касцёл", "сабор", "кляштар", "манастыр", "брама"]):
        return "church"
    if any(w in combined for w in ["помнік", "бюст", "скульптур"]):
        return "monument"
    if any(w in combined for w in ["шыльд", "дошк"]):
        return "plaque"
    if any(w in combined for w in ["музей", "галерэя", "бібліятэк", "тэатр", "клуб", "выдавецтв", "кнігарн"]):
        return "culture"
    return "historical"

def slugify(text):
    text = text.lower()
    translit_map = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'д': 'd', 'е': 'e', 'ё': 'yo',
        'ж': 'zh', 'з': 'z', 'і': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
        'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
        'ў': 'w', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'ы': 'y',
        'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya', '’': '', "'": '', '"': ''
    }
    res = []
    for char in text:
        if char in translit_map:
            res.append(translit_map[char])
        elif char.isalnum():
            res.append(char)
        else:
            res.append('-')
    slug = ''.join(res)
    slug = re.sub(r'-+', '-', slug).strip('-')
    return slug[:45]

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    places_json_path = os.path.join(base_dir, "data", "places.json")
    places_js_path = os.path.join(base_dir, "data", "places.js")
    kml_path = os.path.join(base_dir, "scratch_vilnia.kml")

    with open(places_json_path, "r", encoding="utf-8") as f:
        existing_places = json.load(f)

    existing_titles = set()
    for p in existing_places:
        existing_titles.add(p["title"].get("by", "").lower())
        existing_titles.add(p["id"].lower())

    # Curated additional border places
    border_places = [
        {
            "id": "suprasl-monastery",
            "title": {
                "by": "Супрасльскі Дабравешчанскі манастыр (Падляшша)",
                "ru": "Супрасльский Благовещенский монастырь (Подляшье)",
                "en": "Supraśl Lavra (Annunciation Monastery, Podlasie)"
            },
            "category": "church",
            "country": { "by": "Польшча", "ru": "Польша", "en": "Poland" },
            "city": { "by": "Супрасль", "ru": "Супрасль", "en": "Supraśl" },
            "coordinates": [53.2086, 23.3375],
            "description": {
                "by": "Адна з галоўных духоўных і асветніцкіх святыняў беларускага Падляшша, заснаваная ў 1498 годзе маршалкам ВКЛ Аляксандрам Хадкевічам. Унікальны абарончы храм у стылі готыкі і рэнесансу. Супрасль быў найбуйнейшым цэнтрам кнігадрукавання і летапісання ВКЛ: тут была створана Супрасльская рукапісь XI ст. (помнік ЮНЕСКА) і Супрасльскі летапіс, а Супрасльская друкарня выдала дзясяткі кірылічных выданняў. Цяпер тут дзейнічае Музей ікон.",
                "ru": "Один из ключевых центров православия и просвещения белорусского Подляшья, основанный в 1498 г. воеводой Александром Ходкевичем. Уникальный оборонный храм готики и ренессанса. Центр книгопечатания и летописания ВКЛ (Супрасльский летопись, Супрасльская рукопись XI в.).",
                "en": "Major spiritual and printing center of Belarusian Podlasie, founded in 1498 by GDL magnate Aleksander Chodkiewicz. Featuring a rare fortified Gothic-Renaissance church, historic Cyrillic printing press, and Museum of Icons."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Monastery_of_the_Annunciation_in_Supra%C5%9Bl_2017.jpg/640px-Monastery_of_the_Annunciation_in_Supra%C5%9Bl_2017.jpg",
            "links": [
                { "title": "Вікіпедыя: Супрасльскі Дабравешчанскі манастыр", "url": "https://be.wikipedia.org/wiki/Супрасльскі_Дабравешчанскі_манастыр" },
                { "title": "Артыкул: Супрасльская друкарня і Хадкевічы", "url": "https://be.wikipedia.org/wiki/Супрасльская_друкарня" },
                { "title": "Музей ікон у Супраслі", "url": "https://muzeum.bialystok.pl/muzeum-ikon-w-supraslu/" }
            ],
            "tags": ["Супрасль", "Падляшша", "Хадкевічы", "Абарончы храм", "Кнігадрук"],
            "items": [
                {
                    "title": "Дабравешчанскі сабор (абарончая готыка)",
                    "author": "Дойліды ВКЛ",
                    "year": "1503–1511",
                    "description": "Унікальны храм абарончага тыпу з чатырма кутнімі вежамі і гатычнымі зорчатымі скляпеннямі, адноўлены вернікамі."
                },
                {
                    "title": "Супрасльская рукапісь (XI ст.) і летапіс",
                    "author": "Манахі-летапісцы",
                    "year": "XI–XVI ст.",
                    "description": "Сусветны помнік стараславянскага пісьменства, уключаны ў рэестр ЮНЕСКА 'Памяць свету'."
                },
                {
                    "title": "Супрасльская друкарня",
                    "author": "Манастырскае брацтва",
                    "year": "1695–1803",
                    "description": "Выдала больш за 80 старадрукаў кірыліцай для ўсяго рэгіёна ВКЛ."
                }
            ]
        },
        {
            "id": "daugavpils-belarusian-gymnasium",
            "title": {
                "by": "Дзвінская беларуская гімназія і дзеячы (Даўгаўпілс)",
                "ru": "Двинская белорусская гимназия (Даугавпилс)",
                "en": "Daugavpils Belarusian Gymnasium (Dvinsk, Latvia)"
            },
            "category": "historical",
            "country": { "by": "Латвія", "ru": "Латвия", "en": "Latvia" },
            "city": { "by": "Даўгаўпілс", "ru": "Даугавпилс", "en": "Daugavpils" },
            "coordinates": [55.8710, 26.5160],
            "description": {
                "by": "Дзвінская дзяржаўная беларуская гімназія дзеяла ў 1922–1938 гадах і стала галоўным адукацыйным і навуковым асяродкам беларускай меншасці ў Латвіі. Яе дырэктарам быў выбітны фалькларыст, этнограф і педагог Сяргей Сахараў (аўтар фундаментальных прац пра беларускую народную творчасць Латгаліі). Сярод выкладчыкаў і выпускнікоў — вядомыя пісьменнікі, навукоўцы і грамадскія дзеячы.",
                "ru": "Двинская государственная белорусская гимназия (1922–1938) — главный центр белорусского просвещения в Латвии. Её директором был учёный-фольклорист Сергей Сахаров. Центр культурной жизни белорусов Латгалии.",
                "en": "The Daugavpils State Belarusian Gymnasium (1922–1938) was the intellectual hub of the Belarusian diaspora in Latvia, directed by prominent folklorist and educator Siarhiej Sacharau."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Daugavpils_Gimnazija_Saharov.jpg/640px-Daugavpils_Gimnazija_Saharov.jpg",
            "links": [
                { "title": "Вікіпедыя: Дзвінская беларуская гімназія", "url": "https://be.wikipedia.org/wiki/Дзвінская_дзяржаўная_беларуская_гімназія" },
                { "title": "Артыкул: Сяргей Сахараў і беларусы Латвіі", "url": "https://be.wikipedia.org/wiki/Сяргей_Пятровіч_Сахараў" }
            ],
            "tags": ["Дзвінск", "Латвія", "Сахараў", "Гімназія", "Адукацыя"]
        },
        {
            "id": "smolensk-ssrb-1919",
            "title": {
                "by": "Месца абвяшчэння ССРБ (БССР) у Смаленску",
                "ru": "Место провозглашения ССРБ (БССР) в Смоленске",
                "en": "Site of Declaration of SSRB (BSSR) in Smolensk"
            },
            "category": "historical",
            "country": { "by": "Расія", "ru": "Россия", "en": "Russia" },
            "city": { "by": "Смаленск", "ru": "Смоленск", "en": "Smolensk" },
            "coordinates": [54.7825, 32.0453],
            "description": {
                "by": "У будынку былога Дваранскага сходу (цяпер Смаленская абласная філармонія на вул. Глінкі, 3) 30–31 снежня 1918 года праходзіла VI Паўночна-Заходняя канферэнцыя РКП(б), а 1 студзеня 1919 года быў абвешчаны Маніфест Часовага рэвалюцыйнага рабоча-сялянскага савецкага ўрада Беларусі аб утварэнні ССРБ (першапачаткова са сталіцай у Смаленску). Гістарычна Смаленшчына на працягу стагоддзяў уваходзіла ў склад Вялікага Княства Літоўскага.",
                "ru": "В здании Дворянского собрания (ныне филармония, ул. Глинки, 3) 1 января 1919 г. был обнародован Манифест об образовании Советской Социалистической Республики Белоруссия (ССРБ) со столицей в Смоленске, до переезда правительства в Минск.",
                "en": "In the former Nobles' Assembly building (now Smolensk Philharmonic), the Manifesto declaring the Soviet Socialist Republic of Belarus (SSRB) was proclaimed on January 1, 1919, with Smolensk as its initial capital."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Smolensk_Philharmonic_Hall.jpg/640px-Smolensk_Philharmonic_Hall.jpg",
            "links": [
                { "title": "Вікіпедыя: ССРБ", "url": "https://be.wikipedia.org/wiki/Сацыялістычная_Савецкая_Рэспубліка_Беларусь" },
                { "title": "Артыкул: Смаленск і беларуская дзяржаўнасць", "url": "https://be.wikipedia.org/wiki/Смаленскае_ваяводства" }
            ],
            "tags": ["Смаленск", "ССРБ", "ВКЛ", "Гісторыя", "1919"]
        }
    ]

    for bp in border_places:
        if bp["id"] not in existing_titles:
            existing_places.append(bp)
            existing_titles.add(bp["id"])

    # Parse KML
    tree = ET.parse(kml_path)
    root = tree.getroot()

    # Handle XML namespace
    ns = {'kml': 'http://www.opengis.net/kml/2.2'}
    placemarks = root.findall('.//kml:Placemark', ns)
    if not placemarks:
        placemarks = root.findall('.//{http://www.opengis.net/kml/2.2}Placemark')

    added_kml_count = 0
    for p in placemarks:
        name_el = p.find('kml:name', ns)
        if name_el is None:
            name_el = p.find('{http://www.opengis.net/kml/2.2}name')
        name = name_el.text.strip() if name_el is not None and name_el.text else ""

        if not name:
            continue

        # Skip duplicates or generic headers
        name_lower = name.lower()
        if any(skip in name_lower for skip in ["вострая брама", "базыльянскі кляштар", "хадкевічаў", "росы", "каліноўск"]):
            # These are already deeply curated in existing_places with richer content
            continue

        desc_el = p.find('kml:description', ns)
        if desc_el is None:
            desc_el = p.find('{http://www.opengis.net/kml/2.2}description')
        desc_raw = desc_el.text if desc_el is not None and desc_el.text else ""
        desc = clean_html(desc_raw)

        coords_el = p.find('.//kml:coordinates', ns)
        if coords_el is None:
            coords_el = p.find('.//{http://www.opengis.net/kml/2.2}coordinates')
        if coords_el is None or not coords_el.text:
            continue

        coords_str = coords_el.text.strip()
        parts = coords_str.split(',')
        if len(parts) < 2:
            continue
        try:
            lng = round(float(parts[0]), 5)
            lat = round(float(parts[1]), 5)
        except ValueError:
            continue

        slug = f"vilnia-{slugify(name)}"
        if slug in existing_titles or name_lower in existing_titles:
            continue

        category = detect_category(name, desc)

        place_obj = {
            "id": slug,
            "title": {
                "by": name,
                "ru": name,
                "en": name
            },
            "category": category,
            "country": {
                "by": "Літва",
                "ru": "Литва",
                "en": "Lithuania"
            },
            "city": {
                "by": "Вільня",
                "ru": "Вильнюс",
                "en": "Vilnius"
            },
            "coordinates": [lat, lng],
            "description": {
                "by": desc if desc else f"Гістарычнае беларускае месца ў Вільні: {name}.",
                "ru": desc if desc else f"Историческое белорусское место в Вильнюсе: {name}.",
                "en": desc if desc else f"Historic Belarusian heritage site in Vilnius: {name}."
            },
            "image": "",
            "links": [
                {
                    "title": "Карта «Беларуская Вільня»",
                    "url": "https://www.google.com/maps/d/viewer?mid=1fohygMcC3bikWPX5K1r288vnOFs"
                }
            ],
            "tags": ["Беларуская Вільня", "Вільня", "Гісторыя", category]
        }

        existing_places.append(place_obj)
        existing_titles.add(slug)
        existing_titles.add(name_lower)
        added_kml_count += 1

    print(f"Total places now: {len(existing_places)} (Added {added_kml_count} from KML)")

    # Save to places.json
    with open(places_json_path, "w", encoding="utf-8") as f:
        json.dump(existing_places, f, ensure_ascii=False, indent=2)

    # Save to places.js
    with open(places_js_path, "w", encoding="utf-8") as f:
        f.write("window.INITIAL_PLACES = ")
        json.dump(existing_places, f, ensure_ascii=False, indent=2)
        f.write(";\n")

    print("Successfully written places.json and places.js in pure UTF-8 without BOM!")

if __name__ == "__main__":
    main()
