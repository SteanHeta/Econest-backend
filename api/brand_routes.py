from flask import Blueprint, jsonify
from models.brand import Brand
from flasgger import swag_from

brand_bp = Blueprint('brands', __name__, url_prefix='/api/brands')

@brand_bp.route('/', methods=['GET'], strict_slashes=False)
@swag_from({
    'tags': ['Brands'],
    'summary': 'Get a list of all brands'
})
def get_brands():
    brands = Brand.query.all()
    return jsonify([brand.to_dict() for brand in brands])

@brand_bp.route('/<int:brand_id>', methods=['GET'])
def get_brand(brand_id):
    brand = Brand.query.get_or_404(brand_id)
    return jsonify(brand.to_dict())