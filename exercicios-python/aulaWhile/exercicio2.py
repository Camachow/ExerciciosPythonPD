###Entrada de dados
n = int(input("Digite o número de itereações: "))

###Inicialização das variáveis
cont = 0
soma_sapo, soma_rato, soma_coelho = 0, 0, 0

###Laço
while cont < n:
    qtd, tipo = input("Digite a quantidade e o tipo de animal: ").split()
    qtd = int(qtd)
    if tipo == "S":
        soma_sapo += qtd
    elif tipo == "R":
        soma_rato += qtd
    elif tipo == "C":
        soma_coelho += qtd
    cont += 1
    
###Saída
    print ("Total de cobaias: ", soma_sapo + soma_rato + soma_coelho)
    print ("Total de coelhos: ", soma_coelho)
    print ("Total de ratos: ", soma_rato)
    print ("Total de sapos: ", soma_sapo)


