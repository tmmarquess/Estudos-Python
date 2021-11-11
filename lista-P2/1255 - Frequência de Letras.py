letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def contador(frase):
    qnt = [letras[:],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    for i in frase:
        try:
            qnt[1][letras.index(i)] += 1
        except ValueError:
            print("",end="")

    for i in range(len(qnt[0])-1):
        trocou = False
        for j in range(len(qnt[0])-1-i):
            if qnt[1][j] < qnt[1][j+1]:
                trocou = True
                qnt[1][j], qnt[1][j+1], qnt[0][j], qnt[0][j+1] = qnt[1][j+1], qnt[1][j], qnt[0][j+1], qnt[0][j]
        if not trocou:
            break

    maior = qnt[1][0]
    maiores = ""
    for i in range(len(qnt[1])):
        if qnt[1][i] == maior:
            maiores += qnt[0][i].lower()
        else:
            break
    print(maiores)

for i in range(int(input())):
    contador(input().upper())