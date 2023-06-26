print("--- Programa 37 +Fácil ---")

def imprime(n):
    k = n
    for i in range(1, n):
        imprimeLinha(i, k)
        k = k - 1
    imprimeLinha(n, 1)
    for i in range(n-1, 0, -1):
        k = k + 1
        imprimeLinha(i, k)
    
    
def imprimeLinha(n, vezes):
    for i in range(vezes):
        print(n, end=" ")
    print()

imprime(3)