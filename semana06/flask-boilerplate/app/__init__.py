from flask import Flask
from db import db
from config import Config
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

from app.models import (
    category_model,
    customer_model,
    product_model,
    role_model,
    sale_details_model,
    sale_model,
    user_model
)

from app import router