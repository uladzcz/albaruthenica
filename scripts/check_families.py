import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/persons.json', 'r', encoding='utf-8') as f:
    persons = json.load(f)

for p in persons:
    name_by = p['name']['by']
    if 'род' in name_by.lower() or 'дынастыя' in name_by.lower() or p['id'] in ['radziwills', 'sapehas', 'tyszkiewiczy']:
        print(f"ID: {p['id']}, Name: {name_by}")
