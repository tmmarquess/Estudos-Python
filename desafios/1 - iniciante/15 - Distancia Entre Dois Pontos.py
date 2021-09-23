import math

p1 = input()
p2 = input()

p1 = p1.split()
p2 = p2.split()

for x in range(2):
    p1[x] = float(p1[x])
    p2[x] = float(p2[x])

dist = math.sqrt(((p2[0]-p1[0])**2)+((p2[1]-p1[1])**2))

dist = "{:.4f}".format(dist)

print(dist)