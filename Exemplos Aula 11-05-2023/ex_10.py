# 10 - Leia um numero e informe se ele possui 1, 2, 3 ou 4 algarismos
num = int(input("Informe um numero: "))

# Solução 1:
if num >= 0 and num < 10:
    print("O numero possui um algarismo.")
elif num >= 10 and num < 100:
    print("O numero possui dois algarismos.")
elif num >= 100 and num < 1000:
    print("O numero possui três algarismos.")
elif num >= 1000 and num < 10000:
    print("O numero possui quatro algarismos.")

# Solução 2:
print("O numero possui ", len( str(num) ), " algarismos.")