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

 
    # Seed Users
    # ==================================
    user1 = User(username='Stean', email='stean5973@gmail.com')
    user1.set_password('Stean4lyf2#')
    user2 = User(username='JohnSmith', email='john.smith@example.com')
    user2.set_password('password456')
    
 
    db.session.add_all([user1, user2])
    
    db.session.commit()
    print("Users seeded.")

    # Seed Brands
    # ==================================
    brand_data = [
          {
        "id": 21,
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
        "id": 22,
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
    {
    "id": 23,
    "name": "Sustaina Co.",
    "logo_url": "https://media.canva.com/v2/image-resize/format:JPG/height:452/quality:92/uri:ifs%3A%2F%2FM%2F2d1f9d0e-3c4d-4a5e-8f6e-7d3f8a0e5c6f/watermark:F/width:800?csig=AAAAAAAAAAAAAAAAAAAAALpXqVzRnWmZkIgDQrTlHwNpRqXoVsGtEpMvOj0CqK4S&exp=1750941850&osig=AAAAAAAAAAAAAAAAAAAAANsYqZpZvQbBmVqKwXrLsTnYpZoVqEwIrLmNcXhQ&signer=media-rpc&x-canva-quality=screen",
    "description": "Handmade eco-friendly home goods and décor items.",
    "location": "Tokyo",
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
    "id": 24,
    "name": "Verde Co.",
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
    {
    "id": 27,
    "name": "leanRoots Co.",
    "logo_url": "https://media.canva.com/v2/image-resize/format:JPG/height:452/quality:92/uri:ifs%3A%2F%2FM%2Fba634239-5c1a-4d3f-b661-63db3b7a6579/watermark:F/width:800?csig=AAAAAAAAAAAAAAAAAAAAALrkKDZfHQfLM5Z68EcxZyRy2f6aJDnyIgDpBJKvRjZ&exp=1750942999&osig=AAAAAAAAAAAAAAAAAAAAADvMWF3zmt1xDk6mSQUm8oT8tRUQjvDbNcy5XcbWJSq&signer=media-rpc&x-canva-quality=screen",
    "description": "Outdoor gear that respects the outdoors.",
    "location": "Miami",
    "productCount": 33,
    "rating": 4.5,
    "reviewCount": 122,
    "story": "leanRoots was founded by explorers and nature-lovers who wanted gear that leaves no trace. Our products are made from responsibly sourced materials and designed for longevity in the wild.",
    "founded": 2018,
    "categories": ["Outdoor", "Gear", "Sports & Adventure"],
    "certifications": ["Fair Trade", "EcoCert"],
    "sustainabilityPractices": [
        {"name": "Carbon Neutral", "available": True},
        {"name": "Zero Waste", "available": True},
        {"name": "Renewable Energy", "available": False},
    ]
},
    ]
    for data in brand_data:
        db.session.add(Brand(**data))
    print("Brands prepared.")
    
   
    ## seed products
    # ==================================
    prod1 = Product(name='Organic Cotton T-Shirt', description='Eco-Friendly Fashion: Discover Organic Cotton Tees 🌿', price= 10.0, original_price=14.0 , location='Tokyo' ,category='Fashion', labels='Fair Trade, Carbon Neutral', rating=4.5, brand_name='EcoWear Co.', reviews=50, image_url='https://i.pinimg.com/736x/7a/a6/3b/7aa63bb4f76177e107b7b628c3d60853.jpg', features='Organic')
    prod2 = Product(name='Bamboo Water Bottle', description='Taste The Richness and Feel The Fragrance Of Bamboo With Your Every Sip', price=14.50, original_price=18.00, location='Miami' ,category='Food & Beverage', labels='Local, BPA-Free', rating=4.8, brand_name='GreenLife', reviews=95, image_url='https://i.pinimg.com/736x/29/d5/ae/29d5aed1a61e1d54eb17dec8bc2b05c7.jpg', features='Zero Waste')
    prod3 = Product(name='Recycled Phone Case', description='options to protect your phone from everyday bumps and scratches.', price= 14.89, original_price=18.89 , location='Texas' ,category='Electronics', labels='Carbon Neutral, Durable',  rating=4.7, brand_name='ReNewTech', reviews=156, image_url='https://i.pinimg.com/736x/89/95/a4/8995a42783e7efa7213e08d2f626ec85.jpg', features='Recycled')
    prod4 = Product(name='Natural Soap Set', description='Aloe Vera Soap, Cleansing Essential Oil Handmade Skin Care Soap, Plant-Based Aromatic Bath Bar For Daily Home & Personal Skin CleaningI', price= 9.0, original_price=12.0 , location='Lavington' ,category='Personal Care', labels='Plastic-Free, Organic',  rating=4.3, brand_name='Pure Earth', reviews=78, image_url='https://i.pinimg.com/736x/76/e4/7d/76e47d2972ed275af416c93d3d25fe93.jpg', features='Vegan')
    prod5 = Product(name='Eco Notebook', description='Kathik A5 natural notebook made from eco-friendly jute and cotton', price= 1.0, original_price=1.0 , location='Lavington' ,category='Personal Care', labels='Plastic-Free, Organic', rating=4.0, brand_name='Pure Earth', reviews=318, image_url='https://i.pinimg.com/736x/c0/92/30/c09230280fe9fce9f6033d585ff6f867.jpg', features='Organic, Renewable')
    prod6 = Product(name='Eco Grocery Bag', description='Eco-friendly shopping bags combine style and functionality', price= 5.0, original_price=8.0 , location='Karen' ,category='Home & Garden', labels='Local, Durable', rating=4.9, brand_name='GreenLife', reviews=20, image_url='https://i.pinimg.com/736x/f2/00/26/f20026bce69b2f02567cf9378b9a03a4.jpg', features='Renewable, Vegan')
    prod7 = Product(name='Eco Sunglasses', description='#give back to the Planet #Planet #sustainable handmade sunglasses #wood and bamboo handmade sunglasses', price= 6.0, original_price=10.0 , location='Kilimani' ,category='Fashion', labels='Non-Toxic, Recycled, Plastic-Free',  rating=4.2, brand_name='Verde', reviews=150, image_url='https://i.pinimg.com/736x/e6/ec/2e/e6ec2ee7237a8d0e41a30703493989a9.jpg', features='Organic')
    prod8 = Product(name='Natural Hoodie', description=', where classic style meets West Coast charm.', price= 19.0, original_price=22.0 , location='Miami' ,category='Fashion', labels='Recycled',  rating=3.0, brand_name='EcoWear Co.', reviews=175, image_url='https://i.pinimg.com/736x/0e/d6/56/0ed656ad8a57501e14739cf383b201f5.jpg', features='Compostable, Vegan')
    prod9 = Product(name='Organic Rain Jacket', description='Waterproof, quick-drying, touched soft, comfortable, windproof', price= 25.0, original_price=28.0 , location='Karen' ,category='Sports & Outdoor', labels='Non-Toxic, Durable',  rating=4.0, brand_name='leanRoots', reviews=250, image_url='https://i.pinimg.com/736x/bd/f4/68/bdf468c0d8281a0764844e7a86eab58f.jpg', features='Compostable')
    prod10 = Product(name='Sustainable Hoodie', description='The Environmental Hoodie is the only hoodie youll need this Earth Day!', price= 35.0, original_price=38.0 , location='Tokyo' ,category='Fashion', labels='Fair Trade, Durable',  rating=3.9, brand_name='Sustaina', reviews=50, image_url='https://i.pinimg.com/736x/40/14/4a/40144a03761c21fefd477ded57ab9f3e.jpg', features='Compostable')
    prod11 = Product(name='Organic Toothbrush', description='Say goodbye to plastic, and hello to sustainable style!', price='47.90', original_price='52.01', location='Karen', category='Home & Garden', labels='Durable',rating='4.7', brand_name='Sustaina', reviews='138', image_url='https://i.pinimg.com/736x/4e/e3/eb/4ee3eba4f2f75cf781bddd7e05b393a3.jpg', features='Organic')
    prod12 = Product(name='Eco Rain Jacket', description='Women and Men Fashion Hooded Rain Poncho and other Trench & Rain', price='28.93', original_price='37.14', location='Lavington', category='Fashion', labels='Fair Trade, Plastic-Free, Carbon Neutral',rating='4.8', brand_name='reenLif', reviews='200', image_url='https://i.pinimg.com/736x/6d/56/15/6d56153e9964fa2b80c4db07ac7ccf0b.jpg', features='Biodegradable')
    prod13 = Product(name='Natural Sunglasses', description=' Polarized Women’s Eyeglass Frame Natural Wood Fashion Sun', price='20.80', original_price='24.90', location='Tokyo', category='Fashion', labels='Carbon Neutral, Durable',rating='3.8', brand_name='CleanRoots', reviews='1000', image_url='https://i.pinimg.com/736x/5f/45/6a/5f456a96288a195f7bbf5102b0413d1e.jpg', features='Zero Waste", "Organic')
    prod14 = Product(name='Sustainable Deodorant', description='Biork crystal deodorant stick is a completely natural and sustainable deodorant. Vegan friendly, made from natural crystal.', price='50.76', original_price='56.90', location='Miami', category='Personal Care', labels='Fair Trade, Recycled',rating='4.2', brand_name='EcoWear Co.', reviews='650', image_url='https://i.pinimg.com/736x/64/cd/3c/64cd3c1b033947826116ed1161e6c734.jpg', features='Vegan')
    prod15 = Product(name='Natural Grocery Bag', description='Eco-Friendly: Unlike traditional bags, our green grocery bags are eco-friendly.', price='60.54', original_price='65.09', location='Texas', category='Home & Garden', labels='Non-Toxic, Plastic-Free"',rating='4.4', brand_name='Verde', reviews='380', image_url='https://i.pinimg.com/736x/1a/67/ea/1a67ea3f5ded8f5eb31b8e4d061af36b.jpg', features='Compostable", "Biodegradable')
    prod16 = Product(name='Eco Candle', description='The Product Our toasted coconut scented candle is divinely decadent, subtle and creamy, providing a relaxing and soothing aroma', price='20.87', original_price='34.90', location='Karen', category='Home & Garden', labels='Fair Trade, Durable',rating='4.8', brand_name='CleanRoots', reviews='20', image_url='https://i.pinimg.com/736x/e5/5d/a4/e55da4ad9ba442647811803cde5b00fb.jpg', features='Zero Waste')
    prod17 = Product(name='Natural Tote Bag', description='Product to always be ready on the go', price='9.95', original_price='12.90', location='Tokyo', category='Personal Care', labels='BPA-Free, Plastic-Free',rating='4.3', brand_name='EcoWear Co.', reviews='400', image_url='https://i.pinimg.com/736x/d3/de/5a/d3de5a72521f16e8fd31ad5abf39a3f9.jpg', features='Compostable')
    prod18 = Product(name='Eco Yoga Mat', description='HAHE POE yoga mat is a truly eco-friendly and odorless option. It is softer, lighter, more flexible and more comfortable than TPE yoga mats.', price='52.67', original_price='56.99', location='Kilimani', category='Sports & Outdoor', labels='Fair Trade, Local',rating='3.9', brand_name='Sustaina', reviews='879', image_url='https://i.pinimg.com/736x/1b/23/00/1b2300155c59830ca96a6d8dc09070ea.jpg', features='Vegan, Zero Waste')
    prod19 = Product(name='Sustainable Socks', description='Wear the best from nature connect with it', price='40.87', original_price='43.87', location='Texas', category='Fashion', labels='Carbon Neutral',rating='4.0', brand_name='Verde', reviews='367', image_url='https://i.pinimg.com/736x/5c/95/51/5c955164be76295ab071f2af88152953.jpg', features='Recycled')
    prod20 = Product(name='Natural Face Cream', description='Its made with almond oil to soften and moisturize the skin. Vitamin E tocopherol adds great antioxidant properties to the formula as well!', price='19.80', original_price='23.09', location='Kilimani', category='Persona Care', labels='Organic, BPA-Free',rating='3.6', brand_name='GreenLife', reviews='98', image_url='https://i.pinimg.com/736x/c2/d8/3c/c2d83cc5ac82206390e89ca7788d3a50.jpg', features='Vegan, Biodegradable')

    db.session.add_all([prod1, prod2, prod3, prod4, prod5, prod6, prod7, prod8, prod9, prod10, prod11, prod12, prod13, prod14, prod15, prod16, prod17, prod18, prod19, prod20])

    print("Products prepared.")

 
    # Seed Community Posts
    # ==================================
    post1 = CommunityPost(title='My Zero-Waste Journey', content='Full content here...', excerpt='It all started with a simple change...', author_id=user1.id)
    post2 = CommunityPost(title='Top 5 Eco-Friendly Swaps for 2024', content='Full content here...', excerpt='Looking to reduce your carbon footprint? Here are five easy swaps...', author_id=user2.id)
    db.session.add_all([post1, post2])
    print("Community Posts prepared.")

    db.session.commit()
    print("Database seeded successfully!")