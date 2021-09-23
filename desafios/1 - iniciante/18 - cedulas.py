valor = int(input())


notas = [100,50,20,10,5,2,1]
contador = [0,0,0,0,0,0,0]
matriz = [ ]
matriz.append(notas)
matriz.append(contador)

print(valor)
i = 0
while (valor>=0):
    if(matriz[0][i]>valor):
        if(valor==0):
            break
        i+=1
    else:
        valor-=matriz[0][i]
        matriz[1][i]+=1

tipo = "nota(s)"
for i in range(7):
    print(f"{matriz[1][i]} {tipo} de R$ {matriz[0][i]},00")