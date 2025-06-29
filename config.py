import os
from dotenv import load_dotenv

load_dotenv(override=True)

print("--- LOADING CONFIG (from config.py) ---")
print("DATABASE_URL being used by Config:", os.getenv('DATABASE_URL'))
print("FIREBASE_SERVICE_ACCOUNT_JSON being used by Config:", os.getenv('FIREBASE_SERVICE_ACCOUNT_JSON'))
print("--------------------")

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SWAGGER = {
        'title': 'Eco-Nest Market API',
        'uiversion': 3
    }

    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')

    FIREBASE_SERVICE_ACCOUNT_JSON = os.getenv('FIREBASE_SERVICE_ACCOUNT_JSON')