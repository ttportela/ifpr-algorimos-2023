# 13 - Leia dois valores e informe quanto por cento o primeiro tem de diferença do segundo
val1 = int(input("Digite um valor: "))
val2 = int(input("Digite um outro valor: "))

diferenca = val1 - val2
porcentagem = (diferenca * 100) / val1

print("A diferença do primeiro para o segundo em porcentagem (%) é: ", porcentagem)