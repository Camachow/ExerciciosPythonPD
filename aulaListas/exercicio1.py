import random

#Construção da Lista de 20 elementos aleatorios
lista = []
for i in range(20):
    lista[i] = random.randint(-100, 100)

print(sorted(lista)) #Ordenação da lista
print(lista) #Lista original
print("O index do maior elemento da lista é: ", lista.index(max(lista)))
print("O menor elemento da lista é: ", lista.index(min(lista)))
print("A soma dos elementos da lista é: ", sum(lista))
print("A média dos elementos da lista é: ", sum(lista)/20)
