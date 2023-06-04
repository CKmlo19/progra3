import random

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

fila_aleatoria = random.randint(0, len(matriz) - 1)
columna_1 = random.randint(0, len(matriz[fila_aleatoria]) - 1)
columna_2 = random.randint(0, len(matriz[fila_aleatoria]) - 1)

matriz[fila_aleatoria][columna_1], matriz[fila_aleatoria][columna_2] = matriz[fila_aleatoria][columna_2], matriz[fila_aleatoria][columna_1]

print(matriz)