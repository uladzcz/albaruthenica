# -*- coding: utf-8 -*-
"""
Comprehensive database update:
1. Fix getWikimediaThumb in js/app.js to avoid breaking non-Commons wikimedia URLs.
2. Add 'embassy' category to CATEGORY_CONFIG and renderCategoryPills in js/app.js.
3. Add 'embassy' translations in js/i18n.js.
4. Add styling for .category-embassy in css/style.css.
5. Add embassy option in index.html and bump version.
6. Add new persons and places to data/persons.json and data/places.json, sync to .js files.
"""

import json
import re

def update_app_js():
    with open('js/app.js', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update CATEGORY_CONFIG to add embassy
    if 'embassy:' not in content:
        cat_anchor = "grave: {\n    color: '#475569',\n    icon: `<svg viewBox=\"0 0 24 24\" width=\"14\" height=\"14\" fill=\"currentColor\"><path d=\"M12 2C8.69 2 6 4.69 6 8v12h12V8c0-3.31-2.69-6-6-6zm0 4c.55 0 1 .45 1 1v1h1c.55 0 1 .45 1 1s-.45 1-1 1h-1v4c0 .55-.45 1-1 1s-1-.45-1-1v-4H9c-.55 0-1-.45-1-1s.45-1 1-1h1V7c0-.55.45-1 1-1zm-8 16h16v2H4v-2z\"/></svg>`\n  }"
        embassy_code = """grave: {
    color: '#475569',
    icon: `<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M12 2C8.69 2 6 4.69 6 8v12h12V8c0-3.31-2.69-6-6-6zm0 4c.55 0 1 .45 1 1v1h1c.55 0 1 .45 1 1s-.45 1-1 1h-1v4c0 .55-.45 1-1 1s-1-.45-1-1v-4H9c-.55 0-1-.45-1-1s.45-1 1-1h1V7c0-.55.45-1 1-1zm-8 16h16v2H4v-2z"/></svg>`
  },
  embassy: {
    color: '#0284c7',
    icon: `<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M12 2l4 2.5-4 2.5V2zm-9 6h18v2H3V8zm2 3h2v7H5v-7zm5 0h2v7h-2v-7zm5 0h2v7h-2v-7zm5 0h2v7h-2v-7zM2 19h20v3H2v-3z"/></svg>`
  }"""
        content = content.replace(cat_anchor, embassy_code)

    # 2. Update getWikimediaThumb to ONLY process Commons URLs
    old_thumb_code = """function getWikimediaThumb(url, width = 250) {
  if (!url || typeof url !== 'string') return url;
  if (!url.includes('wikimedia.org')) return url;"""

    new_thumb_code = """function getWikimediaThumb(url, width = 250) {
  if (!url || typeof url !== 'string') return url;
  if (!url.includes('wikimedia.org')) return url;
  // ONLY rewrite commons.wikimedia.org URLs! Local language wikipedias (like be.wikipedia.org) do not support thumb endpoints in this manner
  if (!url.includes('/wikipedia/commons/')) {
    return url;
  }"""
    if '// ONLY rewrite commons.wikimedia.org' not in content:
        content = content.replace(old_thumb_code, new_thumb_code)

    # 3. Update renderCategoryPills to include embassy
    old_cat_pills = """    const categories = [
      { id: 'city', label: dict.categories.city || 'Гарады' },
      { id: 'monument', label: dict.categories.monument },
      { id: 'grave', label: dict.categories.grave },
      { id: 'church', label: dict.categories.church },
      { id: 'culture', label: dict.categories.culture },
      { id: 'historical', label: dict.categories.historical },
      { id: 'plaque', label: dict.categories.plaque }
    ];"""

    new_cat_pills = """    const categories = [
      { id: 'city', label: dict.categories.city || 'Гарады' },
      { id: 'monument', label: dict.categories.monument },
      { id: 'grave', label: dict.categories.grave },
      { id: 'church', label: dict.categories.church },
      { id: 'culture', label: dict.categories.culture },
      { id: 'historical', label: dict.categories.historical },
      { id: 'plaque', label: dict.categories.plaque },
      { id: 'embassy', label: dict.categories.embassy || 'Дыпламатычныя місіі' }
    ];"""
    if "id: 'embassy'" not in content:
        content = content.replace(old_cat_pills, new_cat_pills)

    with open('js/app.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated js/app.js")

def update_i18n_js():
    with open('js/i18n.js', 'r', encoding='utf-8') as f:
        content = f.read()

    # BY
    if 'embassy: "Дыпламатычныя місіі"' not in content:
        content = content.replace(
            'plaque: "Мемарыяльныя дошкі"\n    },',
            'plaque: "Мемарыяльныя дошкі",\n      embassy: "Дыпламатычныя місіі"\n    },'
        )

    # RU
    if 'embassy: "Дипломатические миссии"' not in content:
        content = content.replace(
            'plaque: "Мемориальные доски"\n    },',
            'plaque: "Мемориальные доски",\n      embassy: "Дипломатические миссии"\n    },'
        )

    # EN
    if 'embassy: "Diplomatic Missions"' not in content:
        content = content.replace(
            'plaque: "Memorial Plaques"\n    },',
            'plaque: "Memorial Plaques",\n      embassy: "Diplomatic Missions"\n    },'
        )

    with open('js/i18n.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated js/i18n.js")

def update_style_css():
    with open('css/style.css', 'r', encoding='utf-8') as f:
        content = f.read()

    # CSS root variable
    if '--cat-embassy:' not in content:
        content = content.replace(
            '--cat-grave: #475569;     /* Slate Memorial Graphite */\n}',
            '--cat-grave: #475569;     /* Slate Memorial Graphite */\n  --cat-embassy: #0284c7;   /* Diplomatic Cobalt Blue */\n}'
        )

    # Active pill style
    if '.category-pill.active.category-embassy' not in content:
        embassy_pill_css = """
.category-pill.active.category-embassy {
  background: #f0f9ff;
  border-color: var(--cat-embassy, #0284c7);
  color: #0369a1;
}"""
        content = content.replace(
            '.category-pill.active.category-grave {',
            embassy_pill_css + '\n\n.category-pill.active.category-grave {'
        )

    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated css/style.css")

def update_index_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    if '<option value="embassy">' not in content:
        content = content.replace(
            '<option value="plaque">Мемарыяльная дошка</option>',
            '<option value="plaque">Мемарыяльная дошка</option>\n              <option value="embassy">Дыпламатычная місія / Пасольства</option>'
        )

    # Bump cache buster
    content = re.sub(r'v=\d{8}_\d+', 'v=20261009_10', content)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated index.html")

if __name__ == '__main__':
    update_app_js()
    update_i18n_js()
    update_style_css()
    update_index_html()
