# 02. Altere o programa 01 para ler 100 números:
numEle = 100
n = [0] * numEle # Declaração de um vetor

# leitura de 5 números:
for i in range(numEle): # range(0, 5, 1)
    n[i] = int( input("Informe um número: ") )

soma = 0
maior = -1
menor = float("inf")
for i in range(numEle):
    soma = soma + n[i]
    if n[i] >= maior:
        maior = n[i]
    if n[i] <= menor:
        menor = n[i]

print("A soma dos elementos é:", soma)
print("O maior elemento é:", maior)
print("O menor elemento é:", menor)