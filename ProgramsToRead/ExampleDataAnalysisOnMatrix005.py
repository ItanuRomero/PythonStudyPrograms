"""Exercício Python 087: Aprimore o desafio anterior,
(Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e
preencha com valores lidos pelo teclado. No final, mostre a matriz na tela,
com a formatação correta.) mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""
from os import system
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_coluna_3 = maior_valor_linha2 = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Insira o valor [{linha}, {coluna}]: '))
system('clear')
print(f'{"MATRIZ":-^25}')
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
        if coluna == 2:
            soma_coluna_3 += matriz[linha][coluna]
        if linha == 1:
            if coluna == 0:
                maior_valor_linha2 = matriz[linha][coluna]
            elif matriz[linha][coluna] > maior_valor_linha2:
                maior_valor_linha2 = matriz[linha][coluna]
    print()
print('-=' * 15)
print(f'A soma de todos os valores pares: {soma_pares}\n'
      f'A soma dos valores da terceira coluna: {soma_coluna_3}\n'
      f'O maior valor da segunda linha: {maior_valor_linha2}')
