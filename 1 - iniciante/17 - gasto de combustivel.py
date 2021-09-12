tempo = int(input())
velocidade = int(input())

km = tempo * velocidade
litros = km/12

litros = "{:.3f}".format(litros)

print(litros)   