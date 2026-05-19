"""Crea una aplicacion que busque la palabra ingresada"""

palabras = ["hola", "gato", "python", "rust", "go", "typescript", "perl"]

palabra_ingresada = input("Busca una palabra: ")

se_encontro = False
for palabra in palabras:
    if palabra == palabra_ingresada:
        print(f"Se ha encontrado la palabra {palabra_ingresada}")
        se_encontro = True
        break

if se_encontro == False:
    print("Palabra no encontrada")