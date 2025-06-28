from extensions import db

class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    logo_url = db.Column(db.String(255))
    description = db.Column(db.Text)

    def to_dict(self):
        # CORRECTED: Changed 'c.namae' to 'c.name'
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}