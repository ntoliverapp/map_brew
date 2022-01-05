import os
import re

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
SECRET_KEY = os.environ.get('SECRET_KEY')
# from decouple import config
# SQLALCHEMY_DATABASE_URI = config('DATABASE_URL')
# SECRET_KEY = config('SECRET_KEY')
