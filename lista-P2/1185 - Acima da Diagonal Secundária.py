operacao = input()

matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

soma = 0
for i in range(11):
    for j in range(10-i,-1,-1):
            soma += matriz[i][j] # 66 casas a se somar

if operacao == 'M':
    media = soma / 66
    print("{:.1f}".format(media))
else:
    print("{:.1f}".format(soma))