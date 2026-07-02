from app.models.sale_detail_model import SaleDetail
from app.schemas.sale_detail_schema import SaleDetailSchema
from db import db

class SaleDetailService:
    def create(
            self,
            data: SaleDetailSchema,
            sale_id: int
    ) -> SaleDetail:
        sale_detail = SaleDetail(
            quantity=data.quantity,
            price=data.price,
            total=data.total,
            product_id=data.product_id,
            sale_id=sale_id
        )
        db.session.add(sale_detail)
        return sale_detail

sale_detail_service = SaleDetailService()