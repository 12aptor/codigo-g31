from flask import request
from flask_restful import Resource
from pydantic import ValidationError
from app.schemas.sale_schema import SaleSchema
from db import db
from app.services.product_service import product_service
from app.services.customer_service import customer_service
from app.services.sale_service import sale_service
from app.services.sale_detail_service import sale_detail_service
import requests
import os
from datetime import datetime

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
                    customer,
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

            items = []
            total_gravada = 0
            total_igv = 0
            total_general = 0

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

                precio_unitario = item.price
                total = precio_unitario * item.quantity
                valor_unitario = precio_unitario / 1.18
                subtotal = total / 1.18
                igv = total - subtotal

                items.append({
                    'unidad_de_medida': 'NIU',
                    'codigo': product.code,
                    'descripcion': product.name,
                    'cantidad': item.quantity,
                    'valor_unitario': valor_unitario,
                    'precio_unitario': precio_unitario,
                    'subtotal': subtotal,
                    'tipo_de_igv': 1,
                    'igv': igv,
                    'total': total,
                    'anticipo_regularizacion': False
                })
                total_gravada += subtotal
                total_igv += igv
                total_general += total

            db.session.commit()

            nubefact_url = os.getenv('NUBEFACT_URL')
            nubefact_token = os.getenv('NUBEFACT_TOKEN')

            payload = {
                'operacion': 'generar_comprobante',
                'tipo_de_comprobante': 2,
                'serie': 'BBB1',
                'numero': sale.id,
                'sunat_transaction': 1,
                'cliente_tipo_de_documento': 1,
                'cliente_numero_de_documento': customer.document_number,
                'cliente_denominacion': f'{customer.name} {customer.last_name}',
                'cliente_direccion': customer.address,
                'cliente_email': customer.email,
                'fecha_de_emision': datetime.now().strftime('%d-%m-%Y'),
                'moneda': 1,
                'porcentaje_de_igv': 18.00,
                'total_gravada': total_gravada,
                'total_igv': total_igv,
                'total': total_general,
                'enviar_automaticamente_a_la_sunat': True,
                'enviar_automaticamente_al_cliente': True,
                'items': items
            }

            response = requests.post(
                url=nubefact_url,
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {nubefact_token}'
                },
                json=payload
            )
            json = response.json()
            status = response.status_code

            if status != 200:
                raise Exception(json['errors'])

            return sale.to_json(), 200
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            db.session.rollback()
            return {
                'error': str(e)
            }, 400
        
    def get(self):
        try:
            sales = sale_service.get_all()

            sales_list = []
            for sale in sales:
                sales_list.append(sale.to_json())

            return sales_list, 200
        except Exception as e:
            return {
                'error': str(e)
            }, 400