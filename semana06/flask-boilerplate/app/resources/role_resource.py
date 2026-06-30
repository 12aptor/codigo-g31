from flask_restful import Resource
from flask import request
from pydantic import ValidationError
from db import db
from app.schemas.role_schema import RoleSchema
from app.services.role_service import role_service
from flask_jwt_extended import jwt_required

class RoleResource(Resource):
    @jwt_required()
    def get(self):
        try:
            roles = role_service.get_all()

            roles_list = [rol.to_json() for rol in roles]

            return roles_list, 200        
        except Exception as e:
            return {
                'error': str(e)
            }, 400
    
    @jwt_required()
    def post(self):
        try:
            data = request.get_json()
            validated_data = RoleSchema.model_validate(data)

            role = role_service.create(validated_data)

            return role.to_json(), 200
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'error': str(e)
            }, 400
        
class ManageRoleResource(Resource):
    @jwt_required()
    def get(self, role_id: int):
        try:
            role = role_service.get_by_id(role_id)

            if not role:
                return {
                    'error': 'Role not found'
                }, 404
            
            return role.to_json(), 200
        except Exception as e:
            return {
                'error': str(e)
            }, 400

    @jwt_required()
    def put(self, role_id: int):
        try:
            role = role_service.get_by_id(role_id)

            if not role:
                return {
                    'error': 'Role not found'
                }, 404
            
            data = request.get_json()
            validated_data = RoleSchema.model_validate(data)
            
            updated_role = role_service.update(role, validated_data)

            return updated_role.to_json(), 200
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'error': str(e)
            }, 400

    @jwt_required()
    def delete(self, role_id: int):
        try:
            role = role_service.get_by_id(role_id)

            if not role:
                return {
                    'error': 'Role not found'
                }, 404
            
            role_service.delete(role)

            return None, 200
        except Exception as e:
            return {
                'error'
            }, 400