lista = input()
lista = lista.split()
num = []
for i in lista:
    num.append(float(i))

media = (num[0] * 2 + num[1] * 3 + num[2] * 4 + num[3] * 1) / 10

print(f"Media: {media:.1f}")

if media>=7:
    print("Aluno aprovado.")
elif media<5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")

    exame = float(input())
    print(f"Nota do exame: {exame:.1f}")

    mediaFinal = (media+exame)/2
    if mediaFinal >=5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
        
    print(f"Media final: {mediaFinal:.1f}")