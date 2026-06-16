from flask import Flask
from db import db
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

from app.models import user_model
from app import router