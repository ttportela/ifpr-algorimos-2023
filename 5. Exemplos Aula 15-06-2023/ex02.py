# Ex.02: Crie um programa que calcula a área de um retângulo.
def areaRetangulo(ladoA, ladoB):
    return ladoA * ladoB

def programaAR():
    print("--- Programa - Área do Retângulo ---")
    lado1 = float(input("Informe o tamanho do lado 1: "))
    lado2 = float(input("Informe o tamanho do lado 2: "))
    
    area = areaRetangulo(lado1, lado2)
    
    print("A área do retângulo é:", area)
    
programaAR()