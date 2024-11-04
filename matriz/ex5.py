def main():
  matriz = [[0.0 for _ in range(7)] for _ in range(4)]

  for i in range(4):
    for j in range(7):
      matriz[i][j] = float(input(f"Digite o elemento[{i + 1},{j + 1}]: "))

  menor_elemento = matriz[0][0]
  posicao_menor = (0, 0)

  for i in range(4):
    for j in range(7):
      if matriz[i][j] < menor_elemento:
        menor_elemento = matriz[i][j]
        posicao_menor = (i, j)

  linha_menor = posicao_menor[0]
  coluna_menor = posicao_menor[1]
  maior_elemento_linha_menor = matriz[linha_menor][0]

  for j in range(1, 7):
    if matriz[linha_menor][j] > maior_elemento_linha_menor:
      maior_elemento_linha_menor = matriz[linha_menor][j]

  minmax = maior_elemento_linha_menor
  print(f"\nMINMAX: {minmax}")
  print(f"Posição: linha {linha_menor + 1}, coluna {coluna_menor + 1}")

main()
