def uniao(l1,l2):
    uniao = []
    for i in range(5):
        if l1[i] != l2[i]:
            uniao.append(l1[i])
            uniao.append(l2[i])
        else:
            uniao.append(l1[i])
    uniao.sort()
    i = 0
    while(True):
        if uniao[i] == uniao[i+1]:
            uniao.pop(i)
        if len(uniao)-2 == i:
            break
        else:
            i += 1

    return uniao

def interseccao(l1,l2):
    l1.sort()
    l2.sort()
    intersec = []
    for i in range(5):
        for j in range(5):
            if l1[i] == l2[j]:
                intersec.append(l1[i])
    intersec.sort()
    i = 0
    while(True):
        if intersec[i] == intersec[i+1]:
            intersec.pop(i)
        if len(intersec)-2 == i:
            break
        else:
            i += 1

    return intersec

l1 = []
l2 = []

for i in range(5):
    l1.append(int(input(f"Digite o {i+1}º numero da lista 1: ")))

for i in range(5):
    l2.append(int(input(f"Digite o {i+1}º numero da lista 2: ")))

print(uniao(l1,l2))
print(interseccao(l1,l2))