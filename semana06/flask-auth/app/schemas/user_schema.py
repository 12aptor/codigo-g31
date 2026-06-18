from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str
    document_number: str

class LoginSchema(BaseModel):
    email: EmailStr
    password: str