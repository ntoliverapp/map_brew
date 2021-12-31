# import os
# import re
from decouple import config
SQLALCHEMY_DATABASE_URI = config('DATABASE_URL')
# if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
#     SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
SECRET_KEY = config('SECRET_KEY')
