"""
Exercício Python 096: Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento)
e mostre a área do terreno.
&
Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
"""
def area(lateral1, lateral2):
    area_terreno = lateral1 * lateral2
    print(f'O terreno possui a area:\n'
          f'{lateral1:.2f}m X {lateral2:.2f}m, igual a -> {area_terreno:.2f}m2')


def titulo_programa(escrever):
    tamanho = len(escrever)
    print('~' * tamanho)
    print(escrever)
    print('~' * tamanho)


titulo_programa(' CONTROLE DE TERRENOS ')
largura = float(input('Largura em metros: '))
comprimento = float(input('Comprimento em metros: '))
area(largura, comprimento)
