# 01. Faça um programa que leia 5 números inteiros em um vetor e, ao final apresente:
# - A soma dos elementos
# - O maior elemento
# - O menor elemento

n = [0] * 5 # Declaração de um vetor

# leitura de 5 números:
for i in range(5): # range(0, 5, 1)
    n[i] = int( input("Informe um número: ") )

# A soma dos elementos:
soma = 0
for i in range(5):
    soma = soma + n[i]
print("A soma dos elementos é:", soma)

# O maior elemento:
maior = -1
for i in range(5):
    if n[i] >= maior:
        maior = n[i]
print("O maior elemento é:", maior)

# O menor elemento
menor = float("inf") # maior
for i in range(5):
    if n[i] <= menor:
        menor = n[i]
print("O menor elemento é:", menor)