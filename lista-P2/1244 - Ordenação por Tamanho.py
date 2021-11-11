def ordenar(frase):
    frase = frase.split()

    for i in range(len(frase)-1):
        trocou = False
        for j in range(len(frase)-1-i):
            if len(frase[j]) < len(frase[j+1]):
                trocou = True
                frase[j], frase[j+1] = frase[j+1], frase[j]
        if not trocou:
            break
    
    FraseString = ""
    for i in frase:
        FraseString = FraseString + i + " "
    return FraseString.strip()

n = int(input())

for i in range(n):
    print(ordenar(input()))