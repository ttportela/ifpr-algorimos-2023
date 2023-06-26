def lerItem():
    item = input("Informe o que deseja comprar: ")
    qtd  = int( input("Informe a quantidade: ") )
    return [item, qtd]

def addItem(lista, item):
    lista.append(item)
    
def mostrar(lista):
    for i in range(len(lista)):
        print("Item", i, "-", lista[i][0], ", #", lista[i][1])

def zerarItem(lista):
    print("Qual item deseja zerar?")
    mostrar(lista)
    it = int(input("Item: "))
    lista[it][1] = 0

def main():
    print("--- Lista de Compras ---")
    lsCompras = []
    
    opcao = 1
    while opcao > 0:
        print("---------------------------------------------")
        print("Menu:")
        print(" 1 - Adicionar item")
        print(" 2 - Adicionar vários itens")
        print(" 3 - Mostrar lista")
        print(" 4 - Zerar um item")
        print(" 0 - Sair")
        opcao = int(input("Selecione uma opção: "))
        
        print("---------------------------------------------")
        if opcao == 1:   
            addItem(lsCompras, lerItem())
        elif opcao == 2:
            n = int(input("Adicionar quantos itens? "))
            for i in range(n):
                addItem(lsCompras, lerItem())
        elif opcao == 3:
            mostrar(lsCompras)
        elif opcao == 4:
            zerarItem(lsCompras)
    
main()