from flask import request
from flask_restful import Resource
from pydantic import ValidationError
from app.schemas.sale_schema import SaleSchema
from app.models.customer_model import Customer
from app.models.sale_model import Sale
from app.models.sale_detail_model import SaleDetail
from db import db
from app.services.product_service import product_service
from app.services.customer_service import customer_service
from app.services.sale_service import sale_service
from app.services.sale_detail_service import sale_detail_service

class SaleResource(Resource):
    def post(self):
        try:
            data = request.get_json()
            validated_data = SaleSchema.model_validate(data)

            customer = customer_service.get_by_document_number(
                validated_data.customer.document_number
            )

            if not customer:
                customer = customer_service.create(
                    validated_data.customer
                )
                db.session.flush()
            else:
                customer = customer_service.update(
                    validated_data.customer
                )
            
            next_code = 'V-00001'
            last_sale = sale_service.get_last()

            if last_sale:
                code  = last_sale.code
                next_code = 'C-' + str(int(code.split('-')[1]) + 1).zfill(5)

            sale = sale_service.create(
                next_code,
                validated_data.total,
                customer.id
            )
            db.session.flush()

            for item in validated_data.items:
                product = product_service.get_by_id(item.product_id)

                if not product:
                    raise Exception('Product not found')
                
                if product.stock < item.quantity:
                    raise Exception('Not enough stock')
                
                product.stock -= item.quantity

                sale_detail_service.create(
                    item,
                    sale.id
                )

            db.session.commit()

            # Generar la factura electronica

            return {
                'ok': True
            }, 200
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            db.session.rollback()
            return {
                'error': str(e)
            }, 400