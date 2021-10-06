dias = int(input())

aux = dias%365
anos = int(dias/365)
dias = aux

aux = dias%30
meses = int(dias/30)
dias = aux

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")