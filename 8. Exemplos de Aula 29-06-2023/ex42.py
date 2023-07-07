print("--- Programa 42 ---")

def calculaAplicacao(valor, rendimento, periodo):
    aplicacao = valor
    for i in range(1, periodo+1):
        aplicacao = aplicacao + (aplicacao * rendimento)
        if (i % 12) == 0:
            aplicacao = aplicacao + (aplicacao * (0.25/100))
#            print("Parabéns! 12 meses")
#        print("Mês:", i, " - Apl.:", aplicacao)
    return aplicacao
        
valor = float( input("Informe o valor da aplicação: ") )
rendimento = float( input("Informe o rendimento (x%): ") )
periodo = int( input("Informe o período da aplicação: ") )
                   
apl = calculaAplicacao(valor, rendimento/100, periodo)
print("O valor da aplicação ao final do período é: ", "{:.2f}".format(apl))