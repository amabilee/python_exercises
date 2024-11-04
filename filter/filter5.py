def main():
  sexo = []
  olhos = []
  cabelo = []
  idade = []
  olhosAndCabelos = 0
  qnt = 0
  valorOlhos= 0
  maiorIdade = 0
  mulheresLouras = 0
  for i in range(1, 5):
    sexo.append(input(f"Digite qual o sexo do habitante {i}: F(mulher) - M(homem)"))
    olhos.append(input(f"Digite qual a cor dos olhos do habitante {i}: (A— azuis; ou C — castanhos)"))
    cabelo.append(input(f"Digite qual a cor dos cabelos do habitante {i}:  (L — louros; P — pretos; ou C — castanhos)"))
    idade.append(int(input(f"Digite qual a idade do habitante {i}: ")))
  for i in range(5):
    if olhos[i] == 'c' or olhos[i] == 'C' :
      if cabelo[i] == 'p' or cabelo[i] == 'P':
        olhosAndCabelos += idade[i]
        qnt += 1
        valorOlhos = olhosAndCabelos/qnt
    if idade[i] >= maiorIdade:
      maiorIdade = idade[i]
    if idade[i] >= 18 and idade[i] <= 35:
      if sexo[i] == 'f' or sexo[i] == 'F':
        if olhos[i] == 'a' or olhos[i] == 'A' :
          if cabelo[i] == 'l' or cabelo[i] == 'L':
            mulheresLouras += 1
    else:
      continue
  print(f"Média de idade das pessoas com olhos castanhos e cabelos pretos -> {valorOlhos}; Maior idade entre os habitantes -> {maiorIdade};  quantidade de indivíduos do sexo feminino com idade entre 18 e 35 anos (inclusive) e que tenham olhos azuis e cabelos louros -> {mulheresLouras}")

main()