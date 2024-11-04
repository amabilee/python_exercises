def fat(n):
  if n <= 1:
      return 1
  else:
    return (n * fat(n -1))

def main():
  x = int(input("Digite a qnt de termos: "))
  print(f"O fatorial de {x} é: {fat(x)}")

main()