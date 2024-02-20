from datetime import datetime

from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="user")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha256')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.String(50), nullable=False,index=True)
    user_id = db.Column(db.Integer, nullable=False)
    date_of_purchase = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    total = db.Column(db.Integer)

    # Establishing one-to-many relationship with OrderedProducts
    products = relationship("OrderedProducts", backref="orders", lazy=True)

    def __init__(self, order_id, user_id, status,total, date_of_purchase=None):
        self.order_id = order_id
        self.user_id = user_id
        self.status = status
        self.total= total
        if date_of_purchase is not None:
            self.date_of_purchase = date_of_purchase

    def set_total(self,total):
        self.total=total
class OrderedProducts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(50), nullable=False)
    order_id = db.Column(db.String(50), db.ForeignKey('orders.order_id'))  # Corrected foreign key reference
    qty = db.Column(db.Integer, nullable=False)

    def __init__(self, product_id, qty):
        self.product_id = product_id
        self.qty = qty