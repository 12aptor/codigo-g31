from app.models.product_model import Product
from app.schemas.product_schema import ProductSchema
from db import db

class ProductService:
    def get_all(self) -> list[Product]:
        products = Product.query.filter_by(is_active=True)
        return products

    def get_last(self) -> Product | None:
        product = Product.query.order_by(
            Product.id.desc()
        ).first()
        return product

    def create(
            self,
            data: ProductSchema,
            code: str,
            image: str
    ) -> Product:
        product = Product(
            name=data.name,
            code=code,
            description=data.description,
            image=image,
            brand=data.brand,
            size=data.size,
            price=data.price,
            stock=data.stock,
            category_id=data.category_id
        )
        db.session.add(product)
        db.session.commit()
        return product
    
    def update(
            self,
            product: Product,
            data: ProductSchema,
            image: str | None = None
        ) -> Product:
        if image:
            product.image = image
        product.name = data.name
        product.description = data.description
        product.brand = data.brand
        product.size = data.size
        product.price = data.price
        product.stock = data.stock
        product.category_id = data.category_id
        db.session.commit()
        return product

    def get_by_id(self, id: int) -> Product | None:
        product = Product.query.filter_by(
            id=id,
            is_active=True
        ).first()
        return product

    def delete(self, product: Product) -> None:
        product.is_active = False
        db.session.commit()
        return None

product_service = ProductService()