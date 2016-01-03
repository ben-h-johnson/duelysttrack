import os

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'postgresql://localhost:5432/duelyst'

WTF_CSRF_ENABLED = True
SECRET_KEY = os.environ.get('FORM_KEY', 'schenanigans')