import urllib.request
import urllib.parse
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Query 1: Notable persons born in Belarus or historic Belarusian territories with burial places outside Belarus
sparql_query_burial = """
SELECT DISTINCT ?person ?personLabel ?personDescription ?birthPlace ?birthPlaceLabel ?burialPlace ?burialPlaceLabel ?burialCoord ?burialCountry ?burialCountryLabel ?sitelinks ?image WHERE {
  # Born in Belarus or subdivisions
  ?person wdt:P31 wd:Q5 ;
          wdt:P19 ?birthPlace ;
          wdt:P119 ?burialPlace ;
          wikibase:sitelinks ?sitelinks .
  
  # Filter by significant sitelinks count (filter out non-notables)
  FILTER(?sitelinks >= 20)
  
  # Birthplace in Belarus (Q184) or historical governorates
  {
    ?birthPlace wdt:P17 wd:Q184 .
  } UNION {
    # Minsk, Grodno, Mogilev, Vitebsk, Vilna Governorates
    ?birthPlace wdt:P131* ?gov .
    VALUES ?gov { wd:Q1139414 wd:Q2092288 wd:Q1394592 wd:Q1428587 wd:Q1539242 wd:Q170072 }
  }
  
  # Burial place coordinates
  ?burialPlace wdt:P625 ?burialCoord .
  
  # Burial place NOT in Belarus
  OPTIONAL { ?burialPlace wdt:P17 ?burialCountry . }
  FILTER(!BOUND(?burialCountry) || ?burialCountry != wd:Q184)
  
  OPTIONAL { ?person wdt:P18 ?image . }
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "be,be-tarask,ru,en". }
}
ORDER BY DESC(?sitelinks)
LIMIT 60
"""

url = "https://query.wikidata.org/sparql?query=" + urllib.parse.quote(sparql_query_burial) + "&format=json"
headers = {
    'User-Agent': 'AlbaruthenicaBot/1.0 (https://github.com/albaruthenica; albaruthenica@example.org)',
    'Accept': 'application/sparql-results+json'
}

print("Executing Wikidata query for burial places...")
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        bindings = data.get('results', {}).get('bindings', [])
        print(f"Retrieved {len(bindings)} notable figures with foreign burials:")
        for b in bindings[:25]:
            p_label = b.get('personLabel', {}).get('value', 'Unknown')
            b_place = b.get('birthPlaceLabel', {}).get('value', 'Unknown')
            burial = b.get('burialPlaceLabel', {}).get('value', 'Unknown')
            country = b.get('burialCountryLabel', {}).get('value', '')
            coord = b.get('burialCoord', {}).get('value', '')
            sitelinks = b.get('sitelinks', {}).get('value', '')
            print(f"  • {p_label} (born: {b_place}, sitelinks: {sitelinks}) -> Buried: {burial} ({country}), Coord: {coord}")
        with open('scripts/wikidata_burials.json', 'w', encoding='utf-8') as f:
            json.dump(bindings, f, ensure_ascii=False, indent=2)
except Exception as e:
    print("Error:", e)
