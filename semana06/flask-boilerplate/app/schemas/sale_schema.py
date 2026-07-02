from pydantic import BaseModel
from app.schemas.sale_detail_schema import SaleDetailSchema
from app.schemas.customer_schema import CustomerSchema

class SaleSchema(BaseModel):
    total: float
    customer: CustomerSchema
    items: list[SaleDetailSchema]
