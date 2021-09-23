nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
horas = int(input())

aprovado = nota1>=7 and nota2>=7 and nota3>=7 and (horas>= 0.75*60)

print("Aprovado?",aprovado) 