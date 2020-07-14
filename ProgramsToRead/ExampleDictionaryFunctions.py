'''Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
from random import randint
from time import sleep
from os import system
system('clear')
ranking = 0
dados = {
    'jogador 1': randint(1, 6),
    'jogador 2': randint(1, 6),
    'jogador 3': randint(1, 6),
    'jogador 4': randint(1, 6)
}
print(f'{"JOGANDO OS DADOS":*^30}')
sleep(1)
for key, value in dados.items():
    print(f'O dado do {key} deu: {value}.')
    sleep(1)
print(f'\n{"RESULTADO EM ORDEM":-^30}')
sleep(1)
for item in sorted(dados, key=dados.get, reverse=True):
    ranking += 1
    print(f' - {ranking}o. Lugar: o {item} que tirou {dados[item]}.')
    sleep(1)
