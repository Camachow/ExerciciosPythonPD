maior = float('-inf')
menor = float('inf')

while True:
    i = int(input("Digite um numero: "))
    if i == 0: break

    if i > maior: maior = i
    if i < menor: menor = i

print(f"O maior numero digitado foi {maior} e o menor foi {menor}")
