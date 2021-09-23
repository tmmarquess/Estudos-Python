n = int(input())

horas = 0
minutos = 0
segundos = n

while(segundos>=60):
    if(segundos<60):
        break
    segundos-=60
    minutos+=1

while(minutos>=60):
    if(minutos<60):
        break
    minutos-=60
    horas+=1

print(f"{horas}:{minutos}:{segundos}")