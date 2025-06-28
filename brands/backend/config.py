# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'fallback-secret-key')  # Fallback added
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///brands.db')  # Fallback SQLite DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'fallback-jwt-secret')

    SWAGGER = {
        'title': 'Brands API',
        'uiversion': 3,
        "specs_route": "/apidocs/"
    }

    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')