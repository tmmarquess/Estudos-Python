numeros = []
for i in range(100):
    numeros.append(int(input()))

maior = -1
posicao = -1
for i in range(100):
    if numeros[i] > maior:
        maior = numeros[i]
        posicao = i+1
    
print(maior)
print(posicao)