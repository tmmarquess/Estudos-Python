# 9,16,6,8,10,12,13,18,16;24,44,16,24,28,32,36,50,44
coisado = input().split(";")
coisado[0] = coisado[0].split(",")
coisado[1] = coisado[1].split(",")

for i in range(len(coisado[0])):
    coisado[0][i] =  int(coisado[0][i])
    coisado[1][i] =  int(coisado[1][i])

for i in coisado[0]:
    print(i, end=" ")

print()

for i in coisado[1]:
    print(i, end=" ")