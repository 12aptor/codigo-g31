from flask_restful import Resource
from flask import request
from pydantic import ValidationError
from app.schemas.auth_schema import RegisterSchema
from app.models.user_model import User
from db import db

class LoginResource(Resource):
    pass

class RegisterResource(Resource):
    def post(self):
        try:
            data = request.get_json()
            validated_data = RegisterSchema.model_validate(data)

            user = User.query.filter_by(email=validated_data.email).first()

            if user is not None:
                return {
                    'error': 'Email already exists'
                }, 400

            created_user = User(
                name=validated_data.name,
                last_name=validated_data.last_name,
                email=validated_data.email,
                password=validated_data.password,
                role_id=validated_data.role_id
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