maior_altura = 0
menor_altura = 999999
soma_altura = 0
quantidade = 15
while True:
  altura = int(input("Digite a altura"))
  soma_altura +=  altura
  if altura > maior_altura:
    maior_altura =  altura
  if altura < menor_altura:
    menor_altura = altura
  if quantidade == 0:
    break
  quantidade -= 1
media_altura = soma_altura/15
print("A media das alturas lidas é {}".format(media_altura))
print("A maior altura é {}".format(maior_altura))
print("A menor altura é {}".format(menor_altura))
