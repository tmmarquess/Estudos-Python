def shellSort(vet, size):
    gap = 1
    while(gap < size):
        gap = (3*gap+1)
    while ( gap > 1) :
        gap = int(gap/3)
        for i in range(gap,size):
            value = vet[1][i]
            j = i - gap
            while (j >= 0 and value < vet[1][j]):
                vet [1][j + gap] = vet[1][j]
                aux = vet[0][j + gap]
                vet[0][j + gap] = vet[0][j]
                j -= gap
            vet [1][j + gap] = value
            vet[0][j + gap] = aux

vet = [[1,2,3,4,5,6],[10,5,7,8,9,10]]
shellSort(vet,len(vet[1]))
print(vet)