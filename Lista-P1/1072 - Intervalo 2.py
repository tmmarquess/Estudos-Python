qnt = int(input())
x = []

dentro = 0
fora = 0

for i in range(qnt):
    x.append(int(input()))

for i in x:
    if i>=10 and i<=20:
        dentro+=1
    else:
        fora+=1

print(f"{dentro} in")
print(f"{fora} out")