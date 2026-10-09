import json
import re

# 1. Parse msg1
with open('scratch/msg1.txt', 'r', encoding='utf-8') as f:
    t1 = f.read()

# msg1 is JSON wrapped in ```json ... ```
m1 = re.search(r'```(?:json)?\s*(\[\s*\{.*\}\s*\])\s*```', t1, re.DOTALL)
if m1:
    data1 = json.loads(m1.group(1))
else:
    # try direct json
    data1 = json.loads(t1.strip())
print(f"msg1 parsed: {len(data1)} items")

# 2. Parse msg2
with open('scratch/msg2.txt', 'r', encoding='utf-8') as f:
    t2 = f.read()
# msg2 is raw json object {"historicalSites": [...]}
try:
    obj2 = json.loads(t2.strip())
    data2 = obj2.get('historicalSites', [])
except Exception as e:
    m2 = re.search(r'\{\s*"historicalSites":\s*(\[\s*\{.*\}\s*\])\s*\}', t2, re.DOTALL)
    if m2:
        data2 = json.loads(m2.group(1))
    else:
        print("Failed parsing msg2:", e)
        data2 = []
print(f"msg2 parsed: {len(data2)} items")

# 3. Parse msg3
with open('scratch/msg3.txt', 'r', encoding='utf-8') as f:
    t3 = f.read()
# msg3 contains text and ```json ... ```
m3 = re.search(r'```json\s*(\[\s*\{.*\}\s*\])\s*```', t3, re.DOTALL)
if m3:
    data3 = json.loads(m3.group(1))
else:
    print("Failed parsing msg3")
    data3 = []
print(f"msg3 parsed: {len(data3)} items")

print("\n--- SAMPLE ITEM 1 ---")
if data1:
    print(json.dumps(data1[0], ensure_ascii=False, indent=2))
print("\n--- SAMPLE ITEM 2 ---")
if data2:
    print(json.dumps(data2[0], ensure_ascii=False, indent=2))
print("\n--- SAMPLE ITEM 3 ---")
if data3:
    print(json.dumps(data3[0], ensure_ascii=False, indent=2))
