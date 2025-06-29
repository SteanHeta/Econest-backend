import os
from dotenv import load_dotenv

load_dotenv(override=True)  
print("--- LOADING CONFIG ---")
print("DATABASE_URL being used by Flask:", os.getenv('DATABASE_URL'))
print("--------------------")

class Config:
    """Base Flask configuration."""
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
    FIREBASE_SERVICE_ACCOUNT_KEY_PATH = os.getenv('FIREBASE_SERVICE_ACCOUNT_KEY_PATH')
