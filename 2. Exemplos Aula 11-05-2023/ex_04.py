# 04 - Solicite duas palavras e imprima em ordem alfabética
p1 = input('Digite uma palavra: ')
p2 = input('Digite outra palavra:')

print('Em ordem crescente: ')
# Solução 1:
if p1 > p2:
    print(p2, p1)
else:
    print(p1, p2)

# Solução 2 (comparando apenas a primeira letra):
if p1[0] > p2[0]:
    print(p2, p1)
else:
    print(p1, p2)