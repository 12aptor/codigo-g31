"""Crear una aplicacion para gestionar usuarios.
CRUD (Create, Read, Update, Delete) para esto usaremos
como identificador el DNI del usuario."""

import os

usuarios = {
    '78787878': {
        'nombre': 'John Doe',
        'email': 'john@gmail.com'
    }
}

def buscar_usuario(dni):
    return usuarios[dni]

def crear_usuario():
    pass

def actualizar_usuario():
    pass

def eliminar_usuario():
    pass


while True:
    os.system("clear")
    print("""
    ================================
          GESTIÓN DE USUARIOS
    ================================
          [1] Buscar usuario
          [2] Agregar usuario
          [3] Actualizar usuario
          [4] Eliminar usuario
          [5] Salir
    """)
    opcion = input("Elija una opción: ")

    match opcion:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case _:
            pass