x = input()
x = x.split()

a = int(x[0])
b = int(x[1])
c = int(x[2])

if(a>b):
    if(a>c):
        maior = a
    else:
        maior = c
elif(b>c):
    maior = b
else:
    maior = c


print(str(maior),"eh o maior")