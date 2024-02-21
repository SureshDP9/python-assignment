from flask import jsonify
from flask_jwt_extended import get_jwt_identity, create_access_token

from app import db
from app.models import User

def signup_user(request):
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

def login_user(request):
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
        access_token = create_access_token(identity={"email": user.email, "role": user.role})
        return jsonify({'token': access_token})
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

def update_password(request):
    current_user = get_jwt_identity()
    data = request.get_json()
    user = User.query.get(current_user)
    new_password = data.get('new_password')

    if user.check_password(new_password):
        return jsonify({'message': 'New password must be different from the current password'}), 400

    user.set_password(new_password)
    db.session.commit()
    return jsonify({'message': 'Password updated successfully'}), 200

def delete_user():
    current_user = get_jwt_identity()
    user = User.query.get(current_user)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 200
