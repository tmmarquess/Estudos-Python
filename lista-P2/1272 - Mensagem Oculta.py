n = int(input())

for i in range(n):
    texto = input().strip().split()

    for i in range(len(texto)):
        print(texto[i][0],end="")
    print()