from fastapi import FastAPI, status
from database import init_db
from contextlib import asynccontextmanager
from models import Product


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(title="API FastAPI + MongoDB", lifespan=lifespan)

@app.post("/products", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(product: Product):
    await product.insert()
    return product
