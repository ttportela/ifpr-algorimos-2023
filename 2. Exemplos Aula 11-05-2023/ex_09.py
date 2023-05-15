# 09 - Ler dois números e informar se, e somente se, um deles for 42.
num1 = int(input('Informe um número: '))
num2 = int(input('Informe um outro número: '))

if num1 == 42 ^ num2 == 42:
    print("Um e apenas um dos valores é igual a 42: ", num1, ',', num2)
else:
    print("Nenhum (ou os dois) dos valores são iguais a 42: ", num1, ',', num2)
