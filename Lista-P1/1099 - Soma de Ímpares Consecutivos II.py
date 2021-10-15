n = int(input())

lista = []
for i in range(n):
    numeros = []

    aux = input()
    aux = aux.split()
    aux[0] = int(aux[0])
    aux[1] = int(aux[1])

    if(aux[0]>aux[1]):
        aux[0], aux[1] = aux[1],aux[0]

    numeros.append(aux[0])
    numeros.append(aux[1])

    lista.append(numeros)

for i in range(n):
    soma = 0
    for j in range(lista[i][0]+1,lista[i][1]):
        if j%2 != 0:
            soma+=j
    print(soma)