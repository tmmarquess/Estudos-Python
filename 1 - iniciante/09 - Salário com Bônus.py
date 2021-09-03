num = str(input())
sal = float(input())
vendas = float(input())
comissao = 0.15 * vendas
salFinal = sal + comissao
salFinal = "{:.2f}".format(salFinal)
print("TOTAL = R$ "+str(salFinal))