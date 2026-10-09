import urllib.request
import urllib.parse
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Query historical figures born before 1900 in Belarusian territory
sparql_hist = """
SELECT DISTINCT ?person ?personLabel ?personDescription ?birthPlaceLabel ?birthDate ?deathPlaceLabel ?deathCountryLabel ?deathCoord ?sitelinks WHERE {
  ?person wdt:P31 wd:Q5 ;
          wdt:P19 ?birthPlace ;
          wdt:P569 ?birthDate ;
          wdt:P20 ?deathPlace ;
          wikibase:sitelinks ?sitelinks .
  
  FILTER(?birthDate < "1900-01-01"^^xsd:dateTime)
  FILTER(?sitelinks >= 12)
  
  {
    ?birthPlace wdt:P17 wd:Q184 .
  } UNION {
    ?birthPlace wdt:P131* ?gov .
    VALUES ?gov { wd:Q1139414 wd:Q2092288 wd:Q1394592 wd:Q1428587 wd:Q1539242 wd:Q170072 }
  }
  
  ?deathPlace wdt:P625 ?deathCoord .
  
  OPTIONAL { ?deathPlace wdt:P17 ?deathCountry . }
  FILTER(!BOUND(?deathCountry) || ?deathCountry != wd:Q184)
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "be,be-tarask,ru,en". }
}
ORDER BY DESC(?sitelinks)
LIMIT 60
"""

url = "https://query.wikidata.org/sparql?query=" + urllib.parse.quote(sparql_hist) + "&format=json"
headers = {
    'User-Agent': 'AlbaruthenicaBot/1.0 (https://github.com/albaruthenica; albaruthenica@example.org)',
    'Accept': 'application/sparql-results+json'
}

print("Executing Wikidata query for historical figures (pre-1900)...")
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        bindings = data.get('results', {}).get('bindings', [])
        print(f"Retrieved {len(bindings)} historical figures:")
        for b in bindings[:35]:
            p_label = b.get('personLabel', {}).get('value', 'Unknown')
            b_place = b.get('birthPlaceLabel', {}).get('value', 'Unknown')
            d_place = b.get('deathPlaceLabel', {}).get('value', 'Unknown')
            country = b.get('deathCountryLabel', {}).get('value', '')
            coord = b.get('deathCoord', {}).get('value', '')
            sitelinks = b.get('sitelinks', {}).get('value', '')
            desc = b.get('personDescription', {}).get('value', '')
            print(f"  • {p_label} ({desc}) [born: {b_place}, sitelinks: {sitelinks}] -> Died: {d_place} ({country}), Coord: {coord}")
        with open('scripts/wikidata_historical.json', 'w', encoding='utf-8') as f:
            json.dump(bindings, f, ensure_ascii=False, indent=2)
except Exception as e:
    print("Error:", e)
