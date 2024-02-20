# import os
# from datetime import timedelta
#
#
# class Config:
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SECRET_KEY = os.environ.get('SECRET_KEY', 'your_default_secret_key_here')
#     JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=int(os.environ.get('JWT_EXPIRATION_MINUTES', 30)))
#     JWT_HEADER_TYPE = os.environ.get('JWT_HEADER_TYPE', 'JWT')
#
#     # Define the default database URI
#     DEFAULT_DB_URI = 'mysql://root:root@host.docker.internal:3306/mydatabase'
#
#     # Use the environment variable if it exists, otherwise use the default URI
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', DEFAULT_DB_URI)
#     # local 'mysql://root:root@127.0.0.1:3306/mydatabase'
#     # git 'mysql://root:root@host.docker.internal:3306/mydatabase'
