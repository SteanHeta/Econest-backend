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
    "name": "TerraCraft Supplies",
    "logo_url": "https://media.canva.com/v2/image-resize/format:JPG/height:452/quality:92/uri:ifs%3A%2F%2FM%2F2d1f9d0e-3c4d-4a5e-8f6e-7d3f8a0e5c6f/watermark:F/width:800?csig=AAAAAAAAAAAAAAAAAAAAALpXqVzRnWmZkIgDQrTlHwNpRqXoVsGtEpMvOj0CqK4S&exp=1750941850&osig=AAAAAAAAAAAAAAAAAAAAANsYqZpZvQbBmVqKwXrLsTnYpZoVqEwIrLmNcXhQ&signer=media-rpc&x-canva-quality=screen",
    "description": "Handmade eco-friendly home goods and décor items.",
    "location": "Muthaiga",
    "productCount": 28,
    "rating": 4.6,
    "reviewCount": 187,
    "story": "TerraCraft creates beautiful, functional home goods using natural materials like bamboo, jute, and reclaimed wood. Each item is handcrafted by artisans committed to sustainable living and fair wages.",
    "founded": 2018,
    "categories": ["Home Goods", "Decor"],
    "certifications": ["Fair Trade", "FSC Certified", "B-Corp"],
    "sustainabilityPractices": [
        {"name": "Carbon Neutral", "available": False},
        {"name": "Zero Waste", "available": True},
        {"name": "Renewable Energy", "available": True},
    ]
  },
      {
    "id": 25,
    "name": "GreenRoots Organics",
    "logo_url": "https://media.canva.com/v2/image-resize/format:JPG/height:452/quality:92/uri:ifs%3A%2F%2FM%2F7e6d8c0b-5a7e-4f32-ba2f-d4c8a7e8f9a3/watermark:F/width:800?csig=AAAAAAAAAAAAAAAAAAAAAKiWxLzVnYmZkIgDQrTlHwNpRqXoVsGtEpMvOj0CqK4S&exp=1750941800&osig=AAAAAAAAAAAAAAAAAAAAAMfUuPzZvQbBmVqKwXrLsTnYpZoVqEwIrLmNcXhQ&signer=media-rpc&x-canva-quality=screen",
    "description": "Organic food products grown sustainably and delivered locally.",
    "location": "Karen",
    "productCount": 56,
    "rating": 4.7,
    "reviewCount": 410,
    "story": "We believe in nourishing communities with clean, organic food that’s grown using regenerative farming techniques. Our farms use zero synthetic pesticides and support local biodiversity.",
    "founded": 2015,
    "categories": ["Food", "Organic"],
    "certifications": ["USDA Organic", "Regenerative Organic Certified", "Non-GMO Project Verified"],
    "sustainabilityPractices": [
        {"name": "Carbon Neutral", "available": True},
        {"name": "Zero Waste", "available": False},
        {"name": "Renewable Energy", "available": True},
    ]
    },
       
        {'name': 'leanRoots', 'description': 'Outdoor gear that respects the outdoors.'},
        {'name': 'Sustaina', 'description': 'Wear your values.'},
    ]
    for data in brand_data:
        db.session.add(Brand(**data))
    print("Brands prepared.")
    
   
    
   

    db.session.commit()
    print("Database seeded successfully!")