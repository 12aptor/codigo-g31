from flask_restful import Resource
from flask import request
from pydantic import ValidationError
from db import db
from app.schemas.product_schema import ProductSchema

class ProductResource(Resource):
    def get(self):
        try:
            pass
        except Exception as e:
            return {
                'error': str(e)
            }, 400

    def post(self):
        try:
            data = request.form
            image = request.files.get('image')

            if not image:
                return {
                    'error': 'Image is required'
                }, 400

            if image.filename == '':
                return {
                    'error': 'Image is required'
                }, 400

            if not image.content_type.startswith('image/'):
                return {
                    'error': 'Invalid image type'
                }, 400
            
            validated_data = ProductSchema.model_validate(data)
            
            return {
                'ok': True
            }
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'error': str(e)
            }, 400