import urllib.request, urllib.parse, json

def main():
    title = 'File:Vladas Vildžiūnas "Barbora".png'
    url = f'https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&prop=imageinfo&iiprop=url&iiurlwidth=800&format=json'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as r:
        data = json.loads(r.read())
        pages = data['query']['pages']
        for k, v in pages.items():
            if 'imageinfo' in v:
                print('Thumb URL:', v['imageinfo'][0].get('thumburl') or v['imageinfo'][0].get('url'))

if __name__ == '__main__':
    main()
