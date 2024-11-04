def determinante_3x3(matriz):
    if len(matriz) != 3 or len(matriz[0]) != 3:
        raise ValueError("A matriz deve ser 3x3")

    determinante = (
        matriz[0][0] * (matriz[1][1] * matriz[2][2] - matriz[1][2] * matriz[2][1]) -
        matriz[0][1] * (matriz[1][0] * matriz[2][2] - matriz[1][2] * matriz[2][0]) +
        matriz[0][2] * (matriz[1][0] * matriz[2][1] - matriz[1][1] * matriz[2][0])
    )
    return determinante
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
determinante = determinante_3x3(matriz)
print(f"Determinante da matriz: {determinante}")
