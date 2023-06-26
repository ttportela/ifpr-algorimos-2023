# Ex.06:  Crie um programa que imprima a seguinte estrutura baseado em um valor lido:
'''
    n = 4
    2 2
    4 4 4 4
'''
n = int(input("Informe N: "))

for x in range(2, n+1, 2):
    for y in range(x):
        print(x, end=" ")
    print()