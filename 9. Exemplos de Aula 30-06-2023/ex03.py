# 03. Faça um programa que leia 5 letras vogais e ao final apresente 
#     a quantidade de as, es, is, os, us.

vogais = [0] * 5

for i in range(5):
    vogais[i] = input("Digite uma vogal: ")

contVogais = [0] * 5
for i in range(5):
    if vogais[i] == "a":
        contVogais[0] += 1
    elif vogais[i] == "e":
        contVogais[1] += 1
    elif vogais[i] == "i":
        contVogais[2] += 1
    elif vogais[i] == "o":
        contVogais[3] += 1
    elif vogais[i] == "u":
        contVogais[4] += 1

print("A contagem de vogais é:")
print("  a = ", contVogais[0])
print("  e = ", contVogais[1])
print("  i = ", contVogais[2])
print("  o = ", contVogais[3])
print("  u = ", contVogais[4])