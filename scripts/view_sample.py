import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/vkl_sample_articles.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
for letter, arts in data.items():
    titles = [a['title'] for a in arts]
    print(f"=== {letter} ({len(arts)}) ===")
    print(", ".join(titles[:6]))
