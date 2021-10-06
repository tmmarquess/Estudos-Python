lista = []
numeros = input(f"Digite os numeros: ") # 5 6 1 4 9 0 3 8 7 2
numeros = numeros.split()
for i in range(10):
    lista.append(int(numeros[i]))

print(f"antes: {lista}")

#listaAux = lista
#listaAux.sort()
#print(listaAux)

for i in range(10):
    for j in range(10):
        if(lista[i]<lista[j] and i!=j):
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

print(f"Depois: {lista}")