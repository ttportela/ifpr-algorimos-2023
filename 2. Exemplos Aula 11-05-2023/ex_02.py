# 02 - Ler um numero de 2 algarismos e inverter seus algarismos 
num = int(input('Informe um número: '))

unidade = num % 10
dezena  = num // 10

print('Ordem invertida: ')
print(unidade*10 + dezena)