"""Crea una calculadora de operaciones aritmeticas
(+, -, *, /). El programa debe pedir al usuario que
ingrese dos números, el tipo de operacion y luego
mostrar el resultado de la operación."""


print("""CALCULADORA 🐍
Ingresa dos números y luego la operación
(+, -, *, /)""")
num_1 = float(input("Primer número: "))
num_2 = float(input("Segundo número: "))
operacion = input("Operación: ")

if operacion == "+":
    resultado = num_1 + num_2
elif operacion == "-":
    resultado = num_1 - num_2
elif operacion == "*":
    resultado = num_1 * num_2
elif operacion == "/":
    resultado = num_1 / num_2
else:
    print("Operación incorrecta")

print(f"El resultado es: {resultado}")