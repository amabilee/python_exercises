def somar(v):
  tam = len(v)
  soma = 0
  for i in range(tam):
    soma += v[i]
  return soma

def main():
  vetores = []
  qnt = int(input("Serão quantos vetores? "))
  for i in range(qnt):
    vetores.append(int(input(f"Vetor {i+1} ")))
  print(somar(vetores))


main()