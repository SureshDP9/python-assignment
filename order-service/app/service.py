import os

import requests
import uuid
from datetime import datetime, timezone

from flask import jsonify

from app import db
from app.models import Orders, OrderedProducts



def create_order(request):
    order_id = str(uuid.uuid4())
    data = request.get_json()
    products_data = data.get('products', [])

    order_total = 0
    for product_data in products_data:
        order_total += get_total(product_data.get('product_id'), product_data.get('qty'), request)

    new_order = Orders(order_id=order_id, user_id=data['user_id'], status="Pending", total=order_total, date_of_purchase=datetime.now(timezone.utc))
    db.session.add(new_order)
    db.session.commit()

    for product_data in products_data:
        product_id = product_data.get('product_id')
        qty = product_data.get('qty')
        new_product = OrderedProducts(product_id=product_id, qty=qty)
        new_order.products.append(new_product)

    db.session.commit()
    return jsonify({'message': "Order created successfully"}), 200

def get_orders():
    orders = Orders.query.all()
    orders_data = []
    for order in orders:
        order_info = {
            'id': order.id,
            'order_id': order.order_id,
            'user_id': order.user_id,
            'date_of_purchase': order.date_of_purchase,
            'status': order.status,
            'products': [],  # Initialize products list for the order
            'total': order.total
        }
        for product in order.products:
            product_info = {
                'product_id': product.product_id,
                'qty': product.qty
            }
            order_info['products'].append(product_info)
        orders_data.append(order_info)
    return jsonify(orders_data)

def update_order(request):
    data = request.get_json()
    order = Orders.query.filter_by(order_id=data['order_id']).first()

    if not order:
        return jsonify({'message': 'Order not found'}), 404
    else:
        order_total = 0
        for product_data in data.get('products', []):
            order_total += get_total(product_data.get('product_id'), product_data.get('qty'), request)
        Orders.set_total(order, total=order_total)

    for product_data in data.get('products', []):
        product_id = product_data.get('product_id')
        qty = product_data.get('qty')
        prod = OrderedProducts.query.filter_by(order_id=data['order_id'], product_id=product_id).first()
        if prod:
            prod.qty = qty
            db.session.commit()
    return jsonify({'message': 'Order products updated successfully'}), 200

def delete_order(order_id):
    order = Orders.query.filter_by(order_id=order_id).first()

    if order:
        for product in order.products:
            db.session.delete(product)
        db.session.delete(order)
        db.session.commit()
        return jsonify({'message': 'Order deleted successfully'}), 200
    else:
        return jsonify({'message': 'Order not found'}), 404


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
