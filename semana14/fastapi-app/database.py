from pymongo import AsyncMongoClient
from beanie import init_beanie
from models import Product

MONGO_URI = 'mongodb://localhost:27017'
DATABASE_NAME = 'ecommerce'

async def init_db():
    client = AsyncMongoClient(MONGO_URI)
    await init_beanie(
        database=client[DATABASE_NAME],
        document_models=[Product]
    )