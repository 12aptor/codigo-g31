from pydantic import BaseModel, Field, field_validator, ValidationError
import bcrypt
import psycopg2
import sys

def get_db_connection():
    conn = psycopg2.connect(
        dbname='boilerplate-app',
        user='postgres',
        password='root',
        host='localhost',
        port='5432'
    )
    return conn

def create_user_table():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                dni VARCHAR(8) UNIQUE NOT NULL,
                name VARCHAR(255) NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()
        cursor.close()
        conn.close()
        print('Tabla usuarios creada exitosamente')
    except Exception as e:
        print(f'Error al crear la tabla: {e}')

class User:
    def _hash_password(self, password: str) -> str:
        bytes_password = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(bytes_password, salt)
        return hashed_password.decode('utf-8')
    
    def _check_password(self, password: str, hashed_password_db: str):
        bytes_password = password.encode('utf-8')
        bytes_hashed_password_db = hashed_password_db.encode('utf-8')
        return bcrypt.checkpw(bytes_password, bytes_hashed_password_db)
    
    def create(self, dni: str, name: str, password: str):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO users (dni, name, password) VALUES (%s, %s, %s)',
            (dni, name, self._hash_password(password))
        )
        conn.commit()
        cursor.close()
        conn.close()
        print('\nUsuario creado exitosamente')

    def login(self, dni: str, password: str):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'SELECT dni, name, password FROM users WHERE dni=%s',
            (dni,)
        )
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            hashed_password_db = user[2]
            password_correct = self._check_password(password, hashed_password_db)

            if password_correct:
                print('\nUsuario autenticado exitosamente')
                return
            print('\nContraseña incorrecta')
            return
        
        print(f'\nNo se encontro un usuario con el DNI: {dni}')


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
    
class LoginSchema(BaseModel):
    dni: str
    password: str

def main():
    args = sys.argv
    user = User()

    if len(args) < 2:
        print('Se requiere un argumento, los argumentos disponibles son: --login --create')
        return

    if '--login' in args:
        dni = input("DNI: ")
        password = input("Contraseña: ")

        try:
            validated_user = LoginSchema(
                dni=dni,
                password=password
            )
            user.login(
                dni=validated_user.dni,
                password=validated_user.password
            )
        except ValidationError as e:
            print('\nError de validacion:')
            print(e.errors()[0]['msg'])
        except Exception as e:
            print(f'\nHubo un error: {e}')
        
    elif '--create' in args:
        dni = input("DNI: ")
        name = input("Nombre: ")
        password = input("Contraseña: ")

        try:
            validated_user = UserSchema(
                dni=dni,
                name=name,
                password=password
            )
            user.create(
                dni=validated_user.dni,
                name=validated_user.name,
                password=validated_user.password
            )
        except ValidationError as e:
            print('\nError de validacion:')
            print(e.errors()[0]['msg'])
        except Exception as e:
            print(f'\nHubo un error: {e}')
    else:
        print('Argumento incorrecto, los argumentos disponibles son: --login --create')

if __name__ == '__main__':
    create_user_table()
    main()