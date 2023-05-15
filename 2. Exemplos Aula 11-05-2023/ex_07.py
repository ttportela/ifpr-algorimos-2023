# 07 - Leia 3 números apresente a soma dos positivos e a soma dos negativos.
num1 = int(input('Digite um número 1: '))
num2 = int(input('Digite um número 2: '))
num3 = int(input('Digite um número 3: '))

if num1 >= 0:
    pos += num1
else:
    neg += num1

if num2 >= 0:
    pos += num2
else:
    neg += num2

if num3 >= 0:
    pos += num3
else:
    neg += num3

    
print('A soma dos números positivos é:', pos)
print('A soma dos números negativos é:', neg)