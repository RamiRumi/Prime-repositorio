def ordenar_fila(matriz, fila):
    matriz[fila] = sorted(matriz[fila])

# Matriz de ejemplo
matriz = [
    [3, 1, 2],
    [6, 4, 5],
    [9, 7, 8]
]

print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la segunda fila (índice 1)
fila_a_ordenar = 1
ordenar_fila(matriz, fila_a_ordenar)

print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)