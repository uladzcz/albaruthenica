import urllib.request
import urllib.parse
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Query: Education institutions outside Belarus for persons born in Belarus/Vilna region
sparql_edu = """
SELECT DISTINCT ?person ?personLabel ?birthPlaceLabel ?institution ?institutionLabel ?instCoord ?instCountryLabel ?sitelinks WHERE {
  ?person wdt:P31 wd:Q5 ;
          wdt:P19 ?birthPlace ;
          wdt:P69 ?institution ;
          wikibase:sitelinks ?sitelinks .
  
  FILTER(?sitelinks >= 25)
  
  {
    ?birthPlace wdt:P17 wd:Q184 .
  } UNION {
    ?birthPlace wdt:P131* ?gov .
    VALUES ?gov { wd:Q1139414 wd:Q2092288 wd:Q1394592 wd:Q1428587 wd:Q1539242 wd:Q170072 }
  }
  
  # Institution coordinates
  ?institution wdt:P625 ?instCoord .
  
  # Institution NOT in Belarus
  OPTIONAL { ?institution wdt:P17 ?instCountry . }
  FILTER(!BOUND(?instCountry) || ?instCountry != wd:Q184)
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "be,be-tarask,ru,en". }
}
ORDER BY DESC(?sitelinks)
LIMIT 50
"""

url = "https://query.wikidata.org/sparql?query=" + urllib.parse.quote(sparql_edu) + "&format=json"
headers = {
    'User-Agent': 'AlbaruthenicaBot/1.0 (https://github.com/albaruthenica; albaruthenica@example.org)',
    'Accept': 'application/sparql-results+json'
}

print("Executing Wikidata query for education institutions...")
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        bindings = data.get('results', {}).get('bindings', [])
        print(f"Retrieved {len(bindings)} education institutions:")
        for b in bindings[:25]:
            p_label = b.get('personLabel', {}).get('value', 'Unknown')
            b_place = b.get('birthPlaceLabel', {}).get('value', 'Unknown')
            inst = b.get('institutionLabel', {}).get('value', 'Unknown')
            country = b.get('instCountryLabel', {}).get('value', '')
            coord = b.get('instCoord', {}).get('value', '')
            sitelinks = b.get('sitelinks', {}).get('value', '')
            print(f"  • {p_label} (born: {b_place}, sitelinks: {sitelinks}) -> Studied at: {inst} ({country}), Coord: {coord}")
        with open('scripts/wikidata_education.json', 'w', encoding='utf-8') as f:
            json.dump(bindings, f, ensure_ascii=False, indent=2)
except Exception as e:
    print("Error:", e)
