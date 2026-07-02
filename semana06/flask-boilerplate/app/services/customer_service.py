from app.models.customer_model import Customer
from app.schemas.customer_schema import CustomerSchema
from db import db

class CustomerService:
    def get_by_document_number(
        self,
        document_number: str
    ) -> Customer | None:
        customer = Customer.query.filter_by(
            document_number=document_number
        ).first()
        return customer
    
    def create(self, data: CustomerSchema) -> Customer:
        customer = Customer(
            name=data.name,
            last_name=data.last_name,
            email=data.email,
            document_number=data.document_number,
            address=data.address
        )
        db.session.add(customer)
        return customer
    
    def update(
        self,
        customer: Customer,
        data: CustomerSchema
    ) -> Customer:
        customer.name=data.name
        customer.last_name=data.last_name
        customer.email=data.email
        customer.address=data.address
        return customer

customer_service = CustomerService()