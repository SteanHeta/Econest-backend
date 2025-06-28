from flask import Flask, jsonify

from config import Config
from extensions import db, migrate, bcrypt, jwt, swagger, oauth, cors
from api.home_routes import home_bp
from api.product_routes import product_bp
from api.brand_routes import brand_bp
from api.community_routes import community_bp
from api.auth_routes import auth_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
   
    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db) 
    bcrypt.init_app(app)
    jwt.init_app(app)
    swagger.init_app(app)
    oauth.init_app(app)

    app.register_blueprint(home_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(brand_bp)
    app.register_blueprint(community_bp)
    app.register_blueprint(auth_bp)

    @app.route('/')
    def index():
        return jsonify({"message": "Welcome to the Eco-Nest Market API!", "docs": "/apidocs"})

    return app

from flask import Flask, jsonify
from config import Config
from extensions import db, migrate, bcrypt, jwt, swagger, oauth, cors
from api.home_routes import home_bp
from api.product_routes import product_bp
from api.brand_routes import brand_bp
from api.community_routes import community_bp
from api.auth_routes import auth_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

   
    cors.init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)
    swagger.init_app(app)
    oauth.init_app(app)

    app.register_blueprint(home_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(brand_bp)
    app.register_blueprint(community_bp)
    app.register_blueprint(auth_bp)

    @app.route('/')
    def index():
        return jsonify({"message": "Welcome to the Eco-Nest Market API!", "docs": "/apidocs"})

    return app