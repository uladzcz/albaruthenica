import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/persons.json', 'r', encoding='utf-8') as f:
    persons = json.load(f)

for p in persons:
    if 'radziwill' in p['id'] or 'radzivill' in p['id']:
        print(f"ID: {p['id']}, Name: {p['name']['by']}")
