print("--- PROGAMA 100 PARES ---")

print("\n Solução 1:")
# Solução 1:
for i in range(200):
    if (i % 2) == 0:
        print(i, end=", ")

print()
print("\n Solução 2:")
i = 0
count = 0
while count < 100:
    if (i % 2) == 0:
        print(i, end=", ")
        count += 1
    i += 1

print()
print("\n Solução 3:")
for i in range(0, 200, 2):
    print(i, end=", ")

