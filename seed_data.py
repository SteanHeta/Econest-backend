# seed_data.py

# This file holds the raw data structures that will be used by both
# the seeder and the API routes for mocking.

brands_data = [
    {
        "id": 1,
        "name": "GreenBrush",
        "logo_url": "https://via.placeholder.com/150",
        "slogan": "Leaders in sustainable dental care.",
        "location": "Portland, OR",
        "productCount": 12,
        "rating": 4.9,
        "reviewCount": 512,
        "story": "Founded in 2018, GreenBrush has been a pioneer in creating beautiful, effective, and biodegradable dental care products.",
        "founded": 2018,
        "categories": ["Personal Care", "Zero Waste"],
        "certifications": ["B-Corp", "Vegan", "Cruelty-Free"],
        "sustainabilityPractices": [
            {"name": "Carbon Neutral Shipping", "available": True},
            {"name": "Plastic-Free Packaging", "available": True},
        ]
    },
    # ... add more brand dictionaries here if you have them ...
]

products_data = [
    {
        "id": 1,
        "name": 'Bamboo Toothbrush Set',
        "description": 'A set of 4 biodegradable bamboo toothbrushes.',
        "price": 9.99,
        "originalPrice": 12.99,
        "categoryTag": "Personal Care",
        "brand": "GreenBrush",
        "location": "Portland, OR",
        "imageUrl": "https://i.imgur.com/example-toothbrush.jpg",
        "rating": 4.8,
        "reviewCount": 124,
        "features": ["Biodegradable", "BPA-Free", "Vegan"]
    },
    {
        "id": 2,
        "name": 'Reusable Beeswax Food Wraps',
        "description": 'A sustainable alternative to plastic wrap for keeping food fresh.',
        "price": 14.50,
        "originalPrice": 18.00,
        "categoryTag": "Kitchen",
        "brand": "EcoWrap",
        "location": "Seattle, WA",
        "imageUrl": "https://i.imgur.com/example-wrap.jpg",
        "rating": 4.9,
        "reviewCount": 210,
        "features": ["Organic Cotton", "Reusable", "Plastic-Free"]
    },
    # ... add more product dictionaries here ...
]

community_posts_data = [
    {
        "id": 1,
        "title": 'My Zero-Waste Journey',
        "excerpt": 'It all started with a simple change...',
        "created_at": "2024-06-25T12:00:00Z",
        "author": {"name": "Jane Doe", "avatar": "JD", "tag": "Lifestyle"},
        "likes": 102
    },
    {
        "id": 2,
        "title": 'Top 5 Eco-Friendly Swaps for 2024',
        "excerpt": 'Looking to reduce your carbon footprint? Here are five easy swaps you can make today to live more sustainably.',
        "created_at": "2024-06-24T10:00:00Z",
        "author": {"name": "John Smith", "avatar": "JS", "tag": "Tips"},
        "likes": 230
    },
    # ... add more post dictionaries here ...
]