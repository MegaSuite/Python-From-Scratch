from pathlib import Path
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

import csv


DRIVER_PATH = str(Path('chromedriver').resolve())
BROWSER = webdriver.Chrome(ChromeDriverManager().install())


def write_csv(ads):
    with open('results.csv', 'a',encoding='utf-8-sig') as f:
        fields = ['title', 'link', 'price']

        writer = csv.DictWriter(f, fieldnames=fields)

        for ad in ads:
            writer.writerow(ad)


def get_html(url):
    BROWSER.get(url)
    return BROWSER.page_source


def scrape_data(card):
    try:
        h2 = card.h2
    except:
        title = ''
        link = ''
    else:
        title = h2.text.strip()
        link = h2.a.get('href')

    try:
        price = card.find(
            'span', class_='a-price-whole').text.strip('.').strip()
    except:
        price = ''
    else:
        price = ''.join(price.split('.'))

    data = {'title': title, 'link': link, 'price': price}

    return data



ads_data = []

for i in range(1, 7):

    url = f'https://www.amazon.com/s?k=rapoo+mouse&page={i}&qid=1629080145&ref=sr_pg_2'
    html = get_html(url)

    soup = BeautifulSoup(html, 'lxml')

    cards = soup.find_all(
        'div', {'data-asin': True, 'data-component-type': 's-search-result'})

    for card in cards:
        data = scrape_data(card)
        ads_data.append(data)

write_csv(ads_data)


