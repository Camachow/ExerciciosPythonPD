n1, n2 = int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: "))
if (n1+n2) % 2 == 0:
    print(f"A soma de {n1} e {n2} é par.")
else:
    print(f"A soma de {n1} e {n2} é ímpar.")

### print(f"A soma de {n1} e {n2} é {'par' if (n1+n2) % 2 == 0 else 'ímpar'}."