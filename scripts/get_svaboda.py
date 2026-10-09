import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://www.svaboda.org/a/24876672.html"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print("HTML length:", len(html))
        # Look for article body
        m = re.findall(r'<p>(.*?)</p>', html, re.I | re.S)
        print(f"Found {len(m)} paragraphs:")
        full_text = []
        for p in m:
            clean = re.sub(r'<[^>]+>', ' ', p).strip()
            if clean and len(clean) > 20:
                full_text.append(clean)
        text_out = "\n\n".join(full_text)
        print("Text preview:\n", text_out[:1200])
        with open('scripts/svaboda_petersburg.txt', 'w', encoding='utf-8') as f:
            f.write(text_out)
        print("Saved scripts/svaboda_petersburg.txt")
except Exception as e:
    print("Error:", e)
