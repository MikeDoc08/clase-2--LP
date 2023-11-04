# Bucle "while" simple:

# contador = 0

# while contador < 5:
#     print(f"Valor del contador: {contador}")
#     contador += 2

# ace = 0
# dec = 11

# while ace < 10:
#     ace += 1
#     dec -= 1
#     print(ace, '/', dec)

import random

aleatoreo = random.randint(1, 100)

adivina = 0

while adivina != aleatoreo:
    if adivina == 0:
        print('Inicia el Juego')
    elif adivina < aleatoreo:
        print('demasiado bajo')
    else:
        print('demasiado alto')
    adivina = int(input('Ingresa el numero'))
print('Haz ganado!')

# Segundo commit