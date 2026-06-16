from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from sqlalchemy import DateTime, Text, func, select, Boolean
from sqlalchemy.orm import Mapped, mapped_column, Session
from datetime import datetime
from flask_migrate import Migrate

load_dotenv()

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    status: Mapped[bool] = mapped_column(Boolean, default=True)

@app.route("/")
def home():
    return 'Hello from Flask 🖐️'

@app.route("/users", methods=['GET', 'POST'])
def users():
    method = request.method

    if method == 'POST':
        data = request.get_json()
        user = User(
            name=data['name'],
            email=data['email'],
            password=data['password']
        )
        db.session.add(user)
        db.session.commit()

        return jsonify({
            'message': 'User created successfully'
        }), 200
    elif method == 'GET':
        users = User.query.all()
        
        formated_users = []
        for user in users:
            formated_users.append({
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'created_at': str(user.created_at)
            })
        return jsonify(formated_users), 200

if __name__ == '__main__':
    app.run(debug=True)