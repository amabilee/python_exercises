def cria_produto():
    codigo = int(input("Digite o código do produto: "))
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    return {"codigo": codigo, "preco": preco, "quantidade": quantidade}

def mostra_produto(produto):
    print(f"Código: {produto['codigo']}")
    print(f"Preço: R$ {produto['preco']:.2f}")
    print(f"Quantidade: {produto['quantidade']}")

def busca_produto(codigo):
    if os.path.exists("Produtos"):
        with open("Produtos", "r") as arquivo:
            produtos = []
            for linha in arquivo:
                produtos.append(eval(linha))

            for produto in produtos:
                if produto["codigo"] == codigo:
                    return produto

    return None

def mostra_relatorio(produtos):
    total_quantidade = 0
    total_valor = 0
    for produto in produtos:
        mostra_produto(produto)
        total_quantidade += produto["quantidade"]
        total_valor += produto["preco"] * produto["quantidade"]
    print("\nTotal em estoque:")
    print(f"Quantidade: {total_quantidade}")
    print(f"Valor: R$ {total_valor:.2f}")

estoque = []

while True:
    print("\nMenu:")
    print("1. Cadastrar produto")
    print("2. Buscar produto")
    print("3. Mostrar relatório")
    print("4. Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        novo_produto = cria_produto()
        estoque.append(novo_produto)

        with open("Produtos", "a") as arquivo:
            arquivo.write(str(novo_produto) + "\n")

    elif opcao == 2:
        codigo_busca = int(input("Digite o código do produto a buscar: "))
        produto_encontrado = busca_produto(codigo_busca)

        if produto_encontrado:
            mostra_produto(produto_encontrado)
        else:
            print("Produto não encontrado.")

    elif opcao == 3:
        mostra_relatorio(estoque)

    elif opcao == 4:
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")
