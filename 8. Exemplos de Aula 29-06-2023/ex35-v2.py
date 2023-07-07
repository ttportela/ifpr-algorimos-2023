import random

print("--- Programa 35 ---")
A = [ [0] * 4 ] * 4

random.seed(1)
soma = 0
for i in range(4):
    for j in range(4):
        A[i][j] = random.randrange(0, 100)
        soma = soma + A[i][j]
        
print("A soma é: ", soma)