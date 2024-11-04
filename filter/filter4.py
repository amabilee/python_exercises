ra = input("Qual o numero da matricula? [5 digitos]")
generoFinal = ""
cursoFinal = ""
if len(ra) < 5 or len(ra) > 5:
  print("A matricula deve ter 5 digitos")
else:
  nome = input("Qual o nome completo do aluno? ")
  genero = int(input("Qual o genero do aluno? Opções: 1-[M] ou 2-[F]"))
  if genero >= 3 or genero <= 0:
    print("O genero deve ser 1 ou 2")
  else:
    curso = int(input("Qual o curso do aluno? Opções: 1-[BES], 2-[BEC] ou 3-[ADS]"))
    if curso >= 4 or curso <= 0:
      print("O curso deve ser 1-[BES], 2-[BEC] ou 3-[ADS]")
    else:
      rendimento = int(input("Qual o coeficiente de rendimento do aluno?"))
      if rendimento <= -1 or rendimento >= 101:
        print("O coeficiente de rendimento deve ser maior ou igual a zero e menor ou igual a 100")
      else:
        if genero == 1:
          generoFinal = "Masculino"
        else:
          generoFinal = "Feminino"
        if curso == 1:
          cursoFinal = "Bacharelado em Engenharia de Software"
        elif curso == 2:
          cursoFinal = "Bacharelado em Engenharia de Computação"
        else:
          cursoFinal = "Analise e Desenvolvimento de Sistemas"
        print("RA:",ra, "NOME", nome, "GENERO", generoFinal, "CURSO", cursoFinal, "RENDIMENTO", rendimento)

