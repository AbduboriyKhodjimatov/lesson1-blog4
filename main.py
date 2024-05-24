import requests
from bs4 import BeautifulSoup

url = 'https://upl.uz'  # с конца убрать одну \, так как на сайтах уже будет иметься этот \
# чтобы открыть код на сайте нужно нажать F12
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

# find(tag, filters) - находит первый совпадающий объект
wrapper = soup.find('div', class_='main-story')

articles = wrapper.find_all('div', class_='short-story')


result = []
for article in articles:
    h2 = article.find('h2')
    title = h2.get_text(strip=True)
    print(title)
    link = h2.find('a')['href']
    print(link)
    img_link = url + article.find('img')['data-src']
    print(img_link)
    time_div = article.find('div', class_= 'sh-dat').get_text(strip=True)
    desc = article.find('div', class_= 'sh-pan').next.get_text(strip=True)
    print(desc)
    comments = article.find('span', class_='icom')
    if comments is not None:
        comments_count = comments.get_text(strip=True)
    else:
        comments_count = 0

    result.append({
        'title': title,
        'link': link,
        'description': desc,
        'time': time_div,
        'comments_count': img_link
    })

import json

with open('tt.json', mode='w', encoding='utf-8') as file:
    json.dump(result, file, indent = 4, ensure_ascii=False)