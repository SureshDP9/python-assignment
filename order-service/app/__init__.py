import os
from datetime import timedelta

from dotenv import load_dotenv
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

# from app.config import Config

# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

app = Flask(__name__)

print("environment  : ***************", os.getenv('FLASK_ENV'),"****************")
#open(os.environ.get('SQLALCHEMY_DATABASE_URI_FILE')).read().strip()
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['JWT_HEADER_TYPE'] = os.getenv('JWT_HEADER_TYPE')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=int(os.getenv('JWT_EXPIRATION_MINUTES', 30)))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_default_secret_key_here')
db = SQLAlchemy(app)
jwt = JWTManager(app)


from app import routes, models