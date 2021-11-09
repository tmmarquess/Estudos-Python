operacao = input()

matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

soma = 0
for i in range(12):
    for j in range(1+i,11-i):
        soma += matriz[i][j]

if operacao == 'M':
    media = soma / 30
    print("{:.1f}".format(media))
else:
    print("{:.1f}".format(soma))