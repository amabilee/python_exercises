def mesclar_maiores(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        raise ValueError("As matrizes devem ter o mesmo tamanho")
    matriz_combinada = [
        [
            max(matriz1[i][j], matriz2[i][j])
            for j in range(len(matriz1[0]))
        ]
        for i in range(len(matriz1))
    ]
    return matriz_combinada
matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz2 = [[2, 4, 6], [3, 5, 7], [1, 0, 8]]
matriz_resultado = mesclar_maiores(matriz1, matriz2)
for linha in matriz_resultado:
    print(linha)
