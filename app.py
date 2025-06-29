import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import json
import firebase_admin
from firebase_admin import credentials

from config import Config
from extensions import db, migrate, bcrypt, jwt, swagger, cors, oauth, init_oauth
from api.home_routes import home_bp
from api.product_routes import product_bp
from api.brand_routes import brand_bp
from api.community_routes import community_bp
from api.auth_routes import auth_bp

load_dotenv(override=True)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    CORS(app)
    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)
    swagger.init_app(app)
    init_oauth(app)

    try:
        firebase_config_json_str = os.getenv('FIREBASE_SERVICE_ACCOUNT_JSON')
        if firebase_config_json_str:
            cred = credentials.Certificate(json.loads(firebase_config_json_str))
            if not firebase_admin._apps:
                firebase_admin.initialize_app(cred)
        else:
            print("FIREBASE_SERVICE_ACCOUNT_JSON environment variable not set. Firebase not initialized.")
    except Exception as e:
        print(f"Error initializing Firebase: {e}")

    app.register_blueprint(home_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(brand_bp)
    app.register_blueprint(community_bp)
    app.register_blueprint(auth_bp)

    @app.route('/')
    def index():
        return jsonify({
            "message": "Welcome to the Eco-Nest Market API!",
            "docs": "/apidocs"
        })

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5001)
