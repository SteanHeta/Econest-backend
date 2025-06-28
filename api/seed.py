from app import create_app
from extensions import db
from models.product import Product
from models.brand import Brand
from models.user import User
from models.community_post import CommunityPost

app = create_app()

with app.app_context():
    print("Dropping all tables...")
    db.drop_all()
    print("Creating all tables...")
    db.create_all()
    print("Seeding database...")


    post1 = CommunityPost(title='My Zero-Waste Journey', content='Full content here...', excerpt='It all started with a simple change...', author_id=user1.id)
    post2 = CommunityPost(title='Top 5 Eco-Friendly Swaps for 2024', content='Full content here...', excerpt='Looking to reduce your carbon footprint? Here are five easy swaps...', author_id=user2.id)
    db.session.add_all([post1, post2])
    print("Community Posts prepared.")

    db.session.commit()
    print("Database seeded successfully!")