from flask_restful import Resource
from pydantic import ValidationError
from flask import request
from app.schemas.user_schema import LoginSchema
from app.models.user_model import User
from flask_jwt_extended import create_access_token, create_refresh_token
import bcrypt

class LoginResource(Resource):
    def post(self):
        try:
            data = request.get_json()
            validated_data = LoginSchema.model_validate(data)

            user = User.query.filter_by(
                email=validated_data.email
            ).first()

            if user is None:
                return {
                    'error': 'User not found'
                }, 401
            
            is_password_valid = self._verify_password(
                user.password,
                validated_data.password
            )

            if not is_password_valid:
                return {
                    'error': 'Passsword incorrect'
                }, 401
            
            access_token = create_access_token(
                identity=str(user.id),
                additional_claims={
                    'name': user.name,
                    'email': user.email,
                    'document_number': user.document_number
                }
            )
            refresh_token = create_refresh_token(
                identity=str(user.id)
            )     

            return {
                'access': access_token,
                'refresh': refresh_token
            }, 200
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'error': str(e)
            }, 400

    def _verify_password(self, hashed_pwd: str, pwd: str) -> bool:
        bytes_hashed_pwd = hashed_pwd.encode('utf-8')
        bytes_pwd = pwd.encode('utf-8')
        return bcrypt.checkpw(bytes_pwd, bytes_hashed_pwd)