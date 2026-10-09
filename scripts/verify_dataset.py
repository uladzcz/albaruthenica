import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def verify():
    print("--- Verifying Dataset Integrity ---")
    
    # 1. Check data/places.json
    with open('data/places.json', 'r', encoding='utf-8') as f:
        places = json.load(f)
    print(f"Places in data/places.json: {len(places)}")
    
    # 2. Check data/persons.json
    with open('data/persons.json', 'r', encoding='utf-8') as f:
        persons = json.load(f)
    print(f"Persons in data/persons.json: {len(persons)}")
    
    # 3. Check data/places.js
    with open('data/places.js', 'r', encoding='utf-8') as f:
        pjs = f.read()
    assert pjs.startswith('window.PLACES_DATA = [') and pjs.strip().endswith('];')
    print("data/places.js is valid JS syntax structure")
    
    # 4. Check data/persons.js
    with open('data/persons.js', 'r', encoding='utf-8') as f:
        perjs = f.read()
    assert perjs.startswith('window.PERSONS_DATA = [') and perjs.strip().endswith('];')
    print("data/persons.js is valid JS syntax structure")
    
    # Check Places Schema
    place_ids = set()
    unverified_count = 0
    errors = []
    
    for idx, p in enumerate(places):
        pid = p.get('id')
        if not pid:
            errors.append(f"Place at index {idx} has no ID")
        if pid in place_ids:
            errors.append(f"Duplicate place ID: {pid}")
        place_ids.add(pid)
        
        coords = p.get('coordinates')
        if not coords or len(coords) != 2 or not isinstance(coords[0], (int, float)) or not isinstance(coords[1], (int, float)):
            errors.append(f"Invalid coordinates in place {pid}: {coords}")
        else:
            lat, lng = coords
            if not (-90 <= lat <= 90 and -180 <= lng <= 180):
                errors.append(f"Out of range coordinates in {pid}: {coords}")
                
        # Check title
        title = p.get('title')
        if not title or not isinstance(title, dict) or not title.get('by'):
            errors.append(f"Missing or invalid title in place {pid}")
            
        # Check country & city
        country = p.get('country')
        if not country or not isinstance(country, dict) or not country.get('by'):
            errors.append(f"Invalid country in place {pid}: {country}")
            
        city = p.get('city')
        if not city or not isinstance(city, dict) or not city.get('by'):
            errors.append(f"Invalid city in place {pid}: {city}")
            
        if p.get('unverifiedCoordinates') is True:
            unverified_count += 1
            
        # Check image URL format
        img = p.get('image')
        if img and not img.startswith('http'):
            errors.append(f"Local or invalid image URL in place {pid}: {img}")
            
    print(f"Total unverified coordinates count: {unverified_count}")
    
    # Check Persons Schema
    person_ids = set()
    for idx, per in enumerate(persons):
        pid = per.get('id')
        if not pid:
            errors.append(f"Person at index {idx} has no ID")
        if pid in person_ids:
            errors.append(f"Duplicate person ID: {pid}")
        person_ids.add(pid)
        
        if not per.get('name') or not per['name'].get('by'):
            errors.append(f"Missing name in person {pid}")
            
        # Check placeIds existence
        for p_place_id in per.get('placeIds', []):
            if p_place_id not in place_ids:
                errors.append(f"Person {pid} references unknown place ID: {p_place_id}")
                
    # Check Place person references
    for p in places:
        if p.get('personId') and p['personId'] not in person_ids:
            errors.append(f"Place {p['id']} references unknown personId: {p['personId']}")
        for pid in p.get('personIds', []):
            if pid not in person_ids:
                errors.append(f"Place {p['id']} references unknown person in personIds: {pid}")
        if 'items' in p and isinstance(p['items'], list):
            for it in p['items']:
                if it.get('personId') and it['personId'] not in person_ids:
                    errors.append(f"Item {it.get('title')} in place {p['id']} references unknown personId: {it['personId']}")
                    
    if errors:
        print(f"\nFound {len(errors)} validation errors:")
        for e in errors[:20]:
            print(" -", e)
        raise ValueError("Dataset verification failed!")
    else:
        print("\nAll integrity checks passed! Zero errors.")
        
if __name__ == '__main__':
    verify()
