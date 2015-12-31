import os

DEBUG = True
SECRET_KEY = 'temporary_secret_key'  # make sure to change this

SQLALCHEMY_DATABASE_URI = 'postgresql://localhost:5432/duelyst'

WTF_CSRF_ENABLED = True
SECRET_KEY = os.environ.get('FORM_KEY', 'schenanigans')