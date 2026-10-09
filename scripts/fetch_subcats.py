import urllib.request, urllib.parse, json, time

subcats = [
    'Катэгорыя:Арганізацыі_беларусаў_Францыі',
    'Катэгорыя:Арганізацыі_беларусаў_Канады',
    'Катэгорыя:Арганізацыі_беларусаў_Чэхіі',
    'Катэгорыя:Арганізацыі_беларусаў_Літвы',
    'Катэгорыя:Арганізацыі_беларусаў_Латвіі',
    'Катэгорыя:Арганізацыі_беларусаў_Эстоніі',
    'Катэгорыя:Арганізацыі_беларусаў_Украіны',
    'Катэгорыя:Арганізацыі_беларусаў_Расіі',
    'Катэгорыя:Арганізацыі_беларусаў_Польшчы'
]

with open('scripts/diaspora_subcats_utf8.txt', 'w', encoding='utf-8') as out:
    for sc in subcats:
        time.sleep(1.2)
        url = f'https://be.wikipedia.org/w/api.php?action=query&list=categorymembers&cmtitle={urllib.parse.quote(sc)}&cmlimit=500&format=json'
        req = urllib.request.Request(url, headers={'User-Agent': 'AlbaruthenicaBot/1.0 (contact: info@albaruthenica.org)'})
        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                members = data.get('query', {}).get('categorymembers', [])
                out.write(f'\n--- {sc} ({len(members)}) ---\n')
                for m in members:
                    out.write(f"   * {m['title']}\n")
        except Exception as e:
            out.write(f'Error fetching {sc}: {e}\n')
print("Done fetching subcats.")
