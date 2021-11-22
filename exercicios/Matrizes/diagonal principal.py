matriz = []

for i in range(7):
    linha = []
    for j in range(7):
        linha.append(int(input(f"Digite o numero da Linha {i+1} coluna {j+1}: ")))
    matriz.append(linha)

escolha = int(input(f"Escolha uma linha para mostrar entre 1 e 7: "))

while(escolha<0 and escolha>7):
    escolha = int(input(f"Escolha uma linha para mostrar entre 1 e 7: "))

print(matriz[escolha-1])