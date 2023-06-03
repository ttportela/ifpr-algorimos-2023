print("Programa da Idade")
anoNascimento = int( input("Digite o ano de nascimento: ") )
anoAtual = int( input("Informe o ano atual: ") )

idade = anoAtual - anoNascimento
meses = idade * 12
anosDog = idade * 7

print("A idade real é: ", idade)
print("A idade em meses é: ", meses)
print("A idade em anos de cachorro é: ", anosDog)