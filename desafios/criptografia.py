def declaraMatriz():
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',' ','.',',','?']
    matriz = []

    matriz.append(letras)

    aux = ("0 1 2 3 4 "*6)
    aux = aux.split()

    for i in range(len(aux)):
        aux[i] = int(aux[i])

    matriz.append(aux)

    aux = ""
    for i in range(6):
        aux += (f"{i} "*5)

    aux = aux.split()

    for i in range(len(aux)):
        aux[i] = int(aux[i])

    matriz.append(aux)
    return matriz

def Criptografar(chave,frase):
    matriz = declaraMatriz()
    frase = frase.upper()
    linha1 = []
    linha2 = []
    for i in range(len(frase)):
        for j in range(30):
            if matriz[0][j] == frase[i]:
                linha1.append(matriz[1][j])
                linha2.append(matriz[2][j])
    frase = [linha1,linha2]

    linha1 = []
    linha2 = []
    for i in range(len(frase[0])):
        linha1.append(chave[0][0] * frase[0][i] + chave[0][1] * frase[1][i])
        linha2.append(chave[1][0] * frase[0][i] + chave[1][1] * frase[1][i])

    return [linha1,linha2]

def Descriptografar(chave, fraseCrip):
    matriz = declaraMatriz()
    det = 1/((chave[0][0] * chave[1][1]) - (chave[0][1] * chave[1][0]))
    chave = [det * chave[1][1], det * chave[0][1]*(-1)],[det * chave[1][0]*(-1), det * chave[0][0]]

    linha1 = []
    linha2 = []
    for i in range(len(fraseCrip[0])):
        linha1.append(chave[0][0] * fraseCrip[0][i] + chave[0][1] * fraseCrip[1][i])
        linha2.append(chave[1][0] * fraseCrip[0][i] + chave[1][1] * fraseCrip[1][i])
    
    frase = [linha1,linha2]
    fraseTexto = ""

    for i in range(len(frase[0])):
        for j in range(30):
            if frase[0][i] == matriz[1][j] and frase[1][i] == matriz[2][j]:
                fraseTexto+=matriz[0][j]

    return fraseTexto

def temInversa(matriz):
    det = ((matriz[0][0] * matriz[1][1]) - (matriz[0][1] * matriz[1][0]))

    if det != 0:
        return True
    else:
        return False

while(True):
    escolha = int(input("O que você deseja fazer? [1 = criptografar / 2 = descriptografar]: "))

    if escolha == 1 or escolha ==2:
        break

if escolha == 1:
    frase = input("Digite uma frase: ")

    while(True):
        chave = []
        linha = input("Digite a Linha 1 da matriz chave: ").split()
        for i in range(len(linha)):
            linha[i] = int(linha[i])
        chave.append(linha)

        linha = input("Digite a Linha 2 da matriz chave: ").split()
        for i in range(len(linha)):
            linha[i] = int(linha[i])
        chave.append(linha)

        if not temInversa(chave):
            print("Escolha outra chave [cujo determinante seja diferente de 0]")
        else:
            break

    fraseCrip = Criptografar(chave,frase)
    for i in range(2):
        for j in range(len(fraseCrip[0])):
            print(f"{fraseCrip[i][j]}",end=" ")
        print()
else:
    fraseCrip = []
    linha = input("Digite a Linha 1 da matriz criptografada: ").split()
    for i in range(len(linha)):
        linha[i] = int(linha[i])
    fraseCrip.append(linha)

    linha = input("Digite a Linha 2 da matriz criptografada: ").split()
    for i in range(len(linha)):
        linha[i] = int(linha[i])
    fraseCrip.append(linha)

    while(True):
        chave = []
        linha = input("Digite a Linha 1 da matriz chave: ").split()
        for i in range(len(linha)):
            linha[i] = int(linha[i])
        chave.append(linha)

        linha = input("Digite a Linha 2 da matriz chave: ").split()
        for i in range(len(linha)):
            linha[i] = int(linha[i])
        chave.append(linha)

        if not temInversa(chave):
            print("Esta chave não pode ser utilizada [determinante = 0]")
        else:
            break

    fraseDescrip =  Descriptografar(chave,fraseCrip)

    print(f"Frase descriptografada: {fraseDescrip}")