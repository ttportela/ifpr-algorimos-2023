# Ex.04: Crie um programa com menu para que o usuário selecione o tipo de 
# forma geométrica que deseja calcular a área (quadrado, retângulo ou círculo), 
# faça a leitura dos dados necessários da figura geométrica e apresente o cálculo da área.
def areaQuadrado(lado):
    return lado * lado

def areaCirculo(raio):
    PI = 3.14
    return PI * (raio ** 2)

def areaRetangulo(ladoA, ladoB):
    return ladoA * ladoB

while True:
    print("--- Programa das áreas ---")
    print("Escolha uma opção no menu:")
    print("\t[1] Área do Quadrado")
    print("\t[2] Área do Retângulo")
    print("\t[3] Área do Círculo")
    print("\t[0] Sair")
    op = int(input("Opção desejada: "))
    
    if op == 1:
        # Área do quadrado:
        lado = float(input("Informe o tamanho do lado:"))
        print("A área do quadrado é:", areaQuadrado(lado))
    elif op == 2:
        lado1 = float(input("Informe o tamanho do lado 1: "))
        lado2 = float(input("Informe o tamanho do lado 2: "))
        area = areaRetangulo(lado1, lado2)
        print("A área do retângulo é:", area)
    elif op == 3:
        r = float(input("Informe o raio:"))
        print("A área do círculo é:", areaCirculo(r))
    elif op == 0:
        print("Tenha um bom dia. Bye")
        break
    else:
        print("Opção inválida! Tente outra.")
    print("---------------------------")