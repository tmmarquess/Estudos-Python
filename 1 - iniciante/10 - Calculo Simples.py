item1 = input()
item1 = item1.split()

item2 = input()
item2 = item2.split()

for i in range(3):
    if(i!=2):
        item1[i] = int(item1[i])
        item2[i] = int(item2[i])
    else:
        item1[i] = float(item1[i])
        item2[i] = float(item2[i])

total = float((item1[1] * item1[2]) + (item2[1] * item2[2]))
total = "{:.2f}".format(total)

print("VALOR A PAGAR: R$ "+total)