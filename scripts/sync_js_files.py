import json

with open('data/places.json', 'r', encoding='utf-8') as f:
    places = json.load(f)

with open('data/persons.json', 'r', encoding='utf-8') as f:
    persons = json.load(f)

with open('data/places.js', 'w', encoding='utf-8') as f:
    f.write('window.INITIAL_PLACES = ' + json.dumps(places, ensure_ascii=False, indent=2) + ';\n')

with open('data/persons.js', 'w', encoding='utf-8') as f:
    f.write('window.INITIAL_PERSONS = ' + json.dumps(persons, ensure_ascii=False, indent=2) + ';\n')

print("Fixed places.js and persons.js syntax.")
