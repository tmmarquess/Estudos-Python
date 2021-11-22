matriz = []

linha = 3
coluna = 2

#lê a matriz normal
for i in range(linha):
    l = []
    for j in range(coluna):
        l.append(int(input(f"Digite o elemento [{i+1}][{j+1}]: ")))
    matriz.append(l)

#imprime a matriz normal
for i in range(linha):
    print()
    for j in range(coluna):
        print(f"{matriz[i][j]}",end=" ")
print()

#cria uma matriz transposta zerada
transposta = []
for i in range(coluna):
    l = []
    for j in range(linha):
        l.append(0)
    transposta.append(l)

#preenche essa matriz transposta com os valores da normal
for i in range(linha):
    for j in range(coluna):
        transposta[j][i] = matriz[i][j]

#imprime a matriz transposta
for i in range(coluna):
    print()
    for j in range(linha):
        print(f"{transposta[i][j]}",end=" ")