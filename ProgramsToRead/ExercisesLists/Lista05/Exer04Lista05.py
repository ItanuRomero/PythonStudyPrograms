# Questão 4. Elabore um programa que utilize uma função que necessite de um 
# argumento. A função retorna o valor de caractere ‘P’, se seu argumento 
# for positivo, e ‘N’, se seu argumento for zero ou negativo.

def verifica(num):
    if num > 0:
        print('P')
    else:
        print('N')
num = int(input('Digite um número: '))
verifica(num)
