def fatorial(n):
    fat = 1
    for i in range(1, n+1):
        fat = fat * i
    return fat

for n in range (1, 6):
    meuFatorial = fatorial(n)
    print(f'O fatorial de {n} é {meuFatorial}')
    