from beanie import Document
from pydantic import Field
from typing import Optional

class Product(Document):
    name: str
    description: Optional[str] = None
    price: float = Field(gt=0, description='El precio deber ser mayor a 0')
    stock: int = Field(default=0, ge=0)
    is_active: Optional[bool] = True
    tags: list[str]

    class Settings:
        name = "products"