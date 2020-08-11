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
