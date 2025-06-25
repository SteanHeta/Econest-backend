from flask import Blueprint, jsonify
from models.product import Product  # Import the database model
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
    """
    Retrieves all products from the database, converts each one to a dictionary
    using the model's to_dict() method, and returns the result as JSON.
    """
    # This now queries the live database
    products = Product.query.all()
    
    # Each product object will be transformed by the to_dict() method we just fixed
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
        200: {'description': 'A single product object'},
        404: {'description': 'Product not found'}
    }
})
def get_product(product_id):
    """Retrieves a single product by its ID from the database."""
    product = Product.query.get_or_404(product_id)
    return jsonify(product.to_dict())