from extensions import db

class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    logo_url = db.Column(db.String(1000))
    description = db.Column(db.Text)
    location = db.Column(db.String(100))
    productCount = db.Column(db.Integer, default=0)
    rating = db.Column(db.Float, default=0.0)
    reviewCount = db.Column(db.Integer, default=0)
    story = db.Column(db.Text)
    founded = db.Column(db.Integer)
    categories = db.Column(db.ARRAY(db.String(50)), default=[])
    certifications = db.Column(db.ARRAY(db.String(50)), default=[])
    sustainabilityPractices = db.Column(db.ARRAY(db.JSON), default=[])

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}