"""
Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""
from random import randint
numeros = list()


def preenche_lista():
    print('Sera adicionado a lista: ', end='')
    for contador in range(0, 5):
        numeros.append(randint(1, 10))
        print(numeros[contador], end=' ')
    print()


def soma_pares(lista):
    resultado_soma = 0
    for valor in lista:
        if valor % 2 == 0:
            resultado_soma += valor
    print(f'A soma dos pares em {lista} e igual a : {resultado_soma}')


# MainProgram
preenche_lista()
soma_pares(numeros)