algarismos = ["0","1","2","3","4","5","6","7","8","9"]
while(True):
    contados = [0,0,0,0,0,0,0,0,0,0]
    intervalo = input()
    if intervalo == "0 0":
        break
    intervalo = intervalo.split()

    numeros = ""
    for i in range(int(intervalo[0]),int(intervalo[1])+1):
        for j in str(i):
            contados[algarismos.index(j)] += 1

    qnt = ""
    for i in contados:
        qnt+= str(i)+" "
    print(qnt.rstrip())