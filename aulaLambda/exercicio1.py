op = int(input("(1) maior ou (2) menor: "))
if op == 1:
    result = float('-inf')
    #Se x > y, retorna True e executará a função lambda
    op_func = lambda x, y: x > y
else:
    result = float('inf')
    #Se x < y, retorna True e executará a função lambda
    op_func = lambda x, y: x < y

while True:
    x = int(input("Digite um número: "))
    if x == 0:
        break
    if op_func(x, result):
        result = x
    print(result)