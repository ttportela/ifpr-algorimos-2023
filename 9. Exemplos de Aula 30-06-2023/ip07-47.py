print("--- Programa 47 ---")
sequencia = input("Digite um número binário: ")

tamMaior = 0
tamSubSeq = 0
for i in range(len(sequencia)):
    if sequencia[i] == '1': 
        tamSubSeq += 1
        if tamSubSeq > tamMaior:
            tamMaior = tamSubSeq
    else: # OU se '0'
        tamSubSeq = 0
        

print("O tamanho da maior subsequência é", tamMaior, "dígitos 1´s.")