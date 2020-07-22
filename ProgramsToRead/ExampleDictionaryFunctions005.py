"""
Exercício Python 095: Aprimore o desafio 93 (https://github.com/ItanuRomero/PythonStudyPrograms/blob/master/ProgramsToRead/ExampleDictionaryFunctions003.py) para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""
jogador = dict()
lista_jogadores = list()
while True:
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
    jogador['partidas'] = int(input('Quantidade de partidas: '))
    jogador['gol por partida'] = list()
    for contador in range(1, jogador['partidas'] + 1):
        gol_partida = int(input(f'Quantos gols na partida {contador}: '))
        jogador['gol por partida'].append(gol_partida)
        if contador == 1:
            jogador['total de gols'] = gol_partida
        else:
            jogador['total de gols'] += gol_partida
        jogador['aproveitamento'] = jogador['total de gols'] / jogador['partidas']
    lista_jogadores.append(jogador.copy())
    while True:
        resposta = str(input('Continuar? [s/n] ')).strip().lower()[0]
        if resposta in 'sn':
            break
        print('ERRO, digite novamente: ')
    if resposta == 'n':
        break
print(f'{"FICHAS":-^40}')
print(f'{"No. "}{"NOME":<10}{"PARTIDAS":>10}{"TOTAL DE GOLS":>15}')
for index, dicionario in enumerate(lista_jogadores):
    print(f'{index:^4}{dicionario["nome"]:<10}{dicionario["partidas"]:>10}'
          f'{dicionario["total de gols"]:>15}')
print(f'{" MAIS DETALHES ":=^40}')
while True:
    while True:
        busca_aproveitamento = int(input('Digite o numero do jogador: '))
        if busca_aproveitamento <= len(lista_jogadores) or busca_aproveitamento == 999:
            break
        print('Nao encontramos o jogador desse numero, digite novamente.\n'
              '(digite 999 para parar)')
    if busca_aproveitamento == 999:
        break
    print('Aqui esta:')
    for jogo, gols in enumerate(lista_jogadores[busca_aproveitamento]['gol por partida']):
        print(f'No jogo {jogo + 1}, '
              f'{lista_jogadores[busca_aproveitamento]["nome"]} fez {gols} gols.')
    print()
print(f'\n{"ENCERRANDO":-^40}')
