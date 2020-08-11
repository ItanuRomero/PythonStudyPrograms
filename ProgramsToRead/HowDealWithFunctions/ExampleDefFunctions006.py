"""
Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""
def ficha(nome='Desconhecido', gols='zero'):
    print(f'o jogador {nome} fez {gols} gols.')


nome_jogador = str(input('Nome do jogador: ')).capitalize().strip()
gols_jogador = str(input('Numero de gols: '))
if nome_jogador == '' and gols_jogador == '':
    ficha()
elif nome_jogador == '' and gols_jogador != '':
    ficha(gols=gols_jogador)
elif gols_jogador == '' and nome_jogador != '':
    ficha(nome_jogador)
else:
    ficha(nome_jogador, gols_jogador)