#Cria a Matriz 10x10 e define todos os seus valores para 0
matriz = [ ]
for i in range(10):
    linha = [ ]
    for j in range(10):
        linha.append(0)
    matriz.append(linha)

#recebe o numero de linhas
n = int(input())

#cria uma matriz de N linhas com as colunas D L R C
posicoes = [ ]
for i in range(n):
    linha = input()
    linha = linha.split()
    posicoes.append(linha)

for i in range(n): #Transforma as Strings em Inteiro e altera o valor das coordenadas para poder manipulá-las
    for j in range(4):
        posicoes[i][j] = int(posicoes[i][j])
        if(j == 2 or j == 3):
            posicoes[i][j] -=1

passou_da_matriz = False #verifica se a coordenada está além da matriz de 10x10
for i in range(n): # Povoa a Matriz 10x10 com as coordenadas dos barcos
    if(posicoes[i][0] == 0):
        aux = (posicoes[i][3])
        while(aux<=(posicoes[i][3]+posicoes[i][1]-1)):
            if(posicoes[i][2]>9 or aux>9): #verifica se a coordenada está além da matriz de 10x10
                passou_da_matriz = True
                break
            matriz[posicoes[i][2]][aux]+=1
            aux+=1
    else:
        aux = (posicoes[i][2]-1)
        while(aux<=(posicoes[i][2]+posicoes[i][1]-1)):
            if(posicoes[i][3]>9 or aux>9):  #verifica se a coordenada está além da matriz de 10x10
                passou_da_matriz = True
                break
            matriz[aux][posicoes[i][3]]+=1
            aux+=1

#verifica se na Matriz 10x10 há algum barco que sobrepôs outro
for i in range(10):
    for j in range(10):
        if(matriz[i][j]==4 or matriz[i][j]==0):
            resp = True
        else:
            resp = False
            break

#Imprime a resposta final desejada
if(resp == True and passou_da_matriz == False):
    print("Y")
else:
    print("N")

'''     
#Mostra a matriz 10x10 povoada onde os valores diferentes de 0 são onde se encontram os barcos (e os maiores de 1 são barcos sobrepostos)

for i in range(10):
    teste = ""
    for j in range(10):
        teste+=""+ str(matriz[i][j]) +" "
    print(teste)
'''
