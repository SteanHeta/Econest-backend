import os
import firebase_admin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flasgger import Swagger
from authlib.integrations.flask_client import OAuth
from flask_cors import CORS
from firebase_admin import credentials

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
jwt = JWTManager()
swagger = Swagger()
cors = CORS()
oauth = OAuth()

firebase = None

FIREBASE_SERVICE_ACCOUNT_KEY_PATH = os.getenv('FIREBASE_SERVICE_ACCOUNT_KEY_PATH')

if FIREBASE_SERVICE_ACCOUNT_KEY_PATH:
    try:
        if os.path.exists(FIREBASE_SERVICE_ACCOUNT_KEY_PATH):
            cred = credentials.Certificate(FIREBASE_SERVICE_ACCOUNT_KEY_PATH)
            firebase = firebase_admin.initialize_app(cred)
        else:
            print(f"[Firebase] Error: Key file not found at {FIREBASE_SERVICE_ACCOUNT_KEY_PATH}")
    except Exception as e:
        print(f"[Firebase] Error initializing Firebase Admin SDK: {e}")
else:
    print("[Firebase] Warning: FIREBASE_SERVICE_ACCOUNT_KEY_PATH not set. Firebase not initialized.")

def init_oauth(app):
    oauth.init_app(app)
    
    oauth.register(
        name='google',
        client_id=os.getenv('GOOGLE_CLIENT_ID'),
        client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
        server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
        client_kwargs={
            'scope': 'openid email profile'
        }
    )
