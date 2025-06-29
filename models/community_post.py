from extensions import db
from sqlalchemy import func
from sqlalchemy.orm import relationship

class CommunityPost(db.Model):
    __tablename__ = 'community_posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    excerpt = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    author = relationship('User', back_populates='posts')
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'excerpt': self.excerpt,
            'created_at': self.created_at.isoformat(),
            'author_id': self.author_id,
            'author_username': self.author.username if self.author else None 
        }