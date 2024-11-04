def maior_elemento(matriz):
  maior_elemento = -2147483647
  for linha in matriz:
    for elemento in linha:
      if elemento > maior_elemento:
        maior_elemento = elemento
  return maior_elemento

def multiplica_por_maior(matriz, maior_elemento):
  matriz_resultante = []
  for linha in matriz:
    linha_resultante = []
    for elemento in linha:
      elemento_multiplicado = elemento * maior_elemento
      linha_resultante.append(elemento_multiplicado)
    matriz_resultante.append(linha_resultante)
  return matriz_resultante

def main():
  matriz_m = []
  for i in range(2):
    linha = []
    for j in range(2):
      valor = int(input(f"Digite o elemento M[{i},{j}]: "))
      linha.append(valor)
    matriz_m.append(linha)

  maior_elemento_m = maior_elemento(matriz_m)
  matriz_r = multiplica_por_maior(matriz_m, maior_elemento_m)
  print("\nMatriz R:")
  for linha in matriz_r:
    for elemento in linha:
      print(f"{elemento}", end=" ")
    print()

main()