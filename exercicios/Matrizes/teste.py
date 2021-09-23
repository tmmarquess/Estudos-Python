def conta_digitos(a, b):
    if(b!=0):
        contadores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(a, b+1):
            while i != 0:
                digito = int(i % 10)
                contadores[digito] += 1
                i = int(i/10)
        return contadores
    else:
        return ["","","","","","","","","",""]

imp = ""
for i in range(5):
    a = input()
    a = a.split()
    resp = conta_digitos(int(a[0]),int(a[1]))
    for j in range(10):
        imp += str(resp[j])+" "
    imp += f"\n"
print(imp)