n1 = float(input("Digite um número: "))
operando = input("Digite o operando desejado: ")
n2 = float(input("Digite outro número: "))

if operando == "+":
    resultado = n1 + n2
    print("O resultado da soma é: ", resultado)
elif operando == "-":
    resultado = n1 - n2
    print("O resultado da subtração é: ", resultado)
elif operando == "*":
    resultado = n1 * n2
    print("O resultado da multiplicação é: ", resultado)
elif operando == "/":
    resultado = n1 / n2
    print("O resultado da divisão é: ", resultado)
else:
    print("Operação inválida!")
    
print(f"{n1} {operando} {n2} = {resultado}")