a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
delta = b**2 - 4*a*c
if delta < 0:
    print("Não existem raízes reais.")
elif delta == 0:
    raiz = -b / (2*a)
    print(f"Existe uma raiz real: {raiz:.2f}")
else:
    raiz1 = (-b + delta**(1/2)) / (2*a)
    raiz2 = (-b - delta**(1/2)) / (2*a)
    print(f"Existem duas raízes reais: {raiz1:.2f} e {raiz2:.2f}")