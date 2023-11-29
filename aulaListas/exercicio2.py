import random

#Construção da Lista de 20 elementos aleatorios
lista1, lista2 = [], []
for i in range(20):
    lista1.append(random.randint(0, 50))
    lista2.append(random.randint(0, 50))


intersect = []
for i in lista1:
    if i in lista2 and i not in intersect:
        intersect.append(i)

intersect.sort()
print(intersect)

for i in intersect:
    print(f"{i}: ({lista1.count(i)}, {lista2.count(i)})")
