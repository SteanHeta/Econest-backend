from extensions import db

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
    stock = db.Column(db.Integer, default=0)
    rating = db.Column(db.Float, default=4.5)
    review_count = db.Column(db.Integer, default=100)
    labels = db.Column(db.String(100))
    features = db.Column(db.String(100))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "originalPrice": self.original_price or round(self.price * 1.25, 2), 
            "brand": self.brand_name or "Eco Brand",
            "location": self.location,
            "rating": self.rating,
            "reviewCount": self.review_count,
            "categoryTag": self.category,
            "imageUrl": self.image_url,
            "features": self.features or "Organic, Recycled Materials",
            "labels": self.labels or "Eco-Friendly, Sustainable",
            "description": self.description,
            "stock": self.stock,
        }