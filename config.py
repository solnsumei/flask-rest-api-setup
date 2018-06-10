import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app_environment = os.environ.get('FLASK_ENV')
JWT_AUTH_URL_RULE = '/api/v1/login'
JWT_AUTH_USERNAME_KEY = 'email'
JWT_SECRET_KEY = os.environ.get('SECRET_KEY')

if app_environment == 'development':
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")

if app_environment == 'production':
    SQLALCHEMY_DATABASE_URI = os.environ.get("PROD_DATABASE_URI")

DEBUG = os.environ.get("DEBUG")
SQLALCHEMY_TRACK_MODIFICATIONS = False
