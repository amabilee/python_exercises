def invert(n):
  tam = len(str(n))
  string = str(n)
  valor = ''
  for i in range( 1 , tam+1):
    valor += string[tam-i]
  return(valor)

def main():
  numero = int(input("Digite um numero: "))
  res = invert(numero)
  print(res)

main()