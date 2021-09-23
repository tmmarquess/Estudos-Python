a = int(input())
b = int(input())
c = int(input())

if(a>b):
    if(a>c):
        print(f"Maior = {a}")
        if (b>c):
            print(f"Menor = {c}")
        else:
            print(f"Menor = {b}")
    else:
        print(f"Maior = {c}")
        print(f"Menor = {b}")
else:
    if(b>c):
        print(f"Maior = {b}")
        if(c>a):
            print(f"Menor = {a}")
        else:
            print(f"Menor = {c}")
    else:
        print(f"Maior = {c}")
        print(f"Menor = {a}") 