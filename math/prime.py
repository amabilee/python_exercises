def fill():
  soma = 0
  valores = []
  primos = []
  posicao = []
  for i in range(9):
    res = int(input(f"Digite um vetor na posição: {i + 1} "))
    soma += res
    valores.append(res)
    if valores[i] == 2:
      primos.append(res)
      posicao.append(i)
    if valores[i] == 3:
      primos.append(res)
      posicao.append(i)
    if valores[i] % 2 != 0:
      if valores[i] % 3 != 0:
        primos.append(res)
        posicao.append(i)
  return primos, posicao

def main():
  print(fill())

main()