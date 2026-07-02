from app.models.sale_model import Sale
from db import db

class SaleService:
    def get_last(self) -> Sale | None:
        sale = Sale.query.order_by(
            Sale.id.desc()
        ).first()
        return sale
    
    def create(
        self,
        code: str,
        total: float,
        customer_id: int
    ) -> Sale:
        sale = Sale(
            code=code,
            total=total,
            customer_id=customer_id
        )
        db.session.add(sale)
        return sale

sale_service = SaleService()