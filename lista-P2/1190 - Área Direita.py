operacao = input()

matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

soma = 0
for i in range(11,-1,-1):
    for j in range(i-1,11-i,-1):
        soma+=matriz[j][i]

if operacao == 'M':
    media = soma / 30
    print("{:.1f}".format(media))
else:
    print("{:.1f}".format(soma))