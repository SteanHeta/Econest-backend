from extensions import db
import json

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    original_price = db.Column(db.Float)
    category = db.Column(db.String(50))
    brand_name = db.Column(db.String(50))
    location = db.Column(db.String(50))
    image_url = db.Column(db.String(255))
    reviews = db.Column(db.Integer, default=0)
    rating = db.Column(db.Float, default=4.5)
    labels = db.Column(db.String(255))
    features = db.Column(db.String(255))


    def to_dict(self):

        def parse_json_field(field_data):
            if field_data and isinstance(field_data, str):
                try:
                    return json.loads(field_data)
                except json.JSONDecodeError:
                    return [item.strip() for item in field_data.split(',')]
            return []

        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "originalPrice": self.original_price,
            "category": self.category,
            "brand": self.brand_name,
            "location": self.location,
            "reviews": self.reviews,
            "rating": self.rating,
            "imageUrl": self.image_url, 
            "labels": parse_json_field(self.labels),
            "features": parse_json_field(self.features),
        }