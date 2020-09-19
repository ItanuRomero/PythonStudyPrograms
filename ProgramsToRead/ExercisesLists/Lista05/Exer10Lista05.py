# Questão 10. Faça um programa de implemente um jogo de Craps. O jogador 
# lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira 
# jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você 
# tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. 
# Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10, este é seu "Ponto". 
# Seu objetivo agora é continuar jogando os dados até tirar este número novamente. 
# Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

import random
def lancar_dados():
    return random.randint(2, 12)


jogada = 0
ponto = 0

while True:
    jogada += 1

    if jogada>1:
        print('O valor do ponto é {ponto}')
    valor = lancar_dados()
    print("O valor do dado é",valor)
    if jogada == 1:
        if valor == 7 or valor == 11:
            print('Tirou um natural, ganhou!')
            exit()
        elif valor == 2 or valor == 3 or valor == 12:
            print('Tirou um Craps, perdeu!')
            exit()
        else:
            ponto = valor
    else:
        if valor == 7:
            print('Tirou um 7 antes, perdeu!')
            exit()
        elif ponto == valor:
            print('Tirou seu ponto, ganhou!')
            exit()
