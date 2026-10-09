import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/vkl_letter_b_2021.html', 'r', encoding='utf-8') as f:
    text = f.read()

# look for page navigation links
page_links = re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(\d+|наступная|папярэдняя|&gt;|&raquo;)</a>', text, re.I)
print("Page navigation links:", page_links)

# look for the container of articles
m = re.search(r'(<ul[^>]*class=["\']articles["\'][^>]*>.*?</ul>)', text, re.I | re.S)
if m:
    print("Found articles ul")
else:
    # search where 'Базельскі сабор' appears
    idx = text.find('Базельскі сабор')
    if idx != -1:
        print("Context around Базельскі сабор:")
        print(text[idx-200:idx+400])
