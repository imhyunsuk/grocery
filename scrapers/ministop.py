import requests
import json
from bs4 import BeautifulSoup
import datetime
import time


session = requests.Session()
url = 'https://www.ministop.co.kr/'
response = session.get(url)

items = list()
data = {}
data['date'] = str(datetime.date.today())

# Get 1+1 items
for i in range(1, 200):
    timestamp = time.mktime(datetime.datetime.now().timetuple())

    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    payload = {
        'pageId': 'event/plus1',
        'sqlnum': 1,
        'paramInfo': '1::',
        'pageNum': i,
        'sortGu': None,
        'tm': timestamp
    }

    url = 'https://www.ministop.co.kr/MiniStopHomePage/page/querySimple.do'
    response = session.post(url, data=payload, timeout=3)

    results = response.json()
    products = results['recordList']

    if len(products) == 0:
        break

    for product in products:
        item = {}

        product_name = product['fields'][0]
        product_price = product['fields'][1]
        product_img_src = product['fields'][4]

        item['name'] = product_name
        item['price'] = int(product_price.replace(',', ''))
        item['img'] = 'https://www.ministop.co.kr/MiniStopHomePage/page/pic.do?n=event1plus1.' + product_img_src
        item['event'] = '1+1'
        item['store'] = 'ministop'
        items.append(item)


# Get 2+1 items
for i in range(1, 200):
    timestamp = time.mktime(datetime.datetime.now().timetuple())

    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    payload = {
        'pageId': 'event/plus2',
        'sqlnum': 1,
        'paramInfo': '2::',
        'pageNum': i,
        'sortGu': None,
        'tm': timestamp
    }

    url = 'https://www.ministop.co.kr/MiniStopHomePage/page/querySimple.do'
    response = session.post(url, data=payload, timeout=3)

    results = response.json()
    products = results['recordList']

    if len(products) == 0:
        break

    for product in products:
        item = {}

        product_name = product['fields'][0]
        product_price = product['fields'][1]
        product_img_src = product['fields'][4]

        item['name'] = product_name
        item['price'] = int(product_price.replace(',', ''))
        item['img'] = 'https://www.ministop.co.kr/MiniStopHomePage/page/pic.do?n=event2plus1.' + product_img_src
        item['event'] = '2+1'
        item['store'] = 'ministop'
        items.append(item)


data['items'] = items

with open('../staticfiles/stores/ministop.json', 'w') as f:
    json.dump(data, f)
