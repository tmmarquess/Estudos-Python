x = input()
x = x.split()

a = float(x[0])
b = float(x[1])
c = float(x[2])

areaTri = (a*c)/2
areaTri = "{:.3f}".format(areaTri)

pi = 3.14159
areaCir = pi * c**2
areaCir = "{:.3f}".format(areaCir)

areaTrap = ((a+b) * c)/2
areaTrap = "{:.3f}".format(areaTrap)

areaQuad = b**2
areaQuad = "{:.3f}".format(areaQuad)

areaRet = a*b
areaRet = "{:.3f}".format(areaRet)

print("TRIANGULO: " + str(areaTri))
print("CIRCULO: " + str(areaCir))
print("TRAPEZIO: " + str(areaTrap))
print("QUADRADO: " + str(areaQuad))
print("RETANGULO: " + str(areaRet))