n = int(input("Digite o número de itereações: "))

soma_vitorias, soma_empates, soma_derrotas = 0, 0, 0

for jogo in range(n):
    gols_galo = int(input(f"Digite o número de gols do Galo no jogo {jogo}: "))
    gols_op = int(input(f"Digite o número de gols do oponente no jogo {jogo}: "))

    if gols_galo > gols_op:
        soma_vitorias += 1
    elif gols_galo == gols_op:
        soma_empates += 1
    else:
        soma_derrotas += 1

print("O Galo teve", soma_vitorias, "vitórias,", soma_empates, "empates e", soma_derrotas, "derrotas.")
print("O Galo teve um aproveitamento de", soma_vitorias/n*100, "%.")
print("Pontuação final:", soma_vitorias*3 + soma_empates, "pontos.")