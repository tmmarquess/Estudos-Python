valor = float(input())


notas = [100,50,20,10,5,2,1,0.5, 0.25, 0.10, 0.05, 0.01]
contador = [0,0,0,0,0,0,0,0,0,0,0,0]
matriz = [ ]
matriz.append(notas)
matriz.append(contador)


i = 0
while (valor>=0):
    if(matriz[0][i]>valor):
        if(valor==0):
            break
        i+=1
    else:
        valor-=matriz[0][i]
        valor = float("{:.2f}".format(valor))
        matriz[1][i]+=1

print("NOTAS:")
tipo = "nota(s)"
for i in range(12):
    if(i==6):
        print("MOEDAS:")
        tipo = "moeda(s)"
    print(f"{matriz[1][i]} {tipo} de R$ {matriz[0][i]:.2f}")