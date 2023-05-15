# 03 - Solicite 2 números e imprima em ordem crescente
num1 = int(input('Informe um número: '))
num2 = int(input('Informe outro número: '))

print('Ordem crescente: ')
if num1 >= num2:
    print(num2, num1)
else:
    print(num1, num2)