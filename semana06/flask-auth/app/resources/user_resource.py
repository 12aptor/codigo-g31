from flask_restful import Resource
from app.models.user_model import User
from flask import request

class UserResource(Resource):
    def get(self):
        try:
            users: list[User] = User.query.all()

            users_list = []
            for user in users:
                users_list.append(user.to_json())

            return users_list, 200
        except Exception as e:
            return {
                'error': str(e)
            }, 400

    def post(self):
        pass