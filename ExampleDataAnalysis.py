#program for analysis on data from keyboard input.
from os import system
acumulador_idade = 0
nome_homem_mais_velho = ''
idade_homem = 0
mulheres_acima_20 = 0
for pessoas in range(1, 5):
    nome = str(input(f'Qual o nome da {pessoas} pessoa? ')).capitalize()
    idade = int(input('E a idade dele/a? '))
    sexo = str(input('Qual o sexo? m/f')).lower().strip()
    acumulador_idade += idade
    if sexo == 'm':
        if idade > idade_homem or idade_homem == 0:
            idade_homem = idade
            nome_homem_mais_velho = nome
    if sexo == 'f':
        if idade < 20:
            mulheres_acima_20 += 1
    system('clear')
media_idade = acumulador_idade / 4
print(f'Media de idade do grupo: {media_idade}\n'
      f'Nome do homem mais velho: {nome_homem_mais_velho}\n'
      f'Numero de mulheres acima dos 20 anos: {mulheres_acima_20}')
'''

'''from os import system
system('clear')
total_maiores_18 = total_homens = total_mulheres = 0
while True:
    sexo = resposta = ' '
    print('~' * 10,
          'CADASTRO',
          '~' * 10)
    idade = int(input('DIgite a idade: '))
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        total_maiores_18 += 1
    if sexo == 'M':
        total_homens += 1
    if sexo == 'F' and idade < 20:
        total_mulheres += 1
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
system('clear')
print(f'==FIM PROGRAMA==\n'
      f'Foram cadastradas: \n{total_maiores_18} pessoas maiores de idade\n'
      f'{total_homens} Homens\n'
      f'{total_mulheres} Mulheres abaixo de 20 anos\n'
      f'Obrigado por utilizar este programa!')