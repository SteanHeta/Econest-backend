from flask import Flask, jsonify
from .config import Config
from flask_migrate import Migrate
from extensions import db, migrate, bcrypt, jwt, swagger, oauth, cors
from backend.brand_routes import brands_bp 


def create_app():
    """
    Creates and configures the Flask application.
    Initializes all extensions and registers blueprints.
    """
    app = Flask(__name__)
    app.config.from_object(Config) 

    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db) 
    bcrypt.init_app(app)
    jwt.init_app(app)
    swagger.init_app(app)
    oauth.init_app(app)

    app.register_blueprint(brands_bp)

    @app.route('/')
    def index():
        """
        Root endpoint that returns a welcome message.
        """
        return jsonify({"message": "Welcome to the Brands API!"})

    return app
app = create_app()

db.init_app(app)
migrate.init_app(app, db)
