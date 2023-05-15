# 12 - Leia um valor (R$) e informe quantas notas de 10 e de 1 são necessárias
valor = int(input("Informe um valor: "))

notasDeDez = valor // 10
notasDeUm  = valor - notasDeDez

print("São necessárias", notasDeDez, "notas de 10 e", notasDeUm, "notas de 1 para pagar esse valor.")
