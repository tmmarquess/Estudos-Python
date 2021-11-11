while(True):
    contados = [["0","1","2","3","4","5","6","7","8","9"],[0,0,0,0,0,0,0,0,0,0]]
    intervalo = input()
    if intervalo == "0 0":
        break
    intervalo = intervalo.split()

    numeros = ""
    for i in range(int(intervalo[0]),int(intervalo[1])+1):
        numeros += str(i)
    
    for i in range(len(numeros)):
        contados[1][contados[0].index(numeros[i])] += 1
    qnt = ""
    for i in contados[1]:
        qnt+= str(i)+" "
    print(qnt.strip())