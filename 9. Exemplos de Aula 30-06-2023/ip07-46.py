print("--- Programa 46 ---")
sequencia = input("Digite uma sequencia de caracteres binário ou não: ")

ehBinaria = True
for i in range(len(sequencia)):
    if sequencia[i] != '0' and sequencia[i] != '1':
        ehBinaria = False
        break
        
if ehBinaria:
    print("A sequência é BINÁRIA de", len(sequencia), "dígitos.")
else:
    print("A sequência NÃO é binária.")