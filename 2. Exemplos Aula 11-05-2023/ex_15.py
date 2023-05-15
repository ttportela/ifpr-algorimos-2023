# 15 - Leia a idade de um funcionário e calcule o seu salário:
#    - R$ 3.000,00 + 3% para cada ano acima de 18 anos
#    - R$ 3.000,00 - 2% para cada ano abaixo de 18 anos
print("--- Programa para definição do salário ---")
idade = int(input("Informe a idade do trabalhador:"))

base = 3000
if idade >= 18:
    salario = base + ( (idade-18) * (base * 3/100) )
else:
    salario = base - ( (18-idade) * (base * 2/100) )

print("Para ", idade, " anos, o salário é de: R$", salario)