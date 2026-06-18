from db import db
from sqlalchemy import Integer, String, DateTime, Text, Boolean, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(Text, nullable=False)
    document_number: Mapped[str] = mapped_column(String(8), unique=True, nullable=False)
    status: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())
    

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'document_number': self.document_number,
            'status': self.status,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at)
        }