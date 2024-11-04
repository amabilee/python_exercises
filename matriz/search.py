def localizar_valor(matriz, valor_procurado):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if matriz[linha][coluna] == valor_procurado:
                return linha, coluna
    return None
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
resultado = localizar_valor(matriz, 5)
if resultado:
    print(f"Valor encontrado na linha {resultado[0] + 1} e coluna {resultado[1] + 1}")
else:
    print("Valor não encontrado")
