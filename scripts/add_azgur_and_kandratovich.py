import json

def main():
    with open('data/persons.json', 'r', encoding='utf-8') as f:
        persons = json.load(f)

    with open('data/places.json', 'r', encoding='utf-8') as f:
        places = json.load(f)

    # 1. Add Zair Azgur if not exists
    if not any(p['id'] == 'zair-azgur' for p in persons):
        azgur = {
            "id": "zair-azgur",
            "name": {
                "by": "Заір Азгур",
                "ru": "Заир Азгур",
                "en": "Zair Azgur"
            },
            "role": {
                "by": "Народны мастак Беларусі, выбітны скульптар-манументаліст",
                "ru": "Народный художник Беларуси, выдающийся скульптор-монументалист",
                "en": "People's Artist of Belarus, renowned monumental sculptor"
            },
            "years": "1908–1995",
            "bio": {
                "by": "Адзін з найвыбітнейшых беларускіх скульптараў XX стагоддзя, класік манументальнага мастацтва. Нарадзіўся ў вёсцы Маўчаны Сенненскага раёна. Вучыўся ў Віцебскім мастацкім тэхнікуме, а ў 1928–1929 гг. удасканальваў майстэрства ў Тбіліскай акадэміі мастацтваў у майстэрні Якава Нікаладзэ. Аўтар класічных помнікаў Янку Купалу, Якубу Коласу, Францыску Скарыне, Цётцы і дзясяткаў манументальных партрэтаў.",
                "ru": "Один из крупнейших белорусских скульпторов XX века, классик монументального искусства. Учился в Витебском художественном техникуме, а в 1928–1929 гг. — в Тбилисской государственной академии художеств у Якова Николадзе. Создатель хрестоматийных монументов Янке Купале, Якубу Коласу, Франциску Скорине.",
                "en": "One of the most prominent Belarusian sculptors of the 20th century. Studied at the Vitebsk Art College and in 1928–1929 at the Tbilisi State Academy of Arts under Iakob Nikoladze. Creator of iconic monumental statues of Yanka Kupala, Yakub Kolas, and Francysk Skaryna."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/7/7f/Zair_Azhur._%D0%97%D0%B0%D1%96%D1%80_%D0%90%D0%B7%D0%B3%D1%83%D1%80_%281940%29.jpg",
            "placeIds": [
                "tbilisi-art-academy-azgur"
            ],
            "links": [
                {
                    "title": "Заір Азгур — Вікіпедыя",
                    "url": "https://be.wikipedia.org/wiki/Заір_Ісакавіч_Азгур"
                }
            ]
        }
        persons.append(azgur)
        print("Added zair-azgur")

    # 2. Add Kipryan Kandratovich if not exists
    if not any(p['id'] == 'kipryjan-kandratovich' for p in persons):
        kandratovich = {
            "id": "kipryjan-kandratovich",
            "name": {
                "by": "Кіпрыян Кандратовіч",
                "ru": "Киприан Кондратович",
                "en": "Kipryan Kandratovich"
            },
            "role": {
                "by": "Генерал ад інфантэрыі, галоўнакамандуючы войскаў БНР",
                "ru": "Генерал от инфантерии, главнокомандующий войск БНР",
                "en": "General of the Infantry, Commander-in-Chief of BNR Armed Forces"
            },
            "years": "1859–1932",
            "bio": {
                "by": "Беларускі вайсковы і дзяржаўны дзеяч, генерал ад інфантэрыі. Нарадзіўся ў маёнтку Зіневічы на Лідчыне. Камандаваў 1-м Каўказскім армейскім корпусам (штаб размяшчаўся ў цяперашнім будынку Тбіліскай акадэміі мастацтваў). У 1918 г. увайшоў у склад Рады Беларускай Народнай Рэспублікі, узначаліў Беларускую вайсковую камісію і займаў пасаду міністра народнай абароны (галоўнакамандуючага войскаў) БНР.",
                "ru": "Белорусский военный и государственный деятель, генерал от инфантерии. Уроженец Лидчины. Командовал 1-м Кавказским армейским корпусом со штабом в Тифлисе (ныне Тбилисская академия художеств). В 1918 г. член Рады БНР, министр народной обороны и главнокомандующий войск Белорусской Народной Республики.",
                "en": "Prominent Belarusian military commander and statesman, General of the Infantry. Commanded the 1st Caucasian Army Corps stationed in Tiflis (now Tbilisi Academy of Arts). In 1918, served as Minister of Defense and Commander-in-Chief of the Armed Forces of the Belarusian Democratic Republic (BNR)."
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Kipryjan_Kandratovi%C4%8D._%D0%9A%D1%96%D0%BF%D1%80%D1%8B%D1%8F%D0%BD_%D0%9A%D0%B0%D0%BD%D0%B4%D1%80%D0%B0%D1%82%D0%BE%D0%B2%D1%96%D1%87_%281905%29.jpg/500px-Kipryjan_Kandratovi%C4%8D._%D0%9A%D1%96%D0%BF%D1%80%D1%8B%D1%8F%D0%BD_%D0%9A%D0%B0%D0%BD%D0%B4%D1%80%D0%B0%D1%82%D0%BE%D0%B2%D1%96%D1%87_%281905%29.jpg",
            "placeIds": [
                "tbilisi-art-academy-azgur"
            ],
            "links": [
                {
                    "title": "Кіпрыян Кандратовіч — Вікіпедыя",
                    "url": "https://be.wikipedia.org/wiki/Кіпрыян_Антонавіч_Кандратовіч"
                }
            ]
        }
        persons.append(kandratovich)
        print("Added kipryjan-kandratovich")

    # 3. Update tbilisi-art-academy-azgur in places
    for p in places:
        if p['id'] == 'tbilisi-art-academy-azgur':
            p['image'] = "https://upload.wikimedia.org/wikipedia/commons/b/bc/Tbilisi_Art_Acdemy_photo_from_archive.jpg"
            p['personIds'] = ["zair-azgur", "kipryjan-kandratovich"]
            print("Updated tbilisi-art-academy-azgur with image and personIds")
            break

    # Save persons.json and places.json
    with open('data/persons.json', 'w', encoding='utf-8') as f:
        json.dump(persons, f, ensure_ascii=False, indent=2)

    with open('data/places.json', 'w', encoding='utf-8') as f:
        json.dump(places, f, ensure_ascii=False, indent=2)

    # Sync places.js and persons.js
    with open('data/places.js', 'w', encoding='utf-8') as f:
        f.write('window.INITIAL_PLACES = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

    with open('data/persons.js', 'w', encoding='utf-8') as f:
        f.write('window.INITIAL_PERSONS = ' + json.dumps(persons, ensure_ascii=False, indent=2) + ';\n')

    print("Sync complete. Total places:", len(places), "Total persons:", len(persons))

if __name__ == '__main__':
    main()
