"""
Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""
from os import system
from time import sleep


def progressao(inicio, fim, passo):
    print(f'Calculando a  progressao de {inicio} ate {fim} de {passo} em {passo}')
    if inicio < fim and passo != 0:
        passo = abs(passo)
        for cont in range(inicio, fim + 1, passo):
            print(cont, end=' ')
            sleep(0.5)
        print()
    elif passo == 0 or passo == -1:
        for cont in range(inicio, fim + 1, 1):
            print(cont, end=' ')
            sleep(0.5)
        print()
    elif inicio > fim:
        if passo >= 1:
            passo = passo * -1
            for cont in range(inicio, fim - 1, passo):
                print(cont, end=' ')
                sleep(0.5)
            print()
        else:
            for cont in range(inicio, fim - 1, passo):
                print(cont, end=' ')
                sleep(0.5)
            print()
    else:
        print('Erro, favor tente novamente.')


def limpatela():
    system('clear')


def linha():
    print('-~' * 40)


# MainProgram
limpatela()
sleep(3)
progressao(0, 10 1)
sleep(1)
linha()
progressao(10, 0 2)
sleep(1)
linha()
comeca = int(input('Digite o inicio: '))
termina = int(input('Digite o fim:  '))
razao = int(input('Digite a razao: '))
progressao(comeca, termina, razao)
linha()
