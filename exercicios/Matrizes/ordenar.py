
def ordena(linha):
    for i in range(len(linha)-1):
        trocou = False
        for j in range(len(linha)-1-i):
            if(linha[j] > linha[j+1]):
                trocou = True
                linha[j], linha[j+1] = linha[j+1], linha[j]
        if not trocou:
            break

linha = 5
coluna = 5

matriz = []
for i in range(linha):
    l = []
    for j in range(coluna):
        l.append(int(input()))
    matriz.append(l)

print("Antes:")
for i in range(linha):
    for j in range(coluna):
        print(matriz[i][j],end=" ")
    print()

print("Depois:")
for i in range(linha):
    ordena(matriz[i])
    for j in range(coluna):
        print(matriz[i][j],end=" ")
    print()