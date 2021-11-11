import random

def meuSort(lista):
    for i in range(len(lista)-1):
        trocou = False
        for j in range(len(lista)-1-i):
            if lista[j] > lista[j+1]:
                trocou = True
                lista[j], lista[j+1] = lista[j+1], lista[j]
        if not trocou:
            break

lista = []
for i in range(random.randrange(1,10)):
    lista.append(random.randrange(1,100))

print(f"Antes: {lista}")
print()
meuSort(lista)
print(f"Depois: {lista}")