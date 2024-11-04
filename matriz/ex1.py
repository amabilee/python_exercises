def criarMatriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = int(input(f"digite o valor para a posição [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def multiplicarMatrizes(matriz1, matriz2):
    linhas1 = len(matriz1)
    colunas1 = len(matriz1[0])
    linhas2 = len(matriz2)
    colunas2 = len(matriz2[0])

    if colunas1 != linhas2:
      print("o número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")
      return

    matriz_resultante = []
    for i in range(linhas1):
        linha_resultante = []
        for j in range(colunas2):
            produto = 0
            for k in range(colunas1):
                produto += matriz1[i][k] * matriz2[k][j]
            linha_resultante.append(produto)
        matriz_resultante.append(linha_resultante)

    return matriz_resultante

print("preencha a matriz 4x5:")
matriz_4x5 = criarMatriz(4, 5)

print("\npreencha a matriz 5x2:")
matriz_5x2 = criarMatriz(5, 2)

matriz_4x2 = multiplicarMatrizes(matriz_4x5, matriz_5x2)

print("\nmatriz resultante do produto entre 4x5 e 5x2 (4x2):")
for linha in matriz_4x2:
    print(linha)
