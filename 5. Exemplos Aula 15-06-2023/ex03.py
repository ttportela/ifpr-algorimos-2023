# Ex.03: Crie um programa que calcula a área do círculo (área = PI.raio<sup>2</sup>)
def areaCirculo(raio):
    PI = 3.14
    return PI * (raio ** 2)

print("--- Programa - Área do Círculo ---")
raio = float(input("Informe o valor do raio: "))
print("A área do círculo é:", areaCirculo(raio))