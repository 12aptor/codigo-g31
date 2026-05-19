def saludar():
    print("¡Hola 🤠!")

saludar()

def sumar(a, b):
    return a + b

resultado = sumar(1, 2)
print(resultado)

def saludar(nombre="Invitado"):
    print(f"¡Hola, {nombre}!")

saludar()
saludar("Eduardo")

def mostrar_numeros(*numeros):
    for numero in numeros:
        print(numero)

mostrar_numeros(1, 2, 3, 4, 5)

def mostrar_info(**info):
    for clave, valor in info.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="John Doe", edad=25, email="john@gmail.com")

def funcion_1():
    def funcion_2():
        pass
    funcion_2()
funcion_1()