from flask_restful import Api
from app import app
from app.resources.auth_resource import *
from app.resources.role_resource import *
from app.resources.product_resource import *
from app.resources.category_resource import *
from app.resources.sale_resource import *

api = Api(app, prefix='/api/v1')

api.add_resource(RegisterResource, '/auth/register')
api.add_resource(LoginResource, '/auth/login')

api.add_resource(RoleResource, '/roles')
api.add_resource(ManageRoleResource, '/roles/<int:role_id>')

api.add_resource(ProductResource, '/products')
api.add_resource(ManageProductResource, '/products/<int:product_id>')

api.add_resource(CategoryResource, '/categories')
api.add_resource(ManageCategoryResource, '/categories/<int:category_id>')

api.add_resource(SaleResource, '/sales')