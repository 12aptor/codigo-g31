from db import db
from sqlalchemy import Integer, String, DECIMAL, DateTime, func, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from enum import Enum

class SaleStatus(str, Enum):
    PENDING = 'PENDING'
    CONFIRMED = 'CONFIRMED'
    CANCELLED = 'CANCELLED'

class Sale(db.Model):
    __tablename__ = 'sales'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True)
    code: Mapped[str] = mapped_column(String(7), nullable=False, unique=True) # B-00001
    total: Mapped[float] = mapped_column(DECIMAL(10,4), nullable=False)
    status: Mapped[str] = mapped_column(SQLEnum(SaleStatus), default=SaleStatus.PENDING, nullable=False) # PENDING, CONFIRMED, CANCELLED
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now())
    customer_id: Mapped[int] = mapped_column(ForeignKey('customers.id'), nullable=False)

    customer = relationship('Customer')
    sale_details = relationship('SaleDetail')


    def to_json(self):
        items = []
        for sale_detail in self.sale_details:
            items.append({
                'id': sale_detail.id,
                'quantity': sale_detail.quantity,
                'price': sale_detail.price,
                'total': sale_detail.total,
                'product': sale_detail.product
            })

        return {
            'id': self.id,
            'code': self.code,
            'total': self.total,
            'status': self.status,
            'created_at': str(self.created_at),
            'customer': {
                'name': self.customer.name,
                'last_name': self.customer.last_name,
                'email': self.customer.email,
                'document_number': self.customer.document_number,
                'address': self.customer.address
            },
            'items': items
        }