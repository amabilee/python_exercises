ano = int(input("Digite o ano: "))
def verifyYear(ano):
  if (ano % 2 == 0 and ano % 4 == 0):
    if (ano % 100 == 0 and ano % 400 != 0):
      print(f"O ano {ano} não é bissexto")
    else:
      print(f"O ano {ano} é bissexto")
  else:
    print(f"O ano {ano} não é bissexto")

verifyYear(ano)