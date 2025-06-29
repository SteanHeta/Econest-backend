from flask import Blueprint, jsonify
from models.product import Product
from models.community_post import CommunityPost
from flasgger import swag_from

home_bp = Blueprint('home', __name__, url_prefix='/api/home')

@home_bp.route('/featured-products', methods=['GET'])
@swag_from({
    'tags': ['Home'],
    'summary': 'Get featured products for the homepage',
    'responses': { 200: {'description': 'A list of 3 featured products'} }
})
def get_featured_products():
    products = Product.query.order_by(Product.rating.desc()).limit(3).all()
    return jsonify([p.to_dict() for p in products])

@home_bp.route('/latest-posts', methods=['GET'])
@swag_from({
    'tags': ['Home'],
    'summary': 'Get latest community posts for the homepage',
    'responses': { 200: {'description': 'A list of the 2 most recent posts'} }
})
def get_latest_posts():
    posts = CommunityPost.query.order_by(CommunityPost.created_at.desc()).limit(2).all()
    return jsonify([p.to_dict() for p in posts])