def main():
  nomes_lojas = ["Loja 1", "Loja 2", "Loja 3", "Loja 4", "Loja 5", "Loja 6", "Loja 7", "Loja 8"]
  nomes_produtos = ["Produto 1", "Produto 2", "Produto 3", "Produto 4"]
  precos = [[0 for _ in range(len(nomes_produtos))] for _ in range(len(nomes_lojas))]

  for i in range(len(nomes_lojas)):
    for j in range(len(nomes_produtos)):
      preco = float(input(f"Digite o preço do {nomes_produtos[j]} na {nomes_lojas[i]}: "))
      precos[i][j] = preco

  print("\nRelações produto-loja com preço abaixo de R$ 120,00:")
  for i in range(len(nomes_lojas)):
    for j in range(len(nomes_produtos)):
      if precos[i][j] <= 120.00:
        print(f"{nomes_produtos[j]} - {nomes_lojas[i]} (R${precos[i][j]:.2f})")

main()
