from pydantic import BaseModel, EmailStr

class CustomerSchema(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    document_number: str
    address: str