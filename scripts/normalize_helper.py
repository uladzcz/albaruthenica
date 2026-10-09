import json
import re
import os

COUNTRY_MAP = {
    "Czechia": {"by": "Чэхія", "ru": "Чехия", "en": "Czechia"},
    "Italy": {"by": "Італія", "ru": "Италия", "en": "Italy"},
    "Lithuania": {"by": "Літва", "ru": "Литва", "en": "Lithuania"},
    "Літва": {"by": "Літва", "ru": "Литва", "en": "Lithuania"},
    "Russia": {"by": "Расія", "ru": "Россия", "en": "Russia"},
    "France": {"by": "Францыя", "ru": "Франция", "en": "France"},
    "Poland": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
    "Польшча": {"by": "Польшча", "ru": "Польша", "en": "Poland"},
    "Turkey": {"by": "Турцыя", "ru": "Турция", "en": "Turkey"},
    "Ukraine": {"by": "Украіна", "ru": "Украина", "en": "Ukraine"},
    "Украіна": {"by": "Украіна", "ru": "Украина", "en": "Ukraine"},
    "Germany": {"by": "Германія", "ru": "Германия", "en": "Germany"},
    "Нямеччына": {"by": "Германія", "ru": "Германия", "en": "Germany"},
    "United States": {"by": "ЗША", "ru": "США", "en": "United States"},
    "ЗША": {"by": "ЗША", "ru": "США", "en": "United States"},
    "Switzerland": {"by": "Швейцарыя", "ru": "Швейцария", "en": "Switzerland"},
    "Australia": {"by": "Аўстралія", "ru": "Австралия", "en": "Australia"},
    "Chile": {"by": "Чылі", "ru": "Чили", "en": "Chile"},
    "Japan": {"by": "Японія", "ru": "Япония", "en": "Japan"},
    "Данія": {"by": "Данія", "ru": "Дания", "en": "Denmark"},
    "Denmark": {"by": "Данія", "ru": "Дания", "en": "Denmark"},
    "Israel": {"by": "Ізраіль", "ru": "Израиль", "en": "Israel"},
    "Ізраіль": {"by": "Ізраіль", "ru": "Израиль", "en": "Israel"}
}

CITY_MAP = {
    "Prague": {"by": "Прага", "ru": "Прага", "en": "Prague"},
    "Padua": {"by": "Падуя", "ru": "Падуя", "en": "Padua"},
    "Vilnius": {"by": "Вільня", "ru": "Вильнюс", "en": "Vilnius"},
    "Вільня": {"by": "Вільня", "ru": "Вильнюс", "en": "Vilnius"},
    "Kaliningrad": {"by": "Калінінград", "ru": "Калининград", "en": "Kaliningrad"},
    "Paris": {"by": "Парыж", "ru": "Париж", "en": "Paris"},
    "Kraków": {"by": "Кракаў", "ru": "Краков", "en": "Krakow"},
    "Кракаў": {"by": "Кракаў", "ru": "Краков", "en": "Krakow"},
    "Istanbul": {"by": "Стамбул", "ru": "Стамбул", "en": "Istanbul"},
    "Lviv": {"by": "Львоў", "ru": "Львов", "en": "Lviv"},
    "Weimar": {"by": "Ваймар", "ru": "Веймар", "en": "Weimar"},
    "Rome": {"by": "Рым", "ru": "Рим", "en": "Rome"},
    "Washington, D.C.": {"by": "Вашынгтон", "ru": "Вашингтон", "en": "Washington, D.C."},
    "Philadelphia": {"by": "Філадэльфія", "ru": "Филадельфия", "en": "Philadelphia"},
    "West Point, NY": {"by": "Вест-Пойнт", "ru": "Вест-Пойнт", "en": "West Point, NY"},
    "Solothurn": {"by": "Залатурн", "ru": "Золотурн", "en": "Solothurn"},
    "Chicago": {"by": "Чыкага", "ru": "Чикаго", "en": "Chicago"},
    "Kosciuszko National Park": {"by": "Нацыянальны парк Касцюшка", "ru": "Национальный парк Косцюшко", "en": "Kosciuszko National Park"},
    "Santiago": {"by": "Сант'яга", "ru": "Сантьяго", "en": "Santiago"},
    "La Serena": {"by": "Ла-Серэна", "ru": "Ла-Серена", "en": "La Serena"},
    "Honolulu": {"by": "Ганалулу", "ru": "Гонолулу", "en": "Honolulu"},
    "Amakusa": {"by": "Амакуса", "ru": "Амакуса", "en": "Amakusa"},
    "Vevey": {"by": "Вевэ", "ru": "Веве", "en": "Vevey"},
    "Warsaw": {"by": "Варшава", "ru": "Варшава", "en": "Warsaw"},
    "Варшава": {"by": "Варшава", "ru": "Варшава", "en": "Warsaw"},
    "Saint Petersburg": {"by": "Санкт-Пецярбург", "ru": "Санкт-Петербург", "en": "Saint Petersburg"},
    "Берлін": {"by": "Берлін", "ru": "Берлин", "en": "Berlin"},
    "Нябораў": {"by": "Нябораў", "ru": "Неборов", "en": "Nieborów"},
    "Олыка": {"by": "Олыка", "ru": "Олыка", "en": "Olyka"},
    "Шыдловец": {"by": "Шыдловец", "ru": "Шидловец", "en": "Szydłowiec"},
    "Паланга": {"by": "Паланга", "ru": "Паланга", "en": "Palanga"},
    "Крэтынга": {"by": "Крэтынга", "ru": "Кретинга", "en": "Kretinga"},
    "Хоцін": {"by": "Хоцін", "ru": "Хотин", "en": "Khotyn"},
    "Кодэнь": {"by": "Кодэнь", "ru": "Кодень", "en": "Kodeń"},
    "Красічын": {"by": "Красічын", "ru": "Красичин", "en": "Krasiczyn"},
    "Рынгстэд": {"by": "Рынгстэд", "ru": "Рингстед", "en": "Ringsted"},
    "Каўнас": {"by": "Каўнас", "ru": "Каунас", "en": "Kaunas"},
    "Старыя Трокі": {"by": "Старыя Трокі", "ru": "Старые Троки", "en": "Senieji Trakai"},
    "Стэббарк / Грунвальд": {"by": "Стэббарк (Грунвальд)", "ru": "Стембарк (Грюнвальд)", "en": "Stębark (Grunwald)"},
    "Люблін": {"by": "Люблін", "ru": "Люблин", "en": "Lublin"},
    "Масква": {"by": "Масква", "ru": "Москва", "en": "Moscow"},
    "Лос-Анджэлес": {"by": "Лос-Анджэлес", "ru": "Лос-Анджелес", "en": "Los Angeles"},
    "Нью-Ёрк": {"by": "Нью-Ёрк", "ru": "Нью-Йорк", "en": "New York"},
    "Х'юстан": {"by": "Х'юстан", "ru": "Хьюстон", "en": "Houston"},
    "Рэхавот": {"by": "Рэхавот", "ru": "Реховот", "en": "Rehovot"},
    "Тэль-Авіў": {"by": "Тэль-Авіў / Яфа", "ru": "Тель-Авив / Яффа", "en": "Tel Aviv / Jaffa"},
    "Бостан": {"by": "Бостан", "ru": "Бостон", "en": "Boston"}
}

PERSON_ID_NORMALIZE = {
    "skaryna": "francysk-skaryna",
    "mickiewicz": "adam-mickiewicz",
    "kosciuszko": "tadeusz-kosciuszko",
    "domeyko": "ignacy-domeyko",
    "sudzilouski": "nikolai-sudzilovsky",
    "sienkiewicz": "henryk-sienkiewicz",
    "azheshka": "eliza-orzeszkowa",
    "karski": "yafim-karski"
}

def normalize_text_dict(d):
    res = {}
    if "by" in d:
        res["by"] = d["by"]
    elif "be" in d:
        res["by"] = d["be"]
    res["ru"] = d.get("ru", "")
    res["en"] = d.get("en", "")
    return res

def normalize_country(c):
    if isinstance(c, dict):
        return normalize_text_dict(c)
    return COUNTRY_MAP.get(c, {"by": c, "ru": c, "en": c})

def normalize_city(c):
    if isinstance(c, dict):
        return normalize_text_dict(c)
    return CITY_MAP.get(c, {"by": c, "ru": c, "en": c})

def process_item(item, source_tag=""):
    title = normalize_text_dict(item["title"])
    desc = normalize_text_dict(item["description"])
    country = normalize_country(item["country"])
    city = normalize_city(item["city"])
    
    # image
    img = item.get("image") or item.get("imageUrl") or ""
    
    # links
    links = item.get("links", [])
    if not links and item.get("wikipediaUrl"):
        links = [{"title": "Вікіпедыя", "url": item["wikipediaUrl"]}]
        
    # tags
    tags = item.get("tags", [])
    if not tags:
        city_by = city["by"]
        tags = [city_by]
        if source_tag:
            tags.append(source_tag)
            
    # personId
    pid = item.get("personId")
    if pid in PERSON_ID_NORMALIZE:
        pid = PERSON_ID_NORMALIZE[pid]
        
    obj = {
        "id": item["id"],
        "title": title,
        "category": item.get("category", "historical"),
        "country": country,
        "city": city,
        "coordinates": item["coordinates"],
        "description": desc,
        "image": img,
        "links": links,
        "tags": tags,
        "isUnverifiedCoordinates": True
    }
    
    if pid:
        obj["personId"] = pid
    if "personIds" in item:
        obj["personIds"] = item["personIds"]
    if "items" in item:
        obj["items"] = item["items"]
        
    return obj

print("merge_dataset module ready")
