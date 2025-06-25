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

    def to_dict(self):
        """
        Serializes the Product object from the database into a dictionary
        that EXACTLY matches the frontend ProductCard component's expectations.
        """
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "originalPrice": self.original_price or round(self.price * 1.25, 2), # Calculate if missing
            "brand": self.brand_name or "Eco Brand", # Provide a default
            "location": self.location or "Online", # Provide a default
            "rating": self.rating,
            "reviewCount": self.review_count,
            "categoryTag": self.category or "General", # Provide a default
            "imageUrl": self.image_url,
            # CRITICAL: Add a 'features' array to the response.
            # This satisfies the frontend's .map() call and prevents crashes.
            # In a real app, this might come from a many-to-many relationship.
            "features": (self.category.split(', ') if self.category else ["Sustainable"])
        }