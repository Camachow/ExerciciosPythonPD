juros = 1.01
saldo = 500
print("Saldo inicial: ", saldo)
print(type(saldo)) #int

saldo = saldo * juros #rendimento1
print("Saldo após 1º mês: ", saldo)

saldo = saldo * juros #rendimento2
print("Saldo após 2º mês: ", saldo)

saldo = saldo * juros #rendimento3
print("Saldo após 3º mês: ", saldo)

print(type(saldo)) #float
