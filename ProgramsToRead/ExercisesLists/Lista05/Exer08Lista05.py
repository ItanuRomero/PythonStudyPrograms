# Questão 8. Elabore um programa que utilize uma função que informe a 
# quantidade de dígitos de um determinado número inteiro informado.

def quantidadeDigito(numero):
    print(len(str(numero)))
num = int(input('Digite um número: '))
quantidadeDigito(num)