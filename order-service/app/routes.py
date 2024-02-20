import uuid
from datetime import datetime, timezone

from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_current_user

from app import app, db
from app.models import Orders, OrderedProducts
from app.service import get_total


@app.route('/order', methods=['POST'])
@jwt_required()
def create_order():
    order_id = str(uuid.uuid4())
    data = request.get_json()
    products_data = data.get('products', [])
    #response = check_quantity(data['qty'],data['product_id'],request)

    order_total = 0
    for product_data in products_data:
        order_total += get_total(product_data.get('product_id'),product_data.get('qty'),request)


    new_order = Orders(order_id=order_id, user_id=data['user_id'], status="Pending",total=order_total, date_of_purchase=datetime.now(timezone.utc))
    db.session.add(new_order)
    db.session.commit()

    for product_data in products_data:
        product_id = product_data.get('product_id')
        qty = product_data.get('qty')
        new_product = OrderedProducts(product_id=product_id, qty=qty)
        new_order.products.append(new_product)

    db.session.commit()
    return jsonify({'message': "Order created successfully"}), 200


# Read Orders
@app.route('/orders', methods=['GET'])
@jwt_required()
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
             'total':order.total
        }
        # Iterate through products associated with the order
        for product in order.products:
            product_info = {
                'product_id': product.product_id,
                'qty': product.qty
            }
            order_info['products'].append(product_info)  # Append product info to products list
        orders_data.append(order_info)  # Append order info to orders_data list

    return jsonify(orders_data)

# Update Order
@app.route('/order', methods=['PUT'])
@jwt_required()
def update_order():
    data = request.get_json()
    print(data['order_id'])
    order = Orders.query.filter_by(order_id=data['order_id']).first()

    if not order:
        return jsonify({'message': 'Order not found'}), 404
    else:
        order_total = 0
        for product_data in data.get('products', []):
            #calling product-service to get total of each product
            order_total += get_total(product_data.get('product_id'), product_data.get('qty'), request)
        Orders.set_total(order,total=order_total)

    for product_data in data.get('products', []):
        product_id = product_data.get('product_id')
        qty = product_data.get('qty')
        prod = OrderedProducts.query.filter_by(order_id=data['order_id'], product_id=product_id).first()
        if prod:
            prod.qty = qty
            db.session.commit()
    return jsonify({'message': 'Order products updated successfully'}), 200

# Delete Order
@app.route('/order/<string:order_id>', methods=['DELETE'])
@jwt_required()
def delete_order(order_id):
    order = Orders.query.filter_by(order_id=order_id).first()

    if order:
        # Delete associated ordered products
        for product in order.products:
            db.session.delete(product)

        # Delete the order
        db.session.delete(order)
        db.session.commit()
        return jsonify({'message': 'Order deleted successfully'}), 200
    else:
        return jsonify({'message': 'Order not found'}), 404



# Protected API
@app.route('/test', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(logged_in_as=get_current_user()["email"]), 200