num = int(input("Digite o numero de parada: "))
i = 0
print(f"Multiplos de 3 de 0 até {num}:",end=" ")
while(i<num):
    i+=1
    if((i%3) == 0):
        print(i,end=" ")