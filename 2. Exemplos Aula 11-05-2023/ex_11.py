# 11 - Leia um valor em reais e diga se ele pode ser pago apenas em notas de cinco 
valor = int(input("Informe um valor em reais (R$): "))

if (valor % 5) == 0:
    print("Sim, o valor pode ser pago apenas com notas de R$ 5,00.")
else:
    print("Não, o valor não pode ser pago apenas com notas de R$ 5,00.")