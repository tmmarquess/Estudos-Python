letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n = int(input())

for i in range(n):
    texto = input()
    n = int(input())
    novasletras = letras[-n:] + letras[:-n]
    frase = ""
    for i in texto:
        frase+=novasletras[letras.index(i)]
    print(frase)