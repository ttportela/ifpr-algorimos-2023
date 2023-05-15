# 01 - Ler 1 número e informar se é multiplo de 3.
num = int(input("Informe um número: "))

if (num % 3) == 0:
  print(num, "é múltiplo de 3")
else:
  print(num, "não é múltiplo de 3")