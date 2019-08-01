import requests
import json
import datetime
from bs4 import BeautifulSoup


session = requests.Session()
url = 'http://gs25.gsretail.com/gscvs/ko/products/event-goods#;'
response = session.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
CSRFToken = soup.find('form', id='CSRFForm').find('input', attrs={'name': 'CSRFToken'}).get('value')

items = list()
data = {}
data['date'] = str(datetime.date.today())

for i in range(1, 20):
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    payload = {
        'pageNum': i,
        'pageSize': 50,
        'searchType': None,
        'searchWord': None,
        'parameterList': 'TOTAL'
    }

    url = 'http://gs25.gsretail.com/gscvs/ko/products/event-goods-search?CSRFToken=' + CSRFToken
    response = session.post(url, data=payload)
    results = response.json()
    products = json.loads(results)['results']

    if len(products) == 0:
        break

    for product in products:
        item = {}

        product_event = product['eventTypeNm']
        product_name = product['goodsNm']
        product_price = product['price']
        product_img_src = product['attFileNm']

        item['name'] = product_name
        item['price'] = int(product_price)
        item['img'] = product_img_src
        item['event'] = product_event
        item['store'] = 'gs25'
        items.append(item)


data['items'] = items

with open('../staticfiles/stores/gs25.json', 'w') as f:
    json.dump(data, f)

    # print(product['eventTypeNm'])  # 이벤트 형태
    # print(product['goodsNm'])      # 상품 이름
    # print(product['price'])        # 가격
    # print(product['attFileNm'])    # 이미지파일
