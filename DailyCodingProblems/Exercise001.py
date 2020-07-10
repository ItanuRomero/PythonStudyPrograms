'''
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''
from os import system
lista_entregue = list()
number_key = int(input('insira o valor k: '))
while True:
    lista_entregue.append(int(input('insira um valor da lista: ')))
    resposta = str(input('mais valores? ')).strip().lower()[0]
    if resposta == 'n':
        break
system('clear')
lista_copia = lista_entregue[:]
is_key_on_list = False
for valor in lista_entregue:
    for valor2 in lista_copia:
        if valor + valor2 == number_key:
            print(f'Encontrei, os valores {valor} e '
                  f'{valor2} somados dao: {number_key}')
            is_key_on_list = True
    if is_key_on_list:
        break
if is_key_on_list is not True:
    print(f'nao encontrei nenhum valor na lista, que somado de {number_key}')
