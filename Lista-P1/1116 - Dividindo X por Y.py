n = int(input())
matriz = []
for i in range(n):
    linha = []
    num = input()
    num = num.split()

    linha.append(float(num[0]))
    linha.append(float(num[1]))
    matriz.append(linha)

for i in matriz:
    if i[1] == 0:
        print("divisao impossivel")
    else:
        divisao = i[0]/i[1]
        print(f"{divisao:.1f}")