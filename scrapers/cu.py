import requests
import json
import re
import datetime
from bs4 import BeautifulSoup


session = requests.Session()
url = 'http://cu.bgfretail.com/event/plus.do?category=event&depth2=1&sf=N'
response = session.get(url)

items = list()

for i in range(1, 50):
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    payload = {
        'pageIndex': i,
        'listType': 0,
        'searchCondition': None,
        'user_id': None,
    }

    url = 'http://cu.bgfretail.com/event/plusAjax.do'
    response = session.post(url, data=payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.select('ul > li')

    if len(products) == 0:
        break

    for idx, product in enumerate(products):
        try:
            item = {}

            product_img = product.find('div', class_='photo').find('img')
            product_img_src = product_img['src']
            product_name = product.find('p', class_='prodName').get_text()
            product_price = product.find('p', class_='prodPrice').find('span').get_text()
            product_event = product.find('ul').find('li').get_text()

            item['name'] = product_name
            item['price'] = int(product_price.replace(',', ''))
            item['img'] = product_img_src
            item['event'] = product_event
            item['store'] = 'cu'
            items.append(item)

        except:
            break

data = {}
data['date'] = str(datetime.date.today())
data['items'] = items

with open('../staticfiles/stores/cu.json', 'w') as f:
    json.dump(data, f)

    # print(product_name)
    # print(product_price)
    # print(product_img_src)
    # print(product_event)
