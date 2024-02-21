from flask import request, jsonify
from flask_jwt_extended import jwt_required,get_current_user

from app import app
from app.service import get_products, get_product, add_product, update_product, delete_product, role_required


# Get Products API
@app.route('/products', methods=['GET'])
@jwt_required()
def get_products_route():
    return get_products()

# Get Product API
@app.route('/product/<string:product_id>', methods=['GET'])
@jwt_required()
def get_product_route(product_id):
    return get_product(product_id)

# Add Product API
@app.route('/product', methods=['POST'])
@jwt_required()
@role_required('admin')
def add_product_route():
    return add_product(request)

# Update Product API
@app.route('/product', methods=['PUT'])
@jwt_required()
@role_required('admin')
def update_product_route():
    return update_product(request)

# Delete Product API
@app.route('/product/<string:product_id>', methods=['DELETE'])
@jwt_required()
@role_required('admin')
def delete_product_route(product_id):
    return delete_product(product_id)

# Protected API
@app.route('/test', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(logged_in_as=get_current_user()), 200
