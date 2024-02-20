import requests


def check_quantity(qty, product_id, request):
    url = f'http://localhost:5002/product/{product_id}'
    print(url)

    token = request.headers.get('Authorization')
    print(token)
    headers = {
        'Authorization': token
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        product_data = response.json()

        if product_data:
            if product_data['qty'] > 0 and product_data['qty'] > qty:
                update_url = 'http://localhost:5002/product'
                update_data = {
                    'product_id': product_data['product_id'],
                    'qty': product_data['qty'] - qty
                }
                update_response = requests.put(update_url, json=update_data, headers=headers)

                if update_response.status_code == 200:
                    print('Product updated successfully')
                    return "success"
                else:
                    print('Failed to update product:', update_response.json())
            else:
                return "out of stock"
        else:
            return "Product data not found"
    else:
        return "Failed to fetch product data"


def get_total(product_id, qty, request):
    total = 0
    url = f'http://localhost:5002/product/{product_id}'
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
