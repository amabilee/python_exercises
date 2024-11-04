def pot(k, n):
  res = k**n
  return res

def main():
  num1 = int(input("Digite o primeiro valor: "))
  num2 = int(input("Digite o segundo valor: "))
  print(pot(num1, num2))

main()