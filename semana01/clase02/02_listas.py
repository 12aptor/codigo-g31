animales = ["😺", "🐶", "🐷", "🐮", "🐍"]
numeros = [1, 2, 3, 4]
mixtas = [1, True, "Hola"]
anidadas = [[1, 2, 3], [4, 5, 6]]

"""Acceder a un elemento"""
print(animales[3])
print(animales[4])

"""Slicing [inicio:fin - 1:paso]"""
print(animales[1:4])
print(animales[:4])
print(animales[1:])
print(animales[:])

"""Modificamos elementos de una lista"""
animales[2] = "🦆"
print(animales)

"""Concatenar listas"""
nueva_lista = animales + numeros
print(nueva_lista)

"""Obtener la longitud de una lista"""
print(len(animales))