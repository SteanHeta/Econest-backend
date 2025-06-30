## Econest Backend
This repository contains the backend services for the Econest application.

## Problem Statement
Consumers want to support eco-friendly and local brands but struggle to find trustworthy, transparent, and easily accessible sources. Existing online marketplaces often lack a focus on sustainability, local products, and community engagement, making it challenging for environmentally conscious consumers to make informed shopping choices and connect with sustainable brands.

## Solution
Econest provides a centralized, Eco-friendly Marketplace to list products from local and sustainable brands. User reviews and ratings enable users to evaluate products based on their sustainability and quality. Community tips and articles allow users to share tips, articles, and experiences about sustainable shopping practices. Wishlists and shopping lists enable users to curate lists that promote mindful shopping. Brand profiles provide detailed pages for brands highlighting their eco-certifications and sustainability practices.


## Technologies Used
Language: Python
Framework: Flask
Database: PostgreSQL
Authentication: JWT tokens, social login integration
API Documentation: Swagger UI
Hosting & Deployment: GitHub Actions for CI/CD, 

## Prerequisites
Before you begin, ensure you have the following installed:
Python: v3.8+ (or specify your actual version)
pip: (Python package installer)
PostgreSQL: PostgreSQL installed and running, or access to a PostgreSQL database.
Installation
Clone the repository:
```
git clone https://github.com/SteanHeta/Econest-backend.git
cd Econest-backend
```
Create and activate a virtual environment:
```
python3 -m venv venv
source venv/bin/activate # On Windows: .\venv\Scripts\activate
```
Install dependencies:
```
pip install -r requirements.txt
```
(If requirements.txt does not exist, you might need to create it by running pip freeze > requirements.txt after installing dependencies manually, or install them one by one).

## Set up environment variables:
Create a .env file in the root of the backend directory and add the necessary environment variables.
Example .env (adjust for your specific setup):

FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL="postgresql://user:password@localhost:5432/econest_db" # Your PostgreSQL connection string
SECRET_KEY="your_super_secret_key" 
JWT_SECRET_KEY="your_jwt_secret_key" 

## Running the Application
To start the backend server in development mode:
```
flask run # or python app.py (if your app.py contains a run command)
```
The server will typically run on http://localhost:5001 (or the port specified in your Flask configuration).

## Configuration
All major configurations are managed via environment variables in the .env file. Refer to the config.py (or similar) file for how these variables are loaded and used within the application.

## API Endpoints (Example)
Here's a high-level overview of common API endpoints. Detailed API documentation (e.g., Swagger UI) would be available at a /swagger or /docs endpoint once the server is running.

## Testing
To run the automated tests for the backend:
```
pytest # or flask test (if configured)
```
## Deployment
This backend service can be deployed to various cloud platforms. A common choice for Flask applications is:
Render: Configure as a "Web Service" with the appropriate build and start commands.

## Contributing
Contributions are welcome! Please follow these steps:
Fork the repository.
Create a new branch (git checkout -b feature/your-feature-name).
Make your changes.
Commit your changes (git commit -m 'feat: Add new feature X').
Push to the branch (git push origin feature/your-feature-name).
Open a Pull Request.

## License
[License](./License)