print("Programa dos números")
num = int( input("Informe um número: ") )

# Opção 1:
for i in range(num+1):
    print(i, end=", ")

print()
if (num % 2) != 0:
    print("o número", num, "é ímpar.")

print("-----------------------------")
#Opção 2:
for i in range(1, num+1, 1):
    print(i, end=", ")
print()
if (num % 2) == 0:
    print("Ö número", num, "é par.")