print("--- PROGRAMA DE BUSCA o/ ---")
A = [0] * 10

import random
for i in range(10):
    A[i] = random.randrange(1, 100)
    print(A[i], end=", ")

print("\nBuscar um número.")
num = int( input("Informe o número a ser buscado: ") ) 

pos = -1
for i in range(10):
    if A[i] == num:
        pos = i
        break
    
if pos > -1:
    print("Número", num, "encontrado na posição", pos)
else:
    print("Número", num, "NÃO foi encontrado")