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

 
    

    # Seed Brands
    # ==================================
    brand_data = [
          {
        "id": 23,
        "name": "EcoWear move Co.",
        "logo_url": "https://media.canva.com/v2/image-resize/format:JPG/height:452/quality:92/uri:ifs%3A%2F%2FM%2F46658c74-ee7d-470c-a82c-a2bc88c22068/watermark:F/width:800?csig=AAAAAAAAAAAAAAAAAAAAAFIradi8FadbTDRJqJiWoxVoPE4u576XAe3XpesSD921&exp=1750941429&osig=AAAAAAAAAAAAAAAAAAAAAHzYFnjDoi3rh3Aapnjv3ZKCb2qYTe9MV5lzqZM76-LT&signer=media-rpc&x-canva-quality=screen",
        "description": "Sustainable fashion made from organic and recycled materials",
        "location": "Lavington",
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
        "id": 24,
        "name": "Pure fresh Earth",
        "logo_url": "https://media.canva.com/v2/image-resize/format:JPG/height:452/quality:92/uri:ifs%3A%2F%2FM%2Fb996e5a6-07f2-4e67-9553-f520db356c59/watermark:F/width:800?csig=AAAAAAAAAAAAAAAAAAAAAMUShSuYj7mxW20ZRdPyU5kqQ2winTnqLv3hI1wF-gT2&exp=1750941749&osig=AAAAAAAAAAAAAAAAAAAAAOkSzyWf1S0gmdiLtnYqxnEIcrD85wknvOdmpgEUWtXe&signer=media-rpc&x-canva-quality=screen",
        "description": "Natural personal care products from organic ingredients",
        "location": "Kilimani",
        "productCount": 38,
        "rating": 4.6,
        "reviewCount": 156,
        "story": "Creating pure, effective personal care products that are kind to your skin and the environment. All our ingredients are ethically sourced and sustainably harvested.",
        "founded": 2017,
        "categories": ["Personal Care", "Beauty"],
        "certifications": ["USDA Organic", "Leaping Bunny", "Vegan Society"],
        "sustainabilityPractices": [
            {"name": "Carbon Neutral", "available": False},
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
    
   
    
   

    db.session.commit()
    print("Database seeded successfully!")