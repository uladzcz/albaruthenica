import urllib.request
import re
import html

urls = [
    'https://media.catholic.by/nv/n19/art10.htm',
    'https://media.catholic.by/nv/n20/art5.htm',
    'https://media.catholic.by/nv/n21/art11.htm'
]

for u in urls:
    req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
    raw = urllib.request.urlopen(req).read()
    # Check charset
    m_charset = re.search(rb'charset=([^\">\s]+)', raw)
    detected_charset = m_charset.group(1).decode('ascii', errors='ignore') if m_charset else 'windows-1251'
    print(f"=== {u} (declared charset: {detected_charset}) ===")
    
    # Try encodings
    for enc in [detected_charset, 'windows-1251', 'iso-8859-5', 'cp1251']:
        try:
            txt = raw.decode(enc)
            # Find author and title
            # strip tags
            clean = re.sub(r'<script.*?</script>', '', txt, flags=re.DOTALL)
            clean = re.sub(r'<style.*?</style>', '', clean, flags=re.DOTALL)
            lines = [html.unescape(re.sub(r'<[^>]+>', ' ', l)).strip() for l in clean.splitlines()]
            meaningful = [l for l in lines if len(l) > 15 and not l.startswith('DetectBrowser') and not l.startswith('CATHOLIC.BY')]
            if len(meaningful) > 3:
                print(f"Decoded with {enc}:")
                for l in meaningful[:10]:
                    print("  >", l[:120])
                break
        except Exception as e:
            pass
