# 06 - Ler 3 palavras em variaveis A,B,C e trocar o valor de A por B, B por C e C por A 
a = input("Informe a palavra 1: ")
b = input("Informe a palavra 2:")
c = input("Informe a palavra 3 ")

aux = a
a = b
b = c
c = aux
 
print('Palavras trocadas: ', a, b, c)