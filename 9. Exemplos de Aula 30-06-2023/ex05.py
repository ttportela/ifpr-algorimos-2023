# 05. Modifique o programa 02 para gerar 300 números aleatórios 
#     (entre 1 e 3), em vez de lê-los
import random
numEle = 300
n = [0] * numEle # Declaração de um vetor

# leitura de 5 números:
for i in range(numEle): # range(0, 5, 1)
    n[i] = random.randint(1, 3)

soma = 0
maior = -1
menor = float("inf") # Ou usar um nro maior que 3, ex.: 10
for i in range(numEle):
    soma = soma + n[i]
    if n[i] >= maior:
        maior = n[i]
    if n[i] <= menor:
        menor = n[i]

print("Elementos:", n)
print("A soma dos elementos é:", soma)
print("O maior elemento é:", maior)
print("O menor elemento é:", menor)