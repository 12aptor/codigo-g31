from time import sleep

contador = 0
# while True:
#     print(contador)
#     contador = contador + 1
#     sleep(1)
    
# while contador < 5:
#     print(contador)
#     contador += 1
#     sleep(1)

# while True:
#     if contador == 5:
#         break
#     print(contador)
#     contador += 1
#     sleep(1)

while True:
    contador += 1
    if contador == 5:
        continue
    print(contador)
    sleep(1)