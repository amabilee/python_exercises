string="ArrOZComFeijÃo"
caracteres= 0
ah = 0
caracteres_substituir = ""
letra = ""
comprimento = len(string)
caracteres_lower= "abcdefghijklmnopqrstuvwxyz"
caracteres_high = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for caracteres in range(comprimento):
  if string[caracteres] in caracteres_high:
    caracteres_substituir = string[caracteres]
    print(caracteres_substituir)
    ah = caracteres_high.find(caracteres_substituir)
    letra =  string[caracteres]
    string = string.replace(letra, caracteres_lower[ah])
    print(string)
    caracteres += 1
  else:
    caracteres += 1
    continue