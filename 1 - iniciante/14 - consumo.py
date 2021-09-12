x = int(input())
y = float(input())

consumo = float(x/y)
consumo = "{:.3f}".format(consumo)

print(consumo,"km/l")