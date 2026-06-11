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
def manage_users():
    method = request.method
    user = UserResource()

    if method == 'GET':
        pass
    elif method == 'PUT':
        pass
    elif method == 'DELETE':
        pass


if __name__ == '__main__':
    app.run(debug=True)