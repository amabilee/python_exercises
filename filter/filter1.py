
nomes_estudantes = ["João Silva", "Maria Souza", "Pedro Santos", "Ana Oliveira", "Luiza Pereira"]
def inverter_nomes(lista_nomes):
    nomes_invertidos = [nome.split()[1] + ", " + nome.split()[0] for nome in lista_nomes]
    return nomes_invertidos
def filtrar_por_letra(lista_nomes, letra):
    nomes_filtrados = [nome for nome in lista_nomes if nome.startswith(letra)]
    return nomes_filtrados

nomes_invertidos = inverter_nomes(nomes_estudantes)
print("Nomes invertidos:", nomes_invertidos)

nomes_com_letra_A = filtrar_por_letra(nomes_estudantes, 'A')
print("Nomes com a letra 'A':", nomes_com_letra_A)
