import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

precise_coords = {
    # Tudeley All Saints' Church (OSM: All Saints Church, Crockhurst Street, TN11 0NZ; Wikidata: Q17524671)
    'tudeley-all-saints-chagall-windows': [51.184895, 0.318868],
    
    # Reims Cathedral (Cathédrale Notre-Dame de Reims, OSM Way 23078494)
    'reims-cathedral-chagall-stained-glass': [49.253770, 4.033919],
    
    # Opéra Garnier (Palais Garnier, Paris, OSM Way 24208466)
    'paris-opera-garnier-chagall-ceiling': [48.872029, 2.331785],
    
    # Metz Cathedral (Cathédrale Saint-Étienne de Metz, OSM Way 23067866)
    'metz-cathedral-chagall-stained-glass': [49.120212, 6.175694],
    
    # Hadassah Ein Kerem Synagogue (Chagall Windows Synagogue, Jerusalem)
    'jerusalem-hadassah-chagall-windows': [31.765231, 35.148817],
    
    # Knesset Marc Chagall Hall (Knesset building, Jerusalem)
    'jerusalem-knesset-chagall-hall': [31.776474, 35.205383],
    
    # St. Stephan Mainz (Sankt Stephan, Stefansplatz, Mainz, OSM Way 23157748)
    'mainz-sankt-stephan-chagall-windows': [49.995655, 8.268782],
    
    # Art Institute of Chicago (111 S Michigan Ave, Chicago)
    'chicago-art-institute-chagall-windows': [41.879605, -87.623072],
    
    # Metropolitan Opera House (Lincoln Center, New York)
    'new-york-met-opera-chagall-murals': [40.772871, -73.984792],
    
    # Saint-Paul-de-Vence Cemetery (Cimetière de Saint-Paul-de-Vence, Marc Chagall Grave, Q208260)
    'saint-paul-de-vence-chagall-grave': [43.697222, 7.123056],
    
    # Stedelijk Museum Amsterdam (Museumplein 10, Amsterdam)
    'amsterdam-stedelijk-chagall': [52.357900, 4.879860],
    
    # Kunstmuseum Basel (St. Alban-Graben 16, Basel)
    'basel-kunstmuseum-chagall': [47.553929, 7.594451],
    
    # Fraumünster Zürich (Münsterhof 2, Zürich, OSM Way 27072534)
    'zurich-fraumunster-chagall': [47.369715, 8.541200],
    
    # Musée National Marc Chagall (Avenue Docteur Ménard, Nice, Q1319729)
    'nice-chagall-museum': [43.709340, 7.270030],
    
    # Lytham Hall (Ballam Road, Lytham, Q6710327)
    'lytham-hall-belarusian-timber': [53.744100, -2.976800],
    
    # Kaunas Petrašiūnai Cemetery (Klaudziy Duzh-Dusheuski grave)
    'kaunas-petrasiunai-duzh-dusheuski-grave': [54.888479, 24.010627],
    
    # Kaunas Vytauto pr. 8 (Klaudziy Duzh-Dusheuski residence)
    'kaunas-vytautas-8-duzh-dusheuski-house': [54.891415, 23.924873],
    
    # Warsaw Bulak-Balachowicz Plaque (ul. Paryska 27, Saska Kępa)
    'warsaw-bulak-balachowicz-plaque': [52.229092, 21.057226],
}

with open('data/places.json', 'r', encoding='utf-8') as f:
    places = json.load(f)

updated_count = 0
for p in places:
    pid = p['id']
    if pid in precise_coords:
        p['coordinates'] = precise_coords[pid]
        p.pop('unverifiedCoordinates', None)
        updated_count += 1

print(f"Updated {updated_count} places with verified OSM / Wikidata coordinates.")

with open('data/places.json', 'w', encoding='utf-8') as f:
    json.dump(places, f, ensure_ascii=False, indent=2)

with open('data/places.js', 'w', encoding='utf-8') as f:
    f.write('window.INITIAL_PLACES = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

print("Saved to data/places.json and data/places.js successfully.")
