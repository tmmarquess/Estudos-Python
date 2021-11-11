n = int(input())
m = int(input())

figurinhas = []
for i in range(m):
    num = int(input())
    try:
        figurinhas.index(num)
    except ValueError:
        figurinhas.append(num)

print(n-len(figurinhas))
