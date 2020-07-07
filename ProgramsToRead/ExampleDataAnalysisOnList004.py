'''
Proposta:
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
lista_pessoas = list()
nome_peso = list()
mais_pesadas = list()
mais_leves = list()
quantidade_total_pessoas = 0
while True:
    nome_peso.append(str(input('Nome: ')).strip())
    nome_peso.append(float(input('Peso: ')))
    if quantidade_total_pessoas == 0:
        mais_leves.append(nome_peso[:])
        mais_pesadas.append(nome_peso[:])
    else:
        if nome_peso[1] < mais_leves[0][1]:
            mais_leves.clear()
            mais_leves.append(nome_peso[:])
        elif nome_peso == mais_leves[0][1]:
            mais_leves.append(nome_peso[:])
        if nome_peso[1] > mais_pesadas[0][1]:
            mais_pesadas.clear()
            mais_pesadas.append(nome_peso[:])
        elif nome_peso[1] == mais_pesadas[0][1]:
            mais_pesadas.append(nome_peso[:])
    lista_pessoas.append(nome_peso[:])
    quantidade_total_pessoas += 1
    nome_peso.clear()
    resposta = str(input('Deseja continuar? [s/n] ')).lower().strip()[0]
    if resposta == 'n':
        break
print('{:-^40}'.format('Todas as Pessoas'))
for pessoas in lista_pessoas:
    print(f'Temos o/a {pessoas[0]} com o peso de {pessoas[1]:.2f}Kg')
print('{:-^40}'.format('MAIS LEVES'))
for pessoas_leves in mais_leves:
    print(f'Temos a {pessoas_leves[0]} com {pessoas_leves[1]:.2f}Kg')
print('{:-^40}'.format('MAIS PESADAS'))
for pessoas_pesadas in mais_pesadas:
    print(f'Temos a {pessoas_pesadas[0]} com {pessoas_pesadas[1]:.2f}Kg')
print(f'A quantidade total de pessoas foi de: {quantidade_total_pessoas}')
