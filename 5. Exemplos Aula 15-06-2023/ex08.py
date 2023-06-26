# Ex.08: Crie um programa que imprima a seguinte estrutura baseado em um valor lido:
'''
    n = 5 (somente ímpares)
          1
        3 3 3  
      5 5 5 5 5
'''
n = int(input("Informe o N (ímpar): "))

for i in range(1, n+1, 2):
    for k in range( (n-i)//2 ):
        print(" ", end=" ")
    for j in range(i):
        print(i, end=" ")
    print()