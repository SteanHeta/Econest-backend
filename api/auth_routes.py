import os
from flask import Blueprint, request, jsonify, redirect, url_for
from models.user import User
from extensions import db, bcrypt, jwt, oauth
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flasgger import swag_from

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')
FRONTEND_URL = os.getenv('FRONTEND_URL', 'http://localhost:3000')

@auth_bp.route('/register', methods=['POST'])
@swag_from({
    'tags': ['Authentication'],
    'summary': 'Register a new user',
    'parameters': [{
        'name': 'body', 'in': 'body', 'required': True,
        'schema': { 'properties': {
            'username': {'type': 'string'}, 'email': {'type': 'string'}, 'password': {'type': 'string'}
        }}
    }],
    'responses': { 201: {'description': 'User created'}, 409: {'description': 'User already exists'} }
})
def register():
    data = request.get_json()
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"msg": "Email already exists"}), 409
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"msg": "Username already exists"}), 409

    new_user = User(username=data['username'], email=data['email'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "User created successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
@swag_from({
    'tags': ['Authentication'],
    'summary': 'Log in a user',
    'parameters': [{'name': 'body', 'in': 'body', 'required': True, 'schema': { 'properties': {
        'email': {'type': 'string'}, 'password': {'type': 'string'}
    }}}],
    'responses': { 200: {'description': 'Login successful, returns access token'}, 401: {'description': 'Bad email or password'} }
})
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Bad email or password"}), 401

@auth_bp.route('/profile', methods=['GET'])
@jwt_required()
@swag_from({
    'tags': ['Authentication'], 'summary': 'Get current user profile',
    'security': [{'Bearer': []}],
    'responses': { 200: {'description': 'User profile data'} }
})
def profile():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    return jsonify(user.to_dict())

@auth_bp.route('/google/login')
@swag_from({
    'tags': ['Authentication'],
    'summary': 'Initiate Google OAuth login',
    'description': 'This will redirect the user to Google\'s authentication page.'
})
def google_login():
    redirect_uri = url_for('auth.google_authorize', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

@auth_bp.route('/google/authorize')
@swag_from({
    'tags': ['Authentication'],
    'summary': 'Callback URL for Google OAuth',
    'description': 'Google redirects here after authentication. This is not meant to be called directly.'
})
def google_authorize():
    token = oauth.google.authorize_access_token()
    user_info = oauth.google.get('https://www.googleapis.com/oauth2/v2/userinfo').json()
    
    user = User.query.filter_by(email=user_info['email']).first()
    if not user:
    
        user = User(
            email=user_info['email'],
            username=user_info.get('name', user_info['email'].split('@')[0])
        )
        db.session.add(user)
        db.session.commit()

    access_token = create_access_token(identity=user.id)

    return redirect(f"{FRONTEND_URL}/auth/callback?token={access_token}")