def inverteValor(valor):
    valor_invertido = 0
    while valor > 0:
        valor_invertido = valor_invertido * 10 + valor % 10
        valor = valor // 10
    return valor_invertido

def verficaInverso(valor1, valor2):
    if valor1 == valor2:
        return True
    else:
        return False
    
n = int(input('Digite um inteiro com 2 ou mais digitos: '))
n_invertido = inverteValor(n)
print(f'O inverso de {n} é {n_invertido}')