from pydantic import BaseModel

class SaleDetailSchema(BaseModel):
    quantity: int
    price: float
    total: float
    product_id: int