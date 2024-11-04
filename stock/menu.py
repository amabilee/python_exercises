estoque = {}
while True:
    print("Sistema de Gerenciamento de Estoque")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Visualizar estoque")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        produto = input("Nome do produto a ser adicionado: ")
        quantidade = int(input("Quantidade a ser adicionada: "))
        if produto in estoque:
            estoque[produto] += quantidade
        else:
            estoque[produto] = quantidade
        print(f"{quantidade} unidades de {produto} adicionadas ao estoque.")

    elif opcao == "2":
        produto = input("Nome do produto a ser removido: ")
        if produto in estoque:
            quantidade = int(input(f"Quantidade a ser removida (atualmente em estoque: {estoque[produto]}): "))
            if quantidade <= estoque[produto]:
                estoque[produto] -= quantidade
                print(f"{quantidade} unidades de {produto} removidas do estoque.")
            else:
                print(f"Quantidade insuficiente de {produto} em estoque.")
        else:
            print(f"{produto} não encontrado no estoque.")

    elif opcao == "3":
        print("Estoque Atual:")
        for produto, quantidade in estoque.items():
            print(f"{produto}: {quantidade} unidades")

    elif opcao == "4":
        print("Saindo do sistema.")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
