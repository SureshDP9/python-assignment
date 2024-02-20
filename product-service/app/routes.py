import uuid
from functools import wraps

from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, get_current_user

from app import app, db
from app.models import User, Product


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

@app.route('/products', methods=['GET'])
@jwt_required()
def get_products():
    products = Product.query.all()
    products_data = [{'id': product.id, 'product_id': product.product_id, 'product_name': product.product_name,
                      'price_per_unit': product.price_per_unit, 'qty': product.qty} for product in products]
    return jsonify(products_data)


@app.route('/product/<string:product_id>',methods=['GET'])
@jwt_required()
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

# Add product API
@app.route('/product', methods=['POST'])
@jwt_required()
@role_required('admin')
def add_product():
    # Generate a random UUID as the product ID
    product_id = str(uuid.uuid4())

    data = request.get_json()
    data['product_id'] = product_id

    new_product = Product(**data)
    db.session.add(new_product)
    db.session.commit()

    return jsonify({'message': 'Product added successfully'}), 201


# Update product API
@app.route('/product', methods=['PUT'])
@jwt_required()
@role_required('admin')
def update_product():
    data = request.get_json()
    print(data)
    product = Product.query.filter_by(product_id=data.get('product_id')).first()

    if product:
        for key, value in data.items():
            setattr(product, key, value)
        db.session.commit()
        print("Product updated successfully")
        return jsonify({'message': 'Product updated successfully'}), 200
    else:
        return jsonify({'message': 'Product not found'}), 404


# Delete product API
@app.route('/product/<string:product_id>', methods=['DELETE'])
@jwt_required()
@role_required('admin')
def delete_product(product_id):
    print(product_id)
    product = Product.query.filter_by(product_id=product_id).first()


    print(product_id)
    product = Product.query.filter_by(product_id=product_id).first()
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted successfully'}), 200
    else:
        return jsonify({'message': 'Product not found'}), 404




# Protected API
@app.route('/test', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(logged_in_as=get_current_user()), 200