animales = ["😺", "🐶", "🐷", "🐮", "🐍"]
numeros = [4, 3, 6, 7, 1]

"""Añadir elementos a una lista"""
animales.append("🐬")
print(animales)

animales.insert(2, "🦤")
print(animales)

animales.extend(["🐝", "🐴"])
print(animales)

"""Eliminar elementos de una lista"""
animales.remove("🐝")
print(animales)

animales.pop(1)
print(animales)

del animales[-1]
print(animales)

"""Ordenar listas"""
numeros_ordenados = sorted(numeros)
print(numeros_ordenados)

numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)

"""Contar elementos de una lista"""
print(numeros.count(1))