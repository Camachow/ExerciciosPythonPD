n = int(input("Digite o número de itereações: "))

###Inicialização das variáveis
soma = 0 # resultado da soma
cont = 0 # Variavel de controle do laço

###Laço
while cont < n:
    idade = int(input("Digite a idade: "))
    soma += idade
    cont = cont + 1

###Saída
print ("A média das idades é: ", soma/n)
