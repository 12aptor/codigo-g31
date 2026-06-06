from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return 'Hola desde Flask 🐍'

# Recibir parameros por la ruta
@app.route("/user/<username>")
def user(username: str):
    return f'Bienvenido {username} 🤠'

# string, int, float, path, uuid
@app.route("/product/<int:product_id>")
def product(product_id: int):
    return f'El ID del producto es {product_id}'

@app.route("/users", methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        return 'Ruta para crear un usuario'
    else:
        return 'Ruta para listar usuarios'

@app.route("/html")
def html():
    return '<button>Dame click!</button>'

@app.route("/json")
def json():
    return {
        'id': 1,
        'name': 'John Doe',
        'email': 'john@gmail.com'
    }

@app.route("/list")
def list():
    return [
        {
            'id': 1,
            'name': 'John Doe',
            'email': 'john@gmail.com'
        },
        {
            'id': 2,
            'name': 'Ana Doe',
            'email': 'ana@gmail.com'
        }
    ]

@app.route('/template')
def template():
    users = [
        {
            'id': 1,
            'name': 'John Doe',
            'email': 'john@gmail.com'
        },
        {
            'id': 2,
            'name': 'Ana Doe',
            'email': 'ana@gmail.com'
        }
    ]
    return render_template('hello.html', users=users, title='Lista de usuarios')


if __name__ == '__main__':
    app.run(debug=True)

"""Retornamos 9:30"""