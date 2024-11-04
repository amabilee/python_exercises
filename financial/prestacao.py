def calcular_prestacoes(valor_total, num_prestacoes):
    if num_prestacoes < 12:
        return "O número mínimo de prestações é 12."

    if num_prestacoes >= 36:
        valor_total += valor_total * 0.15
    elif num_prestacoes >= 24:
        valor_total += valor_total * 0.10

    valor_prestacao = valor_total / num_prestacoes
    return valor_prestacao
valor_total = float(input("Digite o valor total em reais: "))
num_prestacoes = int(input("Digite o número de prestações desejadas: "))

valor_prestacao = calcular_prestacoes(valor_total, num_prestacoes)
print("O valor de cada prestação é:", valor_prestacao)