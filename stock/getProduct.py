estoque = []

def buscaProduto(codigo):
    for produto in estoque:
        if produto['codigo'] == codigo:
            return produto
    return None

def criarProduto(codigo, preco, quantidade):
    return {"codigo": codigo, "preco": preco, "quantidade": quantidade}

def mostraProduto(produto):
    print(f"Código: {produto['codigo']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")

for i in range(10):
    codigo = input("Digite o código do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    produto = criarProduto(codigo, preco, quantidade)
    estoque.append(produto)

totalItens = sum([produto['quantidade'] for produto in estoque])
valorTotal = sum([produto['preco'] * produto['quantidade'] for produto in estoque])

print(f"Quantidade total de itens: {totalItens}")
print(f"Valor total do estoque: {valorTotal}")

for produto in estoque:
    mostraProduto(produto)

codigo = input("Digite o código do produto que deseja buscar: ")
produto = buscaProduto(codigo)
if produto:
    mostraProduto(produto)
else:
    print("Produto não encontrado.")