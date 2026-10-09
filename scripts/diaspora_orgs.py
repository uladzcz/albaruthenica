import urllib.request, urllib.parse, json

def get_cat_members(cat_title, depth=1):
    url = f"https://be.wikipedia.org/w/api.php?action=query&list=categorymembers&cmtitle={urllib.parse.quote(cat_title)}&cmlimit=500&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'AlbaruthenicaBot/1.0'})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            members = data.get('query', {}).get('categorymembers', [])
            return members
    except Exception as e:
        print(f"Error fetching {cat_title}: {e}")
        return []

root_cat = "Катэгорыя:Арганізацыі_беларускай_дыяспары"
members = get_cat_members(root_cat)

with open("scripts/diaspora_orgs_utf8.txt", "w", encoding="utf-8") as out:
    out.write(f"=== Members of {root_cat} ===\n")
    subcats = []
    pages = []
    for m in members:
        title = m['title']
        if title.startswith("Катэгорыя:"):
            subcats.append(title)
        else:
            pages.append(title)

    out.write("\nPages in root:\n")
    for p in pages:
        out.write(f" - {p}\n")

    out.write(f"\nSubcategories ({len(subcats)}):\n")
    for sc in subcats:
        out.write(f"\n--- {sc} ---\n")
        sub_members = get_cat_members(sc)
        for sm in sub_members:
            out.write(f"   * {sm['title']}\n")

