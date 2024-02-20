import os

import requests

def get_total(product_id, qty, request):
    total = 0
    product_service_url = os.environ.get('PRODUCT_SERVICE_URL')
    url = f'{product_service_url}{product_id}'
    print(url)

    token = request.headers.get('Authorization')
    print(token)
    headers = {
        'Authorization': token
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        product_data = response.json()
        total = qty * product_data['price_per_unit']
    return total
