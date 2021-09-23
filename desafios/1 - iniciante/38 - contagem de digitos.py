
def qntAlgarismos(n):
    n = n.split()

    n[0] = int(n[0])
    n[1] = int(n[1])

    if (n[0] == 0 and n[1]==0):
        return ""
    algarismos = ["0","1","2","3","4","5","6","7","8","9"]
    contador = [0,0,0,0,0,0,0,0,0,0]
    matriz = [ ]
    matriz.append(algarismos)
    matriz.append(contador)

    for aux in range(n[0],n[1]+1):
        aux = str(aux)
        for tst in range(len(aux)):
            for i in range(10):
                if(aux[tst] == matriz[0][i]):
                    matriz[1][i]+=1

    resp=""
    for i in range(10):
        resp+=str(matriz[1][i])+" "
    return resp

imp = ""
for i in range(5):
    imp+= qntAlgarismos(input())+f"\n"
print(imp)