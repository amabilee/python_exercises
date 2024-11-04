def eh_simetrica(matriz):
    n = len(matriz)
    if n != len(matriz[0]):
        return False
    for i in range(n):
        for j in range(i + 1, n):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True
matriz_simetrica = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
matriz_assimetrica = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(f"Matriz simétrica: {eh_simetrica(matriz_simetrica)}")
print(f"Matriz assimétrica: {eh_simetrica(matriz_assimetrica)}")
