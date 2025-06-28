import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('JWT_SECRET_KEY') 
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

 
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')


    SWAGGER = {
        'title': 'Eco-Nest Market API',

        'uiversion': 3,
        "specs_route": "/apidocs/"
    }
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')