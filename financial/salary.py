vendas = int(input("Qual o valor das vendas?"))
if vendas >= 100000:
  salario = vendas * 0.16 + 700
  print(salario)
elif vendas < 100000 and vendas >= 80000:
  salario = vendas * 0.14 + 650
  print(salario)
elif vendas < 80000 and vendas >= 60000:
  salario = vendas * 0.14 + 600
  print(salario)
elif vendas < 60000 and vendas >= 40000:
  salario = vendas * 0.14 + 550
  print(salario)
elif vendas < 40000 and vendas >= 20000:
  salario = vendas * 0.14 + 500
  print(salario)
elif vendas < 20000:
  salario = vendas * 0.14 + 400
  print(salario)
else:
  print("Não foi possivel calcular")