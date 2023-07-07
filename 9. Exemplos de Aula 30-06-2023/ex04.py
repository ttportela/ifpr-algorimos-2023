# 04. Faça um programa que gere aleatoriamente 50 números 
# e apresente a quantidade de pares e ímpares.
import random

n = [0] * 50

for i in range(50):
    n[i] = random.randint(0, 1000)

pares = 0
impares = 0
for i in range(50):
    if (n[i] % 2) == 0:
        pares += 1
    else:
        impares += 1

print("Elementos:", n)
print("Quantidade de pares...:", pares)
print("Quantidate de ímpares.:", impares)