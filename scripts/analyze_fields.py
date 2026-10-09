import json
import re
import sys

# Set stdout to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/msg1.txt', 'r', encoding='utf-8') as f:
    t1 = f.read()
m1 = re.search(r'```(?:json)?\s*(\[\s*\{.*\}\s*\])\s*```', t1, re.DOTALL)
data1 = json.loads(m1.group(1)) if m1 else json.loads(t1.strip())

with open('scratch/msg2.txt', 'r', encoding='utf-8') as f:
    t2 = f.read()
data2 = json.loads(t2.strip()).get('historicalSites', [])

with open('scratch/msg3.txt', 'r', encoding='utf-8') as f:
    t3 = f.read()
m3 = re.search(r'```json\s*(\[\s*\{.*\}\s*\])\s*```', t3, re.DOTALL)
data3 = json.loads(m3.group(1))

print(f"Data 1 keys: {list(data1[0].keys())}")
print(f"Data 2 keys: {list(data2[0].keys())}")
print(f"Data 3 keys: {list(data3[0].keys())}")

# Check country and city formats
print("\nData 1 country/city types:", type(data1[0]['country']), type(data1[0]['city']), data1[0]['country'], data1[0]['city'])
print("Data 2 country/city types:", type(data2[0]['country']), type(data2[0]['city']), data2[0]['country'], data2[0]['city'])
print("Data 3 country/city types:", type(data3[0]['country']), type(data3[0]['city']), data3[0]['country'], data3[0]['city'])

# Check title formats
print("\nData 1 title keys:", list(data1[0]['title'].keys()))
print("Data 2 title keys:", list(data2[0]['title'].keys()))
print("Data 3 title keys:", list(data3[0]['title'].keys()))

# Check links/images formats
print("\nData 1 img/wiki keys:", [k for k in data1[0].keys() if 'image' in k.lower() or 'url' in k.lower() or 'wiki' in k.lower() or 'link' in k.lower()])
print("Data 2 img/wiki keys:", [k for k in data2[0].keys() if 'image' in k.lower() or 'url' in k.lower() or 'wiki' in k.lower() or 'link' in k.lower()])
print("Data 3 img/wiki keys:", [k for k in data3[0].keys() if 'image' in k.lower() or 'url' in k.lower() or 'wiki' in k.lower() or 'link' in k.lower()])
