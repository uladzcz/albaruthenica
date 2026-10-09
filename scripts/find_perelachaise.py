import urllib.request
import urllib.parse
import json

sparql_query = """
SELECT ?person ?personLabel ?birthPlaceLabel ?birthDate ?deathDate ?desc ?beWiki ?ruWiki ?enWiki WHERE {
  ?person wdt:P119 wd:Q311 .
  {
    ?person wdt:P19 ?birthPlace .
    ?birthPlace wdt:P17 wd:Q184 .
  } UNION {
    ?person wdt:P19 ?birthPlace .
    ?birthPlace wdt:P131* ?region .
    VALUES ?region { wd:Q2007817 wd:Q754020 wd:Q2007811 wd:Q1530960 wd:Q2007813 wd:Q2007815 wd:Q408332 wd:Q408330 wd:Q408328 wd:Q408326 wd:Q408324 wd:Q408322 }
  }
  OPTIONAL { ?person wdt:P569 ?birthDate . }
  OPTIONAL { ?person wdt:P570 ?deathDate . }
  OPTIONAL {
    ?beWiki schema:about ?person ;
            schema:isPartOf <https://be.wikipedia.org/> .
  }
  OPTIONAL {
    ?ruWiki schema:about ?person ;
            schema:isPartOf <https://ru.wikipedia.org/> .
  }
  OPTIONAL {
    ?enWiki schema:about ?person ;
            schema:isPartOf <https://en.wikipedia.org/> .
  }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "be,ru,en,pl,fr". }
}
"""

url = "https://query.wikidata.org/sparql?format=json&query=" + urllib.parse.quote(sparql_query)
req = urllib.request.Request(url, headers={"User-Agent": "AlbaruthenicaBot/1.0 (test@example.com)"})

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        results = data['results']['bindings']
        print(f"Found {len(results)} results:")
        seen = set()
        for r in results:
            pid = r.get('person', {}).get('value', '').split('/')[-1]
            if pid in seen: continue
            seen.add(pid)
            name = r.get('personLabel', {}).get('value')
            bp = r.get('birthPlaceLabel', {}).get('value')
            bdate = r.get('birthDate', {}).get('value', '')[:4]
            ddate = r.get('deathDate', {}).get('value', '')[:4]
            be = r.get('beWiki', {}).get('value', '')
            ru = r.get('ruWiki', {}).get('value', '')
            print(f"- {name} ({bdate}-{ddate}) | Place: {bp} | QID: {pid} | be: {bool(be)} | ru: {bool(ru)}")
except Exception as e:
    print("Error:", e)
