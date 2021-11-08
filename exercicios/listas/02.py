notas = []

for i in range(30):
    av1 = float(input(f"Digite a nota 1 do aluno {i+i}: "))
    av2 = float(input(f"Digite a nota 2 do aluno {i+i}: "))
    notas.append(float((av1+av2)/2))

acima = 0
soma = 0
for i in notas:
    if i >= 8:
        acima += 1
    soma += i

mediaGeral = soma / len(notas)

print(f"{acima} alunos estão acima da média")
print(f"A média da turma é igual a {mediaGeral:.2f}")