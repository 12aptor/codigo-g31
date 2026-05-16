edad = 20

if edad >= 18:
    print("El usuario es mayor de edad")
else:
    print("El usuario es menor de edad")


calificacion = 10

if calificacion >= 18:
    print("Excelente")
elif calificacion >= 14:
    print("Es buena")
elif calificacion >= 12:
    print("Aprobado")
else:
    print("Desaprobado")


tiene_licencia = False

if edad >= 18 and tiene_licencia:
    print("Puede conducir")

if edad >= 18 or tiene_licencia:
    print("Puede conducir")

fin_de_semana = False

if not fin_de_semana:
    print("Aún no es finde")

""" Anidar conficionales """

edad = 25
tiene_dinero = False

if edad >= 18:
    if tiene_dinero:
        print("Puede viajar")
