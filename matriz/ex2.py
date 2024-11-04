def matriz():
    mat = []
    for i in range(10):
        lin = []
        for j in range(5):
            dado = float(input(f"Insira um valor na posição ({i}, {j}): "))
            lin.append(dado)
        mat.append(lin)
    return mat

def calculo(matriz):
    soma = 0
    for i in range(6, 10):
        for j in range(5):
            soma += matriz[i][j]
    return soma

def main():
    m = matriz()
    sm = calculo(m)
    print("A soma dos elementos é:", sm)

main()