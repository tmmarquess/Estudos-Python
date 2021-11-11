t = int(input())

for i in range(t):
    n = int(input())
    nomes = input().split()
    frequencias = input().split()

    for i in range(n):
        aulas = len(frequencias[i])
        soma = 0
        for j in range(len(frequencias[i])):
            if frequencias[i][j] == 'P':
                soma += 1
            elif frequencias[i][j] == 'M':
                aulas -= 1
        porcentagem = (100 * soma)/aulas
        if porcentagem >= 75:
            frequencias[i] = True
        else:
            frequencias[i] = False

    sem_Presenca = ""
    for i in range(len(frequencias)):
        if frequencias[i] == False:
            sem_Presenca+=nomes[i]+" "
    print(sem_Presenca.strip())