"""Crea un progama que determine si un año es
bisiesto. Un año bisiesto es divisible por 4
excepto si es divisible por 100 pero no por 400."""

anio = int(input("Ingrese el año: "))

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")