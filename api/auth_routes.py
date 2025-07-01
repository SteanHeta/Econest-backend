from flask import Blueprint, request, jsonify, redirect, url_for
from models.user import User
from extensions import db, bcrypt, oauth
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flasgger import swag_from

FRONTEND_URL = 'http://localhost:5173'

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/register', methods=['POST'])
@swag_from({'tags': ['Authentication']})
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if User.query.filter((User.email == email) | (User.username == username)).first():
        return jsonify({"message": "Username or email already exists"}), 409

    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
@swag_from({'tags': ['Authentication']})
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token)

    return jsonify({"message": "Invalid credentials"}), 401

@auth_bp.route('/profile')
@jwt_required()
@swag_from({'tags': ['Authentication']})
def profile():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if user:
        return jsonify(user.to_dict())

    return jsonify({"message": "User not found"}), 404

@auth_bp.route('/google/login')
@swag_from({'tags': ['Authentication']})
def google_login():
    redirect_uri = url_for('auth.google_callback', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

@auth_bp.route('/google/callback')
@swag_from({'tags': ['Authentication']})
def google_callback():
    token = oauth.google.authorize_access_token()
    resp = oauth.google.get('https://www.googleapis.com/oauth2/v2/userinfo')
    user_info = resp.json()

    user = User.query.filter_by(email=user_info['email']).first()
    if not user:
        user = User(
            email=user_info['email'],
            username=user_info.get('name', user_info['email'].split('@')[0])
        )
        db.session.add(user)
        db.session.commit()
    access_token = create_access_token(identity=user.id)
    return redirect(f"{FRONTEND_URL}/login/success?token={access_token}")