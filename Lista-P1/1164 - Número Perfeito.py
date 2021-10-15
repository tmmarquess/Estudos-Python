n = int(input())

numeros = []
for i in range(n):
    numeros.append(int(input()))

for i in numeros:
    soma = 0
    for j in range(1,i):
        if i%j == 0:
            soma+=j
    if soma == i:
        print(f"{i} eh perfeito")
    else:
        print(f"{i} nao eh perfeito")
