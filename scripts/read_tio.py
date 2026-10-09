import urllib.request, re, html

req = urllib.request.Request('https://www.tio.by/info/newspaper/6458/', headers={'User-Agent': 'Mozilla/5.0'})
raw = urllib.request.urlopen(req).read().decode('windows-1251', errors='ignore')

# remove scripts and styles
raw = re.sub(r'<script.*?</script>', '', raw, flags=re.DOTALL)
raw = re.sub(r'<style.*?</style>', '', raw, flags=re.DOTALL)

# find paragraphs
clean = html.unescape(re.sub(r'<[^>]+>', '\n', raw))
lines = [l.strip() for l in clean.splitlines() if len(l.strip()) > 30 and 'BYN' not in l and 'ТрэвелСофт' not in l]

print("Found lines:", len(lines))
for l in lines:
    if any(k in l.lower() for k in ['киев', 'короткевич', 'лавр', 'белорус', 'доўнар', 'рынок', 'памятн']):
        print('>', l[:180])
