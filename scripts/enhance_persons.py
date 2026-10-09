import json
import urllib.request
import urllib.parse
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Function to fetch accurate image and summary from Wikipedia
def get_wiki_data(wiki_url):
    m = re.search(r'https?://([a-z]+)\.wikipedia\.org/wiki/(.+)', wiki_url)
    if not m:
        return None, None
    lang = m.group(1)
    title = m.group(2)
    api_url = f"https://{lang}.wikipedia.org/api/rest_v1/page/summary/{title}"
    req = urllib.request.Request(api_url, headers={'User-Agent': 'AlbaruthenicaBot/1.0 (https://github.com/uladzcz/albaruthenica; contact@example.com)'})
    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            img = None
            if 'thumbnail' in data:
                img = data['thumbnail']['source']
            elif 'originalimage' in data:
                img = data['originalimage']['source']
            extract = data.get('extract')
            return img, extract
    except Exception as e:
        print(f"Error fetching {wiki_url}: {e}")
        return None, None

print("Testing get_wiki_data helper...")
test_img, test_ext = get_wiki_data("https://be.wikipedia.org/wiki/Генрык_Сянкевіч")
print("Sienkiewicz image:", test_img)
