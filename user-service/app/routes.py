from flask import request, jsonify
from flask_jwt_extended import jwt_required,get_current_user

from app import app
from app.service import signup_user, login_user, update_password, delete_user


# Signup API
@app.route('/signup', methods=['POST'])
def signup():
    return signup_user(request)

# Login API
@app.route('/login', methods=['POST'])
def login():
    return login_user(request)

# Update Password API
@app.route('/update_password', methods=['POST'])
@jwt_required()
def update_password_route():
    return update_password(request)

# Delete User API
@app.route('/delete_user', methods=['DELETE'])
@jwt_required()
def delete_user_route():
    return delete_user()

# Protected API
@app.route('/test', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_current_user()
    return jsonify(logged_in_as=current_user["email"]), 200
