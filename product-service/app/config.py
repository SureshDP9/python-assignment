from datetime import timedelta


class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://username:password@localhost/db_name'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)  # Token expiration time
    JWT_HEADER_TYPE = 'JWT'  # Set the JWT header type
    # local 'mysql://root:root@127.0.0.1:3306/mydatabase'
    # git 'mysql://root:root@host.docker.internal:3306/mydatabase'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1:3306/mydatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False