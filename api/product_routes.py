from flask import Blueprint, jsonify
from models.product import Product
from flasgger import swag_from

product_bp = Blueprint('products', __name__, url_prefix='/api/products')

@product_bp.route('/', methods=['GET'], strict_slashes=False)
@swag_from({
    'tags': ['Products'],
    'summary': 'Get a list of all products from the database',
    'responses': {
        200: {
            'description': 'A list of all product objects, formatted for the frontend.',
        }
    }
})
def get_products():
  
    products = Product.query.all()
    
    return jsonify([product.to_dict() for product in products])


@product_bp.route('/<int:product_id>', methods=['GET'])
@swag_from({
    'tags': ['Products'],
    'summary': 'Get a single product by its ID',
    'parameters': [{
        'name': 'product_id',
        'in': 'path',
        'required': True,
        'type': 'integer'
    }],
    'responses': {
        200: {'description': 'Product object'},
        404: {'description': 'Product not found'}
    }
})
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify(product.to_dict())