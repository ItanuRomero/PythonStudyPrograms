"""
Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""


def fatorial(numero, show=False):
    """
    Funcao que recebe um numero e devolve seu fatorial.
    :param numero: numero a se calcular.
    :param show: (opcional) mostrar o calculo.
    :return: resultado do calculo fatorial.
    """
    fatorial = 1
    for counter in range(numero, 0, -1):
        fatorial *= counter
        if show:
            if counter > 1:
                print(counter, end=' x ')
            else:
                print(counter, end=' = ')
    return fatorial


# MainProgram
print(f'{"CALCULO DE FATORIAL":-^40}')
numero_fatorial = int(input('Digite um numero: '))
while True:
    mostrar = str(input('Deseja mostrar? [s/n] ')).strip().upper()[0]
    if mostrar in 'SN':
        break
    print('ERRO, DIGITE NOVAMENTE.')
if mostrar == 'S':
    mostrar = True
else:
    mostrar = False
print('CALCULANDO...')
print(fatorial(numero_fatorial, mostrar))
