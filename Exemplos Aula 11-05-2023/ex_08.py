# 08 - Pergunte o nome, sobrenome e ano de nascimento do usuário e sugira 4 combinações para nome de usuário de e-mail.
nome = input("Informe seu nome: ")
sobrenome = input("Informe seu sobrenome: ")
ano = int(input("Informe seu ano de nascimento: "))

print("Sugestões de e-mail:")
print(nome + '.' + sobrenome + '@ifpr.edu.br')
print(nome + '_' + str(ano) + '@ifpr.edu.br')
print(sobrenome + '.' + nome + '@ifpr.edu.br')
print(nome + sobrenome + str(ano) + '@ifpr.edu.br')