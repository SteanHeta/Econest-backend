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

    # ==================================
    # Seed Users
    # ==================================
    user1 = User(username='JaneDoe', email='jane.doe@example.com')
    user1.set_password('password123')
    user2 = User(username='JohnSmith', email='john.smith@example.com')
    user2.set_password('password456')
    
    # Add users to the session first
    db.session.add_all([user1, user2])
    # IMPORTANT: Commit the users so they get an ID from the database
    db.session.commit()
    print("Users seeded.")

    # ==================================
    # Seed Brands
    # ==================================
    brand_data = [
          {
        "id": 1,
        "name": "EcoWear Co.",
        "logo_url": "https://via.placeholder.com/150/EEEEEE/333333?Text=EW",
        "slogan": "Sustainable fashion made from organic and recycled materials",
        "location": "Portland, OR",
        "productCount": 43,
        "rating": 4.8,
        "reviewCount": 342,
        "story": "Founded by environmental enthusiasts who believe fashion shouldn’t cost the earth. We create beautiful, durable clothing using only sustainable materials and ethical manufacturing practices.",
        "founded": 2019,
        "categories": ["Fashion", "Accessories"],
        "certifications": ["GOTS Certified", "Fair Trade", "B-Corp"],
        "sustainabilityPractices": [
            {"name": "Carbon Neutral", "available": True},
            {"name": "Zero Waste", "available": True},
            {"name": "Renewable Energy", "available": True},
        ]
    },
        {
        "id": 2,
        "name": "Pure Earth",
        "logo_url": "https://via.placeholder.com/150/EEEEEE/333333?Text=PE",
        "slogan": "Natural personal care products from organic ingredients",
        "location": "Austin, TX",
        "productCount": 38,
        "rating": 4.6,
        "reviewCount": 156,
        "story": "Creating pure, effective personal care products that are kind to your skin and the environment. All our ingredients are ethically sourced and sustainably harvested.",
        "founded": 2017,
        "categories": ["Personal Care", "Beauty"],
        "certifications": ["USDA Organic", "Leaping Bunny", "Vegan Society"],
        "sustainabilityPractices": [
            {"name": "Carbon Neutral", "available": False}, # Note: This will not have a green dot
            {"name": "Zero Waste", "available": True},
            {"name": "Renewable Energy", "available": True},
        ]
    },
        {'name': 'ReNewTech', 'description': 'Giving technology a second life.'},
        {'name': 'Pure Earth', 'description': 'Natural and organic personal care.'},
        {'name': 'Verde', 'description': 'Stylish and sustainable eyewear.'},
        {'name': 'leanRoots', 'description': 'Outdoor gear that respects the outdoors.'},
        {'name': 'Sustaina', 'description': 'Wear your values.'},
    ]
    for data in brand_data:
        db.session.add(Brand(**data))
    print("Brands prepared.")
    
    # ==================================
    # Seed Products (CORRECTED)
    # ==================================
    # The invalid 'label' keyword has been removed.
    # The feature labels are now correctly stored in the 'category' field as a comma-separated string.
    
    prod1 = Product(name='Organic Cotton T-Shirt', description='Eco-Friendly Fashion: Discover Organic Cotton Tees 🌿', price= 10.0, original_price=14.0 , location='portland' ,category='Fair Trade, Carbon Neutral', rating=4.5, brand_name='EcoWear Co.', stock=50, image_url='https://i.pinimg.com/736x/7a/a6/3b/7aa63bb4f76177e107b7b628c3d60853.jpg')
    prod2 = Product(name='Bamboo Water Bottle', description='Taste The Richness and Feel The Fragrance Of Bamboo With Your Every Sip', price=14.50, original_price=18.00, location='Miami' ,category='Local, BPA-Free', rating=4.8, brand_name='GreenLife', stock=95, image_url='https://i.pinimg.com/736x/29/d5/ae/29d5aed1a61e1d54eb17dec8bc2b05c7.jpg')
    prod3 = Product(name='Recycled Phone Case', description='options to protect your phone from everyday bumps and scratches.', price= 14.89, original_price=18.89 , location='Texas' ,category='Carbon Neutral, Durable', rating=4.7, brand_name='ReNewTech', stock=156, image_url='https://i.pinimg.com/736x/89/95/a4/8995a42783e7efa7213e08d2f626ec85.jpg')
    prod4 = Product(name='Natural Soap Set', description='Aloe Vera Soap, Cleansing Essential Oil Handmade Skin Care Soap, Plant-Based Aromatic Bath Bar For Daily Home & Personal Skin CleaningI', price= 9.0, original_price=12.0 , location='Brazil' ,category='Plastic-Free, Organic', rating=4.3, brand_name='Pure Earth', stock=78, image_url='https://i.pinimg.com/736x/76/e4/7d/76e47d2972ed275af416c93d3d25fe93.jpg')
    prod5 = Product(name='Eco Notebook', description='Kathik A5 natural notebook made from eco-friendly jute and cotton', price= 1.0, original_price=1.0 , location='Lavington' ,category='Plastic-Free, Organic', rating=4.0, brand_name='Pure Earth', stock=318, image_url='https://i.pinimg.com/736x/c0/92/30/c09230280fe9fce9f6033d585ff6f867.jpg')
    prod6 = Product(name='Eco Grocery Bag', description='Eco-friendly shopping bags combine style and functionality', price= 5.0, original_price=8.0 , location='Karen' ,category='Local, Durable', rating=4.9, brand_name='GreenLife', stock=20, image_url='https://i.pinimg.com/736x/f2/00/26/f20026bce69b2f02567cf9378b9a03a4.jpg')
    prod7 = Product(name='Eco Sunglasses', description='#give back to the Planet #Planet #sustainable handmade sunglasses #wood and bamboo handmade sunglasses', price= 6.0, original_price=10.0 , location='Kilimani' ,category='Non-Toxic, Recycled, Plastic-Free', rating=4.2, brand_name='Verde', stock=150, image_url='https://i.pinimg.com/736x/e6/ec/2e/e6ec2ee7237a8d0e41a30703493989a9.jpg')
    prod8 = Product(name='Natural Hoodie', description=', where classic style meets West Coast charm.', price= 19.0, original_price=22.0 , location='Nairobi' ,category='Recycled', rating=3.0, brand_name='EcoWear Co.', stock=175, image_url='https://i.pinimg.com/736x/0e/d6/56/0ed656ad8a57501e14739cf383b201f5.jpg')
    prod9 = Product(name='Organic Rain Jacket', description='Waterproof, quick-drying, touched soft, comfortable, windproof', price= 25.0, original_price=28.0 , location='Conventry' ,category='Non-Toxic, Durable', rating=4.0, brand_name='leanRoots', stock=250, image_url='https://i.pinimg.com/736x/bd/f4/68/bdf468c0d8281a0764844e7a86eab58f.jpg')
    prod10 = Product(name='Sustainable Hoodie', description='The Environmental Hoodie is the only hoodie youll need this Earth Day!', price= 35.0, original_price=38.0 , location='Tokyo' ,category='Fair Trade, Durable', rating=3.9, brand_name='Sustaina', stock=50, image_url='https://i.pinimg.com/736x/40/14/4a/40144a03761c21fefd477ded57ab9f3e.jpg')
    
    db.session.add_all([prod1, prod2, prod3, prod4, prod5, prod6, prod7, prod8, prod9, prod10])
    print("Products prepared.")

    # ==================================
    # Seed Community Posts
    # ==================================
    post1 = CommunityPost(title='My Zero-Waste Journey', content='Full content here...', excerpt='It all started with a simple change...', author_id=user1.id)
    post2 = CommunityPost(title='Top 5 Eco-Friendly Swaps for 2024', content='Full content here...', excerpt='Looking to reduce your carbon footprint? Here are five easy swaps...', author_id=user2.id)
    db.session.add_all([post1, post2])
    print("Community Posts prepared.")

    # Final commit for brands, products, and posts
    db.session.commit()
    print("Database seeded successfully!")