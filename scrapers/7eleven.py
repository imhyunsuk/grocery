import requests
import json
from bs4 import BeautifulSoup
import datetime


session = requests.Session()
url = 'http://www.7-eleven.co.kr/product/presentList.asp'
response = session.get(url)

items = list()
data = {}
data['date'] = str(datetime.date.today())


for i in range(1, 10):

    payload = {
        'intPageSize': 100,
        'intCurrPage': i,
        'cateCd1': None,
        'cateCd2': None,
        'cateCd3': None,
        'pTab': 1
    }


    url = 'http://www.7-eleven.co.kr/product/listMoreAjax.asp'
    response = session.post(url, data=payload)
    response.encoding='utf-8'

    soup = BeautifulSoup(response.text, 'html.parser')

    products = soup.select('div > div.pic_product')

    if len(products) == 0:
        break

    for product in products:
        item = {}

        product_name = product.find('div', class_='name').get_text()  # 상품 이름
        product_price = product.find('div', class_='price').get_text().strip()  # 가격
        product_img_src = product.find('img').get('src')

        item['name'] = product_name
        item['price'] = int(product_price.replace(',', ''))
        item['img'] = 'http://www.7-eleven.co.kr' + product_img_src
        item['event'] = '1+1'
        item['store'] = '7eleven'
        items.append(item)



for i in range(1, 10):

    payload = {
        'intPageSize': 100,
        'intCurrPage': i,
        'cateCd1': None,
        'cateCd2': None,
        'cateCd3': None,
        'pTab': 2
    }


    url = 'http://www.7-eleven.co.kr/product/listMoreAjax.asp'
    response = session.post(url, data=payload)
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, 'html.parser')

    products = soup.select('div > div.pic_product')

    if len(products) == 0:
        break

    for product in products:
        item = {}

        product_name = product.find('div', class_='name').get_text()  # 상품 이름
        product_price = product.find('div', class_='price').get_text().strip()  # 가격
        product_img_src = product.find('img').get('src')

        item['name'] = product_name
        item['price'] = int(product_price.replace(',', ''))
        item['img'] = 'http://www.7-eleven.co.kr' + product_img_src
        item['event'] = '2+1'
        item['store'] = '7eleven'
        items.append(item)


data['items'] = items

with open('../staticfiles/stores/7eleven.json', 'w') as f:
    json.dump(data, f)
