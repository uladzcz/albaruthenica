import sys
import urllib.request
import re
import html

sys.stdout.reconfigure(encoding='utf-8')

urls = [
    'https://m.vk.com/wall-164603650_1269',
    'https://www.google.com/searchviewer/10?svid=CAwSGRIXCgNwdnESEENnb3ZiUzh3Y0dJNGFHUXkYCg',
    'https://knihi-online.com/hto-josc-hto-siarod-bielarusau-svietu-astka-1.html?page=3'
]

for url in urls:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            print(f'=== URL: {url} ===')
            # Extract title and text
            title = re.search(r'<title>(.*?)</title>', content, re.DOTALL | re.IGNORECASE)
            if title:
                print('TITLE:', title.group(1).strip())
            # extract text
            body_text = re.sub(r'<script.*?</script>', '', content, flags=re.DOTALL)
            body_text = re.sub(r'<style.*?</style>', '', body_text, flags=re.DOTALL)
            body_text = re.sub(r'<[^>]+>', ' ', body_text)
            body_text = html.unescape(body_text)
            words = ' '.join(body_text.split())
            print('TEXT SAMPLE:', words[:500])
            print('---')
    except Exception as e:
        print(f'=== URL: {url} ERROR: {e} ===')
