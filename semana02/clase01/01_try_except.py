
# Bloque try: Sirve para ejecutar una sección de código
try:
    division = 5/0

# Bloque except: Sirve para capturar una excepción 
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)

# Bloque finally: Se ejecutará siempre al finalizar
finally:
    print("El bloque finally se ejecutó")


print("Hello!! 😛")