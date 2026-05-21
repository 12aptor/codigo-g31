"""Crear una aplicacion para gestionar usuarios.
CRUD (Create, Read, Update, Delete) para esto usaremos
como identificador el DNI del usuario."""

import os
import subprocess

usuarios = {
    '78787878': {
        'nombre': 'John Doe',
        'email': 'john@gmail.com'
    }
}

def buscar_usuario(dni):
    return usuarios.get(dni)

def crear_usuario(dni, nombre, email):
    if dni in usuarios:
        return False
    
    usuarios[dni] = {
        'nombre': nombre,
        'email': email
    }
    return True

def actualizar_usuario(usuario, nombre, email):
    usuario['nombre'] = nombre
    usuario['email'] = email

def pedir_dni():
    dni = input("Ingrese el DNI: ")
    if not dni:
        print("El número de DNI es incorrecto")
        return None
    if not len(dni) == 8:
        print("El número de DNI debe tener 8 caracteres")
        return None
    return dni

def pedir_datos():
    nombre = input("Ingrese nombre: ")
    if not nombre:
        print("El nombre es incorrecto")
        return None

    email = input("Ingrese email: ")
    if not email:
        print("El email es incorrecto")
        return None
    
    return nombre, email

def pausar():
    input("\nPresione enter para continuar...")


while True:
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)

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
            dni = pedir_dni()
            if not dni:
                pausar()
                continue
            usuario = buscar_usuario(dni)
            if not usuario:
                print(f"Usuario {dni} no encontrado")
            else:
                print("\n--- Datos del usuario ---")
                print(f"Nombre: {usuario['nombre']}")
                print(f"Correo: {usuario['email']}")
                print("--------------------------")
            pausar()
        case "2":
            dni = pedir_dni()
            if not dni:
                pausar()
                continue
            nombre, email = pedir_datos()

            if crear_usuario(dni, nombre, email):
                print("\n✅ Usuario creado exitosamente.")
            else:
                print("\n❌ Error: El dni ya ha sido registrado en el sistema")
            pausar()
        case "3":
            dni = pedir_dni()
            if not dni:
                pausar()
                continue
            usuario = buscar_usuario(dni)
            if not usuario:
                print(f"Usuario {dni} no encontrado")
            else:
                nombre, email = pedir_datos()
                actualizar_usuario(usuario, nombre, email)
                print("\n✅ Usuario actualizado exitosamente.")
                pausar()

        case "4":
            dni = pedir_dni()
            if not dni:
                pausar()
                continue
            usuario = buscar_usuario(dni)
            if not usuario:
                print(f"Usuario {dni} no encontrado")
            else:
                del usuarios[dni]
                print("\n✅ Usuario eliminado exitosamente.")
            pausar()
        case "5":
            print("\nSaliendo de la aplicacion... ¡Hasta luego!")
            break
        case _:
            print("\n❌ Opción no válida. Por favor, intente nuevamente.")
            pausar()