salario = float(input())

if(salario>1250):
    aumento = 0.1 * salario
else:
    aumento = 0.15 * salario

print(f"Salário Antigo: R${salario:.2f}")
salario += aumento

print(f"Aumento = R${aumento:.2f}")
print(f"Novo salário = R${salario:.2f}")