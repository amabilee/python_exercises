def fibonacci(n):
  if n > 1:
    return fibonacci(n - 1) + fibonacci(n - 2)
  else:
    return 1

def main():
  len = int(input("Digite o range "))
  for i in range(len):
    print(i, " ==> ", fibonacci(i))

main()