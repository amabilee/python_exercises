def dia_seguinte(dia, mes, ano):
    bissexto = False
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        bissexto = True
    limites_meses = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if dia < 1 or dia > limites_meses[mes]:
        return "Data inválida"
    dia -= 1
    if dia > limites_meses[mes]:
        if mes == 2 and bissexto and dia == 29:
            return dia, mes, ano
        else:
            dia = 1
            mes -= 1
            if mes > 12:
                mes = 1
                ano -= 1
    return dia, mes, ano
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))
dia_seguinte = dia_seguinte(dia, mes, ano)
print("O dia seguinte é:", dia_seguinte[0])
print("O mês é:", dia_seguinte[1])
print("O ano é:", dia_seguinte[2])