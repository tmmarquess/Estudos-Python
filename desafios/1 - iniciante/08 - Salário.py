num = int(input())
horas = int(input())
valorHora = float(input())
sal = horas * valorHora
sal = "{:.2f}".format(sal)
print("NUMBER = "+str(num))
print("SALARY = U$ "+str(sal))