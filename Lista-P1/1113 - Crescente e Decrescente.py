matriz = []
while True:
    linha = []
    num = input()
    num = num.split()
    
    num[0] = int(num[0])
    num[1] = int(num[1])

    if num[0] == num[1]:
        break
    linha.append(num[0])
    linha.append(num[1])
    matriz.append(linha)

for j in matriz:
    if j[0] > j[1]:
        print("Decrescente")
    else:
        print("Crescente")