import urllib.request
import urllib.parse
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

years = ['2021', '2020', '2019', '2018', '2017', '2016']

for y in years:
    url = f"http://web.archive.org/web/{y}0601000000/http://vkl.by/letter/%D0%91"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            final_url = resp.geturl()
            html = resp.read().decode('utf-8', errors='ignore')
            articles = re.findall(r'<a[^>]+href=["\']([^"\']*/articles/\d+)["\'][^>]*>(.*?)</a>', html, re.I | re.S)
            print(f"Year {y}: final_url={final_url[:60]}... length={len(html)} articles={len(articles)}")
            if len(articles) > 0:
                for href, t in articles[:5]:
                    print("  *", re.sub(r'<[^>]+>', '', t).strip())
                break
    except Exception as e:
        print(f"Year {y} error:", e)
