produto = 1

while True:
    i = int(input("Digite um numero: "))
    if i == 0: break # Sai do loop

    if i < 0: continue # Pula para a proxima iteracao
    
    produto *= i

print(f"O produto dos numeros positivos digitados foi {produto}")