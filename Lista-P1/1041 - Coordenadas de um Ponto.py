lista = input()
lista = lista.split()

x = float(lista[0])
y = float(lista[1])

if x == 0:
    if y==0:
        print("Origem")
    else:
        print("Eixo Y")
elif x>0:
    if y>0:
        print("Q1")
    elif y<0:
        print("Q4")
    else:
        print("Eixo X")
else:
    if y>0:
        print("Q2")
    elif y<0:
        print("Q3")
    else:
        print("Eixo X")
