# Armazenar 8 números em um vetor e imprimi-los. 
# Ao final, indicar o número de números múltiplos de 6 
# e as suas respectivas posições no vetor.

numeros = []
for i in range(8):
    numeros.append(int(input(f"Digite o {i+1}º numero: ")))

for i in numeros:
    print(f"{i}",end=" ") 
print()

print("Multiplos de 6:")
for i in range(len(numeros)):
    if numeros[i] % 6 == 0:
        print(f"{numeros[i]} na posição {i+1}")