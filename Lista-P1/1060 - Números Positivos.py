i = 0
positivos = 0
while i<6:
    num = float(input())
    if num!=0:
        if num>0:
            positivos+=1
        i+=1

print(f"{positivos} valores positivos")