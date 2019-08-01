import requests
import json
from bs4 import BeautifulSoup
import datetime


session = requests.Session()
url = 'https://www.emart24.co.kr/product/eventProduct.asp'
response = session.get(url)

items = list()
data = {}
data['date'] = str(datetime.date.today())


for i in range(1, 50):

    payload = {
        'productCategory': '1n1',
        'cpage': i
    }


    url = 'https://www.emart24.co.kr/product/eventProduct.asp'
    response = session.post(url, data=payload)

    soup = BeautifulSoup(response.text, 'html.parser')

    products = soup.find('ul', class_='categoryListNew').find_all('li')

    if products[0]['class'][0] == 'nodata':
        break

    for product in products:
        item = {}

        product_name = product.find('p', class_='productDiv').get_text()  # 상품 이름
        product_price = product.find('p', class_='price').get_text().strip()  # 가격
        product_img_src = product.find('p', class_='productImg').find('img').get('src')

        item['name'] = product_name
        item['price'] = int(product_price.replace(',', '').replace('&nbsp;', '').replace('원', ''))
        item['img'] = 'https://www.emart24.co.kr' + product_img_src
        item['event'] = '1+1'
        item['store'] = 'emart24'
        items.append(item)


for i in range(1, 50):

    payload = {
        'productCategory': '2n1',
        'cpage': i
    }

    url = 'https://www.emart24.co.kr/product/eventProduct.asp'
    response = session.post(url, data=payload)

    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.find('ul', class_='categoryListNew').find_all('li')

    if products[0]['class'][0] == 'nodata':
        break

    for product in products:
        item = {}

        product_name = product.find('p', class_='productDiv').get_text()  # 상품 이름
        product_price = product.find('p', class_='price').get_text().strip()  # 가격
        product_img_src = product.find('p', class_='productImg').find('img').get('src')

        item['name'] = product_name
        item['price'] = int(product_price.replace(',', '').replace('&nbsp;', '').replace('원', ''))
        item['img'] = 'https://www.emart24.co.kr' + product_img_src
        item['event'] = '2+1'
        item['store'] = 'emart24'
        items.append(item)

data['items'] = items


with open('emart24.json', 'w') as f:
    json.dump(data, f)
