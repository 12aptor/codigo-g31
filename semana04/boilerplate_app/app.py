from pydantic import BaseModel, Field, field_validator, ValidationError
import bcrypt

class User:
    def __init__(self, dni: str, name: str, password: str):
        self.dni = dni
        self.name = name
        self.password = self._hash_password(password)

    def _hash_password(self, password: str) -> str:
        bytes_password = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(bytes_password, salt)
        return hashed_password.decode('utf-8')

class UserSchema(BaseModel):
    dni: str
    name: str
    password: str = Field(min_length=6)

    @field_validator('dni')
    @classmethod
    def validate_dni(cls, value: str) -> str:
        if not value.isdigit():
            raise ValueError('El DNI de contener solo números')
        if len(value) != 8:
            raise ValueError('El DNI debe tener exactamente 8 caracteres')
        return value

def main():
    dni = input("DNI: ")
    name = input("Nombre: ")
    password = input("Contraseña: ")

    try:
        validated_user = UserSchema(dni=dni, name=name, password=password)
        print('\nUsuario creado con éxito')
        user = User(dni=dni, name=name, password=password)
        print(user.dni)
        print(user.name)
        print(user.password)
    except ValidationError as e:
        print('\nError de validacion:')
        print(e.errors()[0]['msg'])

if __name__ == '__main__':
    main()