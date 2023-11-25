#Leitura de Dados (entrada)
valorFaltaPagar = int(input("Digite o valor que falta pagar: "))

#Processamento (transformação)
### Começar da maior nota (quantas notas de 100?)
notasDe100 = valorFaltaPagar // 100 #Divisão inteira => int(valorFaltaPagar / 100)

### Atualizar o valor que falta pagar
valorFaltaPagar = valorFaltaPagar % 100 #Resto da divisão => valorFaltaPagar - (notasDe100 * 100)

### Quantas notas de 50?
notasDe50 = valorFaltaPagar // 50

### Atualizar o valor que falta pagar
valorFaltaPagar = valorFaltaPagar % 50

### Quantas notas de 20?
notasDe20 = valorFaltaPagar // 20

### Atualizar o valor que falta pagar
valorFaltaPagar = valorFaltaPagar % 20

### Quantas notas de 10?
notasDe10 = valorFaltaPagar // 10

### Atualizar o valor que falta pagar
valorFaltaPagar = valorFaltaPagar % 10

### Quantas notas de 5?
notasDe5 = valorFaltaPagar // 5

### Atualizar o valor que falta pagar
valorFaltaPagar = valorFaltaPagar % 5

### Quantas notas de 2?
notasDe2 = valorFaltaPagar // 2

### Atualizar o valor que falta pagar
valorFaltaPagar = valorFaltaPagar % 2

### Quantas notas de 1?
notasDe1 = valorFaltaPagar

### Atualizar o valor que falta pagar
valorFaltaPagar = valorFaltaPagar % 1

#Saída
print(f"Notas de 100: {notasDe100}")
print(f"Notas de 50: {notasDe50}")
print(f"Notas de 20: {notasDe20}")
print(f"Notas de 10: {notasDe10}")
print(f"Notas de 5: {notasDe5}")
print(f"Notas de 2: {notasDe2}")
print(f"Notas de 1: {notasDe1}")
print(f"Valor que falta pagar: {valorFaltaPagar}")
