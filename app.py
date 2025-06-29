import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

from config import Config
from extensions import db, migrate, bcrypt, jwt, swagger, cors, oauth, init_oauth
from api.home_routes import home_bp
from api.product_routes import product_bp
from api.brand_routes import brand_bp
from api.community_routes import community_bp
from api.auth_routes import auth_bp

load_dotenv(override=True)

print("--- LOADING CONFIG ---")
print("DATABASE_URL being used by Flask:", os.getenv('DATABASE_URL'))
print("--------------------")

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
