def mdc(x, y):
  if y == 0:
    return x
  else:
    res = x % y
    x = y
    y = res
    return mdc(x ,y)

def main():
  num1 = int(input("Digite o valor de x: "))
  num2 = int(input("Digite o valor de y: "))
  print(f"O valor de x e y é igual a: {mdc(num1, num2)}")

main()