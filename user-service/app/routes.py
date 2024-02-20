import jwt
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, get_current_user

from app import app, db
from app.models import User


# Signup API
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    role = data.get('role')

    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email already exists'}), 400

    new_user = User(email=email, role=role)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201


# Login API
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
        access_token = create_access_token(identity={"email": user.email, "role": user.role})
        return jsonify({'token': access_token})
    else:
        return jsonify({'message': 'Invalid credentials'}), 401


# Update Password API
@app.route('/update_password', methods=['POST'])
@jwt_required()
def update_password():
    current_user = get_jwt_identity()
    data = request.get_json()
    user = User.query.get(current_user)
    new_password = data.get('new_password')

    if user.check_password(new_password):
        return jsonify({'message': 'New password must be different from the current password'}), 400

    user.set_password(new_password)
    db.session.commit()
    return jsonify({'message': 'Password updated successfully'}), 200


# Delete User API
@app.route('/delete_user', methods=['DELETE'])
@jwt_required()
def delete_user():
    current_user = get_jwt_identity()
    user = User.query.get(current_user)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 200


# Protected API
@app.route('/test', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_current_user()
    return jsonify(logged_in_as=current_user["email"]), 200
