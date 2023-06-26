# Ex.05: Crie um programa que imprima a seguinte estrutura baseado em um valor inteiro lido:
'''
    n = 4
    1
    2 2 
    3 3 3
    4 4 4 4
'''
print("--- Programa bunito ---")
n = int(input("Informe N: "))

for x in range(1, n+1):
    for y in range(x):
        print(x, end=" ")
    print()