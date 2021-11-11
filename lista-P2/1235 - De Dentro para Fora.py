def decodificar(frase):
    tam = len(frase)
    metade = int(tam/2)

    for i in range(metade-1,-1,-1):
        print(frase[i],end="")

    for i in range(tam-1,metade-1,-1):
        print(frase[i],end="")

n = int(input())

for i in range(n):
    decodificar(input())
    print()