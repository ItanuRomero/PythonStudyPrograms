'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
jogador = dict()
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
print(f'{"FICHA":-^40}')
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
numero_partida = 1
for valor in jogador['gol por partida']:
    print(f'  => Na partida {numero_partida}, fez {valor} gols.')
    numero_partida += 1
print(f'Foi um total de {jogador["total de gols"]} gols.\n'
      f'E um aproveitamento de {jogador["aproveitamento"]}.')
