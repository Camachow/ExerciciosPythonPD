""" Faça um programa para ler as dimensões de um terreno em valores inteiros 
(comprimento e largura), bem como o preço do metro quadrado da região em 
ponto flutuante. Calcule o valor do terreno e imprima o resultado como
mostra o exemplo a seguir. 
O terreno possui 250m² e o metro quadrado custa R$ 512,490.50.
Comente na linha acima de cada instrução uma breve descrição do que ela faz."""

#Faz a letura do comprimento do terreno
comprimento = int(input("Digite o comprimento do terreno: "))
#Faz a leitura da largura do terreno    
largura = int(input("Digite a largura do terreno: "))
#Faz a leitura do preço do metro quadrado
preco = float(input("Digite o preço do metro quadrado: "))
#Calcula a área do terreno
area = comprimento * largura
#Calcula o valor do terreno
valor = area * preco
#Imprime o valor do terreno
print(f"O terreno possui {area}m² e o metro quadrado custa R$ {preco:250.2f}.")
print(f"O valor do terreno é R$ {valor:,.2f}.")