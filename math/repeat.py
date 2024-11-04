def qnt(n, r):
  if n == 0:
    return 0
  if n % 10 == r:
    return 1 + qnt(n // 10, r)
  else:
    return qnt(n // 10, r)

def main():
  num = int(input("Digite um número: "))
  k = int(input("Número que você quer ver que repete: "))
  res = qnt(num, k)
  print(f"O número {k} ocorre {res}.")

main()