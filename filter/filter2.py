def ler_dados():
    habitantes = []

    for _ in range(15):
        idade = int(input("Digite a idade do habitante: "))
        sexo = input("Digite o sexo do habitante (M/F): ")
        salario = float(input("Digite o salário do habitante: "))
        filhos = int(input("Digite o número de filhos do habitante: "))

        habitante = {"idade": idade, "sexo": sexo, "salario": salario, "filhos": filhos}
        habitantes.append(habitante)

    return habitantes

def calcular_media_salario(habitantes):
    total_salario = sum(habitante["salario"] for habitante in habitantes)
    media_salario = total_salario / len(habitantes)
    return media_salario

def encontrar_extremos_idade(habitantes):
    idades = [habitante["idade"] for habitante in habitantes]
    menor_idade = min(idades)
    maior_idade = max(idades)
    return menor_idade, maior_idade

def contar_mulheres_tres_filhos_salario(habitantes):
    mulheres_tres_filhos_salario = [habitante for habitante in habitantes
                                     if habitante["sexo"] == "F" and habitante["filhos"] == 3 and habitante["salario"] <= 500.00]
    quantidade = len(mulheres_tres_filhos_salario)
    return quantidade

dados_habitantes = ler_dados()

media_salario = calcular_media_salario(dados_habitantes)
print(f"A média de salário entre os habitantes é: {media_salario}")

menor_idade, maior_idade = encontrar_extremos_idade(dados_habitantes)
print(f"A menor idade do grupo é: {menor_idade}")
print(f"A maior idade do grupo é: {maior_idade}")

quantidade_mulheres_tres_filhos_salario = contar_mulheres_tres_filhos_salario(dados_habitantes)
print(f"A quantidade de mulheres com três filhos que recebem até R$ 500,00 é: {quantidade_mulheres_tres_filhos_salario}")


