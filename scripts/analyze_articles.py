import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

for f in sorted(os.listdir('scripts/extracted_articles')):
    if not f.endswith('.txt'): continue
    path = os.path.join('scripts/extracted_articles', f)
    with open(path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if line.strip()]
    print('==============================')
    print(f'FILE: {f} (total lines: {len(lines)})')
    print('TITLE:', lines[1] if len(lines) > 1 else '')
    # Print lines that look like headings or numbers or locations
    headings = []
    for line in lines[2:]:
        if len(line) < 80 and (
            re.match(r'^\d+[\.\)]', line) or
            'Вул' in line or 'вул' in line or 'ul.' in line or 'Ul.' in line or
            'Палац' in line or 'Касцёл' in line or 'Помнік' in line or 'Музей' in line or
            'Дошка' in line or 'Царква' in line or 'Магіла' in line or 'Парк' in line or
            'Плошча' in line or 'Пляц' in line
        ):
            headings.append(line)
    print('POTENTIAL HEADINGS / LOCATIONS:', len(headings))
    for h in headings[:25]:
        print('  -', h)
