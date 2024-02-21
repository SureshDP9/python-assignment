import uuid
from flask import jsonify
from functools import wraps
from app import db
from app.models import User, Product
from flask_jwt_extended import get_current_user

def role_required(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if get_current_user()["role"] == role:
                return func(*args, **kwargs)
            else:
                return jsonify({'message': 'Invalid user to do this operation'}), 401
        return wrapper
    return decorator

def get_products():
    products = Product.query.all()
    products_data = [{'id': product.id, 'product_id': product.product_id, 'product_name': product.product_name,
                      'price_per_unit': product.price_per_unit, 'qty': product.qty} for product in products]
    return jsonify(products_data)

def get_product(product_id):
    product = Product.query.filter_by(product_id=product_id).first()
    if product:
        return jsonify({
            'id':product.id,
            'product_id': product.product_id,
            'product_name': product.product_name,
            'price_per_unit': product.price_per_unit,
            'qty': product.qty
        })
    else:
        return jsonify({'message': 'Product Not Found'}), 404

def add_product(request):
    product_id = str(uuid.uuid4())
    data = request.get_json()
    data['product_id'] = product_id

    new_product = Product(**data)
    db.session.add(new_product)
    db.session.commit()

    return jsonify({'message': 'Product added successfully'}), 201

def update_product(request):
    data = request.get_json()
    product = Product.query.filter_by(product_id=data.get('product_id')).first()

    if product:
        for key, value in data.items():
            setattr(product, key, value)
        db.session.commit()
        return jsonify({'message': 'Product updated successfully'}), 200
    else:
        return jsonify({'message': 'Product not found'}), 404

def delete_product(product_id):
    product = Product.query.filter_by(product_id=product_id).first()
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted successfully'}), 200
    else:
        return jsonify({'message': 'Product not found'}), 404
