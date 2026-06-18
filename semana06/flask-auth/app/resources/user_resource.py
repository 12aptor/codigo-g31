from flask_restful import Resource
from app.models.user_model import User
from flask import request
from app.schemas.user_schema import UserSchema
from pydantic import ValidationError
from db import db
import bcrypt
from flask_jwt_extended import jwt_required, get_jwt_identity

class UserResource(Resource):
    @jwt_required()
    def get(self):
        try:
            identity = get_jwt_identity()
            users: list[User] = User.query.all()

            users_list = []
            for user in users:
                users_list.append(user.to_json())

            return users_list, 200
        except Exception as e:
            return {
                'error': str(e)
            }, 400

    @jwt_required()
    def post(self):
        try:
            data = request.get_json()
            validated_data = UserSchema.model_validate(data)

            created_user = User(
                name=validated_data.name,
                email=validated_data.email,
                password=self._hash_password(validated_data.password),
                document_number=validated_data.document_number
            )

            db.session.add(created_user)
            db.session.commit()

            return created_user.to_json(), 200
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'error': str(e)
            }, 400
        
    def _hash_password(self, pwd: str) -> str:
        bytes_pwd = pwd.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_pwd = bcrypt.hashpw(bytes_pwd, salt)
        return hashed_pwd.decode('utf-8')