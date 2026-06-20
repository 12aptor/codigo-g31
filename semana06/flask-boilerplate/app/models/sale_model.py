from db import db
from sqlalchemy import Integer, String, DECIMAL, DateTime, func, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column
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