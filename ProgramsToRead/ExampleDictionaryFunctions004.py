'''
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''
lista_cadastros = list()
lista_mulheres = list()
media_idade_grupo = soma_idade = 0
while True:
    cadastro = {
        'nome': str(input('Nome: ')).strip().capitalize()
    }
    while True:
        cadastro['sexo'] = str(input('Sexo: ')).strip().lower()[0]
        if cadastro['sexo'] not in 'mf':
            print('Erro, favor digitar novamente.\n'
                  'Lembrando: possivel digitar f ou m')
        else:
            break
    cadastro['idade'] = int(input('Idade: '))
    lista_cadastros.append(cadastro)
    soma_idade += cadastro['idade']
    if cadastro['sexo'] == 'f':
        lista_mulheres.append(cadastro['nome'])
    while True:
        continuar = str(input('Deseja continuar? [s/n] ')).strip().lower()[0]
        if continuar not in 'sn':
            print('Erro, digite novamente: ')
        else:
            break
    if continuar == 'n':
        break
print(f'{"Cadastro":-^40}')
print(f'Foram cadastradas {len(lista_cadastros)} pessoas.')
media_idade_grupo = soma_idade / len(lista_cadastros)
print(f'A media de idade do grupo e de {media_idade_grupo} anos.')
print(f'As mulheres do grupo sao: ', end='')
for nome_mulher in lista_mulheres:
    print(nome_mulher, end='; ')
print('\nAcima da idade media temos:')
for pessoas in lista_cadastros:
    if pessoas['idade'] > media_idade_grupo:
        for chave, valor in pessoas.items():
            print(f'  => {chave} = {valor}', end=';')
print('\n < ENCERRANDO... >')
