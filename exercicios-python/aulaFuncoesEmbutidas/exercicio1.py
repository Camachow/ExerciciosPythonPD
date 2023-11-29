import random, math

n = int(input("Digite a quantidade de valores: "))
soma = 0

for i in range(n):
    valor = random.randint(0, 100) #Gera um valor aleatório entre 0 e 100
    soma += valor
    print("Valor ", i+1, ": ", valor)

raiz = math.sqrt(soma)

print("A soma dos valores é: ", soma)
print(f"A raiz quadrada da soma dos valores é: {raiz:.2f}")