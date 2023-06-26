# Ex.07 - Desafio:  Crie um programa que imprima a seguinte estrutura baseado em um valor lido:
'''
    n = 4
          1
        2 2
      3 3 3  
    4 4 4 4
'''
n = int(input("Informe o N: "))

for i in range(1, n+1):
    for k in range(n-i):
        print("  ", end="")
    for j in range(i):
        print(" " + str(i), end="")
    print()