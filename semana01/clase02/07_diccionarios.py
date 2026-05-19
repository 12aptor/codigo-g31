usuario = {
    "nombre": "John Doe",
    "email": "john@gmail.com",
    "edad": 25,
    "es_programador": True,
    "lenguajes": ["Python", "Rust", "Go", "C#"]
}


"""Accedemos a los elementos"""
print(usuario['nombre'])
print(usuario['lenguajes'])

"""Modificar los elementos"""
usuario['nombre'] = 'Ana Doe'
print(usuario)

"""Eliminar los elementos"""
del usuario["nombre"]
usuario.pop("edad")
print(usuario)

"""Métodos útiles"""
print(usuario.keys())
print(usuario.values())
print(usuario.items())

for clave, valor in usuario.items():
    print(clave, valor)