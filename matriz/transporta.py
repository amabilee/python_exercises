def obter_transposta(matriz):
    transposta = [
        [matriz[j][i] for j in range(len(matriz))]
        for i in range(len(matriz[0]))
    ]
    return transposta
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposta = obter_transposta(matriz)
for linha in transposta:
    print(linha)
