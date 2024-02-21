from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_current_user

from app import app, db
from app.service import create_order, get_orders, update_order, delete_order


# Create Order
@app.route('/order', methods=['POST'])
@jwt_required()
def create_order_route():
    return create_order(request)

# Read Orders
@app.route('/orders', methods=['GET'])
@jwt_required()
def get_orders_route():
    return get_orders()

# Update Order
@app.route('/order', methods=['PUT'])
@jwt_required()
def update_order_route():
    return update_order(request)

# Delete Order
@app.route('/order/<string:order_id>', methods=['DELETE'])
@jwt_required()
def delete_order_route(order_id):
    return delete_order(order_id)

# Protected API
@app.route('/test', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(logged_in_as=get_current_user()["email"]), 200