from flask import Blueprint, jsonify, request
from models.community_post import CommunityPost
from extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from

community_bp = Blueprint('community', __name__, url_prefix='/api/community')

@community_bp.route('/posts/', methods=['GET'], strict_slashes=False)
@swag_from({
    'tags': ['Community'],
    'summary': 'Get all community posts'
})
def get_posts():
    posts = CommunityPost.query.order_by(CommunityPost.created_at.desc()).all()
    return jsonify([post.to_dict() for post in posts])

@community_bp.route('/posts/', methods=['POST'], strict_slashes=False)
@jwt_required()
@swag_from({
    'tags': ['Community'],
    'summary': 'Create a new community post'
})
def create_post():
    data = request.get_json()
    current_user_id = get_jwt_identity()

    new_post = CommunityPost(
        title=data['title'],
        content=data['content'],
        excerpt=data.get('excerpt', data['content'][:150]),
        author_id=current_user_id
    )
    db.session.add(new_post)
    db.session.commit()
    return jsonify(new_post.to_dict()), 201
    