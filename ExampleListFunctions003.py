lista_geral = list()
aluno_e_media = list()
notas = list()
while True:
    aluno_e_media.append(str(input('Nome aluno: ')))
    for cont in range(1, 3):
        notas.append(float(input(f'nota {cont}: ')))
    media = (notas[0] + notas[1]) / 2
    aluno_e_media.append(notas[:])
    aluno_e_media.append(media)
    resposta = str(input('Mais algum? [s/n] ')).lower().strip()[0]
    lista_geral.append(aluno_e_media[:])
    if resposta == 'n':
        break
    aluno_e_media.clear()
    notas.clear()
print('-=' * 30)
print(f'    BOLETIM:    ')
print(f'{"No.":^3} {"aluno":>10} {"media":>10}')
for valor, l in enumerate(lista_geral):
    print(f'{valor:^3}'
          f'{lista_geral[valor][0]:>10}'
          f'{lista_geral[valor][2]:>10}')
print('-=' * 30)
while True:
    mostrar_notas = int(input('insira o numero do aluno para ver notas '
                              '(999 para parar) '))
    print('-' * 40)
    if mostrar_notas == 999:
        break
    for nota_aluno in range(0, 2):
        print(f'nota 1: {lista_geral[mostrar_notas][1][nota_aluno]}')
