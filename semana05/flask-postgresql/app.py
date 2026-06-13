from flask import Flask, request
from db import create_user_table
from user_resource import UserResource

app = Flask(__name__)

create_user_table()


@app.route('/')
def home():
    return 'Hello Flask 🐍'

@app.route('/users', methods=['GET', 'POST'])
def users():
    method = request.method
    user = UserResource()

    if method == 'GET':
        response = user.list()
        return response
    elif method == 'POST':
        data = request.get_json()
        response = user.create(data)
        return response
    
@app.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_users(user_id: int):
    method = request.method
    user = UserResource()

    if method == 'GET':
        response = user.get_by_id(user_id)
        return response
    elif method == 'PUT':
        data = request.get_json()
        response = user.update(user_id, data)
        return response
    elif method == 'DELETE':
        response = user.delete(user_id)
        return response


if __name__ == '__main__':
    app.run(debug=True)